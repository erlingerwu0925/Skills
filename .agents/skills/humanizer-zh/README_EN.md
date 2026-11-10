# Humanizer-ZH 🇨🇳

> **Eliminate AI writing patterns, translationese, repetitive buzzwords, and chatbot clichés from Chinese text, rewriting it into natural, authentic, human-sounding Chinese.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0.0--cn-orange.svg)](SKILL.md)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Ready-success.svg)](SKILL.md)

---

## Overview

Modern LLMs (such as GPT-5.6 / GPT-5 series, Claude 4.x / 4.5, Gemini 3.x, DeepSeek, etc.) often generate Chinese text with heavy "AI flavor" — translationese, repetitive corporate buzzwords, excessive lists with bold colons, artificial emotional climaxes, and robotic courtesies.

**Humanizer-ZH** is adapted and heavily expanded from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) to deeply target domestic Chinese writing contexts across workplace proposals, social media/columns, technical blogs, and daily communications.

## Key Principles

1. **Meaning Preservation**: Keep 100% of facts, data, terms, claims, and logic intact.
2. **Zero Hallucination**: Never invent names, dates, stats, or citations.
3. **Voice Matching**: If the user provides a writing sample, prioritize matching the author's authentic rhythm, punctuation, and phrasing style.
4. **File Safety**: Code blocks, YAML frontmatter, inline code, and URLs remain completely untouched.

## Installation

### Via Skills CLI
```bash
npx skills add nothing0here/humanizer-zh --global
```

### Manual Installation (Antigravity / Codex / WorkBuddy / Claude Code)
```bash
# Antigravity / Gemini CLI
mkdir -p ~/.gemini/config/skills/humanizer && curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.gemini/config/skills/humanizer/SKILL.md

# Codex
mkdir -p ~/.codex/skills/humanizer && curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.codex/skills/humanizer/SKILL.md

# WorkBuddy
mkdir -p ~/.workbuddy-ai/skills/humanizer && curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.workbuddy-ai/skills/humanizer/SKILL.md

# Claude Code
mkdir -p ~/.claude/skills/humanizer && curl -sSL https://raw.githubusercontent.com/nothing0here/humanizer-zh/main/SKILL.md > ~/.claude/skills/humanizer/SKILL.md
```

## License

[MIT License](LICENSE)
