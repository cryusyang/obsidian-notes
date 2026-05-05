---
title: "DESIGN.md Specification"
url: "https://www.dsebastien.net/design-md-specification/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> DESIGN.md 是 Google Labs 提出的开源规范（Apache-2.0 许可），旨在通过单个、可版本控制的 Markdown 文件，以 YAML 前置数据（机器可读设计令牌）与 Markdown 正文（人类可读设计依据）结合的方式，向编码智能体精准传递设计系统。它填补了设计到代码之间的语义鸿沟，使 AI 能基于品牌视觉规范（如特定色彩、字体、组件样式）而非通用 UI 框架生成一致界面。该规范处于 Alpha 阶段，与 CLAUDE.md/AGENTS.md 同属静态、仓库驻留的 AI 上下文层，支持导出为 Tailwind 或 DTCG 等格式，并由 Google Stitch 工具作为参考实现。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [DESIGN.md Specification](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DESIGN.md+Specification?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则说明。查看权威版本：[DESIGN.md 规范](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DESIGN.md+Specification?ref=dsebastien.net)。

DESIGN.md is an open Apache-2.0 format specification from [Google Labs](https://github.com/google-labs-code/design.md?ref=dsebastien.net) for describing a design system to [coding agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) in a single, version-controllable file. It pairs **machine-readable design tokens in YAML front matter** with **human-readable design rationale in markdown prose** — so an [LLM](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) can apply visual identity correctly instead of defaulting to generic UI.

DESIGN.md 是由[Google Labs](https://github.com/google-labs-code/design.md?ref=dsebastien.net)提出的、采用开放 Apache-2.0 许可的格式规范，旨在通过单个、可版本控制的文件向[编码智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)描述设计系统。它将 **YAML 文件头中的机器可读设计标记（design tokens）** 与 **Markdown 正文中的、人类可读的设计依据（design rationale）** 相结合——从而使[大语言模型（LLM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)能准确应用视觉识别体系，而非退回到通用 UI 默认样式。

It plays the same role for *design context* that `CLAUDE.md` / `AGENTS.md` plays for *engineering context*: a persistent, structured contract that survives sessions and follows the repo. Currently in **alpha**; the format, schema, and CLI are still moving.

它在 *设计上下文（design context）* 中所扮演的角色，正如同 `CLAUDE.md` / `AGENTS.md` 在 *工程上下文（engineering context）* 中所起的作用：一份持久化、结构化的契约，可跨会话保留，并随代码仓库一同演进。当前处于 **Alpha 阶段**；其格式、模式（schema）及命令行工具（CLI）仍在持续迭代中。

Spec home: [https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification) — [Google Stitch](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net) (Google's AI design tool) is the reference consumer.

规范主页：[https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification) — [Google Stitch](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net)（Google 的 AI 设计工具）是该规范的参考实现消费者。

## File anatomy

## 文件结构

```yaml
---
# YAML front matter — design tokens (machine-readable)
colors:
  primary: "#1a3a52"
  background: "#f7f3ec"
typography:
  headline:
    fontFamily: "Inter"
    fontSize: 48
    fontWeight: 700
spacing:
  scale: [4, 8, 16, 24, 32]
---

## Overview         <- markdown body — design rationale
## Colors
## Typography
## Layout
## Elevation & Depth
## Shapes
## Components
## Do's and Don'ts
```

```yaml
---
# YAML 文件头 — 设计标记（机器可读）
colors:
  primary: "#1a3a52"
  background: "#f7f3ec"
typography:
  headline:
    fontFamily: "Inter"
    fontSize: 48
    fontWeight: 700
spacing:
  scale: [4, 8, 16, 24, 32]
---

## 概览         <- Markdown 正文 — 设计依据
## 颜色
## 字体排印
## 布局
## 高度与景深
## 形状
## 组件
## 最佳实践与禁忌
```

The `##` headings are prescribed and ordered. Tokens cover colors (hex), typography (family/size/weight/lineHeight/letterSpacing), spacing, rounded-corner scales, and component-property mappings.

这些 `##` 级标题是强制规定且严格排序的。设计标记涵盖颜色（十六进制值）、字体排印（字族/字号/字重/行高/字间距）、间距、圆角尺寸比例，以及组件与其属性的映射关系。

## Token categories

## 标记类别

| Category | What it captures |
|----------|------------------|
| **Colors** | Hex palettes, semantic roles |
| **Typography** | Family, size, weight, line height, letter spacing |
| **Spacing** | Scale tokens for padding/margin/gap |
| **Rounded corners** | Radius scale |
| **Components** | Named components with property mappings |

| 类别 | 所涵盖内容 |
|------|------------|
| **颜色** | 十六进制调色板、语义化角色 |
| **字体排印** | 字族、字号、字重、行高、字间距 |
| **间距** | 用于内边距/外边距/间隙的尺寸比例标记 |
| **圆角** | 圆角半径比例 |
| **组件** | 具有属性映射关系的命名组件 |

## Why it matters

## 其重要性何在

- **AI-native by design.** Like [Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net) for PKM or `CLAUDE.md` for engineering, DESIGN.md is part of the *plain-text-as-AI-contract* pattern: human-and-machine-readable, version-controlled, follows the repo.

- **原生面向 AI 设计。** 就像用于个人知识管理（PKM）的[Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net)，或面向工程的 `CLAUDE.md` 一样，DESIGN.md 同属 *“纯文本即 AI 契约”* 范式：人类与机器均可读、支持版本控制、随代码仓库演进。

- **Tokens + rationale together.** Pure tokens (Tailwind config, DTCG JSON) give *what*; markdown body gives *why*. Agents need both to make non-trivial design decisions.

- **标记与依据并存。** 纯标记（如 Tailwind 配置、DTCG JSON）仅说明 *“是什么”*；而 Markdown 正文则阐明 *“为什么”*。智能体需二者兼备，方能作出非平凡的设计决策。

- **Closes the design-to-code gap for agents.** Without it, agents fall back to generic Material/shadcn defaults regardless of brand. With it, "deep ink headlines, warm limestone background, Boston Clay CTAs" is reproducible.

- **弥合智能体的“设计到代码”鸿沟。** 若无此规范，智能体将无视品牌特征，一律回退至通用的 Material 或 shadcn 默认样式；而有了它，“深墨色标题、暖石灰背景、波士顿黏土色按钮”等具体设计即可精准复现。

- **Exportable.** Designed to feed downstream toolchains: Tailwind config, DTCG (W3C Design Tokens Community Group) format, etc.

- **可导出。** 专为对接下游工具链而设计：例如生成 Tailwind 配置、DTCG（W3C 设计标记社区组）标准格式等。

## Audience

## 使用对象

| Role | How they use DESIGN.md |
|------|------------------------|
| **AI / coding agents** | Primary consumer — read tokens + rationale to generate UI |
| **Designers** | Author and own the file as the design system source of truth |
| **Developers** | Consume exported tokens (Tailwind, DTCG) and the components map |

| 角色 | 如何使用 DESIGN.md |
|------|---------------------|
| **AI / 编码智能体** | 主要使用者——读取标记与设计依据，以生成 UI |
| **设计师** | 文件作者与所有者，将其作为设计系统的唯一真实信源（source of truth） |
| **开发者** | 消费导出的标记（如 Tailwind、DTCG 格式）及组件映射表 |

## Status

## 当前状态

- **Alpha.** Spec, schema, and CLI are under active development; format changes expected.

- **Alpha 阶段。** 规范、模式（schema）与命令行工具（CLI）均处于积极开发中；格式变更尚在预期之中。

- **Apache-2.0** licensed.

- 采用 **Apache-2.0 许可协议**。

- Backed by Google Labs / Stitch.

- 由 Google Labs / Stitch 提供支持。

## Relation to other "AI-readable" specs

## 与其他“AI 可读”规范的关系

| Spec / file | Role |
|-------------|------|
| **DESIGN.md** | Design system context for coding agents |
| **CLAUDE.md / AGENTS.md** | Engineering / project context for coding agents |
| **MCP servers** | Live, queryable context for any agent |
| **DTCG tokens** | Standardized design token interchange format |

| 规范 / 文件 | 角色 |
|-------------|------|
| **DESIGN.md** | 为编码智能体提供设计系统上下文 |
| **CLAUDE.md / AGENTS.md** | 为编码智能体提供工程/项目上下文 |
| **MCP 服务端** | 为任意智能体提供实时、可查询的上下文 |
| **DTCG 标记** | 标准化的设计标记交换格式 |

DESIGN.md sits with CLAUDE.md / AGENTS.md in the *static, repo-resident, plain-text* context layer — complementary to [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net)'s *dynamic, server-mediated* context layer.

DESIGN.md 与 CLAUDE.md / AGENTS.md 同属于 *静态、驻留于代码仓库、纯文本* 的上下文层级——与 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 所定义的 *动态、服务端中介* 上下文层级互为补充。

## References

## 参考资料

- [https://github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)

- [https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification)

## Related

## 相关内容

- [AI Agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)

- [Google Stitch](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net)

- [Model Context Protocol (MCP)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net)

- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)

- [Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net) — same plain-text-as-AI-contract pattern, applied to PKM

- [Apache 2.0 License](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)

- [Yet Another Markup Language (YAML)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net)
