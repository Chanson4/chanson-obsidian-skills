---
name: chanson-practice
description: generate targeted practice questions from selected chapter notes, mistake notebooks, or user-specified knowledge points. use when the user asks to create exercises based on notes, wrong-question patterns, weak points, chapters, or topics, especially with postgraduate entrance exam style, user-specified question count, difficulty, question types, answers, detailed explanations, traps, review points, or an obsidian skill handoff for writing practice sets.
---

# Chanson Practice

## Purpose

Generate targeted practice questions from the user's own notes, mistakes, weak points, or specified knowledge points.

Use this skill when the user asks for practice questions, exam-style training, targeted drills, or exercises based on selected chapters, mistake notebooks, or knowledge points.

Read `references/chanson-library-protocol.md` for shared Chanson library conventions.

## Core Principle

Practice questions should not be random. They should be generated from the user's actual learning materials, weak points, original questions, mistakes, and target knowledge points.

When the user asks for postgraduate entrance exam style, generate original questions that follow the question design patterns, difficulty, traps, and reasoning style of past exam questions. Do not copy real past exam questions unless the user provides them.

## Inputs

Generate questions from:

- selected chapter notes;
- selected mistake notes or mistake notebooks;
- user-specified knowledge points;
- user-specified chapters;
- user-specified weak areas.

## User-Controlled Parameters

Respect the user's parameters:

- question count;
- difficulty;
- question type;
- subject;
- chapter;
- knowledge points;
- whether to include answers;
- whether to include detailed explanations;
- whether to write into the vault.

If the user specifies the number of questions, generate exactly that number. If the user does not specify the number, default to 5 and mention that the count can be customized. If difficulty is missing, default to medium.

## Difficulty Levels

- 基础: definitions, direct concept checks, simple applications.
- 中等: one or two reasoning steps, standard exam-style problems.
- 偏难: multi-step reasoning, traps, combined knowledge points.
- 真题难度: close to postgraduate entrance exam style and difficulty.
- 拔高: harder transfer problems for strengthening.

## Workflow

1. Identify the source: chapter note, mistake notebook, or specified knowledge points.
2. Extract target knowledge points, weak points, misconceptions, and typical exam patterns.
3. Read the user-specified question count.
4. Read the user-specified difficulty; default to medium if absent.
5. Determine the question type mix unless the user specifies it.
6. Generate original questions following postgraduate entrance exam style and difficulty.
7. For each question, include the tested knowledge point and question intent.
8. Provide the answer unless the user asks for questions only.
9. Provide detailed explanation unless the user asks to hide explanations.
10. Add traps, review points, and post-practice reflection questions.
11. Prepare a handoff section for the Obsidian skill to format and write the practice set.

## Required Practice Set Format

Use this structure unless the user asks otherwise:

# 练习题生成：{{科目}} {{章节 / 知识点}}

## 目标信息
- 科目：
- 章节：
- 来源：章节笔记 / 错题本 / 指定知识点
- 知识点范围：
- 题目数量：
- 难度：
- 题型：
- 建议处理方式：交由 Obsidian Skill 进行最终格式维护与写入

## 出题依据

List target knowledge points, weak points, mistakes, and exam-style patterns.

## 练习题

For each question include:

- 题号
- 题型
- 难度
- 考点
- 出题意图
- 题目
- 选项或作答要求
- 答案
- 解析
- 易错陷阱
- 对应复习点

## 本组题复盘建议

Include key training goals, traps to watch, and after-practice self-check questions.

## Source-Specific Rules

### From chapter notes

Cover the chapter structure reasonably: concept understanding, mechanism explanation, calculation/application, misconception identification, and comprehensive application.

### From mistake notebooks

Prioritize repeated weak points, direct mistake causes, deeper misconceptions, similar-question recognition, and trap resistance.

### From specified knowledge points

Create a difficulty gradient unless the user requests otherwise: basic concept, standard application, trap identification, and comprehensive transfer.

## Quality Checklist

Before finalizing, verify:

- The exact requested question count is met.
- Difficulty follows the user's request.
- Questions are tied to notes, mistakes, or specified knowledge points.
- Each question has a clear tested point and intent.
- Answers and explanations are included unless hidden by request.
- Traps and review points are included.
- Obsidian formatting is prepared as a handoff, not fully duplicated.
