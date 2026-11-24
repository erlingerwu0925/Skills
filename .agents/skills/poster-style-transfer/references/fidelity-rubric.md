# Poster Fidelity Rubric

Score the generated poster against the extracted design system, not against the reference's semantic content.

## Weighted score

| Dimension | Weight | Evaluate |
| --- | ---: | --- |
| Layout skeleton | 25 | Grid, zones, margins, balance, reading path, density map |
| Typography system | 20 | Title footprint, hierarchy, alignment, line behavior, overlap |
| Hero mechanism | 20 | Subject scale, crop, silhouette, medium, layer relationship |
| Color relationships | 15 | Area ratios, contrast, saturation, accent placement |
| Graphic language | 10 | Repeated devices, shapes, borders, icons, decoration density |
| Surface and finish | 10 | Material, lighting, grain, print/3D/photo treatment |

Score each dimension from 0–100, multiply by its weight, and divide the total by 100.

## Interpretation

- **90–100:** Clearly belongs to the same design system while remaining original.
- **85–89:** Strong transfer; minor differences do not weaken recognition.
- **75–84:** Related mood, but at least one structural system has drifted.
- **Below 75:** Style keywords were copied, but the poster grammar was not transferred.

Target at least `85/100`. Reject or revise when layout skeleton, typography system, or hero mechanism scores below `70`, regardless of total score.

## Content checks

Pass all of these independently of the weighted score:

- New theme is immediately legible.
- Hero and props belong to the new theme.
- No reference logo, wording, person, proprietary character, or unique illustration survives.
- Exact supplied copy is correct and readable.
- No random letters, unwanted watermark, or invented official information appears.
- The output is not a pixel-for-pixel reconstruction.

## Revision rules

Identify the lowest high-weight dimension and make one targeted correction.

- Low layout score: restate relative zones, margins, and overlap percentages.
- Low typography score: restate title footprint, line count, alignment, and type behavior.
- Low hero score: restate scale, crop, silhouette, medium, and layer order.
- Low color score: restate color area ratios and contrast roles.
- Incorrect text: change only the copy region and repeat the exact text verbatim.
- Reference leakage: explicitly replace the leaked object and repeat the originality constraints.

Re-score after revision. Do not compensate for weak layout with extra texture or decoration.
