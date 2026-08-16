# Codex Food Visual Skills

一套用于食品商业视觉制作的可复用 Codex Skills。

目前包含：

- [`create-food-ingredient-explosion-poster`](skills/create-food-ingredient-explosion-poster/)：把食品产品照片和准确配料表制作成高质感的“原料爆炸拆解海报”。

## 这个 Skill 能做什么

输入产品照片、产品名称和配料表，Skill 会组织并执行完整的视觉生产流程：

1. 识别产品外形、花纹、颜色、厚度和剖面。
2. 判断应该展示完整产品，还是切开约四分之一展示内部层次。
3. 将配料拆成主角馅料、结构层和基础原料。
4. 生成纯黑背景、白瓷盘、商业美食摄影风格的无字主视觉。
5. 让每种原料以旋转、飞散、前后纵深的状态独立爆炸。
6. 将面粉、白砂糖和液态油制作成靠近产品的大面积高爆炸云。
7. 使用确定性排版添加准确的中文名称、风味说明和金色引线。
8. 输出有字版、无字版和制作说明文件。

默认成稿标准：

- 画幅：3:4竖版
- 尺寸：1440 × 1920 PNG
- 背景：纯黑
- 产品：底部单个产品＋白瓷盘
- 视角：略俯视45度商业美食摄影
- 标注：无外框、无层数、原料名＋简短风味说明
- 引线：暖金色细线，左右交错
- 文案：准确中文，不让图片模型自行生成文字

## 安装

### 方法一：克隆后建立软链接（推荐）

```bash
git clone https://github.com/FrodoQian/codex-food-visual-skills.git
cd codex-food-visual-skills
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/skills/create-food-ingredient-explosion-poster" \
  "${CODEX_HOME:-$HOME/.codex}/skills/create-food-ingredient-explosion-poster"
```

软链接安装后，在仓库中执行 `git pull` 即可同步新版 Skill。

如果目标位置已经存在同名目录或链接，`ln` 会停止并提示，不会覆盖原文件。

### 方法二：直接复制

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/create-food-ingredient-explosion-poster \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重新打开 Codex 任务或开始新任务后，Skill 即可被发现。

## 最简单的使用方法

在 Codex 中附上产品照片，然后输入：

```text
使用 $create-food-ingredient-explosion-poster，
把这些产品照片和配料表制作成3:4的原料爆炸拆解海报。
产品名称：四层蛋黄蛋月烧。
配料：液态油、五星面粉、中粒白砂糖、海鸭蛋黄、红枣泥、雪媚娘。
分解方式沿用黑底、白瓷盘、动态分层和中文标注。
```

也可以使用更自然的中文：

```text
这是我们的桃酥皮椒盐，成分有液态油、五星面粉、中粒白砂糖、
黑芝麻、白芝麻、花生、青花椒、藤椒、盐和小茴香。
请按照之前的方式拆解成一张3:4海报。
```

Skill 的描述包含“拆解、分解、爆炸展示、标注配料”等触发语，因此明确提到这些需求时也可以自动触发。

## 建议提供的资料

为了提高产品保真度，建议一次提供：

- **产品名称**：必须使用的准确名称。
- **整体照片**：用于确认外形、顶部花纹、侧边和烘烤颜色。
- **剖面照片**：用于确认馅料颜色、厚度和内外顺序。
- **准确配料表**：每个名称按成稿中希望出现的写法提供。
- **明确层次**：如果产品有多层结构，说明从外到内的顺序。
- **参考风格图**：如果希望延续已有系列，可附上一张已认可的成稿。
- **特殊要求**：例如“只显示名字”“增加风味说明”“不要层数”“切开四分之一”。

如果没有特别说明，Skill 会采用本仓库已经形成的默认视觉体系。

## 标准工作流程

### 1. 保留产品身份

系统首先检查参考图中的产品轮廓、比例、压花、色泽、酥皮厚度和剖面，不把产品变成通用月饼或其他糕点。

### 2. 规划原料顺序

从上到下通常为：

1. 最有辨识度的主角原料。
2. 其他馅料或风味原料。
3. 与成品最接近的结构层。
4. 面粉、白砂糖和液态油组成的大型基础爆炸云。
5. 白瓷盘中的最终产品。

这是视觉叙事顺序，不代表配料含量或配方比例。

### 3. 先生成无字主视觉

图片生成阶段只负责食物、材质、灯光和构图。提示词明确要求：

- 不生成文字、数字、标签、外框或水印；
- 每种原料独立成层；
- 左右预留黑色标注空间；
- 只出现一个产品和一个白瓷盘；
- 不出现木桌、茶壶、手、包装等无关元素。

### 4. 再添加准确中文

原料名称和风味说明由脚本确定性绘制，避免图片模型写错汉字。完整规则见：

- [文案与验收规范](skills/create-food-ingredient-explosion-poster/references/copy-and-qa.md)
- [JSON标注示例](skills/create-food-ingredient-explosion-poster/references/label-spec.example.json)

### 5. 检查并交付

最终检查产品是否像原图、原料是否齐全、引线是否指向正确位置、3:4尺寸是否准确，再交付有字版和无字版。

## 手动使用标注脚本

脚本依赖 Python 3 和 Pillow：

```bash
python -m pip install Pillow
```

复制并调整示例配置：

```bash
cp skills/create-food-ingredient-explosion-poster/references/label-spec.example.json \
  /path/to/your-label-spec.json
```

执行排版：

```bash
python skills/create-food-ingredient-explosion-poster/scripts/compose_labels.py \
  --input /path/to/generated-no-text.png \
  --output /path/to/final-labeled.png \
  --unlabeled-output /path/to/final-unlabeled.png \
  --spec /path/to/your-label-spec.json
```

只检查配置、不写文件：

```bash
python skills/create-food-ingredient-explosion-poster/scripts/compose_labels.py \
  --input /path/to/generated-no-text.png \
  --output /path/to/unused.png \
  --spec /path/to/your-label-spec.json \
  --validate-only
```

脚本会：

- 将输入无损适配到目标画幅；
- 默认优先补黑边，不裁掉食物；
- 绘制中文名称、风味说明、引线和端点；
- 输出标准RGB PNG；
- 检查标签名称、坐标和画布范围。

macOS默认使用系统中文字体。Linux或Windows用户可以在JSON配置中设置 `font_path`。

## 完整案例

仓库提供三个经过真实项目迭代的案例：

1. **赵州饼**：十一种原料，多层坚果、果干与基础原料爆炸。
2. **桃酥皮椒盐**：芝麻、花生、双花椒、盐和小茴香的相似食材区分。
3. **四层蛋黄蛋月烧**：切开四分之一，展示酥皮、雪媚娘、红枣泥和海鸭蛋黄剖面。

每个案例的输入、层次规划、文案和验收重点见 [完整案例说明](skills/create-food-ingredient-explosion-poster/references/examples.md)。

## 输出文件

建议每个产品保留：

```text
<产品>-整体参考.jpg
<产品>-剖面参考.jpg
<产品>-生成原图.png
<产品>-无字版-3x4.png
<产品>-文案增强版-3x4.png
<产品>-制作说明.json
```

不覆盖已经认可的版本。每次修改使用新的文件名或版本号。

## Skill内部文件

```text
create-food-ingredient-explosion-poster/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── copy-and-qa.md
│   ├── examples.md
│   ├── label-spec.example.json
│   ├── prompt-template.md
│   └── visual-spec.md
└── scripts/
    └── compose_labels.py
```

## 致谢

感谢 **FrodoQian** 持续提供真实食品产品素材、明确的业务目标和细致的审美反馈。从赵州饼、桃酥皮椒盐到四层蛋黄蛋月烧，多轮实际制作与修正共同沉淀出了这套可复用流程。

感谢 **OpenAI Codex 与 ImageGen** 提供参考图理解、视觉生成和自动化工作能力。

感谢 **Pillow** 提供稳定的图像缩放、排版和PNG导出能力，使中文名称与标注能够保持准确。

也感谢每一位使用、测试并继续改进这个 Skill 的创作者。希望它能帮助传统食品与地方特产以更清晰、更有食欲的方式讲述自己的原料故事。
