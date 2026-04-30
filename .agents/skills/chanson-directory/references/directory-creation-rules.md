# Directory Creation Rules

## Required behavior

- Follow the user's hierarchy exactly.
- Create parent folders before child files.
- `.md` means Markdown file.
- No extension means folder by default.
- Existing folders are safe and should be reported as skipped or already present.
- Existing files must not be overwritten by default.
- New Markdown files should contain a title based on the filename and user-requested placeholder headings.

## Template defaults

For chapter notes, use headings such as:

```markdown
# {{chapter title}}

## 核心知识点

## 易错点

## 典型题型

## 复习问题
```

For mistake notebooks:

```markdown
# {{subject}} 错题本

## 错题索引

## 高频错因

## 待复盘题目
```

For practice folders, create only a folder unless the user requests a file template.
