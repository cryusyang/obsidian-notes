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

*这是来自我的<a href="https://notes.dsebastien.net/?ref=dsebastien.net">公开笔记</a>的一则备注。查看权威版本：<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DESIGN.md+Specification?ref=dsebastien.net">DESIGN.md 规范</a>。*

*这是来自<a href="https://github.com/google-labs-code/design.md?ref=dsebastien.net">Google Labs</a>的一项开源 Apache-2.0 协议规范，名为 DESIGN.md，用于在单个、可版本控制的文件中向<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">编码智能体（coding agents）</a>描述设计系统。它将<strong>YAML 前置元数据中的机器可读设计标记（design tokens）</strong>与<strong>Markdown 正文中的人类可读设计依据（design rationale）</strong>相结合——从而使<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLM）</a>能准确应用视觉识别体系，而非退回到通用 UI 模板。*

*它在<strong>设计上下文（design context）</strong>中所扮演的角色，正如同 <code>CLAUDE.md</code> / <code>AGENTS.md</code> 在<strong>工程上下文（engineering context）</strong>中所起的作用：一份持久化、结构化的契约，可跨越会话持续存在，并随代码仓库一同流转。当前处于<strong>Alpha 阶段</strong>；其格式、模式（schema）及命令行工具（CLI）仍在持续演进中。*

*规范主页：<a href="https://stitch.withgoogle.com/docs/design-md/specification?ref=dsebastien.net">https://stitch.withgoogle.com/docs/design-md/specification</a> —— <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net">Google Stitch</a>（Google 的 AI 设计工具）是该规范的参考实现消费者。*

## 文件结构

```markdown
---
# YAML 前置元数据 —— 设计标记（机器可读）
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

## 概览         ← Markdown 正文 —— 设计依据
## 颜色
## 字体排印
## 布局
## 层级与景深
## 形状
## 组件
## 最佳实践与禁忌
```

`##` 级标题为强制规定且顺序固定。标记涵盖颜色（十六进制）、字体排印（字体族/字号/字重/行高/字间距）、间距、圆角半径刻度，以及组件属性映射。

## 标记分类

| 分类 | 所涵盖内容 |
|------|------------|
| **颜色** | 十六进制配色方案、语义化角色定义 |
| **字体排印** | 字体族、字号、字重、行高、字间距 |
| **间距** | 用于内边距/外边距/间隙的刻度标记 |
| **圆角** | 圆角半径刻度 |
| **组件** | 具名组件及其属性映射关系 |

## 其重要性何在？

- **原生支持 AI。** 就像用于个人知识管理（PKM）的<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net">Tolaria</a>，或用于工程领域的 <code>CLAUDE.md</code> 一样，DESIGN.md 是“纯文本即 AI 契约”（plain-text-as-AI-contract）范式的一部分：人类与机器均可阅读、受版本控制、随代码仓库流转。
- **标记与依据并存。** 纯标记（如 Tailwind 配置、DTCG JSON）仅说明“是什么”；而 Markdown 正文则阐明“为什么”。智能体需二者兼备，方能做出非平凡的设计决策。
- **弥合智能体从设计到代码的鸿沟。** 若无此规范，智能体会无视品牌特性，直接回退至通用 Material 或 shadcn 默认样式；而有了它，“深墨色标题、暖石灰背景、波士顿黏土色行动按钮（CTA）”等具体设计意图即可被精准复现。
- **可导出性强。** 专为向下游工具链提供支持而设计：例如生成 Tailwind 配置、W3C 设计标记社区组（DTCG）标准格式等。

## 目标用户

| 角色 | 如何使用 DESIGN.md |
|------|-------------------|
| **AI / 编码智能体** | 主要使用者——读取标记与设计依据，以生成 UI |
| **设计师** | 作为设计系统的唯一真实信源（source of truth）撰写并维护该文件 |
| **开发者** | 使用导出的标记（如 Tailwind、DTCG）及组件映射表 |

## 当前状态

- **Alpha 阶段。** 规范、模式（schema）及命令行工具（CLI）均处于积极开发中；格式变更在所难免。
- 采用 **Apache-2.0 许可协议**。
- 由 Google Labs / Stitch 支持。

## 与其他“AI 可读”规范的关系

| 规范 / 文件 | 定位 |
|-------------|------|
| **DESIGN.md** | 为编码智能体提供设计系统上下文 |
| **CLAUDE.md / AGENTS.md** | 为编码智能体提供工程/项目上下文 |
| **MCP 服务器** | 为任意智能体提供实时、可查询的上下文 |
| **DTCG 标记** | 标准化的设计标记交换格式 |

DESIGN.md 与 CLAUDE.md / AGENTS.md 同属<strong>静态、驻留于代码仓库、纯文本</strong>的上下文层——与<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net">MCP</a> 所代表的<strong>动态、服务端中介</strong>上下文层互为补充。

## 参考资料

- <a href="https://github.com/google-labs-code/design.md?ref=dsebastien.net">https://github.com/google-labs-code/design.md</a>
- <a href="https://stitch.withgoogle.com/docs/design-md/specification?ref=dsebastien.net">https://stitch.withgoogle.com/docs/design-md/specification</a>

## 相关链接

- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI 智能体</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net">Google Stitch</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net">模型上下文协议（MCP）</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLMs）</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net">Tolaria</a> —— 同样采用“纯文本即 AI 契约”范式，应用于个人知识管理（PKM）
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net">YAML（Yet Another Markup Language）</a>
