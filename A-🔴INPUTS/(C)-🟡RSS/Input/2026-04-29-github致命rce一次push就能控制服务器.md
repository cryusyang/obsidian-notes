---
title: "GitHub致命RCE！一次Push就能控制服务器"
url: "https://mp.weixin.qq.com/s/_KGe8FSfUcjotKBs7LkWVA"
source: "骨哥说事"
date: 2026-04-29
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Wiz研究团队利用AI增强的逆向工程工具，在GitHub内部git基础设施中发现高危注入漏洞CVE-2026-3854，允许经认证用户仅通过一条`git push`命令即可在GitHub.com共享节点或GitHub Enterprise Server（GHES）上执行任意代码，威胁数百万公私仓库及系统密钥。该漏洞源于多服务架构中对不安全`X-Stat`头部的盲目信任与“后写入优先”解析机制，是首批由AI在闭源二进制中发现的关键漏洞之一。GitHub已在6小时内缓解GitHub.com风险并发布GHES补丁（3.19.3+），但目前仍有88%的GHES实例未升级，亟需立即更新。

---

<table>
 <tbody>
  <tr>
   <td valign="top" width="557">
    <h1>
     <strong>
      <span style="font-size: 18px;">
       <span style="color: rgb(255, 0, 0);">
        <strong>
         <span style="font-size: 15px;">
          <span>
           声明：
          </span>
         </span>
        </strong>
       </span>
      </span>
     </strong>
     <span style="font-size: 18px;">
      <span style="font-size: 15px;">
       <span>
        文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。
       </span>
      </span>
     </span>
    </h1>
   </td>
  </tr>
 </tbody>
</table>
<h1>
 <span>
  <br />
 </span>
</h1>
<section style="margin-bottom: 0px;">
 <span>
  
  
 </span>
</section>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span style="letter-spacing: 0.544px; background-color: rgb(255, 251, 0);">
  <strong>
   <span>
    <br />
   </span>
  </strong>
 </span>
</p>
<h1>
 <span style="letter-spacing: 0.544px; background-color: rgb(255, 251, 0);">
  <strong>
   <span>
    防走失：
   </span>
  </strong>
  <strong>
   <span style="color: rgb(0, 82, 255);">
    <span>
     https://gugesay.com/
    </span>
   </span>
  </strong>
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   不想错过任何消息？设置星标
  </span>
 </strong>
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   ↓ ↓ ↓
  </span>
 </strong>
</p>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="text-align: center; margin-bottom: 0px;">
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="width: 247px !important; height: auto !important;" />
 </span>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <span>
  Wiz研究团队在GitHub内部的git基础设施中发现了一个高危漏洞（CVE-2026-3854），可能同时影响GitHub.com和GitHub Enterprise Server。通过利用GitHub内部协议中的一个注入漏洞，任何经过身份验证的用户仅需一个标准的git客户端和一条
 </span>
 <code>
  <span>
   git push
  </span>
 </code>
 <span>
  命令，就能在GitHub的后端服务器上执行任意命令。
 </span>
</p>
<p>
 <span>
  值得注意的是，这是利用AI在闭源二进制文件中发现的首批高危漏洞之一，标志着此类漏洞识别方式的转变。尽管底层系统复杂，但该漏洞的利用却异常简单。在GitHub.com上，此漏洞允许在共享存储节点上执行远程代码。该研究团队确认，受影响的节点上可以访问属于其他用户和组织、数量达数百万计的公共及私有仓库。在GitHub Enterprise Server上，同一漏洞会造成服务器完全被攻陷，包括访问所有托管的仓库和内部密钥。
 </span>
</p>
<p>
 <span>
  GitHub在收到报告后的6小时内，对GitHub.com上的此问题进行了缓解，为所有受支持的GitHub Enterprise Server版本发布了补丁，并在发布时公布了CVE。
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   GitHub Enterprise Server客户应立即升级——截至本文撰写时，数据表明仍有88%的实例处于易受攻击状态。
  </span>
 </strong>
 <span>
  详细的修复步骤和更深入的技术细节可在 GitHub的安全博客文章 中查阅。
 </span>
</p>
<blockquote>
 <p style="margin: 0px 0px 0.75em; padding: 0px; border: 0px; font-style: inherit; font-weight: 400; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(80, 89, 102);">
  <span>
   GitHub 高度赞赏 Wiz 团队在整个过程中展现的合作、专业精神与伙伴关系。如此高水平和严重性的发现实属罕见，为我们漏洞赏金计划赢得了最高等级的奖励之一。这也提醒我们，最有影响力的安全研究来自那些知道如何提出正确问题的熟练研究人员。随着形势的发展，与有才华的漏洞猎人和研究人员建立紧密的合作关系比以往任何时候都更加重要。
  </span>
 </p>
 <p style="margin: 0px 0px 0.75em; padding: 0px; border: 0px; font-style: inherit; font-weight: 400; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(80, 89, 102);">
  <span>
   Alexis Wales, GitHub首席信息安全官（CISO）
  </span>
 </p>
</blockquote>
<p>
 <span>
  本文剖析了该漏洞，阐述了完整的利用链条，并为GHES管理员提供了保护其环境的建议。
 </span>
</p>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZia1BxJoniaC2nib8tHhd37nLbsAaGGHLlHgrBc9gXVX32VFCmI8P6dKpQx7sxsdOYuBHJO9pibVbOHIncyy3j5RM7Sk7Hs0Kw7dJ0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; height: auto !important; width: 680px !important;" />
 </span>
 <span>
  <br />
 </span>
 <span>
  图示：漏洞概述——一次
 </span>
 <code>
  <span>
   git push
  </span>
 </code>
 <span>
  即可攻陷GitHub内部基础设施
 </span>
</p>
<p>
 <span style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  需要采取的行动与缓解措施
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   GitHub.com：
  </span>
 </strong>
 <span>
  GitHub已缓解此问题。GitHub.com用户无需采取任何行动。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   GitHub Enterprise Server：
  </span>
 </strong>
 <span>
  需要立即行动。
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
  <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
   <span>
    升级到GHES 3.19.3或更高版本
   </span>
  </strong>
  <section>
   <span>
    – 此版本修复了
   </span>
   <code>
    <span>
     CVE-2026-3854
    </span>
   </code>
  </section>
 </li>
</ul>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   受影响的版本
  </span>
 </strong>
</h3>
<table>
 <thead>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <section>
     <span>
      组件
     </span>
    </section>
   </th>
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <section>
     <span>
      受影响的版本
     </span>
    </section>
   </th>
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <section>
     <span>
      已修复版本
     </span>
    </section>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      GitHub Enterprise Server
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      &lt;= 3.19.1
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      3.14.24, 3.15.19, 3.16.15, 3.17.12, 3.18.6 及 3.19.3
     </span>
    </section>
   </td>
  </tr>
 </tbody>
</table>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   使用Wiz查找易受攻击的GHES实例
  </span>
 </strong>
</h2>
<p>
 <span>
  Wiz客户可以使用 Wiz威胁中心中的这个预构建查询 ，识别其环境中易受此漏洞影响的GitHub Enterprise Server实例。该查询能找出所有运行着受此问题影响版本的GHES实例。
 </span>
</p>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjqcMeaMLibsXjTp6jFhFic2DPoUGsiaEDn5eoOr9FgIaGQV73iapI4xGUaeNyLmTvDLFl6btOKk8oZhCcvkqUTmge4UhqpEGqOTVQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; height: auto !important; width: 680px !important;" />
 </span>
 <span>
  <br />
 </span>
 <span>
  图示：用于查找易受攻击GHES实例的Wiz威胁中心查询界面
 </span>
</p>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   我们为何研究GitHub的Git基础设施
  </span>
 </strong>
</h2>
<p>
 <span>
  GitHub是全球最大的代码托管平台，是数亿个仓库的家园，涵盖了开源项目、企业代码库和关键基础设施。其内部的git基础设施——处理每一次
 </span>
 <code>
  <span>
   git push
  </span>
 </code>
 <span>
  操作的管道——是互联网上最安全敏感的的系统之一。当用户推送代码时，它会通过多个内部服务，每个服务由不同的编程语言编写。这种多服务架构造成了各个组件在解析和信任共享数据方式上的不一致性。
 </span>
</p>
<p>
 <span>
  Wiz研究团队过去曾深入研究GitHub Enterprise Server（GHES），以寻找这类漏洞。然而，要提取和分析运行此管道的海量编译后黑盒二进制文件，过去需要花费大量不切实际的时间和人工成本。
 </span>
</p>
<p>
 <span>
  但这是第二回合，格局已经改变。通过利用AI增强的工具——特别是使用IDA MCP进行自动化逆向工程——研究团队得以完成此前成本过高的任务。借助AI，他们能快速分析GitHub的编译后二进制文件，重建内部协议，并系统地识别用户输入可以在整个管道中影响服务器行为的位置。得益于这种新能力，他们发现了用户输入在GitHub多服务架构中流转的根本性缺陷。
 </span>
</p>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   技术深度剖析
  </span>
 </strong>
</h2>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   理解架构
  </span>
 </strong>
</h3>
<p>
 <span>
  当用户通过SSH向GitHub执行
 </span>
 <code>
  <span>
   git push
  </span>
 </code>
 <span>
  时，请求会流经以下几个关键组件：
 </span>
</p>
<ol class="list-paddingleft-1">
 <li style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <code>
     <span>
      babeld
     </span>
    </code>
   </strong>
   <span>
    – 一个git代理，是所有git操作的入口点。它接收用户的SSH连接，并将身份验证请求转发给
   </span>
   <code>
    <span>
     gitauth
    </span>
   </code>
   <span>
    。
   </span>
  </p>
 </li>
 <li style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <code>
     <span>
      gitauth
     </span>
    </code>
   </strong>
   <span>
    – 一个内部身份验证服务。它验证用户的凭据，检查用户是否拥有对目标仓库的推送权限，并返回适用于会话的安全策略——文件大小限制、分支命名规则等。
   </span>
   <code>
    <span>
     babeld
    </span>
   </code>
   <span>
    获取此响应，并构建一个包含所有这些安全元数据的内部头部（Header）。
   </span>
  </p>
 </li>
 <li style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <code>
     <span>
      gitrpcd
     </span>
    </code>
   </strong>
   <span>
    – 一个内部RPC服务器。它接收来自
   </span>
   <code>
    <span>
     babeld
    </span>
   </code>
   <span>
    的请求，解析
   </span>
   <code>
    <span>
     X-Stat
    </span>
   </code>
   <span>
    头部，并为下游进程设置环境。关键在于，
   </span>
   <code>
    <span>
     gitrpcd
    </span>
   </code>
   <span>
    自身不执行任何身份验证——它完全信任
   </span>
   <code>
    <span>
     babeld
    </span>
   </code>
   <span>
    ，并将X-Stat头部中的每个字段都视为权威。
   </span>
  </p>
 </li>
 <li style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <span>
     pre-receive（预接收）钩子
    </span>
   </strong>
   <span>
    – 一个编译后的Go二进制文件，在推送被接受前强制执行安全策略。它检查文件大小限制、分支命名规则、LFS完整性，并运行任何管理员定义的自定义钩子。
   </span>
  </p>
 </li>
</ol>
<p>
 <span>
  这些组件之间关键的链接是
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <code>
   <span>
    X-Stat
   </span>
  </code>
  <span>
   头部
  </span>
 </strong>
 <span>
  。它以分号分隔的键值对形式携带安全关键字段。内部服务通过按
 </span>
 <code>
  <span>
   ;
  </span>
 </code>
 <span>
  分割此头部来解析它，并填充到一个映射（Map）中。一个关键细节是：该映射遵循
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   后写入优先（last-write-wins）
  </span>
 </strong>
 <span>
  语义。如果一个键出现两次，后一个值会自动静默覆盖前一个值。
 </span>
</p>
<p>
 <span>
  当
 </span>
 <code>
  <span>
   babeld
  </span>
 </code>
 <span>
  转发推送请求时，其中一个内部请求会在
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中包含
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   推送选项
  </span>
 </strong>
 <span>
  。Git推送选项是用户可以通过
 </span>
 <code>
  <span>
   git push -o
  </span>
 </code>
 <span>
  传递的任意字符串，是Git协议的一个标准功能，旨在为服务器提供提示。
 </span>
 <code>
  <span>
   babeld
  </span>
 </code>
 <span>
  将它们编码为带编号的字段——
 </span>
 <code>
  <span>
   push_option_0
  </span>
 </code>
 <span>
  、
 </span>
 <code>
  <span>
   push_option_1
  </span>
 </code>
 <span>
  等——并附带一个
 </span>
 <code>
  <span>
   push_option_count
  </span>
 </code>
 <span>
  。
 </span>
</p>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjwuYJWyQFaibibRicfe2VItEHPOpDPZB3LUV4NqQSq6UyuUBvlQgdk1spdNAAXWmcAwqwxTDhjCr20RpiaTykQOo1LNbliaibicia7OQc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; height: auto !important; width: 680px !important;" />
 </span>
 <span>
  <br />
 </span>
 <span>
  图示：GitHub内部的git推送管道
 </span>
</p>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   漏洞原理：X-Stat字段注入
  </span>
 </strong>
</h3>
<p>
 <span>
  那么，当用户控制的输入未经适当净化（sanitization）就进入
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部时，会发生什么？
 </span>
</p>
<p>
 <code>
  <span>
   babeld
  </span>
 </code>
 <span>
  将git推送选项的值直接复制到
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中——
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   但是没有对分号进行净化
  </span>
 </strong>
 <span>
  。由于
 </span>
 <code>
  <span>
   ;
  </span>
 </code>
 <span>
  是
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  字段的分隔符，推送选项值中的任何分号都会脱离其指定的字段，并创建新的、由攻击者控制的字段。
 </span>
</p>
<p>
 <span>
  考虑一个包含分号后跟一个安全字段名的推送选项值。
 </span>
 <code>
  <span>
   babeld
  </span>
 </code>
 <span>
  将其按原样嵌入，产生如下头部：
 </span>
</p>
<pre><code><span>X-Stat: ...; large_blob_rejection_enabled=bool:true; ...;</span><span><br /></span><span>  push_option_0=x;large_blob_rejection_enabled=bool:false;</span><span><br /></span><span>  push_option_count=1; ...</span></code></pre>
<p>
 <span>
  当按
 </span>
 <code>
  <span>
   ;
  </span>
 </code>
 <span>
  分割时，该头部解析为：
 </span>
</p>
<pre><code><span>push_option_0                = x</span><span><br /></span><span>large_blob_rejection_enabled = bool:false   ← INJECTED (overrides earlier bool:true)</span><span><br /></span><span>push_option_count            = 1</span></code></pre>
<p>
 <span>
  攻击者的值会“胜出”，因为它出现在头部的更后面——后写入优先。
 </span>
</p>
<p>
 <span>
  该团队通过二进制分析和在线捕获都证实了这一点——在运行的GHES实例上进行的数据包捕获显示，被注入的字段出现在
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中，并与合法的对应字段并存并覆盖了它们。
 </span>
</p>
<p>
 <span>
  通过结合对pre-receive二进制文件的逆向工程和线级分析，他们绘制出了可注入的
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  字段。以下是安全相关性特别高的字段：
 </span>
</p>
<table>
 <thead>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <section>
     <span>
      字段
     </span>
    </section>
   </th>
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <section>
     <span>
      用途
     </span>
    </section>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      rails_env
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      控制钩子执行路径（沙盒执行 vs 直接执行）
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      custom_hooks_dir
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      自定义钩子脚本查找的基目录
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      repo_pre_receive_hooks
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      要执行的预接收钩子的JSON定义
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      large_blob_rejection_enabled
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      强制执行文件大小限制
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      reject_sha_like_refs
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      阻止类似SHA的分支名
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <code>
     <span>
      user_operator_mode
     </span>
    </code>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      启用内部调试输出
     </span>
    </section>
   </td>
  </tr>
 </tbody>
</table>
<p>
 <span>
  前三个字段最为重要——结合起来，它们导致了远程代码执行。
 </span>
</p>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   升级到远程代码执行（RCE）
  </span>
 </strong>
</h3>
<p>
 <span>
  覆盖
 </span>
 <code>
  <span>
   large_blob_rejection_enabled
  </span>
 </code>
 <span>
  这样的安全标志很有趣，但真正的问题是：我们能否将字段注入转化为代码执行？
 </span>
</p>
<p>
 <span>
  答案就在于上表中的三个字段：
 </span>
 <code>
  <span>
   rails_env
  </span>
 </code>
 <span>
  、
 </span>
 <code>
  <span>
   custom_hooks_dir
  </span>
 </code>
 <span>
  和
 </span>
 <code>
  <span>
   repo_pre_receive_hooks
  </span>
 </code>
 <span>
  。要理解原因，我们需要看看pre-receive钩子二进制文件如何处理自定义钩子。
 </span>
</p>
<p>
 <span>
  GHES支持管理员定义的
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   自定义预接收钩子
  </span>
 </strong>
 <span>
  ——在推送被接受前运行的脚本。通过逆向工程pre-receive二进制文件，他们发现它有
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   两种执行路径
  </span>
 </strong>
 <span>
  ，完全由
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中的
 </span>
 <code>
  <span>
   rails_env
  </span>
 </code>
 <span>
  字段控制：一个是生产环境值，在沙盒内运行钩子；另一个是任何其他值，直接运行钩子——没有沙盒，没有隔离——以
 </span>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  服务用户的身份拥有完整的文件系统访问权限。
 </span>
</p>
<p>
 <span>
  区分这两种路径的唯一标准就是
 </span>
 <code>
  <span>
   rails_env
  </span>
 </code>
 <span>
  的值。而这个值可以被注入。
 </span>
</p>
<p>
 <span>
  将漏洞升级为RCE需要链接三个注入步骤：
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   第1步 – 绕过沙盒。
  </span>
 </strong>
 <span>
  注入一个非生产环境的
 </span>
 <code>
  <span>
   rails_env
  </span>
 </code>
 <span>
  值，从沙盒化的生产路径切换到非沙盒路径。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   第2步 – 重定向钩子目录。
  </span>
 </strong>
 <span>
  注入
 </span>
 <code>
  <span>
   custom_hooks_dir
  </span>
 </code>
 <span>
  来控制二进制文件查找钩子脚本的基础目录。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   第3步 – 注入带路径遍历（Path Traversal）的钩子定义。
  </span>
 </strong>
 <span>
  注入
 </span>
 <code>
  <span>
   repo_pre_receive_hooks
  </span>
 </code>
 <span>
  ，其中的script字段包含一个精心构造的路径遍历序列（例如
 </span>
 <code>
  <span>
   ../../../../tmp/payload
  </span>
 </code>
 <span>
  ）。二进制文件的路径解析会将攻击者控制的基目录与遍历有效载荷连接起来，解析为文件系统上的任意二进制文件。
 </span>
</p>
<p>
 <span>
  接着，非生产路径会直接执行解析后的路径——没有参数，没有沙盒——以
 </span>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  服务用户的身份：
 </span>
</p>
<pre><code><span>git push -o '&lt;injected fields&gt;' origin master</span><span><br /></span><span><br /></span><span>Enumerating objects: 3, done.</span><span><br /></span><span>Counting objects: 100% (3/3), done.</span><span><br /></span><span>Writing objects: 100% (3/3), 250 bytes | 250.00 KiB/s, done.</span><span><br /></span><span>Total 3 (delta 0), reused 0 (delta 0), pack-reused 0</span><span><br /></span><span>remote: uid=500(git) gid=500(git) groups=500(git)       ← RCE as the git service user</span><span><br /></span><span>To github.com:user/repo.git</span><span><br /></span><span>   abc1234..def5678  master -&gt; master</span></code></pre>
<p>
 <span>
  以
 </span>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  用户身份获得非沙盒化的代码执行后，攻击者就拥有了对GHES实例的完全控制权，包括文件系统的读写权限和对内部服务配置的可见性。
 </span>
</p>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   从GHES到GitHub.com
  </span>
 </strong>
</h3>
<p>
 <span>
  他们在GitHub Enterprise Server上获得了RCE。下一个问题显而易见——这在GitHub.com上是否也奏效？
 </span>
</p>
<p>
 <span>
  他们对GitHub.com上的一个仓库运行了相同的利用链。推送成功完成，但自定义钩子从未执行。没有
 </span>
 <code>
  <span>
   remote:
  </span>
 </code>
 <span>
  输出，没有代码执行——什么都没有。
 </span>
</p>
<p>
 <span>
  为了理解发生了什么，他们注入了
 </span>
 <code>
  <span>
   user_operator_mode=bool:true
  </span>
 </code>
 <span>
  以在两个平台上启用调试输出。对比两边的输出，他们注意到GitHub.com缺少了在GHES上出现的某些钩子执行步骤——自定义钩子的代码路径根本没有被触发。
 </span>
</p>
<p>
 <span>
  他们回到二进制文件进行更深入的挖掘。通过进一步的逆向工程，他们识别出
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中的一个布尔标志，它控制服务器是否以企业模式运行。在GHES上，此标志默认为true——因此自定义钩子路径始终处于激活状态。在GitHub.com上，它默认为false，意味着在正常情况下永远不会到达自定义钩子路径。
 </span>
</p>
<p>
 <span>
  由于此标志也通过
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部携带，因此可以通过相同的机制注入。多注入一个字段后，完整的利用链在GitHub.com上就成功了。这次，他们执行了
 </span>
 <code>
  <span>
   hostname
  </span>
 </code>
 <span>
  而不是
 </span>
 <code>
  <span>
   id
  </span>
 </code>
 <span>
  ：
 </span>
</p>
<pre><code><span>Enumerating objects: 3, done.</span><span><br /></span><span>Counting objects: 100% (3/3), done.</span><span><br /></span><span>Writing objects: 100% (3/3), 250 bytes | 250.00 KiB/s, done.</span><span><br /></span><span>Total 3 (delta 0), reused 0 (delta 0), pack-reused 0</span><span><br /></span><span>remote: Operator mode enabled.</span><span><br /></span><span>remote: starting PreReceiveBlobCheck(100.00, 50.00) hook...</span><span><br /></span><span>remote: finished PreReceiveBlobCheck(100.00, 50.00) hook in 0s</span><span><br /></span><span>remote: starting PreReceiveRedirectCheck hook...</span><span><br /></span><span>remote: finished PreReceiveRedirectCheck hook in 0s</span><span><br /></span><span>remote: starting PreReceiveRefsCheck hook...</span><span><br /></span><span>remote: finished PreReceiveRefsCheck hook in 0s</span><span><br /></span><span>remote: starting PreReceiveRefLengthCheck hook...</span><span><br /></span><span>remote: finished PreReceiveRefLengthCheck hook in 0s</span><span><br /></span><span>remote: starting PreReceiveForcePushCheck hook...</span><span><br /></span><span>remote: finished PreReceiveForcePushCheck hook in 0s</span><span><br /></span><span>remote: starting PreReceiveLFSIntegrity hook...</span><span><br /></span><span>remote: finished PreReceiveLFSIntegrity hook in 0s</span><span><br /></span><span>remote: starting PreReceiveCustomHooksCheck hook...</span><span><br /></span><span>remote: ██████████████████████████.github.net            ← inside GitHub.com infrastructure</span><span><br /></span><span>remote: finished PreReceiveCustomHooksCheck hook in 2ms</span><span><br /></span><span>To github.com:user/repo.git</span><span><br /></span><span>   abc1234..def5678  main -&gt; main</span></code></pre>
<p>
 <span>
  GitHub.com上的RCE——确认。
 </span>
</p>
<h3>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   跨租户影响
  </span>
 </strong>
</h3>
<p>
 <span>
  GitHub Enterprise Server上的RCE是一个高危漏洞。在GitHub.com上，由于相同的缺陷和共享的服务基础设施，其影响范围更为广泛。
 </span>
</p>
<p>
 <span>
  GitHub.com是一个多租户平台。属于数百万不同组织和用户的仓库存储在共享的后端基础设施上。当研究团队在GitHub.com上实现代码执行时，他们着陆在以
 </span>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  用户身份运行的共享存储节点上。
 </span>
</p>
<p>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  用户的存在有其原因：它服务于该节点上所有仓库的操作。根据设计，它对托管在该节点上的每个仓库都有广泛的文件系统访问权限。攻陷此用户意味着可以读取节点上的任何仓库，无论其所有者是哪个组织或用户。他们枚举了从两个已攻陷节点可访问的仓库索引条目，在每个节点上都发现了属于其他用户和组织的数百万条条目。
 </span>
</p>
<p>
 <span>
  需要明确的是：该研究团队并未访问其他租户仓库的内容。他们仅使用自己的测试账户验证了跨租户暴露的风险，确认
 </span>
 <code>
  <span>
   git
  </span>
 </code>
 <span>
  用户的文件系统权限确实允许读取节点上的任何仓库。
 </span>
</p>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   结论
  </span>
 </strong>
</h2>
<p>
 <span>
  仅需一条
 </span>
 <code>
  <span>
   git push
  </span>
 </code>
 <span>
  命令，就足以利用GitHub内部协议中的一个缺陷并在后端基础设施上实现代码执行。该漏洞链突显了一种模式，其影响范围远超GitHub本身。当由不同语言编写的多个服务通过共享的内部协议传递数据时，每个服务对该数据所做的假定就成为了一个关键的攻击面。在这个案例中，一个服务假定推送选项值可以安全地按原样嵌入；另一个服务假定
 </span>
 <code>
  <span>
   X-Stat
  </span>
 </code>
 <span>
  头部中的每个字段都是由可信来源设置的；pre-receive钩子假定在生产环境中一个环境变量只能是
 </span>
 <code>
  <span>
   production
  </span>
 </code>
 <span>
  。每一个假定孤立来看都是合理的——但组合在一起就变得危险。
 </span>
</p>
<p>
 <span>
  生产二进制文件中存在非生产代码路径、对钩子脚本缺少路径遍历验证、以及使用基于分隔符的协议而不做输入净化，这些模式出现在许多代码库中。团队鼓励构建多服务架构的开发团队审计用户控制的输入如何在内部协议中流动——尤其是在安全关键配置源自共享数据格式的场景。
 </span>
</p>
<p>
 <span>
  这项研究得益于AI增强的逆向工程工具，特别是IDA MCP，这使得研究团队能够以人工操作难以企及的速度快速分析编译后的二进制文件并重建内部协议。随着这些工具的不断成熟，预计它们将在发现需要深度跨组件分析的漏洞类别中发挥越来越重要的作用。
 </span>
</p>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   负责任的披露时间线
  </span>
 </strong>
</h2>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-04
  </span>
 </strong>
 <span>
  – Wiz研究团队发现X-Stat推送选项注入漏洞。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-04
  </span>
 </strong>
 <span>
  – 在GHES 3.19.1上确认RCE。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-04
  </span>
 </strong>
 <span>
  – Wiz研究团队向GitHub报告该漏洞。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-04
  </span>
 </strong>
 <span>
  – GitHub确认收到报告。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-04
  </span>
 </strong>
 <span>
  – GitHub在GitHub.com上部署修复。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-10
  </span>
 </strong>
 <span>
  – 分配CVE-2026-3854，CVSS评分为8.7。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-03-10
  </span>
 </strong>
 <span>
  – 发布GHES补丁。
 </span>
 <span>
  <br />
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   2026-04-28
  </span>
 </strong>
 <span>
  – 公开披露。
 </span>
</p>
<p>
 <span>
  原文：
  <span style="text-decoration: underline;">
   https://www.wiz.io/blog/github-rce-vulnerability-cve-2026-3854
  </span>
 </span>
</p>
<hr />
<p>
 <span>
  <span style="font-weight: bold;">
   感谢阅读，如果觉得还不错的话，动动手指给个三连吧～
  </span>
 </span>
</p>
<p style="display: none;">
 
 
</p>
