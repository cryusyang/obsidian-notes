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
> Book Exporter 是一款 Obsidian 插件，可将结构化的笔记树（以单个“清单笔记”为入口）自动编译为专业格式的电子书（EPUB/PDF）。该插件通过解析清单笔记的 frontmatter（含元数据）和正文中的标题+wikilink 构成的目录树，递归内联各章节笔记，并调用 Pandoc 完成格式转换。它无需强制命名、文件夹或标签，支持每本书独立配置导出参数，并提供验证命令确保元数据完整、链接有效，显著简化了从 Obsidian 写作到出版的流程。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Book+Exporter+plugin+for+Obsidian?ref=dsebastien.net"><em>Book Exporter plugin for Obsidian</em></a><em>.</em></p><p>A plugin that turns a structured Obsidian note tree into an actual book; exported to EPUB and PDF.</p><p>The Book Exporter plugin treats one note as the <strong>manifest</strong> for a book: its frontmatter holds the metadata (title, authors, language, cover, ISBN, etc.) and its body lists the table of contents through wikilinks. Each chapter and section is a separate note in the vault. When the plugin runs, it walks the manifest, compiles every linked note into a single <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net">Markdown</a> manuscript, then hands the result to <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> for EPUB and PDF generation.</p><p>The model is <strong>one note = one book</strong>. There are no mandatory naming conventions, no required folders, no special tags. Any Markdown note can act as a manifest.</p><p>This is a plugin that I have created. It removes the friction between writing a book inside Obsidian and shipping it to readers; no manual concatenation, no Scrivener detour, no copy-paste into Word.</p><h2 id="why-it-matters">Why it matters</h2><p>Writing a long-form work in Obsidian gives you backlinks, atomic notes, and a real graph. Until now the cost was that exporting was a chore. With this plugin, the same vault that holds your research is the vault that produces the EPUB.</p><h2 id="manifest-contract">Manifest contract</h2><p>The manifest&apos;s body is a <strong>heading tree</strong>. There are no reserved heading names &#x2014; the structure is yours.</p><ul><li><code># H1</code> is the book title (or use <code>title:</code> in frontmatter &#x2014; that wins).</li><li>Every <code>## H2</code> &#x2026; <code>###### H6</code> is a section at the matching level. Sections nest under the previous higher-level section.</li><li>Every bullet under a section that contains one or more <code>**wikilinks**</code> adds those links &#x2014; in source order &#x2014; to the section. The linked notes are inlined at that point.</li><li>Bullets without wikilinks are ignored. Text around a wikilink is dropped (commentary).</li></ul><h2 id="manifest-example">Manifest example</h2><pre><code># The Context Layer

## Foreword
- **Foreword**

## Part I &#x2014; The Problem
### Chapter 1 &#x2014; Why Notes Fail
- **Why Notes Fail**
- **The Cost of Forgetting**

## Part II &#x2014; The Solution
### Chapter 2 &#x2014; Building Context
- **Building Context**

## Acknowledgements
- **Acknowledgements**
- **About the Author**
</code></pre><p>When the manifest is parsed, configured &quot;sections to skip&quot; (default <code>Related</code>, <code>References</code>, <code>Title Options</code>, <code>Target Audience</code>) are dropped from the body first &#x2014; so authoring scaffolding sections stay in the manifest but never reach the export. The same list is then applied to each linked note when it&apos;s inlined: frontmatter is stripped, configured sections removed, first <code># H1</code> dropped, remaining headings demoted, and Obsidian-only syntax (callouts, embeds, comments, internal links) is rewritten.</p><h2 id="per-book-overrides">Per-book overrides</h2><p>Global settings are configured once in the plugin settings (output folder, default formats, Pandoc path, PDF engine, sections to skip, etc.). Any of those can be overridden per book via a <code>book_export:</code> block in the manifest frontmatter; output folder, PDF engine, formats, TOC depth, page-break behavior, and extra Pandoc flags are all configurable per book.</p><h2 id="validation">Validation</h2><p>The plugin ships a dedicated <strong>Validate current book</strong> command that checks the manifest before export: missing chapters, broken wikilinks, incomplete metadata. Errors are reported clearly so a broken book never reaches the export step.</p><h2 id="commands">Commands</h2><ul><li>Export current book to EPUB / PDF</li><li>Export current book to all formats</li><li>Preview compiled manuscript (.md)</li><li>Validate current book</li><li>Open exports folder</li></ul><h2 id="requirements">Requirements</h2><p>Desktop only. <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> is the single hard prerequisite. For PDF, the recommended engine is Typst; a single small binary that produces professional book-quality output without the LaTeX install. xelatex / tectonic / weasyprint / wkhtmltopdf remain available as alternatives.</p><h2 id="why-pandoc">Why Pandoc</h2><p><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> is the industry-standard document converter. No production-ready JavaScript or Node alternative exists, and bundling Pandoc inside the plugin is impractical given its size and per-platform binaries. Requiring it as an external dependency is the pragmatic trade.</p><h2 id="installation">Installation</h2><ul><li>Manual install, or via the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/BRAT+plugin+for+Obsidian?ref=dsebastien.net">BRAT plugin for Obsidian</a></li><li>Install <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> (system PATH or configured in plugin settings)</li><li>Install <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net">Typst</a> (recommended PDF engine)</li><li>Open a manifest note and run <strong>Book Exporter: Export current book to EPUB</strong> (or PDF, or all formats) from the command palette</li></ul><h2 id="references">References</h2><ul><li>Source code: <a href="https://github.com/dsebastien/obsidian-book-exporter?ref=dsebastien.net">https://github.com/dsebastien/obsidian-book-exporter</a></li><li>Documentation: <a href="https://dsebastien.github.io/obsidian-book-exporter/?ref=dsebastien.net">https://dsebastien.github.io/obsidian-book-exporter/</a></li><li>Pandoc: <a href="https://pandoc.org/?ref=dsebastien.net">https://pandoc.org</a></li><li>Typst: <a href="https://typst.app/?ref=dsebastien.net">https://typst.app</a></li><li>Article: <a href="https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/">https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/</a></li></ul><h2 id="related">Related</h2><ul><li><a href="https://obsidianstarterkit.com/?ref=dsebastien.net">Obsidian Starter Kit</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dataview+Serializer+plugin+for+Obsidian?ref=dsebastien.net">Dataview Serializer plugin for Obsidian</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Expander+plugin+for+Obsidian?ref=dsebastien.net">Expander plugin for Obsidian</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Obsidian+Publish?ref=dsebastien.net">Obsidian Publish</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net">Markdown</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net">Typst</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Announcing+Book+Exporter+-+A+New+Obsidian+Plugin+(Article)?ref=dsebastien.net">Announcing Book Exporter - A New Obsidian Plugin (Article)</a></li></ul>

## 中文译文

这是我的公开笔记中的一则说明。查看权威版本：Obsidian 的 Book Exporter（图书导出）插件。

一款可将结构化的 Obsidian 笔记树转化为真实图书的插件，支持导出为 EPUB 和 PDF 格式。

Book Exporter 插件将一份笔记视作整本图书的“清单文件”（manifest）：其 YAML 前置元数据（frontmatter）中存放图书元信息（如标题、作者、语言、封面、ISBN 等），正文则通过 Wikilink（双括号链接）列出目录结构。每一章、每一节均对应知识库（vault）中的一份独立笔记。插件运行时，会遍历该清单文件，将所有被链接的笔记按顺序编译为单一的 Markdown 手稿，再交由 Pandoc 生成 EPUB 与 PDF。

其设计模型为“一份笔记 = 一本图书”。无需强制命名规范，不依赖特定文件夹结构，也不要求特殊标签。任何标准 Markdown 笔记皆可担任清单文件角色。

这是我开发的一款插件，旨在消除在 Obsidian 中写作图书与面向读者发布之间的障碍：无需手动拼接文本，无需转向 Scrivener 等第三方写作工具，也无需复制粘贴到 Word 中处理。

为何重要

在 Obsidian 中撰写长篇作品，可享受双向链接、原子化笔记以及真实的知识图谱优势。但此前，导出环节却始终是一大负担。借助本插件，承载你全部研究资料的知识库，亦可直接产出最终的 EPUB 文件。

清单文件契约（Manifest Contract）

清单文件的正文须为一个层级分明的标题树（heading tree）。不存在预设的标题名称限制——整个结构完全由你自主定义。

- `# H1` 标题即为图书主标题（或使用 frontmatter 中的 `title:` 字段，后者优先级更高）。
- 每个 `## H2` 至 `###### H6` 标题均代表对应层级的章节或小节；各小节依序嵌套于前一个更高级别的标题之下。
- 在某一小节下方，凡以项目符号（bullet）列出、且其中包含一个或多个 **Wikilink** 的条目，均会将这些链接所指向的笔记，按其在源文件中出现的顺序，内联（inline）插入至该位置。
- 不含 Wikilink 的项目符号条目将被忽略；Wikilink 周围的其他文字（如说明性内容）亦会被舍弃。

清单文件示例

解析清单文件时，系统首先剔除配置中指定的“需跳过的章节”（默认包括：Related、References、Title Options、Target Audience）。此举使得用于写作辅助的“脚手架章节”可保留在清单文件中，却不会进入最终导出内容。随后，同一跳过规则还将应用于每一个被内联的链接笔记：其 frontmatter 将被剥离；已配置的章节被移除；首个 `# H1` 标题被删除；其余标题层级整体降级（如 `##` 变为 `#`，`###` 变为 `##`，以此类推）；Obsidian 特有语法（如提示框 callouts、嵌入 embeds、注释 comments、内部链接 internal links）则被重写为通用 Markdown 或 Pandoc 兼容格式。

每本书的个性化覆盖设置（Per-book Overrides）

全局设置（如输出文件夹路径、默认导出格式、Pandoc 可执行文件路径、PDF 渲染引擎、需跳过的章节等）统一在插件设置中完成一次配置。但上述任一选项均可通过在清单文件的 frontmatter 中添加 `book_export:` 区块实现单书级覆盖。支持按书定制的参数包括：输出路径、PDF 引擎、导出格式列表、目录（TOC）深度、分页行为（page-break behavior），以及额外的 Pandoc 参数标志（extra Pandoc flags）。

校验功能（Validation）

插件内置专属命令“Validate current book”（校验当前图书），可在导出前对清单文件进行全面检查：是否存在缺失章节、损坏的 Wikilink、不完整的元数据等。所有错误均以清晰方式呈现，确保问题图书绝不会进入导出流程。

可用命令（Commands）

- 导出当前图书为 EPUB / PDF  
- 导出当前图书为全部支持格式  
- 预览编译后手稿（.md 文件）  
- 校验当前图书  
- 打开导出文件夹  

系统要求（Requirements）

仅限桌面端使用。Pandoc 是唯一硬性依赖。对于 PDF 导出，推荐使用 Typst 作为渲染引擎——它是一个轻量级二进制程序，无需安装庞大的 LaTeX 环境，即可生成专业级出版品质的 PDF 输出。此外，xelatex / tectonic / weasyprint / wkhtmltopdf 等替代方案仍保持可用。

为何选用 Pandoc？

Pandoc 是业界公认的标准文档转换器。目前尚无生产就绪（production-ready）的 JavaScript 或 Node.js 替代方案；而鉴于 Pandoc 体积庞大、且需为不同操作系统提供专用二进制文件，将其打包进插件本身并不现实。因此，将其设为外部依赖是一项务实而合理的选择。

安装步骤（Installation）

- 手动安装，或通过 Obsidian 的 BRAT 插件安装  
- 安装 Pandoc（确保其位于系统 PATH 中，或在插件设置中指定其路径）  
- 安装 Typst（推荐的 PDF 渲染引擎）  
- 打开一份清单文件，在命令面板中运行 “Book Exporter: Export current book to EPUB”（或 PDF，或 all formats）

参考资料（References）

- 源代码：https://github.com/dsebastien/obsidian-book-exporter  
- 文档说明：https://dsebastien.github.io/obsidian-book-exporter/  
- Pandoc 官网：https://pandoc.org  
- Typst 官网：https://typst.app  
- 发布文章：https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/  

相关插件与工具（Related）

- Obsidian Starter Kit  
- Dataview Serializer 插件（Obsidian）  
- Expander 插件（Obsidian）  
- Obsidian Publish  
- Markdown  
- Pandoc  
- Typst  
- 《发布 Book Exporter：一款全新的 Obsidian 插件》（文章）
