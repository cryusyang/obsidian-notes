---
title: "Java '幽灵比特位'（Ghost Bits）引发的waf通杀"
url: "https://mp.weixin.qq.com/s/axBKmlxttJTcDtGys9RHcg"
source: "迪哥讲事"
date: 2026-04-29
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 该文章介绍了在 Black Hat Asia 2026 上披露的 Java 生态新型底层安全威胁——“Ghost Bits（幽灵比特位）”，源于 Java 中 char 强制转 byte 时高位截断导致的编码不一致问题。攻击者可利用此缺陷构造绕过 WAF/IDS 的变形 payload，触发 SQL 注入、反序列化 RCE、文件上传、SMTP 注入、HTTP 请求走私等多种高危漏洞，影响 Spring、Tomcat、Jackson、fastjson、GeoServer 等主流组件。文章详细说明了成因、典型攻击场景及已确认受影响的组件，并提供了升级修复建议（如升级 BCEL、Fastjson、HttpClient 等至指定版本）和临时缓解措施（如 Unicode 归一化、禁用危险类型转换等）。

---

<p>
 <span>
  <br />
 </span>
</p>
<h2 class="">
 <span>
  <span>
   正文
  </span>
 </span>
</h2>
<p>
 <span>
  Java 是目前企业级应用中最广泛使用的编程语言之一，其生态内的 Spring、Tomcat、Jackson、fastjson 等框架和组件被全球数以亿计的系统所依赖。2026 年 4 月，在 Black Hat Asia 2026 大会上，安全研究员 Zhihui Chen（1ue）与安全研究员 Xinyu Bai（浅蓝）发表了题为《Cast Attack: A New Threat Posed by Ghost Bits in Java》的研究成果。
 </span>
</p>
<p>
 <span>
  该研究揭示了 Java 生态中一个系统性、长期被忽视的底层编码缺陷——"Ghost Bits（幽灵比特位）"，并证明攻击者可利用该缺陷对 WAF/IDS 等安全设备实现全面绕过，进而触发 SQL 注入、反序列化 RCE、文件上传、SMTP 注入、请求走私等多种高危攻击链。漏洞影响范围覆盖 Java 主流框架与中间件，利用门槛低，建议相关用户高度重视并尽快完成自查修复。
 </span>
</p>
<p>
 <span>
  Ghost Bits/幽灵比特 成因：
 </span>
</p>
<p>
 <span>
  Java 里的 char 是 16 位，但某些代码把它强行转成 8 位 byte 。
 </span>
</p>
<p>
 <span>
  结果造成：高 8 位被悄悄丢掉，只剩低 8 位。 攻击者可以利用这个特性，让安全检查看到“奇怪中文/Unicode”，但底层真正执行时变成危险字符
 </span>
</p>
<p>
 <span>
  比如：
 </span>
</p>
<pre><code><span>陪 = U+966A</span><br style="cursor: pointer;" /><span>低 8 位 = 0x6A</span><br style="cursor: pointer;" /><span>0x6A = ASCII 字符 </span><span style="color: rgb(152, 195, 121); cursor: pointer; line-height: 26px;"><span>'j'</span></span><br style="cursor: pointer;" /></code></pre>
<p>
 <span>
  所以：
 </span>
</p>
<pre><code><span>1.陪sp</span><br style="cursor: pointer;" /></code></pre>
<p>
 <span>
  在某些 Java 处理链里可能会变成：
 </span>
</p>
<pre><code><span>1.jsp</span><br style="cursor: pointer;" /></code></pre>
<p>
 <span>
  WAF / 文件类型检查看到的是：
 </span>
</p>
<pre><code><span>1.陪sp</span><br style="cursor: pointer;" /></code></pre>
<p>
 <span>
  服务器保存时却可能变成：
 </span>
</p>
<pre><code><span>1.jsp</span><br style="cursor: pointer;" /></code></pre>
<h2 class="">
 <span>
  <span>
   受影响组件
  </span>
 </span>
</h2>
<p>
 <span>
  以下组件已被确认受 Ghost Bits 影响：
 </span>
</p>
<section>
 <table style="border-collapse: collapse; cursor: pointer; display: table; text-align: left;">
  <thead>
   <tr style="cursor: pointer;">
    <th>
     <section>
      <span>
       组件
      </span>
     </section>
    </th>
    <th>
     <section>
      <span>
       漏洞类型
      </span>
     </section>
    </th>
   </tr>
  </thead>
  <tbody>
   <tr style="cursor: pointer; color: rgb(63, 63, 63); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Apache Commons BCEL
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       WAF 绕过 / 反序列化 RCE
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(0, 0, 0); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Jackson Databind
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       WAF 绕过 / SQL 注入
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(63, 63, 63); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Fastjson
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       WAF 绕过 / 反序列化 RCE
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(0, 0, 0); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Apache Tomcat
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       文件上传绕过（Webshell）
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(63, 63, 63); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Spring Framework
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       URL 解码绕过 / 路径穿越
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(0, 0, 0); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Jetty
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       URL 解码绕过 / CRLF 注入
      </span>
     </section>
    </td>
   </tr>
   <tr style="cursor: pointer; color: rgb(63, 63, 63); width: auto; height: auto;">
    <td>
     <section>
      <span>
       Undertow
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       URL 解码绕过
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       Vert.x
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       URL 解码绕过
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       Angus Mail
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       SMTP 注入
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       Apache HttpClient ≤ 4.5.9
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       HTTP 请求走私（HTTPCLIENT-1974/1978）
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       ActiveJ
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       HTTP CRLF 注入
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       Lettuce（Redis 客户端）
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       Redis 命令注入
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       Jodd
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       路径穿越
      </span>
     </section>
    </td>
   </tr>
   <tr>
    <td>
     <section>
      <span>
       XMLWriter
      </span>
     </section>
    </td>
    <td>
     <section>
      <span>
       XML 标签注入
      </span>
     </section>
    </td>
   </tr>
  </tbody>
 </table>
</section>
<h2 class="">
 <span>
  <span>
   造成的影响
  </span>
 </span>
</h2>
<p>
 <span>
  WAF/IDS 全面绕过： 攻击者通过 Ghost Bits 变形 Payload 可绕过绝大多数现有基于规则的 WAF 检测，使已有安全防护形同虚设。
 </span>
</p>
<p>
 <span>
  触发多类高危漏洞：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    SQL 注入：Jackson charToHex（ch &amp; 255）截断，SQL 注入 Payload 隐写于 Unicode 字符中，WAF 无告警，后端还原并执行。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    反序列化 RCE：BCEL ClassLoader 解码、fastjson \u/ \x 转义均存在 Ghost Bits，可绕过 WAF 触发反序列化远程代码执行。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    文件上传绕过：Tomcat RFC2231Utility 处理文件名时截断高位，可将 .jsp 伪装为非敏感 Unicode 字符，绕过 WAF 上传 Webshell。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    路径穿越 / 认证绕过：Spring、Jetty、Undertow、Vert.x 等框架 URL 解码路径存在 Ghost Bits，可绕过 WAF 实现目录穿越；Openfire CVE-2023-32315 可借此绕过 WAF 防护直接利用。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    已知高危 CVE WAF 绕过：GeoServer CVE-2024-36401（CVSS 9.8）、Spring4Shell（CVE-2022-22965）等漏洞的现有 WAF 防护均可被 Ghost Bits 变体 Payload 绕过，直接触发 RCE。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    SMTP 注入：Angus Mail 等邮件库存在 Ghost Bits，可将隐写 CRLF 序列还原为换行符，触发 SMTP 注入，实现邮件劫持或业务逻辑绕过（已在 Jira、Confluence 上复现）。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    HTTP 请求走私 / XSS：Apache HttpClient（≤ 4.5.9）、JDK 原生 HttpServer 等组件同样受 Ghost Bits CRLF 影响。
   </span>
  </section>
 </li>
</ul>
<h2 class="">
 <span>
  <span>
   解决修复方案
  </span>
 </span>
</h2>
<p>
 <span>
  请关注上述各受影响组件的官方 Security Advisory，升级至已修复版本。
 </span>
</p>
<p>
 <span>
  重点关注：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    Apache Commons BCEL：升级至 6.12.0 及以上版本 Fastjson：升级至 2.x 系列最新版本
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    Apache HttpClient：升级至 4.5.10 及以上版本，或迁移至 HttpClient 5.x
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    GeoServer：升级至 2.28.3 及以上版本
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    Openfire：升级至 5.0.4 及以上版本
   </span>
  </section>
 </li>
</ul>
<p>
 <span>
  临时缓解方案:
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    WAF 规则：现有基于字符串特征的 WAF 规则对 Ghost Bits 变形 Payload 防护效果有限，建议在解码层面进行语义检测，或引入 Unicode 规范化预处理后再执行规则匹配。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    代码层面：排查自研代码中 (byte)ch、ch &amp; 0xFF、baos.write(ch)、DataOutputStream
    <a class="wx_topic_link" href="" style="color: #576B95 !important;">
     #writeBytes
    </a>
    () 等写法，改为使用 String.getBytes(StandardCharsets.UTF_8) 等明确指定编码的方式。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    输入验证：在输入校验阶段对关键字段（文件名、邮件地址、URL 参数、JSON 键名等）严格过滤非 ASCII 字符或进行 Unicode 归一化（NFC/NFKC）处理。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <section style="cursor: pointer; margin-top: 5px; margin-bottom: 5px; color: rgb(63, 63, 63); font-size: 16px; line-height: 1.8em; letter-spacing: 0.02em; text-align: left; font-weight: normal;">
   <span>
    网络层面：对暴露在公网的 Java 应用服务，在完成代码修复前限制访问来源，降低攻击面。
   </span>
  </section>
 </li>
 <li style="cursor: pointer;">
  <p style="text-align: center;">
   <span>
    如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
   </span>
  </p>
 </li>
</ul>
<p style="text-align: center;">
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
 </span>
</p>
<section>
 <span style="text-align: center; display: inline-block; height: 38px; line-height: 42px; color: rgb(72, 179, 120); background-position: left center; background-size: 63px; margin-top: 38px; font-size: 18px; margin-bottom: 10px;">
  <span>
   往期回顾
  </span>
 </span>
</section>
<h1>
 <span>
  <br />
 </span>
</h1>
<h1>
 <span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247497813&amp;idx=1&amp;sn=c778ad6a4bffd7a0a72a900144ea90ca&amp;scene=21#wechat_redirect" target="_blank">
   如何利用ai辅助挖漏洞
  </a>
 </span>
</h1>
<h1>
 <span>
  <br />
 </span>
</h1>
<h1>
 <span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247497880&amp;idx=1&amp;sn=b9b980464333074216b55ea94c8a743a&amp;scene=21#wechat_redirect" target="_blank">
   如何在移动端抓包-下
  </a>
 </span>
</h1>
<h1>
 <span>
  <br />
 </span>
</h1>
<h1>
 <span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247497491&amp;idx=1&amp;sn=a1b00b9a8a54eb96aa3ba8bf23cb7e28&amp;scene=21#wechat_redirect" target="_blank">
   如何绕过签名校验
  </a>
 </span>
</h1>
<h1>
 <span>
  <br />
 </span>
</h1>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247495880&amp;idx=1&amp;sn=65d42fbff5e198509e55072674ac5283&amp;chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&amp;scene=21#wechat_redirect" target="_blank">
   一款bp神器
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247496898&amp;idx=1&amp;sn=b6088e20a8b4fc9fbd887b900d8c5247&amp;scene=21#wechat_redirect" target="_blank">
   挖掘有回显ssrf的隐藏payload
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247495841&amp;idx=1&amp;sn=bbf477afa30391b8072d23469645d026&amp;chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&amp;scene=21#wechat_redirect" target="_blank">
   ssrf绕过新思路
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247496380&amp;idx=1&amp;sn=78c0c4c67821f5ecbe4f3947b567eeec&amp;chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&amp;scene=21#wechat_redirect" target="_blank">
   一个辅助测试ssrf的工具
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247488819&amp;idx=1&amp;sn=5141f88f3e70b9c97e63a4b68689bf6e&amp;chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&amp;scene=21#wechat_redirect" target="_blank">
   dom-xss精选文章
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247487187&amp;idx=1&amp;sn=622438ee6492e4c639ebd8500384ab2f&amp;chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&amp;scene=21#wechat_redirect" target="_blank">
   年度精选文章
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247487122&amp;idx=1&amp;sn=32459310408d126aa43240673b8b0846&amp;chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&amp;scene=21#wechat_redirect" target="_blank">
   Nuclei权威指南-如何躺赚
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247486973&amp;idx=1&amp;sn=6ec419db11ff93d30aa2fbc04d8dbab6&amp;chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&amp;scene=21#wechat_redirect" target="_blank">
   漏洞赏金猎人系列-如何测试设置功能IV
  </a>
 </span>
</p>
<p>
 <span>
  <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247486764&amp;idx=1&amp;sn=9f78d4c937675d76fb94de20effdeb78&amp;chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&amp;scene=21#wechat_redirect" target="_blank">
   漏洞赏金猎人系列-如何测试注册功能以及相关Tips
  </a>
 </span>
 <span style="display: none; line-height: 0px;">
  <span>
   <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&amp;mid=2247486764&amp;idx=1&amp;sn=9f78d4c937675d76fb94de20effdeb78&amp;chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&amp;scene=21#wechat_redirect" target="_blank">
    ‍
   </a>
  </span>
 </span>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<p style="text-align: center;">
 <span>
  <br />
 </span>
</p>
<h2 class="">
 <span>
  <span>
   参考
  </span>
 </span>
</h2>
<p>
 <span>
  1.Black Hat Asia 2026 议题：Cast Attack: A New Threat Posed by Ghost Bits in Java  作者：Xinyu Bai（@b1u3r / @iSafeBlue）、Zhihui Chen（@1ue1166323）、贡献者 Zongzheng Zheng（@chun_springX）
 </span>
</p>
<p>
 <span>
  2.https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv
 </span>
</p>
<p>
 <span>
  3.https://github.com/advisories/GHSA-gw42-f939-fhvm
 </span>
</p>
<p>
 <span>
  4.https://spring.io/security/cve-2022-22965
 </span>
</p>
<section>
 <span>
  <br />
 </span>
</section>
<section style="margin-bottom: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="display: none;">
 
 
</p>
