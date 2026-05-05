---
title: "Tolaria"
url: "https://www.dsebastien.net/tolaria/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Tolaria 是一款开源、AI 原生的桌面知识管理工具，以纯 Markdown 文件（含 YAML 前置元数据）存储内容，强调本地优先与数据自主。它内置块编辑器、双向链接、Git 版本控制，并原生集成 Model Context Protocol（MCP），使 Claude Code 等 AI 工具可直接读写知识库。区别于 Obsidian、Logseq 等现有工具，Tolaria 从设计之初就围绕 AI 协作构建，采用 AGPL 许可证，代表新一代“可被大模型无障碍推理”的工具型思考（TfT）范式。

---

*这是来自我的 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 的一则笔记。查看规范版本：[Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net)。*

*这是来自我的 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 的一则笔记。查看规范版本：[Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net)。*

Tolaria 是一款免费、开源的桌面应用，用于管理 Markdown 知识库，由 [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)（《[Refactoring](https://refactoring.fm/?ref=dsebastien.net)》通讯作者）开发。它被定位为“AI 时代的第二大脑”，所有数据均以纯文本 [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) 文件形式存储在本地磁盘，并辅以 [YAML](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net) 前置元数据；内置基于区块（block-based）的编辑器，支持 [双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net) 和斜杠命令；集成 [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 实现版本控制与同步；并提供一个 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端，使 [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net) 能直接读写你的知识库（vault）。

Tolaria 是一款免费、开源的桌面应用，用于管理 Markdown 知识库，由 [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)（《[Refactoring](https://refactoring.fm/?ref=dsebastien.net)》通讯作者）开发。它被定位为“AI 时代的第二大脑”，所有数据均以纯文本 [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) 文件形式存储在本地磁盘，并辅以 [YAML](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net) 前置元数据；内置基于区块（block-based）的编辑器，支持 [双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net) 和斜杠命令；集成 [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 实现版本控制与同步；并提供一个 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端，使 [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net) 能直接读写你的知识库（vault）。

它进入了一个已被 [Obsidian](https://obsidian.md/?ref=dsebastien.net)、[Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)、[Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net) 和 [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net) 主导的拥挤赛道，但确立了清晰的差异化定位：以文件为根基、自诞生起即原生适配 AI、采用 [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 授权，并围绕 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 构建深度集成能力，而非后期拼接式 AI 功能。

它进入了一个已被 [Obsidian](https://obsidian.md/?ref=dsebastien.net)、[Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)、[Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net) 和 [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net) 主导的拥挤赛道，但确立了清晰的差异化定位：以文件为根基、自诞生起即原生适配 AI、采用 [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 授权，并围绕 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 构建深度集成能力，而非后期拼接式 AI 功能。

## 关键特性

## 关键特性

| 特性 | 描述 |
|------|------|
| **基于文件** | 纯 `.md` 文件 + YAML 前置元数据，不依赖数据库 |
| **区块编辑器** | 支持斜杠命令、拖放操作、富文本区块 |
| **[双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)** | 支持维基链接（Wikilinks）及反向链接（backlinks） |
| **原生关系** | 笔记间具备一等公民地位的、有类型定义的连接关系 |
| **集成 Git** | 内置提交历史记录与变更追踪功能 |
| **[MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端** | 原生支持 Claude Code 集成 |
| **跨平台** | 支持 macOS、Windows、Linux |
| **开源** | 采用 [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0，永久免费 |

| 特性 | 描述 |
|------|------|
| **基于文件** | 纯 `.md` 文件 + YAML 前置元数据，不依赖数据库 |
| **区块编辑器** | 支持斜杠命令、拖放操作、富文本区块 |
| **[双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)** | 支持维基链接（Wikilinks）及反向链接（backlinks） |
| **原生关系** | 笔记间具备一等公民地位的、有类型定义的连接关系 |
| **集成 Git** | 内置提交历史记录与变更追踪功能 |
| **[MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端** | 原生支持 Claude Code 集成 |
| **跨平台** | 支持 macOS、Windows、Linux |
| **开源** | 采用 [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0，永久免费 |

## Tolaria 与其他工具对比

## Tolaria 与其他工具对比

| 维度 | Tolaria | [Obsidian](https://obsidian.md/?ref=dsebastien.net) | [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net) |
|------|---------|---------------------------------------------------|----------------------------------------------------|
| **存储格式** | Markdown + YAML | Markdown | Markdown / Org |
| **许可证** | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 | 专有（免费版） | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 |
| **源代码开放性** | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) | 闭源 | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) |
| **编辑器** | 基于区块、所见即所得（WYSIWYG） | Markdown + 实时预览 | 大纲式区块（outliner blocks） |
| **AI 集成** | 原生 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端 | 插件 / BYOK（Bring Your Own Key） | 插件 |
| **版本控制** | 内置 Git 客户端 | 插件（Obsidian Git） | 手动配置（DIY） |
| **移动端** | 仅限桌面端（当前） | iOS + Android | iOS + Android |
| **价格** | 免费 | 免费 / 同步付费 / 发布功能付费 | 免费 |

| 维度 | Tolaria | [Obsidian](https://obsidian.md/?ref=dsebastien.net) | [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net) |
|------|---------|---------------------------------------------------|----------------------------------------------------|
| **存储格式** | Markdown + YAML | Markdown | Markdown / Org |
| **许可证** | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 | 专有（免费版） | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 |
| **源代码开放性** | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) | 闭源 | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) |
| **编辑器** | 基于区块、所见即所得（WYSIWYG） | Markdown + 实时预览 | 大纲式区块（outliner blocks） |
| **AI 集成** | 原生 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端 | 插件 / BYOK（Bring Your Own Key） | 插件 |
| **版本控制** | 内置 Git 客户端 | 插件（Obsidian Git） | 手动配置（DIY） |
| **移动端** | 仅限桌面端（当前） | iOS + Android | iOS + Android |
| **价格** | 免费 | 免费 / 同步付费 / 发布功能付费 | 免费 |

## 其意义所在

## 其意义所在

Tolaria 是 2026 年涌现的一波 [个人知识管理（PKM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net) 工具的一员——这些工具从设计之初便原生面向 AI：它们并非将 [AI 智能体（AI agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) 生硬地嫁接到封闭格式之上，而是通过 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 为智能体提供对知识库（vault）的一等公民级访问权限，同时保持底层存储开放且可审查。其核心判断是：下一代 [思维工具（TfTs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net) 将是那些能让 [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) 无障碍地读取、写入与推理的知识系统。

Tolaria 是 2026 年涌现的一波 [个人知识管理（PKM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net) 工具的一员——这些工具从设计之初便原生面向 AI：它们并非将 [AI 智能体（AI agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) 生硬地嫁接到封闭格式之上，而是通过 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 为智能体提供对知识库（vault）的一等公民级访问权限，同时保持底层存储开放且可审查。其核心判断是：下一代 [思维工具（TfTs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net) 将是那些能让 [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) 无障碍地读取、写入与推理的知识系统。

采用 [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) 的 [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 许可证、纯文本文件与 [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 的组合，是对 [本地优先（local-first）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net) 理念的有力宣言——你的数据、运行于你的设备、版本历史亦由你掌控。

采用 [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) 的 [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 许可证、纯文本文件与 [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 的组合，是对 [本地优先（local-first）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net) 理念的有力宣言——你的数据、运行于你的设备、版本历史亦由你掌控。

## 参考资料

## 参考资料

- [https://tolaria.md/](https://tolaria.md/?ref=dsebastien.net)
- [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria?ref=dsebastien.net)
- [https://news.ycombinator.com/item?id=47882697](https://news.ycombinator.com/item?id=47882697&ref=dsebastien.net)

- [https://tolaria.md/](https://tolaria.md/?ref=dsebastien.net)
- [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria?ref=dsebastien.net)
- [https://news.ycombinator.com/item?id=47882697](https://news.ycombinator.com/item?id=47882697&ref=dsebastien.net)

## 相关内容

## 相关内容

- [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)
- [Obsidian](https://obsidian.md/?ref=dsebastien.net)
- [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)
- [Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net)
- [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net)
- [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net)
- [个人知识管理（PKM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net)
- [思维工具（TfTs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net)
- [双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)
- [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net)
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)
- [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net)
- [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)
- [本地优先软件（Local-First Software）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net)
- [AI 就绪型第二大脑（AI-Ready Second Brain）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI-Ready+Second+Brain?ref=dsebastien.net)

- [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)
- [Obsidian](https://obsidian.md/?ref=dsebastien.net)
- [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)
- [Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net)
- [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net)
- [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net)
- [个人知识管理（PKM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net)
- [思维工具（TfTs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net)
- [双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)
- [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net)
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)
- [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net)
- [Affero 通用公共许可证（AGPL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)
- [本地优先软件（Local-First Software）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net)
- [AI 就绪型第二大脑（AI-Ready Second Brain）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI-Ready+Second+Brain?ref=dsebastien.net)
