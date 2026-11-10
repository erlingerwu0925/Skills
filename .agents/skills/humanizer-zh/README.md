# Humanizer-ZH 🇨🇳

> **消除中文文本中的“AI味”（大模型腔、机器翻译腔、互联网黑话套话、模板化八股、空洞宏大叙事），重写为地道、自然、有血有肉的人类语言。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0.0--cn-orange.svg)](SKILL.md)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Ready-success.svg)](SKILL.md)
[![Compatible With](https://img.shields.io/badge/Compatible-Claude_Code_|_Codex_|_Antigravity_|_WorkBuddy_|_Cursor-8A2BE2.svg)](README.md)

---

## 💡 为什么需要 Humanizer-ZH？

各大主流大模型（如 GPT-5.6 / GPT-5 系列、Claude 4.x / 4.5 系列、Gemini 3.x 系列、DeepSeek 最新系列等）在生成中文文本时，往往伴随着极其明显且令人审美疲劳的 **“AI 味”**：

1. **大词轰炸 & 职场黑话**：动辄“赋能”、“打通闭环”、“底层逻辑”、“抓手”、“协同效应”、“构建护城河”、“多维度深层次”。
2. **过度夸大 & 虚假里程碑**：一件普通的小事被描绘为“标志着重要转折点”、“具有里程碑意义”、“谱写了崭新篇章”。
3. **欧化翻译腔 & 恶性被动句**：通篇“被广泛认为”、“被赋予”、“随着……对于……通过……”句首病，长修饰语与连环“的”字。
4. **格式与排版八股**：通篇由 `- **加粗小标题：** 内容` 机械清单组成，毫无段落呼吸感；到处堆砌 Emoji（🚀💡🔥📌✨）。
5. **对话机器人残留 & 鸡汤凤尾**：“好的！这是一个深刻的问题”、“希望以上内容对您有所帮助！”、“在时代的洪流中唯有拥抱变化方能行稳致远，让我们拭目以待！”。

**Humanizer-ZH** 基于维基百科 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) 项目，针对**国内中文语言习惯、互联网/职场语境、中文自媒体生态及欧化翻译腔**进行了全面重构与扩充。

---

## 🎯 核心原则

- 🛡️ **去味不改意（Meaning Preservation）**：完整保留原文本中的**所有事实、数据、专有名词、逻辑关系与结论**，严禁篡改原意。
- 🚫 **严禁脑补（Zero Hallucination）**：绝不凭空增加未经证实的细节、数据、人名、时间或信源。
- 🎙️ **声调自适应（Voice Matching）**：支持用户传入个人的**写作样本**，优先拟合作者原有的句式长短、标点偏好与行文语气。
- 📂 **文件级安全（File Safe）**：处理 Markdown / 文档时，**严格保护**代码块、Frontmatter YAML 元数据、内联代码及链接 URL 不被破坏。

---

## 🚀 快速安装

### 1. 一键安装（通用 Skills CLI）

```bash
npx skills add nothing0here/humanizer-zh --global
```

### 2. 各主流 AI 编程助手与 Agent 安装

#### 🔹 Antigravity / Gemini CLI
```bash
mkdir -p ~/.gemini/config/skills/humanizer
curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.gemini/config/skills/humanizer/SKILL.md
```

#### 🔹 Codex
```bash
mkdir -p ~/.codex/skills/humanizer
curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.codex/skills/humanizer/SKILL.md
```

#### 🔹 WorkBuddy / WorkBuddy AI
```bash
mkdir -p ~/.workbuddy-ai/skills/humanizer ~/.workbuddy/skills/humanizer
curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.workbuddy-ai/skills/humanizer/SKILL.md
curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.workbuddy/skills/humanizer/SKILL.md
```

#### 🔹 Claude Code
```bash
mkdir -p ~/.claude/skills/humanizer
curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.claude/skills/humanizer/SKILL.md
```

#### 🔹 Cursor / Windsurf / Roo Code / Cline
将 `SKILL.md` 的内容添加到项目的 `.cursorrules`、`.windsurfrules` 或通用系统提示词（System Prompt）中即可。

---

## 📖 使用指南

### 1. 基础调用

直接在对话框中调用技能或粘贴需要去 AI 味的文字：

```markdown
/humanizer

请帮我把下面这段文案去一下 AI 味：
[粘贴你的文本]
```

### 2. 声调拟合（Voice Matching，推荐 ⭐⭐⭐⭐⭐）

提供 1~2 段你自己平时手写的真实文字，AI 将完美复刻你的写作习惯与呼吸感：

```markdown
/humanizer

这是我平时的写作样本：
[粘贴 1-2 段你自己的真实文字]

现在请根据我的语气风格润色这段内容：
[粘贴需要润色的 AI 文本]
```

### 3. 文件就地润色（File Mode）

指定文件路径，直接安全替换正文段落（代码块、配置元数据、链接保持完好）：

```markdown
humanize docs/announcement.md
```

---

## 🎨 四大中文场景定制规范

| 场景 | 调优核心 | 重点动作 |
| :--- | :--- | :--- |
| **A. 自媒体 / 公众号 / 专栏 / 随笔** | 真实感、有温度、好读 | 多用短句与口语化转折；保留主观感受与具象细节；彻底消除官话大词与鸡汤结尾。 |
| **B. 职场公文 / 汇报 / PRD / 方案** | 严谨干练、结论先行、落地 | 用具体动作与量化指标替代“赋能/闭环”；逻辑紧凑；拿掉一切空洞口号。 |
| **C. 技术博客 / 开发文档 / 开源说明** | 极简、精准、即查即用 | 开门见山交代配置与原理；保留准确术语；代码块/参数/链接绝对不变。 |
| **D. 日常沟通 / 邮件 / IM 消息** | 效率第一、得体克制 | 第一句直接给结论与待办；剔除客服式寒暄与谄媚客套。 |

---

## 📊 改写对照示例

### 案例 1：产品/商业文案

* **❌ AI 味原稿**：
  > 在数字化转型纵深推进的时代背景下，XX云原生开发平台作为一款革命性的生产力工具，凭借其卓越的架构设计，全方位赋能企业研发全链路。平台不仅打破了传统开发模式中的信息孤岛，实现了团队间深层次的协同效应，更通过引入智能化调度算法，打造了从代码编写到自动部署的敏捷闭环。可以说是企业构建核心技术护城河的里程碑式飞跃。展望未来，XX平台必将持续引领行业发展潮流，谱写数字创新的璀璨篇章！🚀✨
* **✅ Humanizer-ZH 润色后**：
  > XX 云原生开发平台主要针对团队协作和持续交付做了优化。它集成了代码编写与自动部署流水线，并采用自动化调度算法分配计算资源，减少了跨部门沟通与手动配置环境的时间，让项目交付速度明显提升。

---

### 案例 2：个人旅游与生活随笔

* **❌ AI 味原稿**：
  > 刚刚结束了为期三天的成都之旅，不得不说，这座充满烟火气与深厚历史底蕴的城市彻底俘获了我的心。漫步在宽窄巷子，历史与现代在此交织碰撞。当然，不得不提的还有地道美食，每一口都是对味蕾的极致犒赏。那么，成都最吸引人的究竟是什么？答案其实藏在人民公园的一杯盖碗茶里。成都不仅是一个旅游胜地，更是一种生活态度的生动写照。如果你也渴望逃离都市的喧嚣，不妨背起行囊，来这里开启一段治愈心灵的旅程吧！💡✨
* **✅ Humanizer-ZH 润色后**：
  > 在成都呆了三天，印象最深的倒不是景点，而是人民公园里喝茶晒太阳的大爷大妈。宽窄巷子游客很多，两边的老房子翻修得很整齐，商业气息稍重了些，不过沿街的蛋烘糕和火锅味道确实在线。下午在茶馆要了碗十块钱的盖碗茶，旁边桌在聊家常，整个人一下子松弛下来了。比起赶景点打卡，空出一个下午随便找家茶馆坐坐更有意思。

---

## 🤝 参与贡献

欢迎提交 Issue 和 Pull Request！如果你发现了新的中文大模型高频套话或特定场景的优化需求，欢迎一同完善。

## 📄 开源许可证

本项目基于 [MIT License](LICENSE) 开源。
