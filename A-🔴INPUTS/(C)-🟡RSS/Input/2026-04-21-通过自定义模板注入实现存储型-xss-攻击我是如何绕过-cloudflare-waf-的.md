---
title: "通过自定义模板注入实现存储型 XSS 攻击——我是如何绕过 Cloudflare WAF 的"
url: "https://mp.weixin.qq.com/s/-PPCkmq7tMx3pJHRezbN6Q"
source: "安全狗的自我修养"
date: 2026-04-21
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章描述了一次针对电商平台的渗透测试，发现其自定义模板引擎（使用%%…%%语法）存在存储型XSS漏洞。该漏洞因Cloudflare WAF缺乏对专有模板语法的检测规则而被成功绕过。攻击者注入的模板表达式虽未在输入位置直接执行，却在用户名称显示的多个上下文（如个人资料、好友列表、支持工单等）中被客户端渲染并执行JavaScript，造成广泛影响。案例凸显了专有实现对标准化安全防护（如WAF）的规避风险，以及客户端模板注入（CSTI）演变为高危存储型XSS的攻击路径。

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
 <strong>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     <br />
    </span>
   </font>
  </font>
 </strong>
</p>
<p>
 <span>
 </span>
</p>
<p>
 
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnu1Aog7X5icUOJ4OyvVXO0FzAGNjkdvJCncEGILVszYRn7FJYvVibkzLqPkxlg1EHtBs2eZxCGPst06ms7MrZeIpCYvyBJNKYv9o/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
  </span>
 
</p>
<p>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在测试一个电商平台时，我发现了一个存储型 XSS 漏洞，攻击者通过自定义模板注入
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    完全绕过了 Cloudflare WAF 的保护。更有趣的是，攻击载荷并没有
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在我注入的位置执行，而是悄无声息地渲染到了完全不同的其他地方。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    问：什么是模板注入？
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    答：模板注入是指将用户输入嵌入到模板引擎中，并将其作为代码执行，而不是
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    作为纯文本处理。根据引擎和上下文的不同，这可能导致信息泄露、跨站脚本攻击 (XSS)，甚至远程代码执行
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    ——
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    侦察——模糊处理一切
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    测试开始时一切如常。我正在测试一个电商网站应用——那种包含
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    客服聊天、用户个人资料、好友列表和产品评论等功能的平台。我决定用一个经典的多语言有效载荷对应用中的每个输入字段进行模糊测试
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    ：
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>#^&lt;&amp;'"-</span></font></font></span></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    大多数字段都没有返回任何有用的信息，只有一些普通的、经过处理的响应或通用错误。但当我输入
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    地址字段时，却得到了意想不到的结果。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    应用程序没有对我的输入进行清理或拒绝，而是泄露了一个原始模板渲染错误：
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% 错误 %</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> % </span></font></font><span><br /></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% getCurrentAddress.billing_name %</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> % </span></font></font><span><br /></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% getCurrentAddress.billing_address | decode_htmlentities %</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> % </span></font></font><span><br /></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% getCurrentAddress.billing_country | decode_htmlentities %</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> % </span></font></font><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>+ </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% parseFloat(getVatRate(getCurrentCountryCode)) + '% </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>' </span></font></font><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>%% 增值税%%</span></font></font></span></span></pre>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsz3ZoHVibHibaNSc3icScvBIyEq3mxENanwDdUWGJfEPNyCeD7DC0xdOBTzS33MXajiaak7FrqK56euiax4QTPFWVicVYFM0XeuhbgA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 371px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这下可有意思了。这个应用程序泄露了内部模板语法、变量名，甚至还有辅助
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    函数。我立刻注意到了 %% … %% 分隔符——这肯定不是 Jinja2、Twig、Mako 或任何已知的模板
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    引擎。这是一个自定义的专有模板引擎。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    墙——Cloudflare WAF
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我知道该应用程序位于 Cloudflare WAF 之后，因此我意识到标准的 SSTI 有效负载永远无法通过：
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    {{7*7}} ← 已屏蔽
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    ${7*7} ← 已屏蔽
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    &lt;%= 7*7 %&gt; ← 已屏蔽
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    但问题在于——WAF（Web应用防火墙）只能检测已知的模板语法模式。它们不知道%%..%%是什么意思，因为它不在
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    它们的规则手册中。所以我决定用应用程序自身的语法来测试它。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我在应用程序的每个输入字段（姓名、地址、个人简介、评论字段）中注入了 %%7*7%%，
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    每个字段一个有效负载。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    请求已发送。已检查响应。无响应。没有 49 号错误。没有执行。什么都没有。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我尝试了各种方法，不同的字段，不同的端点，但仍然不行。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    啊……😤
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我整整尝试了两天，但毫无进展。我确信模板引擎根本没有解析用户
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    输入，我看到的错误只是一个调试漏洞，根本没有真正的利用途径。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我放弃了。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    突破——它一直都在那里
   </span>
  </font>
 </font>
</p>
<p>
 
  <span>
   <br />
  </span>
 
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    两天后，我因为其他问题提交了一个支持工单。就在那时，我看到了它。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我的显示名称显示为 49。
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  <span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      按回车键或点击查看完整尺寸的图片
     </span>
    </font>
   </font>
  </span>
 </p>
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntZ63llWdIby07e0MBLFh5XDXMvXMSCE2qibJkeQOUzwPcFdlnTvRTByvlGm0icc6YFiaKHTHwPzTmLibBqsAObibsQpeUXNLV0ia1ico/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    等等，什么？
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我赶紧跑到设置页面查看——名称字段里仍然存储着 %%7*7%%。模板引擎执行了
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    7*7=49。注入确实有效。只是它没有在我注入的地方渲染——而是在一个完全不同的上下文中渲染了
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    名称字段在每次显示时（例如在支持工单、好友
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    列表和用户个人资料中）都会通过模板引擎进行评估。我一直都在错误的地方寻找输出结果。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    自定义的 %%..%% 语法完全绕过了 Cloudflare，因为 WAF 没有规则来检测它。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    升级——从SSTI到XSS
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    现在我知道注射是真的了。是时候升级行动了。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我注射了：
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>％％</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>自己</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>％％</span></font></font></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    输出结果：
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>[</span></font></font><span style="color: rgb(100, 56, 32);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>对象窗口</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>]</span></font></font></span></pre>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  <span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      按回车键或点击查看完整尺寸的图片
     </span>
    </font>
   </font>
  </span>
 </p>
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsYR6pr3HPe7H1SVPybGHLE2N46icWH1ZBb6pmicia0prg641r7WBe719eKzia3e7krjuTd41AA80gycUCtuaP35xdhro4tvoXuhgQ/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这证实了我拥有对 JavaScript 全局作用域的访问权限。模板引擎在客户端执行表达式
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    ——这就是客户端模板注入 (CSTI)，这意味着我有可能利用 XSS 漏洞。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    最终有效载荷：
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    %% alert('XSS') %%
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  <span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      按回车键或点击查看完整尺寸的图片
     </span>
    </font>
   </font>
  </span>
 </p>
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntNVUmAdMnWsSQORZZmlojsSKibHZlTG7hicGLCeQR0uDcn14gRSOKCG7rD39jV8GiaS6wkNibE7MlPk2qcDp39KxTibYwicbBlpZQ4A/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    轰隆隆！💥
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    JavaScript 执行成功。无论我的名字出现在何处，都会弹出 alert() 提示——而出现的地方非常多。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    影响——存储型 XSS 无处不在
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这不仅仅是一个自XSS攻击，而是一个影响多个高影响力表面的存储型XSS攻击：
   </span>
  </font>
 </font>
</p>
<ul class="list-paddingleft-1" style="margin: 0px; padding: 0px;">
 <li>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     用户个人资料页面——任何访问您个人资料页面的人都会触发恶意代码
    </span>
   </font>
  </font>
  <section>
   <span>
    <br />
   </span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      ——好友列表——添加好友会在其个人资料页面上执行恶意代码
     </span>
    </font>
   </font>
   <span>
    <br />
   </span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      ——支持工单——支持人员查看工单会触发恶意代码执行
     </span>
    </font>
   </font>
   <span>
    <br />
   </span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      ——产品页面评论——产品评论/评价部分也存在同样的漏洞
     </span>
    </font>
   </font>
  </section>
 </li>
</ul>
<section>
 <span>
  <br />
 </span>
</section>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  <span>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      按回车键或点击查看完整尺寸的图片
     </span>
    </font>
   </font>
  </span>
 </p>
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntlXMY5Xz11wXfSSneWfKWZibdpcgqqR99PHdHKOADxFNaibxaC5V0mXA9wkPSic7p9XlExa4WVpCNMW1EhUhBRZdNhtVZYiaYIWhw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
 <figcaption>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     💸💸
    </span>
   </font>
  </font>
 </figcaption>
</figure>
<p>
 <span>
  <br />
 </span>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    为什么 Cloudflare 没能发现这个问题：
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    Cloudflare WAF 使用基于签名的检测方法来识别已知的模板语法（{{, ${, &lt;%)）。自定义的 %%..%% 分隔符
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    与任何现有的 WAF 规则都不匹配。这是一个典型的例子，说明了为什么专有实现往往
   </span>
  </font>
 </font>
 <span>
  <br />
 </span>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    会破坏标准化的安全控制。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    <br />
   </span>
  </font>
 </font>
</p>
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
<h2 class="js_darkmode__29">
 <strong>
 </strong>
</h2>
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
<section>
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsZKK1qXJ3b15N1JJwMqU3QltJTclwGDibnxx7YIoelgDFRt6ia0WYnpBuZCMQuhs3iapict1ykzNzCCnytLkAHWp1o1ibyGSywZ3icg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=5" />
</section>
<section>
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvQtmL2d0ibA4461cWoTggghMOYhxa1sb8Eh8Qf1VlzSNqsodfFibTk2wwrRlqZdwia09gLhyrELIHmK4ibAsicKEH7XGwiaUGP2NKPU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=7" />
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
 <strong>
 </strong>
</p>
<ul class="list-paddingleft-1">
 <ul class="list-paddingleft-1">
  <li>
   <section>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=omk5zkfc&amp;tp=webp#imgIndex=5" />
   </section>
  </li>
 </ul>
</ul>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    <br />
   </span>
  </font>
 </font>
</p>
<p style="display: none;">
 
 
</p>
