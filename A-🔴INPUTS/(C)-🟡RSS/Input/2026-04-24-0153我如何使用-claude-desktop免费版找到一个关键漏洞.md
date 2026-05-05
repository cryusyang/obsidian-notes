---
title: "0153.我如何使用 Claude Desktop（免费版）找到一个关键漏洞"
url: "https://mp.weixin.qq.com/s/KU4eE8a6XRPr9LMCMvJuAw"
source: "Rsec"
date: 2026-04-24
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文讲述了一位安全研究员利用Claude AI分析压缩的JavaScript代码，意外发现多个高危漏洞的过程。AI虽未直接识别漏洞，但快速解析出隐藏API端点、参数结构并生成有效请求，帮助研究员发现了未经授权的可预测用户ID（IDOR），进而暴露知名用户的敏感财务信息。进一步测试揭示该接口还存在严重写入缺陷：允许攻击者任意重定向资金、劫持邮箱和篡改账户余额。根本原因在于缺乏服务端授权校验、使用连续整数ID及危险的批量参数赋值机制。作者强调AI是高效“第二双眼睛”，能突破人工疲劳导致的盲区，大幅提升漏洞挖掘效率。

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
   类型：JS信息泄露
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
 <section>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     简而言之：
    </span>
   </strong>
   <span>
    我把一个 JavaScript 代码包导入到
   </span>
   <strong>
    <span>
     Claude Desktop
    </span>
   </strong>
   <span>
    （我用 Burp MCP 搭配 Claude）中。它发现了一些我多次检查后仍然遗漏的隐藏端点。这一个提示让我深入挖掘：可预测的用户 ID 泄露了知名人士的个人身份信息，写入操作允许资金重定向、邮箱劫持和余额操纵。人工智能虽然没找到漏洞本身，但它给了我一盏指路明灯。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <em>
    <span>
     有趣的是：我之前多次检查过这个 JavaScript 文件，却始终没发现其中的漏洞。直到我把代码输入到
    </span>
   </em>
   <strong>
    <em>
     <span>
      Claude
     </span>
    </em>
   </strong>
   <em>
    <span>
     中，它才解析出端点结构，并帮助我构建了一个有效的请求。人工智能本身并没有发现漏洞，但它给了我所需的视角，让我看到了一直隐藏在眼前的漏洞。
    </span>
   </em>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <em>
    <span>
     <br />
    </span>
   </em>
  </p>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 20px; font-weight: bold;">
     目标
    </span>
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    这是一个为健身公司打造的私有漏洞赏金计划。用户包括名人、运动员和公司高管。该平台负责会员管理、赏金发放和合作伙伴计划——真金白银通过真实的 API 接口流动。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    程序名称将予以隐去。你懂的。
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
     第一步：让人工智能读取我看不见的东西
    </span>
   </span>
  </h2>
 </section>
 <section>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    我坚信应该手动阅读 JavaScript 代码。自动扫描器固然好用，但它们不会
   </span>
   <em>
    <span>
     思考
    </span>
   </em>
   <span>
    。问题是？有时候我自己也不会思考——至少在第三次盯着同一个压缩包看之后是这样。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    所以我尝试了不同的方法。我把 JS 文件拖到 Claude 里，让它分析代码，枚举 API 端点，构建请求，并找出任何有趣的东西。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    几秒钟之内，它就返回了一个结构化的分解结果：端点路径、HTTP 方法、参数模式，甚至还为我构建了一个有效的
   </span>
   <code>
    <span>
     POST
    </span>
   </code>
   <span>
    请求，以测试一个与财务功能相关的特别重要的路由。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    我之前明明已经看过这段代码好几遍了，却还是没发现。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <figure>
   <p style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <br />
    </span>
   </p>
   <p style="margin-bottom: 0px; margin-top: 0px;">
    
     <span>
      <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvxJDhy8lyq9zuL7HFftkibD69RYg3fVKyALGo5d6gttrXmsOx473Gia7CFRuFu8zRicNN3e4VCSR2rEqBJeJD2f6z8mGwIP8YGjw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
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
    经验教训：
   </span>
   <strong>
    <span>
     有时候，第二双眼睛并不一定非得是人。
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
     第二步：IDOR——“等等，那不是我的账户”
    </span>
   </span>
  </h2>
 </section>
 <section>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    有了人工智能生成的请求，我用自己的账户 ID（一个简单的数字值）访问了目标端点。得到的响应非常慷慨：
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
   </ul>
   <pre class="code-snippet__js"><code><span>→ Full name</span></code><code><span>→ Email </span></code><code><span><span>address</span></span></code><code><span>→ Bank account identifier</span></code><code><span>→ Account balance</span></code><code><span>→ Internal account status</span></code></pre>
  </section>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   
    <span>
     <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuscwHeC9ZsQa3wSY2P9LJ7CFUJkZul6F0PYFTbXsH3HJYRGXeYCID4HCj7efYiclKX5Px1bMecRDO9J3Jukfx2ZNGBcKZVcv5yM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
    </span>
   
  </p>
  <p>
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    好的。现在我只需把那个 ID 改成 1……
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    相同的数据，不同的人。没有授权检查。服务器不在乎是
   </span>
   <em>
    <span>
     谁
    </span>
   </em>
   <span>
    在请求，只在乎提供了
   </span>
   <em>
    <span>
     什么
    </span>
   </em>
   <span>
    ID。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    我不断增加请求次数。每一次请求都返回了包含财务详情的完整资料。而且我看到的这些账户？这些并非测试用户。这些都是
   </span>
   <strong>
    <span>
     知名人士
    </span>
   </strong>
   <span>
    ——那种数据泄露会成为头条新闻的人物。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <figure>
   <p style="margin-bottom: 0px; margin-top: 0px; text-align: center;">
    
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButOUkgty51Irh5WqLThSpTT1vkicMxycv1Wl1ueORNOQKSYu1RmFT5COfJaApVtd0Fw5OSaIQCn7sh2MwfqAvqFqNX3cbmJsgHk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 482.984375px !important; height: auto !important;" />
     </span>
    
   </p>
  </figure>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 20px; font-weight: bold;">
     第三步：“我也可以写吗？”——剧透：可以
    </span>
   </span>
  </h2>
 </section>
 <section>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    当你泄露公众人物的银行信息时，只读 IDOR 就已经至关重要了。但我想要的是完整的信息。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    我再次使用人工智能助手，这次请它帮我理解该接口接受哪些可修改的参数。它根据 JS 源代码帮我映射出了可写字段。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    然后我测试了三件事：
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   
    <span>
     <br />
    </span>
   
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     资金重定向
    </span>
   </strong>
   <span>
    ——我修改了银行账户参数。服务器接受了修改。这样一来，款项就可以重定向到任何账户。我的账户、你的账户，任何人的账户。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     电子邮件劫持
    </span>
   </strong>
   <span>
    ——篡改目标账户的电子邮件地址。现在，只需触发密码重置，在你的收件箱中截获邮件，即可控制该账户。这种攻击手法经典、危害巨大，但完全可以预防。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     余额操作
    </span>
   </strong>
   <span>
    ——这一点连我都感到惊讶。余额字段是可写的。我可以把它设为零，也可以设为一百万。服务器每次都回复“好的，没问题”。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px; text-align: center;">
   
    <span>
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusMauGeWapdn3155bzlrAQpRDl7icf677brt4g4aRF6IfPpiaqTCs78eZrclfehPh9oRjfobyOcmebq3N5FlO3icvzc981u3bibFCc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px !important; height: auto !important;" />
    </span>
   
  </p>
  <p>
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    挖掘链
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
   </ul>
   <pre class="code-snippet__js"><code><span>借助人工智能辅助阅读 JavaScript → 发现隐藏的端点 + 正确的请求结构</span></code><code><span>↓</span></code><code><span>发送带有顺序编号的 POST 请求 → 获取任何用户的完整个人识别信息</span></code><code><span>↓</span></code><code><span>列举 ID → 大规模数据泄露</span></code><code><span>↓</span></code><code><span>修改银行账户 → 重新分配资金</span></code><code><span>修改电子邮件 → 账户被冒用</span></code><code><span>修改余额 → 财务欺诈</span></code></pre>
  </section>
  <p>
   <span>
    <br />
   </span>
  </p>
  <pre style="margin-bottom: 0px; margin-top: 0px;"><span><span>一个 JavaScript 文件。一次 AI 对话。完全妥协。</span></span></pre>
  <pre style="margin-bottom: 0px; margin-top: 0px;"><span><span><br /></span></span></pre>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 20px; font-weight: bold;">
     为什么会发生这种情况
    </span>
   </span>
  </h2>
 </section>
 <section>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    三个经典的失败案例叠加在一起：
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-weight: bold;">
      无需授权
     </span>
     。API
    </span>
   </strong>
   <span>
    信任客户端只会请求自身的数据。剧透一下：攻击者可不会遵守这种信任机制。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-weight: bold;">
      可预测的 ID
     </span>
     。
    </span>
   </strong>
   <span>
    使用连续整数作为用户标识符。枚举操作就像使用
   </span>
   <code>
    <span>
     for
    </span>
   </code>
   <span>
    循环一样简单。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-weight: bold;">
      批量赋值。
     </span>
    </span>
   </strong>
   <span>
    该 API 允许客户端写入本不应由客户端控制的字段——例如银行账户、电子邮件和余额。没有允许列表，没有验证，也没有针对敏感更改的单独工作流程。
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
     人工智能因素
    </span>
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    我想坦诚地说明这一点，因为我认为这对社区很重要。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    人工智能并没有“入侵”任何东西。它既没有利用漏洞，也没有将其标记为安全问题。它所做的
   </span>
   <strong>
    <span>
     ，只是比我第四次遍历压缩后的 JavaScript 代码，更快、更系统地处理了信息。
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
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    它列举了所有端点，按 HTTP 方法进行分类，识别了参数结构，并为我构建了一个可用的请求。这种繁琐的工作通常需要花一个小时眯着眼睛研究晦涩难懂的代码才能完成——而现在只需几秒钟就能搞定。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    漏洞发现、测试写入权限的直觉、权限提升策略——这些都出自人类的判断。但最初的出发点呢？却来自一个人工智能对一段我早已放弃的代码的解读。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     如果你的侦察工作流程中没有使用人工智能，你就等于放弃了很多漏洞。就我而言，那是一个价值四位数的漏洞。
    </span>
   </strong>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <figure>
   <p style="margin-bottom: 0px; margin-top: 0px;">
    
     <span>
      <img src="https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuuZdVhSqCa9OKNU8rLYicxR4fj5Rz0VpxsGa3LBlIbzdO5SyQjArBadMeAkSxx18fdKEwhfSFZoCoqdGOX8oubGRoe212TN4Zng/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 642.984375px !important; height: auto !important;" />
     </span>
    
   </p>
  </figure>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <h2 style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 20px; font-weight: bold;">
     最后想说的话
    </span>
   </span>
  </h2>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    仔细阅读 JavaScript 代码，深入研究目标代码。如果你已经读过，那就把它交给 AI 再读一遍。bug 不会藏在你没看过的代码里，它们就藏在你已经看过却忽略的代码里。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    之后我肯定购买了 Claude Pro 订阅。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    当你发现读取漏洞时，一定要检查是否存在写入漏洞。这才是漏洞严重程度从“有趣”跃升至“决定漏洞赏金之旅的关键”的关键所在。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    祝你狩猎愉快。
   </span>
  </p>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <br />
   </span>
  </p>
  <span>
   <span style="font-size: 17px; font-weight: normal;">
    如果您觉得这篇文章有用，
   </span>
  </span>
  <span>
   <span>
    <span style="font-size: 17px; font-weight: normal;">
     请点个赞👍
    </span>
   </span>
  </span>
 </section>
 <section>
  <span>
   <span>
    <br />
   </span>
  </span>
 </section>
 <p style="margin-bottom: 0px; margin-top: 0px;">
  <span>
   <br />
  </span>
 </p>
</section>
<section>
 
 
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="display: none;">
 
 
</p>
