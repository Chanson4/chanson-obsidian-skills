---
name: chanson-mistakes
description: organize original wrong questions, wrong answers, practice records, and mistake discussions into reviewable mistake-note drafts. use when the user asks to maintain a mistake notebook, preserve the original question, preserve the user's wrong answer or wrong reasoning, analyze direct and deep causes, link related knowledge points, identify traps, generate transfer reminders, review questions, or hand content to an obsidian skill for final formatting and writing.
---

# Chanson Mistakes

## Purpose

Transform raw wrong questions into reviewable mistake notes.

Use this skill for single wrong questions, batches of mistakes, AI discussions about mistakes, and mistake notebook maintenance. A mistake is not just a wrong answer; it is evidence of a knowledge gap, misconception, or failed recognition pattern.

Read `references/chanson-library-protocol.md` for shared Chanson library conventions.

## Core Principle

Preserve the original question and the user's wrong answer or wrong reasoning. Then explain the correct method and convert the mistake into future prevention rules.

## Workflow

1. Identify subject, chapter, topic, question type, and available information.
2. Preserve the original question as completely as possible.
3. Preserve the user's wrong answer, wrong reasoning, or original confusion.
4. Identify the correct answer. If missing, infer only when safe and mark uncertainty.
5. Reconstruct the correct solution process.
6. Analyze the direct cause of the mistake.
7. Analyze the deeper knowledge gap or misconception.
8. Link the mistake to related knowledge points.
9. Identify the trap, misleading condition, or failed recognition pattern.
10. Generate transfer reminders, next-time steps, and review questions.
11. Prepare a handoff section for an Obsidian skill to format and write into the mistake notebook.

## Required Mistake Note Format

Use this structure unless the user asks otherwise:

- Title: 错题整理：{{题目主题}}
- 目标信息: subject, chapter, question type, target mistake notebook, handoff note
- 原题: preserve the original question
- 我的错误答案 / 错误思路: preserve the user's wrong answer or reasoning
- 正确答案: provide or infer carefully
- 正确解法: show reasoning, not only the answer
- 错因分析: separate direct cause and deep cause
- 涉及知识点: list related knowledge points
- 易错陷阱: identify traps and misleading conditions
- 举一反三: explain transfer to similar questions
- 下次遇到这类题的判断步骤: give operational steps
- 复盘问题: active recall questions
- 建议交给 Obsidian Skill 的格式任务: tags, wikilinks, callouts, final insertion

## Missing Information Rules

- If the correct answer is missing, say it is not explicitly provided and infer only when safe.
- If the user's reasoning is missing, preserve the wrong option or answer and mark reasoning as unknown.
- If the original question is incomplete, proceed with best effort unless the missing part prevents meaningful analysis.

## Batch Mistake Summary

For multiple mistakes, also add:

- 高频错因。
- 反复混淆的知识点。
- 下一轮复习优先级。
- 可用于 Chanson Practice 的针对性出题方向。

## Quality Checklist

Before finalizing, verify:

- The original question is preserved.
- The user's wrong answer or wrong reasoning is preserved.
- Correct reasoning is explained.
- Direct and deep causes are separated.
- Related knowledge points are listed.
- Traps and transfer rules are included.
- Review questions are generated.
- Obsidian formatting is prepared as a handoff, not fully duplicated.
