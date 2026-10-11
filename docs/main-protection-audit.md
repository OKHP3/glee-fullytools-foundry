# Main protection audit

The scheduled Monday and manual `Main protection audit` workflow reads the live
GitHub settings for `OKHP3/glee-fullytools-foundry` on `main`. Repository identity
accepts case-only differences in the complete owner/name, not a different owner,
repository or default branch. It fails if the classic branch rule no longer
requires pull requests with exactly zero approvals under the documented
solo-owner policy, stops dismissing stale reviews, loses the `Validate manifest`
check or its up-to-date requirement,
stops enforcing admins, or permits force pushes or deletion. It also checks
that the `github-pages` environment retains deployment branch restrictions and
that a custom branch policy, when used, permits `main`. An unreadable API
response fails the job as **incomplete**, not as a pass. No settings are changed.

**Activation:** This workflow runs after it is merged into the default branch.
The built-in `GITHUB_TOKEN` is tried, but it may not have permission to read
branch protection. If the job reports HTTP 403, report it as incomplete and leave
credential changes to a separately authorized owner action. The optional
repository Actions secret `REPO_SETTINGS_READ_TOKEN` would need a fine-grained,
repository-scoped credential with **Administration: read** permission (and
Metadata: read access). Do not paste tokens into code, logs, or issue comments.
The secret is available only to the scheduled/manual job, never to PR code.
The separate PR job runs offline tests without an audit credential.

The settings receipt in `docs/repo-settings-review/protection-receipt.json`
records **zero** required approvals, and [the solo-owner recap](repo-settings-recap.md)
explains the owner's decision. The October 11, 2026 authorized checker repair
reverses the audit's conflicting one-approval expectation, not the live rule.
Zero approvals still requires the pull-request rule, stale-review dismissal,
required CI and all other controls listed above. No settings, secrets, tokens
or workflow permissions are changed. Failures appear in GitHub Actions and are
subject to the repository owner's Actions notification preferences. Any missing
read privilege is an owner access decision, not permission to bypass the check.
After merge and owner review, a separately authorized `workflow_dispatch` can
verify the scheduled credential's live read access.

This is a periodic check of the classic branch rule and one deployment
environment, not a complete audit of inherited rulesets or all environments.
It does not attest to delivery of email notifications. If `main` is renamed
or the required check/environment changes intentionally, update the checker
and its tests together.
