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
> Tolaria 是一款开源、AI 原生的 Markdown 知识管理桌面应用，以“AI 时代的第二大脑”为定位，所有数据以带 YAML 前置元数据的纯文本文件形式本地存储，并原生集成 Git 版本控制与 Model Context Protocol（MCP）服务器，使 Claude Code 等 AI 工具可直接读写知识库。它区别于 Obsidian、Logseq 等竞品，强调从设计之初即面向 AI 协作，而非后期添加 AI 功能，并采用 AGPL 许可证践行本地优先、数据自主理念。其核心价值在于构建一个 LLM 可无障碍理解、编辑和推理的开放知识基座，代表新一代“工具即思考”（TfTs）的发展方向。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一条备注。查看权威版本：[Tolaria](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tolaria?ref=dsebastien.net)。

Tolaria is a free, open-source desktop app for managing markdown knowledge bases, created by [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net) (author of the [Refactoring](https://refactoring.fm/?ref=dsebastien.net) newsletter). Positioned as "a second brain for the AI era", it stores everything as plain [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) files with [YAML](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net) frontmatter on disk, ships a block-based editor with [Bidirectional Links](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net) and slash commands, integrates [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) for version control and sync, and exposes a [Model Context Protocol (MCP)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) server so [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net) can read and write the vault directly.

Tolaria 是一款免费、开源的桌面应用，用于管理 Markdown 知识库，由 [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)（《[Refactoring](https://refactoring.fm/?ref=dsebastien.net)》通讯作者）开发。它定位为“AI 时代的第二大脑”，所有内容均以纯 [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) 文件加 [YAML](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Yet+Another+Markup+Language+(YAML)?ref=dsebastien.net) 前置元数据形式存储于本地磁盘；内置基于区块的编辑器，支持 [双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net) 和斜杠命令；深度集成 [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 实现版本控制与同步；并内置 [模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端，使 [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net) 可直接读写知识库。

It enters a crowded space dominated by [Obsidian](https://obsidian.md/?ref=dsebastien.net), [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net), [Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net), and [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net), but stakes a clear position: file-based, AI-native from day one, [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-licensed, and built around the [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) integration story rather than bolted-on AI features.

它进入了一个由 [Obsidian](https://obsidian.md/?ref=dsebastien.net)、[Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)、[Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net) 和 [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net) 主导的拥挤赛道，但确立了清晰的差异化定位：以文件为本、自诞生起即原生适配 AI、采用 [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 许可证，并围绕 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 深度集成构建，而非后期拼凑 AI 功能。

## Key Features

## 核心功能

| Feature | Description |
|---|---|
| **File-based** | Plain `.md` files + YAML frontmatter, no database |
| **Block editor** | Slash commands, drag-and-drop, rich blocks |
| **[Bidirectional Links](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)** | Wikilinks with backlinks |
| **Native relationships** | First-class typed connections between notes |
| **Integrated Git** | Commit history and change tracking built-in |
| **[MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) server** | Native Claude Code integration |
| **Cross-platform** | macOS, Windows, Linux |
| **Open source** | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0, free forever |

| 功能 | 描述 |
|---|---|
| **基于文件** | 纯 `.md` 文件 + YAML 前置元数据，无需数据库 |
| **区块编辑器** | 支持斜杠命令、拖拽操作、富文本区块 |
| **[双向链接](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)** | 支持维基链接及反向链接 |
| **原生关系** | 笔记间具备类型化、头等地位的连接能力 |
| **集成 Git** | 内置提交历史与变更追踪功能 |
| **[模型上下文协议（MCP）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端** | 原生支持 Claude Code 集成 |
| **跨平台** | 支持 macOS、Windows、Linux |
| **开源** | 采用 [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 协议，永久免费 |

## Tolaria vs the field

## Tolaria 与竞品对比

| Aspect | Tolaria | [Obsidian](https://obsidian.md/?ref=dsebastien.net) | [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net) |
|---|---|---|---|
| **Storage** | Markdown + YAML | Markdown | Markdown / Org |
| **License** | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 | Proprietary (free tier) | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 |
| **Source** | [Open Source](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) | Closed source | [Open Source](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) |
| **Editor** | Block-based, WYSIWYG | Markdown + live preview | Outliner blocks |
| **AI integration** | Native [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) server | Plugins / BYOK | Plugins |
| **Version control** | Built-in Git client | Plugin (Obsidian Git) | DIY |
| **Mobile** | Desktop only (for now) | iOS + Android | iOS + Android |
| **Price** | Free | Free / Sync paid / Publish | Free |

| 维度 | Tolaria | [Obsidian](https://obsidian.md/?ref=dsebastien.net) | [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net) |
|---|---|---|---|
| **存储格式** | Markdown + YAML | Markdown | Markdown / Org |
| **许可证** | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 | 专有（免费版） | [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)-3.0 |
| **源代码** | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) | 闭源 | [开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) |
| **编辑器** | 区块式、所见即所得（WYSIWYG） | Markdown + 实时预览 | 大纲式区块 |
| **AI 集成** | 原生 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 服务端 | 插件 / BYOK（自带密钥） | 插件 |
| **版本控制** | 内置 Git 客户端 | 插件（Obsidian Git） | 自行配置 |
| **移动端** | 仅桌面端（当前） | iOS + Android | iOS + Android |
| **价格** | 免费 | 免费 / 同步付费 / 发布功能付费 | 免费 |

## Why it matters

## 其重要性何在

Tolaria is part of a 2026 wave of [Personal Knowledge Management (PKM)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net) tools designed AI-native from the start: rather than retrofitting [AI agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) onto a closed format, it gives the agent first-class access to the vault via [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) while keeping the storage open and inspectable. The bet is that the next generation of [Tools for Thought (TfTs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net) will be the ones that a [LLM](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) can read, write, and reason over without friction.

Tolaria 属于 2026 年兴起的新一代 [个人知识管理（PKM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net) 工具浪潮——从设计之初即原生面向 AI：它并非将 [AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) 生硬嫁接到封闭格式上，而是通过 [MCP](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net) 赋予智能体对知识库的一等访问权，同时保持存储层开放且可检查。其核心判断是：下一代 [思维工具（TfTs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net) 将是那些能让 [大语言模型（LLM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) 无障碍地读取、写入和推理的知识系统。

The [Open Source](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) license + plain-files + [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) combination is a strong signal of [local-first](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net) values — your data, your machine, your version history.

[开源](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net) 的 [AGPL](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net) 许可证 + 纯文本文件 + [Git](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Git?ref=dsebastien.net) 的组合，强烈彰显了 [本地优先（local-first）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net) 的理念——你的数据、运行于你的设备、版本历史由你掌控。

## References

## 参考资料

- [https://tolaria.md/](https://tolaria.md/)
- [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)
- [https://news.ycombinator.com/item?id=47882697](https://news.ycombinator.com/item?id=47882697)

- [https://tolaria.md/](https://tolaria.md/)
- [https://github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)
- [https://news.ycombinator.com/item?id=47882697](https://news.ycombinator.com/item?id=47882697)

## Related

## 相关主题

- [Luca Rossi](https://notes.dsebastien.net/30+Areas/36+People/Luca+Rossi?ref=dsebastien.net)
- [Obsidian](https://obsidian.md/?ref=dsebastien.net)
- [Logseq](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Logseq?ref=dsebastien.net)
- [Notion](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Notion?ref=dsebastien.net)
- [Roam Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Roam+Research?ref=dsebastien.net)
- [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net)
- [Personal Knowledge Management (PKM)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Personal+Knowledge+Management+(PKM)?ref=dsebastien.net)
- [Tools for Thought (TfTs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tools+for+Thought+(TfTs)?ref=dsebastien.net)
- [Bidirectional Links](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Bidirectional+Links?ref=dsebastien.net)
- [Model Context Protocol (MCP)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Model+Context+Protocol+(MCP)?ref=dsebastien.net)
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)
- [Open Source](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Open+Source?ref=dsebastien.net)
- [Affero General Public License (AGPL)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Affero+General+Public+License+(AGPL)?ref=dsebastien.net)
- [Local-First Software](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Local-First+Software?ref=dsebastien.net)
- [AI-Ready Second Brain](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI-Ready+Second+Brain?ref=dsebastien.net)

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
