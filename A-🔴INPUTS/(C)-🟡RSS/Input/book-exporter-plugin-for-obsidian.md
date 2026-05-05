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
> Book Exporter 是一款 Obsidian 插件，可将结构化的笔记树（以单个“清单笔记”为入口）自动编译为专业格式的电子书（EPUB/PDF）。该插件通过解析清单笔记的 frontmatter（含元数据）和正文中的 wikilink 目录树，递归内联各章节笔记，并调用 Pandoc 完成格式转换，全程无需手动拼接或外部工具。它支持灵活的结构约定（如标题层级对应章节嵌套）、按需跳过 scaffolding 章节、每本书独立配置导出参数，并提供前置验证命令确保导出质量。

---

<p><em>这是来自我的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>公开笔记</em></a><em> 的一则记录。查看权威版本：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Book+Exporter+plugin+for+Obsidian?ref=dsebastien.net"><em>Obsidian 的 Book Exporter 插件</em></a><em>。</em></p>

<p>一款将结构化的 Obsidian 笔记树转化为真实图书的插件；可导出为 EPUB 和 PDF 格式。</p>

<p>Book Exporter 插件将某一份笔记视作整本书的<strong>清单（manifest）</strong>：其 Frontmatter 中保存元数据（标题、作者、语言、封面、ISBN 等），正文则通过 Wikilink 列出目录结构。每一章与每一节均为知识库（vault）中独立的笔记。插件运行时，会遍历该清单，将所有被链接的笔记编译为一份单一的 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net">Markdown</a> 手稿，再交由 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> 生成 EPUB 与 PDF。</p>

<p>其设计模型是<strong>一份笔记 = 一本书</strong>。无需强制命名规范、无需特定文件夹结构、也无需特殊标签。任何 Markdown 笔记皆可作为清单使用。</p>

<p>这是我开发的一款插件，它消除了在 Obsidian 中写作成书与向读者交付成品之间的摩擦；无需手动拼接、无需绕道 Scrivener、更无需复制粘贴到 Word 中。</p>

<h2 id="why-it-matters">为何重要</h2>

<p>在 Obsidian 中撰写长篇作品，可享有双向链接、原子化笔记以及真实的图谱（graph）功能。但此前的代价是导出流程繁琐不堪。借助本插件，存放你全部研究资料的知识库，亦可直接产出 EPUB 成品。</p>

<h2 id="manifest-contract">清单契约（Manifest Contract）</h2>

<p>清单的正文是一棵<strong>标题层级树（heading tree）</strong>。没有保留标题名——结构完全由你自主定义。</p>

<ul>
<li><code># H1</code> 表示全书标题（或使用 frontmatter 中的 <code>title:</code> 字段——该字段优先级更高）。</li>
<li>每个 <code>## H2</code> …… <code>###### H6</code> 均表示对应层级的章节；各章节按顺序嵌套于前一个更高层级的章节之下。</li>
<li>每个章节下，若某条列表项包含一个或多个 <code>**wikilinks**</code>，则这些链接将按源码顺序加入该章节——所链接的笔记内容将在该处内联展开。</li>
<li>不含 wikilink 的列表项将被忽略；wikilink 周围的文本（如说明性文字）也将被丢弃。</li>
</ul>

<h2 id="manifest-example">清单示例</h2>

<pre><code># The Context Layer

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
</code></pre>

<p>当清单被解析时，首先会移除配置中指定的“跳过章节”（默认为 <code>Related</code>、<code>References</code>、<code>Title Options</code>、<code>Target Audience</code>）——因此用于写作辅助的支架型章节可保留在清单中，却不会进入最终导出结果。同一跳过列表还会在每次内联引用笔记时再次应用：frontmatter 将被剥离，配置的章节被移除，首个 <code># H1</code> 标题被删除，其余标题层级整体降级，且所有 Obsidian 专属语法（信息块 callouts、嵌入 embeds、注释 comments、内部链接 internal links）均会被重写为通用格式。</p>

<h2 id="per-book-overrides">每本书的个性化覆盖设置</h2>

<p>全局设置只需在插件设置中配置一次（输出文件夹、默认导出格式、Pandoc 路径、PDF 引擎、跳过章节等）。上述任意设置均可通过清单 frontmatter 中的 <code>book_export:</code> 区块为单本书单独覆盖；包括输出路径、PDF 引擎、导出格式、目录深度（TOC depth）、分页行为（page-break behavior）及额外 Pandoc 参数等，全部支持按书定制。</p>

<h2 id="validation">校验功能</h2>

<p>插件内置专用命令：<strong>校验当前图书（Validate current book）</strong>，可在导出前检查清单完整性：是否存在缺失章节、损坏的 wikilink、不完整的元数据等。所有错误均以清晰方式报告，确保问题图书绝不会进入导出环节。</p>

<h2 id="commands">可用命令</h2>

<ul>
<li>将当前图书导出为 EPUB / PDF</li>
<li>将当前图书导出为所有支持格式</li>
<li>预览编译后的手稿（.md 文件）</li>
<li>校验当前图书</li>
<li>打开导出文件夹</li>
</ul>

<h2 id="requirements">运行要求</h2>

<p>仅限桌面端使用。<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> 是唯一硬性依赖。PDF 导出推荐使用 Typst 引擎：它是一个轻量级二进制程序，无需安装 LaTeX 即可输出专业级图书品质；xelatex / tectonic / weasyprint / wkhtmltopdf 仍作为备选方案保留。</p>

<h2 id="why-pandoc">为何选用 Pandoc</h2>

<p><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a> 是业界标准的文档转换器。目前尚无生产就绪（production-ready）的 JavaScript 或 Node.js 替代方案；而将 Pandoc 直接打包进插件又因体积庞大、需适配多平台二进制文件而极不现实。将其设为外部依赖，是务实而合理的选择。</p>

<h2 id="installation">安装步骤</h2>

<ul>
<li>手动安装，或通过 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/BRAT+plugin+for+Obsidian?ref=dsebastien.net">Obsidian 的 BRAT 插件</a> 安装</li>
<li>安装 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a>（确保其位于系统 PATH 中，或在插件设置中指定路径）</li>
<li>安装 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net">Typst</a>（推荐的 PDF 引擎）</li>
<li>打开一份清单笔记，在命令面板中运行 <strong>Book Exporter: Export current book to EPUB</strong>（或 PDF，或全部格式）</li>
</ul>

<h2 id="references">参考资料</h2>

<ul>
<li>源代码：<a href="https://github.com/dsebastien/obsidian-book-exporter?ref=dsebastien.net">https://github.com/dsebastien/obsidian-book-exporter</a></li>
<li>文档：<a href="https://dsebastien.github.io/obsidian-book-exporter/?ref=dsebastien.net">https://dsebastien.github.io/obsidian-book-exporter/</a></li>
<li>Pandoc：<a href="https://pandoc.org/?ref=dsebastien.net">https://pandoc.org</a></li>
<li>Typst：<a href="https://typst.app/?ref=dsebastien.net">https://typst.app</a></li>
<li>相关文章：<a href="https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/">https://www.dsebastien.net/announcing-book-exporter-a-new-obsidian-plugin/</a></li>
</ul>

<h2 id="related">相关资源</h2>

<ul>
<li><a href="https://obsidianstarterkit.com/?ref=dsebastien.net">Obsidian Starter Kit</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dataview+Serializer+plugin+for+Obsidian?ref=dsebastien.net">Obsidian 的 Dataview Serializer 插件</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Expander+plugin+for+Obsidian?ref=dsebastien.net">Obsidian 的 Expander 插件</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Obsidian+Publish?ref=dsebastien.net">Obsidian Publish</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Markdown?ref=dsebastien.net">Markdown</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Pandoc?ref=dsebastien.net">Pandoc</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Typst?ref=dsebastien.net">Typst</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Announcing+Book+Exporter+-+A+New+Obsidian+Plugin+(Article)?ref=dsebastien.net">《发布 Book Exporter：一款全新的 Obsidian 插件》（文章）</a></li>
</ul>
