# Writing Skills for Codex / 中文写作技能库

本仓库用于在 Codex 项目中安装和管理第三方写作 Skills（中文去 AI 味、语言润色、学术写作、校对、Word 编辑）。

技能目录：`.agents/skills/<skill-name>/SKILL.md`。

安装后可在 Codex 中使用 `$skill-name` 显式调用；也可将本仓库中的 `.agents/skills/` 复制到其他项目，或者复制到个人目录 `~/.agents/skills/`。网页 Codex 需要将本仓库用作项目或将技能同步到所工作的仓库，单独存在这个仓库不会自动影响其他仓库。

## GitHub Actions 说明

这八个 Skill 已经直接提交到仓库，不需要运行自动安装任务。`Actions → Verify eight writing skills → Run workflow` 可按需**手动校验** `SKILL.md`、关键配套资料与 Python 脚本的语法。该工作流不会联网更新技能，也不会自动修改或推送仓库，避免同步期间出现 Git 提交冲突。

这些技能来自独立第三方项目，并非本仓库原创；请遵守各技能附带的许可证。具体来源见 `SOURCES.md`。

## 质量提醒

去 AI 味应改进文字质量与可读性，不能用于捏造事实、伪造文献或承诺绕过 AI 检测。写作技能应保留事实、引文、数据和原意。科学写作的参考资料与验证脚本不能代替人工核实。
