# EverAI — Brand Study

Observed 1 October 2026 · Prepared by Ayo Ahmed

Source: [EverAI website](https://www.everai.ai/). Measurements reference the live homepage and its published styles at desktop (1,440 × 900), tablet (782 × 896) and mobile (390 × 840) viewports. This is an independent reference, not an official brand manual. Observed values and recommendations are labelled separately.

## Design character

Black foundations, white type and a concentrated electric-blue accent. Generous space makes the page feel expansive. Reflective abstract forms supply the colour and texture; the interface stays simple. Regular-weight geometric sans-serif headlines gain a human accent through a single italic serif word.

The page alternates dark hero/about/contact/footer areas with white vision and careers sections. Preserve that contrast when recreating the site. The accompanying guide uses a dark editorial layout to display the collected system; its composition is a reference presentation, not a copy of the homepage.

## Logo

- Original transparent raster wordmark: [assets/logo.webp](assets/logo.webp). Native size: 254 × 31px.
- Uppercase, widely spaced lettering. The first part is white; the final two letters have a muted blue/lilac treatment built into the image. Do not replace those colours with the button blue.
- Desktop header and footer display width: 130px. Mobile header wrapper remains 130px with 20px left padding, leaving approximately 110px for the image.
- The native proportions are about 8.19:1. Keep the aspect ratio and do not rebuild the wordmark using typed letters.
- Small symbol: [assets/favicon.png](assets/favicon.png). Treat it as the observed browser icon; a broader standalone symbol system was not established.
- No vector logo or light-background logo variant was found in the homepage assets. Use the original on black or a dark image rather than inventing a variant.

**Recommendation:** leave at least one logo-height of clear space around the wordmark. This is a practical rule for the study, not a published minimum. Avoid scaling the raster beyond its native width for sharp production artwork; obtain a vector master for larger use.

## Colours

### Active homepage palette

| Role | Value | Evidence / application |
|---|---|---|
| Black | `#000000` | Page, hero, about and footer backgrounds; careers headline |
| White | `#FFFFFF` | Main text on dark surfaces; vision and careers surfaces; inverse button |
| Electric blue | `#0428CB` | Main action fills; declared `--blu-hero` |
| Ink navy | `#080D31` | Inverse button text and careers label; declared `--text-color` |
| Deep blue | `#00052E` | Hero backdrop from the wide-screen rule |
| Muted text on black | `rgba(255,255,255,0.7)` / `#FFFFFFB3` | Supporting descriptions and footer details; appears approximately `#B3B3B3` on black |
| Muted text on white | `#676767` | Careers description |
| Subtle light edge | `rgba(255,255,255,0.15)` / `#FFFFFF26` | Hero overlay top border |
| Dark image overlay | `rgba(0,0,0,0.1)` / `#0000001A` | Hero overlay |

Additional emphasis spans use black or white at 50% opacity. Their visible colour depends on the background. The lilac and violet highlights in imagery are baked into the assets, not universal interface colour values.

### Declared, but not active in the measured homepage

`#A8DE81` (green), `#4F4F4F` (grey) and `#D5D5D5` (light grey) remain in shared styles for older components. Do not promote them to the current primary palette. Inherited `#333333` on empty logo links is likewise not a visible wordmark colour.

### Contrast

White on electric blue: approximately **9.67:1**. White on black: **21:1**. Ink navy on white: approximately **18.88:1**. The muted white at 70% opacity on black is approximately **10:1**. These pairings exceed 4.5:1 for normal-sized text. Electric blue on black is approximately **2.17:1**, so use blue as a fill with white text, not small blue text on black.

## Typography

### Families

**Aspekta Variable** is the active homepage sans-serif. The published family alias is `Aspektavf`; the declared weight range is 100–900. Most visible text uses 400, actions use 500–600, and section labels use 600. Local file: [assets/aspekta-variable.ttf](assets/aspekta-variable.ttf).

**Newsreader Italic**, weight 400, is the live headline accent, selected by `.heder-italic`. The local specimen uses the italic font supplied by the same font service referenced by the homepage: [assets/newsreader-italic.ttf](assets/newsreader-italic.ttf). Use it for a short word or phrase, not a whole paragraph.

The shared stylesheet also declares “Newsreader 60 Pt” and Times, and loads Poppins. Their presence is not evidence that they are the homepage's primary typography. Use Aspekta plus Newsreader for this study.

### Observed type scale

| Role / selector | Desktop | Mobile | Weight / tracking |
|---|---|---|---|
| Hero `.heding-style-heder` | 72px / 79.2px | 9vw / 110%; 35.1px / 38.61px at 390px | 400 / normal |
| Feature `.heding-style-h2` | 40px / 44px | Mobile uses a separate text presentation, 24px / 28px | 400 / normal |
| About statement `.heding-style-h3` | 40px / 48px | 24px / 28.8px | 400 / normal |
| Contact `.heading-12` | 64px / 70px | 40px / 50px | 400 / normal |
| Careers `.heding-style-h1` | 51px / 50px | 51px / 50px | 400 / normal |
| Small headline `.heding-style-h4` | 25px / 40px | 20px / 30px | 400 / normal |
| Body `.text-style-normal.is-color` | 16px / 25.92px | 14px / 20px; compact service copy 12px / 20px | 400 / 1px |
| Careers description `.text-block-19` | 20px / 27px | 20px / 27px | 400 / normal |
| Contact description `.text-block-20` | 18px / 30.96px | 16px / 21.6px | 400 / normal |
| Section labels `.text-block-18` | 13px / inherited 20px | Same | 600 / uppercase |
| Actions | 14px / 19.6px | 13px / 16.9px | Blue 500; white 600 / uppercase |
| Navigation | 16px / 20px | Menu links 40px / 20px, with 30px vertical padding | Desktop 400; mobile menu 300 |

The hero uses **7vw below 992px**, **6vw below 768px** and **9vw below 480px**. These are distinct rules rather than a single smooth size formula. Preserve them when matching the original. Hover transitions can produce intermediate computed action sizes during measurement; the table records the settled stylesheet values.

**Recommendation:** retain readable 14–16px body text in new small-screen designs instead of copying the observed 12px service text everywhere. Keep italic descenders clear and preserve the source's comfortable headline line-height.

## Spacing and layout

The site uses several recurring gaps, not a strict single-step spacing scale.

| Element | Desktop observation | Small-screen observation |
|---|---|---|
| Main container `.conteiner-large` | 946px base; 1,200px from 1,280px viewport upward | Automatic width, 20px margin on each side below 992px |
| Outer margins at 1,440px | `(1440 − 1200) / 2 = 120px` | At 390px: 350px content width |
| Header | 60px high; 1,200px wide at 1,440px | Menu replaces inline navigation below 992px |
| Hero frame | 100vh; 4px padding above 1,280px, otherwise 10px | 100vh; 10px padding |
| Hero background | 99vw × 99vh; 10px corners | Same declared size |
| Hero text area | Maximum 700px; centred | Contracts to available width |
| Hero heading → action | 70px flex gap | 70px |
| Main section spacing `.pading-global` | 170px top and bottom margin | 80px below 992px |
| Vision section spacing `.is-margin` | 170px top and bottom padding | 100px below 992px |
| Careers section padding | 170px top and bottom | 115px below 992px |
| Feature panels | 40px vertical gap | 80px gap in the separate mobile presentation |
| Feature text stack | 40px gap; 405px text width | Adapts to stacked presentation |
| About statement → services | 100px | 100px |
| Services | Three columns with 24px gap | Stacked rows with 40px gap; image/text gap 12px below 480px |
| Inner service text stack | 24px | 24px |
| Contact text stack | 50px gap; maximum 600px | 28px below 768px |
| Footer columns | `2fr .5fr .5fr`; 16px gaps | Stacked flex layout with 72px gap below 768px |
| Action padding | 15px vertical / 30px horizontal | Same blue actions; white action 23.5px horizontal below 768px |

Recurring observed sizes: **12, 16, 20, 24, 28, 30, 36, 40, 50, 70, 80, 100, 115 and 170px**. Use the element-specific value rather than forcing every component onto an invented grid.

### Responsive boundaries

- **≥1,280px:** 1,200px container; 4px hero frame.
- **≥1,440px:** select image alignment and text-stack adjustments.
- **≤991px:** 20px side margins, expanded navigation menu, stacked features/services and reduced section spacing.
- **≤767px:** smaller statement/headline styles, contact changes, stacked footer.
- **≤479px:** 9vw hero headline; compact service descriptions; 12px image/text gap.

## Components and surface treatment

**Blue action:** `#0428CB` background, white uppercase label, 500 weight, 14px desktop size, 15px × 30px padding, 100px corner radius. On hover, the primary hero action becomes white with navy text. Transition duration: 0.4 seconds. The careers action has matching base styling but no separate hover declaration was found.

**White action:** white background, navy uppercase label, 600 weight, same desktop padding and radius. On hover it becomes electric blue with white text. Transition duration: 0.4 seconds.

**Images:** 10px corners, full-bleed crop, cover sizing. Small service images use 2.5px corners below 768px. Their native artwork creates depth; avoid extra decorative shadows.

**Labels:** 13px uppercase text, 600 weight, paired with an 8px square marker and 12px gap in the source. White marker on black; navy marker on white.

**Navigation:** transparent over the hero. Desktop links are restrained and title case. The contact link is smaller and uppercase with an arrow. Small screens reveal a large-link menu.

**Motion:** the hero plays a looping, muted abstract background film. This guide displays its original poster as a still. Other measured transitions are 0.4 seconds. For new work, respect reduced-motion settings and keep readable text steady.

## Imagery

| Local asset | Observed use |
|---|---|
| `assets/hero-poster.jpg` | Still from the abstract reflective hero sequence |
| `assets/feature-01.webp` | Blue-lit sculptural portrait on black |
| `assets/feature-02.webp` | Companion feature artwork |
| `assets/abstract-01.webp`–`abstract-03.webp` | Reflective abstract service imagery |
| `assets/careers.webp` | Wide careers illustration |
| `assets/contact-background.png` | Wide blue contact background |
| `assets/arrow-up-right.svg` | Original directional arrow |

The asset language is glossy, sculptural and dimensional: cobalt lighting, lilac reflections, deep black shadows and large crops. Keep colour within imagery rather than adding unrelated interface gradients.

## Practical reuse

1. Use the original wordmark, Aspekta 400 and short Newsreader italic accents.
2. Start with black, white, blue and navy. Use muted text only for supporting information.
3. Keep one clear action per content block. Preserve the pill shape and generous padding.
4. Centre large content areas, keep 20px mobile side margins and allow sections to breathe.
5. Use collected artwork for the specimen; obtain appropriate rights before broader publication. Brand artwork remains owned by its respective rights holders.

### Compact style reference

```css
:root {
  --black: #000000;
  --white: #ffffff;
  --blue: #0428cb;
  --ink: #080d31;
  --deep-blue: #00052e;
  --muted-dark: rgb(255 255 255 / 70%);
  --muted-light: #676767;
  --image-radius: 10px;
  --action-radius: 100px;
}
```

Open [visual-guide.html](visual-guide.html) for the visual reference. All displayed fonts and imagery are local files. Original asset addresses, file sizes and checksums are recorded in [assets/sources.json](assets/sources.json).
