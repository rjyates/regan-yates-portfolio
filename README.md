# Regan Yates Portfolio

A standalone professional portfolio focused on technology leadership, systems architecture, automation, and business transformation. The visual foundation is Regan's supplied Stitch export.

## Pages

- `/`: selected professional work, personal projects, leadership direction, experience, and contact.
- `/links/`: mobile-first networking page.
- `/resume/`: readable professional background and résumé summary.

Only `dist/` is published. The baseline, assignment documentation, and original Stitch export are outside the public site. Hosting and version history are dedicated to this portfolio and separate from assistant projects. No assistant services, credentials, or integrations are connected.

## Source and editing

- `scripts/build.py` generates the HTML from resume-backed content and the supplied Stitch document's font definitions.
- `dist/stitch.css` contains static equivalents of the Stitch utility classes used by these pages.
- `dist/refinements.css` adapts the layout for mobile and adds working navigation and networking-page styles.
- `dist/site.js` implements the mobile menu and project filters.
- `references/stitch/` preserves the original exported HTML, design specification, and screenshot.
- `baseline/` preserves the initial comparison artifact.
- `process/` records decisions and remaining class requirements.

Run `python scripts/build.py` after content edits. The builder uses `lxml`. Serve `dist/` with any static HTTP server; for example `python -m http.server 4321 --directory dist`. Styles use Google Fonts with local serif/sans-serif fallbacks. The production page does not need the Tailwind browser runtime or a JavaScript framework.

## Content integrity

OneGauge is ongoing development. The Temporary Access Pass work is a proposal presented to the CIO. Organizational scale figures describe the supported organization, not independently measured individual outcomes. Luther is a built research tool; Vera remains in design/development. Index is omitted pending a substantive description. The Stitch example persona, financial results, executive level, compliance claims, and invented architecture records are not part of the portfolio.

## Verification

Checked internal routes, assets and anchors; one primary heading per page; JavaScript syntax; desktop and mobile layouts; filter behavior; mobile menu and link destinations. See the process record for specifics and remaining submission work.
