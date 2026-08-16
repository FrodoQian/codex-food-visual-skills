# Reference-guided image-generation prompt template

Replace every bracketed value. Remove sections that do not apply. Keep the final request text-free.

```text
Use case: ads-marketing
Asset type: premium ingredient-deconstruction food poster

Create one ultra-realistic commercial food photography poster in a strict 3:4 vertical composition with a pure seamless deep-black background.

INPUT IMAGES
- Reference 1 defines [whole-product identity: silhouette, pattern, crust, side wall, color].
- Reference 2 defines [cross-section identity: outside-to-inside layers and textures].
- Reference 3 defines only [approved series style: black background, white plate, lighting, explosion language]. Ignore and do not reproduce any text from style references.

BOTTOM PRODUCT
Place one single [EXACT PRODUCT NAME] on an elegant clean white porcelain plate at the bottom. Preserve [PRODUCT INVARIANTS].

[Choose one:]
- Keep the product whole and fully visible.
- Remove one neat wedge of approximately one quarter and place it slightly beside the remaining product, with the cut face turned toward camera.

The cut face must clearly show these layers from outside to inside:
1. [OUTER LAYER]
2. [SECOND LAYER]
3. [THIRD LAYER]
4. [CENTER]

No hands, no utensils, no teapot, no table, no extra products.

BASE INGREDIENT EXPLOSION
Immediately above the product, create a very large, high, wide explosion combining exactly:
- [BASE INGREDIENT 1 and its visual behavior]
- [BASE INGREDIENT 2 and its visual behavior]
- [BASE INGREDIENT 3 and its visual behavior]

Keep every base ingredient separately identifiable. The event should be powerful, high-reaching, and appetizing.

INDEPENDENT UPPER LAYERS
Above the base cloud, build exactly [N] independent floating ingredient layers with clean black gaps, ordered strictly from bottom to top:
- [LAYER 1: exact ingredient plus shape, color, texture, behavior, and a critical NOT constraint]
- [LAYER 2: exact ingredient plus shape, color, texture, behavior, and a critical NOT constraint]
- [LAYER N]

Every layer must be dynamic and sculptural: rotation, flying fragments, front-back depth, varied scale, outward energy, and believable gravity frozen in motion. Keep each ingredient visually pure. Do not mix ingredients between layers.

COMPOSITION AND LIGHT
Use a slightly elevated 45-degree premium food advertising view, precise warm rim light, glossy highlights, realistic micro-texture, and strong appetite appeal. Use a tall balanced rhythm with lively motion. Leave generous clean negative space along both left and right edges for later exact Chinese labels and fine leader lines. Keep all key ingredients away from extreme side edges.

CONSTRAINTS
- Exactly one remaining product and one removed wedge when using a cutaway.
- Exactly one white porcelain plate.
- Preserve the supplied product identity.
- Show every listed ingredient and no unlisted ingredient.
- Pure black background.
- No text, letters, labels, numbers, frames, logos, packaging, props, or watermark.
```

## Targeted correction template

Use one correction at a time:

```text
Change only [INCORRECT REGION OR MATERIAL].
Replace it with [PRECISE CORRECTION].
Preserve the product, plate, all other ingredient layers, black background, lighting, camera, composition, empty label margins, and lack of text exactly as they are.
```

Do not use a full regeneration to fix deterministic labels or output dimensions.
