---
title: "Obsidian 周报 2026-03-27：CLI 终端优化、Bases 日历视图、AI 重构三连发"
url: "https://mp.weixin.qq.com/s/WDyso3sgXHt7cXHto54PlA"
source: "PKMer知识社区"
date: 2026-03-29
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文为 Obsidian Weekly 2026-03-27 期简报，聚焦三大主题：CLI 终端性能优化（新版二进制 CLI 显著提速并增强自动补全）、Bases 日历视图插件（支持日期驱动的日程规划与元数据同步）及 AI 插件三连更（YOLO v1.5.3 实现多窗口聊天、精准编辑器联动与新标签页快捷入口）。同时汇总了官方 v1.12.7 版本的多项 Bug 修复与改进，以及 Graphic Organizer、Synaptic View 等新增实用插件。

---

<section style="color: rgb(57, 57, 57); letter-spacing: 1px; line-height: 1.75; padding-right: 15px; padding-left: 15px; font-size: 14px; font-style: normal; font-weight: 400; text-align: justify; margin-bottom: 0px;">
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEUQ7IicYxWfvicl4vppe6N6zVz94CbRYyC3qJINqhKsRIqTOzwQPYG4ElZYbibBjyIBOBiatox6RlbjYgQcj7K9m2V2cfuzJCllxG8/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 650px !important;" />
 </section>
 <section>
  <section>
   <section style="text-align: justify; font-size: 12px; color: rgb(160, 160, 160); width: 100%;">
    <p style="white-space: normal; margin: 0px; padding: 0px;">
     <span>
      由于微信限制，
     </span>
     <span style="color: rgb(52, 54, 60); font-size: 14px;">
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
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEULafowCicQsAlD0HAkEjLPUQquE6bZDMRU5jlO3XcILJIo6C5C4VYBicVIUR40NW70nsBQgl4t7icqGhoNU91ib9VLu59sbdUOYZ8/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
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
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEUaGZmuxnPrtmD18zCIIWu2KRLRA5rB35PhShrjHnWfleiaDCKibhK6mQLibkFD99LTg6j6hqjBazjzqcX8FibHs1gibvvmO1LF5VDM/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="text-align: center; font-size: 19px;">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Obsidian Weekly 2026-03-27：
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    CLI 终端优化、Bases 日历视图、
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    AI 重构三连发
   </span>
  </p>
 </section>
 <section style="text-align: left; font-size: 12px; color: rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <em>
    <span>
     <span>
      统计时间：2026-03-20 12:00 ~ 2026-03-27 12:00
     </span>
    </span>
   </em>
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
 <section style="text-align: center; font-size: 18px; color: rgb(169, 152, 255);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    官方资讯
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <b>
     <span>
      1.12.7 版本说明
     </span>
    </b>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   包含截至
  </span>
  <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
   <span>
    Obsidian Desktop v1.12.7
   </span>
  </span>
  <span>
   的所有新功能和错误修复。
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     改进
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     Obsidian CLI
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Obsidian Installer 现在捆绑了一个新的二进制文件用于 CLI。此新方法取代了调用 Electron 二进制文件的旧方法，显著提升了终端交互速度。需要下载最新的安装程序。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在使用
     </span>
     <span>
      <span>
       id=
      </span>
     </span>
     <span>
      参数时，为终端界面 (TUI) 添加了 Obsidian 命令的自动补全功能。
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     Bug修复
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     Obsidian CLI
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复了 Obsidian CLI 在 macOS 上错误检查 Linux 特定目录的问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      将 macOS 和 Linux 上的 CLI socket 文件更改为隐藏的 dotfile。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    编辑器
   </span>
  </strong>
 </p>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复了未选中文本时进行复制、剪切和粘贴的几个问题。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     复制并粘贴一行时，光标不再处于错误位置。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     在表格中，未选中文本时进行复制或剪切，现在能正确仅复制单元格内容。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     当有文本跨多个光标被选中时粘贴 URL，现在会将每个选中的内容包裹为 Markdown 链接（
    </span>
    <span>
     <span>
      [selected text](url)
     </span>
    </span>
    <span>
     ）。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复了阅读模式下，callout 内的图片显示不必要滚动条的问题。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复了在实时预览中双击图片无法重置其大小的问题。
    </span>
   </p>
  </li>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    开发者
   </span>
  </strong>
 </p>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <section>
    <span>
     安装程序已更新为使用 Electron v39.8.3（需要下载最新的安装程序）。
    </span>
   </section>
  </li>
 </ul>
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
 <section style="text-align: center; font-size: 18px; color: rgb(169, 152, 255);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    插件新闻
   </span>
  </p>
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
      新增
     </span>
    </strong>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
   <span>
    Calendar Bases
   </span>
  </span>
  <span>
   by Edrick Leong
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEW99o5g6icRyuFLyLibu47I0nevR4Eqq80DHQRr5cKrGUQIyKicS84DKuuwjpv6dGURwQwcd2MiaqtfowLQhZu9lLXu5KpS7QLVwB4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Calendar Bases 插件可将 Obsidian Bases 的结果转换为日历，这样带有日期属性的笔记就能在月视图中显示在其对应的位置。该插件专注于已包含开始日期的条目，当某条目持续多天时，还能处理结束日期。你可以在日历上移动项目来重新安排时间，插件会更新笔记的前置元数据以与之匹配，这使得该视图不仅可用于查看 Vault 中已有的内容，还能用于规划。它还支持直接从日历打开条目，并可使用上下文菜单执行相关操作。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Graphic Organizer
   </span>
  </span>
  <span>
   by Nick Le Guillou - Superhuman Curiosity
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEVdcBcnIrOAd4BiaibqMgBY0wQsaKvochftsdDzK3m7TONyRqibfmDticib3suu4o1ZxAUQL3c24WNXdvwMRbp9F7CuKnhpO7SEPy1s/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Graphic Organizer 插件能将存储库转换为可视化树状结构，在可缩放的画布上显示文件夹和文件。它帮助人们更快理解大型结构，无需停留在文件资源管理器中就能移动内容。点击即可打开文件，文件夹可按需展开，存储库中的更改会实时显示。你可以将文件或文件夹拖入其他文件夹，使用右键菜单创建或删除项目，并通过清晰的图标识别不同的文件类型。该视图还添加了大型文件夹警告、可配置的间距、缩放限制和可选的平滑动画，这让存储库变得杂乱时的导航更加轻松。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Synaptic View
   </span>
  </span>
  <span>
   by Yongmin
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEVs6x97KOSdYFczqdq3K2UXic1pricjjPxWuDySQObssusvfHCviaFRxvNzb93SJtoAJB7nPe8038Dicpk4lRkQqdhyh5hes9c0zxE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Synaptic View 插件能将一条笔记转变为可配置的仪表盘，无需手动构建主页，就能打开你最需要的文件、网页、日志和日历视图。它添加了笔记、URL、定期笔记和基于日期的导航的快速访问按钮，还可以替代新标签页视图，让仪表盘随时触手可及。每日按钮和日历按钮能显示未完成任务的数量，这使得日常工作一目了然，便于查看。按住 Ctrl 或 Cmd 键点击，可在侧边窗格中以编辑模式打开受支持的项目，这在你想同时进行读写操作时非常有用。设置界面还包含图标选择、排序、可见性、默认视图以及一些显示清理功能。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    LighterPack importer
   </span>
  </span>
  <span>
   by Nicola Siniscalchi
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEUj7TwWxGlQoq0VLPSHlnicQJib33A9zqiaYUfzv8PMtvjJEJLoZV4orucr6U7dyyUsibVp7ynX26IVOJn524MFXVLKlPDzkNIePnM/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    LighterPack 导入插件可将 lighterpack.com 上的公开打包清单导入你的知识库，并将其转换为一组简洁的 Markdown 笔记。它会为不同类别创建文件夹，为每个物品添加笔记，并生成一个汇总页面，其中包含总计、类别细分和重量分布图表。这使得旅行或徒步装备清单在导入后更易于浏览、链接和编辑，即使在离线状态下也是如此。导入流程简单，通过功能区操作和命令面板条目即可完成，只需输入共享清单的 URL 即可。
   </span>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     LskyPro Upload V2
    </span>
   </span>
   <span>
    by 3kk0
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Obsidian 的自动图片上传插件，LskyPro Upload V2 插件会将笔记中的本地图片发送到自建的 LskyPro 服务器，并将其替换为托管链接，这样图片处理就不会占用笔记库空间。该插件兼容 V1 和 V2 版本的 API，支持人们常用的文件插入方式，包括粘贴、拖放、右键操作以及基于命令的批量处理。此外，该插件还能上传当前笔记中的所有本地图片，也可在需要时将远程图片下载回来。相关设置涵盖网络图片处理、路径修复、可选的源文件删除、图片处理以及上传并发等功能。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <b>
     <span>
      更新
     </span>
    </b>
   </p>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      AI 增强与智能助手
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     YOLO
    </span>
   </span>
   <span>
    By Lapis0x0
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    1.5.3 多窗口联动与底层架构重构 🚀
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      🪟 多窗口支持与编辑器联动
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🌐 原生多窗口 Chat：现在支持在侧栏、新标签页或独立窗口中同时打开多个 Chat 窗口，互不干扰。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🎯 精准路由联动：重构了编辑器与对话框的通信逻辑。选区引用、文件添加、续写参数等操作现在可以准确地路由到目标 Chat 窗口。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ⚡ 新标签页入口：在 Obsidian 空白“新标签页”中新增了直接打开 YOLO 聊天的快捷入口，并支持右侧分屏打开。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📍 悬浮窗体验优化：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        优化了 Cursor Chat 触发的 Quick Ask 弹窗定位，默认显示在选区下方，避免遮挡原文。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        进入选区改写模式时，Quick Ask 状态位将明确显示为“改写”，消除歧义。
       </span>
      </p>
     </li>
    </ul>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      ⚙️ 底层架构与 Provider 增强
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🧩 协议与 Provider 解耦：正式将 Provider 类型与底层 API 协议拆分。现在支持在 Provider 级别自由切换 API 类型（OpenAI Compatible / OpenAI Responses / Gemini / Anthropic）。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🔐 ChatGPT OAuth 支持：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        支持通过 ChatGPT OAuth 登录并作为自定义 Provider 使用。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        支持更多 OAuth 渠道模型，并部分修复了思维链（CoT）摘要获取不到的问题。
       </span>
      </p>
     </li>
    </ul>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🛡️ 安全与清理：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        为删除 Provider 操作增加了二次确认机制，防止误删。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        移除了已过时的 base 模型相关冗余逻辑。
       </span>
      </p>
     </li>
    </ul>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      🔍 搜索与 AI 工具
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🌐 内置联网搜索 (OpenAI)：新增 GPT 工具类型并内置 Web Search 开关。OpenAI 官方及兼容协议模型无需手填参数即可直接启用联网搜索。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🐞 引用来源修复：修复了 GPT 模型开启 Web Search 后 Source（来源）不可见的 Bug。`
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      💄 UI/UX 细节优化
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📏 输入框高度调整：支持通过拖拽直接调整输入框高度。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🎨 设置面板优化：整体优化了“模型设置”分区的样式，内容呈现更加清晰、符合逻辑。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🛠️ 独立窗口适配：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        修复了独立窗口下宽/窄顶栏样式无法切换的 Bug。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        优化了对话间的间距与图表文字尺寸，视觉效果更统一。
       </span>
      </p>
     </li>
    </ul>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   1.5.3.1 后台 Agent 与基础设施完善
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      🤖 后台 Agent 与多任务处理
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ⛓️ 后台挂机能力：Agent 现支持在后台运行，长任务执行期间你可以切换到其他文档或窗口，无需原地等待。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🔔 任务通知提醒：新增 Agent 任务通知系统，包括工具调用审批提醒与任务完成提醒
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📊 状态栏交互：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        Obsidian 右下角状态栏现会实时显示运行中的 Agent 数量及审批状态。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        快速导航：点击状态栏图标可弹出当前活跃会话列表，并支持一键在右侧分屏打开。
       </span>
      </p>
     </li>
    </ul>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      🌐 网络连接与协议重构
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🚀 Node Fetch 传输：重构了 OpenAI/Anthropic 等渠道的请求链路，通过 Node.js 层进行转发，有效解决了部分渠道（如 Nvidia/NIM）在 Obsidian 环境下的跨域（CORS）限制，并提供更完整的流式支持。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🔗 远程 MCP 代理：新增远程 MCP HTTP/SSE 代理支持，自动兼容 HTTP_PROXY 等系统环境变量。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🔐 OAuth 交互优化：在配置 ChatGPT OAuth 提供商时，自动隐藏不适用的 API Key 和 Base URL 输入框。
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      💄 交互体验与智能增强
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📏 输入框高度记忆：手动调整后的输入框高度会自动保存，并在侧边栏、新标签页、新窗口中保持同步。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🏷️ 标题实时同步：Chat 标签页/窗口的标题现会跟随对话标题自动更新，便于多开时快速识别。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ✍️ 回复片段引用：支持选中 AI 回复的某一部分，以 Mention 形式引用到输入框中参与后续对话。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📅 时间变量支持：系统提示词现支持引用当前日期、小时和分钟等时间变量，增强 Agent 的时间感知。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🎯 聊天命名优化：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        原“工具模型”更名为更准确的“对话命名模型”。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        对话命名触发点提早至用户首次输入阶段，避免 Agent 运行期间长时间显示“未命名”。
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        优化重命名交互：点击编辑标题后，编辑图标直接切换为确认图标，点击即可保存。
       </span>
      </p>
     </li>
    </ul>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      🐞 Bug 修复与细节优化
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       📜 滚动逻辑修复：修复了聊天记录在鼠标 Hover 时可能产生的异常滚动问题。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ✨ 自动滚动策略：优化了生成时的自动滚动算法，修复了停止生成按钮可能横向遮挡内容的 UI 问题。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       🏗️ 品牌统一：统一了控制台日志命名，前缀现已全部规范化为 YOLO。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ⌨️ 新增命令：新增 Obsidian 命令，支持在当前 YOLO 视图中直接新建对话。
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Copilot
   </span>
  </span>
  <span>
   By Logan Yang
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Composer V2：editFile 工具替换 replaceInFile，实现更可靠精确的文件编辑
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      从 Copilot 聊天面板拖拽笔记和源文件到编辑器，即时插入 Wiki 链接
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Azure OpenAI 和 Azure Foundry 统一为单一 Azure Provider
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Obsidian Bases 支持：base:create 命令、.base 活动笔记支持、只读 obsidianBases CLI 工具
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      LM Studio：支持 Responses API 并复用 KV 缓存，本地模型对话更快更高效
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Gemini Embedding 2 预览支持
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      GitHub Copilot Chat 支持工具调用
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      自动重命名文件以匹配主题标题
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      OpenRouter 提示缓存支持
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Miyo：可自定义库名称、远程后端移动端重新索引、许可证认证头
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      CLI 工具升级：每日/随机阅读工具、推理摘要、增强指令、每日笔记模板修复
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Agent 和搜索修复：内联引用、查询去重、答案源优先级、扩展搜索限制
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      UI/UX 打磨：Quick Ask 面板定位、LaTeX 渲染、Ollama numCtx、“None” 系统提示选项
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      本地模型修复：剥离泄露的特殊 token，agent 工具路径中的 vault.read
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      YouTube 转录修复：支持经典和现代 DOM 结构
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      Tiktoken CDN 超时深度防御修复
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Khoj
   </span>
  </span>
  <span>
   By Debanjum Singh Solanky
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复禁用记忆后使用 Web 应用时，从未设置聊天模型的用户遇到的问题
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复 Khoj 云端过时横幅显示问题
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Notemd
   </span>
  </span>
  <span>
   By Jacob
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      核心亮点
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       将所有 Mermaid 图表生成/改写/批量任务链路统一接入自动修复，显著减少图表渲染失败和人工返工
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       侧边栏升级为可自定义的一键工作流按钮系统，支持内置动作自由组装，内置默认 One-Click Extract 工作流
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      破坏性更新
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Mermaid 自动修复默认开启且触发范围扩大（Process、Generate from title、批量生成、研究总结、Mermaid 摘要、翻译等），若需旧行为请在设置中关闭
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新特性
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       所有 Mermaid 相关任务完成后自动执行修复
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可视化 Workflow Builder，无需手写 DSL 即可创建/编辑自定义工作流
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       工作流错误策略支持 stop_on_error 与 continue_on_error
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       侧边栏按功能分组（核心/生成/翻译/知识/工具），增加快捷工作流、进度和日志区域
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      Bug 修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复 Mermaid 修复仅在部分生成功能中生效的问题，现统一对目标文件/目录执行
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复批量生成场景下 Mermaid 修复目标目录解析分散的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复自定义工作流 DSL 配置异常导致按钮不可用的问题，配置错误时回退到默认工作流并提示警告
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Vault LLM Assistant
   </span>
  </span>
  <span>
   By Brians Tjipto
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新功能
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持通过直接 API 集成 Anthropic Claude 模型
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持在请求中包含 Markdown 图像（库内图像）到 OpenAI、Gemini 和 Claude 视觉模型
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      改进
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新预定义模型列表，包含 Claude 3 和 Claude 3.5 系列
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Note Companion AI
   </span>
  </span>
  <span>
   By Benjamin Ashgan Shafii
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新功能
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新增命令和上下文菜单：将选中文本提取到新笔记，自动替换为 Wiki 链接
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       AI 聊天界面集成提取功能，支持斜杠命令 /extract to new note
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       实现编辑器选择跟踪机制，即使在聊天界面获得焦点时也能可靠提取
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      技术改进
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       大幅改进 CSS 可访问性、视觉清晰度，侧边栏和聊天界面样式统一
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       增强聊天斜杠命令系统，支持编辑器上下文，执行后可靠移除触发文本
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Pure Chat LLM
   </span>
  </span>
  <span>
   By Justice Vellacott
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      依赖更新与常量修改
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新 eslint、typescript-eslint 等依赖
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       在常量中添加 think 属性
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       注释掉 LLMService.ts 中的 requestUrl 调用
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Steward
   </span>
  </span>
  <span>
   By Dang Nguyen
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新增
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       回退多个操作
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       SubAgent 系统：生成具有特定能力的专用代理
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       SPAWN_SUBAGENT 工具
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       通过 frontmatter 中的 conversation_title 更新嵌入标题
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       变更
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       技能系统：用 read_content 替换 use_skills，按路径按需读取
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       命令输入显示当前模型和 Provider
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       将 grep 工具处理移至单独工具 vaultExists
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       历史视图 UI 改进，不显示子代理笔记
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       VaultCreate 可创建空文件夹
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       VaultList 渲染和搜索行为改进
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       优雅处理 no_stool_error
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       编辑审查更新为通用用途
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       帮助视图显示禁用的规则和技能
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       修复
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复使用 DOM 事件而非文件内容导致的对话指示器问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Daily News Briefing
   </span>
  </span>
  <span>
   By Adam Chen
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       1.11.5
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复每日新闻内容缓存：仅在新闻生成成功时缓存
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       移除重复通知，添加更多失败信息
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加计划时间
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     内容创作与编辑增强
    </span>
   </strong>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Nova
   </span>
  </span>
  <span>
   By Shawn Duggan
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     1.4.0 更新内容
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        写作分析面板
       </span>
      </strong>
      <span>
       （本地运行，无需 AI）：
      </span>
     </p>
    </li>
    <ul class="list-paddingleft-2" style="padding-left: 20px;">
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        可读性等级（Flesch-Kincaid 年级水平 + 通俗标签）
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        编辑器内下划线高亮：长句、被动语态、副词、弱强调词，按严重程度分色
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        可折叠面板显示：字数、句数、阅读时间、被动语态比例、副词密度、强调词数量
       </span>
      </p>
     </li>
     <li>
      <p style="margin: 0px; padding: 0px;">
       <span>
        手动分析按钮，支持 frontmatter 中 nova-writing: false 禁用
       </span>
      </p>
     </li>
    </ul>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可自定义长句阈值
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        自动上下文改进
       </span>
      </strong>
      <span>
       ：增删 [[wikilinks]] 时自动更新上下文面板
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        <span>
         移动端优化
        </span>
       </span>
      </strong>
      <span>
       ：写作面板触摸适配、字体大小、滚动；隐私指示器左对齐
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        <span>
         Bug 修复
        </span>
       </span>
      </strong>
      <span>
       ：修复撤销/重做不触发分析更新；弱强调词重复高亮；Ollama 末尾斜杠导致连接失败；降低副词和强调词误报阈值；token 预算条在用量极小时隐藏，改为显示百分比
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Sheet Plus
   </span>
  </span>
  <span>
   By ljcoder
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     2.8.8 (2026-03-26)
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新 univer 版本至 0.18.0
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       优化嵌入式表格渲染逻辑
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Continuous Mode
   </span>
  </span>
  <span>
   By Michael Schrauzer
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    修复：打字机滚动仅在箭头导航时工作，实际输入时无效的问题
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Inline Admonitions
   </span>
  </span>
  <span>
   By Scott Tomaszewski
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    支持正则表达式 Inline Admonitions 块
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Codeblock Customizer
   </span>
  </span>
  <span>
   By mugiwara
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修改
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       增加 Mac 修饰键支持
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      Bug 修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复编辑模式下表格中内联代码在 PDF 打印未启用时不渲染的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复编辑模式下未换行代码块滚动无效的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复 PDF 打印时排除所有使用 MarkdownPreviewRenderer 的代码块
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复“启用 PDF 打印”开关无效的问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Automatic Renumbering
   </span>
  </span>
  <span>
   By Omri Levi
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      改进
     </span>
    </strong>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <span>
     更新依赖以解决安全漏洞（ajv、minimatch、flatted）
    </span>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Image Converter
   </span>
  </span>
  <span>
   By xRyul
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新选项：恢复 Obsidian 1.12 之前的图像点击行为
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新增“禁用 Obsidian 图像点击选择”选项，点击图像直接显示链接，隐藏编辑块图标、图像轮廓和角落调整
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       光标位置可设置：点击图像后光标置于链接前或后（复用现有设置）
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新选项：处理当前笔记时跳过文件夹
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持普通文件夹路径、glob 模式和正则匹配，包含文件夹建议/自动完成
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      其他
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       改进图像标注撤销行为：箭头绘制创建单次撤销步骤
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新安装默认设置：全局预设 Webp 75，标题默认禁用，拖拽时锁定宽高比默认开启
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    HiWords
   </span>
  </span>
  <span>
   By Kai
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新增单词释义 Tab 展示功能
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可在单词文件中使用 --- 分隔不同内容块，用标题作为段名称，HiWords 在侧边栏单词卡和悬停释义弹窗中渲染为可切换的 Tab
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       适合整理为“释义/例句/笔记”等多分区内容
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Line Arrange
   </span>
  </span>
  <span>
   By Chitwan Singh
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复有序列表在行和块操作中的行为
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       排序、随机打乱或反转后，有序列表现在能正确重新编号（之前保留原编号导致渲染错误）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       当选区为完整有序列表时自动修复编号
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      空行处理更一致
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       块操作完全忽略空行，不再将其视为列表项
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       关闭“保留空行”的行操作干净地丢弃空行，而非收集到输出顶部
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Featured Image
   </span>
  </span>
  <span>
   By Johan Sanneblad
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     新增
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新设置：编辑时自动运行（默认开启），笔记更改时自动更新特色图像
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新命令：更新当前文件中的特色图像，从命令面板刷新
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Pixel Perfect Image
   </span>
  </span>
  <span>
   By Johan Sanneblad
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复 Obsidian 1.12 及更高版本中图像上的重复上下文菜单
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复当多个文件夹包含相同文件名时，本地文件操作打开错误图像的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复插件窗口内的点击不再触发 Pixel Perfect Image 操作
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Excalidraw
   </span>
  </span>
  <span>
   By Zsolt Viczian
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复新 ExcalidrawAutomate 函数 ea.parseText() 在文本是嵌入图像或 PDF 文档时中断，导致 MindMap Builder 粘贴问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复自定义笔刷粗糙度未保存到模板绘图的问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Markitdown File Converter
   </span>
  </span>
  <span>
   By Ethan Troy
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      安全
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       消除 shell 注入漏洞：使用 spawn() 替代 exec()，参数数组且 shell: false
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       打包的 Python 包装脚本使用 argparse，无用户输入字符串插值
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       输出文件夹、图像目录和图像格式处理中的路径遍历防护
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       插件参数中的原型污染防护
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       错误消息在显示前剥离绝对路径
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新增
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       从 PDF 和 EPUB 提取图像：base64 数据 URI 解码到 {filename}-images/ 子文件夹
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       插件参数编辑器：设置中为第三方 Markitdown 插件提供键值对 UI
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       上下文菜单：文件资源管理器中支持的文件类型右键“转换为 Markdown”
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       设置向导：Python 检测和 Markitdown 安装的引导模态框
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       批量进度条：文件夹转换的视觉进度指示器
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Python 路径回退：macOS/Linux 上 python 不可用时自动检测 python3
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       实时设置刷新：更改 Python 路径后立即重新检查依赖
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      变更
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       将单体 main.ts（735 行）分解为 12 个模块
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       通过 PYTHONUTF8=1 环境变量支持 Unicode
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       模态框中使用异步文件 I/O
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       构建目标更新为 ES2020，TypeScript 5.x 严格模式
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       最低 Obsidian 版本保持 0.15.0
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      移除
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       移除 Docling 转换器（推迟到单独插件）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       代码库中不再使用 child_process.exec()
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Time Bullet
   </span>
  </span>
  <span>
   By pedrogdn
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复窗口移动后的键处理，添加回归测试
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加切换时间子弹命令及测试
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     库管理、导航与同步
    </span>
   </strong>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Sync Vault CE
   </span>
  </span>
  <span>
   By Camus Qiu
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复受控模式面板打开失败
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复自动同步结束后看板同步状态未刷新
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Weread Plugin
   </span>
  </span>
  <span>
   By hank zhao
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     Bug 修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复标题含特殊字符（如冒号）的书籍同步失败问题：对文件夹名称应用 sanitizeTitle() 函数，移除特殊字符
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Homepage
   </span>
  </span>
  <span>
   By mirnovov
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      为 Obsidian 新命令行界面增加两个命令：homepage 打开首页，homepage:read 打印首页内容到 stdout
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复历史记录偶尔不保存的问题
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      命令需要 Obsidian 1.12.0+，但此版本在 1.11.x 上仍可工作
     </span>
    </p>
   </li>
  </ul>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Custom Commands
    </span>
   </span>
   <span>
    By Staaaaaaaaaan
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复创建命令时路径中包含 {{time}} 导致文件名非法字符的问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Note Toolbar
   </span>
  </span>
  <span>
   By Chris Gurney
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新功能
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       手机上可选择隐藏 Obsidian 顶部导航栏
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       手机端自动隐藏样式：工具栏在顶部固定时可过渡隐藏
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      改进
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       增加“将项目移动到工具栏”选项
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       设置项按平台显示，上下文菜单重命名“标签栏”为“顶部导航”
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       手机端按钮样式默认使用浮动导航样式
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       修复
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       手机端顶部/底部工具栏位置修正、非 Markdown 文件顶部工具栏不再产生额外间距、浮动按钮动画一致
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复空标签页项目阴影被裁剪、手机端工具提示遮挡、iOS 卡片左边框不渲染、无可见项目时不显示文本工具栏等
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      AP
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       ntb.suggester() 增加 prefixes 选项，支持前缀触发建议（如 # 触发标签建议，[[ 触发文件建议）
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Quartz Syncer
   </span>
  </span>
  <span>
   By Emile Bangma
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      编译器管道从基于正则的转换迁移到基于 AST 的转换（使用 remark-obsidian）
     </span>
    </p>
   </li>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Obsidian 注释通过 AST 剥离，正确处理代码块内的注释
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       链接和图像的库路径剥离通过 AST 节点访问器处理
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       表格行内的 Wiki 链接管道符自动转义
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       提示语法正确保留
      </span>
     </p>
    </li>
   </ul>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      渲染转换委托给 Quartz v5 构建管道（Wiki 链接解析、嵌入展开、SVG 内联、高亮语法、标签渲染）
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复图像嵌入在与其他内容相邻时混叠的问题
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      移除嵌入和 SVG 嵌入逻辑（现由 Quartz v5 处理）、发布文件缓存系统、无用设置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      简化 Excalidraw 集成为仅推送文件，移除 SVG 转换、SCSS 样式和 ExcalidrawAutomate 依赖
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      拆分 Git 连接状态为读/写独立检查
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复 canvas 提取资源链接时仅收集资产文件而非所有文件节点的问题
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Datacore
   </span>
  </span>
  <span>
   By Michael Brenan
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     0.1.29
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       使 cleantext 适用于带 id 的列表项
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持指定查询函数返回的类型
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       将文档和注释中的 row 重命名为 $row
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       为列表块的第二遍处理添加空值检查
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       安全访问可能缺失的画布索引和缓存
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新 manifest.json
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Startpage
   </span>
  </span>
  <span>
   By kuzzh
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      增强笔记元数据、搜索排除和 UI 模态框
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Folder notes
   </span>
  </span>
  <span>
   By Lost Paul
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    增加选项：打开文件夹笔记时，在路径中隐藏文件夹笔记名称，仅显示文件夹名
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Notebook Navigator
   </span>
  </span>
  <span>
   By Johan Sanneblad
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      改进
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       右侧窗格日历始终显示 6 周
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       列表窗格属性药丸支持自定义 URI 方案（如 zotero://、file://）
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       布尔和数字属性现显示为列表窗格中的属性药丸
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       元数据清理现在移除过时的属性键选择
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    TODOseq
   </span>
  </span>
  <span>
   By Stephen Cross
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复任务行无内容时导致受影响页面任务列表无结果的问题
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复点击状态栏任务计数触发的搜索筛选器未进行精确文件匹配的问题
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Task List Kanban
   </span>
  </span>
  <span>
   By Chris Kerr
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     Bug 修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       使用 Obsidian 字体大小设置作为看板内容，使看板尊重用户配置的文本大小
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持原生 Obsidian 链接修饰键行为（ctrl/cmd+ 点击）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       抑制构建输出中已知的 svelte-select 编译器警告
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Quick Switcher++
   </span>
  </span>
  <span>
   By darlal
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    修复标准模式下启用“恢复之前输入”时显示 null 的问题
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Current View
   </span>
  </span>
  <span>
   By Lucas Ostmann
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     1.5.0 (2026-03-21)
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <span>
     增加按标签自动切换视图模式的规则
    </span>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Bookmarks Caller
   </span>
  </span>
  <span>
   By namikaze-40p
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     改进
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       原生高亮：建议列表中匹配文本加粗显示
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       安全更新：更新内部依赖以解决报告的安全漏洞
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Tab Selector
   </span>
  </span>
  <span>
   By namikaze-40p
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     改进
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       智能搜索排序：精确字符串匹配优先于分散的模糊匹配
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       原生高亮：建议列表中匹配文本加粗显示
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       安全更新：更新内部依赖以解决报告的安全漏洞
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <section style="direction: ltr;">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Note Status
    </span>
   </span>
   <span>
    By Aleix Soler
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     变更
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       实现插件设置的多设备同步
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复新 Obsidian 版本中的 UI 问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持新笔记的默认状态
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       模板市场、预定义模板、模板特征化
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       改进状态选择器模态框
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       集成 Notebook Navigator + 修复文件重命名
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       改进状态组 UI
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Self-hosted LiveSync
   </span>
  </span>
  <span>
   By vorotamoroz
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     0.25.54 (2026-03-18)
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       远程存储大小检查现在再次正常工作
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       设置对话框中的一些按钮现在再次正确响应
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      重构
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       P2P 复制器重构，更健壮且更易理解
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       删除不再使用的可能导致潜在问题的项目
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      CLI
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复帮助消息显示乱码的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       移除一些不必要的代码
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       WebApp
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复日志窗格中未应用详细级别的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       弹出窗口现在显示
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加测试覆盖
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Web 应用中同样显示弹出窗口
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    File Ignore
   </span>
  </span>
  <span>
   By Feng
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     Bug 修复和安全更新
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       防止显示/恢复重命名原本以点开头的文件（除非被插件隐藏）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       对单文件恢复和批量计划应用相同的保护
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新 minimatch 至 5.1.8，esbuild 至 0.27.4
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       验证：npm audit 结果为 0 漏洞
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Day Planner (OG)
   </span>
  </span>
  <span>
   By James Lynch (continued by Erin Schnabel)
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     0.7.3 (2026-03-17)
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       改进模式变更处理
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       启用插件时记录当前计划
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span style="font-size: 15px; color: rgb(47, 200, 255);">
    <span>
     实用工具与 UI 优化
    </span>
   </span>
  </strong>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    RSS Dashboard
   </span>
  </span>
  <span>
   By Aditya Amatya
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     2.2.0-beta.8 (2026-03-24)
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      新功能
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       侧边栏自定义排序（拖拽）、自定义工具栏图标（显示/隐藏、排序）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       侧边栏标签过滤：AND/OR/NOT 逻辑，内联添加标签与颜色选择器
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       播客播放器睡眠定时器（5-120 分钟）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       播客“在浏览器中打开”改进：解析网站 URL，降级到 RSS 链接，下拉菜单包含音频文件链接
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Pocket Casts 导入支持，多代理降级解析播客源，iTunes Search API 备用发现
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加/编辑 Feed 时检查 CORS 代理状态并给出警告
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       OPML 导入菜单重构，视图筛选器状态持久化，启动时可应用多个筛选器
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       阅读器标签菜单与仪表板卡片统一，保存按钮点击后直接打开已保存 Markdown 文件
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       改进 X/Twitter (Nitter) 源在阅读器中的渲染
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复因全局 CSS 未限定作用域导致的 Obsidian 属性类型错误
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       设置迁移（filters → rules），向后兼容
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复因 GUID 变化导致的重复文章问题（如 BBC），自动去重
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复切换视图时分页控件不更新，新增“全部”选项，分页设置同步
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       开发
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加 CSS 作用域检查，设置面板重构为模块化（9 个专用渲染模块），Feed 管理器重构，ReaderView 重构
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Tag Group Manager
   </span>
  </span>
  <span>
   By Stargazer-cc
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     Bug 修复：
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复新版插件无法读取旧版标签颜色数据，导致“应用标签于正文”功能失效的问题。现可在设置中手动快捷导入旧版颜色数据。
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <span>
     其他改进：
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       精简控制台输出内容
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       优化开启正文标签样式后，预览和编辑视图下的渲染稳定性
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Edit in Neovim
   </span>
  </span>
  <span>
   By Theseus
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     依赖更新
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       升级 esbuild、minimatch、flatted 等依赖版本
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Github Issues
   </span>
  </span>
  <span>
   By LonoxX
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复与更新
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复文件与文件夹操作时仓库缓存同步问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复 YAML 列表变量中单引号转义问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       升级 TypeScript 至 6.0.2
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Disciples Journal
   </span>
  </span>
  <span>
   By Scott Tomaszewski (Xentis)
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    为 passage 笔记增加 cssclasses: hide-dj-passage-properties 以隐藏干扰属性
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Ink Player
   </span>
  </span>
  <span>
   By Uglyboy
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       解决 ink 故事激活间歇性失败的问题
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <span>
     新功能
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加波兰语本地化，重新设计选项样式，修复本地化问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Shell Path Copy
   </span>
  </span>
  <span>
   By Charles Kelsoe (ckelsoe)
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Windows 上绝对路径复制现在可用（替换了不可用的内部 API）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       Windows file:// URL 不再对驱动器冒号进行编码
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      移除
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       放弃使用文件资源管理器 DOM 查询进行命令面板文件检测（依赖内部 CSS 类名，可能随 Obsidian 更新而中断），命令面板命令现在要求打开一个文件，否则显示明确提示
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      技术
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       将路径格式化逻辑提取为纯函数（无 Obsidian 依赖），添加 37 个单元测试，CI 运行测试和检查废弃 API 使用，发布前运行测试
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Pixel Pets
   </span>
  </span>
  <span>
   By Lucas Jin
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     修复
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复名字反向问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复抛球卡在顶部的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复抚摸宠物时的闪烁/切换效果问题
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <span>
     新功能
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可通过将鼠标变为猫玩具与猫玩耍
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可将宠物游乐场从模态框改为整个 Obsidian 库（使用透明覆盖层，完全保留正常功能）
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Data Fetcher
   </span>
  </span>
  <span>
   By qf3l3k
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     1.1.4 (2026-03-21)
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       新增
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       缓存浏览器条目显示别名感知标签
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       缓存浏览器筛选匹配别名、哈希、类型和 URL
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      <span>
       变更
      </span>
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       端点编辑器对话框为长端点提供更多水平空间
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       缓存浏览器列表和预览窗格使用更多对话框空间
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       新缓存条目存储轻量查询元数据，使标签更易理解
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Tick Tones
   </span>
  </span>
  <span>
   By DontBlameMe
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     依赖更新
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       升级多个开发依赖（@types/node、typescript-eslint、@eslint/js、eslint、minimatch、obsidian、esbuild、jest 等）
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Messager
   </span>
  </span>
  <span>
   By Rainyluo
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    公众号内容获取改为生成新文件
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    EasyLink
   </span>
  </span>
  <span>
   By isitwho
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      Bug 修复
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复因未去除标点导致搜索结果缺失的问题（如 “word.” 未匹配 “word”）
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复“仅标题”开关与关闭按钮重叠的问题
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       修复“仅标题”模式下 Cmd+Enter 打开错误笔记的问题
      </span>
     </p>
    </li>
   </ul>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      改进
     </span>
    </strong>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       重复结果去重从 O(n²) 优化为 O(n)
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    GitHub Stars
   </span>
  </span>
  <span>
   By Flying Nobita
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     主要变更
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       即使缓存条目仍然有效，也可从 GitHub 刷新当前笔记
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       更新嵌入的星标文本而不嵌入普通链接
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       在阅读视图和实时预览刷新路径中，当设置启用时更新现有嵌入星标
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加刷新令牌警告控制和刷新失败时的更安全回退行为
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       添加覆盖缓存绕过和嵌入星标刷新回归的单元测试
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    GridExplorer
   </span>
  </span>
  <span>
   By Devon22
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    修复：搜索标签时中文输入法意外被截断的问题
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <b>
     <span>
      PKM出品
     </span>
    </b>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Easy Typing
   </span>
  </span>
  <span>
   By yaozhuwa
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     6.0.6 (2026-03-20)
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        规则编辑与列表优化
       </span>
      </strong>
      <span>
       ：修复正则规则编辑时反斜杠重复转义、内置规则描述显示异常、类型与触发模式按钮颜色问题，优化规则列表预览
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        设置面板与响应式适配
       </span>
      </strong>
      <span>
       ：优化间距与文案，删除失效链接，改进窄宽度自适应布局和移动端排版
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        Bug 修复
       </span>
      </strong>
      <span>
       ：修复删除空白行时误删引用与列表间空行的问题，修复 IME 取消输入时误触发转换规则的问题
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="margin-top: 10px; margin-bottom: 10px; text-align: center;">
  <section style="padding: 1px 0px;">
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
   <section>
    <section style="width: 100%; border: 1px solid rgb(160, 160, 160); padding: 10px;">
     <section style="text-align: justify; color: rgb(47, 200, 255);">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <span>
        声明
       </span>
      </p>
     </section>
     <section style="text-align: justify;">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <span>
        本栏目致力于为广大 Obsidian 中文用户汇总全面的官方资讯与插件、外观动态。为了保持信息的全面性，我们的
       </span>
       <strong>
        <span>
         <span>
          收录并不等同于推荐
         </span>
        </span>
       </strong>
       <span>
        ，还请各位用户知悉并理解，根据自身需求进行判断和选择。
       </span>
       <span>
        <br />
       </span>
       <span>
        若阁下有独到的见解或新颖的想法，诚邀您在文章下方留言，与大家共同探讨。
       </span>
      </p>
     </section>
    </section>
   </section>
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
 </section>
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
         <img src="https://mmbiz.qpic.cn/mmbiz_jpg/dibCdrCystEX1ZjgcVr6zic86ibV7Jg3n46G3yMounFW46Sn2N5t0gibK1Moeu3SYcwvKiaf0C1P9m6JumoQGFXFricl3UeM05siam2HSEIDN8Jy5k/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEU7dFfK4GgzTmiaUyAWy6W70UYqWEjpna1QtrlJnxOslMwHNTfvdZOUFUAYTJ8kG32hsXGqBibmGgAib9AvmYSB7p1afibVse9rP1Y/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/dibCdrCystEVzYapjZVboVew0bpb37yN4jJEawhaXj7L2x9YOnrWHU0CgSpDzV7cYsYoebzDoHu1jroYfwELSYY9Agg5D4ic3Y27AAUZSYUhQ/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; width: 261.796875px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEUhsAG7PYpNagGTUJmzpqVI6vaoKzc2HhYHelB58nZV21JnKBC2QRrRp8u5qQ74GfPdmG0Jjaf3S8bsx7PUVUAYUm2A03TGic24/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="vertical-align: middle; width: 66.984375px !important; height: auto !important;" />
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
           ：PKMer.cn
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEUakkSxcoK8RTlabgZ7xXBoWcUv9W8A81GsF8JkFiaJ7m1icuJmmEf77pp7uLXDAqeAQ7VIEpA4K5vryXCsPicrq0KFCBLKic4zAjE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="vertical-align: middle; width: 256.90625px !important; height: auto !important;" />
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
