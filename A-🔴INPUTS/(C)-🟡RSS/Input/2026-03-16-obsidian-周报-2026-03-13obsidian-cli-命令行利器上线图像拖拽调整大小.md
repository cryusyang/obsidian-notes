---
title: "Obsidian 周报 2026-03-13：Obsidian CLI 命令行利器上线，图像拖拽调整大小，附件自动清理新体验"
url: "https://mp.weixin.qq.com/s/0Hnuc89V1bNVTpgs9yPqVw"
source: "PKMer知识社区"
date: 2026-03-16
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文为Obsidian Weekly 2026-03-13期摘要，重点介绍v1.12.4与v1.12.5版本更新：新增iOS分享扩展、快捷指令及无头模式同步支持，优化CLI命令自动补全与多光标链接包裹等编辑体验，并修复多项复制粘贴、表格操作及UI交互问题。社区插件方面，新增Capitaliser、Double-Click Image Opener、Role Switch和Bluesky等实用工具。AI相关插件（如YOLO、QuickAdd）在权限管理、上下文引用、Token优化及模板复用等方面均有显著增强。

---

<section style="color: rgb(57, 57, 57); letter-spacing: 1px; line-height: 1.75; padding-right: 15px; padding-left: 15px; font-size: 14px; font-style: normal; font-weight: 400; text-align: justify; margin-bottom: 0px;">
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 100%;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEVIor2hyVWltoBckudkYBC9s2Y2blCb5L4gspw2rf62wGIb1AqzWrcXiay9jgFjibcicticm2WibV04k5cibDAA0P7Q7czghvPgE5Dbg/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
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
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEXUla1Pibokyd9yJreLHRwkrW4N02UqAQF47SFmLrbQ5zpLKhZlNR4p3p7p3OmqicVkt89TjJsZHNDdjJbia5p6pcKPCqjBxhXBHU/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
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
       <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEUkGGkicR2YZtsneZibuGiaQnae0FbRQIjPH7rrqtWNeJZicbzw9RGI28uoTx7kS6zEupLKQFud7Vpkhmxm2Maiaia7MicLpjd4wVqHZE/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="text-align: center; font-size: 19px;">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Obsidian Weekly 2026-03-13：Obsidian CLI 命令行利器上线
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    图像拖拽调整大小
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    附件自动清理新体验
   </span>
  </p>
 </section>
 <section style="text-align: left; font-size: 12px; color: rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <em>
    <span>
     统计时间：2026-02-23 21:00 ~ 2026-03-13 21:00
    </span>
   </em>
  </p>
 </section>
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
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      版本 v1.12.5
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     改进
    </span>
   </strong>
  </p>
 </section>
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
     为在终端界面 (TUI) 中使用
    </span>
    <span>
     <span>
      id=
     </span>
    </span>
    <span>
     参数时的 Obsidian 命令添加了自动补全功能。
    </span>
   </p>
  </li>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     错误修复
    </span>
   </strong>
  </p>
 </section>
 <section>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      修复了在未选中文本时进行复制、剪切和粘贴的若干问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      复制和粘贴一行时，光标不再放置在错误的位置。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在表格中，未选中内容时进行复制或剪切，现在只会正确地复制单元格内容。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      当多光标选中文本时粘贴 URL，现在会将每个选中部分包裹为 Markdown 链接（
     </span>
     <span>
      <span>
       [选中的文本](url)
      </span>
     </span>
     <span>
      ）。
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    Obsidian Sync 现在支持使用
   </span>
   <span>
    <span>
     obsidian-headless
    </span>
   </span>
   <span>
    客户端进行无头模式运行。了解更多关请结合
   </span>
   <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
    <span>
     Obsidian Headless 与 Sync
    </span>
   </span>
   <span>
    的信息。
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
      版本 v1.12.4
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      新增功能
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       iOS
      </span>
     </strong>
     <span>
      : 新增分享扩展功能，无需打开 Obsidian 即可从其他应用（如 Safari、社交网络）将内容保存到你的知识库。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       iOS
      </span>
     </strong>
     <span>
      : 新的快捷指令操作“添加书签链接”，用于将 URL 保存为 Obsidian 书签。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      改进
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      应用现在默认使用系统语言，并在新用户引导过程中增加了语言选择器。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      新增了“独立笔记”App 快捷操作（长按应用图标时显示的菜单）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      改进了对平板电脑上指针设备（如 Magic Trackpad）的支持：
     </span>
    </p>
   </li>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       子菜单现在在悬停时展开。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       在属性编辑器中，右键点击会显示上下文菜单。
      </span>
     </p>
    </li>
   </ul>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      已修复问题
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      从文件删除提示中移除了“删除且不再询问”选项。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       Obsidian 同步
      </span>
     </strong>
     <span>
      : 修复了如果在 Obsidian 保存最新的同步状态前关闭应用，文件可能会被覆盖的问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       iOS
      </span>
     </strong>
     <span>
      : 修复了与边栏项目交互后，工具提示有时会出现的问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       iOS
      </span>
     </strong>
     <span>
      : 修复了导致“每日笔记”和“书签”快捷指令无法工作的问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       iOS
      </span>
     </strong>
     <span>
      : 修复了“查看笔记”小组件无法立即刷新的问题。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       幻灯片
      </span>
     </strong>
     <span>
      : 修复了在移动端状态栏上关闭按钮的位置问题。
     </span>
    </p>
   </li>
  </ul>
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
    插件新闻
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      社区插件
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <b>
    <span>
     新增
    </span>
   </b>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
   <span>
    Capitaliser
   </span>
  </span>
  <span>
   By Emanuel Oliveira
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWibtr0TNuWMDbXWl4dicYHkR3wglOXuzTJRg87ib2VSCicrGSM5ica5OZUFibSBaEkglGWuRNYNeZ2afBd5Vv8hRFKZiaRZe6CW9XIBI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    通过快捷键循环切换所选文本的大小写格式，在全小写、单词首字母大写和全大写之间快速切换。
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
     Double-Click Image Opener
    </span>
   </span>
   <span>
    By atman
   </span>
  </p>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEXJ4RwBxOHIv4iaIbHnbUqMxYNTCiaxhTH6RUWJf1VlyyXXjRpBnfDXDvRtW1ZOemsTeuP3LMm84Q92W8hZYYybpIIOj277Dbw4E/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    在预览模式下双击图片，即可调用系统默认图片查看器打开原图，适合放大查看或交给专业图像工具继续编辑。
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
     Role Switch
    </span>
   </span>
   <span>
    By Zafrem
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    为不同“工作角色”（如开发者、写作者、研究者等）创建独立的工作状态视图，在切换角色时进行有意识的过渡，并记录会话与专注时间，帮助管理多角色、多项目的上下文切换成本。
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
    Bluesky
   </span>
  </span>
  <span>
   By eharris128
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    在侧边栏提供 Bluesky 面板与“扩音器”图标，可直接在 Obsidian 内撰写并发布 Bluesky 帖子或长线程，支持使用 Bluesky App Password 登录，在笔记与社交分享之间无缝切换。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      AI 与自动化
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
    By Lapis0x0 Agent
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       与工具链稳定性
      </span>
     </strong>
     <span>
      ：为 Chat 模式新增“打开技能”与“读取文件”权限，扩展能力边界；减少工具调用时的页面闪动；优化 Agent 模式下工具调用的前端识别与渲染速度；深度优化 Agent 文件工具的调用链路，降低参数解析失败概率。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       智能上下文与 @ 引用
      </span>
     </strong>
     <span>
      ：在 @ 一级菜单中新增“当前文件”选项；优化对 @文件/@文件夹 的引用逻辑，默认仅传递路径信息，需要时通过只读工具按需读取内容，大幅降低上下文 Token 消耗。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       编辑与渲染精度
      </span>
     </strong>
     <span>
      ：统一工具调用显示文本；修复从 Obsidian 块复制的文本与渲染预览不匹配的问题；优化高亮选择样式，修复与系统选择重叠时的“重影”问题；增强 Obsidian 格式编辑稳定性，精确替换失败时采用模糊匹配（阈值 0.95）查找高相似块，自动拒绝歧义候选。
     </span>
    </p>
   </li>
  </ul>
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
     QuickAdd
    </span>
   </span>
   <span>
    By Christian B. B. Houmann
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      .base 模板成为可重用的 QuickAdd 构建块
     </span>
    </strong>
    <span>
     ：
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       可将实时 Base 驱动的部分插入现有 Markdown 笔记（如 MOC、仪表盘、项目中心）。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       在 Capture 格式中使用
      </span>
      <span>
       <span>
        {{TEMPLATE:...}}
       </span>
      </span>
      <span>
       重用
      </span>
      <span>
       <span>
        .base
       </span>
      </span>
      <span>
       模板，将 Base 内容插入活动笔记。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       直接从 Template 选择创建真正的
      </span>
      <span>
       <span>
        .base
       </span>
      </span>
      <span>
       文件。
      </span>
      <strong>
       <span>
        直接捕获到 Canvas 卡片
       </span>
      </strong>
      <span>
       ：
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       支持两种 Canvas 捕获工作流：捕获到指定
      </span>
      <span>
       <span>
        .canvas
       </span>
      </span>
      <span>
       文件中的特定节点；捕获到活动 Canvas 中选中的一张卡片。
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
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    SystemSculpt AI
   </span>
  </span>
  <span>
   By SystemSculpt.com
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       错误提示改进
      </span>
     </strong>
     <span>
      ：纯文本 413（上传过大）错误现在直接展示，而不是被错误地包装为“JSON 解析失败”。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       上传分片策略改进
      </span>
     </strong>
     <span>
      ：音频上传的分片决策改为基于估算的 multipart 请求大小，更好避免接近大小上限的录音被拒绝。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       移动端转写对齐
      </span>
     </strong>
     <span>
      ：移动端转写改用 hosted jobs pipeline，与桌面端更接近一致。
     </span>
    </p>
   </li>
  </ul>
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
     Large Language Models
    </span>
   </span>
   <span>
    By eharris128, r-mahoney, &amp; jsmorabito
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新模型支持
      </span>
     </strong>
     <span>
      ：新增 Mistral AI 远程提供方；新增 Ollama 本地 LLM 支持；新增 OpenAI 模型 GPT-4o-mini、GPT-4.1、o3、o4-mini、gpt-image-1；新增 Claude 4.5/4.6 模型 Sonnet 4.6、Opus 4.6、Haiku 4.5。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       图像生成
      </span>
     </strong>
     <span>
      ：简化图像质量验证；修复 gpt-image-1 的 b64_json 处理，图片现在能正确渲染；用 gpt-image-1 替代 DALL-E 2/3。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       其他
      </span>
     </strong>
     <span>
      ：添加功能区图标切换设置；用户可选的空白新聊天头像 SVG。
     </span>
    </p>
   </li>
  </ul>
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
     Copilot
    </span>
   </span>
   <span>
    By Logan Yang
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    聊天历史记录现在渐进加载，支持无限滚动。 Miyo 改进：支持自定义服务器 URL（远程部署），启用前增加确认对话框，更顺畅的启用流程。 修复了 Copilot Plus 用户的“连接错误”（TLS 证书问题）。 修复了 Gemini 的流式崩溃和代理循环中途停止的问题。 移动端和 UI 修复：移动端浮层正确关闭；聊天中表格正确渲染；过时的选中文本不再渗入后续消息。
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
     AI Tagger Universe
    </span>
   </span>
   <span>
    By Hu Nie
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    改进 LM Studio 错误信息，HTTP 502/503 错误显示可操作的故障排查提示；新增“保留现有标签”选项，启用后 AI 标签与现有标签合并而非替换；可配置请求超时时间，默认从 30 秒增加到 60 秒，现在可在 15–300 秒间调节。
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
     Canvas LLM
    </span>
   </span>
   <span>
    By Mike Farlenkov
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    为
   </span>
   <span>
    <span>
     Text input
    </span>
   </span>
   <span>
    节点新增“阅读模式”。
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
     AI Agent
    </span>
   </span>
   <span>
    By Manuel Magaña López
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增 3.1 Gemini 模型；
   </span>
   <span>
    <span>
     open-agent-sidebar
    </span>
   </span>
   <span>
    热键改为
   </span>
   <span>
    <span>
     toggle-agent-sidebar
    </span>
   </span>
   <span>
    ，允许用户关闭已打开的侧边栏；作者将恢复项目开发，计划新增除 Google 外的模型提供商。
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
     Github Copilot
    </span>
   </span>
   <span>
    By Vasseur Pierre-Adrien
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    允许用户选择是否在启动时自动打开聊天。
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
     Steward
    </span>
   </span>
   <span>
    By Dang Nguyen
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      工具
     </span>
    </strong>
    <span>
     ：新增在命令流中直接切换 Agent 容量的工具。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      Guardrails
     </span>
    </strong>
    <span>
     ：增加 Guardrails 支持，通过基于规则的防护限制文件和文件夹访问。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      对话压缩
     </span>
    </strong>
    <span>
     ：添加对话压缩功能，保持长聊天性能的同时保留完整消息召回。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      UI
     </span>
    </strong>
    <span>
     ：更新思考块渲染，对长响应应用最大高度以提高可读性。
    </span>
   </p>
  </section>
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
     Auto Note Importer
    </span>
   </span>
   <span>
    By uppinote RateLimiter
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    现在自动检测 429（请求过多）响应，并根据服务器指定的延迟重试，默认最大重试次数 3，后备延迟 30 秒。
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
     Nexus AI Chat Importer
    </span>
   </span>
   <span>
    By Superkikim
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     自动识别所选 ZIP 的提供方（provider），多提供方混选时忽略不匹配的压缩包。
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        拆分导入报告
       </span>
      </strong>
      <span>
       为 3 份交叉链接的报告：移动端轻量浏览索引、完整逐会话列表、全局统计与压缩包级状态汇总。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        统一 ZIP 处理模型
       </span>
      </strong>
      <span>
       ：桌面与移动端统一策略，先检查 central directory，再仅读取必要条目。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        移动端导入稳定性
       </span>
      </strong>
      <span>
       ：支持补齐/更新缺失或变更的笔记；支持“重新处理并重建全部笔记”；一次只处理一个 ZIP 以控制内存占用。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        首次安装引导
       </span>
      </strong>
      <span>
       ：欢迎对话框点击 Get Started 直接打开插件设置，便于首次导入前配置目录。
      </span>
     </p>
    </li>
   </ul>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      任务与项目管理
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Task List Kanban
    </span>
   </span>
   <span>
    By Chris Kerr, Erika Rice Scherpelz
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    限制“添加新文件”的范围仅为看板文件夹；（可能）修复了安卓平板设置齿轮不显示的问题；（可能）修复了水平流动模式下垂直滚动不工作的问题；修复了标签过滤器选择状态未正确重新计算的问题。
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
    Tag Timer
   </span>
  </span>
  <span>
   By quantavil
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       完全重新设计
      </span>
     </strong>
     <span>
      ：从头使用现代 TypeScript 和 CodeMirror 6 重建。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       高效渲染
      </span>
     </strong>
     <span>
      ：使用 CodeMirror 6 ViewPlugin 和 WidgetType，在实时预览和阅读视图中实现非破坏性、高性能的 UI 叠加。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       零依赖
      </span>
     </strong>
     <span>
      ：无外部库，占用极小，稳定性高。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       计时功能
      </span>
     </strong>
     <span>
      ：热键 Alt+D 删除定时器，Alt+C 切换倒计时，Alt+S 切换秒表。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       可靠性
      </span>
     </strong>
     <span>
      ：每行自动确保只有一个计时器；跨所有库文件的运行中计时器稳健跟踪；退出时自动暂停，重启时无缝恢复。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       手动时间输入
      </span>
     </strong>
     <span>
      ：流畅的模态框，可精确设置或调整计时器值（支持 mm:ss、hh:mm:ss 或分钟）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       设计
      </span>
     </strong>
     <span>
      ：全新项目品牌横幅；活动计时器视觉提示（⌛/⏳）；完美适配 Obsidian 亮/暗主题；交互式徽章，点击切换，右键菜单丰富。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       数据持久化
      </span>
     </strong>
     <span>
      ：计时器以轻量级 Markdown 标签形式内联存储，完全可搜索，面向未来。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    TickTick Quick Add Task
   </span>
  </span>
  <span>
   By Muxin Li
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增标签位置设置：可选择将
   </span>
   <span>
    <span>
     #ticktick
    </span>
   </span>
   <span>
   </span>
   <span>
    追加在末尾或前置到开头；新增选择模式设置：可在“捕获当前行”与“捕获整个段落”之间切换。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      写作与创作
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Storyteller Suite
    </span>
   </span>
   <span>
    By Maws
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       战役与 DnD 模式
      </span>
     </strong>
     <span>
      ：新增完整战役会话管理（队伍状态、物品栏、生命值、状态、标记、已揭示设定、阵营声望）；新增战役命令（打开会话、继续最近会话、从当前场景开始、记录游玩日志）；强化场景分支逻辑，分支可对物品、标记、设定解锁、阵营声望变化作出反应；新增更高级的物品效果，例如生命值变化、状态变化、场景移动、设定揭示、阵营声望变化等。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       角色卡预设
      </span>
     </strong>
     <span>
      ：新增 DnD 主题角色卡预设；新增基于 Markdown 与 Callout 的“Obsidian 风格”预设；改进角色卡预览与保存流程。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       时间线与甘特图体验重做
      </span>
     </strong>
     <span>
      ：重做时间线/甘特图，更干净、更稳定；改进分组泳道、进度渲染、里程碑过滤、依赖箭头与依赖关系持久化。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       地图与战役看板
      </span>
     </strong>
     <span>
      ：将图片地图作为“可交互看板”接入战役流程；改进密集地图下的图钉、弹窗与标记交互；新增 SVG 支持两种模式（大 SVG 栅格化分块、轻量 SVG 直接叠加）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       编译与写作流程
      </span>
     </strong>
     <span>
      ：扩展编译工作流，支持自定义编译步骤；改进手稿输出的草稿与工作流处理；优化新建文件与草稿提示相关的场景/草稿行为。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       实体系统与笔记同步
      </span>
     </strong>
     <span>
      ：分组笔记以“真正的、由笔记支撑的实体”方式工作；改进笔记与插件状态之间的同步；改进 WikiLink 属性，使链接实体在属性面板/图谱中显示更正确；统一实体弹窗中大量自定义字段的行为。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       图库
      </span>
     </strong>
     <span>
      ：新增多图上传；改进图库文件夹同步与托管文件夹发现；优化图库渲染与选择器行为。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       移动端、引导与文档
      </span>
     </strong>
     <span>
      ：新增真正的首次启动上手指南；新增应用内“更新亮点”弹窗；更新文档与教程以匹配当前功能集；改进移动端仪表盘行为并清理拥挤的界面细节。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Note to MP
   </span>
  </span>
  <span>
   By Sun Booshi
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <span>
     支持使用 LESS 定义文章样式，可完全自定义文章样式（新增“自定义”主题）；优化超宽表格显示（横向滚动）。
    </span>
   </p>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        工作流支持
       </span>
      </strong>
      <span>
       ：可与 n8n、Coze 等工作流平台联动，支持发布前/后自动执行额外动作，支持 AI 自动生成内容。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        会员功能
       </span>
      </strong>
      <span>
       ：更安全获取公众号 AccessToken 的专用接口；在笔记中插入
      </span>
      <span>
       <span>
        workflow
       </span>
      </span>
      <span>
       代码块，发布前/后自动调用外部工作流；工作流参数支持动态引用当前笔记属性、笔记内容、仓库文件。
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <strong>
       <span>
        会员功能
       </span>
      </strong>
      <span>
       ：支持将 Obsidian 笔记发布为 𝕏（推特）长文章（需配合浏览器插件「文兔兔助手」）。
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
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Custom Slides
   </span>
  </span>
  <span>
   By David V. Kimball
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       自动缩放
      </span>
     </strong>
     <span>
      ：添加可选的自动缩放开关，自动缩小溢出的垂直幻灯片内容以适配视口。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       幻灯片编号
      </span>
     </strong>
     <span>
      ：可选显示幻灯片编号，位置可选左下或右下。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       页脚文本
      </span>
     </strong>
     <span>
      ：在所有非标题幻灯片上显示可配置的页脚文本。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      卡片笔记
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Decks
    </span>
   </span>
   <span>
    By Xherdi Lika
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <section style="width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      设置
     </span>
    </strong>
    <span>
     ：更改牌组标签时会自动迁移个人资料 - 标签映射以使用新标签。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      解析
     </span>
    </strong>
    <span>
     ：牌组标签现在可在插件设置中配置（解析部分）。新安装默认为
    </span>
    <span>
     <span>
      #decks
     </span>
    </span>
    <span>
     ，现有用户保留
    </span>
    <span>
     <span>
      #flashcards
     </span>
    </span>
    <span>
     直到手动更改。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      UI
     </span>
    </strong>
    <span>
     ：筛选占位符和空状态帮助文本现在反映配置的牌组标签。
    </span>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Spaced Repetition
   </span>
  </span>
  <span>
   By Stephen Mwangi
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    实现可自定义的一天开始时间；实现当复习序列只有一个牌组时，直接打开闪卡视图；添加一个按钮，可跳转到笔记中的当前复习项。
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
    Text Autocomplete
   </span>
  </span>
  <span>
   By Christ Degni
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    支持从文本文件导入词典（必须是
   </span>
   <span>
    <span>
     .txt
    </span>
   </span>
   <span>
    文件，每行一个单词）；调整了默认词典的过滤。
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
    Note Definitions
   </span>
  </span>
  <span>
   By Dominic Let
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    添加“区分大小写”选项。
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
    Yanki
   </span>
  </span>
  <span>
   By Eric Mika
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    在文件浏览器上下文菜单中添加项目，可将文件夹添加/移除 Anki 闪卡文件夹列表。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      界面与外观
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Pixel Banner
    </span>
   </span>
   <span>
    By Justin Parker
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    修复了当笔记包含 frontmatter 并使用文件夹组横幅时，每次按键都闪烁的问题；修复了更改设置后内容起始位置未正确应用的问题；修复了普通路径对视频文件 (
   </span>
   <span>
    <span>
     .mp4
    </span>
   </span>
   <span>
    ,
   </span>
   <span>
    <span>
     .mov
    </span>
   </span>
   <span>
    ) 无效的问题；修复了 .webp 图片不显示的问题；新增对 AI 图像生成模型
   </span>
   <span>
    <span>
     Seedream 4
    </span>
   </span>
   <span>
    、
   </span>
   <span>
    <span>
     Nano Banana
    </span>
   </span>
   <span>
    的多图像引用支持；修复了“Pixel Banner Plus Server” URL 错误的问题。
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
    Codeblock Customizer
   </span>
  </span>
  <span>
   By mugiwara
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    可在编辑器模式下使用 PrismJS 进行语法高亮，使更多语言获得高亮，并让编辑/阅读模式的高亮更一致。
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
    Custom Note Width
   </span>
  </span>
  <span>
   By 0skater0
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       单位扩展
      </span>
     </strong>
     <span>
      ：支持 %、px 和 ch，每个单位有用户可配置的最小/最大范围。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       代码块宽度
      </span>
     </strong>
     <span>
      ：独立于编辑器宽度的代码块宽度控制，每个模式（阅读、源码、实时预览）可单独切换。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       国际化
      </span>
     </strong>
     <span>
      ：支持英语、德语和 en-GB，自动检测语言。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       UI 改进
      </span>
     </strong>
     <span>
      ：设置界面重新设计，分为语言、宽度、代码块和每笔记部分。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       性能优化
      </span>
     </strong>
     <span>
      ：滑块交互使用 250ms 防抖写入 YAML；直接从元数据缓存同步读取宽度；双 CSS 策略防止标签切换时闪烁。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       YAML 向后兼容
      </span>
     </strong>
     <span>
      ：旧版纯数字值被解释为百分比。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Mouse Navigation
   </span>
  </span>
  <span>
   By HoBeomJeon
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增手势引擎设置，有两个选项：
   </span>
   <span>
    <span>
     legacy-v1
    </span>
   </span>
   <span>
    和
   </span>
   <span>
    <span>
     modern-v2
    </span>
   </span>
   <span>
    。如果升级后行为异常，可切换回 legacy-v1。
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
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      文件与链接
     </span>
    </span>
   </strong>
  </p>
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
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新 API 2.0
      </span>
     </strong>
     <span>
      ：添加 whenReady()、标签集合助手、属性节点助手、新的标签和属性上下文菜单钩子等。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新命令
      </span>
     </strong>
     <span>
      ：切换双窗格方向（水平/垂直）。 新设置：列表 &gt; 笔记 &gt; 将属性药丸链接到 URL（点击打开 URL）；将属性药丸链接到笔记（点击打开文件）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新设置
      </span>
     </strong>
     <span>
      ：列表 &gt; 笔记 &gt; 特色图像像素大小（缩略图最大宽度可调至 512 像素）；特色图像显示大小（列表窗格中最大垂直尺寸可调至 128 像素）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新设置
      </span>
     </strong>
     <span>
      ：列表 &gt; 笔记 &gt; 未完成任务背景色，便于在列表窗格中快速找到未完成任务。 可在菜单或 frontmatter 中为文件设置背景色。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       彩虹色
      </span>
     </strong>
     <span>
      ：可为快捷方式、最近文件、文件夹、标签或属性设置单独的彩虹色，可选色轮或 RGB 混合。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       改进
      </span>
     </strong>
     <span>
      ：快捷键行在快捷键徽章为“无”时不再预留尾部徽章空间；可在“属性键可见性模态框”中直接点击属性键快速在三个位置（导航窗格、列表窗格、文件菜单）切换可见性。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       更改
      </span>
     </strong>
     <span>
      ：更新 fontawesome 图标 7.1→7.2，simple-icons 15.20→16.11（注意：simple-icons 移除了 44 个图标，如 canva、openai、slack，需重新分配）。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       修复
      </span>
     </strong>
     <span>
      ：修复了当导航窗格中无可见属性且“显示属性文件夹”禁用时，属性文件夹仍显示的问题；修复了禁用“显示快捷方式和最近项图标”时也禁用了属性根虚拟文件夹图标的问题；修复了删除活动笔记时可能触发 Linter“文件未找到”错误的问题。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Neighbouring Files
   </span>
  </span>
  <span>
   By Fabian Untermoser
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增基于文件夹的导航命令；新增跨文件夹导航。
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
    Media Viewer
   </span>
  </span>
  <span>
   By Devon22
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    在上下文菜单中添加重命名选项；音乐文件也可以使用 img 参数设置缩略图。
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
    Diagram Zoom Drag
   </span>
  </span>
  <span>
   By ChenPengyuan
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    改进 SVG 图表导出：内联所有 CSS 样式，做到“屏幕所见即导出/复制所得”；新增：通过图片右键菜单复制完成后给出通知；调整：将 SVG 图片（图表等）恢复为在 Popup 模式中打开（beta）。
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
    Folder Links
   </span>
  </span>
  <span>
   By Stefan Rausch
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增对移动端的支持。
   </span>
  </p>
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
     更清晰的产品说明：文档明确说明 File Ignore 通过重命名磁盘上的文件/文件夹工作。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      恢复支持
     </span>
    </strong>
    <span>
     ：持久化最近批次状态，可从设置页面撤销中断的运行。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      更安全的批处理执行
     </span>
    </strong>
    <span>
     ：自动跳过受保护路径、目标冲突、重复目标以及当父目录已在重命名时的嵌套子条目。
    </span>
   </p>
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      执行前计划
     </span>
    </strong>
    <span>
     ：隐藏/显示现在在执行前计算重命名计划。
    </span>
   </p>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      数据与同步
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span style="color: rgb(40, 102, 186); text-decoration: underline;">
    <span>
     Google Contacts
    </span>
   </span>
   <span>
    By aleksejs1
   </span>
  </p>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    新增设置项：同步时可保留邮箱/电话/地址的类型标签（home/work/mobile）。
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
    Data Fetcher
   </span>
  </span>
  <span>
   By qf3l3k
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       导入支持两种 JSON 结构
      </span>
     </strong>
     <span>
      ：完整导出载荷
     </span>
     <span>
      <span>
       { version, exportedAt, endpoints }
      </span>
     </span>
     <span>
      或纯 endpoints 数组 JSON。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       设置中新增 Endpoint 导入/导出
      </span>
     </strong>
     <span>
      ，用于在设备间迁移别名配置。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       Endpoint 导入新增两种模式
      </span>
     </strong>
     <span>
      ：合并（按 alias 更新并追加新增项）或替换（覆盖当前全部 endpoints）。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    NotePix
   </span>
  </span>
  <span>
   By Ayush Parkara
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    添加了 mtime 安全的迁移写入，避免覆盖较新的编辑；添加了源笔记感知的替换回退，避免活动编辑器时机错过；添加了仓库候选限制和冷却时间，避免重复检查并减少延迟；添加了基于令牌的相同用户仓库发现，用于旧版图片解析；添加了安全的旧版链接迁移（从
   </span>
   <span>
    <span>
     obsidian://notepix/&lt;path&gt;
    </span>
   </span>
   <span>
    到 v2 格式），仅在成功解析仓库后执行。
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
    Instapaper
   </span>
  </span>
  <span>
   By Instapaper
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    可自定义笔记模板：使用 Mustache 模板完全控制高亮内容写入笔记的格式；可自定义文章属性：选择要写入的属性，并可重命名字段；为高亮生成块标识：使用 Obsidian 块引用语法 (
   </span>
   <span>
    <span>
     ^h{highlight_id}
    </span>
   </span>
   <span>
    )；最低 Obsidian 版本要求提升至 1.11.0。
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
    <strong>
     <span>
      PKMer出品
     </span>
    </strong>
   </p>
  </section>
 </section>
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
       <strong>
        <span>
         Info
        </span>
       </strong>
      </p>
     </section>
     <section style="text-align: justify;">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <strong>
        <span>
         PKMer
        </span>
       </strong>
       <span>
        （
       </span>
       <span style="color: rgb(40, 102, 186); text-decoration: underline;">
        <span>
         PKMer.cn
        </span>
       </span>
       <span>
        、
       </span>
       <span style="color: rgb(40, 102, 186); text-decoration: underline;">
        <span>
         PKMer.net
        </span>
       </span>
       <span>
        ）旨在打造东半球强大的知识管理社区。Personal Knowledge Management (PKM) + “er”，其中 “er” 表示人，专注、喜爱个人知识管理工作、追求效率的人们，都可以划入这个行列，希望社区凝聚更多这样的人。
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
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="color: rgb(40, 102, 186); text-decoration: underline;">
   <span>
    Floating Search
   </span>
  </span>
  <span>
   By Boninall
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left: 2px solid rgb(160, 160, 160);">
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       CMDK 快速搜索模态框
      </span>
     </strong>
     <span>
      ：通过
     </span>
     <span>
      <span>
       chooser.addSuggestion()
      </span>
     </span>
     <span>
      批量渲染建议项，提升 UI 流畅度；支持文件名/路径的模糊匹配 + 标题模糊匹配；使用 Obsidian
     </span>
     <span>
      <span>
       metadataCache
      </span>
     </span>
     <span>
      做渐进式标题搜索（零 I/O、即时结果）；支持双击 Shift（可配置）唤起快速搜索，并实时预览文件。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       新增设置
      </span>
     </strong>
     <span>
      ：双击间隔灵敏度（150ms–600ms）；快速搜索触发键可选 Double Shift / Ctrl / Alt / Meta，或禁用。 使用
     </span>
     <span>
      <span>
       setViewState
      </span>
     </span>
     <span>
      实现更可靠的文件导航，并支持 heading 子路径。 在 FloatSearchModal 中使用方向键导航时支持自动预览。
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <strong>
      <span>
       配图
      </span>
     </strong>
     <span>
      ：暂无官方配图。
     </span>
    </p>
   </li>
  </ul>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
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
  <p style="margin: 0px; padding: 0px;">
   <span>
    切换规则存储路径后：自动重新加载规则引擎，并即时刷新设置面板；设置面板新增：文件夹选择器（基于 AbstractInputSuggest）与迁移按钮；新增：支持自定义规则文件存储路径，可将规则文件存放在库内任意文件夹中，提升与 Obsidian Sync 的兼容性。
   </span>
  </p>
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
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/dibCdrCystEVgNvsKEnKNg9vbjZUnL2iab7apEnvFGPfuc7LzWb1phdjRAmGNHqib6Njk1D4M0MiaEnylj24q8R8FcqdrEzDqqqgWAAiciatPDcHU/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEViaQFshI8p7pI07M8c4fl3CiaetLkfrQQLVdKPiajD6JQFsPmUVTz2Vkpiauhnf2QOluru9HDQKYcsdicC3nav0L1n8XfhvHkDu7wA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/dibCdrCystEVMqm58T9Rbhmau0lVLzr6JaNMRgQA5oia11KyTk6GjWaDDDaLhofOeGrv2J1j11FkXlE23pCF3Mrp9rkj8EJJcsghQHV3wSG7o/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; width: 261.796875px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEUicMibDibdnLwdJozyjjvFUN6AsTiaENT7yt7E4fIyBoickJmnHCq9TdIUTia58m9vRaBUibb6DVW9iaXcmSlVtO9sozeAZfibv1EVBq8Y/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; width: 66.984375px !important; height: auto !important;" />
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
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEUf17ic2HnQn2J5dKmWud9doAxiaZtQfW10CHCO9qb8PhYGbnJX0zVsC5vYwxbDnNPMOib0iboQkwrsXoicF0TDIny034Oiat1aGDKGY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; width: 256.90625px !important; height: auto !important;" />
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
   <section style="font-size: 10px; letter-spacing: 2px; color: rgb(57, 57, 57);">
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
