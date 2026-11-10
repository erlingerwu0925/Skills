# 上游来源 / Attribution

本仓库的第三方 Skill 来自下列公开项目，保留各 Skill 自带许可证和配套文件。
同步流程：GitHub Actions → `Install eight writing skills`；也可以执行 `bash scripts/sync-skills.sh`。同步后在 `UPSTREAM_VERSIONS.txt` 记录对应上游 Git commit。

| 本仓库技能目录 | 上游仓库和相对路径 | 用途 |
|---|---|---|
| `humanizer-chinese` | https://github.com/jiji262/humanizer-chinese | 中文去 AI 味 |
| `humanizer-zh` | https://github.com/nothing0here/humanizer-zh | 中文自然润色 |
| `general-writing` | https://github.com/msimchowitz/writing-skills/tree/main/for-agents/general-writing | 综合写作编辑 |
| `academic-voice` | https://github.com/msimchowitz/writing-skills/tree/main/for-agents/academic-voice | 学术表达 |
| `professional-proofreader` | https://github.com/sickn33/agentic-awesome-skills/tree/main/skills/professional-proofreader | 全文校对 |
| `scientific-writing` | https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing | 科研写作与证据核验 |
| `plain-writing` | https://github.com/docwriter-org/plain-writing-skill/tree/main/skills/plain-writing | 清晰简练写作 |
| `docx` | https://github.com/anthropics/skills/tree/main/skills/docx | Word 文档处理 |

## 安装与注意事项

目录 `.agents/skills` 适用于以本仓库作为工作仓库的 Codex。其他项目请复制这八个子目录到目标项目的 `.agents/skills`，或个人目录 `~/.agents/skills`。Skill 提供的是操作指令与辅助脚本，并不意味着外部运行环境已安装 Python 包、LibreOffice 或其他必要依赖。运行外部脚本前请检查源码与依赖，并依据上游要求安装。Skill 是第三方内容，不代表 OpenAI 的官方认可。
