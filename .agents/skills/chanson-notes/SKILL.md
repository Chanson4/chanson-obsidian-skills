---
name: chanson-notes
description: distill ai learning dialogues, chatgpt codex claude markdown records, study conversations, and course discussion notes into high-quality study note drafts. use when the user asks to refine learning dialogue, preserve original user questions, identify the underlying confusion, explain knowledge points with reasoning, generate misconceptions, exam-facing points, review questions, or hand content to an obsidian skill for final formatting and vault insertion.
---

# Chanson Notes

## Purpose

Turn AI-assisted learning dialogues into durable study-note drafts.

Use this skill when the input is a learning conversation, exported AI chat Markdown, or study discussion record. The goal is not to summarize mechanically. Preserve the learner's original questions and reconstruct the reasoning that changed confusion into understanding.

Read `references/chanson-library-protocol.md` for shared Chanson library conventions.

## Core Principle

The user's original questions are high-value learning material. They reveal the learner's real confusion and must be preserved.

Do not only summarize the AI's answer. For each important knowledge point, identify:

- the user's original question;
- the underlying confusion;
- the knowledge point that resolves it;
- the reasoning process;
- examples, analogies, derivations, or corrections;
- misconceptions and exam-facing conclusions.

## Workflow

1. Identify subject, chapter, section, and topic.
2. Extract the user's original questions verbatim where possible.
3. Group original questions by knowledge point.
4. Identify the underlying confusion behind each question.
5. Extract the useful explanation from AI responses.
6. Rewrite the explanation into concise but complete study notes.
7. Preserve key reasoning chains, examples, analogies, calculations, and correction processes.
8. Add misconceptions, exam patterns, review questions, and follow-up questions.
9. Produce a clean content draft and handoff metadata for an Obsidian skill.

## Required Draft Format

```markdown
# Chanson 学习笔记草稿：{{科目}} {{章节}}

## 目标信息

- 科目：
- 章节：
- 建议目标笔记：
- 建议处理方式：交由 Obsidian Skill 进行最终格式维护与写入

## 本次对话解决的核心问题

## 用户原始疑问索引

1. > {{用户原始提问}}
   - 对应知识点：{{知识点}}
   - 问题本质：{{问题本质}}

## 知识点精炼

### {{知识点名称}}

**原始疑问：**
> 用户原问：{{用户在对话中的真实提问}}

**问题本质：**
{{这个问题真正卡住的地方。}}

**核心结论：**
{{知识点结论。}}

**为什么是这样：**
{{解释原因，不要只写结论。}}

**关键理解过程：**
{{推理链、例子、类比、计算过程或纠错过程。}}

**易错点与纠偏：**
{{用户可能混淆或已经混淆的地方。}}

**典型考法：**
{{考试中可能如何考。}}

**复习问题：**
- {{主动回忆问题}}

## 从困惑到理解的路径

## 待追问问题

## 建议交给 Obsidian Skill 的格式任务
- 添加或修正 frontmatter。
- 根据 vault 规范生成 tags。
- 生成必要的 wikilinks。
- 使用 callouts 标记易错点、重要结论和注意事项。
- 将内容追加到对应章节笔记。
```

## Quality Checklist

Before finalizing, verify:

- Original user questions are preserved.
- Each important question is connected to a knowledge point.
- Each conclusion includes a why or reasoning process.
- Misconceptions and corrections are retained.
- The output is concise but not skeletal.
- The output is not a copied transcript.
- Obsidian formatting is prepared as a handoff, not fully duplicated.
