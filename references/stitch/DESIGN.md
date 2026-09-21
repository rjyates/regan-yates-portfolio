---
name: Executive Architectural Editorial
colors:
  surface: '#faf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f4f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e4'
  surface-container-highest: '#e3e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ed'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#715a3e'
  on-secondary: '#ffffff'
  secondary-container: '#fdddb9'
  on-secondary-container: '#786044'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#111c2c'
  on-tertiary-container: '#798499'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#fdddb9'
  secondary-fixed-dim: '#e0c29f'
  on-secondary-fixed: '#281803'
  on-secondary-fixed-variant: '#584329'
  tertiary-fixed: '#d8e3fa'
  tertiary-fixed-dim: '#bcc7dd'
  on-tertiary-fixed: '#111c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#faf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e3e2df'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 56px
    fontWeight: '400'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Newsreader
    fontSize: 38px
    fontWeight: '400'
    lineHeight: 46px
    letterSpacing: -0.015em
  headline-xl:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: -0.015em
  headline-xl-mobile:
    fontFamily: Newsreader
    fontSize: 30px
    fontWeight: '400'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 22px
    fontWeight: '500'
    lineHeight: 30px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  code-tech:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.02em
spacing:
  gutter: 1.5rem
  gutter-desktop: 2.5rem
  margin: 1.25rem
  margin-tablet: 2.5rem
  margin-desktop: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.75rem
  space-xl: 3rem
---

## Brand & Style

This design system is calibrated for executive technology leadership—Solutions Architects, IT Directors, and VP/CTO candidates. It replaces typical SaaS aesthetics and neon-tinted developer clichés with quiet confidence, intellectual rigor, and architectural precision. 

The aesthetic is anchored in warm architectural minimalism and Swiss-inspired editorial restraint. The visual language evokes high-end architectural monographs, strategic white papers, and legacy broadsheet typography. It communicates systematic thinking, governance, high-level business acumen, and structural engineering discipline. Interfaces emphasize deliberate pacing, structured hairline grid divisions, deliberate micro-typography, and high-density data presented with calm legibility.

## Colors

The color system relies on natural, low-fatigue materials rather than cold synthetic grays:

- **Canvas & Surfaces:** The primary ground is `#FAF9F6` (Linen), layered with `#F5F4F0` (Alabaster Warm) for surface containers, cards, and structured groupings. Pure white (`#FFFFFF`) is used sparingly, reserved for elevated interactive panels or code/schema viewports.
- **Ink Palette:** Deep Ink (`#111111`) commands high-contrast headlines and critical metrics, while Charcoal Ink (`#2A2A28`) handles body text. Supporting structural labels and metadata use Muted Ink (`#6E6D67`).
- **Architectural Lines:** Hairline borders, dividers, and grid outlines rely strictly on Stone Rule (`#E5E3DC`) and Deep Rule (`#D4D2C9`).
- **Executive Accents:** Warm Architectural Bronze (`#8C7355`) indicates primary actions, featured metrics, and editorial flourishes. Deep Slate (`#4A5568`) supports technical categorization, infrastructure status, and secondary tags.
- **Functional Semantics:** System indicators avoid primary red/green saturations. Instead, muted terra cotta (`#A64B3E`), sage green (`#4A6B53`), and warm amber (`#9E742A`) provide subtle, authoritative status cues.

## Typography

The typographic system creates an intentional dialogue between three distinct voices:

1. **The Executive Voice (`Newsreader`):** Used across hero displays, project titles, and strategic pull quotes. Rendered with optical sizing considerations and moderate weights (Regular 400 to Medium 500), projecting scholarship, legacy, and decisive judgment.
2. **The Systematic Engine (`Inter`):** Applied to narrative body copy, executive summaries, bullet points, and high-density interface controls. Neutral, legible, and structurally sound at small sizes.
3. **The Technical Substrate (`JetBrains Mono`):** Reserved for technical stack tags, system architecture specifications, dates, indices, and numerical KPIs. Kept small, precise, and understated.

Pairings must strictly align: avoid italicizing sans-serif text, and use italic styles within `Newsreader` sparingly for editorial emphasis or secondary contextual definitions.

## Layout & Spacing

The layout follows a strict, disciplined grid model inspired by architectural framing:

- **Grid Structure:** A 12-column system on desktop (`>= 1024px`), an 8-column system on tablet (`768px - 1023px`), and a 4-column system on mobile (`< 768px`). 
- **Column Alignments:** Case study cards, executive metrics, and architecture diagrams snap strictly to column edges. Asymmetric column spans (e.g., 4 columns for an executive briefing sidebar, 8 columns for technical implementation analysis) are encouraged to preserve editorial balance.
- **Rhythm & Padding:** Whitespace is treated as a physical material. Content density remains high inside structured data regions, but breathing room between major architectural sections (`space-xl` or greater) prevents cognitive fatigue.
- **Structural Lines:** Dividers follow the grid channels, producing visible horizontal and vertical axes (`1px solid #E5E3DC`) that structure reading order.

## Elevation & Depth

This system avoids layered dropshadows, blurred scrims, and floating cards. Depth is conveyed purely through surface materiality, nested framing, and hairline demarcation:

- **Surface Layering:** The primary canvas (`#FAF9F6`) serves as the basement tier. Structural cards and modules sit flat upon it using `#F5F4F0`, separated by a `1px` crisp hairline (`#E5E3DC`).
- **Low-Contrast Outlines:** Visual containment relies on 1px solid outlines instead of box-shadows. The perimeter of interactive elements takes on `#D4D2C9` at rest, darkening to `#8C7355` or `#111111` on hover/focus.
- **Subtle Elevation Exceptions:** For floating modals, persistent navigation headers, or command palettes, an ultra-fine, diffused grounding shadow is permitted: `0 8px 24px -6px rgba(17, 17, 17, 0.04), 0 2px 6px -2px rgba(17, 17, 17, 0.02)`.

## Shapes

The design system employs a strict `0` roundedness level. All corners—buttons, cards, metric containers, interactive chips, and media viewports—are razor-sharp (`0px` border-radius). 

This crisp geometry reinforces architectural blueprints, institutional trust, and deliberate construction. Precision is achieved through aligned hairlines rather than smoothed pill forms or casual circular curves.

## Components

### Buttons
- **Primary:** Solid `#111111` fill, `#FAF9F6` text (`Inter`, 13px, Medium), sharp corners, padding `0.75rem 1.5rem`. Subtle transition on hover to `#8C7355`.
- **Secondary (Architectural Line):** Background transparent, 1px solid `#111111` border, `#111111` text. Hover state fills `#F5F4F0` with accent `#8C7355` border.
- **Tertiary/Ghost:** Text-only in `#111111` with an underline offset of 4px using `#D4D2C9`, shifting to `#8C7355` on focus.

### Case Study & Architecture Cards
- **Structure:** Crisp rectangular panels framed with a 1px `#E5E3DC` boundary.
- **Header:** Features a top horizontal index bar: project category and date stamp rendered in `JetBrains Mono` (`11px`, `#6E6D67`), separated by an em-dash.
- **Body:** Serif project title (`Newsreader`, 22px), followed by a brief strategic narrative (`Inter`, 14px).
- **Footer:** Metrics strip showing business outcomes (e.g., "$4.2M Cloud OpEx Saved" or "99.999% SLA") separated by subtle vertical rules.

### Metric Panels (Executive Impact Summaries)
- **Container:** High-density, light grey `#F5F4F0` background with sharp borders.
- **Figure:** Sized at `36px` to `48px` using `Newsreader` (Medium), rendered in `#111111` or `#8C7355`.
- **Annotation:** Subtitle in `Inter` (`12px`, `#6E6D67`, uppercase, `0.05em` letter-spacing) placed directly below or above the metric.

### Tech Stack Chips / Badges
- **Styling:** Monospaced (`JetBrains Mono`, `11px`), flat `#FFFFFF` background with a 1px `#E5E3DC` stroke. 
- **Padding:** `0.2rem 0.55rem`. Zero corner radius. Text color `#4A5568`.

### Inputs & Form Controls
- **Field:** Background `#FAF9F6`, baseline or fully boxed border using 1px `#D4D2C9`. Focus shifts stroke to `#111111` with no outer glow.
- **Labels:** Micro-caps (`Inter`, 11px, bold, uppercase, letter-spacing `0.08em`, color `#6E6D67`).

### Checkboxes & Radios
- **Geometry:** Strict squares for checkboxes (no radius); crisp circular or diamond glyphs for radios.
- **Border:** 1px solid `#111111` with solid `#111111` interior tick or center square on selection.

### Systems Blueprint Viewer / Diagram Framing
- Technical diagrams and architecture flowcharts are framed within an inner `#F5F4F0` container bounded by crosshair marks at each corner, reminiscent of precision CAD drawings and mechanical drafting schematics.