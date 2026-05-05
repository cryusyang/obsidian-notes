---
title: "【工具推荐】一款管理Markdown知识库的开源macOS应用程序"
url: "https://mp.weixin.qq.com/s/TWrTu6oojchz9Xs6LiMTng"
source: "骨哥说事"
date: 2026-04-24
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Tolaria 是一款面向 macOS 的原生桌面应用，旨在构建“AI 可理解的个人知识库”，而非传统笔记工具。它以 Markdown 为基础，强调结构化（类型/属性系统）、关系建模与 Git 原生支持，使 AI Agent 能高效读取、编辑、连接和沉淀上下文。其核心目标是解决 AI 编程中的长期挑战：提供持久化上下文、支持多 Agent 协作、管理项目知识并记录决策过程。相比 Obsidian（侧重人类使用），Tolaria 更聚焦于人机协同的知识操作系统。

---

<section>
 <h1 style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这两天，一个叫
  </span>
  <strong>
   <span>
    Tolaria
   </span>
  </strong>
  <span>
   的新项目在开发者圈开始被讨论。它不是又一个 ChatGPT 套壳，也不是普通笔记软件，而是一个非常有意思的方向：
  </span>
 </h1>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     让 AI 和人类一起管理知识库、协作开发、沉淀上下文。
    </span>
   </strong>
  </p>
 </blockquote>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgyNSH3t6P5WTgcicTJnIoWCeG8zvy4D1YFsbgO69QI1582lBjibicuk6X6vTwZvYhz6oddib9pwM5EAt2ib4wLEtPJGiaA0eic7ZDlTY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 660px !important;" />
 </section>
 <figure style="margin: 10px 0px; display: flex;">
  <span>
   <br />
  </span>
 </figure>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h1 style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Tolaria 是一个
  </span>
  <strong>
   <span>
    macOS 原生桌面应用
   </span>
  </strong>
  <span>
   ，用于管理 Markdown 知识库，同时让 AI Agent 更容易理解、读取、编辑你的知识系统。
  </span>
 </h1>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   简单说：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     Obsidian 是给人用的第二大脑
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     Notion 是团队协作数据库
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     Cursor 是 AI 写代码工具
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      Tolaria 是 AI + 知识库 + 工作流操作系统
     </span>
    </strong>
   </section>
  </li>
 </ul>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h1 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   AI 编程的核心问题，已经不是写代码了
  </span>
 </h1>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   而是：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     如何给 AI 提供长期上下文？
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     如何让多个 Agent 协作？
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     如何沉淀决策记录？
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     如何管理项目知识，而不是一次次重复提示词？
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Tolaria 就是在解决这个问题。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   项目作者甚至说：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    这是他与 AI 协作的主界面，AI 会在里面创建笔记、连接信息、编辑已有内容。
   </span>
  </p>
 </blockquote>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h1 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   为什么 Markdown 很重要？
  </span>
 </h1>
 <p style="font-weight: bold; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255); padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   对人类：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     可读
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     可迁移
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     不锁平台
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     Git 友好
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <span>
     可长期保存
    </span>
   </section>
  </li>
 </ul>
 <h3 style="font-weight: bold; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255); padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   对 AI：
  </span>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     纯文本结构清晰
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     容易索引
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     容易 RAG 检索
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     容易编辑
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     容易建立知识图谱
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   换句话说：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    Tolaria 不是做笔记工具，而是在做
   </span>
   <strong style="font-weight: bold; color: black;">
    <span>
     AI 可理解的个人数据库
    </span>
   </strong>
  </p>
 </blockquote>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h1 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   和 Obsidian 最大区别是什么？
  </span>
 </h1>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   用户评论有人直接问了这个问题，作者回答：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Tolaria 更关注：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     关系建立
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     属性系统
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     类型系统
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     First-class Git 支持
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   也可以理解为：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Obsidian 偏个人笔记， Tolaria 偏
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    AI 协作知识系统
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   项目地址：
   <span style="text-decoration: underline;">
    https://github.com/refactoringhq/tolaria
   </span>
  </span>
 </p>
</section>
<hr />
<section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <br />
  </span>
 </p>
 <p style="margin-bottom: 32px; border-width: 0px; border-color: initial; line-height: inherit; vertical-align: baseline; letter-spacing: normal; text-align: left;">
  <strong>
   <span style="font-size: 18px;">
    <span>
     <span style="font-weight: bold;">
      感谢阅读，如果觉得还不错的话，动动手指给个三连吧～
     </span>
    </span>
   </span>
  </strong>
 </p>
</section>
<p style="display: none;">
 
 
</p>
