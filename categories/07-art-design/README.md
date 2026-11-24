# 07｜艺术设计

本分类用于高级海报、策展前言与后记、校园作品展、大尺寸印刷和可编辑中文长文排版。以下六项 Skill 的原始 SKILL.md 和许可已经存入 `.agents/skills/`，可在 Codex 项目中识别。

| Skill | 主要用途 | Codex 调用入口 |
|---|---|---|
| poster-design | 大型海报构图、可编辑印刷规范 | [SKILL.md](../../.agents/skills/poster-design/SKILL.md) |
| poster-style-transfer | 参考海报的风格提取与原创迁移 | [SKILL.md](../../.agents/skills/poster-style-transfer/SKILL.md) |
| poster-generator | 20种海报风格与版式 | [SKILL.md](../../.agents/skills/poster-generator/SKILL.md) |
| academic-poster | 大型可编辑PPTX及文字测量 | [SKILL.md](../../.agents/skills/academic-poster/SKILL.md) |
| impeccable | 视觉层级、字体和排版精修 | [SKILL.md](../../.agents/skills/impeccable/SKILL.md) |
| canvas-design | 原创视觉构图与艺术创作 | [SKILL.md](../../.agents/skills/canvas-design/SKILL.md) |

## 曲江第二学校作品展的工作流

1. 使用 `poster-style-transfer` 分析美术馆参考，提取布局语言，不复制原海报。
2. 使用 `poster-design` 设计正文与标题层级；长篇可编辑正文交给 `academic-poster` 处理。
3. 使用 `impeccable` 反复审查字体、留白、尺寸与阅读顺序。
4. 使用 `canvas-design` 制作原创背景，`poster-generator` 提供多风格草案。
5. 通过可编辑 PPTX / HTML 转入 Canva，复核内容、字体替换与物理印刷尺寸。

> 注意：Skill 是指令与辅助资源，不等于其引用的外部软件、图像模型、字体和环境已安装。不能保证将生成的扁平图片变成可编辑图层。
