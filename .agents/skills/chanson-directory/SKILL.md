---
name: chanson-directory
description: create learning vault directory structures and markdown skeleton files from user-provided folder and file hierarchies. use when the user asks to create obsidian vault folders, subject directories, chapter note frameworks, mistake notebooks, practice folders, raw dialogue folders, or template markdown files. this skill creates safe directory structures and basic placeholders while leaving advanced obsidian formatting and final style maintenance to an obsidian skill.
---

# Chanson Directory

## Purpose

Create and verify learning-focused vault directory structures from a user's requested hierarchy.

Use this skill for folders, `.md` files, chapter-note shells, mistake-book folders, practice-question folders, raw-dialogue archives, and other study-vault scaffolding. Do not use this skill to deeply format finished Obsidian notes; hand advanced formatting to an Obsidian skill.

Read `references/chanson-library-protocol.md` for shared Chanson library conventions.

## Workflow

1. Identify the vault path and target root directory.
2. Parse the user's hierarchy exactly.
3. Treat paths ending in `.md` as Markdown files.
4. Treat paths without a file extension as folders unless the user says otherwise.
5. Create missing parent folders automatically.
6. Never overwrite existing files unless the user explicitly requests overwrite.
7. For new Markdown files, insert only a title and requested placeholder headings.
8. Return a creation report with created folders, created files, skipped paths, and errors.

## Safety Rules

- Preserve Chinese names, numbering, and chapter labels exactly.
- Do not delete, rename, or overwrite existing files unless explicitly requested.
- If the hierarchy is ambiguous, infer conservatively and report the assumptions.
- If the current environment cannot access the user's filesystem, output a JSON or tree plan that the user can run locally.

## Optional Script

For deterministic local creation, use `scripts/create_vault_structure.py`. It accepts a JSON spec with:

```json
{
  "vault_path": "/path/to/vault",
  "root": "考研/408/计算机组成原理",
  "items": [
    {"type": "folder", "path": "章节笔记"},
    {"type": "file", "path": "章节笔记/第3章 存储系统.md", "template": "# 第3章 存储系统\n\n## 核心知识点\n"}
  ],
  "overwrite": false
}
```

Run:

```bash
python scripts/create_vault_structure.py spec.json
```

## Report Format

```markdown
## 目录创建报告

### 已创建文件夹
- ...

### 已创建文件
- ...

### 已存在，已跳过
- ...

### 创建失败
- ...

### 后续交给 Obsidian Skill 的任务
- 维护 frontmatter、tags、wikilinks、callouts 和 vault 风格一致性。
```
