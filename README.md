<p align="center"><img src="docs/assets/banner.svg" alt="Professional Portfolio — Connecting technical work with a broader direction." width="100%"></p>

[Regan Yates](https://github.com/rjyates) · [Homelab](https://github.com/rjyates/homelab)


# Regan Yates — professional portfolio

**[Visit the portfolio](https://regan-yates-portfolio.reyyates.chatgpt.site/)** · [Background & résumé](https://regan-yates-portfolio.reyyates.chatgpt.site/resume/)

A static portfolio and mobile networking site presenting my technical background, selected projects, and developing direction in technology leadership. It connects experience with interests in systems architecture, automation, and business problem-solving.

## Pages

| Route | Purpose |
| :--- | :--- |
| `/` | Introduction, selected work, approach, experience, and contact |
| `/links/` | Compact mobile networking page |
| `/resume/` | Readable professional background |

## Local preview

The generated site is already in `dist/`. From the repository root:

```text
python -m http.server 4321 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:4321`. The browser site requires no JavaScript framework or application database. Google Fonts are external dependencies, with local fallback fonts.

## Editing and rebuilding

The builder requires Python and `lxml` in your chosen environment:

```text
python -m pip install lxml
python scripts/build.py
```

Edit source content in `scripts/`, then rebuild rather than treating generated HTML as the only source. Publish **only `dist/`** after reviewing its contents.

| Location | Responsibility |
| :--- | :--- |
| [scripts/build.py](scripts/build.py) | Page generation and shared layout |
| [scripts/project_stories.py](scripts/project_stories.py) | Project-story content |
| [dist/](dist/) | Generated public site |
| `dist/stitch.css`, `dist/refinements.css`, `dist/catppuccin.css` | Styling and responsive refinements |
| `dist/site.js` | Mobile navigation and project filtering |
| [references/stitch/](references/stitch/) | Supplied design source and provenance |
| [process/](process/) | Existing process/verification records |

## Design and content boundaries

The supplied Stitch export is the design foundation; the repository preserves that provenance. This documentation uses the shared Catppuccin presentation, while the website preserves its responsive layout with a Catppuccin color overlay.

Content distinguishes current responsibilities, proposals, completed work, and ongoing projects. OneGauge work remains ongoing; the Temporary Access Pass workflow is a proposal, not a claimed deployment. Vera remains in development. Organizational scale is not presented as a measured personal outcome.

No assistant services or private integrations are connected to this standalone site. The public portfolio URL above was verified during this documentation review.

## Verification and next steps

Existing process notes describe prior visual and behavior checks. The current documentation pass checks generated local routes/assets; it does not certify deployment or repeat all interactive tests. Fresh responsive screenshots and a repeatable build/link check are useful next steps.
