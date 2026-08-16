---
name: create-food-ingredient-explosion-poster
description: Create, refine, label, and export premium vertical food ingredient deconstruction posters from product photos and exact ingredient lists. Use when the user asks to 拆解、分解、爆炸展示、标注配料, or make an exploded-view poster for pastries, mooncakes, snacks, dishes, beverages, or packaged foods; especially for 3:4 black-background commercial food photography with a white plate, cutaway product, independently floating ingredient layers, exact Chinese labels, short flavor notes, and deterministic final exports.
---

# Create Food Ingredient Explosion Poster

Turn product references and an ingredient list into a repeatable premium food poster. Preserve the real product, generate the food imagery without text, then add exact labels deterministically.

## Load the right references

- Read [references/visual-spec.md](references/visual-spec.md) before deciding composition, material treatment, or layer order.
- Read [references/prompt-template.md](references/prompt-template.md) before calling an image-generation tool.
- Read [references/copy-and-qa.md](references/copy-and-qa.md) before writing flavor notes, placing labels, or approving the export.
- Read [references/examples.md](references/examples.md) when adapting the workflow to a new product or when the user asks how prior products were handled.
- Use [scripts/compose_labels.py](scripts/compose_labels.py) for exact 3:4 padding, Chinese typography, leader lines, and final PNG export.

## Core contracts

1. Preserve product identity. Keep the supplied silhouette, proportions, embossed pattern, browning, side profile, crust thickness, filling colors, and cross-section recognizable.
2. Treat the ingredient list as exact content. Do not add, rename, merge, omit, or silently reorder ingredients.
3. Keep generated imagery text-free. Add Chinese names, notes, numbers, logos, and claims only with deterministic composition.
4. Do not invent nutrition, origin, certification, health, quality, or production claims.
5. Work non-destructively. Copy source references into a durable project folder and create versioned outputs.
6. Inspect the final raster at full size. Do not hand off an unverified image.

## Established default art direction

Use these defaults when the user says “和之前一样” or gives only product photos and ingredients:

- Exact final aspect ratio: 3:4 portrait.
- Standard export: 1440 × 1920 PNG.
- Background: pure seamless black.
- Product: one hero product on an elegant white porcelain plate at the bottom.
- Cutaway: remove about one quarter when internal fillings or layers matter; turn the cut face toward camera.
- Ingredients: independent floating layers above the product, with clean black gaps.
- Motion: rotation, outward fragments, foreground/background depth, suspended particles, and believable frozen motion.
- Base explosion: flour, sugar, and liquid oil form the largest, highest, widest cloud nearest the product.
- Lighting: warm cinematic rim light, appetizing highlights, realistic micro-texture, premium advertising finish.
- Labels: ingredient names plus optional one-line sensory notes; no boxes and no layer numbers.
- Leader lines: fine warm-gold lines, alternating left and right where practical.
- Product title: place near the plate with a concise layer or flavor summary.

Change a default only when the user requests a different format or the product needs a different visual truth.

## Workflow

### 1. Capture the brief

Collect or infer only what is safe:

- Exact product name.
- One or more product photographs.
- Exact ingredient names.
- Which photos define the whole product, surface pattern, cutaway, filling, or style.
- Required aspect ratio and output directory.
- Whether flavor notes are wanted.
- Any prohibited copy or visual elements.

Ask a question only when a missing answer changes product truth, ingredient truth, or public-facing copy. Otherwise use the established defaults and state the assumption briefly.

### 2. Prepare durable inputs

Create one product-specific output directory. Copy references there with descriptive filenames such as:

```text
<product>-whole-reference.jpg
<product>-cross-section-reference.jpg
<product>-style-reference.png
```

Inspect every source image. Assign one explicit role to each reference in the generation prompt. Never rely on a temporary chat attachment path as the only retained source.

### 3. Plan the story and layer order

Divide ingredients into:

- **Hero fillings or toppings:** visually distinctive ingredients that explain the product's flavor or cross-section.
- **Structural layers:** mochi, custard, paste, cream, crust, sauce, or other intermediate food materials.
- **Base ingredients:** flour, sugar, oil, salt, or similar foundational ingredients.

Arrange the vertical story from top to bottom:

1. The most recognizable hero ingredient.
2. Secondary fillings and flavor materials.
3. Structural layers closest to the finished product.
4. A large base-ingredient explosion.
5. The finished product on its plate.

This is a storytelling order, not a quantitative recipe claim. Never imply ingredient percentage unless the user supplies it.

Make visually similar ingredients unmistakable. Separate black and white sesame, green peppercorn and vine peppercorn, sugar and salt, or oil and syrup into distinct layers with different color, shape, and texture.

### 4. Plan the product presentation

Choose one of two bottom compositions:

- **Whole-product composition:** use when the surface identity matters more than the filling.
- **Quarter-cut composition:** use when the cross-section explains the product. Show one remaining product plus its removed wedge, not a pile of duplicate products.

For layered products, describe the cross-section from outside to inside and repeat that order in the prompt. Use the user's supplied layer names verbatim.

### 5. Generate the text-free base image

Use a reference-guided bitmap image-generation tool. Build the prompt from [references/prompt-template.md](references/prompt-template.md).

Always specify:

- The role of each input image.
- The exact product invariants.
- The exact ingredient set and vertical order.
- Material-specific appearance for each ingredient.
- Pure black side negative space for later labels.
- One product, one plate, and no unrelated props.
- No text, letters, labels, numbers, boxes, logos, packaging, or watermark.

When a Creative Production board is available, open it once for the product workflow, begin generation immediately before the image call, and complete the same board item with the durable output path. Do not open replacement boards during iteration.

### 6. Validate before adding text

Inspect the generated image and confirm:

- The product still resembles the source.
- The product count and plate count are correct.
- Every requested ingredient is visible exactly once as a logical layer.
- Similar ingredients are visually distinct.
- The cut face shows the requested outside-to-inside order.
- There is enough black space for labels.
- The composition can become exact 3:4 without cropping essential food.
- There is no generated text or watermark.

If one material or identity detail is wrong, make one targeted edit. Preserve all successful regions. Do not regenerate repeatedly for minor typography needs.

### 7. Make the export exact 3:4

Prefer padding over cropping when the generated image is taller than 3:4. A common 1024 × 1536 source becomes 1152 × 1536 by adding black side space, then scales cleanly to 1440 × 1920. This preserves the plate and top ingredient layer while creating label room.

Use `compose_labels.py` with a JSON label specification:

```bash
python scripts/compose_labels.py \
  --input generated.png \
  --output final-labeled.png \
  --spec label-spec.json \
  --unlabeled-output final-unlabeled.png
```

Start from [references/label-spec.example.json](references/label-spec.example.json). Set every target point after inspecting the actual generated image.

### 8. Add exact copy

Use the exact ingredient names supplied by the user. Add short sensory notes only when requested or established by the approved series style.

Good notes describe sensory contribution without unverifiable claims:

```text
咸香绵密
枣香浓郁
软糯拉丝
构筑酥松饼皮
甜度柔和 · 入口酥化
润泽起酥
```

Keep each note shorter than the ingredient name line when possible. See [references/copy-and-qa.md](references/copy-and-qa.md) for copy rules and unsafe claim categories.

### 9. Export and verify

Save at least:

```text
<product>-generated-source.png
<product>-unlabeled-3x4.png
<product>-labeled-3x4.png
<product>-manifest.json
```

Verify:

- Pixel size is exactly 1440 × 1920 unless another size was requested.
- File is a valid RGB or RGBA PNG.
- All Chinese strings match the approved copy.
- Every leader line ends on the correct ingredient.
- Text remains legible over black and does not cover key food.
- No edge is accidentally cropped.

Record source paths, ingredient order, product layers, final paths, dimensions, generation mode, and deterministic post-processing in the manifest.

### 10. Hand off

Lead with the completed result. Provide clickable absolute paths for the labeled and unlabeled versions, then show the final image inline when the interface supports local media. Summarize the generation route and the exact visual story in one or two sentences.

## Failure patterns to avoid

- Generating Chinese labels inside the food image model.
- Showing a second finished product when only one was requested.
- Mixing ingredient layers into an ambiguous pile.
- Depicting snow-mochi as cheese or whipped cream.
- Depicting jujube paste as chocolate.
- Depicting sugar and salt with identical crystals in adjacent layers.
- Flattening ingredients into static horizontal rows without rotation or depth.
- Cropping the white plate to force 3:4.
- Using flavor notes as factual health or quality claims.
- Overwriting the user's approved version instead of producing a sibling revision.

## Worked examples

Use [references/examples.md](references/examples.md) for three complete patterns:

- a many-ingredient nut-and-fruit pastry;
- a savory pepper-salt pastry with visually similar spices;
- a four-layer salted-duck-yolk pastry with a quarter-cut cross-section.

Reuse the decision pattern, not the product-specific ingredient list. Always replace names and layer order with the current user's exact brief.

## Completion standard

Consider the task complete only when the poster is visually inspected, exact copy is deterministic, all ingredients are accounted for, the final ratio and dimensions are verified, durable files exist, and the user can open the labeled export directly.
