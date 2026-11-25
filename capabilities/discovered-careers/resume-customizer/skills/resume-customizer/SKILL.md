---
name: resume-customizer
description: >-
  Tailor an existing resume to a specific job posting. Map each important requirement to evidence, revise the most relevant sections and preserve a traceable role-specific version.
license: MIT
metadata:
  version: "0.2.0"
---

# Resume Customizer

## Scope

Request the base resume and vacancy text or excerpts. If only one is available, extract supported achievements from the resume or requirements from the posting and identify what is needed to match them. Keep the original available.

## Workflow

1. Separate essential duties, explicit qualifications and preferences. Select the few requirements most relevant to the work. Record the posting's wording only where a reader would benefit from the employer's terminology.
2. For each priority requirement, mark direct evidence, transferable evidence or a gap. Attach the exact fact, project or bullet that supports the match. A similar platform can support transferability but cannot establish hands-on use of the named platform.
3. Reorder and rewrite the summary, skills and strongest experience bullets around the supported matches. Preserve official titles, employers, dates and credential status. Keep unrelated chronology concise. Avoid keyword lists that imply unsupplied qualifications.
4. Return the targeted version, a short change log and any gaps the person could clarify. Label the version with the target employer and role when supplied. If two postings are requested, build separate variants from the same base. Output copy-ready text unless verified file export is available.

## Build the application copy

Start a small match table with one row per requested qualification. Use the columns **Posting requirement**, **Resume evidence**, **Match** and **Editing decision**. In the decision, name the summary line or experience entry to change. Put an unsupported requirement in the gap notes outside the resume. A job posting describes the employer's needs. It supplies no evidence about the applicant.

Give the user the edited sections themselves. Begin the summary with the applicant's actual area of work and lead the experience section with the strongest relevant example. Use the posting's term when it accurately names the same work. If the user supplied only excerpts, deliver a replacement for those excerpts and keep their role heading. When the user supplies a full resume, return a complete draft if requested, including the chronology and qualifications they supplied. Keep editing notes and unresolved gaps outside copy-ready text.

For example, a candidate who wrote recovery steps for a volunteer help desk can describe documenting recovery procedures. A listing that also asks for incident command leaves a separate gap. Only identify the candidate as incident commander when supplied evidence establishes that responsibility.

## Revise and identify the version

Use the employer and role as the draft label, then distinguish revisions within that target with a simple number. When the user corrects a figure or ownership, apply it to the summary, bullets, skills and match table wherever it occurs. Read the whole copy for remnants of the earlier claim. Return the revised copy plus a short statement of what changed. A second employer receives a separate variant so an edit made for one role cannot silently carry into another. A version label helps the user save a draft even when the conversation has no file storage.

## Verify the result

Compare the final version with both documents. Every major rewrite should answer a real posting requirement and still be true if the employer asks for a concrete example.

## Sources and limits

The source reference lists vocabulary and tone examples. Treat them as editing aids. Employer screening scores, private applicant-tracking behavior and placement outcomes are unverified.

When included in the package, use `resume-keywords-by-industry.csv` to look up a sector's vocabulary and `resume-tone-examples.md` to choose a writing register. Label a vocabulary suggestion separately until the candidate supplies supporting evidence. If a reference is unavailable, work from the supplied documents and identify any requested lookup you could not verify.

Repository records

- `capabilities/discovered-careers/resume-customizer/source/references/resume-keywords-by-industry.csv`
- `capabilities/discovered-careers/resume-customizer/source/references/resume-tone-examples.md`
