---
title: "0148.我的第一份 HackerOne 审核通过的报告：在 5 个目标中发现暴露的 Weglot API 密钥"
url: "https://mp.weixin.qq.com/s/9q-BW-wVXEeWqNxJNMy2uw"
source: "Rsec"
date: 2026-04-16
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文讲述了作者在HackerOne平台上首次被接受的漏洞报告经历：通过源码和JS文件中以“wg_”开头的线索，发现多个网站意外暴露Weglot翻译服务API密钥。作者利用Wappalyzer等工具批量识别使用Weglot的目标，并在5个有赏金计划的网站上复现该问题。文章强调了模式识别、智能侦察和负责任披露的重要性，指出此类密钥泄露可能导致未授权使用、资源滥用及高额账单等风险。

---

<section>
 <span>
  <span style="font-weight: bold;">
   本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。
  </span>
 </span>
 <span>
  <br />
 </span>
</section>
<section>
 <span>
  <span style="font-weight: bold;">
   声明：本文搬运自互联网，如你是原作者，请联系我们！
  </span>
 </span>
</section>
<section>
 <span>
  <span style="font-weight: bold;">
   类型：
  </span>
 </span>
 <span>
  <span style="font-weight: bold;">
   密钥泄露
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<figure>
 <p style="margin-bottom: 0px; margin-top: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvMajg38otT04pZ4P4ibW1GM5O0AAXneY8lfkcE1AhUX63VDeMCYB5qFqaQyWLlX2EBW8uia6mJ73cADfYkgiaKZXQicInxTnmYNvA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 280px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  各位晚上好。这篇文章是关于我
 </span>
 <strong>
  <span>
   在 HackerOne 上收到的第一份报告
  </span>
 </strong>
 <span>
  ，以及我是如何在
 </span>
 <strong>
  <span>
   5 个不同的目标
  </span>
 </strong>
 <span>
  上发现同一个问题的。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  今天我们来聊聊
 </span>
 <strong>
  <span>
   Weglot API 密钥
  </span>
 </strong>
 <span>
  。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   Weglot 是什么？
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  Weglot 是一款付费翻译服务，被许多网站用于提供多语言内容。它通过 API 处理翻译请求。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   我是如何发现它的
  </span>
 </span>
</h2>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  在测试网站时，我检查了
 </span>
 <strong>
  <span>
   页面源代码
  </span>
 </strong>
 <span>
  和 JavaScript 文件。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  一个常见的指标是按以下方式开头的键或变量
  <span style="font-weight: bold;">
   ：wg_
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  有时这些值直接出现在 HTML 源代码中，有时出现在链接的
 </span>
 <code>
  <span>
   .js
  </span>
 </code>
 <span>
  文件中。
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h2>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-weight: bold;">
   快速侦察方法
  </span>
 </span>
</h2>
<ol class="list-paddingleft-1">
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    打开目标网站
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    查看页面源代码
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    搜索：
   </span>
   <code>
    <span>
     weglot
    </span>
   </code>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    搜索以
   </span>
   <code>
    <span>
     wg_ 开头的键
    </span>
   </code>
  </section>
 </li>
</ol>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <code>
  <span>
   <br />
  </span>
 </code>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  如果发现暴露的 API 密钥，请测试其是否仍然有效。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   概念验证请求
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我使用如下的翻译请求测试了密钥：
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
 </ul>
 <pre class="code-snippet__js"><code><span>curl -X POST \</span></code><code><span><span>'https://api.weglot.com/translate?api_key=wg_*******' \</span></span></code><code><span>-H 'Content-Type: application/json' \</span></code><code><span>-d '{</span></code><code><span>  <span>"l_from"</span>:<span>"en"</span>,</span></code><code><span>  <span>"l_to"</span>:<span>"fr"</span>,</span></code><code><span>  <span>"request_url"</span>:<span>"https://www.google.com/"</span>,</span></code><code><span>  <span>"words"</span>:[</span></code><code><span>    {<span>"w"</span>:<span>"This is a blue car"</span>,<span>"t"</span>:1},</span></code><code><span>    {<span>"w"</span>:<span>"This is a black car"</span>,<span>"t"</span>:1}</span></code><code><span>  ]</span></code><code><span>}'</span></code></pre>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  如果 API 成功返回翻译后的内容，则该密钥处于激活状态并可用。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   为什么这很重要
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  泄露的第三方 API 密钥可能导致：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    未经授权使用付费服务
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    资源滥用
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    意外的账单费用
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    失去对外部整合的控制
   </span>
  </section>
 </li>
</ul>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我的第一份被 HackerOne 接受的报告
 </span>
</h2>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我已将此问题提交给 HackerOne，并且已被接受。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 
  <span>
   <br />
  </span>
 
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  那使它成为我旅途中最令人难忘的发现之一。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   我如何在 5 个不同的 Target 网站上找到它
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  在了解了这种模式之后，我扩大了研究规模。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我使用了诸如以下技术指纹识别平台：
 </span>
</p>
<ul class="list-paddingleft-1">
</ul>
<ul class="list-paddingleft-1">
 <li>
  <section>
   <span>
    Wappalyzer
   </span>
  </section>
 </li>
 <li>
  <section>
   <span>
    BuiltWith
   </span>
  </section>
 </li>
 <li>
  <section>
   <span>
    PublicWWW
   </span>
  </section>
  <section>
   <span>
    <br />
   </span>
  </section>
 </li>
</ul>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  这些平台帮助我使用 Weglot 识别网站。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  然后我筛选出那些有公开漏洞赏金计划的目标，并负责任地对它们进行了测试。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   关键
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  有时，一项小小的发现可能会衍生出多份有效的报告，例如：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    了解根本原因
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    识别可重用的模式
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    以合乎道德的方式扩大规模
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    保持在范围内
   </span>
  </section>
 </li>
</ul>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h2>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   最后想说的话
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  这对我来说是一个重要的里程碑，因为它表明智能侦察和模式识别比随机测试更有价值。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  始终负责任地进行测试，并遵守每个程序的规则。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<section>
 
 
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="display: none;">
 
 
</p>
