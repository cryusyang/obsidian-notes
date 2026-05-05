---
title: "BurpSuite2026.4专业(稳定版)下载Windows/Linux/Mac支持Java21以上（支持Markdown语法）"
url: "https://mp.weixin.qq.com/s/UlKzfkpowA_xcJWWUPHyeA"
source: "渗透安全HackTwo"
date: 2026-04-25
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了一款集成Burp AI功能的汉化版Burp Suite工具更新，支持中英文切换、修复Mac平台中文包Bug，并提供详细安装指南（含Mac教程）和启动方式；强调该工具仅限合法授权的安全测试使用，要求用户自行搭建靶机环境，不得用于非法渗透；同时声明所有POC仅作理论判断，不含真实攻击能力，并附有严格的免责声明与使用约束条款。

---

<section style="padding: 0px; display: flex;">
 <section style="margin: 0px 0px 12px; padding: 0px 10px; display: flex;">
  <section style="padding: 2px 0px 4px; display: flex;">
   <section style="margin: 0px; padding: 0px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
    <section>
     <section style="background-position: right 16px top 0px; background-size: 4px 4px; margin: 0px; padding: 0px; display: flex;">
      <section style="background-position: right 9px top 0px; background-size: 4px 4px; margin: 0px; padding: 0px; display: flex;">
       <section style="background-position: right 1px top 0px; background-size: 4px 4px; margin: 0px; padding: 4px 0px 0px; display: flex;">
        <section style="background-position: left 0px top 32px; background-size: 58px 4px; margin: 0px; padding: 0px 0px 4px; display: flex;">
         <section style="margin: 0px; padding: 0px 3px 4px 8px; border-bottom-width: 1px; border-bottom-color: rgb(55, 68, 149); border-bottom-style: solid; display: flex;">
          <p style="margin: 0px; padding: 0px 6px; color: rgb(62, 62, 62); font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: left;">
           <span>
            前言
           </span>
          </p>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px; padding: 0px 10px; display: flex;">
  <section style="padding: 9px 0px 0px; display: flex;">
   <section style="margin: 0px; padding: 0px 22px 38px 26px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
    <section>
     <section style="background-position: left 6px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px; display: flex;">
      <section style="background-position: left 20px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px; display: flex;">
       <section style="background-position: left 34px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px 0px 34px; display: flex;">
        <section style="background-position: left 0px top 0px; background-size: 12px 17px; margin: 0px; padding: 0px 0px 0px 2px; display: flex;">
         <section style="background-position: left 12px top 0px; background-size: 12px 17px; margin: 0px; padding: 43px 0px 0px; display: flex;">
          <section style="margin-top: 16px;">
           <span>
            <span style="font-size: 16px;">
             Burp Suite是一个无需安装软件，下载完成后，直接从命令行启用即可。
            </span>
           </span>
           <span>
            <span style="font-size: 16px;">
             开箱即可使用支持LInux/Windows/Mac版本
            </span>
           </span>
          </section>
          <section style="text-align: center; margin-top: 16px;">
           <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq56icH5Nef6QNicUu8WXicflcvcTDViaxI1jymOYF1E2RbfxtzYBeKiclxy8YiaMR2ccQwJmE0taw0nyrWQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 610px !important;" />
          </section>
          <p style="margin-top: 16px; margin-bottom: 16px;">
           <span>
            <span style="font-size: 16px;">
             全新界面，引入
            </span>
           </span>
           <span>
            <span style="font-size: 16px;">
             Burp AI 在 Repeater 中的核心功能
            </span>
           </span>
          </p>
          <blockquote style="border-style: none; border-color: initial; padding: 0px; margin: 0px; color: rgb(62, 62, 62); font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
           <section style="text-align: center;">
            <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUZpoHsmhOBDEuiasrNPyUP2caPNN1M1ngKN5M3G6rfek3W2iaggx4BKCVmVQ9TELBtmVaXvQ5dhuoibUOcsdibfvMsva8dV2bwtiak/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 610px !important;" />
           </section>
           <section style="text-align: center; margin-bottom: 16px; margin-top: 16px;">
            <span>
            </span>
           </section>
          </blockquote>
          <p style="margin-bottom: 16px;">
           <span>
            支持中英文切换，更新设置没有汉化的问题
           </span>
          </p>
          <section style="text-align: center;">
           <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUp6LgFusThvMboruqIUPqCOGmsyVNWk7MgA0lrS7U1fWfOtenwmFmscRAsgOn2x2fYCFNTISLTWxwftATlTJAtpEiat9TeStib0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 610px !important;" />
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px; padding: 0px; display: flex;">
  <p style="margin: 0px; padding: 0px 10px; color: rgb(62, 62, 62); font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="margin: 0px 0px 12px; padding: 0px 10px; display: flex;">
  <section style="display: flex; height: 100%; margin: 0px; padding: 0px;">
   <section>
    <section style="margin: 0px; padding: 0px 3px 0px 7px; background-color: rgb(255, 255, 255); border-radius: 0%; border-width: 1px; border-color: rgb(55, 68, 149); border-style: solid; display: flex;">
     <section style="margin: 0px; padding: 0px; color: rgb(55, 68, 149); font-style: normal; font-weight: 400; font-size: 20px; line-height: 1.4; text-decoration: none; text-align: center;">
      <span>
       <span>
        01
       </span>
      </span>
     </section>
    </section>
   </section>
   <section style="margin: 0px; padding: 0px; display: flex;">
    <section style="margin: 0px; padding: 3px 3px 3px 8px; background-color: rgb(55, 68, 149); border-radius: 0%; display: flex;">
     <h1 style="margin: 0px; padding: 0px 6px; color: rgb(255, 255, 255); font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.5; text-decoration: none; text-align: left;">
      <span>
       更新介绍
      </span>
     </h1>
    </section>
   </section>
  </section>
 </section>
</section>
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
  <li>
  </li>
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>此次更新推出了用于专业版和社区版 Burp Suite 的联合安装程序，增强了对 HTTP 流量的控制能力，在 Notes 中增加了 Markdown 支持，在 Organizer 中提供了收集级别备注功能，同时还包含了一些改进和修复的错误。</span></code><code><span>作为一项强化措施，我们已移除了 Java 二进制文件。如此举影响到您的工作流程，请通过 support<span>@portswigger</span>.net 联系我们。</span></code><code><span><br /></span></code><code><span><span>#组合安装程序</span></span></code><code><span>我们为 Burp Suite 专业版和社区版推出了一个组合安装文件，这使得您能够更轻松地开始使用。您的安装、配置和授权方式与之前保持一致，因此您可以进行升级而不会出现中断的情况。</span></code><code><span>对 HTTP 流量的扩展控制得到了增强</span></code><code><span>现在，扩展功能能够阻止请求的发送，或者在 Burp 中完全处理这些请求，通过返回自定义响应来实现。</span></code><code><span>此前，扩展程序只能在数据发送之前或响应接收之后对其进行修改。此次更新消除了常见的解决方法的必要性，并使扩展程序能够完全掌控 HTTP 数据流量。</span></code><code><span><br /></span></code><code><span><span>#Notes 中的 Markdown 支持</span></span></code><code><span>现在您可以通过 Markdown 来格式化笔记，这使得编写更长的文档时能够更方便地使用标题、列表、链接和内联格式等元素进行结构化排版。</span></code><code><span>“组织者”中的集合级备注</span></code><code><span>现在，您可以通过新的“关于”选项卡为集合添加备注，从而为每个集合提供一个专门的区域来记录背景信息、目标或摘要。</span></code><code><span><br /></span></code><code><span><span>#质量的提升</span></span></code><code><span>我们已经实现了以下方面的生活质量提升：</span></code><code><span>现在您可以在“设置”&gt;“网络”&gt;“连接”中为上游代理规则添加描述。这有助于您更轻松地识别规则，尤其是在处理多个上游代理时。</span></code><code><span>现在您可以从“设置”&gt;“网络”&gt;“DNS”中清除 Burp 的 DNS 缓存。点击“清除 DNS 缓存”以删除缓存条目。</span></code><code><span>现在您可以在比较器中使用“发送到”功能将选定的内容发送到其他工具。</span></code><code><span>发送到“组织者”的请求现在包含响应时间数据，这使得更容易识别延迟并测试基于时间的行为。</span></code><code><span>现在您可以从站点地图中选择多个项目并将其发送到重复器和组织者。</span></code><code><span><br /></span></code><code><span><span>#修复内容</span></span></code><code><span>我们已修复以下问题：</span></code><code><span>入侵者现在在使用“从上一选项卡复制配置”功能时，能够正确地对所有类型的负载数据应用处理规则。</span></code><code><span>现在，消息在从 Burp 工具之间发送时会保留其已应用的突出显示效果。</span></code><code><span>在自定义操作测试对话框中的控制台面板现在在运行测试时会保持其大小和位置，因此您无需每次重新调整其大小。</span></code><code><span>Burp 现在即使在“Content-Type”头部不包含分号后空格的情况下也能正确识别 SSE 响应。</span></code><code><span>现在，当使用具有空白主题的证书时，您可以轮询私有协作服务器。</span></code></pre>
</section>
<section>
 <code>
  <span>
   <br />
  </span>
 </code>
</section>
<section>
 <code>
  <span>
   <br />
  </span>
 </code>
</section>
<section style="padding: 0px; display: flex;">
 <code>
  <span>
   <br />
  </span>
 </code>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 10px; display: flex;">
  <section>
   <code>
    <span>
     <br />
    </span>
   </code>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 10px; display: flex;">
  <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
   <section>
    <section style="margin: 0px 0px 0px 0px; padding: 0px 3px 0px 7px; background-color: #FFFFFF; border-radius: 0% 0% 0% 0%; border-width: 1px; border-color: #374495; border-style: solid; display: flex;">
     <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #374495; font-style: normal; font-weight: 400; font-size: 20px; line-height: 1.4; text-decoration: none; text-align: center;">
      <span>
       <span>
        03
       </span>
      </span>
     </section>
    </section>
   </section>
   <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
    <section style="margin: 0px 0px 0px 0px; padding: 3px 3px 3px 8px; background-color: #374495; border-radius: 0% 0% 0% 0%; display: flex;">
     <h1 style="margin: 0px 0px 0px 0px; padding: 0px 6px 0px 6px; color: #FFFFFF; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.5; text-decoration: none; text-align: left;">
      <span>
       使用/安装方法
      </span>
     </h1>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 11px 0px 10px; display: flex;">
  <section style="background-position: left 0px bottom 0px; background-size: 131px 183px; margin: 0px; padding: 0px 0px 7px 7px; display: flex;">
   <section style="background-position: right 0px top 0px; background-size: 131px 183px; margin: 0px; padding: 7px 6px 0px 0px; display: flex;">
    <section style="margin: 0px 0px 0px 0px; padding: 41px 15px 31px 22px; background-color: #F8F8F8; border-radius: 0% 0% 0% 0%; display: flex;">
     <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
      <section style="margin: 0px 0px 36px 0px; padding: 0px 0px 0px 0px; display: flex;">
       <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
        <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span>
            <span style="font-size: 16px;">
             1.脚本改进
            </span>
           </span>
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
           <li>
           </li>
           <li>
           </li>
           <li>
           </li>
           <li>
           </li>
          </ul>
          <pre class="code-snippet__js"><code><span><span>windows</span> bat文件中增加自动查找当前目录下的burpsuite_pro_v<span>*.jar</span>文件</span></code><code><span>for /R <span>"%~dp0"</span> %%i in (burpsuite_pro_v<span>*.jar</span>) do (</span></code><code><span>    set <span>"burp_jar=%%~fi"</span></span></code><code><span>    goto :Found</span></code><code><span>)</span></code><code><span>linux sh文件中增加自动查找当前目录下的burpsuite_pro_v<span>*.jar</span>文件</span></code><code><span><span># 使用globbing找到以"burpsuite_pro_v"开头的jar文件</span></span></code><code><span>for jarfile in burpsuite_pro_v<span>*.jar</span>; <span>do</span></span></code><code><span>    <span># 如果找到了文件，就跳出循环</span></span></code><code><span>    if [[ -e <span>"</span><span><span>$jarfile</span></span><span>"</span> ]]; <span>then</span></span></code><code><span>        <span>break</span></span></code><code><span>    fi</span></code><code><span>done</span></code></pre>
         </section>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span>
            <span style="font-size: 16px;">
             2.修复Mac版的中文包bug
            </span>
           </span>
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span>
            <span style="font-size: 16px;">
             3.首次安装请查看安装文档PDF进行安装
            </span>
           </span>
          </span>
         </p>
         <p style="text-align: center;">
          <span>
           <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq4VibjmWEueOxeWSGicwjWEXellv8LKJ0cVlRxUJcGQJiaTcozBz64Ho1d2xNh5ib8qqHojIWpDcUFheQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 455px !important;" />
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span>
            <span style="font-size: 16px;">
             4.老用户直接打开使用即可
            </span>
           </span>
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
            <span>
             <span style="font-size: 16px;">
              5.英文版点击
             </span>
            </span>
           </span>
           <span>
            <span style="font-size: 16px;">
             burpsuiteProEN
            </span>
           </span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
            <span>
             <span style="font-size: 16px;">
              启动
             </span>
            </span>
           </span>
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
            <span>
             <span style="font-size: 16px;">
              6.中文版点击创建桌面快捷方式即可启动
             </span>
            </span>
           </span>
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
            <span>
             <span style="font-size: 16px;">
              7.新增Mac版安装教程
             </span>
            </span>
           </span>
          </span>
         </p>
         <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
          <span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
            <span>
             <span style="font-size: 16px;">
              8.优化中文汉化问题
             </span>
            </span>
           </span>
          </span>
         </p>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
  <p style="margin: 0px 0px 0px 0px; padding: 0px 10px 0px 10px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
  <p style="margin: 0px 0px 0px 0px; padding: 0px 10px 0px 10px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 10px; display: flex;">
  <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
   <section>
    <section style="margin: 0px 0px 0px 0px; padding: 0px 3px 0px 7px; background-color: #FFFFFF; border-radius: 0% 0% 0% 0%; border-width: 1px; border-color: #374495; border-style: solid; display: flex;">
     <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #374495; font-style: normal; font-weight: 400; font-size: 20px; line-height: 1.4; text-decoration: none; text-align: center;">
      <span>
       <span>
        04
       </span>
      </span>
     </section>
    </section>
   </section>
   <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
    <section style="margin: 0px 0px 0px 0px; padding: 3px 3px 3px 8px; background-color: #374495; border-radius: 0% 0% 0% 0%; display: flex;">
     <h1 style="margin: 0px 0px 0px 0px; padding: 0px 6px 0px 6px; color: #FFFFFF; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.5; text-decoration: none; text-align: left;">
      <span>
       免责声明
      </span>
     </h1>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 11px; display: flex;">
  <section style="margin: 0px 0px 0px 0px; padding: 39px 20px 14px 25px; background-color: #F8F8F8; border-radius: 0% 0% 0% 0%; display: flex;">
   <section style="background-position: right 34px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px; display: flex;">
    <section style="background-position: right 20px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px; display: flex;">
     <section style="background-position: right 6px bottom 0px; background-size: 8px 8px; margin: 0px; padding: 0px 0px 32px; display: flex;">
      <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
       <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
        <section>
         <section style="margin: 0px 0px 22px 0px; padding: 0px 0px 0px 0px; display: flex;">
          <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
           <section style="margin: 0px 0px 17px 0px; padding: 0px 0px 0px 0px; display: flex;">
            <section style="padding: 0px 1px 0px 0px; display: flex;">
             <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 4px 0px; border-bottom-width: 1px; border-bottom-color: #E0BE75; border-bottom-style: solid; display: flex;">
              <section>
               <section style="background-position: left 0px bottom 8px; background-size: 10px 10px; margin: 0px; padding: 0px 0px 0px 18px; display: flex;">
                <h1 style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #374495; font-style: normal; font-weight: 700; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: left;">
                 <span>
                  获取方法
                 </span>
                </h1>
               </section>
              </section>
             </section>
            </section>
           </section>
           <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 1px; display: flex;">
            <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
             <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
              <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
               <strong style="font-size: 24px; letter-spacing: 0.578px; white-space: normal; background-color: rgb(248, 248, 248);">
                <span>
                 公众号回复20260425获取软件
                </span>
                <span>
                 <br />
                </span>
               </strong>
              </p>
              <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
               <span style="font-size: 17px;">
                <span>
                 全新设计界面（密码:HackTwo）
                </span>
               </span>
               <strong style="font-size: 24px; letter-spacing: 0.578px; white-space: normal; background-color: rgb(248, 248, 248);">
                <span>
                 <br />
                </span>
               </strong>
              </p>
              <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
               <strong>
                <span>
                 <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497496&amp;idx=2&amp;sn=05fc9eb156cce34fff4a02b7d72092ae&amp;scene=21#wechat_redirect" style="letter-spacing: 0.578px; background-color: rgb(248, 248, 248);" target="_blank">
                  👉点击加入内部VIP星球享受VIP资源
                 </a>
                </span>
               </strong>
               <strong>
                <span>
                 👈
                </span>
               </strong>
              </p>
              <p style="text-align: center;">
               <span>
                <br />
               </span>
              </p>
              <section style="text-align: center;">
               <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWQ0tian9JfekiatMYXCWYtoxMJh0fGf7gh7tjUhnInbeVVPuH4U92e5YMazHYBG9IWyJboFBQyN13guoz16HsZZvzGkp5WXMUUs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 613px !important;" />
              </section>
              <section style="text-align: center;">
               <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6Jl1LibyR6CRFyZro5yq18UkPRWKBs8GfTCB8sMqVvPmOWOSLicSKXoBTYPqNH5ziaGzlvZIwROozXw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 613px !important;" />
              </section>
             </section>
            </section>
           </section>
          </section>
         </section>
         <section style="margin: 0px 0px 22px 0px; padding: 0px 0px 0px 0px; display: flex;">
          <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
           <section style="margin: 0px 0px 17px 0px; padding: 0px 0px 0px 0px; display: flex;">
            <section style="padding: 0px 1px 0px 0px; display: flex;">
             <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 4px 0px; border-bottom-width: 1px; border-bottom-color: #E0BE75; border-bottom-style: solid; display: flex;">
              <section>
               <section style="background-position: left 0px bottom 8px; background-size: 10px 10px; margin: 0px; padding: 0px 0px 0px 18px; display: flex;">
                <h1 style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #374495; font-style: normal; font-weight: 700; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: left;">
                 <span>
                  最后必看
                 </span>
                </h1>
               </section>
              </section>
             </section>
            </section>
           </section>
           <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 1px; display: flex;">
            <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
             <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
              <p style="margin-bottom: 0px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span style="font-size: 16px;">
                <span>
                 本工具及文章技巧仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。
                </span>
                <span style="letter-spacing: 0.578px;">
                 <span>
                  为避免被恶意使用，本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。
                 </span>
                </span>
               </span>
              </p>
              <p style="margin-bottom: 0px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span>
                <br />
               </span>
              </p>
              <p style="margin-bottom: 0px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span style="font-size: 16px;">
                <span>
                 在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。
                </span>
                <span style="letter-spacing: 0.578px;">
                 <span>
                  如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具来源于网络，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！
                 </span>
                </span>
               </span>
              </p>
              <p style="margin-bottom: 0px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span>
                <br />
               </span>
              </p>
              <p style="margin-bottom: 0px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span style="font-size: 16px;">
                <span>
                 在安装并使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
                </span>
               </span>
              </p>
              <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
               <span>
                <br />
               </span>
              </p>
             </section>
            </section>
           </section>
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
  <p style="margin: 0px 0px 0px 0px; padding: 0px 10px 0px 10px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
   <span>
    <br />
   </span>
  </p>
 </section>
 <section style="margin: 0px 0px 36px 0px; display: flex;">
  <section style="padding: 0px 0px 1px 0px; background-color: #adadad; display: flex;">
   <section style="text-align: center; border-style: none; border-color: initial; font-size: 1px; line-height: 0.01;">
    <span>
     <br />
    </span>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 11px 0px 10px; display: flex;">
  <section style="margin: 0px 0px 0px 0px; padding: 29px 24px 38px 27px; background-color: #F8F8F8; border-radius: 0% 0% 0% 0%; display: flex;">
   <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
    <section style="margin: 0px 0px 39px 0px; padding: 0px 0px 0px 0px; display: flex;">
     <section>
      <h1 style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #374495; font-style: normal; font-weight: 700; font-size: 18px; line-height: 1.56; text-decoration: none; text-align: left;">
       <span>
        <span>
         往期推荐
        </span>
       </span>
      </h1>
     </section>
    </section>
    <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
     <section>
      <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           1.
           <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497496&amp;idx=2&amp;sn=05fc9eb156cce34fff4a02b7d72092ae&amp;scene=21#wechat_redirect" target="_blank">
            内部VIP知识星球福利介绍V1.5（AI自动化工具）
           </a>
          </span>
         </strong>
        </span>
       </p>
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           2.
           <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247483949&amp;idx=1&amp;sn=cae68096be06be4f0ea746ee5908dc79&amp;scene=21#wechat_redirect" target="_blank">
            CS4.8-CobaltStrike4.8汉化+最新插件集成版
           </a>
          </span>
         </strong>
        </span>
       </p>
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           3.
           <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497007&amp;idx=1&amp;sn=655770af8334a93b9c6c325ac307a14e&amp;scene=21#wechat_redirect" target="_blank">
            最新Nessus2026.2.7版本下载
           </a>
          </span>
         </strong>
        </span>
       </p>
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           4.
          </span>
         </strong>
        </span>
        <span style="font-size: 12px;">
         <strong>
          <span>
           <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247483882&amp;idx=1&amp;sn=e1bf597eb73ee7881ae132cc99ac0c8e&amp;chksm=cf16a75af8612e4c73eda9f52218ccfc6de72725eb37aff59e181435de095b71e653b446c521&amp;scene=21#wechat_redirect" style="font-size: 12px;" target="_blank">
            最新xray1.9.11高级版下载Windows/Linux
           </a>
          </span>
         </strong>
        </span>
        <span>
         <br />
        </span>
       </p>
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           5.
           <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247488648&amp;idx=1&amp;sn=bd330935e34f86acbc1b09dc936949ae&amp;chksm=cf16b238f8613b2e67bb625e366975e7a9a18f6e4fa47b77168a166e8690441affd832ac10cf&amp;scene=21#wechat_redirect" target="_blank">
            记一次挖洞springboot未授权到反弹shell
           </a>
          </span>
         </strong>
        </span>
        <span>
         <br />
        </span>
       </p>
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-size: 12px;">
         <strong>
          <span>
           6.
          </span>
         </strong>
        </span>
        <span style="font-size: 12px;">
         <strong>
          <span>
           <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497507&amp;idx=1&amp;sn=5b6961225d8adb6ba8d5e43d4943ef9e&amp;scene=21#wechat_redirect" target="_blank">
            最新HCL AppScan10.9.28408特别版下载
           </a>
          </span>
         </strong>
        </span>
        <span>
         <br />
        </span>
       </p>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 10px; display: flex;">
  <section style="margin: 0px 0px 0px 0px; padding: 24px 35px 24px 24px; background-color: #F8F8F8; border-radius: 0% 0% 0% 0%; display: flex;">
   <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
    <section style="margin: 0px 10px 0px 0px; padding: 0px 0px 0px 0px; width: 64.86784140969164%; display: flex;">
     <section style="display: flex; height: 100%; margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px;">
      <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
        <span style="font-weight: 700; letter-spacing: 0.578px; text-align: left; font-size: 17px;">
         <span>
          渗透安全HackTwo
         </span>
        </span>
       </p>
      </section>
      <section style="margin: 0px 0px 9px 0px; padding: 0px 0px 0px 0px; display: flex;">
       <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: left;">
        <span>
         <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; text-align: left; background-color: rgb(248, 248, 248);">
          <span>
           微信号：
          </span>
         </span>
         <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; text-align: left; background-color: rgb(248, 248, 248);">
          <span>
           关注公众号获取
          </span>
         </span>
        </span>
       </p>
      </section>
      <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; display: flex;">
       <section style="padding: 3px 0px 2px 0px; display: flex;">
        <section style="margin: 0px 0px 0px 0px; padding: 0px 10px 0px 10px; background-color: #374495; border-radius: 0% 0% 0% 0%; display: flex;">
         <section>
          <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #FFFFFF; font-style: normal; font-weight: 400; font-size: 15px; line-height: 1.87; text-decoration: none; text-align: left;">
           <span>
            <span>
             扫码关注 了解更多
            </span>
           </span>
          </p>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
    <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; width: 31.828193832599116%; display: flex;">
     <section style="margin: 0px 0px 0px 0px; padding: 4px 4px 4px 5px; background-color: #E0BE75; border-radius: 0% 0% 0% 0%; display: flex;">
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="letter-spacing: 0.578px; white-space: normal; background-color: rgb(222, 175, 74); width: 182.28125px !important; overflow: hidden; display: block; height: auto !important;" />
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
  <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
   <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
    <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
     <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
      <p style="padding-right: 10px; padding-left: 10px; color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
       <span style="font-size: 16px;">
        <br />
       </span>
      </p>
     </section>
     <section style="margin-bottom: 12px; padding-right: 10px; padding-left: 10px; letter-spacing: 0.578px; display: flex;">
      <section style="border-bottom: 2px solid rgb(55, 68, 149); display: flex;">
       <section style="padding-top: 2px; padding-bottom: 1px; display: flex;">
        <section style="padding-right: 7px; padding-left: 5px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
         <section>
          <section style="display: flex;">
           <section style="padding-right: 13px; display: flex;">
            <p style="padding-right: 6px; padding-left: 6px; color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75; text-align: left;">
             <span>
              <span style="font-size: 14px;">
               上一篇文章：
              </span>
             </span>
             <span>
              <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247492839&amp;idx=1&amp;sn=b6f091114fbd8e8922153a996c8f4f1c&amp;scene=21#wechat_redirect" target="_blank">
               Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面
              </a>
             </span>
             <span>
              <br />
             </span>
            </p>
           </section>
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0px 12px 0px; padding: 0px 10px 0px 10px; display: flex;">
  <section style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; border-bottom-width: 2px; border-bottom-color: #374495; border-bottom-style: solid; display: flex;">
   <section style="padding: 2px 0px 1px 0px; display: flex;">
    <section style="margin: 0px 0px 0px 0px; padding: 0px 7px 0px 5px; background-color: #F8F8F8; border-radius: 0% 0% 0% 0%; display: flex;">
     <section>
      <section style="margin: 0px 0px 0px 0px; display: flex;">
       <section style="display: flex;">
        <section style="padding: 0px 13px 0px 0px; display: flex;">
         <p style="margin: 0px 0px 0px 0px; padding: 0px 6px 0px 6px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: left;">
          <span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; text-align: left; background-color: rgb(248, 248, 248);">
            <span>
             喜
            </span>
           </span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; text-align: left; background-color: rgb(248, 248, 248);">
            <span>
             欢的朋友可以点赞转
            </span>
           </span>
           <span style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; text-align: left; background-color: rgb(248, 248, 248);">
            <span>
             发
            </span>
           </span>
          </span>
         </p>
        </section>
        <section>
         <img src="https://mmbiz.qpic.cn/mmbiz_svg/tqRiaNianNl1mGavBwp9Mf5RO17Jib6HN2NRSYwVT0jk8EzYYGOCRUxicpRHooD7KBlfkawia1zgicxnwMXlqxhFowCpwANhQJxA6A/640?tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" />
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
</section>
<p style="display: none;">
 
 
</p>
