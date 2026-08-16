# Codex Food Visual Skills

Reusable Codex skills for premium food ingredient deconstruction visuals.

## Available skill

### `create-food-ingredient-explosion-poster`

Turns product photographs and an exact ingredient list into a polished 3:4 commercial food poster with:

- a recognizable product on a white porcelain plate;
- an optional quarter-cut cross-section;
- independently floating ingredient layers;
- a large flour, sugar, and liquid-oil base explosion;
- deterministic Chinese ingredient labels and sensory notes;
- labeled, unlabeled, and manifest exports.

The full workflow, visual system, prompt template, copy rules, QA checklist, JSON label schema, and reusable Pillow composition script live in [the skill folder](skills/create-food-ingredient-explosion-poster/).

## Use

Install or copy the skill into your Codex skills directory, then invoke it with a request such as:

```text
Use $create-food-ingredient-explosion-poster to turn these product photos and this ingredient list into a 3:4 exploded ingredient poster.
```

The skill defaults to a pure black background, white plate, premium food photography, warm-gold leader lines, exact Chinese copy, and a 1440 × 1920 PNG export.
