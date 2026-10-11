#!/usr/bin/env python3
"""Read-only drift check for this repository's main branch and deployment gate."""

import json
import os
import sys
from fnmatch import fnmatchcase
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPOSITORY = "OKHP3/glee-fullytools-foundry"
BRANCH = "main"
REQUIRED_CHECK = "Validate manifest"
DEPLOYMENT_ENVIRONMENT = "github-pages"


def fetch(path, token):
    request = Request(
        "https://api.github.com" + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + token,
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "foundry-protection-audit",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            return json.load(response)
    except HTTPError as exc:
        # Never print the response body, headers, request or token.
        raise RuntimeError(f"GitHub returned HTTP {exc.code} for {path}") from None
    except (URLError, TimeoutError, ValueError) as exc:
        raise RuntimeError(f"Could not read GitHub settings at {path}: {type(exc).__name__}") from None


def check(protection, environment, deployment_branches=None):
    issues = []
    reviews = protection.get("required_pull_request_reviews")
    if not isinstance(reviews, dict):
        issues.append("main must require pull request reviews")
    else:
        count = reviews.get("required_approving_review_count")
        if type(count) is not int or count != 0:
            issues.append("main must require zero approving reviews under the solo-owner policy")
        if reviews.get("dismiss_stale_reviews") is not True:
            issues.append("main must dismiss stale reviews")

    checks = protection.get("required_status_checks")
    contexts = checks.get("contexts") if isinstance(checks, dict) else None
    if not isinstance(contexts, list) or REQUIRED_CHECK not in contexts:
        issues.append(f"main must require the {REQUIRED_CHECK} status check")
    if not isinstance(checks, dict) or checks.get("strict") is not True:
        issues.append("main must require up-to-date status checks")

    for field, expected in (
        ("enforce_admins", True),
        ("allow_force_pushes", False),
        ("allow_deletions", False),
    ):
        value = protection.get(field)
        if not isinstance(value, dict) or value.get("enabled") is not expected:
            issues.append(f"main {field} must be {str(expected).lower()}")

    if not isinstance(environment, dict) or environment.get("name") != DEPLOYMENT_ENVIRONMENT:
        issues.append(f"{DEPLOYMENT_ENVIRONMENT} deployment environment must exist")
    else:
        policy = environment.get("deployment_branch_policy")
        if not isinstance(policy, dict) or not (
            policy.get("protected_branches") is True
            or policy.get("custom_branch_policies") is True
        ):
            issues.append(f"{DEPLOYMENT_ENVIRONMENT} must restrict deployment branches")
        elif policy.get("custom_branch_policies") is True:
            if not isinstance(deployment_branches, list) or not any(
                isinstance(branch, dict)
                and isinstance(branch.get("name"), str)
                and fnmatchcase(BRANCH, branch["name"])
                for branch in deployment_branches
            ):
                issues.append(f"{DEPLOYMENT_ENVIRONMENT} must permit main through its deployment branch policy")
    return issues


def main():
    token = os.environ.get("REPO_SETTINGS_READ_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Protection audit incomplete: set REPO_SETTINGS_READ_TOKEN with repository Administration read access.")
        return 2
    base = "/repos/" + REPOSITORY
    try:
        repo = fetch(base, token)
        full_name = repo.get("full_name")
        # GitHub owner/repository names are case-insensitive. Compare the full
        # pinned target, without accepting a different owner, rename or branch.
        if (
            not isinstance(full_name, str)
            or full_name.lower() != REPOSITORY.lower()
            or repo.get("default_branch") != BRANCH
        ):
            raise RuntimeError("Repository identity or default branch did not match the audit target")
        protection = fetch(base + "/branches/" + BRANCH + "/protection", token)
        environments = fetch(base + "/environments?per_page=100", token)
        if not isinstance(environments.get("environments"), list) or environments.get("total_count", 0) > 100:
            raise RuntimeError("Could not inspect the complete environment list")
        matches = [item for item in environments["environments"] if item.get("name") == DEPLOYMENT_ENVIRONMENT]
        environment = fetch(
            base + "/environments/" + quote(DEPLOYMENT_ENVIRONMENT, safe=""), token
        ) if matches else None
        deployment_branches = None
        if environment and (environment.get("deployment_branch_policy") or {}).get("custom_branch_policies") is True:
            policies = fetch(
                base + "/environments/" + quote(DEPLOYMENT_ENVIRONMENT, safe="")
                + "/deployment-branch-policies?per_page=100",
                token,
            )
            deployment_branches = policies.get("branch_policies")
            if not isinstance(deployment_branches, list) or policies.get("total_count", 0) > 100:
                raise RuntimeError("Could not inspect the complete deployment branch policy list")
        issues = check(protection, environment, deployment_branches)
    except (RuntimeError, AttributeError, TypeError) as exc:
        print(f"Protection audit incomplete: {exc}")
        return 2

    for issue in issues:
        print(f"Protection drift: {issue}")
    if issues:
        return 1
    print("Main protection audit passed (classic branch rule and github-pages deployment branch policy).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
