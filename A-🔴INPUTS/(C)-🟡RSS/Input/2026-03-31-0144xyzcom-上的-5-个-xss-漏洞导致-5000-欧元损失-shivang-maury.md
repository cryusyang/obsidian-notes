---
title: "0144.xyz.com 上的 5 个 XSS 漏洞导致 5000 欧元损失 — Shivang Maurya"
url: "https://mp.weixin.qq.com/s/axfsM4D-aSnqk1XfOlAobA"
source: "Rsec"
date: 2026-03-31
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文记录了一名安全研究员在2026年初针对XYZ公司开展漏洞赏金计划的实战经历，成功发现并报告了5个反射型XSS漏洞，获得5000欧元奖励。作者详细阐述了三种核心挖掘方法：一是利用Google Dorks定位非标准JS端点，并通过深度URL编码绕过WAF实现XSS；二是通过源码分析发现前端未使用的隐藏参数（如`?mode=`），进而触发未经转义的DOM反射；三是采用“金丝雀字符串+参数模糊测试”策略，结合Burp Suite自动化探测隐藏反射点，批量发现多个XSS漏洞。

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
   类型：XSS
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  新年伊始，我的目标是成功完成一次漏洞赏金猎杀。2026 年 1 月初，我决定将精力集中在 XYZ 公司的基础设施上。在绘制攻击面图并深入研究应用程序逻辑后，我成功地发现了五个反射型跨站脚本（XSS）漏洞，并因此获得了 5000 欧元的赏金。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  以下是我的方法分解以及我如何找到每个漏洞的详细说明。
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
   漏洞 1：谷歌技术达人的力量与 WAF 规避
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我总是喜欢先从寻找非标准端点开始侦察。我没有直接进行主动扫描，而是利用 Google Dorks 来绘制 JavaScript 资源文件图。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  使用搜索词
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   site:xyz.com ext:jsq
  </span>
 </span>
 <span>
  <span style="background-color: rgb(214, 214, 214);">
  </span>
  ，我发现了一个有趣的端点：
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   /bundle/resource/js/main.jsq=
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
  我最初测试了一些标准的 XSS 攻击载荷，例如
  <span style="font-weight: bold;">
  </span>
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   &lt; "&gt; ;
  </span>
 </span>
 <span>
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
  </span>
  ，但应用程序要么阻止了它们，要么直接屏蔽了输入。然而，我注意到，当我使用 URL 编码时，Web 应用防火墙 (WAF) 并没有抛出 403 Forbidden
 </span>
 <span>
  错误。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我改变策略，利用 XSS0r 漏洞，精心构造了一个经过大量 URL 编码的有效载荷，成功绕过了过滤器：
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   有效载荷：
  </span>
 </strong>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>%2</span>2%3e%3c<span>%6</span>9%6d<span>%6</span>7%2f<span>%7</span>3<span>%7</span>2<span>%6</span>3%2f%6f%6e<span>%6</span>5<span>%7</span>2<span>%7</span>2%6f<span>%7</span>2<span>%3d</span>.<span>%3</span>1%7c<span>%6</span>1%6c<span>%6</span>5<span>%7</span>2<span>%7</span>4<span>%6</span>0<span>%3</span>1<span>%6</span>0<span>%2</span>0<span>%6</span>3%6c<span>%6</span>1<span>%7</span>3<span>%7</span>3%3d<span>%6</span>4<span>%3e</span></span></code></pre>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   解码：
  </span>
 </strong>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>"&gt;&lt;img/src/onerror=.1|alert`1` class=d&gt;</span></code></pre>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  有效载荷执行完美。
 </span>
 <strong>
  <span>
   漏洞
   <a class="wx_topic_link" href="" style="color: rgb(87, 107, 149) !important;">
    #1
   </a>
   已修复。
  </span>
 </strong>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   Bug 2：源代码分析与被遗忘的参数
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  接下来，我将目标范围扩大到子域名，最终选定了
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   scl.xyz.com
  </span>
 </span>
 <span>
  。我首先进行了标准的 UI 测试，访问每个页面并记录参数。在注册页面 ( register.aspx
 </span>
 <span>
  ) 上，UI 中唯一可见的参数是
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   ?email=
  </span>
 </span>
 <span>
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
  </span>
  。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  不出所料，这一输入信息得到了很好的保护。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  构建 Web 应用程序会让你了解开发人员可能会在哪些方面偷工减料。通常，前端 UI 中未积极使用的参数在后端清理逻辑中会被完全忽略。我没有就此作罢，而是深入研究了原始源代码，发现了一个未使用的参数：
  <span style="background-color: rgb(214, 214, 214); font-weight: bold;">
   ?mode=
  </span>
  。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <code>
  <span>
   <br />
  </span>
 </code>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <code>
  <span>
   由于它隐藏在标准用户流程之外，我怀疑它可能缺乏适当的验证。我注入了一个简单的有效载荷：
  </span>
 </code>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   有效载荷：
  </span>
 </strong>
</p>
<section>
 <span>
  HTML
 </span>
</section>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>/register.aspx?mode=PasswordReset<span>%2</span>7<span>%22</span>()<span>%2</span>6<span>%2</span>5%3Czzz%3E%3CScRiPt<span>%2</span>0<span>%3Ealert</span>(<span>1234</span>)<span>%3C</span>/ScRiPt<span>%3E</span></span></code></pre>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  应用程序直接将输入内容反映到 DOM 上下文中，而没有转义脚本标签，导致弹出警告框。
 </span>
 <strong>
  <span>
   第二个错误已修复。
  </span>
 </strong>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</p>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   漏洞 3、4 和 5：参数模糊测试和“Shivangdon”金丝雀
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
  对于剩余的漏洞，我主要依靠自动化和参数发现。在测试身份验证门户时，我发现了端点 sessionLogin.xjsp
 </span>
 <span>
  。唯一可见的参数是 login={token}
 </span>
 <span>
  。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我没有着眼于显而易见的因素，而是决定寻找隐藏的因素。我的方法很简单：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    获取网站上所有使用过的参数。
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    将它们附加到目标端点。
   </span>
  </section>
 </li>
 <li>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    注入一个唯一的金丝雀字符串（我使用了 shivangdon
   </span>
   <span>
    ）作为值。
   </span>
  </section>
 </li>
</ul>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  例如：
 </span>
 <code>
  <span>
   sessionLogin.xjsp?{fuzzed_parameter}=shivangdon
  </span>
 </code>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <code>
  <span>
   <br />
  </span>
 </code>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我启动了 Burp Suite Intruder，将我的私有参数字典加载到有效载荷位置，然后让它运行。经过一段时间的分析响应后，我的 canary shivangdon
 </span>
 <span>
  出现在了反射的 HTML 中。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  一旦我知道哪个隐藏参数反映了输入，我就把金丝雀替换成了混淆的 XSS
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   有效载荷：
  </span>
 </strong>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>1</span>%<span>3</span>CWOQGK3%<span>3</span>ETCXTG[!%<span>2</span>B!]%<span>27</span>%<span>22</span>%<span>3</span>C%<span>00</span>!—%<span>00</span>%<span>3</span>E%<span>3</span>C%<span>00</span>Img/Src/<span>On</span>%<span>00</span>Error=(conf%<span>00</span>irm)(<span>1</span>)%<span>3</span>E%<span>3</span>C/WOQGK3%<span>3</span>E</span></code></pre>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  这种参数暴力破解方法被证明非常有效。通过在多个端点上重复此过程，我成功发现了第 3、4 和 5 个 XSS 漏洞。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  我使用的是我自己创建的单词表，如有需要请告知。
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   啊，这是我的第一篇稿子，请告诉我任何错误和建议。
  </span>
 </strong>
</p>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="display: none;">
 
 
</p>
