---
title: "告别模板混乱：QuickAdd Multi 实现 Obsidian 卡片化笔记快速创建"
url: "https://mp.weixin.qq.com/s/-HSEg_MwHvjGnmiUrP1S9g"
source: "PKMer知识社区"
date: 2026-04-10
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了在 Obsidian 中如何高效管理多元笔记格式（如 Markdown、Canvas、Excalidraw 等），提出“以 Markdown 为核心、其他类型为辅助”的策略，并强调按用途分类使用非线性笔记工具。针对多格式笔记创建繁琐的问题，重点推荐 QuickAdd 插件，通过 Multi 多级菜单整合各类笔记模板与自动化动作，支持快捷键唤起和卡片化界面优化。此外，结合 Slash Commander 实现正文中快速插入与嵌入子笔记，进一步提升写作与知识管理效率。

---

<section style="color: rgb(57, 57, 57); letter-spacing: 1px; line-height: 1.75; padding-right: 15px; padding-left: 15px; font-size: 14px; font-style: normal; font-weight: 400; text-align: justify; margin-bottom: 0px;">
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 100%;">
   <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEV7TBGh5Ng2vu6JLJZLlWXxPfIuE6YrT5hBugByDyTHgpnnc87FNOBjgqxMxDHaq91wSICNXMO4YzbJv3kk77siaKLzzOG7icM90/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <section>
  <section>
   <section style="text-align: justify; font-size: 12px; color: rgb(160, 160, 160); width: 100%;">
    <p style="white-space: normal; margin: 0px; padding: 0px;">
     <span>
      由于微信限制，
     </span>
     <span style="color: rgb(52, 54, 60); font-size: 14px; text-decoration: underline 2px rgb(160, 160, 160);">
      <span>
       公众号文章内无法添加可跳转的外部链接
      </span>
     </span>
     <span>
      ，如果想要了解文内提到的更多信息，请点击文末的
     </span>
     <span>
      <span>
       阅读原文
      </span>
     </span>
     <span>
      ，查看本期内容
     </span>
    </p>
   </section>
  </section>
 </section>
 <section style="display: flex; text-align: left; margin: 10px 0px 20px;">
  <section style="display: inline-block; vertical-align: top; width: 5%; height: auto;">
   <section style="margin: 0px 0%; text-align: center; display: flex;">
    <section style="display: inline-block; width: 17px; vertical-align: top; height: auto; line-height: 0; background-color: rgb(57, 57, 57); border-width: 0px;">
     <section style="margin: 0px 0%; line-height: 0;">
      <section style="vertical-align: middle; display: inline-block; line-height: 0;">
       <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEXhbFn1YToBHGSBibFzRXro0tJI6cuAEw0P2ojJMtvEXHQ8hAGaEsYrdwZGY8Icbts77N3vwHmQQC9frm1fXSVdzb1s2OgfpycA/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; width: auto !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(62, 62, 62); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section>
   <section style="font-size: 11px; color: rgb(252, 186, 101); text-align: center; line-height: 1; letter-spacing: 0px; padding: 0px 20px;">
    <p style="margin: 0px; padding: 0px;">
     <span>
      PKMer
     </span>
    </p>
   </section>
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(62, 62, 62); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(57, 57, 57); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: top; width: 4%; height: auto;">
   <section style="margin: 0px 0%; text-align: center; display: flex;">
    <section style="display: inline-block; width: 17px; vertical-align: top; height: auto; line-height: 0; background-color: rgb(57, 57, 57); border-width: 0px;">
     <section style="margin: 0px 0%; line-height: 0;">
      <section style="vertical-align: middle; display: inline-block; line-height: 0;">
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEXiay8n59S81yIkeVXnvI4kOHep9siaEtHI9KJR3ZzyUlhVYziaSecwULOLnnyk9fibnNNt12VqB5x1U2gzDZvNwTozd51KuP6cImU/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; width: auto !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      前言：
     </span>
    </strong>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   随着 Obsidian 插件生态的日益繁荣以及原生功能的不断扩展，笔记的文件格式也愈发多元化（如 Canvas、Bases、Excalidraw 等）。如今，记录不再局限于传统的 Markdown 线性文本，还涵盖了思维导图、无限画板等多种表现形式。针对不同的内容选择最合适的记录载体，不仅能让记录过程更高效，还能显著提升信息的消化与吸收能力。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEX4iab8Z60mkek6YbLmKhHoib2icPMicadMSbia18hw014J6OFY7aFEqJPniaDfhLxc4IocNq2zeVoTWgqOXhADcFcgKWThn2VEDUazg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    然而，笔记形式的增多有时如同一把双刃剑：记录载体过于丰富，反而可能增加操作成本，导致管理混乱。因此，我建议采用“
   </span>
   <strong>
    <span>
     <span>
      以 Markdown 为核心，其他类型为辅助
     </span>
    </span>
   </strong>
   <span>
    ”的策略。Markdown 笔记主要由文本、标题、列表等基础元素构成，辅以表格整理信息或流程图进行可视化表达，所谓一图胜千言。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    对于非线性笔记，应明确其核心应用场景：例如，Excalidraw 擅长头脑风暴与素材整理，Canvas 则更适合梳理逻辑思路。它们在直观性上弥补了 Markdown 的局限，因为合适的工具才能发挥最大的效能。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    针对不同类型的文件可以采用不同文件夹来存放。类似于附件文件夹专门用来存放媒体文件，Canvas 和 Excalidraw 这类文件也可以使用专门的零散文件夹进行临时存放，后续再与配套的笔记或通过 FolderNote 插件进行迁移整理。
   </span>
  </p>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEX9swv52vPUmOiaZtooefrPJQZkMchkicrV2of6XuHMq62b9R91LLekSA71h6om4BqYiah4ic7X5DicUr8yScJpicPTgibicpQpySmFAJs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    在了解了不同类型笔记的用途后，新的挑战接踵而至：如何快速创建这些文件并将其自动存放到预设位置（如特定的归档目录或当前笔记所在的同级目录）？虽然利用模板插件可以创建预设文件，但随着模板数量的增长，逐个查找和调用的成本也随之增加。而
   </span>
   <strong>
    <span>
     QuickAdd
    </span>
   </strong>
   <span>
    插件正是解决这一问题的利器。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     QuickAdd
    </span>
   </strong>
   <span>
    作为 Obsidian 中极具威力的自动化插件，旨在显著优化笔记的创建与处理效率。它支持通过自定义命令、模板 (Template)、捕获 (Capture) 及宏 (Macro) 等多种核心功能，实现一键新建笔记、快速插入数据或批量处理文件。利用其
   </span>
   <strong>
    <span>
     Multi
    </span>
   </strong>
   <span>
    （多级菜单）功能，我们可以将不同类型的笔记创建入口整合在一起，实现分类明确的精准分发。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    尽管 QuickAdd 的功能异常强大，但其配置门槛也让不少新手望而却步。下文我将结合自己的实操经验，分享一套完整且美观的高效工作流方案。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      利用 QuickAdd Multi 整合多类型笔记创建：
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEUSzico99nGav6S6zMlWa5zsgpD3qnReGv778mbvsfJ0WjvyPCUbafoPsuS0SLTiaq9mA59Q7HB8yv9OibmDoA2b9TgeKcibSWXLibo/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   在 QuickAdd 设置中添加一个
  </span>
  <strong>
   <span>
    Multi
   </span>
  </strong>
  <span>
   选项。通过预先配置好的 Template 或 Capture 动作，将其嵌套在 Multi 菜单下，即可一键呼出新建列表，涵盖 Excalidraw、Markdown、Markmind、Kanban 等各类文件。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWvMeo7k1hMiak5UFECzibIiaUstZukZxr5nSozvMDQ3xELdr5InVS0efDMu9yCbRkUF0pTSLOYG13FiaKG79qelGElJosoZY16Ic4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   实例，新建 Excalidraw 的配置如下：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWADFB225o2JwXNls05JJfAVGZ7dibvgn8xoPIricDrxOxiaYWQMAicd0nhHVZWHo990hLiaITk5HncjL0Em746yEthoxxdK3S2CDR8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   如上图所示，在新建 Excalidraw 配置中，你可以灵活定义文件模板、文件名格式、存储路径以及创建后的打开方式。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEVXibHQ024ZNpyd8eFHQEpPX9jia01mKNq5lRoqIvWbDaPPx19TibFNLcM6kibmC7HFuQibWKO8cbWWzCwLyI5Y9mHBiaibeM79xibEbaQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   对于更加复杂的逻辑，可以通过
  </span>
  <strong>
   <span>
    <span>
     Macro
    </span>
   </span>
  </strong>
  <span>
   调用 JavaScript 脚本来实现。例如，在创建项目 (Project)、任务笔记 (TaskNote) 或日记 (Journal) 时，脚本可以根据当前上下文动态配置目标文件夹、命名规则及模板内容，极大扩展了工作流的灵活性。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWHtPMIHFp96JsHBQKK7bku5k64O2y8tCB7uwu1ODoorMCohn2ls3ibZq9lvxSic14gTy5hIBbTsZMyK8nTvvRHQkRFjBC0qCfqE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEVH0AhpSlibDRCNliafsvHricAA3VibYwVNkSyONtNLJic8dxcXaxwzPATyefRPibbRQDFjm86guHxYibwZtgZaDXibetZW8w9cFZicXC4A/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   Multi 菜单不仅支持直接嵌套单一动作，还可以进行
  </span>
  <strong>
   <span>
    层级嵌套
   </span>
  </strong>
  <span>
   。例如，为 Markmind 插件配置模板时，可以创建一个二级菜单，并在内部提供“Rich 模式”与“Markdown 模式”两个选项。这种树状结构让选择过程更加直观，支持快速点击创建或随时返回上一级。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEVH4c9qAs8l8g7ufVPPg9FicibDXDBHL7KBuz9yNRr1TOc1nkH4VPP6XXRHZaz3yqiaha8GShCemIQ55P6o1IB4qBgYCvgxo1DhN8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   最后，为该 Multi 动作设置一个全局快捷键。考虑到
  </span>
  <span>
   <span>
    Ctrl+N
   </span>
  </span>
  <span>
   通常用于快速创建默认笔记或草稿，我推荐使用
  </span>
  <span>
   <span>
    Ctrl+Shift+N
   </span>
  </span>
  <span>
   来唤起这个全功能新建面板。为了进一步提升视觉体验，我还编写了一段 CSS 代码，将原本单一的列表转换成更加现代的
  </span>
  <strong>
   <span>
    <span>
     卡片化界面样式
    </span>
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section>
  <ul class="code-snippet__line-index code-snippet__js">
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
   <li>
   </li>
  </ul>
  <pre class="code-snippet__js"><code><span><span>/* 仅针对 QuickAdd（prompt-results 内出现 quickadd-choice-suggestion 的模态框） */</span></span></code><code><span><span>.modal-container.mod-dim</span><span>:has</span>(<span>.prompt-results</span> <span>.quickadd-choice-suggestion</span>) {</span></code><code><span><br /></span></code><code><span>  <span>/* 居中显示 */</span></span></code><code><span>  <span>.prompt</span> {</span></code><code><span>    <span>position</span>: absolute;</span></code><code><span>    <span>top</span>: <span>50%</span>;</span></code><code><span>    <span>left</span>: <span>50%</span>;</span></code><code><span>     <span>transform</span>: <span>translate</span>(-<span>50%</span>, -<span>50%</span>);</span></code><code><span>    <span>margin-top</span>: <span>0</span>;</span></code><code><span>  }</span></code><code><span>  <span>/* 设置quickadd 的提示框为 */</span></span></code><code><span><br /></span></code><code><span>  <span>/* 1. 容器改为网格布局 */</span></span></code><code><span>  <span>.prompt-results</span> {</span></code><code><span>    <span>display</span>: grid <span>!important</span>;</span></code><code><span>    <span>grid-template-columns</span>: <span>repeat</span>(auto-fit, <span>minmax</span>(<span>160px</span>, <span>1</span>fr));</span></code><code><span>    <span>/* 自动填充，每列最小140px */</span></span></code><code><span>    <span>gap</span>: <span>12px</span>;</span></code><code><span>    <span>/* 卡片间距 */</span></span></code><code><span>    <span>padding</span>: <span>15px</span>;</span></code><code><span>    <span>max-height</span>: <span>400px</span>;</span></code><code><span>    <span>overflow-y</span>: auto;</span></code><code><span>  }</span></code><code><span><br /></span></code><code><span>  <span>/* 2. 卡片基础样式 */</span></span></code><code><span>  <span>.suggestion-item.quickadd-choice-suggestion</span> {</span></code><code><span>    <span>display</span>: flex;</span></code><code><span>    <span>flex-direction</span>: column;</span></code><code><span>    <span>align-items</span>: center;</span></code><code><span>    <span>justify-content</span>: center;</span></code><code><span>    <span>padding</span>: <span>20px</span> <span>10px</span>;</span></code><code><span>    <span>border-radius</span>: <span>8px</span>;</span></code><code><span>    <span>background-color</span>: <span>var</span>(--background-secondary);</span></code><code><span>    <span>border</span>: <span>1px</span> solid <span>var</span>(--background-modifier-border);</span></code><code><span>    <span>/* transition: all 0.2s ease; */</span></span></code><code><span>    <span>cursor</span>: pointer;</span></code><code><span>    <span>text-align</span>: center;</span></code><code><span>  }</span></code><code><span><br /></span></code><code><span>  <span>/* 3. 悬停效果 (Hover) */</span></span></code><code><span>  <span>.suggestion-item.quickadd-choice-suggestion</span><span>:hover</span> {</span></code><code><span>    <span>background-color</span>: <span>var</span>(--background-modifier-hover);</span></code><code><span>     <span>transform</span>: <span>translateY</span>(-<span>2px</span>);</span></code><code><span>    <span>box-shadow</span>: <span>04px</span> <span>12px</span> <span>rgba</span>(<span>0</span>, <span>0</span>, <span>0</span>, <span>0.1</span>);</span></code><code><span>  }</span></code><code><span><br /></span></code><code><span>  <span>/* 4. 选中状态样式 (Selected) */</span></span></code><code><span>  <span>.suggestion-item.quickadd-choice-suggestion.is-selected</span> {</span></code><code><span>    <span>background-color</span>: <span>var</span>(--interactive-accent) <span>!important</span>;</span></code><code><span>    <span>color</span>: white <span>!important</span>;</span></code><code><span>    <span>border-color</span>: <span>var</span>(--interactive-accent);</span></code><code><span>  }</span></code><code><span><br /></span></code><code><span>  <span>/* 5. 文字样式调整 */</span></span></code><code><span>  <span>.suggestion-item</span> <span>p</span> {</span></code><code><span>    <span>margin</span>: <span>0</span>;</span></code><code><span>    <span>font-size</span>: <span>0.9em</span>;</span></code><code><span>    <span>font-weight</span>: <span>500</span>;</span></code><code><span>    <span>word-break</span>: break-word;</span></code><code><span>  }</span></code><code><span>}</span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      使用 Slash Commander 实现行内快速创建与嵌入
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEU6dFUanOgS22SkYEDR37eAxlcNhHNJCGQcarYnk74HtxjticwgVibXVqicQ1Jsa8wxMfF4xNdFXyOTePlc0USDjFAeIspndKBwT4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   如果你希望在正文书写过程中快速插入并关联子笔记，可以配合
  </span>
  <strong>
   <span>
    Slash Commander
   </span>
  </strong>
  <span>
   插件实现“正斜杠菜单”调用：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEXUiaXaSuSRFB8I2mDiav59NgCRJtvgV2icFaewp0RZKcpJxbc3A15aaV3libInjBxk3ewWjxwp2orjffrO0a88DcybPCxiaehhicVNQ/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   在 Slash Commander 中关联对应的 QuickAdd Insert 动作。其核心逻辑是在 QuickAdd 的 Template 参数中配置笔记链接的插入行为及文件的打开方式。
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEX9Agia6QribHHDoh8s5pGWZQEwWH46CDK7TS79zHkMOfRm92A50clzrflEeJ9P7M5kqFrcZZ0oyRuf0LWlGYxtQxLSzbg9YwX9A/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="vertical-align: middle; width: auto !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   关于 SVG 的创建可以采用
  </span>
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    QuickAdd脚本-插入并编辑SVG文件
   </span>
  </span>
  <span>
   来实现，其他的都可以通过 Quickadd 的 Template 模式来生成。
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="margin: 15px 0px 20px;">
  <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      - THE END -
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="display: flex; width: 100%;">
  <section style="height: auto;">
   <section>
    <section style="display: inline-block; width: auto; vertical-align: bottom; height: auto; padding: 0px 0px 0px 4px;">
     <section style="display: grid; width: 100%; overflow: hidden; line-height: 1.6; font-size: 16px; letter-spacing: 0px; color: rgb(0, 0, 0);">
      <section>
       <section>
        <section style="display: inline-block; width: 100%; vertical-align: middle; border-style: dashed; border-width: 0px 0px 2px; border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(57, 57, 57); height: auto;">
         <section style="margin: 0px 0%;">
          <section style="border-top: 1px dashed transparent;">
           <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
           </svg>
          </section>
         </section>
        </section>
       </section>
      </section>
      <section style="display: flex;">
       <svg height="100%" viewBox="0  0 349 31" width="100%" xmlns="http://www.w3.org/2000/svg">
        <svg height="61.15%" width="45.1776%" x="-5.55034%" xmlns="http://www.w3.org/2000/svg" y="26.7512222195471%">
         <foreignObject height="100%" width="100%">
          <section style="font-size: 7px; height: 100%;">
           <section style="font-size: 12px; color: rgb(52, 54, 60); text-align: center;">
            <p style="margin: 0px; padding: 0px;">
             <span style="color: rgb(255, 202, 0);">
              <span>
               //
              </span>
             </span>
             <span style="color: rgb(255, 202, 0);">
              <span>
              </span>
             </span>
             <span>
              <span>
               长按二维码·加入我们
              </span>
             </span>
            </p>
           </section>
          </section>
         </foreignObject>
        </svg>
       </svg>
      </section>
      <section style="padding-top: 9%;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
     <section style="display: flex;">
      <section style="display: inline-block; vertical-align: middle; width: 25%; height: auto; border-style: dashed solid dashed dashed; border-width: 0px;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/mmbiz_jpg/dibCdrCystEWK5iaHKpux9kZhSM1qy2yOk7vBicsFs5EFiaSIZbhpOuu2bAmCibtrnzR1KAoficvAORJ1IHn5iaP482WsW3wj31njdCicbQprZCf0DI/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="vertical-align: middle; width: auto !important; height: auto !important;" />
        </section>
       </section>
       <section>
        <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
         <p style="margin: 0px; padding: 0px;">
          <span>
           QQ群
          </span>
         </p>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: top; width: 2%; height: auto;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 25%; height: auto;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEUL7yiaSUYE067Lc1EvE1iaJdZHT3lOMAKf312RfVNbhAumV9UEfWCmB2Cso2MIwUCmicn1Uvn7y3Za5pJFKLKKzoAqibicLv11xibzI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="vertical-align: middle; width: auto !important; height: auto !important;" />
        </section>
       </section>
       <section>
        <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
         <p style="margin: 0px; padding: 0px;">
          <span>
           微信群
          </span>
         </p>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 5%; height: auto;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: auto; height: auto; padding: 0px 0px 0px 16px;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/mmbiz_jpg/dibCdrCystEV3ZLxhuoFMGURcj0icv4m5RPQVInuPNictmnBicvsBQ1ZhbZ3j8EYEbuWXeuEDIYrvKxpFDWbVmXLWW4zn79mobcXibavWU6YVfYo/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="vertical-align: middle; width: auto !important; height: auto !important;" />
        </section>
       </section>
      </section>
     </section>
     <section>
      <section style="display: inline-block; vertical-align: middle; width: 49%; border-style: dashed; border-width: 0px 0px 2px; border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(57, 57, 57); height: auto;">
       <section style="margin: 0px 0%;">
        <section style="border-top: 1px dashed transparent;">
         <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
         </svg>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 17%; height: auto;">
       <section style="text-align: center; margin: 0px 0%; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 61%; height: auto;">
         <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEVULNiavp1oFicicic60wx50t8iaWs4U8trP0RtC52fbiaJa8pW1eiaPciazj9NdUK2Vtqicic8zDANQibTk3zWZ2fsTxxjBCAtgTEAr1VrDE/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="vertical-align: middle; width: auto !important; height: auto !important;" />
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 31%; border-width: 0px 0px 2px; border-style: dashed; border-bottom-color: rgb(57, 57, 57); height: auto;">
       <section style="margin: 0px 0%;">
        <section style="border-top: 1px dashed transparent;">
         <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
         </svg>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section>
  <section style="display: grid; width: 100%; overflow: hidden; line-height: 1.6; font-size: 16px; letter-spacing: 0px; color: rgb(0, 0, 0);">
   <section style="display: flex;">
    <svg height="100%" viewBox="0  0 353 68" width="100%" xmlns="http://www.w3.org/2000/svg">
     <svg height="84.43%" width="42.1123%" x="57.3167%" xmlns="http://www.w3.org/2000/svg" y="-1.91416364471241%">
      <foreignObject height="100%" width="100%">
       <section style="height: 100%; font-size: 13px;">
        <section style="font-size: 12px; color: rgb(160, 160, 160); text-align: center;">
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong style="letter-spacing: 0px;">
           <span>
            作者
           </span>
          </strong>
          <span style="letter-spacing: 0px;">
           <span>
            ：熊猫别熬夜
           </span>
          </span>
         </p>
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong>
           <span>
            来源
           </span>
          </strong>
          <span>
           ：PKMer
          </span>
         </p>
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong>
           <span style="letter-spacing: 0px;">
            <span>
             排版
            </span>
           </span>
          </strong>
          <span style="letter-spacing: 0px;">
           <span>
            ：Wis_Ocean
           </span>
          </span>
         </p>
        </section>
       </section>
      </foreignObject>
     </svg>
    </svg>
   </section>
   <section>
    <section style="text-align: center; line-height: 0; font-size: 9px; height: 100%;">
     <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 85%; height: auto;">
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWSBR0PTCe5urHRpzHjAXcwN636QFpj1KDkMreicicxl1pOTCfiaEJgYAkb5PzbgOYLNSeZXQwibstOPwGNbJYggZb8suWO83Aicmuw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=19" style="vertical-align: middle; width: auto !important; height: auto !important;" />
     </section>
    </section>
   </section>
   <section>
    <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
    </svg>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0%;">
  <section style="border-top: 1px dashed transparent;">
   <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
   </svg>
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px;">
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="display: flex;">
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(227, 163, 92);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center; margin: 0px;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(255, 222, 110);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(255, 236, 196);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto; padding: 0px 10px;">
   <section style="font-size: 10px; letter-spacing: 2px;">
    <p style="margin: 0px; padding: 0px;">
     <span>
      点击阅读原文查看更多
     </span>
    </p>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0.5em 0px;">
    <section style="background-color: rgb(57, 57, 57); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
 </section>
</section>
<p style="display: none;">
 
 
</p>
