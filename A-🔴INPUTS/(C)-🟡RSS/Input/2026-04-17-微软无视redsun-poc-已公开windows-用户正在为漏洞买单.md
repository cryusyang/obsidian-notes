---
title: "微软无视，RedSun PoC 已公开（Windows 用户正在为漏洞买单？！）"
url: "https://mp.weixin.qq.com/s/bPvnEjx9SGvQt7ro1EIMmw"
source: "骨哥说事"
date: 2026-04-17
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章披露了安全研究员在微软未及时响应漏洞报告后，连续公开三个针对Microsoft Defender的高危漏洞（BlueHammer、UnDefend、RedSun），其中RedSun尤为严重：它利用Defender自身的“云端判断”与文件恢复机制，诱使其以SYSTEM权限将恶意程序写入C:\Windows\System32目录，实现无感知提权。该漏洞影响Windows 10/11及部分Server版本，且暂无官方补丁。事件暴露出安全软件高权限特性带来的“信任反噬”风险，并引发对厂商-研究员漏洞披露机制有效性的深层质疑。

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
 <span style="letter-spacing: 0.544px;">
 </span>
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
 <span style="letter-spacing: 0.544px;">
 </span>
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
<section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你可能听过这句话：
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    "不要相信任何杀毒软件。"
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但你听过**"杀毒软件亲手把木马写进系统目录"**吗？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这件事，就发生在昨天。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <span style="background-color: rgb(255, 251, 0); color: rgb(255, 41, 65); font-weight: bold;">
    PoC 见文末链接。
   </span>
  </span>
 </p>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <span>
    一封被无视的报告
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   故事得从一封漏洞报告说起。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   一位安全研究员发现了 Microsoft Defender（也就是Windows自带杀毒软件）存在严重漏洞。按照行业惯例，他先把问题私下提交给了微软安全响应中心（MSRC），希望能和平解决。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   毕竟，这种漏洞如果被恶意利用，后果不堪设想。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    但微软没理他。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   具体原因我们不清楚。是判定为"非漏洞"？是优先级不够？还是单纯漏掉了？没人知道。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   唯一知道的是：
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    沉默的时间有点长。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   研究员的耐心被消耗殆尽。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   于是，他直接——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    把漏洞直接公开，而且一个接一个。
   </span>
  </strong>
 </p>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <span>
    13天，3个漏洞，杀伤力递增
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这件事的时间线大概是这样的：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    4月初，BlueHammer 登场。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Defender 本地提权漏洞，能让普通程序拿到 SYSTEM 权限。后来拿到了自己的 CVE 编号（CVE-2026-33825），微软随后修复。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    4月中，UnDefend 登场。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这次更狠——直接破坏 Defender 的更新机制，让它彻底无法升级，等于阉割掉整个防护系统。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    4月15日，RedSun 登场。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   最新，
   <span style="font-weight: bold;">
    也是最炸裂的一个。
   </span>
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    RedSun 到底干了什么？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   先说原理，不讲技术细节，只说逻辑：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Defender 有个"云端判断"机制。当它扫描到一个可疑文件时，会给文件打上"cloud tag"（云标签）。随后为了某种恢复逻辑，Defender 可能会尝试把文件"恢复"到它的原始路径。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    攻击者就利用了这个机制。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   他们精心设计了一个场景：
  </span>
 </p>
 <ol class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     构造一个带有云标签的恶意文件
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     利用 Windows 的文件锁竞争（Oplock）、目录重定向（Junction）等特性
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     当 Defender 试图"恢复"文件时，把它误导到
    </span>
    <code>
     <span>
      C:\Windows\System32
     </span>
    </code>
    <span>
     目录
    </span>
   </section>
  </li>
 </ol>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    然后，攻击发生了。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Defender 作为系统最高权限进程，亲手把恶意程序写进了系统目录。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   恶意程序随即以 SYSTEM 身份运行——这意味着它拥有 Windows 的最高权限。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你可以把它理解为：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    保安队长亲自给小偷开的门，还顺便帮他换上了正式工牌。🚪
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   讽刺吗？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   太讽刺了。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    受影响范围有多大？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   根据目前公开的信息：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     Windows 10
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     Windows 11
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     Windows Server（部分版本）
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    而且即便是安装了 2026 年 4 月补丁的系统，依然可以中招。
   </span>
  </strong>
 </p>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgGf54ao0e9Jd7FaYyaJ3eQdEicOauGRmYGd8PtcqeYMXeXZc63p5XY6SdxSUKWcVdv4l0YUR2hy4iaTUqEoWlrrDAgMUxRz3ONc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 660px !important;" />
 </section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这意味着什么？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   目前没有现成的修复方案。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    普通用户会遭遇什么？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   让我们把场景说得具体一点——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    如果 RedSun 被恶意软件利用，会发生什么？
   </span>
  </strong>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第一步：普通用户先运行了恶意程序
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这一步没有捷径，你得自己"打开"那个来路不明的 EXE 文件。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第二步：RedSun 帮攻击者完成提权
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   不需要你输入密码，不需要弹 UAC 确认窗，不需要任何额外操作。攻击者直接拿到 SYSTEM 权限。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第三步：后果自负
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   拿到 SYSTEM 之后，攻击者理论上可以：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    🔓 偷走你浏览器里保存的所有密码
   </span>
  </p>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    🍪 导出你的 Cookie，会话直接劫持
   </span>
  </p>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    💬 抓取 Discord Token、VPN 凭证、企业登录票据
   </span>
  </p>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    💣 勒索软件登场：删卷影副本、加密全盘文件、禁用安全工具
   </span>
  </p>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    🌐 企业内网：横向移动，Kerberos 票据伪造，域管理员权限拿下
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   整个攻击链，从"用户运行恶意程序"到"机器完全沦陷"，可能只需要几分钟。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    而且用户很可能毫不知情。
   </span>
  </strong>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    为什么是 3 个漏洞，而不是 1 个？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这才是这件事最值得玩味的地方。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   BlueHammer → UnDefend → RedSun
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   13 天，3 个针对 Defender 的漏洞依次公开。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这不像是"一时冲动"，更像是"系统性清算"。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   研究员用行动回答了一个问题：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     如果厂商不及时修复，我就一个接一个爆，直到你重视为止。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   当然，这种做法争议很大。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   有人认为"公开披露逼厂商修复"是合理的，有人认为"连续释放 3 个漏洞利用"太过激进了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    但无论如何，这件事撕开了一个问题：厂商与独立研究员之间的漏洞披露机制，是否真的健康运转？
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   一个可能影响数亿用户的漏洞，从发现到修复，中间到底卡在哪儿了？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个问题，比漏洞本身更值得深思。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    微软的尴尬时刻
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   让我们换个角度看看这件事。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Microsoft Defender 是微软近年来力推的安全产品。从 Windows 10 开始，微软就在不断强化 Defender 的能力，打出"系统自带就够用"的旗号，甚至直接提示用户可以卸载第三方杀毒软件。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   很多用户的心理认知是：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     "系统自带 Defender = 足够安全"
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但 RedSun 事件打脸了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全软件天然拥有最高权限，因为只有这样才能深度扫描系统、拦截恶意进程。这没问题。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    但问题在于：如果安全软件自己出现漏洞，那它就是最高权限的漏洞。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这不是 Defender 独有的问题。历史上，卡巴斯基、迈克菲、赛门铁克等主流杀软都曾出现过类似的本地提权漏洞。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全软件 = 高权限 = 高风险。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    这条等式，从来没有被真正解决过。
   </span>
  </strong>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    你现在能做什么？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   聊完故事，说点实际的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   RedSun 目前没有官方修复补丁，但不代表你什么都做不了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    ✅ 第一，保持系统更新
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   微软很可能会快速跟进修复补丁，一旦推送，立刻安装。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    ✅ 第二，别随便运行来路不明的程序
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   RedSun 是本地提权漏洞，意味着攻击者需要先让你"主动运行"恶意程序。这是目前攻击链的起点，也是你最能控制的一环。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    ✅ 第三，日常使用标准账户
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   不要用管理员账户登录日常电脑。提权漏洞在标准用户权限下破坏力会小很多。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    ✅ 第四，企业用户加强监控
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   重点关注以下异常行为：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     Defender 进程向 System32 目录写入文件
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     可疑进程突然获得 SYSTEM 权限
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     Defender 子进程链出现异常路径
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这些都可能是攻击者正在利用漏洞的信号。🛡️
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    一个更大的信号
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   RedSun 事件背后，其实藏着一个趋势。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    过去几年，攻击者的重点正在转移。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   以前，黑客想攻入一台机器，往往要找操作系统的漏洞——Windows 漏洞、iOS 漏洞、Android 漏洞。找洞难，利用也难。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但现在，局面变了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全软件、EDR（端点检测与响应）、驱动程序、系统管理工具……这些"安全组件"因为需要高权限才能工作，反而成了新的攻击目标。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    道理很简单：
   </span>
  </strong>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     操作系统本身经过多年打磨，漏洞越来越少
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     但装在系统里的安全工具，却可能存在设计缺陷
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     而它们拥有最高权限，一旦被攻破，收益巨大
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   换句话说：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     当所有人都装上盾牌的时候，攻击者的目标就从"砍穿盾牌"变成了"让盾牌自己裂开"。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Defender 只是最新的例子，但它不会是最后一个。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    写在最后
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   RedSun 最终会不会被大规模利用？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   目前还不好说。公开的 PoC 技术含量不低，完整武器化需要额外工作。但这只是时间问题。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    真正的问题是：
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   微软会怎么应对？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   修补一个漏洞容易，修补与安全社区之间的信任关系，难。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   一个研究员愿意花时间找漏洞并提交报告，说明他对这个平台还有信任。当这种信任被辜负，选择公开叫板，对任何厂商来说都是双输的结局。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   而对于我们普通用户，这件事再次验证了一个老道理：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     没有绝对安全的软件，只有持续警惕的人。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   保持更新、谨慎运行来源不明的程序、给系统留个心眼——这些老生常谈的操作建议，在 RedSun 这样的漏洞面前，依然是最后一道防线。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    PoC：
   </span>
   <span>
    <span style="font-weight: normal; text-decoration: underline;">
     https://github.com/Nightmare-Eclipse/RedSun
    </span>
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    你怎么看这件事？
   </span>
  </strong>
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
