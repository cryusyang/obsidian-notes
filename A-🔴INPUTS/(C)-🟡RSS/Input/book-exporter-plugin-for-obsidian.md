---
title: "Book Exporter plugin for Obsidian"
url: "https://www.dsebastien.net/book-exporter-plugin-for-obsidian/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Book Exporter 是一款 Obsidian 插件，可将结构化的笔记树（以单个“清单笔记”为入口）自动编译为专业格式的电子书（EPUB/PDF）。清单笔记通过 frontmatter 定义元数据（如标题、作者、封面等），正文以标题层级和 wikilinks 构建目录，插件递归内联所有链接笔记并交由 Pandoc 渲染。它无需强制命名、文件夹或标签，支持每本书独立配置导出参数，并提供预验证功能确保元数据完整、链接有效，从而消除从 Obsidian 写作到出版之间的手动整合成本。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Book Exporter plugin for Obsidian](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Book+Exporter+plugin+for+Obsidian?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则说明。查看权威版本：[Obsidian 的 Book Exporter 插件](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Book+Exporter+plugin+for+Obsidian?ref=dsebastien.net)。

A plugin that turns a structured Obsidian note tree into an actual book; exported to EPUB and PDF.

一个将结构化的 Obsidian 笔记树转化为真实书籍的插件；支持导出为 EPUB 和 PDF 格式。

The Book Exporter plugin treats one note as the **manifest** for a book: its frontmatter holds the metadata (title, authors, language, cover, ISBN, etc.) and its body lists the table of contents through wikilinks. Each chapter and section is a separate note in the vault. When the plugin runs, it walks the manifest, compiles every linked note into a single [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) manuscript, then hands the result to [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) for EPUB and PDF generation.

Book Exporter 插件将某一份笔记视为整本书的**清单（manifest）**：其前置元数据（frontmatter）中存放书籍元信息（如标题、作者、语言、封面、ISBN 等），正文部分则通过维基链接（wikilinks）列出目录结构。每一章、每一节都对应知识库（vault）中一份独立的笔记。插件运行时，会遍历该清单，将所有被链接的笔记编译成一份完整的 [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net) 手稿，再交由 [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) 生成 EPUB 和 PDF。

The model is **one note = one book**. There are no mandatory naming conventions, no required folders, no special tags. Any Markdown note can act as a manifest.

其模型是 **“一份笔记 = 一本书”**。无需强制命名规范、无需特定文件夹结构、也无需特殊标签——任意 Markdown 笔记皆可作为清单使用。

This is a plugin that I have created. It removes the friction between writing a book inside Obsidian and shipping it to readers; no manual concatenation, no Scrivener detour, no copy-paste into Word.

这是我开发的一款插件，旨在消除在 Obsidian 中写作与向读者交付成品之间的摩擦：无需手动拼接文本、无需绕道 Scrivener、也无需复制粘贴进 Word。

## Why it matters

## 为何重要

Writing a long-form work in Obsidian gives you backlinks, atomic notes, and a real graph. Until now the cost was that exporting was a chore. With this plugin, the same vault that holds your research is the vault that produces the EPUB.

在 Obsidian 中撰写长篇作品，可获得双向链接、原子化笔记和真实的图谱关系。但此前的代价是：导出始终是一项繁琐任务。而借助本插件，承载你全部研究的知识库，也正是直接产出 EPUB 的知识库。

## Manifest contract

## 清单契约（Manifest Contract）

The manifest's body is a **heading tree**. There are no reserved heading names — the structure is yours.

清单的正文是一棵**标题层级树**。不存在保留标题名称——结构完全由你定义。

- `# H1` is the book title (or use `title:` in frontmatter — that wins).
- 每个 `# H1` 表示全书标题（或在前置元数据中用 `title:` 字段指定——该字段优先级更高）。
- Every `## H2` … `###### H6` is a section at the matching level. Sections nest under the previous higher-level section.
- 每个 `## H2` … `###### H6` 对应相应层级的章节；各章节按前一个更高级别标题进行嵌套。
- Every bullet under a section that contains one or more `**wikilinks**` adds those links — in source order — to the section. The linked notes are inlined at that point.
- 在某章节下，每个包含一个或多个 `**wikilinks**` 的项目符号条目，都会按源码顺序将这些链接加入该章节；被链接的笔记将在该位置内联展开。
- Bullets without wikilinks are ignored. Text around a wikilink is dropped (commentary).
- 不含维基链接的项目符号条目将被忽略；维基链接周围的文字（如说明性注释）亦会被舍弃。

## Manifest example

## 清单示例

```markdown
# The Context Layer

## Foreword
- **Foreword**

## Part I — The Problem
### Chapter 1 — Why Notes Fail
- **Why Notes Fail**
- **The Cost of Forgetting**

## Part II — The Solution
### Chapter 2 — Building Context
- **Building Context**

## Acknowledgements
- **Acknowledgements**
- **About the Author**
```

当清单被解析时，首先会移除配置中指定的“需跳过章节”（默认包括 `Related`、`References`、`Title Options`、`Target Audience`）——这样，仅用于作者写作支撑的章节可保留在清单中，却不会进入最终导出内容。随后，同一跳过列表还会应用于每个被内联的链接笔记：剥离其前置元数据、移除配置指定的章节、删除首个 `# H1` 标题、对其余标题降级（如 `##` → `#`），并将 Obsidian 专属语法（提示框 callouts、嵌入 embeds、注释 comments、内部链接 internal links）重写为通用格式。

## Per-book overrides

## 每本书的个性化覆盖设置

Global settings are configured once in the plugin settings (output folder, default formats, Pandoc path, PDF engine, sections to skip, etc.). Any of those can be overridden per book via a `book_export:` block in the manifest frontmatter; output folder, PDF engine, formats, TOC depth, page-break behavior, and extra Pandoc flags are all configurable per book.

全局设置只需在插件设置中配置一次（如输出文件夹、默认导出格式、Pandoc 路径、PDF 引擎、需跳过的章节等）。其中任一选项均可通过清单笔记前置元数据中的 `book_export:` 区块为每本书单独覆盖：输出路径、PDF 引擎、导出格式、目录深度、分页行为、额外 Pandoc 参数等，全部支持按书定制。

## Validation

## 验证功能

The plugin ships a dedicated **Validate current book** command that checks the manifest before export: missing chapters, broken wikilinks, incomplete metadata. Errors are reported clearly so a broken book never reaches the export step.

插件自带专用的 **“验证当前书籍”** 命令，可在导出前检查清单：是否存在缺失章节、失效维基链接、不完整元数据等。所有错误均以清晰方式报告，确保问题书籍绝不会进入导出流程。

## Commands

## 命令列表

- Export current book to EPUB / PDF  
- 将当前书籍导出为 EPUB / PDF  
- Export current book to all formats  
- 将当前书籍导出为全部支持格式  
- Preview compiled manuscript (.md)  
- 预览已编译的手稿（.md）  
- Validate current book  
- 验证当前书籍  
- Open exports folder  
- 打开导出文件夹  

## Requirements

## 系统要求

Desktop only. [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) is the single hard prerequisite. For PDF, the recommended engine is Typst; a single small binary that produces professional book-quality output without the LaTeX install. xelatex / tectonic / weasyprint / wkhtmltopdf remain available as alternatives.

仅限桌面端使用。[Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) 是唯一硬性依赖。PDF 导出推荐使用 Typst 引擎：一个轻量级二进制程序，无须安装 LaTeX 即可生成专业级图书品质输出。xelatex / tectonic / weasyprint / wkhtmltopdf 仍作为可选替代方案保留。

## Why Pandoc

## 为何选用 Pandoc

[Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) is the industry-standard document converter. No production-ready JavaScript or Node alternative exists, and bundling Pandoc inside the plugin is impractical given its size and per-platform binaries. Requiring it as an external dependency is the pragmatic trade.

[Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) 是业界标准的文档转换器。目前尚无生产就绪的 JavaScript 或 Node 替代方案；且因 Pandoc 体积庞大、需为各平台分别提供二进制文件，将其打包进插件亦不现实。因此，将其设为外部依赖是一项务实的权衡。

## Installation

## 安装步骤

- Manual install, or via the [BRAT plugin for Obsidian](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/BRAT+plugin+for+Obsidian?ref=dsebastien.net)  
- 手动安装，或通过 [Obsidian 的 BRAT 插件](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/BRAT+plugin+for+Obsidian?ref=dsebastien.net) 安装  
- Install [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net) (system PATH or configured in plugin settings)  
- 安装 [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net)（添加至系统 PATH，或在插件设置中指定路径）  
- Install [Typst](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net) (recommended PDF engine)  
- 安装 [Typst](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net)（推荐的 PDF 引擎）  
- Open a manifest note and run **Book Exporter: Export current book to EPUB** (or PDF, or all formats) from the command palette  
- 打开一份清单笔记，在命令面板中运行 **“Book Exporter：将当前书籍导出为 EPUB”**（或 PDF，或全部格式）  

## References

## 参考资料

- Source code: [https://github.com/dsebastien/obsidian-book-exporter](https://github.com/dsebastien/obsidian-book-exporter)  
- 源代码：[https://github.com/dsebastien/obsidian-book-exporter](https://github.com/dsebastien/obsidian-book-exporter)  
- Documentation: [https://dsebastien.github.io/obsidian-book-exporter/](https://dsebastien.github.io/obsidian-book-exporter/)  
- 文档：[https://dsebastien.github.io/obsidian-book-exporter/](https://dsebastien.github.io/obsidian-book-exporter/)  
- Pandoc: [https://pandoc.org](https://pandoc.org)  
- Pandoc：[https://pandoc.org](https://pandoc.org)  
- Typst: [https://typst.app](https://typst.app)  
- Typst：[https://typst.app](https://typst.app)  
- Article: [https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/](https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/)  
- 文章：[https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/](https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/)  

## Related

## 相关资源

- [Obsidian Starter Kit](https://obsidianstarterkit.com)  
- [Obsidian 启动套件](https://obsidianstarterkit.com)  
- [Dataview Serializer plugin for Obsidian](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dataview+Serializer+plugin+for+Obsidian?ref=dsebastien.net)  
- [Obsidian 的 Dataview Serializer 插件](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dataview+Serializer+plugin+for+Obsidian?ref=dsebastien.net)  
- [Expander plugin for Obsidian](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Expander+plugin+for+Obsidian?ref=dsebastien.net)  
- [Obsidian 的 Expander 插件](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Expander+plugin+for+Obsidian?ref=dsebastien.net)  
- [Obsidian Publish](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Obsidian+Publish?ref=dsebastien.net)  
- [Obsidian Publish](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Obsidian+Publish?ref=dsebastien.net)  
- [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net)  
- [Markdown](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net)  
- [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net)  
- [Pandoc](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net)  
- [Typst](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net)  
- [Typst](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net)  
- [Announcing Book Exporter - A New Obsidian Plugin (Article)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Announcing+Book+Exporter+-+A+New+Obsidian+Plugin+(Article)?ref=dsebastien.net)  
- [《发布 Book Exporter：一款全新的 Obsidian 插件》（文章）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Announcing+Book+Exporter+-+A+New+Obsidian+Plugin+(Article)?ref=dsebastien.net)
