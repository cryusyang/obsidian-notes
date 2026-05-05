---
title: "Cat Readme.txt 也能 GetShell"
url: "https://mp.weixin.qq.com/s/dHTN2lzxJXEPsdO7-KWfjQ"
source: "骨哥说事"
date: 2026-04-18
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文披露了iTerm2中一个严重的安全漏洞：攻击者可通过恶意构造的终端输出（如`cat readme.txt`）触发SSH集成功能的协议混淆，使iTerm2误将普通文本当作可信的远程conductor会话，进而执行任意本地命令。漏洞根源在于iTerm2未验证终端输出来源，盲目解析DCS 2000p和OSC 135等转义序列，导致攻击者能伪造conductor响应、操控状态机，并利用可控的`sshargs`字段构造base64编码的`run(...)`命令，最终以本地Shell权限执行恶意可执行文件。该漏洞已在2024年3月30日报告并获修复。

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
  <span>
   在之前关于Vim和Emacs中AI发现漏洞的文章中，我们探讨了看似无害的工作流程如何跨越到代码执行的惊人边界。这次我们想把这个问题推向更深处：
  </span>
  <code>
   <span>
    cat readme.txt
   </span>
  </code>
  <span>
   安全吗？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   事实证明，如果使用iTerm2，它是不安全的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这看起来很疯狂，直到你理解了iTerm2为一个合法功能所做的努力，它如何使用PTY，以及当终端输出能够冒充该功能协议的一端时会发生什么。
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    我们要感谢OpenAI与我们在该项目上的合作。
   </span>
  </p>
 </blockquote>
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <span>
    背景：iTerm2的SSH集成
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   iTerm2有一个SSH集成功能，使其能够更深入地理解远程会话。为了实现这一功能，它不仅仅是在远程Shell中"盲目输入命令"。相反，它在远程端引导一个名为conductor的小型辅助脚本。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   大致模型如下：
  </span>
 </p>
 <ol class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
     <span>
      iTerm2启动SSH集成，通常通过
     </span>
     <code>
      <span>
       it2ssh
      </span>
     </code>
     <span>
      。
     </span>
    </p>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
     <span>
      iTerm2通过现有SSH会话发送远程引导脚本——conductor。
     </span>
    </p>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
     <span>
      该远程脚本成为iTerm2的协议对等方。
     </span>
    </p>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
    <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
     <span>
      iTerm2和远程conductor交换终端转义序列来协调以下操作：
     </span>
    </p>
   </section>
  </li>
  <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
   <li>
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
     <span>
      发现登录Shell
     </span>
    </section>
   </li>
   <li>
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
     <span>
      检查Python
     </span>
    </section>
   </li>
   <li>
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
     <span>
      更改目录
     </span>
    </section>
   </li>
   <li>
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
     <span>
      上传文件
     </span>
    </section>
   </li>
   <li>
    <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1, 1, 1); font-weight: 500;">
     <span>
      运行命令
     </span>
    </section>
   </li>
  </ul>
 </ol>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   重要的一点是，没有单独的网络服务。conductor只是一个在远程Shell会话内运行的脚本，协议通过普通终端I/O传输。
  </span>
 </p>
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <span>
    PTY复习
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   终端曾经是真正的硬件设备：连接到一个机器的键盘和屏幕，程序从该设备读取输入并向其写入输出。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   像iTerm2这样的终端模拟器是硬件终端的现代软件版本。它绘制屏幕、接受键盘输入，并解释终端控制序列。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但Shell和其他命令行程序仍然期望与看起来像真正终端设备的东西通信。这就是操作系统提供PTY（即伪终端）的原因。PTY是旧硬件终端的软件替代品，它位于终端模拟器和前台进程之间。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在普通SSH会话中：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     iTerm2向PTY写入字节
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     前台进程是
    </span>
    <code>
     <span>
      ssh
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      ssh
     </span>
    </code>
    <span>
     将这些字节转发到远程机器
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     远程conductor从其stdin读取它们
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   所以当iTerm2想要"向远程conductor发送命令"时，它实际在本地做的是向PTY写入字节。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    conductor协议
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   SSH集成协议使用终端转义序列作为传输层。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这里有两个关键部分：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      DCS 2000p
     </span>
    </code>
    <span>
     用于钩住SSH conductor
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      OSC 135
     </span>
    </code>
    <span>
     用于预分帧器conductor消息
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在源代码层面，
  </span>
  <code>
   <span>
    DCS 2000p
   </span>
  </code>
  <span>
   导致iTerm2实例化一个conductor解析器。然后解析器接受
  </span>
  <code>
   <span>
    OSC 135
   </span>
  </code>
  <span>
   消息，例如：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      begin &lt;id&gt;
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     命令输出行
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      end &lt;id&gt; &lt;status&gt; r
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      unhook
     </span>
    </code>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   因此，合法的远程conductor可以通过终端输出与iTerm2进行完整对话。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    核心漏洞
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   该漏洞是信任失败。iTerm2从实际上并非来自可信的、真正的conductor会话的终端输出中接受SSH conductor协议。换句话说，不受信任的终端输出可以冒充远程conductor。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这意味着恶意文件、服务器响应、标语或MOTD可以打印：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     伪造的
    </span>
    <code>
     <span>
      DCS 2000p
     </span>
    </code>
    <span>
     钩子
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     伪造的
    </span>
    <code>
     <span>
      OSC 135
     </span>
    </code>
    <span>
     回复
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   iTerm2将开始表现得好像它正处于真正的SSH集成交换的中间。这就是漏洞利用的原语。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    漏洞利用的实际行为
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   漏洞利用文件包含一个虚假的conductor会话记录。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   当受害者运行：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   iTerm2渲染该文件，但该文件不仅仅是文本。它包含：
  </span>
 </p>
 <ol class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     一条虚假的
    </span>
    <code>
     <span>
      DCS 2000p
     </span>
    </code>
    <span>
     行，宣布一个conductor会话
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     虚假的
    </span>
    <code>
     <span>
      OSC 135
     </span>
    </code>
    <span>
     消息，回答iTerm2的请求
    </span>
   </section>
  </li>
 </ol>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   一旦钩子被接受，iTerm2就开始其正常的conductor工作流程。在上游源代码中，
  </span>
  <code>
   <span>
    Conductor.start()
   </span>
  </code>
  <span>
   立即发送
  </span>
  <code>
   <span>
    getshell()
   </span>
  </code>
  <span>
   ，之后成功时发送
  </span>
  <code>
   <span>
    pythonversion()
   </span>
  </code>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   所以漏洞利用不需要注入这些请求。iTerm2自己发出它们，恶意输出只需要冒充回复。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    遍历状态机
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   虚假的
  </span>
  <code>
   <span>
    OSC 135
   </span>
  </code>
  <span>
   消息很小但很精确。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   它们这样做：
  </span>
 </p>
 <ol class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     为
    </span>
    <code>
     <span>
      getshell
     </span>
    </code>
    <span>
     启动命令体
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     返回看起来像Shell发现输出的行
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     成功结束该命令
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     为
    </span>
    <code>
     <span>
      pythonversion
     </span>
    </code>
    <span>
     启动命令体
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     以失败结束该命令
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     取消钩子
    </span>
   </section>
  </li>
 </ol>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这足以将iTerm2推入其正常的回退路径。此时，iTerm2相信它已经完成了足够的SSH集成工作流，可以进入下一步：构建并发送
  </span>
  <code>
   <span>
    run(...)
   </span>
  </code>
  <span>
   命令。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <code>
    <span>
     sshargs
    </span>
   </code>
   <span>
    的来源
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   伪造的
  </span>
  <code>
   <span>
    DCS 2000p
   </span>
  </code>
  <span>
   钩子包含多个字段，包括攻击者控制的
  </span>
  <code>
   <span>
    sshargs
   </span>
  </code>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个值很重要，因为iTerm2稍后在构造 conductor的
  </span>
  <code>
   <span>
    run ...
   </span>
  </code>
  <span>
   请求时将其用作命令材料。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   漏洞利用选择
  </span>
  <code>
   <span>
    sshargs
   </span>
  </code>
  <span>
   ，使得当iTerm2进行base64编码时：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   run
  </span>
  
   
   
  
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   最后一个128字节块变成：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   ace/c+aliFIo
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个字符串不是任意的。选择它是因为它既是：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     conductor编码路径的有效输出
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     有效的相对路径名
    </span>
   </section>
  </li>
 </ul>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    使漏洞利用成为可能的PTY混淆
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   在合法的SSH集成会话中，iTerm2向PTY写入base64编码的conductor命令，
  </span>
  <code>
   <span>
    ssh
   </span>
  </code>
  <span>
   将它们转发到远程conductor。在漏洞利用的情况下，iTerm2仍然向PTY写入这些命令，但没有真正的SSH conductor。本地Shell将它们作为普通输入接收。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这就是为什么会话记录看起来像这样：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      getshell
     </span>
    </code>
    <span>
     显示为base64
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      pythonversion
     </span>
    </code>
    <span>
     显示为base64
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     然后出现一个长的base64编码的
    </span>
    <code>
     <span>
      run ...
     </span>
    </code>
    <span>
     有效载荷
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     最后一个块是
    </span>
    <code>
     <span>
      ace/c+aliFIo
     </span>
    </code>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   早期的块作为无效命令失败。最后一个块起作用的前提是该路径在本地存在且可执行。
  </span>
 </p>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    复现步骤
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你可以使用
  </span>
  <code>
   <span>
    genpoc.py
   </span>
  </code>
  <span>
   复现原始的基于文件的PoC：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这会创建：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      ace/c+aliFIo
     </span>
    </code>
    <span>
     ，一个可执行辅助脚本
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <code>
     <span>
      readme.txt
     </span>
    </code>
    <span>
     ，一个包含恶意
    </span>
    <code>
     <span>
      DCS 2000p
     </span>
    </code>
    <span>
     和
    </span>
    <code>
     <span>
      OSC 135
     </span>
    </code>
    <span>
     序列的文件
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   第一个愚弄iTerm2与虚假的conductor对话，第二个在最终块到达时 Get Shell一些真正要执行的东西。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   为了让漏洞利用工作，从包含
  </span>
  <code>
   <span>
    ace/c+aliFIo
   </span>
  </code>
  <span>
   的目录运行
  </span>
  <code>
   <span>
    cat readme.txt
   </span>
  </code>
  <span>
   ，这样最后一个攻击者形状的块解析为一个真实的可执行路径。
  </span>
 </p>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjmltZwzRYuCy4e8MVNdib6O613H9cVSO1Yib4OWFxUFpwrIJZSnQ6zu6icuuWjWHDg3Avia6za3uyvju5aXicicV36Y6PtyQuSYQVCs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 660px !important;" />
 </section>
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    披露时间线
   </span>
  </span>
 </h2>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     3月30日：我们向iTerm2报告了该漏洞。
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     3月31日：该漏洞在提交
    </span>
    <code>
     <span>
      a9e745993c2e2cbb30b884a16617cd5495899f86
     </span>
    </code>
    <span>
     中修复。
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     在撰写本文时，修复尚未到达稳定版本。
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   当补丁提交落地时，我们尝试仅使用补丁从头重建漏洞利用。在该过程中使用的提示词在
  </span>
  <code>
   <span>
    prompts.md
   </span>
  </code>
  <span>
   中，生成的漏洞利用是
  </span>
  <code>
   <span>
    genpoc2.py
   </span>
  </code>
  <span>
   ，它的工作方式与
  </span>
  <code>
   <span>
    genpoc.py
   </span>
  </code>
  <span>
   非常相似。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   原文：
  </span>
  <span>
   https://blog.calif.io/p/mad-bugs-even-cat-readmetxt-is-not
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
