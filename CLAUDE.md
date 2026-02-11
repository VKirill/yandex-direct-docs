# Yandex Direct Documentation

This repository contains the complete Yandex Direct documentation (509 articles) in Markdown format.

## Project Structure

```
docs/                          # 509 markdown articles organized by section
.claude/skills/yandex-direct/  # Agent Skill for AI assistants
.claude/agents/                # Custom agents for Yandex Direct consulting
scripts/                       # Scraping and cleanup utilities
context7.json                  # Context7 MCP configuration
SKILL.md                       # Standalone skill file (copy for quick use)
```

## Working With This Repo

- All documentation is in `docs/` — search with `grep -r "keyword" docs/`
- Each file has `source:` front matter with original URL
- Internal links use relative paths (`../section/file.md`)
- Language: Russian

## Available Agents

- **yandex-direct-consultant** — answers questions about Yandex Direct using the documentation

## Available Skills

- **yandex-direct** — reference skill with full documentation navigation map

## Rules

- When answering questions, always cite the source file path
- Answer in Russian unless the user writes in another language
- If the documentation doesn't cover the question, say so explicitly
- Do not invent information — only use what's in the docs
