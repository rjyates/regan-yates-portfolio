# Portfolio site — agent instructions

Static professional portfolio and mobile networking site. Routes: `/` (introduction and work), `/links/`, `/resume/`.

## Build and preview
- Source content lives in `scripts/`; `dist/` is generated output. Edit source, then rebuild: `python scripts/build.py` (requires `lxml`).
- Preview: `python -m http.server 4321 --bind 127.0.0.1 --directory dist` → http://127.0.0.1:4321
- Never hand-edit `dist/` as the only change.

## Content rules
- Facts about experience, projects and achievements must come from the user or existing content. Never invent roles, metrics, dates or outcomes.
- Keep a professional, concise tone aimed at technology leadership roles.
- Accessibility: semantic HTML, alt text, sufficient contrast, works without JavaScript.
- Public site: no phone numbers, home address or private details unless the user explicitly adds them.

## Working conventions
- Branch per change; rebuild and preview before committing; commit source and regenerated `dist/` together.
