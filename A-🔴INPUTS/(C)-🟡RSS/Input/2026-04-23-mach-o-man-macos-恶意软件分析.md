---
title: "“Mach-O Man” macOS 恶意软件分析"
url: "https://mp.weixin.qq.com/s/QfQW60xCpRjGZLjGRTWvPA"
source: "骨哥说事"
date: 2026-04-23
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文深度剖析了Lazarus组织发起的新型macOS攻击活动“ClickFix”，其核心是利用虚假会议邀请进行社会工程，诱导用户在终端中手动执行恶意命令，从而绕过传统安全防护。攻击使用名为“Mach-O Man”的Go语言编写的Mach-O恶意软件工具包，通过伪装成Zoom、Teams等应用窃取macOS钥匙串、浏览器会话及用户凭证，并借助Telegram隐蔽回传数据。该攻击高度依赖人为操作与原生系统工具，检测难度大，对金融科技、加密货币等行业及高管、开发者等高价值目标构成严重威胁。

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
  <em style="font-style: italic; color: black;">
   <strong style="font-weight: bold; color: black;">
    <span>
     编者按：
    </span>
   </strong>
  </em>
  <span>
   本文研究由Mauro Eldritch撰写。他是一位进攻性安全专家，也是专注于威胁情报与狩猎的公司BCA LTD的创始人。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   近期兴起的ClickFix攻击浪潮，引入了多种危害用户的新手段，似乎已成为一种将长期存在的攻击技术。我们观察到臭名昭著的Lazarus组织正在利用这种方法，分发从知名家族到各种奇特变种在内的多种恶意软件，例如基于Python重写的PyLangGhostRAT。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在本文中，我们将深入分析该攻击活动的最新阶段：一个当前正被
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    积极分发
   </span>
  </strong>
  <span>
   的新发现的macOS恶意软件工具包——“Mach-O Man”。
  </span>
 </p>
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     执行摘要
    </span>
   </strong>
  </span>
 </h2>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       当前威胁态势：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      Lazarus组织正发起一场活跃的攻击战役，利用
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       虚假会议邀请
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      作为诱饵，旨在窃取企业系统访问权限、用户凭证和敏感数据
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       高风险目标：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      金融科技、加密货币行业，以及高管、开发人员和决策者
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       广泛使用macOS的高价值环境
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       入侵手法：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      利用社会工程学陷阱，诱导受害者
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       自行复制并执行恶意命令
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ，从而绕过传统安全控制，实现悄无声息的入侵
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       核心目标：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      窃取
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       凭证、浏览器会话以及macOS钥匙串数据
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ，以获得对核心基础设施和金融资产的直接访问权限
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       难检测原因：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      攻击高度依赖
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       社会工程
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      和原生macOS程序，传统终端检测与响应工具对此类活动的可见性低
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       数据外泄渠道：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      利用
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       Telegram
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      这一受信任的通讯平台作为隐蔽的数据外传通道
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       潜在危害：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      导致账户被接管、基础设施被非法访问、财务损失以及核心数据泄露
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       对CISO的警示：
      </span>
     </span>
    </strong>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       一台被攻陷的macOS设备
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      就可能导致攻击者获得内部系统、生产环境或加密资产的完整控制权
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       SOC应对策略：
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      在威胁研判流程中，可引入跨平台分析能力，据称能
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       将凭证泄露的早期检测率提升36%
      </span>
     </span>
    </strong>
   </section>
  </li>
 </ul>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     新的 Lazarus ClickFix macOS 攻击活动深度解析：企业为何面临高风险
    </span>
   </strong>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Lazarus组织正积极运作一项攻击活动，将看似寻常的业务通信（如同事发来的会议邀请）变成通向
  </span>
  <strong>
   <span>
    凭证盗窃
   </span>
  </strong>
  <span>
   和
  </span>
  <strong>
   <span>
    数据泄露
   </span>
  </strong>
  <span>
   的直接路径。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   该攻击通常通过
  </span>
  <strong>
   <span>
    Telegram
   </span>
  </strong>
  <span>
   瞄准企业管理人员。攻击者会利用被盗的同事或联系人账户，向受害者发送看起来非常逼真的会议邀请。受害者点击链接后，会被重定向到一个模仿Zoom、Microsoft Teams或Google Meet的虚假协作平台。由于场景熟悉且紧急，受害者警惕性下降，更有可能进行下一步操作。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhicnMdMWOYsYcrvlOQccvYLaKTMPQ0Qibibd1J4MkuYemTBe1Qu7ydXbIryUROeicDLgicvJaQEgDDB1micGUib7loFPaNXTukiaibVPHg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="width: 410px !important; height: auto !important;" />
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <span>
   Lazarus组织成员发送的攻击信息。来源：Bitso Quetzal团队
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   攻击的核心不在于利用技术漏洞，而在于
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    一个简单的指令
   </span>
  </strong>
  <span>
   。受害者会被提示需要“修复”连接问题，方法是
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    复制并执行一个给定的命令
   </span>
  </strong>
  <span>
   。由于这个动作是用户自己执行的，因此它能绕过许多传统安全控制的检测，直接将系统控制权转交给攻击者。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   一旦执行了命令，攻击便会全力、迅速地榨取商业价值。首要目标是收集
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    用户凭证、浏览器会话和系统存储的秘密信息
   </span>
  </strong>
  <span>
   ，特别是
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    macOS钥匙串
   </span>
  </strong>
  <span>
   中的数据。这些资产能让攻击者立刻访问企业内网系统、各类SaaS平台和金融账户。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Telegram再次被启用，这次是作为
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    隐蔽的数据外泄通道
   </span>
  </strong>
  <span>
   。被盗的数据能通过这个合法服务传输，从而混入大量的正常网络流量中，难以被识别。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   等到安全团队发现异常时，可能为时已晚——
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    凭证早已泄露，敏感数据也已流出
   </span>
  </strong>
  <span>
   。组织将面临：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      业务系统和账户的
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       未授权访问风险
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      欺诈交易或访问权限滥用导致的
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       直接财务损失
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      敏感数据泄露引发的
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       合规处罚与声誉危机
      </span>
     </span>
    </strong>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这次攻击行动的核心是一个被Quetzal团队新发现的macOS恶意软件工具包——“
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    Mach-O Man
   </span>
  </strong>
  <span>
   ”。它由一系列采用
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    Go语言编写
   </span>
  </strong>
  <span>
   的Mach-O二进制文件构成，显示出攻击者正将目光更多地投向原生的macOS平台威胁。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     技术分析：“Mach-O Man”工具包运作全解密
    </span>
   </strong>
  </span>
 </h2>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    第一阶段：植入程序
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在这次“ClickFix”攻击中，受害者会通过Telegram收到攻击者（伪装成受损联系人）发来的会议链接。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZgD7Mw9ZcHiaX6DAqskibTu9MzBHoNmPpjgHCzpjtBC3HgyPD1Ey9gLN47kImkXrYTNJNo2Imr0lghsibOq4PiatiblGY1mqNcN5HP8/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    完整的“Mach-O Man”恶意软件工具包及其所有组件
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   点击链接后，受害者会看到一个伪造的Zoom、Meet或Teams会议页面。接着，页面会弹出一个虚假的错误提示，声称为了解决问题，用户必须将显示的一条命令
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    复制并粘贴到macOS终端中执行
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   通过使用ANY.RUN的交互式沙箱，我们可以在一个
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    安全隔离的macOS虚拟机
   </span>
  </strong>
  <span>
   中放心地执行这条命令，观察其恶意行为，而不必担心危害真实系统。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    在沙箱中实时查看虚假应用的分析过程：
   </span>
  </strong>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZht8EePPiaSHhLK1zbGPkEHdYr4JBMeSIYBBkcichwkFicpDIuuiatZKHia0Mgo7ksmRPXdggpMfklHRTR2nvEMW23G66sazITOU2MQ/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   执行后，终端命令会下载并运行第一个恶意组件——植入程序
  </span>
  <code>
   <span>
    teamsSDK.bin
   </span>
  </code>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在分析中，我们观察到一个有趣的现象：如果
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    不带任何参数
   </span>
  </strong>
  <span>
   运行这个二进制文件，它会显示一个“使用说明”。这个说明不仅告诉攻击者如何激活它，还透露了它能
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    伪装成Google Meet、Zoom、Microsoft Teams，甚至一个名为“System”的通用Mac系统提示
   </span>
  </strong>
  <span>
   。有个趣闻是：如果您尝试选择“Google”选项，它会礼貌地提示该功能“尚未实现”。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZhxVnbNrSjMUwlXkwGr84UMT4yrInmXhub4LGYJBglKxibORq0w2MB0rEaeK3RYQeINS6F8alXbqNQZP79MQUQhdogbrPkyjoibM/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    植入程序
   </span>
   <code>
    <span>
     teamsSDK.bin
    </span>
   </code>
   <span>
    的使用说明界面
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   当用正确参数启动后，它会下载一个伪造的macOS应用程序包，伪装成上述平台之一。为了能让系统顺利执行这个应用，恶意软件使用macOS的
  </span>
  <code>
   <span>
    codesign
   </span>
  </code>
  <span>
   工具为其
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    应用一个临时的签名
   </span>
  </strong>
  <span>
   ，让它看起来像是经过合法开发者签名的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这些不同的钓鱼应用实际上
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    内核代码几乎一模一样
   </span>
  </strong>
  <span>
   ，只在图标、名称等视觉元素上略有区别。它们会用蹩脚的英文，
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    连续三次
   </span>
  </strong>
  <span>
   提示用户输入密码。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZgYc3oY4ETNJTYg4dc9guyddnLpFbrgWkfSxRxiarhxX9MUibDs7L3lITpljaXxe9dtaHjn749xH9e2ufmV9phYt0hKGUSOicGVUw/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    伪装成Teams的钓鱼应用，正在索要用户凭证
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   有趣的是，前两次输入（无论密码是否正确）都会导致窗口“抖动”并提示密码错误；第三次输入后，窗口会直接消失，模拟出“登录成功”的假象。最终，所有应用都会显示Zoom的logo和一条“安装成功”的消息，显得非常混乱。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjTEia8oagLVD7xO93R6JO2ooctSsJIg5PAU2RJ6mH9iacyN3zUcyia49haUvictF5hU4ZALLkcc6bLPnqwnIicJIiaMKEib1Ad3krKhY/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    在虚假Teams应用上，竟然显示了Zoom的徽标
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   通过命令行交互式运行这些应用，会发现很多执行错误。这表明这些恶意软件的开发
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    并未经过充分的测试和完善
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZhMADMumclqtDLWrgiabqUwnew8ialvWnqylCavKnbsxT2WZDo4eJmgZHbVhQshNicO5Xj3ZthiaJNnHSI5qCTNbbGysiazAute7JEE/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    大多数恶意模块都存在功能性缺陷或意外错误
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在后台，系统正悄悄下载第二阶段的恶意程序，通常命名为
  </span>
  <code>
   <span>
    D1{??????}.bin
   </span>
  </code>
  <span>
   （如
  </span>
  <code>
   <span>
    D1YrHRTg.bin
   </span>
  </code>
  <span>
   ,
  </span>
  <code>
   <span>
    D1yCPUyk.bin
   </span>
  </code>
  <span>
   ）。同时，植入程序会通过
  </span>
  <code>
   <span>
    sysctl
   </span>
  </code>
  <span>
   命令执行基本的
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    主机指纹采集
   </span>
  </strong>
  <span>
   ，收集CPU信息、系统启动时间等。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjKhfiaueXX2XLXXI50Eauria834cWcmYOkykXBwP3fpTibib8ibZFFx1h8AyvN6LoWz7WicHoE8z0EOicJwkJXcv0WhHwBBgQZkgkLDI/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-indent: 0px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    对系统进行基本的信息收集
   </span>
  </em>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    第二阶段：信息收集器
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个程序的作用是充当
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    系统“探针”
   </span>
  </strong>
  <span>
   。它向攻击者的命令与控制服务器注册受害者主机，并发送一份详细的系统配置文件。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   和前一个组件类似，如果直接运行它，也会显示一个“友好的”使用说明。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZgMUCuicf4icIicicXGgafwNic5CicPIQNWYbZCKES1qVkhSm5hNNLs7eaQ4Db9vZC9rMFPTBOJHgKubZU8dzM6wQdP9GT2Tfb082icM8/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    大多数恶意模块都包含了帮助信息
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   该模块会利用macOS的系统命令和本地工具，构建一份
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    涵盖主机硬件、软件和网络信息的详尽档案
   </span>
  </strong>
  <span>
   ，并写入一个文本文件发送给C2。信息包括：主机名、CPU类型、运行进程列表，以及
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    专门针对Chrome、Safari、Firefox、Brave等浏览器安装的扩展程序
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZiaazGbnpMqOlEdeIu2B5KD11owNPx4DiaPpibYRNkV4X7smvYGVyHXUNvvapJdjTqSSr3Kfmlc6UM0PEsl74mon8qr4ICR8GGsrA/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    准备发送给C&amp;C服务器的系统信息文本文件
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个模块存在一个显著的
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    自我暴露缺陷
   </span>
  </strong>
  <span>
   ：有时它会进入
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    无限循环
   </span>
  </strong>
  <span>
   ，反复发送同一个配置文件给C2服务器，可能导致系统资源被耗尽，从而让用户轻易察觉到异常。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZiaWuG4dyOzJgPyia1ssumyqib0KtFACO8CUWUicwbUmzZR37nmtDVwbuR2OiavibwMCkI0ibzETZSM5sGjmH54iaSnqUvXtujSPpv3Yjs/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    恶意软件陷入无限循环，不断重复上传同一个文件
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   完成信息收集后，它会从C2服务器的
  </span>
  <code>
   <span>
    /payload
   </span>
  </code>
  <span>
   路径下载第三个组件：
  </span>
  <code>
   <span>
    minst2.bin
   </span>
  </code>
  <span>
   ，标志着
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    持久化驻留阶段
   </span>
  </strong>
  <span>
   的开始。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    第三阶段：持久化机制
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <code>
   <span>
    minst2.bin
   </span>
  </code>
  <span>
   这个组件稍微复杂一些，没有自带使用说明。通过逆向工程分析我们得知，它会接受参数并下载一个名为
  </span>
  <code>
   <span>
    localencode
   </span>
  </code>
  <span>
   的文件，将其保存到本地并重命名为
  </span>
  <code>
   <span>
    OneDrive
   </span>
  </code>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   为了实现持久化，它会在用户的Library目录下创建一个名为“
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    Antivirus Service
   </span>
  </strong>
  <span>
   ”的文件夹来存放这个恶意程序。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjIUiaibFwkSXaTt4sIcNzqMicVODsxibn0Rqxxiax7YJ4ibXyLc5xRlVEvDuC6xS4OcCVJGWuIPqFIic0c1JnV1ouOabhvyf7ZV7IPlI/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    创建一个Bash脚本来维持恶意软件自启动
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   最关键的一步是，它会创建一个macOS的
  </span>
  <strong style="font-weight: bold; color: black;">
   <code>
    <span>
     LaunchAgent
    </span>
   </code>
   <span>
    持久化启动项
   </span>
  </strong>
  <span>
   。这个启动项相当于Windows中的服务，确保恶意程序在用户每次登录时都会自动运行。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjUbcupiaUEewM5GUYAHZl0P2Eia5ZlIUMunVWpKPA2SfVfJgpvLh5pT3u0NLMiaicxAdoesicje42933ZevUtQqPUib875enzzYXUHw/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    负责持久化的 LaunchAgent 文件
   </span>
  </em>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    第四阶段：终极窃密程序
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   最终的窃密组件
  </span>
  <code>
   <span>
    macrasv2
   </span>
  </code>
  <span>
   同样从
  </span>
  <code>
   <span>
    /payload
   </span>
  </code>
  <span>
   端点下载。它负责
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    打包并窃取所有有价值的敏感数据
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    在沙箱中查看macrasv2的行为分析
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   它会将所有已收集的数据（如浏览器扩展数据、保存的登录凭证cookie、macOS钥匙串等）暂存到一个临时目录，并将其
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    压缩成一个名为
   </span>
   <code>
    <span>
     user_ext.zip
    </span>
   </code>
   <span>
    的归档文件
   </span>
  </strong>
  <span>
   ，准备外泄。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjcoKkn3Id2XctiaqibCTMgzA1Uq3ltEsx97oSgSl02ib1lsrywfDdgicRoY0fj31AA1uuJH0JNy2EheN7uFjN2QEyCAqef5mItNwU/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    准备外泄的，包含所有敏感数据的ZIP文件
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   数据外泄再次通过
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    Telegram
   </span>
  </strong>
  <span>
   进行。然而，这次攻击者犯了一个严重的错误：
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    他们泄漏了自己的Telegram机器人API密钥
   </span>
  </strong>
  <span>
   。这意味着任何人（包括安全研究员）都可以截获机器人发送的信息，甚至向其发送指令或追溯其所有者。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZiaUEdaEDmXAMI5fVITicx6nQA4ibGcP4Yiajk1agU1MWqQpJ7K654UkHickZzAUtEZV97KHEmtt3KhpxrQFTxzLsZbBqnhfNgXO7TI/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" />
  </span>
  <em style="font-style: italic; color: black;">
   <span>
    被捕获并暴露的Telegram Bot API密钥
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZghgsW7UEvKKERrfG1eric8H3LJrDDDQof7LpDuK71eVGoFt6xBULzI3qPpZicagwNLw6yt0REs8EwXGALII4g7piclGbYQJuhgyY/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" />
  </span>
  <em style="font-style: italic; color: black;">
   <span>
    通过泄漏的Bot密钥，甚至可以识别出背后操作者的信息
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   窃密完成后，该恶意软件会执行一个
  </span>
  <code>
   <span>
    delete_self.sh
   </span>
  </code>
  <strong style="font-weight: bold; color: black;">
   <span>
    自删除脚本
   </span>
  </strong>
  <span>
   ，清除入侵痕迹。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZhZgrMCS3jeCyhhianDZtTYqmMZ8BlNGnTfZkhuSxIm6aBdYRggjMbC4o9hIIicBzZBS4LYLx0C8PS8Zxb2uCxwU4PibOXN71M7gs/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px; text-align: center;">
  <em style="font-style: italic; color: black;">
   <span>
    执行
   </span>
   <code>
    <span>
     rm
    </span>
   </code>
   <span>
    命令删除自身及其他组件的脚本
   </span>
  </em>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   至此，从诱导点击到窃密清除的
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    完整攻击链
   </span>
  </strong>
  <span>
   便宣告完成。得益于macOS沙箱分析能力，从而在短时间内完整地复现了整个流程。值得注意的是，这是一种
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    前所未见的新型恶意软件
   </span>
  </strong>
  <span>
   ，若使用传统分析方法进行拆解和分析，将耗费大量时间。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     其他关键发现
    </span>
   </strong>
  </span>
 </h2>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       恶意软件质量低下
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：部分组件存在无限循环等代码缺陷，可能因消耗过多系统资源而暴露自身
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       操作安全存在重大疏忽
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：暴露了Telegram机器人令牌，且某些C2端点缺少基本认证
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       意图规避安全审查
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：使用macOS的“临时签名”功能来让恶意应用看起来被“签名”了，以此绕过系统的执行控制
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       网络特征明显
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：恶意软件主要使用8888和9999端口与C2通信，HTTP请求的User-Agent通常为“Go-http-client”，与其他Go语言组件的特征吻合
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       攻击者基础设施暴露
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：除了C2服务器，还暴露了WinRM（Windows远程管理）、Chrome Remote Desktop和RDP服务，反映出攻击者基础设施管理的混乱
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       核心技术栈
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：逆向分析证实，该恶意软件套件的
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       主要开发语言是Go
      </span>
     </span>
    </strong>
   </section>
  </li>
 </ul>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     防御 Lazarus 攻击的行动指南
    </span>
   </strong>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   以
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    “Mach-O Man”
   </span>
  </strong>
  <span>
   为代表的攻击揭示了现代威胁的核心：
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    信任滥用
   </span>
  </strong>
  <span>
   。攻击者利用合法平台（如Telegram、会议软件）和紧迫情境，操控用户心理，诱骗其执行高风险操作，从而轻易绕过传统基于签名的防御。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   对SOC团队而言，挑战在于
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    早期发现
   </span>
  </strong>
  <span>
   ，因为这些攻击混杂在大量合法的用户驱动行为之中，难以识别。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    关键对策：增强跨平台威胁研判与响应能力
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   面对此类威胁，SOC必须将
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    交互式沙箱分析
   </span>
  </strong>
  <span>
   作为威胁研判流程的核心支柱。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   与仅能自动化扫描的解决方案不同，交互式沙箱
  </span>
  <span>
   能够在一个
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    统一的沙箱环境中，对Windows、macOS、Linux和Android系统上的恶意文件及URL进行交互式分析
   </span>
  </strong>
  <span>
   ，从根本上消除了因操作系统差异造成的安全盲点。
  </span>
 </p>
 <figure style="margin: 0; margin-top: 10px; margin-bottom: 10px; display: flex;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjcm7jYMpZmhI1IJvxAicSvUpLiaJugQZ7lRHfVbHsAQLox58QZ9WMuLibAx9oeXXfibHiaTPJYBd4D7vtfnlaibic8Zzw39uQ8IjxCwU/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" />
  </span>
 </figure>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <em style="font-style: italic; color: black;">
   <span>
    这意味着安全分析师无需为每种操作系统准备不同的分析环境，便可
   </span>
  </em>
  <strong style="font-weight: bold; color: black;">
   <span>
    手动模拟用户点击、输入等交互行为
   </span>
  </strong>
  <span>
   ，完整揭示攻击链条中的隐藏阶段（如异常的
  </span>
  <code>
   <span>
    macOS sysctl
   </span>
  </code>
  <span>
   查询、Mach-O文件的后续下载行为等），并提取关键的
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    行为指示器
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   对于业务流程而言，这实现了
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    流程化的高效威胁研判
   </span>
  </strong>
  <span>
   ，能够大幅缩短分析时间，并能无缝集成到SIEM/SOAR平台，实现自动化威胁调查。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   根据 ANY.RUN 提供的数据，将沙箱集成到SOC工作流中，可以带来以下可量化的效果：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       尽早发现凭证泄露风险
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：威胁检测时间缩短至
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       60秒内
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ，在事件升级前降低泄露概率
     </span>
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       大幅缩短平均修复时间
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：响应速度提升达
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       21分钟
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ，IOC提取效率提升
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       50%
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       捕获更多高相关威胁
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：借助实时、沙箱验证的情报，威胁识别率提升
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       58%
      </span>
     </span>
    </strong>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       降低高严重性事件数量
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：早期检测能减少事件升级比例，限制其对业务运营的冲击
     </span>
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       无需增员即可提升团队效能
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：安全团队整体效率可提升高达
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       3倍
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ，一级分析师工作量减少
     </span>
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       20%
      </span>
     </span>
    </strong>
   </section>
  </li>
 </ul>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <strong style="font-weight: bold; color: black;">
    <span>
     攻击指标与战术技术映射
    </span>
   </strong>
  </span>
 </h2>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    网络IOC（入侵指标）
   </span>
  </strong>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    IP地址
   </span>
  </strong>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      172[.]86[.]113[.]102
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      144[.]172[.]114[.]220
     </span>
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    域名
   </span>
  </strong>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      update-teams[.]live
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     <span style="font-size: 14px;">
      livemicrosft[.]com
     </span>
    </span>
   </section>
  </li>
 </ul>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    文件IOC
   </span>
  </strong>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      关键文件名：
     </span>
    </strong>
    <code>
     <span>
      teamsSDK.bin
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      D1YrHRTg.bin
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      minst2.bin
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      macrasv2
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      localencode
     </span>
    </code>
    <span>
     (本地保存为
    </span>
    <code>
     <span>
      OneDrive
     </span>
    </code>
    <span>
     )
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      可疑路径：
     </span>
    </strong>
    <code>
     <span>
      ~/Library/LaunchAgents/com.onedrive.launcher.plist
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      /Users/$USER/.local/bin/OneDrive
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      多项SHA256哈希值
     </span>
    </strong>
    <span>
     （详细列表请参考原文，此处略过）
    </span>
   </section>
  </li>
 </ul>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    主机IOC
   </span>
  </strong>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      持久化项目：
     </span>
    </strong>
    <code>
     <span>
      ~/Library/LaunchAgents/com.onedrive.launcher.plist
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      其他可疑文件/目录：
     </span>
    </strong>
    <code>
     <span>
      ~/Library/.initialized
     </span>
    </code>
    <span>
     ,
    </span>
    <code>
     <span>
      $TMPDIR/geniex_client_sleep_state
     </span>
    </code>
   </section>
  </li>
 </ul>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    ATT&amp;CK 战术技术矩阵
   </span>
  </strong>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       权限提升
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：滥用sudo及sudo缓存机制
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       防御规避
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：修改文件目录权限、沙箱检测规避、使用临时代码签名
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       凭证窃取
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：从密码存储中获取凭证、利用未安全的凭证
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       发现与收集
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：全面收集系统信息、进程、文件以及浏览器数据
     </span>
    </span>
   </section>
  </li>
  <li style="font-size: 14px;">
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      <span style="font-size: 14px;">
       数据外泄
      </span>
     </span>
    </strong>
    <span>
     <span style="font-size: 14px;">
      ：通过Telegram Bot API等合法Web服务进行数据外传
     </span>
    </span>
   </section>
  </li>
 </ul>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <strong style="font-weight: bold; color: #fff;">
   <span>
    原文参考链接
   </span>
  </strong>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      原始研究报告
     </span>
    </strong>
   </section>
  </li>
  <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
   <li style="font-size: 14px;">
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
     <span>
      <span style="font-size: 14px;">
       Quetzal Team 文章: https://open.substack.com/pub/quetzalteam/p/north-koreas-safari-hunting-for-rats
      </span>
     </span>
    </section>
   </li>
   <li style="font-size: 14px;">
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
     <span>
      <span style="font-size: 14px;">
       LevelBlue Labs 情报摘要: https://otx.alienvault.com/pulse/69d9c62d24ae9bc8d5653f56
      </span>
     </span>
    </section>
   </li>
  </ul>
 </ul>
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
