# Chanson Skills Library

<p align="center">
  <a href="#中文说明">中文</a> |
  <a href="#english">English</a>
</p>

## 中文说明

Chanson Skills Library 是一组面向学习复盘、Obsidian 知识库和 Codex 工作流的技能集合。它的目标不是简单总结聊天记录，而是把学习过程中的提问、困惑、错因、推理过程和复习价值沉淀成可长期维护的学习材料。

本仓库包含 4 个相互独立但可以组合使用的 skills：

- `chanson-directory`：创建学习仓库目录、章节笔记框架、错题本目录和练习题目录。
- `chanson-notes`：将 AI 学习对话、课程讨论或导出的聊天记录精炼成学习笔记草稿。
- `chanson-mistakes`：将错题、错误答案、错误思路和复盘讨论整理成可复习的错题笔记草稿。
- `chanson-practice`：根据章节笔记、错题本、薄弱知识点生成针对性练习题。

### 推荐使用环境

建议在使用 Chanson skills 的环境中同时存在 `obsidian-skills` 这一 skill。

Chanson skills 主要负责学习内容质量、结构化整理、错因分析和练习题设计；`obsidian-skills` 更适合负责最终的 Obsidian 格式维护，例如：

- frontmatter
- tags
- wikilinks
- callouts
- embeds
- 笔记追加位置
- vault 内部风格一致性

推荐协作方式：

```text
Chanson 负责内容理解与学习结构
↓
obsidian-skills 负责 Obsidian 格式与写入
↓
最终进入你的 Obsidian 学习仓库
```

如果环境中没有 `obsidian-skills`，Chanson 仍然可以输出干净的 Markdown 草稿，但最终写入 Obsidian 时的格式一致性、链接关系和 vault 风格需要人工处理。

### 安装方式

将本仓库中的 `.agents/skills` 目录复制到你的 Codex 项目或本地 skills 目录中。

项目结构：

```text
.agents/
└── skills/
    ├── chanson-directory/
    ├── chanson-notes/
    ├── chanson-mistakes/
    └── chanson-practice/
```

也可以只复制其中某一个 skill，例如只安装 `chanson-notes` 用于学习对话精炼。

### Skill 介绍

#### chanson-directory

用于创建学习仓库目录结构和 Markdown 框架文件。

适合场景：

- 创建 Obsidian 学习仓库目录。
- 创建科目目录、章节笔记、错题本目录。
- 根据用户给出的目录树批量创建文件夹和 `.md` 文件。
- 创建原始对话记录、练习题、复盘笔记等分类目录。

它会尽量安全地操作文件系统：

- 保留中文名称、章节编号和用户给出的路径。
- 自动创建缺失的父目录。
- 默认不覆盖已有文件。
- 对新建 Markdown 文件只写入基础标题和占位结构。

典型请求：

```text
按这个目录创建数学笔记目录，格式跟计组笔记一样。
```

#### chanson-notes

用于把 AI 学习对话精炼成高质量学习笔记草稿。

它强调保留学习者真实问题，因为原始提问通常暴露了真正的理解障碍。整理时不会只摘抄 AI 回答，而是会重构：

- 用户原始问题
- 问题背后的真实困惑
- 对应知识点
- 为什么是这样
- 推理链、例子、类比、计算过程
- 易错点与纠偏
- 考研或考试中的常见考法
- 复习问题

适合场景：

- 将 ChatGPT、Codex、Claude 等学习对话整理为笔记。
- 精炼章节学习记录。
- 保留关键例子和理解过程，而不是只留下概念定义。
- 生成可交给 `obsidian-skills` 写入 vault 的笔记草稿。

典型请求：

```text
这是我在计组3-6节学习中与AI的对话记录，请精炼知识点，但要保留关键过程，避免只存在知识点没有解释的情况，将精炼后的笔记存入对应章节的计组笔记。
```

#### chanson-mistakes

用于把错题整理成可复习、可迁移的错题笔记草稿。

它不会只记录“正确答案”，而是把错题当成一次知识漏洞暴露，重点整理：

- 原题
- 我的错误答案或错误思路
- 正确答案
- 正确解法
- 直接错因
- 深层知识漏洞
- 相关知识点
- 易错陷阱
- 举一反三
- 下次遇到同类题的判断步骤
- 复盘问题

适合场景：

- 把截图题、错题讨论、原始题干加入错题本。
- 维护考研数学、408、英语等科目的错题复盘。
- 从错题中提炼下一轮复习优先级。
- 为 `chanson-practice` 提供针对性出题依据。

典型请求：

```text
把这几题加入计组错题，章节为3.6。
```

#### chanson-practice

用于从笔记、错题、薄弱点或指定章节生成针对性练习题。

它强调练习题应该来自用户真实的学习材料，而不是随机生成。可以控制：

- 题目数量
- 难度
- 题型
- 科目和章节
- 知识点范围
- 是否包含答案
- 是否包含详细解析
- 是否写入 vault

支持的难度倾向：

- 基础：概念定义、直接判断、简单应用。
- 中等：一到两步推理，标准考试题。
- 偏难：多步推理、陷阱识别、知识点组合。
- 真题难度：贴近考研真题风格和难度。
- 拔高：用于强化迁移能力的提高题。

典型请求：

```text
根据计组3.5的错题和笔记，生成10道中等难度选择题，带答案和解析。
```

### 推荐工作流

#### 1. 创建学习仓库结构

```text
使用 chanson-directory
↓
创建科目、章节、错题、练习题目录
↓
交给 obsidian-skills 维护 frontmatter、tags 和链接规范
```

#### 2. 整理学习对话

```text
使用 chanson-notes
↓
提取原始疑问、理解过程、例子和易错点
↓
交给 obsidian-skills 写入对应章节笔记
```

#### 3. 整理错题

```text
使用 chanson-mistakes
↓
保留原题、错误思路、正确解法和错因分析
↓
交给 obsidian-skills 写入错题本
```

#### 4. 生成针对性练习

```text
使用 chanson-practice
↓
从笔记或错题中提炼薄弱点并生成练习
↓
交给 obsidian-skills 写入练习题目录
```

### 设计原则

- 保留学习者的真实问题。
- 不做机械摘要，要解释从困惑到理解的过程。
- 不只写答案，要保留关键推理和典型例子。
- 错题整理要区分直接错因和深层知识漏洞。
- 练习题要来自真实笔记、错题和薄弱点。
- Obsidian 最终格式交给 `obsidian-skills`，Chanson 专注学习内容。

### 适合人群

- 使用 Obsidian 做长期学习管理的人。
- 使用 Codex 辅助整理笔记、错题和练习题的人。
- 备考考研、408、数学、英语或其他需要长期复盘的学习者。
- 希望把 AI 对话转化为稳定知识资产的人。

---

## English

Chanson Skills Library is a learning-focused skill set for Codex, Obsidian vaults, study notes, mistake reviews, and targeted practice. It is designed to turn real learning conversations, confusion, wrong answers, and reasoning paths into durable study materials.

This repository contains 4 independent skills that can also work together:

- `chanson-directory`: creates learning vault folders, chapter note skeletons, mistake notebook folders, and practice folders.
- `chanson-notes`: distills AI learning dialogues, course discussions, or exported chat records into study-note drafts.
- `chanson-mistakes`: turns wrong questions, wrong answers, and mistake discussions into reviewable mistake-note drafts.
- `chanson-practice`: generates targeted practice questions from notes, mistake notebooks, weak points, or selected chapters.

### Recommended Environment

It is strongly recommended to have the `obsidian-skills` skill available in the same environment when using Chanson skills.

Chanson skills focus on learning-content quality, structure, mistake analysis, and practice design. `obsidian-skills` should handle the final Obsidian-specific layer, such as:

- frontmatter
- tags
- wikilinks
- callouts
- embeds
- insertion location
- vault style consistency

Recommended collaboration:

```text
Chanson handles learning content and structure
↓
obsidian-skills handles Obsidian formatting and writing
↓
Final content enters your Obsidian study vault
```

If `obsidian-skills` is not available, Chanson can still produce clean Markdown drafts, but final Obsidian formatting, links, tags, and vault conventions may need to be handled manually.

### Installation

Copy the `.agents/skills` folder from this repository into your Codex project or local skills directory.

Repository layout:

```text
.agents/
└── skills/
    ├── chanson-directory/
    ├── chanson-notes/
    ├── chanson-mistakes/
    └── chanson-practice/
```

You can also copy only the skill you need. For example, install only `chanson-notes` if you only want to process learning conversations.

### Skill Details

#### chanson-directory

Creates learning vault directory structures and Markdown skeleton files.

Best for:

- Creating Obsidian study vault structures.
- Creating subject folders, chapter notes, and mistake notebooks.
- Creating folders and `.md` files from a user-provided directory tree.
- Creating folders for raw dialogues, practice sets, and review notes.

Safety behavior:

- Preserves Chinese names, numbering, and chapter labels.
- Creates missing parent folders automatically.
- Does not overwrite existing files by default.
- Writes only basic titles and placeholder headings into new Markdown files.

Example request:

```text
Create a math note directory using this structure, and keep the format consistent with my computer organization notes.
```

#### chanson-notes

Distills AI-assisted learning dialogues into high-quality study-note drafts.

It preserves the learner's original questions because those questions reveal the real confusion. Instead of only summarizing an AI response, it reconstructs:

- original user questions
- underlying confusion
- related knowledge points
- why the conclusion is true
- reasoning chains, examples, analogies, and calculations
- misconceptions and corrections
- exam-facing points
- review questions

Best for:

- Turning ChatGPT, Codex, Claude, or other AI learning conversations into notes.
- Refining chapter learning records.
- Preserving examples and reasoning instead of keeping only concepts.
- Producing a draft that can be handed to `obsidian-skills` for vault insertion.

Example request:

```text
This is my AI dialogue while studying Chapter 3.6 of Computer Organization. Please refine the knowledge points, preserve the key reasoning process, avoid leaving only bare concepts, and write the refined notes into the corresponding chapter note.
```

#### chanson-mistakes

Turns wrong questions into reviewable mistake-note drafts.

It treats mistakes as evidence of knowledge gaps, misconceptions, or failed recognition patterns. It records:

- original question
- user's wrong answer or wrong reasoning
- correct answer
- correct solution process
- direct mistake cause
- deeper knowledge gap
- related knowledge points
- traps and misleading conditions
- transfer rules
- next-time decision steps
- review questions

Best for:

- Adding screenshot questions or raw wrong questions to a mistake notebook.
- Maintaining mistake reviews for math, CS408, English, or other exam subjects.
- Extracting review priorities from repeated mistakes.
- Providing source material for `chanson-practice`.

Example request:

```text
Add these questions to my Computer Organization mistake notebook, chapter 3.6.
```

#### chanson-practice

Generates targeted practice questions from notes, mistake notebooks, weak points, or selected chapters.

Practice questions should not be random. They should come from the user's actual learning material and weak areas. Supported controls include:

- question count
- difficulty
- question type
- subject and chapter
- knowledge point range
- whether to include answers
- whether to include detailed explanations
- whether to write into the vault

Difficulty levels:

- Basic: definitions, direct checks, simple applications.
- Medium: one or two reasoning steps, standard exam-style questions.
- Hard: multi-step reasoning, traps, combined knowledge points.
- Past-exam level: close to postgraduate entrance exam style and difficulty.
- Advanced: transfer questions for stronger mastery.

Example request:

```text
Based on my Chapter 3.5 notes and mistake notebook, generate 10 medium-difficulty multiple-choice questions with answers and explanations.
```

### Recommended Workflow

#### 1. Create a learning vault structure

```text
Use chanson-directory
↓
Create subject, chapter, mistake, and practice folders
↓
Let obsidian-skills maintain frontmatter, tags, and link conventions
```

#### 2. Refine learning dialogues

```text
Use chanson-notes
↓
Extract original questions, reasoning paths, examples, and misconceptions
↓
Let obsidian-skills write the content into the target chapter note
```

#### 3. Organize mistakes

```text
Use chanson-mistakes
↓
Preserve original questions, wrong reasoning, correct solution, and mistake causes
↓
Let obsidian-skills write the content into the mistake notebook
```

#### 4. Generate targeted practice

```text
Use chanson-practice
↓
Extract weak points from notes and mistakes, then generate exercises
↓
Let obsidian-skills write the practice set into the practice folder
```

### Design Principles

- Preserve the learner's real questions.
- Explain the path from confusion to understanding.
- Keep key reasoning and typical examples, not only final concepts.
- Separate direct mistake causes from deeper knowledge gaps.
- Generate practice from real notes, mistakes, and weak points.
- Let `obsidian-skills` own final Obsidian formatting while Chanson focuses on learning content.

### Who This Is For

- Learners who maintain long-term study systems in Obsidian.
- Codex users who want structured notes, mistake notebooks, and practice sets.
- Students preparing for postgraduate entrance exams, CS408, math, English, or similar long-cycle exams.
- Anyone who wants to turn AI learning conversations into stable knowledge assets.

