# Portfolio iteration using Stitch

## Inputs and sequence

1. User supplied Regan_Yates_Resume_Rebuilt_With_Links.docx.
2. An initial resume-only content baseline was saved. See baseline-record.md for its context limitations.
3. User clarified career goals: near-term management, architecture, platform/automation, and transformation opportunities; IT Director/Director of Technology as the next major target; CTO long term.
4. Codex began a technical portfolio draft. The unreviewed pre-Stitch HTML was preserved in pre-stitch-draft.html as a process record, not a standalone finished prototype.
5. User supplied stitch_ai_assisted_personal_portfolio.zip and explicitly selected that front end. The exported code.html, screen.png, and DESIGN.md are preserved under references/stitch/.
6. Codex adapted the selected Stitch design to the actual resume and career goals, then implemented navigation, project filters, a mobile links page, and a background/résumé page.

## Design decisions

- Preserve the warm paper surfaces, Newsreader serif headings, Inter body copy, JetBrains Mono metadata, bronze accent, square corners, and structured case-study layout from Stitch.
- Retain its two-column narrative/technical-board composition and responsibility matrix treatment.
- Make the main page personal and professionally accurate rather than retaining the example executive persona.
- Replace invented financial services and healthcare results with OneGauge product development and the onboarding proposal.
- Replace the sample deployed infrastructure diagram with a clearly labeled conceptual product progression.
- Use organizational context and actual responsibilities where measured business outcomes are unavailable.
- Keep the baseline and assignment materials outside the published directory.
- Implement the exported utility styling as static CSS, removing the development-only Tailwind CDN runtime.
- Use the same visual system on the mobile networking page.

## Content still worth enriching

- OneGauge: approved screenshots, release status, architecture details, and outcomes when available.
- Onboarding proposal: adoption status, implementation steps, and measured improvements if implemented.
- Luther and Vera: approved screenshots, project-specific repository/demo links, technology choices, and limitations.
- Index: substantive description; the resume currently contains a placeholder.
- The leadership philosophy line is proposed portfolio copy, not a quote from the source resume.

## Actual AI evidence and limits

Two tools are represented: the user's supplied Stitch design and this Codex implementation. The Stitch prompt, model identity, and generation history were not supplied. Do not claim a controlled same-prompt comparison has been completed. Preserve the user's actual Stitch prompt and run the same prompt through another tool/model to complete that assignment activity.

## Validation

- Verified all internal navigation destinations and referenced local assets across `/`, `/links/`, and `/resume/`.
- Confirmed one H1 per page and removal of sample identity, L8, HIPAA, fictional dollar outcomes, and placeholder text from published HTML.
- Checked JavaScript syntax.
- Visually inspected desktop layout at 1440 × 1000 and mobile at 390 × 844.
- Confirmed the IT Operations filter selects only the onboarding case study and updates its accessible result count.
- Confirmed the mobile menu expands, and the Quick Links entry opens the dedicated mobile page.
- Confirmed mobile page links match the supplied email, LinkedIn, and GitHub destinations.

## Remaining class deliverables

- Actual same-prompt comparison evidence and the original Stitch prompt.
- Student review/feedback on the refined design and any subsequent iteration screenshots.
- GitHub backup: authentication verified successfully with network access. A dedicated private repository is being created for this portfolio.
- Final audience/access setting for sharing the site with instructors and employers.
- Student's 5–10 minute Loom video and personal reflection.
- Notion submission page and Blackboard submission.

This document records the process; it does not invent the student's personal reflection or claim unperformed work.

## September 22 content refinement

At Regan's request, removed the onboarding improvement proposal from the published portfolio. Featured work now includes OneGauge, Luther, and Vera only. Removed the IT Operations filter, updated the project count to three, and renumbered projects. Employment history remains in the experience and resume sections. Earlier process records and the baseline are preserved as historical class artifacts outside the public site.

## High-level overview refinement

Regan requested a site about their work and direction rather than another resume. Replaced the homepage chronology, skills list, education list, detailed OneGauge case study, and project filters with a personal introduction, three focus areas, short project summaries, approach, and career direction. Retained detailed background on /resume/. Preserved the Stitch typography, colors, and editorial style.

## Supplied PDF resume

Added Regan_Yates_Resume.pdf exactly as supplied, with downloads on the resume and quick-links pages. Regan explicitly chose to keep the onboarding proposal in this PDF only; the homepage still excludes it. The LinkedIn hyperlink in the PDF points to the existing profile, despite its shortened display label.

## Career direction language and LinkedIn

Removed specific target job titles from the direction section at Regan's request. Now describes technology leadership and management, with cybersecurity, systems architecture, automation, and business transformation as interests. Verified the supplied LinkedIn profile matches the existing canonical profile links in the footer and mobile quick-links page; omitted tracking query parameters.
