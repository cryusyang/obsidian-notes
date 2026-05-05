---
title: "0149.HackerOne 报道的真实 SSRF 案例（涉及 IPv6 和重定向）"
url: "https://mp.weixin.qq.com/s/NVmjDqL0v-wRX-LIkH1y4w"
source: "Rsec"
date: 2026-04-17
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文披露了一个结合IPv6地址编码与HTTP重定向滥用的SSRF漏洞案例，发生在Webhook功能中。尽管目标应用对IPv4内网地址（如127.0.0.1）进行了严格过滤，但其未识别IPv6格式的等价表示（如[::ffff:7f00:1]），导致绕过失败。攻击者利用服务自动跟随重定向且不重新校验目标地址的缺陷，成功发起SSRF，进而手动探测出多个内部开放端口（如5000、8090、8126等），暴露调试接口与管理面板。该漏洞凸显了安全过滤机制因覆盖不全而失效的风险，而非逻辑本身存在明显缺陷。

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
   类型：重定向+SSRF
  </span>
 </span>
</section>
<section style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <font>
  <font>
   <font>
    <span>
     在网络安全领域，即使是像 Webhook 这样看似无害的功能也可能隐藏着严重的漏洞。本文将深入探讨一个在 Webhook 实现中发现的
    </span>
    <strong>
     <span>
      服务器端请求伪造 (SSRF)
     </span>
    </strong>
    <span>
     漏洞。这个案例的特别之处在于，只有将
    </span>
    <strong>
     <span>
      IPv6
     </span>
    </strong>
    <span>
     行为与
    </span>
    <strong>
     <span>
      重定向
     </span>
    </strong>
    <span>
     技巧结合起来才能利用该漏洞。以下是
    </span>
    <em>
     <span>
      我
     </span>
    </em>
    <span>
     和我的好友 madara_ 如何发现并利用此漏洞的技术解析。
    </span>
   </font>
  </font>
 </font>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <font>
  <font>
   <font>
    <span>
     <br />
    </span>
   </font>
  </font>
 </font>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  在现代应用中，像 Webhook 这样的功能随处可见。它们能够实现自动化、集成和实时工作流程。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
 
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuuJepCT7bCPXgSy8M66iaP56GxFr8DepgP0IpJSHz3JSib1Jq0JjaFkQ2IFUjNzTiaiczvVdGGBJVtDmuCn0oQIyLjbZbs8d3CnXicA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
  </span>
 
</p>
<figcaption style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</figcaption>
<p>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
</p>
<figcaption style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</figcaption>
<p>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  但它们也带来了一些危险的东西：
 </span>
</p>
<blockquote>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  <strong>
   <em>
    <span>
     <span style="font-weight: bold;">
      您允许您的服务器代表用户发出请求。
     </span>
    </span>
   </em>
  </strong>
 </p>
</blockquote>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  而这正是问题开始出现的地方。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  这是一个看似“安全”的 webhook 实现如何导致
 </span>
 <strong>
  <span>
   服务器端请求伪造 (SSRF)
  </span>
 </strong>
 <span>
  的故事，该攻击结合了
 </span>
 <strong>
  <span>
   IPv6 编码
  </span>
 </strong>
 <span>
  和
 </span>
 <strong>
  <span>
   重定向滥用
  </span>
 </strong>
 <span>
  。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span>
   <br />
  </span>
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
 
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89Buv90YialkePeGDaMQESsJViahsia9BqPHfxo3PnTu6rPpCzWDQJHgOUyeiaDWe2icE6xcXLzbL30MqRXibbJsOVB2PUlSic0ianLMKBRrU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
  </span>
 
</p>
<p>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <strong>
  <span>
   <span style="font-weight: bold;">
    首先，什么是 SSRF（快速解释）……
   </span>
  </span>
 </strong>
 <br />
 <span>
  服务器端请求伪造是指攻击者诱骗服务器向非预期目标发送请求，例如：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    内部服务（ 127.0.0.1
   </span>
   <span>
    ）
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    私有 API
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    云元数据端点
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    管理界面
   </span>
  </section>
 </li>
</ul>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  你不用直接攻击，而是让服务器为你完成攻击。
 </span>
</p>
<h3 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   入口点：Webhook 功能
  </span>
 </span>
</h3>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  在 HackerOne 上测试目标时，我们发现了一个 webhook 功能。这没什么不寻常的。直到我们注意到：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    它接受用户控制的 URL
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    它触发了服务器端请求
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    它设有一些过滤装置。
   </span>
  </section>
 </li>
</ul>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  乍一看，它似乎很坚硬。
 </span>
</p>
<h3 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   初始行为
  </span>
 </span>
</h3>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  该应用程序具有保护措施：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    屏蔽十进制格式的内部 IP 地址（例如 127.0.0.1
   </span>
   <span>
    ）
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    过滤常见的 SSRF 有效载荷
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    允许重定向，但仍以十进制格式阻止内部 IP 地址
   </span>
  </section>
 </li>
</ul>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  所以……没有直接的 SSRF 攻击。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  但接下来我们重点测试一些简单的东西：
 </span>
 <strong>
  <span>
   重定向。
  </span>
 </strong>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span>
   <br />
  </span>
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
 
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButS9sBAfP2Fg39tKFRWxqbUY1ec9nVbZ57FZmhKSVG0Bd8m8mNpVvV3uB4Yjvy06JUYhGnmjl0RskLkoGBk0PmRjM9dQicuJ1KU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
  </span>
 
</p>
<p>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  我们发现后端会自动跟随重定向，但没有重新验证目标地址，这是一个典型的错误，因此我们没有直接访问内部资源，而是尝试了以下方法：
 </span>
 <br />
 <em>
  <span>
   http://attacker.com
  </span>
 </em>
 <span>
  → 重定向 → 内部资源（十进制） → 仍然被阻止。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButZhmheRqmTQCMCYP5I16vcRAib8kQrADEkAFUVL8StnWm6gdKsDlNicVjf64W2A0FL3vON0ZcYyytfibF8YzG1Dagta3RLzFdCj4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 665px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  于是我们深入探究。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<h3 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   突破：IP 表示技巧
  </span>
 </span>
</h3>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  过滤器通常会阻止这种行为：127.0.0.1
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  但别忘了，同一个 IP 地址可以有不同的写法。[::ffff:7f00:1]
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 
  <span>
   <br />
  </span>
 
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  这本质上是将 IPv4 编码为 IPv6……而过滤器呢？没能拦截下来。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuuqdDUdiaCm1AnRddr8KNrvGoibicCB2FfydOKH5Yjuy8ce4ZGW6DJicSOl1esr2oYCo1HJG17cuXj2JjuKfyMQh2UJMgJ4XMSCQYI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 315.984375px !important; height: auto !important;" />
   </span>
  
 </p>
 <figcaption style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <br />
  </span>
 </figcaption>
</figure>
<figure>
 <figcaption style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <br />
  </span>
 </figcaption>
</figure>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  这是我们用来检查漏洞是否存在的重定向文件。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<pre style="margin-top: 0px; margin-bottom: 0px;"><span></span></pre>
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
 </ul>
 <pre class="code-snippet__js"><code><span><span>&lt;?php</span></span></code><code><span><span>header</span>(<span>"Access-Control-Allow-Origin: *"</span>);</span></code><code><span><span>header</span>(<span>"Access-Control-Allow-Methods: GET, POST, PUT, DELETE"</span>);</span></code><code><span><span>header</span>(<span>"Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept"</span>);</span></code><code><span><span>header</span>(<span>"Content-Type: application/json"</span>);</span></code><code><span><span>header</span>(<span>"Location: http://[::ffff:a9fe:a9fe]"</span>);</span></code><code><span><span>?&gt;</span></span></code></pre>
</section>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <span>
    <br />
   </span>
  </span>
 </p>
 <p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusdZDoUwdribDBDsHkGibZex8u3oLCuR6KzdqfDOKIKCdTceHLCicQkBG03VqL3SGuz3UibJqCicEKeHT9fYo45mLXFcSGXiclWAbeGY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
 <figcaption style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <br />
  </span>
 </figcaption>
</figure>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  当我们意识到我们已经掌握了内部基础设施的入口后，下一步显然就是：端口扫描，但系统另有打算。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  webhook 的响应极其不稳定……到处都是延迟，没有可靠的时间安排，也没有清晰的信号。端口开放、端口关闭……一切看起来都一样。自动化完全不起作用。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  所以我们做出了调整。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  我们没有依赖工具，而是采取了手动方式；缓慢、谨慎、专注。我们开始逐个探测常用端口，寻找任何异常行为。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  虽然速度不快，但奏效了。
 </span>
</p>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <span>
    <br />
   </span>
  </span>
 </p>
 <p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89But4A2X5CTWPkMLY4ScxZSicALooZ2UsXBFrw2TQVT2ZYMSIVicldia4nCM1edvZdjicuv9Kvs89tnh4jUv463wXzkKahcdKTibn1nec/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <strong>
  <span>
   发现开放端口：
  </span>
 </strong>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    5000
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    5012
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    8090
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    8126
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    24220
   </span>
  </section>
 </li>
</ul>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  接下来就更有意思了。内部服务通常会暴露以下问题：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    调试端点
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    管理面板
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    内部 API
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    指标体系
   </span>
  </section>
 </li>
</ul>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <span>
    <br />
   </span>
  </span>
 </p>
 <p style="margin-top: 0px; margin-bottom: 0px; text-align: center;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusB8zEDEkmK0QkBMs9icmMhdCdboRZsC1ia6NwOdJ0qjRGSBD4n6qPde7OEJ0Y2MIXoGt6iaUqBCPv8CX0zHrIMpOL8Lm6NwckchA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<figure>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  <span>
   <span>
    <br />
   </span>
  </span>
 </p>
 <p style="margin-top: 0px; margin-bottom: 0px;">
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvnXKGIsroGMWpSZB1dfP52kH7np5azdVOiaXfOZSMMS6YV4Y87aMxLqHXdkRqUW47VAHhvdjfEGhoicfFzaHKnbXK5QWwj8s1vs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  在此过程中，我们还发现，即使在重定向之后，仍然可以使用八进制和 IPv6 等替代 IP 表示形式来绕过过滤机制。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  为了简化攻击过程，我们最终使用了如下的有效载荷：
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>https</span>://ourserver/h1/redirector.php?url=http://[::ffff:<span>7</span>f00:<span>1</span>]:§<span>5000</span>§</span></code></pre>
</section>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <code>
  <span>
   <br />
  </span>
 </code>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  这个漏洞并非旨在破坏系统，而是旨在让系统比它自身更了解自身。过滤器失效并非因为其自身存在缺陷，而是因为其本身并不完整。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<h2 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   时间线
  </span>
 </span>
</h2>
<ul class="list-paddingleft-1">
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    2024年1月2日——报告已提交
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1月3日——“需要更多信息”
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1月8日——分诊
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1月9日——“请不要再升级事态了……”😅
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1月10日——严重程度降低
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1月16日——悬赏2500美元
   </span>
  </section>
 </li>
 <li>
  <section style="margin-top: 0px; margin-bottom: 0px;">
   <span>
    1 月 30 日——披露[点击
   </span>
   <em>
    <span>
     此处
    </span>
   </em>
   <span>
    查看报告]
   </span>
  </section>
 </li>
</ul>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <font>
  <font>
   <font>
    <span>
     点击
    </span>
    <em>
     <span>
      此处
     </span>
    </em>
    <span>
     查看更多关于 SSRF 绕过技术的详细幻灯片。
    </span>
   </font>
  </font>
 </font>
</p>
<h2 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</h2>
<h2 style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   鸣谢
  </span>
 </span>
</h2>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  特别感谢
 </span>
 <strong>
  <span>
   madara_ 的
  </span>
 </strong>
 <span>
  合作。
 </span>
</p>
<p style="margin-top: 0px; margin-bottom: 0px;">
 <span>
  记住，关键从来不仅仅在于漏洞本身，而在于你能把它推向多远。
 </span>
</p>
<p style="display: none;">
 
 
</p>
