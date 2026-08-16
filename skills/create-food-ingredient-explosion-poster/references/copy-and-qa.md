# Copy, labeling, and QA rules

## Contents

1. Exact ingredient names
2. Sensory-note writing
3. Leader-line placement
4. Final QA checklist
5. Manifest requirements

## 1. Exact ingredient names

Copy ingredient names verbatim from the user. Preserve distinctions such as:

- 液态油 versus 大豆油 or 花生油
- 五星面粉 versus 面粉
- 中粒白砂糖 versus 白砂糖
- 青花椒 versus 藤椒
- 海鸭蛋黄 versus 蛋黄

Do not “correct” a product name or ingredient name without user confirmation. Do not change list order when the user provides an explicit order.

## 2. Sensory-note writing

Use short descriptions of flavor, aroma, mouthfeel, or structural function. Favor four-to-eight Chinese characters.

Safe patterns:

- Aroma: 枣香浓郁、清香细腻、温润回香、鲜麻提香
- Taste: 咸香绵密、甜度柔和、平衡咸香
- Texture: 软糯拉丝、酥香饱满、入口酥化
- Structural role: 构筑酥松饼皮、润泽起酥

Avoid unsupported claims:

- health or medical benefits;
- nutritional superiority;
- percentage, grade, origin, age, scarcity, or certification;
- “zero additives,” “organic,” “handmade,” “best,” or similar facts not supplied by the user.

For a product subtitle, summarize visible layers instead of inventing a slogan:

```text
酥皮 · 雪媚娘 · 枣泥 · 海鸭蛋黄
```

## 3. Leader-line placement

For every label:

1. Place the name in outer black space.
2. Place the sensory note 40–46 px below the name at 1440 × 1920.
3. Start the line 18–24 px after the text bounding box.
4. Use one horizontal segment and one short angled segment.
5. End on an unmistakable part of the ingredient.
6. Use a gold endpoint with a dark center so the target remains visible.
7. Avoid crossing another label, ingredient name, or important product feature.

For the base cloud, point separately to:

- an opaque white flour tower;
- a visible faceted sugar crystal cluster;
- a glossy gold liquid-oil ribbon.

Do not point all three labels at the center of the same mixed cloud.

## 4. Final QA checklist

### Product

- [ ] Product silhouette and surface remain recognizable.
- [ ] Exactly one intended product composition is shown.
- [ ] White plate is complete and undistorted.
- [ ] Cutaway order matches the brief.
- [ ] No hands, utensils, table, packaging, or unrelated props remain.

### Ingredients

- [ ] Every exact ingredient name has a corresponding visible material.
- [ ] No extra ingredient has been introduced.
- [ ] Layers follow the planned top-to-bottom order.
- [ ] Similar ingredients are visually distinguishable.
- [ ] Every layer has motion, depth, and a clean black gap.
- [ ] Base flour, sugar, and oil remain separately readable.

### Copy

- [ ] Names match the user character-for-character.
- [ ] Notes are sensory or structural, not factual claims.
- [ ] No boxes or layer numbers appear unless requested.
- [ ] Product title is exact.
- [ ] Product subtitle matches visible layers.

### Layout and export

- [ ] Final aspect ratio is exactly 3:4.
- [ ] Final size is 1440 × 1920 unless specified otherwise.
- [ ] Text and lines stay inside the canvas.
- [ ] Each endpoint targets the correct material.
- [ ] No important food was cropped to force the ratio.
- [ ] Labeled and unlabeled PNGs open successfully.
- [ ] Manifest paths and ingredient order are accurate.

## 5. Manifest requirements

Record:

```json
{
  "project": "<product> ingredient deconstruction",
  "aspect_ratio": "3:4",
  "final_size": "1440x1920",
  "source_images": [],
  "generated_source": "",
  "unlabeled_image": "",
  "final_image": "",
  "ingredient_order_top_to_bottom": [],
  "product_layers_outside_to_inside": [],
  "style": "",
  "provenance": "reference-guided image generation plus deterministic typography"
}
```
