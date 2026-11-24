# Poster Style Spec

Use this schema to convert a reference poster into reusable production constraints. Omit only fields that genuinely cannot be inferred from visible evidence.

## Identity

- **Archetype:** typography-led, character-led, portrait-led, product-led, illustration-led, collage, 3D/surreal, editorial-grid, cinematic, or minimal-symbol.
- **Purpose:** event, campaign, product, cultural, editorial, retail, entertainment, or concept.
- **One-line design thesis:** Explain what creates the poster's identity without naming its subject.

## Canvas and layout

- Aspect ratio and orientation.
- Outer margin as approximate percentage of width.
- Grid family: single column, multi-column, modular, axial, radial, diagonal, or freeform.
- Primary zones with relative bounds.
- Visual center and balance type.
- Negative-space map.
- Reading path.
- Density map: low, medium, or high by zone.

Describe relative geometry, for example:

```text
Title occupies the upper-left 42% of the canvas.
Hero enters from lower-right and covers about 65% of height.
Title overlaps the hero by roughly 8%.
Supporting information stays inside the lower-left safe zone.
```

## Typography system

- Main-title category: serif, grotesk, condensed, geometric, display, handwritten, pixel, or decorative.
- Weight, width, case, and apparent scale.
- Alignment, line count, line break behavior, tracking, and leading.
- Stretching, rotation, cropping, outline, shadow, mask, or distortion.
- Chinese/Latin relationship when both scripts appear.
- Subtitle and microcopy behavior.
- Text/image overlap and layer order.

Describe visual behavior instead of inventing an exact font family.

## Hero visual system

- Hero category: person, character, product, object, symbol, or type-as-image.
- Medium: photography, illustration, 3D, collage, craft, mixed media.
- Count, scale, crop, viewpoint, pose/action, and direction.
- Silhouette and shape language.
- Layering with title, background, and decoration.
- Treatment: cutout, duotone, halftone, felt, plastic, ink, blur, grain, glow, photocopy, or other visible method.
- Grounding: floor, shadow, reflection, float, frame edge, or none.

Extract the mechanism, not the original subject identity.

## Color system

- Background, dominant, secondary, and accent colors.
- Approximate area ratio.
- Saturation and temperature.
- Lightness contrast among background, hero, and title.
- Where the highest-contrast accent appears.
- Flat, gradient, duotone, limited-palette, fluorescent, metallic, or photographic behavior.

Prefer relationship statements such as `65% cyan background + 25% dark hero + 10% coral accents`.

## Graphic language

- Borders, rules, blocks, checkerboards, grids, arrows, labels, stamps, stickers, numbers, icons, or repeated type.
- Shape style: geometric, organic, pixelated, torn, hand-drawn, technical, or ornamental.
- Stroke thickness, corner behavior, repetition, and density.
- Symmetry or asymmetry.

## Surface, light, and finish

- Material cues: paper, ink, fabric, felt, clay, plastic, chrome, glass, or photographic skin.
- Lighting direction, hardness, contrast, and shadow character.
- Grain, noise, bloom, halftone, misregistration, scan, print, or compression texture.
- Sharpness and depth behavior.
- Overall finish: handmade, commercial-polished, editorial, raw, retro, futuristic, or hybrid.

## Lock map

### Hard lock

List 5–8 rules whose loss would make the new poster feel unrelated.

### Soft lock

List 3–6 adaptable rules.

### Must replace

List all semantic content and proprietary elements that must not survive the transfer.

## Prompt variables

Recommend the variables most useful for this poster system, including hero type, title length, prop count, palette, aspect ratio, and supporting information.
