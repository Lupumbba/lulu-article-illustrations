# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art with slightly wobbly pen lines. Lots of empty white space. Sparse handwritten Chinese annotations in red, orange, and blue. Clean product-sketch feeling, warm, calm, lightly absurd. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's book style, no realistic UI.

Recurring IP character required:
噜噜, a warm yellow-orange chubby capybara-like character with tiny black dot eyes, rounded blunt body, calm blank expression, short limbs, a small orange fruit or clear orange mark on top of the head, and optional simple shorts. 噜噜 must perform the core conceptual action, not decorate the scene. Make 噜噜 emotionally stable, slow, serious, and gently funny, not childish and not a sticker mascot.

Theme:
{正文配图主题}

Structure type:
{结构类型：缓冲带 / 承接托盘 / 前后对比 / 系统局部 / 沉淀池 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：噜噜在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art, structure, objects, and primary text. Warm yellow-orange only for 噜噜's body and identity marks. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense explainer, meme, avatar, sticker sheet, or children's illustration. Invent a fresh warm and calm visual metaphor for this specific article. It should be clear but not instructional, gentle but not childish, strange but clean.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: Lulu character, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强噜噜参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 噜噜 central to the conceptual action. 噜噜 should physically hold, buffer, push, carry, soak, support, or slowly move the key idea through the structure, not stand beside the diagram. Keep the clean white hand-drawn style, sparse Chinese labels, and warm yellow-orange Lulu identity.
```

降低表情包感：

```text
Regenerate this illustration with less mascot energy and more article-body illustration feeling. Keep 噜噜 calm, slow, blank-faced, and useful to the structure. Reduce oversized head, exaggerated emotion, decorative hearts, stickers, cute props, and poster-like composition. Preserve the core idea and 16:9 white hand-drawn layout.
```

修正颜色和背景：

```text
Edit or regenerate with a pure white background, black hand-drawn line art, warm yellow-orange only on 噜噜, and sparse red/orange/blue handwritten Chinese annotations. Remove gradients, paper texture, shadows, dense color fills, and commercial vector styling.
```
