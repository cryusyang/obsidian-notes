---
title: "剖析 PlugX 活动：Contebrew 有效载荷分析"
url: "https://mp.weixin.qq.com/s/37Xm9MLB1GytP7YyaLCAsQ"
source: "安全狗的自我修养"
date: 2026-04-17
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文详细分析了一次针对 PlugX 恶意软件的新型攻击活动，重点追踪了名为“Contebrew”的可疑安装文件。该文件通过伪装成 RStudio 下载链接（rstudio-desktop.fr.download[.]it）分发，具有多态性特征——同一 URL 在短时间内提供不同 SHA256 哈希值的变种，表明其具备动态生成与反检测能力。静态分析显示其为 Delphi 编写的 InnoSetup 安装程序，内嵌经 ZLB 压缩的多层 PNG 文件，利用隐写术隐藏恶意载荷，并包含反调试、反虚拟机等规避机制。进一步解析揭示其结构为级联嵌套的 PNG 文件，末层疑似含 MZ 头与 LZMA 压缩数据，指向最终的 PlugX 加载器或执行体。

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
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
   </span>
  </font>
 </font>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
   </span>
  </font>
 </font>
</h2>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 40px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnuiafm6LW3ANh2icIEK2nnBLpAxH2NHV3Hhy5u8kQLhL8VMZxX985AA7fa2hnqnCTVxuO4iafTtK9UQ43cA061N0Pu8w2QFJFECIg/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    最近几周，与 PlugX 相关的攻击活动表现出持续的演变能力，无论是在感染途径还是持久性和逃避机制方面。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这种恶意软件历史上与有针对性的间谍活动有关，至今仍是攻击链中的关键组成部分，经常被整合到多阶段攻击活动中。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    正是在这种背景下，微软发布的一条警报引起了我的注意。在对该事件进行初步分析时，有一个要素尤为突出：下载了一个名为“Contebrew”的文件。虽然这种文件名看似无害，但它通常是一个底层指标，隐藏着恶意载荷或中间加载器，这是现代 PlugX 相关攻击活动的典型特征。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在此，我们将尝试对该文件进行深入分析。我们将逐步介绍调查的各个阶段，从初步检测到高级二进制分析。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在最初的警报中，我们追踪到了下载源。请注意，该链接可能仍然有效，存在风险。
   </span>
  </font>
 </font>
</p>
<blockquote>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     下载网址：
    </span>
   </font>
  </font>
  <br />
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     https://rstudio-desktop.fr.download[.]it
    </span>
   </font>
  </font>
 </p>
</blockquote>
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsmc7IFgicOLcFWWKQmBmWZWL2mxmQ06Nr1eib9GTNRrsYk4CnK8JZ4EvvtiaAYibkgk2SnsmbD3CqW5MAZ5aicVkesqOffc5EDrA3U/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们将URL通过安全环境（在本例中为Flare虚拟机）进行访问。我们成功获取了文件，但文件内容有所不同。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    警报触发后，我们使用以下 SHA256 哈希值检索了该文件：fefc50eeb48503f9b6861cea46fb9c8ef50acbaab39a52d31b9a1d0d538a388c
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    但几个小时后我再次下载时，从同一来源下载的文件却具有不同的哈希值。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    SHA256：
   </span>
  </font>
 </font>
 <br />
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    02801c0bd1457293ae009477c9ad7b7e8b9342b446c86391efb10b4884ac46fd
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    实际上，它差不多在同一时间发布在了VT上（我发誓不是我发的）。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们开始分析吧。
   </span>
  </font>
 </font>
</p>
<blockquote>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     免责声明：本文以分析过程中产生的思路为依据撰写，因此在得出结论之前，某些观点可能存在缺陷或错误。本文旨在分享和展示分析思维的过程。
    </span>
   </font>
  </font>
 </p>
</blockquote>
<section>
 <span>
  <br />
 </span>
</section>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    文件静态分析
   </span>
  </font>
 </font>
</h2>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    为此，让我们在
   </span>
  </font>
 </font>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    SandGuard
   </span>
  </font>
 </font>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    沙箱中运行它
   </span>
  </font>
 </font>
 <br />
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    。这是一个全新的法国沙箱，专注于隐私和深度分析的新方法，真正为恶意软件分析师量身定制。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们分析一下初步结果
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntVUzczsUzCfegVDVnTMqNBpdI2r5iaQMia0icib5jF2Zmr4rCEBYwZ2PicOWst34sFARqlELFAmVBo5cPzDOOPu5FbGEWoo72ovC3g/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    机器学习和病毒库似乎都检测不到它。考虑到该文件看起来是最近生成的，而且是一个安装程序，这也很合理。这只是一条 YARA 规则。我们来仔细看看细节。
   </span>
  </font>
 </font>
 <br />
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    触发这条 YARA 规则的原因是它检测到了：
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>字符串：</span></font></font><br /><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>$c1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"启用执行保护支持" </span></font></font></span><br /><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>$c2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"不设置信息进程" </span></font></font></span><br /><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>$c3</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"虚拟保护Ex" </span></font></font></span><br /><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>$c4</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"设置进程DEPPolicy" </span></font></font></span><br /><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>$c5</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"Zw保护虚拟内存"</span></font></font></span></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们从基础知识开始：语言、编译和属性：
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSggvzMUjOMKphYy9NPXRZspiczkQh7ftNMAfreAuhQicJATOMKHVSJgCetiabuUricWIwlXoHIoSz1KpbZzzx5uSd4UTGibyFHJAw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnudrqwlym8ADmw2sqv8oLdBfPwnyWXgGk2B84w2xria95dADQjCH1IfzDFIAIiasVs59b9lZ96ffPvUnmwrR6rjJiazj198ib1oWks/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们最初的假设得到了证实；它确实是一个用 Delphi 编写的 InnoSetup 安装程序。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    现在让我们来看看我们的文件在注册表项、导入和导出方面使用了哪些内容。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    有一些有趣的 API 调用
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsXMqe9ibgQlCHYfalxVnep5YlhRAKwIwSq2xCrwiaQOD3SKHAhfsA6zGugljUDaNTjcrsyVLibeYMckC2Mia3AOk9Pe8x8NEcL80Q/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvoO2QpDaSRJhmpL46slnf3Iiapk9ormdkm1vGcdpCwFAc4If95hXnHibfTe08WrQDmDrOe9n4WiagHqmYUzNChHnicb8Gh3Se9yR8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    沙箱会列出所有这些调用，以及 .dll 文件和 API 的导入数量。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntntdwgYRf6AMMxicFndBuKJyhF4HDty3ZwXOhzOlHicKtZKgIr6cwjSFmWZXCN1hWy1mmLgM7VVJ7WCFjYUzxcJ6GETia8WEx2OA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnu79EibPEJuODoqapibBhTwq38cLVt7pZibJSeX6BaNlm7VWzIeXMYMZOmqalCxTRYXCZzaC7og5eBWOgZnM6pTucIq8sRYpfwYGI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们还收到所有打给图书馆的敏感电话。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们获取进口信息，包括分类、逃税和投机取巧等情况。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnthvtFVR4QqWEhyANlax2T4ougEq4uHib8hrzORrSjKNqhewXnBnPzsa3pk2iafJFyNVgHaKomM6eln77AiarXbW1RS21y7JY3obQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuIm35s03HkfoBQic93ZYpjYLJma0q9XWW1SZsNJkEGTFc8pjjWw1TaXbPgfYVQwic1aHMVibHiciaqGllXdyFbwJjZMDjfBiamQiaReI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们没有关于这部分的更多信息。正如您所预期的，作为安装程序，您需要上传解压缩后的文件，然后看看情况如何。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt1YjyAqicJfbsKfIsqLUwkpvhxuLpH6BzkLE0ibhsJB7FnzfFH5Vf23pDj4q1wzaHLnIibwiaibuNicsBiaNyYKD1Wziaqben0spm1icN4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    接下来，我们将开始分析代码；我们会打开IDA来查看能发现什么，但在此之前，沙箱会提供一些信息，帮我们完成部分工作。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnu9oCRVIdo1vFjo0L9hX1BhV4AQVbq3PyibpDvuX5VeWT2WiaCQ0b4qv28wuPVCllVQTMc0jqVLNFTT8AWRgXg030C3qC92SbvMI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们注意到该文件似乎使用了 UPX 打包（注意：此评估置信度较低，可能性不大），并且包含反调试、反虚拟机和反沙箱措施的代码。我们稍后会对此进行验证。
   </span>
  </font>
 </font>
 <br />
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    验证后，未发现 UPX 打包的证据。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们甚至找到了疑似文件的开头部分（入口点），其中包含标志元素：
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvo8eeiayAnrEiarDbIRFibtFO6GusPVhPZPH2NEvaQnDYCCjr0r5jUJxP5DoufsnRZYyyubYSS6vOfyZoTkqgCxR4dpHoOseEZD0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    各章节之间似乎存在一些出入，但我稍后会核实。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsdRrWFdhR2UcMkvqSb0m78eC5uU7C9FgVo3O8sQMzuuE1o1DI29ibjaFWh9UmBYIMiaxZSMjsicD6AJPicibo8AxJOR5QO8U282xMg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    让我们分析一下安装程序中找到的字符串提取部分。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvd6UNw41cgJrzU90e63PiaOk48a0drP7Q2wHxDWQ9KiaB12L19fdC83ZSX3mZUZJy7zZfQSNiaqnJS72ia72QiaoTFrgqnIO0Cibjeg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们看到了一个微软的网址；它是清单中列出的网址，所以在这里它并不特别相关。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    既然我们已经了解了这个文件的作用，那么在进行静态分析之前，不妨先用IDA打开它。根据我们目前发现的情况，代码分析可能不会提供太多信息。
   </span>
  </font>
 </font>
</p>
<section>
 <span>
  <br />
 </span>
</section>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    国际发展协会
   </span>
  </font>
 </font>
</h2>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    首先要做的是：找到主函数
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    令人惊讶的是，该文件似乎由 Innova MEDIA 签名，尽管它通常属于 Posit Software。它是否被修改过，以便由 InnoSetup 安装？
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntIv5oc9we4VM2Amibu6CjPHfic7KRMzYXgEPNpFianN1hUBBz0Q3qWnVPceu8bFl6tVNicTmPVEsCIU0CIqKD9SJpibDice0pYcicEj0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    代码证实这是一个 Inno 安装程序。此外，已知 InnoSetup 模块会启动并安装广告软件。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这一点已由初始化函数（此处已翻译）证实。
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>void </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_4A9270 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>()</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> { </span></font></font><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 获取参数总数（在 Delphi 中为 ParamCount）</span></font></font></span><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>int </span></font></font></span><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>paramCount </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>=</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> sub_4A3260(); </span></font></font><br /><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>if</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (paramCount &lt;= </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ) goto end; </span></font></font><br /><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>for</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ( </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>int </span></font></font></span><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>i </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>= </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; i &lt;= paramCount; i++) { </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        WSTR arg; </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        sub_4A32C4(i, &amp;arg);   </span></font></font><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// arg = ParamStr(i) </span></font></font></span><br /><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 检查参数是否以“/SP-”开头</span></font></font></span><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>if</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (!sub_41B984(arg, </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"/SP-"</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> )) { </span></font></font><br /><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 从 arg 的第一个字符开始提取前 10 个字符</span></font></font></span><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>WSTR </span></font></font></span><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub1 </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>=</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> sub_408DB0(arg, </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>10</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ); </span></font></font><br /><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 检查此子参数是否以“/SPAWNWND=”开头</span></font></font></span><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>if</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (!sub_41B984(sub1, </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"/SPAWNWND="</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> )) { </span></font></font><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// Ni /SP- ni /SPAWNWND= → 启用“无飞溅”模式</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>                byte_4B4BDD = </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>continue</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>            } </span></font></font><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 找到 /SPAWNWND= → 继续解析</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        } </span></font></font><br /><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 测试 "/Lang=" </span></font></font></span><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>WSTR </span></font></font></span><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub2 </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>=</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> sub_408DB0(arg, </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>6</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ); </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>if</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (!sub_41B984(sub2, </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"/Lang="</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> )) { </span></font></font><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 提取“/Lang=”之后的值（最多 7 个字符 = 7FFFFFFFh = 无限制）</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>             sub_408DB0(arg, </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0x7FFFFFFF</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , &amp;dword_4BC124); </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>continue</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        } </span></font></font><br /><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 测试“/Password=" </span></font></font></span><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>WSTR </span></font></font></span><span style="color: rgb(63, 110, 116);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub3 </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>=</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> sub_408DB0(arg, </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>10</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ); </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>if</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (!sub_41B984(sub3, </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"/Password="</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> )) { </span></font></font><br /><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>// 提取“/Password=”之后的值</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>            sub_408DB0(arg, </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>11</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0x7FFFFFFF</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , &amp;dword_4BC128); </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>continue</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        } </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>    } </span></font></font><br /><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>end: </span></font></font><br /><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>return</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ; </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>}</span></font></font></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    由于这是一个安装程序，我们将重点关注它。InnoSetup 将其有效载荷存储在资源中或 PE 文件末尾。要提取它，您可以使用解压缩工具或 7-Zip。但是，这些元素可能被阻止。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntiaickey8NbpwtOu1m45YxaZ4gX8sV125CaQvfLwnmg58ib9HJ0BRU4AXmPDicdk0k5CTqvp0k9iaBicmBdJ2INzSribskybNPiaYCkxg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    其中一个文件似乎稍大一些，与其他文件明显不同“[0]”
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    试试吧！
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>熵：</span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>8.0000</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>大小：</span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>5071176</span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>字节</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>魔</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>数</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>（</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>十六进制</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>）：7a6c621a1c012cc389504e470d0a1a0a</span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>魔</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>数</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>（</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>ASCII</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>）：</span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>b'zlb\x1a\x1c\x01,\xc3\x89PNG\r\n\x1a\n'</span></font></font></span></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    好的。以下字节
   </span>
  </font>
 </font>
 <code>
  <span>
   89 50 4E 47 0D 0A 1A 0A
  </span>
 </code>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    是嵌入式 PNG 的魔数——一种经典的隐写术或多语言文件技术。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    熵值为 8.0000 是理论最大值，此时内容要么经过 AES 加密，要么使用高效算法（LZMA max）压缩。在我们的案例中，完美的熵值恰好为 8.0（而非 7.9x），这是由于数据块使用 InnoSetup 的 ZLB 算法压缩而导致的测量误差，并非一定是 AES 加密造成的。这种区别至关重要。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们会检查文件头，以确保它确实是一个 PNG 文件。
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>02 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>03 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>04 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>05 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>06 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>07 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>08 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>09 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F </span></font></font></span><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000000 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>6</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>62 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C C3 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>89 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>50 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>4</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>47 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A zlb... </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>,</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> Ã‰PNG.... </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000010 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>49 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>48 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>44 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>52 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>80 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>80</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>   ....IHDR...€...€ </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000020 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>08 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>02 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>4</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>5</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C F6 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>9</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>73 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>52 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>47</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>   .....L </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>\</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> öœ....sRG </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000030 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>42 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D9 C9 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>09 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>70 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>48 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>59 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>73 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>   B.ÙÉ </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>,</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ⌂....pHYs.. </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000040 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>12 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>74 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>12 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>74 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DE </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>66 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>78 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>69 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>49</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>   .t...t.Þf.x.. </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>,</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> iI </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000050 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>44 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>41 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>54 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>78 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>9</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C E5 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>69 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>23</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B7 B1 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E D0 E8 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>9</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D DATxœå </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>}</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> i </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>{ </span></font></font></span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span><a class="wx_topic_link" href="" style="color: #576B95 !important;">#·±</a>.Ðè </span></font></font></span><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000060 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>9</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B D6 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>91 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>34 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>76 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>3</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>8</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>6 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> CE </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>93</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> FF FF </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>73 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>72 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>3 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E4 ' </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>4</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> v </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>&lt;</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ŽoÎ“..sr </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>?</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ä </span></font></font><br /><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00000070 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>71</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> E2 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> C </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>36 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>6</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>D DC </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>05 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>70 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>5 </span></font></font></span><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>F </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>54</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> B1 </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>31 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>8</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> A qâ。</span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>{ </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>6</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> mÜz.p_T± </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>1 </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>-</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> Š</span></font></font></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    文件 [0] 实际上是一个有效的 PNG 文件，从偏移量 0x08 开始；前 8 个字节（7A 6C 62 1A 1C 01 2C C3）是 PNG 文件前面的自定义 InnoSetup 标头。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    如果你稍微懂一点 Python，你会发现实际上有好几个 PNG 文件。
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>在偏移量0x4833E2</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>MZ </span></font></span></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>(PE)文件；</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x4AD7B1处找到</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>MZ </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>( </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>PE)</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>文件</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x4BC620</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 PNG 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x8</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 PNG 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x2CD5</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 GZIP 文件；</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>在偏移量 0x6555 处找到 GZIP 文件；</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x11EA0处找到 GZIP 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x4549C处找到</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>GZIP 文件；</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x5A482处找到 GZIP 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0x8C498</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 GZIP 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0xB7A5F</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 GZIP 文件；在偏移量</span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>0xC007</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>处找到 GZIP 文件。</span></font></span></font><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    此外还有 ZIP 文件。GZIP 文件很可能是 PNG 文件中压缩的 IDAT 数据块（这是正常现象），或者是安装程序在安装过程中部署的组件。我们将重点关注这两个 PNG 文件。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsm9WcW25ZHYIbbhuADdEYSHPPoazkzibg2D7yRC1ZjkWsMgbfJqyv5EsiascibKia3IcIf2icRpjqBJCwia9JYqG5X33NibFKqmzraWM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    假设结构：
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>有效载荷</span></font></font><span style="color: rgb(155, 112, 63);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>.bin</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> └── </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>[0x08]</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>      PNG1（有效</span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>头部</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>）</span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>    └── </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>[IEND a 0x2CC4]</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>  实际 PNG 的结尾</span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        └── </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>[0x2CD5]</span></font></font></span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>头部</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>InnoSetup "zlb" + PNG2 </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>            └── PNG2（有效</span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>头部</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>）</span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>                └── ... 可能还有其他层级，例如 zip</span></font></font></span></pre>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvt5x2Ww9LlfWFvhTNIne8fFLgNlSCFl5URtrKgqvtWbnsOeU5ic8p3ys8NfhdIMRc4G4D1jlQ41stliblEurodlNfOtyYvx8ibzg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=19" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    结构已确认——PNG 文件以级联方式嵌套，每层之间都有 InnoSetup zlb 头部。最后一个 after_iend2 头部这次有所不同：它后面没有紧跟的 PNG 文件；这可能是最终的有效载荷（至少在其他有效载荷之前）。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们修改一下代码
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvtWkfRJmGorDibWTTxGYI0RZntf2CIbibHD4P6hwzYiczz5szeQuC678zhicI3qjvwVPibWr8ibaGdlq8MR0kHSSXfUjMlKJyUice9vs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=20" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们在 0xBD3 处有一个 MZ，在 0x3C4AAB 处有一个 LZMA。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    然而，位于 0xeb644b0c 的 e_lfanew 无效，因此对于合法的 PE 文件来说过大。它并非真正的 PE 文件头；而是一个在加密或压缩数据中发现的误报 MZ 模式。如果我们修改代码并统计 MZ 的数量，会发现
   </span>
  </font>
 </font>
 <br />
 <strong>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     MZ 的数量为 71。
    </span>
   </font>
  </font>
 </strong>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    因此，任何有效的 PE 文件都无法“确认”内容是否已加密或压缩。我们通过验证
   </span>
  </font>
  <strong>
   <em style="font-style: italic;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      e_lfanew
     </span>
    </font>
   </em>
  </strong>
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    是否指向有效的
   </span>
  </font>
  <strong>
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     PE\x00\x00
    </span>
   </font>
  </strong>
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    签名以及文件大小是否一致
   </span>
  </font>
 </font>
 <br />
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    来验证 MZ 文件。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <strong>
   <em style="font-style: italic;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      0x3C4AAB
     </span>
    </font>
   </em>
  </strong>
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    处的
   </span>
  </font>
 </font>
 <strong>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     LZMA
    </span>
   </font>
  </font>
 </strong>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    是
   </span>
  </font>
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    下一个线索吗？
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    这种方法行不通，因为……我没有得到任何结果，我现在明白了。结构很清晰。我们可以看到 LZMA 标头之前有一个自定义的 InnoSetup 包装器：
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0x3C4A9E : </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>87 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>28 </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7c </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2f </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>→</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>校验</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>和 CRC32</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>概率</span></font></font></span><br /><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0x3C4AA2 : </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>73 </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>7c </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>→</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>字节大小</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>或</span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>标志</span></font></font></span><br /><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>0x3C4AA4 : </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00 </span></font></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>01 </span></font></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>→ </span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>InnoSetup</span></font></span></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>标志</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>0x3C4AA7 : </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>5f </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>d1 </span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>20 </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>a3 </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>→ </span></font></span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>4</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>字节</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>未知数据</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>（填充</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>或</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>IV）</span></font></span><span style="color: rgb(131, 108, 40);"><font dir="auto" style="vertical-align: inherit;"><span>0x3C4AAB : </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>5d </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>... </span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>→</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>头部</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>LZMA从</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>此处</span></font></span><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>开始</span></font></span></font><br /><br /></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    很遗憾，我的所有尝试都失败了，所以我还是回到PNG格式吧。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    它看起来像个洋葱。稍后我们会确认这一点，因为安装程序本身会安装多个安装程序。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsxicwTnIPZJWiavXKicwmJL8TBibdteqL5iczVicEHIwBPwf5eAnRN9xBR1qMFV685mmEUDB8zGgk4elPruicviag7C7Q0OcbdJZWE7qw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=21" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    现在整个结构清晰可见。七个嵌套的 zlb 块构成了一个 InnoSetup 压缩洋葱结构。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    但是，字典大小无效，因为它们太大了。在 i=11 处找到的 0x5d 是数据中的误报，并非实际的 LZMA 头部信息。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    块 0x1 完全不包含任何 0x5d 值，因为它直接指向嵌入的 PNG 文件。因此，我们再次改变方法：不再尝试手动解压缩，而是使用 FlareVM 上提供的 innounp 库，该库原生支持此格式。
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>安装文件已损坏</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>或</span></font></font></span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>由</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>不兼容的版本生成</span></font><font dir="auto" style="vertical-align: inherit;"><span>。或许</span></font></font><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>根本就不是 Inno Setup 安装的。</span></font></font></span><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>（</span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DAA）</span></font></font></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    嗯……这个二进制文件要么是故意被篡改的，要么是使用了修改过的/定制版的InnoSetup。这是一种已知的反分析技术；这可能就是我们在沙箱中检测到的问题所在。
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
    让我们通过访问地址 0x492DAA，在 IDA 中尝试找出原因。
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>loc_492DA2:</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>                              ; 代码交叉引用: sub_492D6C+ </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> D↑j </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>. </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> : </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DA2 mov eax, [ebx] </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>. </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> : </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DA4                  </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>call</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>     sub_490ED0 </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>. </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> : </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DA9 test al, al </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>. </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> : </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> DAB jz       </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>short</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> loc_492D9B </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>. </span></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> : </span></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> DAD mov esi, [ebx] </span></font><font dir="auto" style="vertical-align: inherit;"><span>. </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> : </span></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> DAF                  </span></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><span>xor</span></font></span><font dir="auto" style="vertical-align: inherit;"><span>      edx, edx </span></font><font dir="auto" style="vertical-align: inherit;"><span>. </span></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> : </span></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> DB1 mov eax, esi </span></font><font dir="auto" style="vertical-align: inherit;"><span>. </span></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> : </span></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> DB3                  </span></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>call</span></font></span><font dir="auto" style="vertical-align: inherit;"><span>     sub_490D68 </span></font><font dir="auto" style="vertical-align: inherit;"><span>. </span></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>text</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> : </span></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><span>00492</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> DB8</span></font></font><br /><br /><br /><br /></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们通过访问地址 0x492DAA，在 IDA 中尝试找出原因。
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>int </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_492D6C</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> () </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>{ </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>  while (!(unsigned __int8) </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_490ED0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ()) </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>  { </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>    if ((unsigned __int8)(sub_491318() - </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>2</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ) &lt; </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>3u</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ) </span></font></font><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_492DD0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (); </span></font></font><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_493228</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (); </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>    while (!(unsigned __int8) </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_490ED0</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ()) </span></font></font><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_492F84</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (); </span></font></font><br /><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_490D68</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (); </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>  } </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>  return </span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>sub_490D68</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (); </span></font></font><br /><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>}</span></font></font></span></pre>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntrOAOgzoc9jtNVgiblQmVEqUen91EmvbCSc9gGBQibfciaHTrKhe7TEiawibYwnkRYuqBVylQCpO17OSdo4gHwCU5euWdnwR446weA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=22" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    现在结构很清晰了。这是一个基于 sub_492C90 的自定义流解析器，sub_492C90 是实际的解析引擎，但目前我们缺少一些信息或组件。这表明我们正在处理的是一个后续会部署其他软件包的安装程序，这就是为什么我们在这里找不到任何内容的原因。
   </span>
  </font>
 </font>
</p>
<section>
 <span>
  <br />
 </span>
</section>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    动态分析
   </span>
  </font>
 </font>
</h2>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    接下来，我们将进行动态分析，更深入地了解恶意软件的运行机制。为此，我们将使用公共沙箱，并在我们自己的环境中触发恶意软件。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们先从公共沙箱开始；我将使用 JoeSandbox。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsz2QObBQ9vhGSWpNHM2ZbE2zqvVcspscQiaTHYdccQmROw2jmiaHrZvsQpmibt3YvMojvdIiakSo1c5ib0mruvnn43JD5UWRt3u6tM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=23" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    让我们来详细分析一下树状图的构建过程：
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们先来看一个有趣的方面，它似乎与 PUA（潜在有害应用程序）有关，即下载其他“广告支持”软件的软件。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuDCSgXjH4yGEkIN6hz4VaYRvjuF9GTib2iarkDG58xX8CVLOwBGicaAt2Cp30ngWgCSt6qbiaGlOIAZUCJUChNtw7vEXWa7JcJ0A0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=24" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    我们还可以看到，一旦广告软件安装完毕，它就会打开一个 Chrome 标签页，显示 Download[.]it 下载感谢页面。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnv4ANcw9V5rdgLNDjuDLo635uX8btSt95TSeLc2F0ctvE2lGpvFfVJ4icLCRqaFDObpSjia27licicEOayjrYAmWvXTTtol6I6ZsXI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=25" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt1ibWZLKYRXDjmazzahZfP2P9Z11nGy1L2O159MoiblH7TEu4iahAVcWmaVoUZMoicWbFhE85uGFU04XYcR16w3pEkYgNKLPJUHbg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=26" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    让我们回到包含恶意软件的主目录，分析这些进程。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsjDseD0lzdWhZEogNMwcGPLWrpNjibU8ricIeQQbZnsIQaV39gWibv878mSEEdwREwcmJhcHj3DyvfiboXyVhiaEwWuZYxjgYo6LA0/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=27" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    分析结果似乎指向临时文件；让我们仔细查看一下这些信息。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvfzhmALBCq6AT9Qhib3rNJATQWCl6YDbW2mwNdCs4o3VLic16ib23WMpsyzmDkia3FYfzfm1ysD1fxBMDpNtnurr1cGMgDHfG8z84/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=28" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    好的，我们可以看到安装文件和关于我们广告软件的部分。我们还看到了之前在代码中出现的“/SPAWNWND”命令，这证实它是一个Inno安装文件。仔细观察，我们可以发现似乎已经联系过某个域名——我们来试着找出是哪个域名。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnubpo3gEapZCG5ch0A5Iogx045SzYpbkM61kKZRB10GLOYKjoBqjUaI8jjgsx1BZIE53b6vbCBvo97fgdCjA8laB4dVCRp9bCQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=29" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    Cloudfront 并不相关；我们已经看到了“static.download[it]”——那是源下载域。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    让我们关注域名“ghttp://dl.jalecdn.com/FR/rstudio-desktop[.exe]”
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    如果你在沙盒环境中测试这个URL，你会发现它允许你再次下载该文件。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuaDX6Jwmcu3bjBwqn1cicOelQNBbjy9XcuurjF9qMqoQjWYSUZh2zYTu4butBo9DPaDUrW3niaQbNv45ef3fkNS89vKia1hVjciaA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=30" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    这很奇怪（或者说完全正常，因为它是一个伪造的初始二进制文件）；如果你在执行过程中仔细观察，你会注意到“真正的”可执行文件实际上是在安装过程中下载的。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvHs8IdoEAiaKtWrXdU8PPg195NQMIJgJCMx9dG8t7NFEWnIeoC1T5PFV0zGWyAzqrj8563hcrZXA7BsOXdazibmXD6X3Gb7q4ib8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=31" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    好的，在线沙箱不允许我们进行完整的分析，也无法检查广告软件（在本例中是 Avast 和 McAfee）是否“合法”或是否已被感染，更不允许我们获取下载的软件版本来验证是否是正确的版本。所以现在我们要在自己的环境中完成所有这些工作。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们将同时运行 Wireshark 和 Procmon。没错，这并非最隐蔽的方法，而且很有可能会被标记，但我们目前还没有遇到任何反虚拟机功能，所以无论如何都要试一试。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnswC49bmicIFAQexQgTd0FTm37V8OMVl08QlKyddPDjViauUDUQeOs3iaqYGk60bXk91jzlSlOz1RWDvvjdibrmNnSOys1usg8kdxs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=32" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntu3oRQt1M8Qcibp2R1mvIicvjKx2coHXC8dQHQeNtzvseeoR0mClYA0om9ZM8netylnTRsP2MkPQ3u4ppP5Pcnntdqe1wvMmOwU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=33" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
   </span>
  
 </p>
</figure>
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntgf2ialMzA7mGnbyGfg0mjKLXicryiaQ9yom1ZKVDsBUwWmmuMjrf59CT7FgP1SA2ibbCzQ2cdsofYiblt1xoTRd2FTtiaccnxibuC8Q/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=34" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    安装完成后，我们将停止操作并启动该工具。请注意，必须先安装 R 语言。我们暂时暂停分析，待 R 安装完成后再继续，因为我们假设下载此软件的用户计算机上已经安装了 R 语言。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    安装完成后，我检查 Avast 是否已正确安装，但在 Windows 程序列表中找不到它。然而，两分钟后，我收到一条来自微软的通知：
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnt8iayFRJV9NZvUJSJicSw6zxAfms9AxSMtr8vH8PxBLZ42iaI4vI5NBn9IiakcOJ7wkFibjicDohhBF9Gq7rgjDleckLlicoH4kCaYLM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=35" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    Avast 似乎已经安装好了，无论版本如何，但它在哪里呢？
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnspCt6flrYNNXjEMj7wpDDK3lx9K4KpRExA7iaqaWkogptZ7SicajXRK3GtzuAfryJ6l1ov9AW0ParlALP6kjTXq3loicYCK3oDGE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=36" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: auto !important; height: auto !important;" />
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
    邮件里肯定有，我们稍后会用 Procmon 和 Wireshark 再打开看看。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    但首先，让我们整理一下我们已有的信息，以便收集一些资料。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我在 Wireshark 中运行了一个初始过滤器，以提取某些特定元素：
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>DNS || HTTP || TCP</span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>端口</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>== </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>80</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> || TCP</span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>端口</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>== </span></font></font><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>443</span></font></font></span></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在 DNS 层面上，有几个域名：
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnu4M1CzhWYRcibq3LTdFs3vMAMSrg2o8DMdCuEb9nNGo6gJI8uu2ryg3jD92hVFPlQU629nkOzAkfouCziajH0vFyxeI3IpbgbxE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=37" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    我们还发现我们的
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>静态</span></font></font><span style="color: rgb(155, 112, 63);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>下载</span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>[它]</span></font></font></span></span></pre>
<p>
 <span>
  <br />
 </span>
</p>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuiaoUA6PYR3diaYLDGS8GKYtCeeFWfwFhylxlyBjorruh1ysAwLqpSVpk56bnWla8XWBFBddPQp2Zb6ib755kBVDnhwHSnKic34KQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=38" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 493px; height: auto;" />
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
    多个 HTTP 请求：
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuMzFve7u7ZwuB3yoah958b8jM27l1eibaGZNx4LudoGia5qaFNwuCHfcNU51NDe3L65XfSalX5PA5hTZ3rVPuhFBAa9GJkiaEozc/640?wx_fmt=png&amp;from=appmsg#imgIndex=39" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 314px; height: auto;" />
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
    我们看到对 WPAD 的请求
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuX0CpflXKspWOPrE8PzyFtricoUeNnF4VFxzNNSjR5jzd9hqIsUeiccGic9hcCLa7Hl2nTD7xcmicX4YYQ6mklzwhubicYvicQRosr8/640?wx_fmt=png&amp;from=appmsg#imgIndex=40" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 574px; height: auto;" />
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
    与 Avira 的联系显而易见
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsR3tUF4lXps1pXASIPicXMGqcaC4axde8CH2Wo4Xa3H3818j7KczqpPnmqYU9zGuicxicJSOQgwU9CY4UiblIhaia1L1Mkugiay9hlQ/640?wx_fmt=png&amp;from=appmsg#imgIndex=41" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    最终，我们遇到了一个有趣的话题。
   </span>
  </font>
 </font>
</p>
<pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>leaseweb[ </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>.com</span></font></font></span></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在VT上检查域名时，您会发现很多疑似恶意链接。VT标记的网站主机并不意味着域名本身是恶意的，可能只有特定的IP地址或子域名是恶意的。
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    我们会记住这一点；我们收到了关于“R”项目的需求。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnviaoOHpCTepwRtxDevmTSSXxRJGVKEhZ94ge7krR50JR8RtA1gMPzVeJlomrJk9aMThkjsbc4GU0mBF7TMxyEVoFFKcbKUPhXI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=42" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 394px; height: auto;" />
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
    目前为止没什么特别有趣的地方；我们继续往下看。我们来看看恶意软件的启动过程：
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnviaOlxibWqY93jOGO7Oibt0jIwdP9uBh4PNaPxYR51u2yGHY9miauWBvwyMBOF8TmYxQMYYytP2Bibne1JbqFNvEBtRwCH76dFoiczM/640?wx_fmt=png&amp;from=appmsg#imgIndex=43" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    使用 Procmon，您可以查看进程树。
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuBy4F5Zyb6DLOicHGDA4hQXPcXTvcrSz7yfpu1Kv0GS7940pwMnCA7TUlmo2HSKhKlQS7KJP9wynStUzvxibScpw6rmiauhKQth0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=44" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 586px; height: auto;" />
   </span>
  
 </p>
</figure>
<figure style="margin: 56px auto 0px; clear: both;">
 <p>
  
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuShz4bDnGb4XhcduCGg2QqdoYXcicxYwm20ugTlbQAaibXHqqfLF0S5MeoMSXd01YwXQchm2yzZxvRsIS5L7yxqVzfh9b2duTSQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=45" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 487px; height: auto;" />
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
    很明显，该恶意软件使用“saBSI.exe”和“installer.exe”来安装Avast和McAfee。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuobzPaoeowxRBibwJAZ7TxhZlrP4HNjJdRpd8M85srWooPlQ2iboIGdPfwDxO9JMyDBRBqu8cjhGqHuPmXVozbQloguPXmKb0Wo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=46" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 625px; height: auto;" />
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
    此压缩文件包含我们的安装程序
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvFaFpE9nWTQoznHmNGo3lRHaicuKSQgU8Sia0sX8Jq0VNba8mgicKdEhx4E3JwBW1R2mibhqAtfl7S9KiaBlXEELYpMF1eK3X8W5k0/640?wx_fmt=png&amp;from=appmsg#imgIndex=47" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 650px; height: auto;" />
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
    文件还在，所以我们可以进行分析。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsD4ibBISPGTRUXpuaf2ibU9JGjyQFFYFFJfgAnE95FpOb9T0cncHuEW6JBb4YxBCZqR7UqR3hVfqAJHicOz6dSGiaGjAcONQVgyTk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=48" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    McAfee 已签署：SandGuard 结果在此
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
    <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntQ8HQJvkl7ReoA7w5vErPYB34vNHZ5uGYcb1x1vp8QUbsj5soDxStYr0qJtLzS88CGO5LPnvXZTA1g7WKZ1LCztibnDwrT3Hxw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=49" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    它明显存在于许多广告软件中。
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    但这样做，他向我们展示了“drop”软件显然就是真正的McAfee软件。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我们最终跳到了他再次下载软件的时间线；我们想知道这次的版本是否是真的。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntia5G436RGcmUh1NJjBeCwhSpwZFHknsy6jglReRcY6PgPzsZLAYJ4TA3lWicoGeicouTNDCL53D1DjWuDIfRaAiaRql1TbH7nu9c/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=50" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    当我们查找它时，发现它实际上就在我们的电脑上，所以我们可以检索到它的哈希值 MD5：E308F15D8852DF5C8AD4C261660B74B0
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    在VT上查看后，可以看到它确实是正版软件：
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    同时，我们检索提取过程中使用的临时文件夹。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntV1QWpz52wTXVu0sa1Am7tpVQPXd3D69d336Xss9EYZG9xxDBdR58pojcw0v25NHnSEPW6Td5zo10VrpS6sx3YONFCGRnicXicw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=51" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 634px; height: auto;" />
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
    我们找到了疑似 Avast 软件；经检查，它确实有 Avast 的签名，并且似乎是 Avast 免费杀毒软件安装程序的一部分。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    事实上，这些不就是我们刚才用IDA找到的PNG文件吗？
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    好吧，有一件事让我困惑——实际上是两件事。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    WerFault.exe 在安装过程中以及使用 msEdge.exe 时触发。
   </span>
  </font>
 </font>
</p>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    我似乎无法恢复一个临时文件——你可能会说这很正常，因为它是一个 .temp 文件。
   </span>
  </font>
 </font>
</p>
<pre><span><span style="color: rgb(28, 0, 207);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>C:</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> \Users\Jony\AppData\Local\Temp\</span></font></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>是</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>-A2MOQ.tmp\_isetup\_setup64.tmp</span></font></font></span></pre>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    接下来，我们需要连接到一个 IP 地址。
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnv8cj29YqOmGLGMS3u4dorA6hvjlyquYAxOdGibB1iacHUvPBLtPQz4TxcPVXFibM9uRKia1NK3m3OTJiaAc9Vficbic357kNUiceu4eNQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=52" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 569px; height: auto;" />
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
    当我们检查这个 IP 地址时，我们注意到它与我们之前找到的“Leaseweb”相关联，然后，当我们深入查看时，我们注意到了一些有趣的事情：
   </span>
  </font>
 </font>
</p>
<p>
 <span>
  <br />
 </span>
</p>
<h2>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h2>
<h3>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    病毒总数
   </span>
  </font>
 </font>
</h3>
<p>
 <font dir="auto" style="vertical-align: inherit;">
  <font dir="auto" style="vertical-align: inherit;">
   <span>
    VirusTotalwww.virustotal.com
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
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvk5C13ajglIVAJ7buYribBUo9Uxmay87xVvZO1dcic4YKGx6se1umEDNdPib7ibXickUVXv1mhmg9qOLbOiaictPvtQh4MRtEZ3s2o2s/640?wx_fmt=png&amp;from=appmsg#imgIndex=53" style="vertical-align: middle; background-color: rgb(255, 255, 255); width: 680px; height: auto;" />
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
    我们在日志中找到了一个与之前发现的 URL 非常相似的 URL。
   </span>
  </font>
 </font>
</p>
<ul class="list-paddingleft-1">
 <li>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsYq1YcBYTHGBlg8IFBnHKxzl5iaIUia8ACHLQjxI2uNu3djQSicetuEp5vwYOhV0EFBH8Wcc0AoknRfv41P0WkiaySR69Dgk9HkeM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=5" />
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsYBf9sSedx0cSia94t7u8rMUNQiaHjGsFmC4bzVynMH1XfNTfQkAeJG1UKRyYEy9uibf66yr9LSicbic1mduKyeNgQ9Sy6gchwBhKk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=7" />
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
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=omk5zkfc&amp;tp=webp#imgIndex=5" />
   </section>
  </li>
 </ul>
 <ul class="list-paddingleft-1">
 </ul>
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
</ul>
<p style="display: none;">
 
 
</p>
