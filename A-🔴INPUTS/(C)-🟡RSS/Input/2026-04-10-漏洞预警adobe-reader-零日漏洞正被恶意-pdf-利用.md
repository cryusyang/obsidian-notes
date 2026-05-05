---
title: "【漏洞预警】Adobe Reader 零日漏洞正被恶意 PDF 利用"
url: "https://mp.weixin.qq.com/s/nvxDC2P-wJxkSm18r5_96w"
source: "骨哥说事"
date: 2026-04-10
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> EXPMON发现一个针对Adobe Reader的高级零日PDF漏洞利用样本，可绕过沙箱调用特权API（如`util.readFileIntoStream()`和`RSS.addFeed()`），实现本地文件读取、系统信息收集及远程数据回传。该样本通过混淆JavaScript触发漏洞，已在最新版Adobe Reader中验证有效，具备后续投递远程代码执行或沙箱逃逸载荷的能力。尽管测试中未获取到第二阶段攻击载荷，其信息窃取能力已构成严重威胁。研究者已紧急公开披露并同步Adobe安全团队，提醒用户高度警惕。

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
<p style="text-align: center; margin-bottom: 0px;">
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="width: 247px !important; height: auto !important;" />
 </span>
</p>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgPC7RsPPpCLr5iaVDKkUot7mfmF46jEBIgS6HP3TY8GLvPaibLPa8KkYf7ibjl7sjUCOcyyrwokH19UMO0iaRRlucrV82FebsEIBw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     摘要
    </span>
   </strong>
  </span>
 </h2>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       EXPMON系统检测到一个针对Adobe Reader用户的高度复杂的PDF漏洞利用。
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       根据我们的分析，该样本属于一个初始漏洞利用程序，具备收集和泄露各类信息的能力，可能后续会结合远程代码执行和沙箱逃逸攻击。
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      它滥用了Adobe Reader中的一个零日/未修补漏洞，从而能够执行特权Acrobat API，并已确认可在Adobe Reader最新版本上正常工作。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       具体来说，它调用了
      </span>
     </span>
     <code>
      <span>
       <span style="font-size: 14px; font-weight: normal;">
        util.readFileIntoStream()
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       API，允许其读取本地系统上（由沙箱化Reader进程可访问的）任意文件。
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      通过这种方式，它可以收集本地系统的广泛信息并窃取本地文件数据。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       调用
      </span>
     </span>
     <code>
      <span>
       <span style="font-size: 14px; font-weight: normal;">
        RSS.addFeed()
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       API主要用于两个目的：向远程服务器发送从本地系统收集的信息，并接收要执行的额外JavaScript代码。
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       这种机制使得威胁行为者能够收集用户信息、窃取本地数据、执行高级“指纹识别”并发动后续攻击。
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      如果目标符合攻击者的条件，攻击者可能会投递额外的漏洞利用程序以实现远程代码执行或沙箱逃逸。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       然而，在我们的测试中，我们未能获取到所说的额外漏洞利用程序——服务器已连接，但未返回响应。
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      这可能由于多种原因——例如，我们的本地测试环境可能未满足攻击者的特定条件。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       尽管如此，这种用于广泛信息收集的零日/未修补能力，以及后续可能的远程代码执行/沙箱逃逸潜力，已足以让安全社区保持高度警惕。
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      这就是为什么我们选择立即发布这些发现，以便用户保持警惕。我们也将把此博客文章与Adobe安全团队分享。
     </span>
    </span>
   </section>
  </li>
 </ul>
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     检测过程
    </span>
   </strong>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   就在几周前的3月26日，有人通过EXPMON提交了一个PDF样本。虽然提交者将其命名为“yummy_adobe_exploit_uwu.pdf”，但它触发了EXPMON的一项先进的"深度检测"功能。可以在此处查看原始提交：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    https://pub.expmon.com/analysis/328131/
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   此样本自3月23日起也在VirusTotal上检出，目前检出率较低，为5/64，可以在此链接找到。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <em style="font-style: italic; color: black;">
   <span>
    注：EXPMON不收集任何有关提交者的信息，因此我们不知道是谁提交了该样本。
   </span>
  </em>
 </p>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgXvtse9u49934f9vjOUQtGxTumN6VjSRribosAZh9l66HfUSpjqxtYB9XeqsbxOBMchL73TaIvdC2YsMNliamY9F6kKOaJ31cQo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 680px !important;" />
 </section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   可以看到，该样本在“
  </span>
  <em style="font-style: italic; color: black;">
   <span>
    winx64(update20250816)_reader(2023.006.20320)[acrobatreader]
   </span>
  </em>
  <span>
   ”环境中被检测为以下状态：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     信息类 - "此PDF可能产生可疑活动，请检查（此为实验性深度检测功能的结果，可能会存在误报，欢迎报告误报）"
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   对于那些不熟悉EXPMON对抗高级零日或未知漏洞利用策略的用户，让我尝试更详细地解释。EXPMON通过三个流程识别“恶意样本”：
  </span>
 </p>
 <ol class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       第一
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      种是系统在界面或通过Web API立即报告威胁。在这个案例/样本中，系统成功地标记该样本为可疑并要求进行人工分析。这是理想且最快的检测方法。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       第二
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      种是管理员（对于EXPMON公共版而言是我）可以在控制器上检查检测日志，或者如果你只是一位分析师，可以检查界面/Web API上显示的指标——即使高级别的检测结果仍标记为“未检测到”。这些日志和指标包含了更细粒度的信息，使分析师能够发现自动化系统可能未立即标记的复杂漏洞利用程序。虽然这种人工审查可能很快，但它确实需要专门的人力和深厚的领域知识。
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px; font-weight: normal;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      寻找真正高级零日或未知漏洞利用程序的
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px; font-weight: normal;">
       最后
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px; font-weight: normal;">
      一种方法是我称之为“大数据分析”的流程。得益于EXPMON系统的架构，我们能够在数百万条日志中进行有意义的大数据分析。在这个过程中，我们可能会发现前两个流程遗漏的异常或威胁，并学习如何改进我们的检测逻辑。这是一种强大的威胁狩猎方式；然而，它涉及大量的人工分析，通常需要很长时间。
     </span>
    </span>
   </section>
  </li>
 </ol>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   此特定样本触发的"深度检测"功能是我专门为Adobe Reader开发的非常先进的检测能力。它旨在应对Acrobat PDF JavaScript引擎的复杂性和灵活性。虽然目前我还不愿完全披露该功能的工作原理（正如公开版本中编辑掉的指标名称所示）——原因显而易见——
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    出于检测目的，这种性质的触发本身就值得进行人工分析。
   </span>
  </strong>
  <span>
   如果你是EXPMON用户并看到以这种方式检测到的样本，你应该进行深入的手动分析并谨慎处理。
  </span>
 </p>
 <h3>
  <span>
   <strong style="font-weight: bold; color: rgb(255, 255, 255);">
    <span>
     样本的手动分析
    </span>
   </strong>
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   最近，我不经常查看EXPMON公共平台收集的日志或对其数据进行大数据分析——我一直在忙于另一个关于"大规模模糊测试Office"的项目。然而，本周，在计划进行一个拖延已久的大数据分析时，这个样本立刻引起了我的注意，因为它触发了Acrobat的"深度检测"功能！因此我决定对这个样本进行一次手动分析，然后很快就遇到了一个"哇哦"的时刻——事实证明这个样本非常高级。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   首先，它尝试在对象9内执行JavaScript；如下方图片所示，JS代码被严重混淆。
  </span>
 </p>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiatx6Zs5UKXfIhnCA2hZvnXbLsv6SJkAptcIibYWibUqdAq7YIHib8znezJ0vuHUEISIYabsAZHskFgAoEK9mcBdibUicdd6MJQbhRA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <span style="font-size: 14px;">
    然后……是的，我使用了人工智能，并快速将代码去混淆，得到类似下面的内容。
   </span>
  </span>
 </figure>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <code>
    <span>
     app.t = app["setTimeOut"](util["stringFromStream"](SOAP["streamDecode"](util["streamFromString"](getField("btn1")["value"]), ("base64"))
    </span>
   </code>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   基本上，上面的代码所做的是对一个名为“btn1”的对象中的字符串进行base64解码，然后将其作为JavaScript运行。查看“btn1”的位置，我们发现它位于对象7中。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiagwwrqZC1qzGBN3wwFclHxxpEHI4EclWhDQ7hO6zLocLiaoicZfQibH4KMJn0NTerQJm5YEPEsgoyte6p5bfZTkEhr5raRKu5UNU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 680px !important;" />
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   然后，我们用base64解码了这个长字符串，结果露出了大量JavaScript代码。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZh9bowOBSAhiaX0ibBZhUPaicviaK9mibIhmQ2Guf1dMxRGnb5ZwibZ3326zeOYTzUeZ2dibMqE62eMSCTYVYBFwbMnFu6yvYVz5efgkM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 680px !important;" />
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   正如上图所示，base64解码后的JavaScript仍然严重混淆。我请人工智能帮我进行JS代码去混淆工作（虽然体验有好有坏——哎），最终，我设法大致理解了清理后的代码。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   以下是基于混淆代码由AI生成的一些可读性强的、清理过的代码块。请注意，根据我的经验，这种AI生成的代码仅能帮助你快速理解恶意代码大致在做什么行为，它与实际可运行的、完全去混淆的JavaScript代码并不相同。请记住这一点。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     开始部分，以特权方式调用
    </span>
   </span>
   <code>
    <span>
     <span style="font-weight: normal;">
      RSS.addFeed()
     </span>
    </span>
   </code>
   <span>
    <span style="font-weight: normal;">
     API。
    </span>
   </span>
  </strong>
 </p>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhRrDlPvjtLkuvb83K8GkSEs4Mxt5cexRbJqiboibBBnnIxMfEco7Mibr72BxmbibMUX9xEYp6VibpiaxPHeQBySQpf0lWnY1c0oFicwE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 680px !important;" />
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZj6YwIcDdbuC7McKqr2lic4rZ3VV7pL9k9nbw7UvfpbNR6psfGiaDZ6fsPmrHOicD3GDXue3KiaR6R9BicYkW0iapqEIUC3M9jd6F3BY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <br />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     调用
    </span>
   </span>
   <code>
    <span>
     <span style="font-weight: normal;">
      RSS.addFeed()
     </span>
    </span>
   </code>
   <span>
    <span style="font-weight: normal;">
     时的URL参数。
    </span>
   </span>
  </strong>
 </p>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjTUE6x0lpez91Kqsaj5IAicQ2jAhlodGUwiaJsewUMHwXsouwP6mmPxrInYpZjUIR4PcBW5a1ctmk0ibe9d7GXJibXZY23R96XJXw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <br />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   请注意，脚本收集来自本地系统的各种信息，包括语言设置、Adobe Reader版本号、确切的OS版本以及PDF文件的本地路径。然后，它将这些数据作为URL的一部分发送到远程服务器。服务器地址是“
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    169.40.2.68:45191
   </span>
  </strong>
  <span>
   ”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   通过调用特权API
  </span>
  <code>
   <span>
    util.readFileIntoStream()
   </span>
  </code>
  <span>
   ，它甚至可以读取本地文件。下面的抽象代码读取ntdll.dll文件中的数据，并从中计算出准确的OS版本号。这对于未来的漏洞利用尤其有用。
  </span>
 </p>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjvQlxjr4GpBnsetbNIcTknAvNj6VttqicSIVZ3Dic16SoPyxDyLnrlMeyImlticc1re3FVWtbrWoAA0BblOLMzmsysx2hibMc0viak/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure>
  <span>
   如果它成功从远程、攻击者控制的服务器（通过
  </span>
  <code>
   <span>
    RSS.addFeed()
   </span>
  </code>
  <span>
   API）获得返回的JavaScript时，它甚至会使用密码学来解密payload，我猜这可能是为了规避基于网络的检测。
  </span>
 </figure>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjakcTDN4iaaACUVhBOVwtBGHwBqnvRUToFMtMHNxnCKfbJFZ8eqmR9Dib2MY2cEPiaJUlokiaLQ9aq3bLiaeowhVCpd3ICLkmpNS9I/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <br />
  </span>
 </figure>
 <h3>
  <span>
   <strong style="font-weight: bold; color: rgb(255, 255, 255);">
    <span>
     测试样本
    </span>
   </strong>
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   根据之前对
  </span>
  <span>
   抽象代码的理解，我们现在可以进行实际测试和分析。请注意，之前的静态分析（借助人工智能）只生成了抽象代码—
  </span>
  <span>
   —虽然这可能帮助你理解大致行为，但实际上，你需要在真实环境中进行一些动态测试来确认任何情况。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   我在Adobe Reader最新版本（26.00121367）上测试了该样本，它仍然有效。因此，我们检测到的能够收集本地信息并发送到远程服务器的初始漏洞利用程序，截至本文撰写时，仍然是一个零日/未修补漏洞。
  </span>
 </p>
</section>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhdlSES3Wl8xATHulWlM1fLYGbyKuSU59WhKue9p6j0O3Gof37RIfmpBzKgTvhicNLZ4Blib8icPVYDhLvibtXklnZ6YfPj4kL49Hg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 680px !important;" />
</section>
<section>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <span style="font-size: 14px;">
    在测试时，攻击者控制的服务器仍在线——如上图所示，它已连接。然而，它并未提供样本中显示的潜在远程代码执行/沙箱逃逸漏洞利用程序。这可能是由于多种因素：例如，攻击者的服务器可能“屏蔽”了我的IP地址，或者可能需要我提供特定的本地信息才能满足服务器的条件。这非常类似于高级指纹识别攻击。
   </span>
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   无论如何，如果有其他人设法弄清楚远程代码执行/沙箱逃逸或额外漏洞利用程序的具体内容，我很感兴趣。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    我甚至更进一步...
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     1. 修改了漏洞利用代码，使其连接到我的服务器。
    </span>
   </span>
  </strong>
  <span>
   <span style="font-weight: normal;">
    当我的服务器返回一行简单的JavaScript代码——
   </span>
  </span>
  <code>
   <span>
    <span style="font-weight: normal;">
     app.alert("inside the JS returned from the server!")
    </span>
   </span>
  </code>
  <span>
   <span style="font-weight: normal;">
    ——它被Adobe Reader客户端成功执行。
   </span>
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     这证实了远程服务器确实具备交付并启动后续远程代码执行或沙箱逃逸漏洞利用程序的能力。
    </span>
   </span>
  </strong>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiacnFJnFzVJJXBXph5jz0jZT0ItM96STBqkDa3MtVmLjNviavtE30TRuYz7PGUjH1d1tTpKHMByXybLd2iawCGvqgicI11diaPfyKM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     2. 修改了代码，让它从system32目录读取一个本地.png文件并发送到我控制的服务器。
    </span>
   </span>
  </strong>
  <span>
   <span style="font-weight: normal;">
    它成功地执行了此任务。
   </span>
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    <span style="font-weight: normal;">
     这证明，即使没有后续的远程代码执行/沙箱逃逸漏洞利用程序，此初始漏洞利用程序也完全能够从本地系统窃取广泛的敏感数据。
    </span>
   </span>
  </strong>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaujTl9lFYE5yiaRhkQia27YLkN2EOcbAT8HErb2T3WP7Tnibl8Vo1ziagE0sKpQSianLO6YFnv5ZmibU6zicAVMmASo15dzABHsF4EoU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" />
  </span>
 </figure>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     结论
    </span>
   </strong>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在此博客文章中，我们分享了EXPMON对一种针对Adobe Reader用户的高度复杂、指纹识别式PDF漏洞利用的检测和分析。此"指纹识别"漏洞利用程序已被证实利用了零日/未修补漏洞，该漏洞可在Adobe Reader最新版本上工作，除了打开PDF文件外不需要任何用户交互。更令人担忧的是，此漏洞利用程序允许威胁行为者不仅收集/窃取本地信息，还可能发起后续的远程代码执行/沙箱逃逸攻击，从而可能导致完全控制受害者的系统。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    在防御方面
   </span>
  </strong>
  <span>
   ，我们将立即将我们的发现通知Adobe安全团队。我们希望他们能尽快修补此次初始攻击中利用的零日漏洞。我们建议Adobe Reader用户在官方补丁可用前，对不受信任方发送的PDF文件保持警惕。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    在检测方面
   </span>
  </strong>
  <span>
   ，如果已经部署了安全产品，你也可以在此样本中包含的攻击者控制IP地址——
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    169.40.2.68:45191
   </span>
  </strong>
  <span>
   ——上进行阻断和监控，但请记住，这不会阻止使用不同基础设施的其他变种。更好的方法是查看所有在User Agent字段中带有"Adobe Synchronizer"字符串的http/https流量。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   如果遇到可疑的PDF样本，可以考虑将其提交到EXPMON公共平台。正如我们所讨论的，EXPMON系统采用了高度先进的"深度检测"功能来对抗像这样的复杂PDF零日漏洞利用程序。如果你看到类似此类的检测，必须格外小心，因为它可能是一个新的变种。EXPMON系统旨在无需任何签名更新即可检测此类变种。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    【[4月8日]更新】
   </span>
  </strong>
  <span>
   @greglesnewich 今天发现了一个新的变种。我已确认此发现，它连接到IP地址
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    188.214.34.20:34123
   </span>
  </strong>
  <span>
   。此样本于2025年11月28日出现在VT上，表明这次0day/APT攻击活动至少已持续了4个月之久。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   原文：
  </span>
  <span>
   https://justhaifei1.blogspot.com/2026/04/expmon-detected-sophisticated-zero-day-adobe-reader.html
  </span>
 </p>
 <span style="font-size: 15px; display: block; text-align: center; margin-top: 50px; color: #999; border-bottom: 1px solid #eee;">
  <span>
   - END -
  </span>
 </span>
</section>
<p style="margin-bottom: 32px; border-width: 0px; border-color: initial; line-height: inherit; vertical-align: baseline; letter-spacing: normal; text-align: left;">
 <strong>
  <span style="font-size: 18px;">
   <span>
    <span style="font-weight: bold;">
     感谢阅读，如果觉得还不错的话，动动手指给个三连吧～
    </span>
   </span>
  </span>
 </strong>
</p>
<p style="display: none;">
 
 
</p>
