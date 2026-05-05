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

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DESIGN.md+Specification?ref=dsebastien.net"><em>DESIGN.md Specification</em></a><em>.</em></p><p>DESIGN.md is an open Apache-2.0 format specification from <a href="https://github.com/google-labs-code/design.md?ref=dsebastien.net">Google Labs</a> for describing a design system to <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">coding agents</a> in a single, version-controllable file. It pairs <strong>machine-readable design tokens in YAML front matter</strong> with <strong>human-readable design rationale in markdown prose</strong> &#x2014; so an <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">LLM</a> can apply visual identity correctly instead of defaulting to generic UI.</p><p>It plays the same role for <em>design context</em> that <code>CLAUDE.md</code> / <code>AGENTS.md</code> plays for <em>engineering context</em>: a persistent, structured contract that survives sessions and follows the repo. Currently in <strong>alpha</strong>; the format, schema, and CLI are still moving.</p><p>Spec home: <a href="https://stitch.withgoogle.com/docs/design-md/specification?ref=dsebastien.net">https://stitch.withgoogle.com/docs/design-md/specification</a> &#x2014; <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net">Google Stitch</a> (Google&apos;s AI design tool) is the reference consumer.</p><h2 id="file-anatomy">File anatomy</h2><pre><code>---
# YAML front matter &#x2014; design tokens (machine-readable)
colors:
  primary: &quot;#1a3a52&quot;
  background: &quot;#f7f3ec&quot;
typography:
  headline:
    fontFamily: &quot;Inter&quot;
    fontSize: 48
    fontWeight: 700
spacing:
  scale: [4, 8, 16, 24, 32]
---

## Overview         &lt;- markdown body &#x2014; design rationale
## Colors
## Typography
## Layout
## Elevation &amp; Depth
## Shapes
## Components
## Do&apos;s and Don&apos;ts
</code></pre><p>The <code>##</code> headings are prescribed and ordered. Tokens cover colors (hex), typography (family/size/weight/lineHeight/letterSpacing), spacing, rounded-corner scales, and component-property mappings.</p><h2 id="token-categories">Token categories</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Category</th>
<th>What it captures</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Colors</strong></td>
<td>Hex palettes, semantic roles</td>
</tr>
<tr>
<td><strong>Typography</strong></td>
<td>Family, size, weight, line height, letter spacing</td>
</tr>
<tr>
<td><strong>Spacing</strong></td>
<td>Scale tokens for padding/margin/gap</td>
</tr>
<tr>
<td><strong>Rounded corners</strong></td>
<td>Radius scale</td>
</tr>
<tr>
<td><strong>Components</strong></td>
<td>Named components with property mappings</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<h2 id="why-it-matters">Why it matters</h2><ul><li><strong>AI-native by design.</strong> Like <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net">Tolaria</a> for PKM or <code>CLAUDE.md</code> for engineering, DESIGN.md is part of the <em>plain-text-as-AI-contract</em> pattern: human-and-machine-readable, version-controlled, follows the repo.</li><li><strong>Tokens + rationale together.</strong> Pure tokens (Tailwind config, DTCG JSON) give <em>what</em>; markdown body gives <em>why</em>. Agents need both to make non-trivial design decisions.</li><li><strong>Closes the design-to-code gap for agents.</strong> Without it, agents fall back to generic Material/shadcn defaults regardless of brand. With it, &quot;deep ink headlines, warm limestone background, Boston Clay CTAs&quot; is reproducible.</li><li><strong>Exportable.</strong> Designed to feed downstream toolchains: Tailwind config, DTCG (W3C Design Tokens Community Group) format, etc.</li></ul><h2 id="audience">Audience</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Role</th>
<th>How they use DESIGN.md</th>
</tr>
</thead>
<tbody><tr>
<td><strong>AI / coding agents</strong></td>
<td>Primary consumer &#x2014; read tokens + rationale to generate UI</td>
</tr>
<tr>
<td><strong>Designers</strong></td>
<td>Author and own the file as the design system source of truth</td>
</tr>
<tr>
<td><strong>Developers</strong></td>
<td>Consume exported tokens (Tailwind, DTCG) and the components map</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<h2 id="status">Status</h2><ul><li><strong>Alpha.</strong> Spec, schema, and CLI are under active development; format changes expected.</li><li><strong>Apache-2.0</strong> licensed.</li><li>Backed by Google Labs / Stitch.</li></ul><h2 id="relation-to-other-ai-readable-specs">Relation to other &quot;AI-readable&quot; specs</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Spec / file</th>
<th>Role</th>
</tr>
</thead>
<tbody><tr>
<td><strong>DESIGN.md</strong></td>
<td>Design system context for coding agents</td>
</tr>
<tr>
<td><strong>CLAUDE.md / AGENTS.md</strong></td>
<td>Engineering / project context for coding agents</td>
</tr>
<tr>
<td><strong>MCP servers</strong></td>
<td>Live, queryable context for any agent</td>
</tr>
<tr>
<td><strong>DTCG tokens</strong></td>
<td>Standardized design token interchange format</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<p>DESIGN.md sits with CLAUDE.md / AGENTS.md in the <em>static, repo-resident, plain-text</em> context layer &#x2014; complementary to <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net">MCP</a>&apos;s <em>dynamic, server-mediated</em> context layer.</p><h2 id="references">References</h2><ul><li><a href="https://github.com/google-labs-code/design.md?ref=dsebastien.net">https://github.com/google-labs-code/design.md</a></li><li><a href="https://stitch.withgoogle.com/docs/design-md/specification?ref=dsebastien.net">https://stitch.withgoogle.com/docs/design-md/specification</a></li></ul><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI Agents</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+Stitch?ref=dsebastien.net">Google Stitch</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net">Model Context Protocol (MCP)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">Large Language Models (LLMs)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net">Tolaria</a> &#x2014; same plain-text-as-AI-contract pattern, applied to PKM</li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 License</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net">Yet Another Markup Language (YAML)</a></li></ul>

## 中文译文

这是我的公开笔记中的一则备注。请参阅权威版本：DESIGN.md 规范。

DESIGN.md 是由 Google Labs 发布的一项开源规范，采用 Apache-2.0 许可协议，旨在以单一、可版本控制的文件形式，向编码智能体（coding agents）描述设计系统。该规范将机器可读的设计令牌（design tokens）以 YAML 前置元数据（front matter）形式组织，并辅以人类可读的设计原理说明（markdown 正文），从而让大语言模型（LLM）能够准确应用视觉识别体系，而非退回到通用用户界面（UI）默认样式。

它在设计上下文层面所起的作用，与 CLAUDE.md / AGENTS.md 在工程上下文层面所起的作用一致：即提供一份持久化、结构化的契约，该契约可跨越会话持续存在，并随代码仓库一同流转。当前处于 Alpha 阶段；其格式、模式（schema）及命令行工具（CLI）仍在持续演进中。

规范主页：https://stitch.withgoogle.com/docs/design-md/specification — Google Stitch（Google 推出的 AI 设计工具）是该规范的参考实现消费者。

文件结构

## 标题层级为强制规定且顺序固定。设计令牌涵盖颜色（十六进制值）、排版（字体族/字号/字重/行高/字间距）、间距、圆角尺寸标尺，以及组件属性映射关系。

设计令牌分类

为何重要？

原生面向 AI 构建。正如 Tolaria 之于个人知识管理（PKM）、CLAUDE.md 之于工程实践，DESIGN.md 同属“纯文本即 AI 契约”（plain-text-as-AI-contract）范式：既可供人类阅读，亦可供机器解析；支持版本控制；随代码仓库同步流转。

设计令牌与设计原理并存。仅含令牌的配置（如 Tailwind 配置文件、DTCG JSON）仅说明“是什么”（what）；而 Markdown 正文则阐明“为什么”（why）。智能体需二者兼备，方能做出非平凡的设计决策。

弥合智能体在设计到代码转化过程中的鸿沟。缺乏此规范时，智能体无论品牌调性如何，均会回退至通用 Material 或 shadcn 等默认样式；而引入该规范后，“深墨色标题、暖石灰色背景、波士顿黏土色按钮”等具体视觉表达即可被稳定复现。

可导出性强。专为对接下游工具链而设计，例如生成 Tailwind 配置、W3C 设计令牌社区组（DTCG）标准格式等。

适用对象

当前状态

Alpha 阶段。规范内容、数据模式（schema）及命令行工具（CLI）均处于积极开发中；格式变动尚属预期之内。

采用 Apache-2.0 开源许可证。

由 Google Labs 及 Google Stitch 提供支持。

与其他“AI 可读”规范的关系

DESIGN.md 与 CLAUDE.md / AGENTS.md 共同构成静态、驻留于代码仓库内的纯文本上下文层；该层与 Model Context Protocol（MCP）所代表的动态、服务端中介的上下文层互为补充。

参考资料

https://github.com/google-labs-code/design.md  
https://stitch.withgoogle.com/docs/design-md/specification  

相关主题

AI 智能体（AI Agents）  
Google Stitch  
模型上下文协议（Model Context Protocol, MCP）  
大语言模型（Large Language Models, LLMs）  
Tolaria — 同样采用“纯文本即 AI 契约”范式，应用于个人知识管理（PKM）领域  
Apache 2.0 许可证  
又一种标记语言（Yet Another Markup Language, YAML）
