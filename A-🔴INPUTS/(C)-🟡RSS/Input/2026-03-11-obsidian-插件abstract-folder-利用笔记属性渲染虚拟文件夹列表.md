---
title: "Obsidian 插件：Abstract Folder 利用笔记属性渲染虚拟文件夹列表"
url: "https://mp.weixin.qq.com/s/MAkSIbLJNcp_UiCN5hoSxg"
source: "PKMer知识社区"
date: 2026-03-11
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了 Obsidian 插件“Abstract Folder”，该插件通过在笔记 Frontmatter 中定义父子关系，构建虚拟文件夹结构，实现笔记的多归属、无重复分类与灵活层级管理。插件摒弃传统物理文件夹的刚性限制，支持单向/双向连接、彩色缩进树状视图、垂直 Miller 列视图及工作区分组等功能，并提供物理文件夹与抽象结构双向转换工具，兼顾灵活性与兼容性。作者从PKM中“过度分类”痛点出发，阐述了该设计如何更贴合人类思维的网状关联本质。

---

<section style="color: rgb(57, 57, 57); letter-spacing: 1px; padding-left: 15px; padding-right: 15px; line-height: 1.75; font-size: 14px; font-style: normal; font-weight: 400; text-align: justify; margin-bottom: 0px;">
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 100%;">
   <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEVxkXdVhN2b6aw5qK0yTmPLBicKuEnnhKgu9rALricTO74NKekamfKp5ZjQiaHWamkLEy78ydMjYlAt5YgiaUBpooa4CezVl1KRGOk/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
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
       <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEVSIiaJ2oxd5esqfBcxeNne4gfyAiaEerfCtVdEdQbvf77AEJyGFkxicq3KTW3ia8vyZSdF33sLgs4ZInK184uC6adjhFhv9nuH4WU/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
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
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEX9GnI1CodAhHz7LfbBPn63ibu6iaVqrhMmoSWfxUn97jW6W6aqtaTTg1AphF6icCKEz1FHTrCgsibzlVE7gK9pn3kLPATDFNjFAgA/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="text-align: center; font-size: 18px; color: rgb(169, 152, 255);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Obsidian 插件：Abstract Folder
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    利用笔记属性渲染虚拟文件夹列表
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
        插件名片
       </span>
      </p>
     </section>
     <section style="text-align: justify;">
      <ul class="list-paddingleft-2" style="padding-left: 20px;">
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件名称：Abstract Folder
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件作者：RahmaniErfan
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件版本：1.14.0
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件概述：Abstract Folder在 Obsidian 中创建了一个虚拟文件浏览器，它的结构由用户在 Frontmatter 中定义。任何文件都可以是其它文件的“亲文件夹”；任何文件都无须一式多份，即可同时属于多个“文件夹”。如果用户想要修改上下级关系，只需改动文本即可，真实的文件系统结构不会受到任何改动。
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件项目地址：
         </span>
         <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
          <span>
           点我跳转
          </span>
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          国内下载地址：
         </span>
         <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
          <span>
           下载安装
          </span>
         </span>
        </p>
       </li>
      </ul>
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
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <b>
     <span>
      术语解说
     </span>
    </b>
   </p>
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px; width: 100%; background-color: rgb(247, 247, 247); padding: 19px; border-left-width: 2px; border-left-style: solid; border-left-color: rgb(160, 160, 160);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    以下作者在个人播客中写的一篇文章，说明了他为什么要写这个插件，在开始阅读插件文档之前，请先阅读这篇文章以期获得更深入的了解。
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span style="font-size: 15px;">
   <strong>
    <span style="color: rgb(47, 200, 255);">
     <span>
      为什么使用文件夹
     </span>
    </span>
   </strong>
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    对于文件夹是什么，我就不多废话了。好吧，可能还是要说一下。文件夹早在操作系统和计算机出现之前就已经存在（是不是很意外）。它的理念是：一个文件夹代表一个通用类别，用来存放属于该类别的项目。这个文件夹会被放进一个抽屉，而这个抽屉又按更广泛、更通用的类别进行分类。文件夹本身也会有子类别，通过那些小标签进行组织。这个概念被引入操作系统中，而且它确实很合理。它们的工作方式是一样的。然而，当涉及到 PKM（个人知识管理）工具时，就出现了一个巨大的问题——过度分类的陷阱：“我最顶层的文件夹应该是什么？”“这个文件该放在这个文件夹，还是那个？好像两个都属于……”
   </span>
  </p>
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
     为什么它们行不通
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    人类的思想是复杂的，复杂在它们之间的连接是无限的。而文件夹是刚性的；它们无法支撑这一复杂的连接系统。一个文件必须归属于单一一个文件夹，而一个想法却可以同时属于多个类别。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    假设你刚开始记笔记。最初你的文件以扁平结构组织，没有创建任何文件夹。然后你决定要整理一下。你首先要做的是想出这些文件所属的最一般领域或范围。你决定分为 Work（工作）、Personal（个人）和 University（大学）。这些是居于所有其他类别之上的通用分类。你开始把文件分别放进对应的文件夹，直到某样东西让你停了下来。“嗯，这是一个日志文件。我在所有主分类下都有日志。那是不是意味着我要在每个主文件夹下面都创建一个‘日志’文件夹？”于是你这么做了。然后你意识到你希望有一个统一视图，可以快速查看所有日志。但你无法轻松做到这一点。于是你开始使用属性。你的工作日志文件会有一个值为 Work 的属性 ”domain“，还有一个值为 Logs 的 ”subdomain“。然后再用标签来细化。这听起来比创建无限的子子子子分类要好。两个属性加标签，似乎不错。
   </span>
  </p>
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
     这听起来是不是非常非常耗时又令人沮丧？
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    是的，确实如此。至少对我来说是这样。所以我在想，应该有更好的方式。既然文件夹结构本身已经描述了文件——个人→个人计划→为什么文件夹烂透了——这个结构已经说明了一切。那为什么我们只是为了让这个僵硬的系统稍微灵活一点，就要被迫添加属性？
   </span>
  </p>
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
     如何摆脱它
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    操作系统中文件夹的运作方式很简单（好吧，其实并非如此，但我会简化说明）：你有一个文件夹，这个文件夹可以链接到其他文件夹。就这样——一个单一的值就决定了它们之间的关系。根文件夹则没有链接。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    我把这个想法应用到了我制作的 Obsidian 插件中（顺便说一句，我还没提到它的名字，叫 Abstract Folder）。我意识到，文件夹结构本身已经描述了文件的分类。我所需要的只是一个单一的值，用来建立文件之间的连接。我甚至根本不需要文件夹，哈哈！而且，我还可以添加任意多个亲级！（后来我意识到这些文件还有其他用途，而且整个操作系统都是围绕文件夹构建的，所以彻底去掉文件夹会带来问题。）
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    我决定使用 Markdown 笔记的 Frontmatter 区来创建这种连接。简单的解决方案！现在，如果我有一个叫“为什么文件夹烂透了”的文件，我可以把它链接到一个名为“个人”的亲“文件夹”，它就等于被分类了，某种意义上。我将完全依赖这些连接，不需要任何“物理”文件夹。但这带来了一个问题。某些文件没有 Frontmatter。实际上，大多数文件都没有。如果你不知道什么是 Frontmatter，在 Obsidian 中，它基本上就是笔记顶部的 以 YAML 语言写成的笔记属性，用来列举元数据。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    为了解决这个问题，有几种办法。但我意识到最简单也是最好的方案是使用单向关系。一个亲文件可以有亲级，但也可以同时有子级！因此，举例来说，在亲文件“个人计划”中，我会添加一个名为”children“的属性用来列出它的子文件。整个“文件夹结构”将通过同时查看 parents 和 children 来构建。
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    很多问题解决了，但还有一些。我之前提到完全没有文件夹会导致的问题。整个操作系统都依赖这个系统。如果你想把文件转移到其他地方，或者从 Obsidian 迁移到别的应用，一切都会变成扁平结构。所以我修复了这个问题。我创建了一个转换工具，可以根据文件之间的链接关系导出实际的文件夹结构。与此同时，我也创建了反向转换工具——将传统文件夹结构转换为这个插件使用的“抽象文件夹”格式。简单来说，这个转换工具会检查文件夹及其内容，并自动添加相应的属性。如果文件不是 Markdown 文件，它们会在亲文件中被声明为子文件。
   </span>
  </p>
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
     我还添加了一些可用性功能：
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     彩色缩进，用于区分树状视图的层级深度（可自定义）
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     垂直 Miller 列视图，类似 macOS 中 Finder 的列视图，但方向为垂直排列
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     工作区分组（Workspace groups）：可以创建不同分组来切换过滤视图。例如，你的工作分组只显示
    </span>
    <span style="color: rgb(40, 102, 186); text-decoration: underline;">
     <span>
      work.md
     </span>
    </span>
    <span>
     和
    </span>
    <span style="color: rgb(40, 102, 186); text-decoration: underline;">
     <span>
      todo.md
     </span>
    </span>
    <span>
     的子文件
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     图标
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
     以及大量兼容性功能：
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     显示非 Markdown 文件的文件格式
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     右键菜单显示菜单项（包括其他插件的指令）
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     通过右键创建笔记，可以在空白处创建，也可以在文件上下文中创建（例如在某个文件“下方”创建）
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     别名（Aliases）
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     排序
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     以及一些我记不太清的小功能（概念上小，但开发起来并不小……）
    </span>
   </p>
  </li>
 </ul>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    当然，这个插件也不是完美无缺的。还是有一个问题。在传统文件夹系统中，只要位于不同文件夹，你可以拥有同名文件。但在扁平结构中不行。我考虑过一些解决方案，比如使用 ID 替代文件名，但那会带来其他问题。所以我选择添加别名功能。你可以使用一个具有描述性的真实文件名，然后添加 alias 属性作为显示名称；或者使用命令在重名时自动生成唯一文件名。
   </span>
  </p>
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
     现在你拥有以下“特权”：
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     可以把“文件夹”当作真正的文件使用！就像 Notion 那样。你可以在这个通用类别文件里直接记录相关内容。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     创建“幽灵节点”（ghost nodes）！你可以有一个名为 logs 的亲文件，而你的工作、个人和大学日志都可以连接到它，从而统一归类。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     图标！（虽然有其他插件也能实现，但我还是加了）
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     不用担心“无法回退”，因为你可以随时把扁平结构转换回真实文件夹结构。
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     隐藏笔记。是的，我差点忘了提。你可以隐藏整个抽象文件夹！
    </span>
   </p>
  </li>
 </ul>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    你也可以给我打赏，链接在 GitHub 仓库里 ;)。我也许应该把这句话放在最前面，因为不是每个人都会读到这里。不过如果你读到了，谢谢你的阅读！
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
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
      基本用法
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    简单来说，
   </span>
   <span>
    <span>
     Abstract Folder
    </span>
   </span>
   <span>
    的原理就是根据笔记属性中规定的亲子关系，渲染出一个虚拟文件夹列表，与笔记文件在系统资源管理器中的实际位置无关，如此一来，无须再操心文件的物理位置，哪怕所有文件都以扁平结构位于库下，只要笔记属性中存在亲子关系，插件就能在虚拟文件夹列表中虚拟地渲染出文件夹结构
   </span>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在命令面板中执行
     </span>
     <span>
      <span>
       Abstract Folder: Open View
      </span>
     </span>
     <span>
      命令，然后手动在笔记属性区为当前文件指定其亲文件，
     </span>
    </p>
   </li>
   <ul class="list-paddingleft-2" style="padding-left: 20px;">
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       具有单个亲文件的子文件的笔记属性例`parent: “[[亲文件名1]]”
      </span>
     </p>
    </li>
    <li>
     <p style="margin: 0px; padding: 0px;">
      <span>
       具有多个亲文件的子文件的笔记属性例：
      </span>
      <span>
       <span>
        parent: ["[[亲文件名1]]", "[[亲文件名2]]"]
       </span>
      </span>
     </p>
    </li>
   </ul>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      如果用户希望自上而下地指定亲子关系，对于不支持属性区的格式比如白板、
     </span>
     <span>
      <span>
       Excalidraw
      </span>
     </span>
     <span>
      、图片或 pdf 等文件，可以在亲文件的笔记属性区将它们指定为子文件，例：`children: [“[[子文件名1]]”, “[[子文件名2]]”]
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      同一个文件可以有多个亲文件或多个子文件，建议将属性格式设置为列表
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      如果用户想要为某子文件更换亲文件，直接在虚拟文件夹列表中拖拽即可，直接拖拽是剪切，按住
     </span>
     <span>
      <span>
       Ctrl
      </span>
     </span>
     <span>
      键同时拖拽是复制，笔记属性区会自动更改
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
     将已有文件夹架构转化为虚拟文件夹
    </span>
   </strong>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   如果想将已有文件夹架构转化为虚拟文件夹（原文件夹结构并不会被破坏），点击
  </span>
  <span>
   <span>
    Abstract Folder
   </span>
  </span>
  <span>
   虚拟文件夹列表上方工具栏左起第三个按钮，或执行命令面板中的
  </span>
  <span>
   <span>
    Abstract Folder: Convert folder structure to plugin format
   </span>
  </span>
  <span>
   命令，在选择需要转换的文件夹后，会弹出如图对话框：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEVunbDcoEoDjUJYibKiaiauG5fIt3t29e4kg8QFrYEia0zHZtmHpiayjDeaSslbylGMQNjbpjicV5CWibMwLGw1w1RRmiasjmlViaIhVSqM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; width: 615px !important; height: auto !important;" />
  </section>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Create parent notes
     </span>
    </span>
    <span>
     ：如启用，若将要转换的文件夹没有一个同名文件，则为它创建一个
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Existing relationships
     </span>
    </span>
    <span>
     ：如将要转换的文件夹下的文件的parent属性中已指定亲文件，则
    </span>
   </p>
  </li>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Append new parents
      </span>
     </span>
     <span>
      ：在parent属性的末尾加上新的亲文件
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Replacing existing parents
      </span>
     </span>
     <span>
      ：将原有亲文件转换为新制定的亲文件
     </span>
    </p>
   </li>
  </ul>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Folder note strategy
     </span>
    </span>
    <span>
     ：决定要在哪里搜索将要转换的文件夹的同名文件
    </span>
   </p>
  </li>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Outside (Sibling note, e.g. "Folder.md" next to " Folder/")
      </span>
     </span>
     <span>
      ：在该文件夹外，与其平级
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Inside (Index note, e.g. "Folder/Folder.md")
      </span>
     </span>
     <span>
      ：在该文件夹内点击确认后，插件会自动为文件夹中的子文件创建parent属性（属性名文本可在设置中修改）并指定亲文件
     </span>
    </p>
   </li>
  </ul>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   Abstract Folder虚拟文件夹列表渲染效果如图：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEV3ZGIzmShezDu3R3icGV7IgI2PQAYH73bmAMib0n4J5nY58HLCbiakLuZVgOpChvibicYS5vRvYk1iaYlwrMeYm33iaRMR1rGN6hOA08/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    也可以在命令面板中执行
   </span>
   <span>
    <span>
     Abstract Folder: Create folder stucture from plugin format
    </span>
   </span>
   <span>
    命令，将原来并非处于文件夹结构，但已经在笔记属性区指定亲/子文件的文件在系统资源管理器中创建传统的文件夹结构
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      自定义分组视图
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    如果想列出某个特定笔记文件的所有子文件，可点击
   </span>
   <span>
    <span>
     Abstract Folder
    </span>
   </span>
   <span>
    虚拟文件夹列表上方工具栏左起第八个按钮，在下拉菜单中选择
   </span>
   <span>
    <span>
     Manage groups
    </span>
   </span>
   <span>
    再选择
   </span>
   <span>
    <span>
     Add new group
    </span>
   </span>
   <span>
    ，或执行命令面板中的
   </span>
   <span>
    <span>
     Abstract Folder: Manage groups
    </span>
   </span>
   <span>
    会弹出如下对话框：
   </span>
  </p>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEU9hwT6CL6jBJM9n2opGibP9a1ibbrKsahtyb00DnvWT3zfnF2KpQEHY9ahxezX5H35n2AmrSp6YgupibkcZic0JFuK2xfNUSicM014/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Group name
     </span>
    </span>
    <span>
     ：在空白栏中填入的文本将被视为分组名
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Add parent note
     </span>
    </span>
    <span>
     ： 在空白栏中填入需要作为亲文件的笔记文件点击加号选择库内笔记文件
    </span>
   </p>
  </li>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   如果想直接以当前笔记文件为亲文件创建分组，在命令面板中执行
  </span>
  <span>
   <span>
    Abstract Folder: Creat group with active file
   </span>
  </span>
  <span>
   命令即可
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
      独特排序
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    点击虚拟文件夹列表最上方工具栏左起第六个按钮，可以对文件进行排序，除了常见的首字母、创建时间和修改时间之外，
   </span>
   <span>
    <span>
     Abstract Folder
    </span>
   </span>
   <span>
    还提供了以下三种独特的排序方式：
   </span>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Sort by thermal
      </span>
     </span>
     <span>
      ：插件会根据每 24 小时内的最新程度和互动辨别库的哪一部分当前正在使用，一个笔记文件被打开得越多，其亲子关系变化得越多，它的分数就越高
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Sort by stale rot
      </span>
     </span>
     <span>
      ：插件会根据笔记文件的最后一次编辑日期计算其不活跃时间，一个笔记文件的子文件越多，而且其不活跃时间越长，它的分数就越高，有助于用户重温重要但被忽视已久的笔记
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Sort by gravity
      </span>
     </span>
     <span>
      ：插件会计算含子文件最多的亲文件，并据此进行排序
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
      设置说明
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
      Excluded Paths
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    在空白栏中填入的文件夹路径将被插件忽略
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
      Properties
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Parent Property Names
      </span>
     </span>
     <span>
      ：在空白栏中填入的属性名称将被用来指定该笔记文件的亲文件，可设置多个，用英文逗号隔开，区分大小写
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Children Property Names
      </span>
     </span>
     <span>
      ：在空白栏中填入的属性名称将被用来指定该笔记文件的子文件，可设置多个，用英文逗号隔开，区分大小写
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Created date field names
      </span>
     </span>
     <span>
      ：在空白栏中填入的属性名称将被用来存放该笔记文件的创建时间
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      <span>
       Modified date field names
      </span>
     </span>
     <span>
      ：在空白栏中填入的属性名称将被用来存放该笔记文件的最后一次修改时间
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
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     Display name
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Show Aliases
     </span>
    </span>
    <span>
     ：如启用，则aliases属性的第一个值将被用作文件在虚拟文件夹列表中的显示名
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Display name priority
     </span>
    </span>
    <span>
     ：在空白栏中有三个属性名称，分别为basename、aliases和title，它们分别代表文件在系统资源管理器中的文件名、笔记属性中用aliases指定的别名、用title指定的标题，用户可自定义其先后顺序以决定其在虚拟文件夹列表中的优先级，用英文逗号隔开
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
     Behavior
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Expand parent folder for active file
     </span>
    </span>
    <span>
     ：如启用，则插件将自动在虚拟文件夹列表中展开当前文件的所有亲文件，并高亮当前文件
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Scroll to active file
     </span>
    </span>
    <span>
     ：如启用，则虚拟文件夹列表将自动滚动至该文件位置以展示其亲子关系
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Expand children when opening a file
     </span>
    </span>
    <span>
     ：如启用，则插件将自动在虚拟文件夹列表中展开当前文件的直接子文件
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Expand target folder on drap &amp; drop
     </span>
    </span>
    <span>
     ：如启用，在虚拟文件夹列表中拖拽文件时，目的亲文件将自动展开
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Remember expanded folders
     </span>
    </span>
    <span>
     ：如启用，则哪怕用户转换视图或重启软件，虚拟文件夹列表也将保持上一次的展开状态
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
     Startup &amp; Layout
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Default new note path
     </span>
    </span>
    <span>
     ：在空白栏中填入的文件夹路径将被视作新文件的默认创建路径，如留空，则新文件将被默认创建在库根目录下
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Open on Startup
     </span>
    </span>
    <span>
     ：如启用，则虚拟文件夹列表将随 Obsidian 自动启动
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Open Position
     </span>
    </span>
    <span>
     ：选择虚拟文件夹列表是在左侧边栏还是右侧边栏
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Show Ribbon Icon
     </span>
    </span>
    <span>
     ：如启用，则将在功能区显示插件的命令按钮
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
     Visuals
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Enable Rainbow Indents
     </span>
    </span>
    <span>
     ：如启用，则虚拟文件夹列表将用彩色缩进线在视觉上区分层级
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Rainbow Palette
     </span>
    </span>
    <span>
     ：为彩色缩进线选择样式
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Rainbow indent-varied item colors
     </span>
    </span>
    <span>
     ：启用后没看出来有什么变化
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
     Toolbar &amp; Search
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     前十个选项依次为：自定义是否展示虚拟文件夹列表上方工具栏的搜索、视图切换、聚焦当前文件、转换虚拟文件夹/真实文件夹、全部收起、全部展开、排序、筛选、分组和新建笔记按钮
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Max menu name length
     </span>
    </span>
    <span>
     ：在 10-100 范围内选择右击文件名唤出的菜单所能显示的最大文件名字符数
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
     Naming conflicts
    </span>
   </strong>
  </p>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Conflict resolution strategy
     </span>
    </span>
    <span>
     : 在扁平结构内，如何处理重名文件，可以选择分别命名、亲文件或最上级亲文件
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Conflict separator
     </span>
    </span>
    <span>
     ：选择是用 dash 还是 bracket 来隔开亲文件名和文件名，例：亲文件名 - 文件名，亲文件名 [文件名]
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Conflict naming order
     </span>
    </span>
    <span>
     ：选择是亲文件名在前还是文件名在前
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
     Debug：
    </span>
   </strong>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   向插件作者反映 bug 用的，不高兴翻译了，自己看吧，看不懂说明你用不上ψ(｀∇´)ψ
  </span>
 </p>
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
        讨论
       </span>
      </p>
     </section>
     <section style="text-align: justify;">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
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
         <img src="https://mmbiz.qpic.cn/mmbiz_jpg/dibCdrCystEVVQzhic4w5Mkw189EdtKdPxww4mhG1gADTSM2OIepQxTEVaJHibfGSEu6r3C5q5PS7dcrgaI3RZlHeW8wXz3YOzXXf5jjLhaUOs/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEVia5GXkxPRHj2gML7OIOOt4Ug71AZ0hRPQne4iar09ib8HwkEbHByvdGhkAzZrIwkQdiagNoxedInSVzhjbqK3xYUlm2TU2H6qtdo/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/mmbiz_jpg/dibCdrCystEUyRKoXYghBBXg9xcsia8svkqQBd2PWoVRU6MpvHKB1pY8EdWPNB39Q6kmW7y6Q3aBPAsG8GAwNLfO5YRRQRwIp9rc3GfFNcHN0/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; width: 261.796875px !important; height: auto !important;" />
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
         <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEX0IbAv5NFXMMSN0eFyBdFYZLLlP3D3I2gX0vIHHnGfB8fqGOACBGFEsGC1CUzaxHzMUBdnUiadDlX1eGYLBjsa1r1EM2GnDZr8/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; width: 66.984375px !important; height: auto !important;" />
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
            ：血海狂屠
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEUN4OHnJOSlJ2kllFnfCicvpJib1V3z6xWcuq3AzbISoGYZDwQ1WcTkZMsQw5fBB9QSpdmuLjicTCEklb0ibaMfTRJNBibNN6fnX3w8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="vertical-align: middle; width: 256.90625px !important; height: auto !important;" />
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
