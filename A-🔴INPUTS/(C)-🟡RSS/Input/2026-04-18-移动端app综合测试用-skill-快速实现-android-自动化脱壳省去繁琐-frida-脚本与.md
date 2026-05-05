---
title: "移动端App综合测试|用 Skill 快速实现 Android 自动化脱壳、省去繁琐 Frida 脚本与手动 Dump 操作"
url: "https://mp.weixin.qq.com/s/j9u-ctFRyfTClMr-zCTPaA"
source: "渗透安全HackTwo"
date: 2026-04-18
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了 reverse-skills 开源项目推出的 AI 自动化脱壳工具 rev-dex-dumper，集成于 Claude Code 中，可一键完成 Android 应用脱壳全流程，包括设备检测、包名识别、工具推送、内存 Dump 和 DEX 拉取等，大幅简化传统繁琐的手动操作。该工具支持自动识别前台应用或指定包名脱壳，要求设备已 Root 并通过 ADB 连接，且需等待 App 完全启动以确保解密后 DEX 加载至内存。脱壳结果保存在本地 panda/ 目录，支持后续使用 jadx 或 IDA 进行反编译与深度分析。

---

<section>
 <section>
  <section>
   <p>
    <span>
     <span>
      0x01 工具介绍
     </span>
     <span>
     </span>
    </span>
   </p>
   <section>
    <p style="margin-bottom: 16px;">
     <span style="font-size: 17px;">
      <span style="white-space: pre-wrap;">
       <span>
        <span style="font-size: 17px;">
         <span>
          <span>
           <span>
            Android 脱壳是逆向分析的基础工作，但传统流程繁琐：Root 设备、配置 Frida、编写脚本、Dump 内存、拉取文件……一天重复多遍耗时耗力。
           </span>
          </span>
          <strong>
           <span>
            reverse-skills
           </span>
          </strong>
          <span>
           <span>
            开源项目推出的
           </span>
          </span>
          <code>
           <span>
            rev-dex-dumper
           </span>
          </code>
          <span>
           <span>
            技能，将这些步骤压缩成一句话。只需在 Claude Code 中输入指令，AI 即可自动完成从设备连接到 DEX 回收的全流程，让脱壳效率提升十倍。
           </span>
          </span>
         </span>
        </span>
       </span>
      </span>
     </span>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAX5ib9tpOuGDEjDIwU8bb44TqxWzzUMiaUIERIrYf5ZPDjaZx2HUmo9fNFYnM1GbFM99eDc1NkwrLTwNQGLL1yFAnJatPibmO2aTA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
    </section>
    <span>
    </span>
   </section>
  </section>
  <span>
  </span>
  <p style="font-size: 14px; margin-bottom: 16px; margin-top: 16px;">
   <span>
    <span style="font-size: 16px;">
     注意：
    </span>
   </span>
   <span style="text-decoration: none;">
    <span>
     <span>
      <span>
       <span style="font-size: 16px;">
        现在只对常读和星标的公众号才展示大图推送，建议大家把
       </span>
      </span>
     </span>
     <span>
      <strong>
       <span>
        <span style="font-size: 16px;">
         渗透安全HackTwo
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        "
       </span>
      </span>
     </span>
     <strong>
      <span>
       <span>
        <span style="font-size: 16px;">
         设为
        </span>
       </span>
      </span>
     </strong>
     <strong>
      <span>
       <span>
        <span style="font-size: 16px;">
         星标
        </span>
       </span>
       <strong style="letter-spacing: 0.578px;">
        <strong>
         <span>
          <span style="font-size: 16px;">
           ⭐️
          </span>
         </span>
        </strong>
       </strong>
      </span>
     </strong>
     <span>
      <span>
       <span style="font-size: 16px;">
        "
       </span>
      </span>
     </span>
     <span>
      <strong>
       <span>
        <span style="font-size: 16px;">
         否
        </span>
       </span>
      </strong>
      <strong>
       <span>
        <span style="font-size: 16px;">
         则可能就看不到了啦！
        </span>
       </span>
      </strong>
     </span>
    </span>
   </span>
  </p>
 </section>
</section>
<p>
 <strong>
  <span>
   <span>
    <span style="font-size: 16px;">
     下载地址在末尾
    </span>
   </span>
   <span>
    <a class="wx_topic_link" href="" style="color: rgb(87, 107, 149) !important;">
     <span style="font-size: 16px;">
      #渗透安全HackTwo
     </span>
    </a>
   </span>
  </span>
 </strong>
</p>
<section>
 <p>
  <span>
   <span>
    <span style="font-size: 17px;">
     0x02
    </span>
   </span>
   <span>
    <span style="font-size: 17px;">
     功能介绍
    </span>
   </span>
   <span>
    <span>
     <br />
    </span>
   </span>
  </span>
 </p>
 <p>
  <span>
   <span style="font-size: 16px;">
    ✨Skill功能说明
   </span>
  </span>
 </p>
</section>
<ul class="list-paddingleft-1">
</ul>
<section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
 <section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <section style="text-align: left; margin-top: 16px; margin-bottom: 0px;">
    <h3>
     <span>
      <span style="font-size: 16px;">
       1. 一句话脱壳，零手工干预
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span style="font-size: 16px;">
       输入指令后，Claude Code 自动完成：
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ ADB 设备连接检测
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ 前台应用包名识别
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ 脱壳工具推送与执行
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ 内存 Dump 操作
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ DEX 文件自动拉取
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         ✅ 设备临时文件清理
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-top: 16px;">
     <strong style="font-family: inherit; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; vertical-align: baseline;">
      <span>
       <span style="font-size: 16px;">
        全程无需手动操作，十几秒完成。
       </span>
      </span>
     </strong>
    </p>
    <h3>
     <span>
      <span style="font-size: 16px;">
       2. 智能包名识别
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span style="font-size: 16px;">
       支持两种使用方式：
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 8px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <strong style="font-family: inherit; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; vertical-align: baseline;">
        <span>
         <span style="font-size: 16px;">
          自动识别
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：运行 App 后直接说"帮我脱壳"
        </span>
       </span>
      </p>
     </li>
     <li style="font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px 0px 0px 6px; border: 0px; vertical-align: baseline; padding-inline-start: 6px;">
      <p style="margin-top: 16px;">
       <strong style="font-family: inherit; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; vertical-align: baseline;">
        <span>
         <span style="font-size: 16px;">
          精准定位
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：指定包名
        </span>
       </span>
       <code>
        <span>
         <span style="font-size: 16px;">
          "帮我脱 com.example.app 的壳"
         </span>
        </span>
       </code>
      </p>
     </li>
    </ul>
    <h3>
     <span>
      <span style="font-size: 16px;">
       3. 不止于脱壳的完整技能集
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px; margin-bottom: 16px;">
     <span>
      <span style="font-size: 16px;">
       reverse-skills 项目目前包含 5 大核心技能：
      </span>
     </span>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU9icJJf80otTbG79cicCpTrlibJciaiagYu2cPfMxyzMTUt05Zzwo0SKbjwClYuBCrNcrFXicVQpTc7NjrYPOpXWRTmLfx416IGFyWY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
    </section>
    <h2>
     <span>
      <br />
     </span>
     <span>
     </span>
    </h2>
    <section>
     <p style="margin-bottom: 0px;">
      <span>
       <span>
        <span>
         <br />
        </span>
       </span>
      </span>
     </p>
     <p style="border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px; margin-bottom: 0px;">
      <span>
       <span style="border-style: none;">
        0x03 更新介绍
       </span>
      </span>
     </p>
    </section>
   </section>
   <section>
    <ul class="code-snippet__line-index code-snippet__js">
     <li>
     </li>
    </ul>
    <pre class="code-snippet__js"><code><span><span>Reverse</span> engineering skills for Claude Code | 逆向工程 Claude Code Skills 插件</span></code></pre>
   </section>
   <section style="margin-bottom: 16px; margin-top: 16px;">
    <span>
     <span>
      <br />
     </span>
    </span>
    <p style="border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px;">
     <span>
      <span style="border-style: none;">
       0x04 使用介绍
      </span>
     </span>
    </p>
    <section>
     <section>
      <p style="text-indent: 0px;">
       <span>
        <span>
         <span style="font-size: 16px; font-weight: bold;">
          📦
         </span>
         <span style="font-weight: bold;">
          准备工作
         </span>
        </span>
       </span>
      </p>
     </section>
    </section>
    <ol class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            设备要求
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          ：已 Root 的 Android 手机或模拟器
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            连接确认
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          ：USB 连接电脑，执行
         </span>
        </span>
       </span>
       <span>
        <code>
         <span>
          <span style="font-size: 16px;">
           adb devices
          </span>
         </span>
        </code>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          能看到设备
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            应用启动
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          ：打开目标 App，
         </span>
        </span>
       </span>
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            等待进入主界面
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          （确保壳已完成解密加载）
         </span>
        </span>
       </span>
      </p>
     </li>
    </ol>
    <blockquote>
     <p style="margin-top: 16px;">
      <span>
       <span>
        <span style="font-size: 16px;">
         ⚠️
        </span>
       </span>
      </span>
      <span>
       <strong>
        <span>
         <span>
          <span style="font-size: 16px;">
           关键提示
          </span>
         </span>
        </span>
       </strong>
      </span>
      <span>
       <span>
        <span style="font-size: 16px;">
         ：加固壳通常在
        </span>
       </span>
      </span>
      <span>
       <code>
        <span>
         <span style="font-size: 16px;">
          Application.attachBaseContext()
         </span>
        </span>
       </code>
      </span>
      <span>
       <span>
        <span style="font-size: 16px;">
         阶段完成解密，必须等 App 完全启动后，真实 DEX 才会出现在内存中。
        </span>
       </span>
      </span>
     </p>
    </blockquote>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        操作步骤
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Step 1：安装技能
         </span>
        </span>
       </span>
      </strong>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>npx skills add P4nda0s/reverse-skills</span></code></pre>
    </section>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Step 2：验证就绪
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        在 Claude Code 中询问："你能帮我脱壳吗？" 如果 AI 回应并提到
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px;">
         rev-dex-dumper
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ，即表示安装成功。
       </span>
      </span>
     </span>
    </p>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Step 3：执行脱壳
         </span>
        </span>
       </span>
      </strong>
     </span>
    </p>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        方式 A - 自动识别当前应用：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>帮我脱壳，我已经运行 app</span></code></pre>
    </section>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        方式 B - 指定目标包名：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>帮我脱 com.example.targetapp 的壳</span></code></pre>
    </section>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Step 4：获取结果
         </span>
        </span>
       </span>
      </strong>
     </span>
    </p>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        脱壳完成后，DEX 文件会保存在当前工作目录的
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px;">
         panda/
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        文件夹中。
       </span>
      </span>
     </span>
    </p>
    <blockquote>
     <p style="margin-top: 16px;">
      <span>
       <span>
        <span style="font-size: 16px;">
         📁
        </span>
       </span>
      </span>
      <span>
       <strong>
        <span>
         <span>
          <span style="font-size: 16px;">
           文件说明
          </span>
         </span>
        </span>
       </strong>
      </span>
      <span>
       <span>
        <span style="font-size: 16px;">
         ：Dump 出多个 DEX 是正常现象，通常包含壳自身 DEX 和原始业务代码 DEX。
        </span>
       </span>
      </span>
     </p>
    </blockquote>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Step 5：后续分析
         </span>
        </span>
       </span>
      </strong>
     </span>
    </p>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        将获取的 DEX 文件导入：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            jadx
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 查看反编译后的 Java 代码
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            IDA
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 进行深入的 Native 层分析
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3>
     <span>
      <br />
     </span>
    </h3>
   </section>
  </section>
 </section>
</section>
<section>
 <section>
  <section style="letter-spacing: 0.578px;">
   <section>
    <p style="margin-top: 8px; border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px;">
     <span>
      <strong style="letter-spacing: 0.544px;">
       <span>
        0x05 内部
       </span>
       <span>
        VIP
       </span>
       <span>
        星球介绍-V1.5（福利）
       </span>
      </strong>
     </span>
    </p>
    <section style="letter-spacing: 0.578px;">
     <section>
      <section style="letter-spacing: 0.578px;">
       <p style="letter-spacing: 0.578px;">
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <span>
          <span style="font-size: 15px;">
           如果你想学习更多
          </span>
         </span>
         <strong>
          <span>
           <span style="font-size: 15px;">
            渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等
           </span>
          </span>
         </strong>
         <span>
          <span style="font-size: 15px;">
           欢迎加入我们
          </span>
         </span>
        </span>
        <strong style="letter-spacing: 0.578px; font-size: 16px;">
         <span style="color: rgb(255, 76, 65);">
          <span>
           <span style="font-size: 15px;">
            内部星球
           </span>
          </span>
         </span>
        </strong>
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <span>
          <span style="font-size: 15px;">
           可获得内部工具字典和享受内部资源和
          </span>
          <span style="font-size: 15px; font-weight: bold;">
           内部交流群，
          </span>
         </span>
         <span style="letter-spacing: 0.578px; font-size: 16px;">
          <strong>
           <strong style="color: rgb(255, 76, 65); letter-spacing: 0.578px;">
            <span>
             <span style="font-size: 15px;">
              每天更新1day/0day漏洞刷分上分
             </span>
            </span>
           </strong>
          </strong>
         </span>
        </span>
        <strong style="font-size: 16px;">
         <span style="letter-spacing: 0.578px;">
          <span>
           <span style="font-size: 15px;">
            (
           </span>
          </span>
          <span style="color: rgb(0, 0, 0); letter-spacing: 0.578px;">
           <span>
            <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497496&amp;idx=2&amp;sn=05fc9eb156cce34fff4a02b7d72092ae&amp;scene=21#wechat_redirect" target="_blank">
             2026POC更新至5732+
            </a>
           </span>
          </span>
         </span>
         <span style="letter-spacing: 0.578px;">
          <span>
           <span style="font-size: 15px;">
            )
           </span>
          </span>
         </span>
        </strong>
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <strong>
          <span>
           <span style="font-size: 15px;">
            ，
           </span>
          </span>
         </strong>
         <span>
          <span style="font-size: 15px;">
           包含全网一些
          </span>
         </span>
         <strong>
          <span>
           <span style="font-size: 15px;">
            付费扫描
           </span>
          </span>
         </strong>
         <strong>
          <span>
           <span style="font-size: 15px;">
            工具及内部原创的Burp自动化漏
           </span>
          </span>
         </strong>
         <strong>
          <span>
           <span style="font-size: 15px;">
            洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等
           </span>
          </span>
         </strong>
         <span>
          <span style="font-size: 15px;">
           。shadon/
          </span>
          <span style="font-size: 15px; font-weight: bold;">
           Hunter
          </span>
          <span style="font-size: 15px;">
           /
          </span>
         </span>
         <span>
          <span style="font-size: 15px;">
           0zone
          </span>
         </span>
         <span>
          <span style="font-size: 15px;">
           /
          </span>
          <span style="font-size: 15px; font-weight: bold;">
           Zoomeye
          </span>
          <span style="font-size: 15px;">
           /Quake/
          </span>
          <span style="font-size: 15px; font-weight: bold;">
           Fofa高级会员/AI账号
          </span>
          <span style="font-size: 15px;">
           /CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复"
          </span>
         </span>
        </span>
        <span style="letter-spacing: 0.578px; font-size: 16px; color: rgb(255, 76, 65);">
         <strong>
          <span>
           <span style="font-size: 15px;">
            星球
           </span>
          </span>
         </strong>
        </span>
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <span>
          <span style="font-size: 15px;">
           "有优惠券名额有限先到先得
          </span>
         </span>
         <span style="letter-spacing: 0.578px; font-size: 16px;">
          <strong style="letter-spacing: 0.578px;">
           <span>
            <span style="font-size: 15px;">
             ❗️
            </span>
           </span>
          </strong>
         </span>
         <span>
          <span style="font-size: 15px; font-weight: bold;">
           啥都有
          </span>
         </span>
         <span style="letter-spacing: 0.578px; font-size: 16px;">
          <strong style="letter-spacing: 0.578px;">
           <span>
            <span style="font-size: 15px;">
             ❗️
            </span>
           </span>
          </strong>
         </span>
         <span>
          <span style="font-size: 15px;">
           全网资源
          </span>
         </span>
         <span style="letter-spacing: 0.578px;">
          <span>
           <span style="font-size: 15px;">
            最新
           </span>
          </span>
         </span>
         <span>
          <span style="font-size: 15px;">
           最丰富
          </span>
         </span>
         <span style="letter-spacing: 0.578px; font-size: 16px;">
          <strong style="letter-spacing: 0.578px;">
           <span>
            <span style="font-size: 15px;">
             ❗️
            </span>
           </span>
          </strong>
         </span>
         <strong style="letter-spacing: 0.578px;">
          <span>
           <span style="font-size: 15px;">
            （
           </span>
          </span>
          <span>
           <span style="font-size: 15px;">
            🤙截止目前已有2500+多位师傅选择加入
           </span>
          </span>
          <span>
           <span style="font-size: 15px;">
            ❗️早加入早享受）
           </span>
          </span>
          <span>
           <br />
          </span>
         </strong>
        </span>
       </p>
       <p style="letter-spacing: 0.578px;">
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <strong style="letter-spacing: 0.578px;">
          <span>
           <br />
          </span>
         </strong>
        </span>
       </p>
       <section>
        <span>
         <span>
          <span style="font-size: 16px; color: rgb(255, 76, 65); font-weight: bold;">
           最新漏洞情报分享：
          </span>
         </span>
         <span>
          <span style="font-size: 16px; color: rgb(0, 0, 0); font-weight: bold;">
           https://t.zsxq.com/VuWGw
          </span>
         </span>
         <span>
          <br />
         </span>
        </span>
       </section>
       <p style="letter-spacing: 0.578px;">
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <strong style="letter-spacing: 0.578px;">
          <span>
           <br />
          </span>
         </strong>
        </span>
       </p>
      </section>
     </section>
    </section>
    <p style="letter-spacing: 0.578px;">
     <strong style="font-size: 16px;">
      <span>
       👉
      </span>
     </strong>
     <strong style="font-size: 16px;">
      <span>
       <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497496&amp;idx=2&amp;sn=05fc9eb156cce34fff4a02b7d72092ae&amp;scene=21#wechat_redirect" target="_blank">
        点击了解加入--&gt;&gt;内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新
       </a>
      </span>
     </strong>
    </p>
    <p>
     <span>
      <strong>
       <span>
        <br />
       </span>
      </strong>
     </span>
    </p>
   </section>
  </section>
 </section>
</section>
<section style="margin-bottom: 12px; padding-right: 10px; padding-left: 10px; letter-spacing: 0.578px; display: flex;">
 <section style="display: flex; height: 30px;">
  <section>
   <section style="padding-right: 3px; padding-left: 7px; background-color: rgb(255, 255, 255); border-radius: 0%; border-width: 1px; border-color: rgb(55, 68, 149); border-style: solid; display: flex;">
    <section style="color: rgb(55, 68, 149); font-size: 20px; line-height: 1.4; text-align: center;">
     <span style="font-size: 16px;">
      结尾
     </span>
    </section>
   </section>
  </section>
  <section style="display: flex;">
   <section style="padding: 3px 3px 3px 8px; background-color: rgb(55, 68, 149); border-radius: 0%; display: flex;">
    <h1 style="padding-right: 6px; padding-left: 6px; color: rgb(255, 255, 255); line-height: 1.5; text-align: left;">
     <span style="font-size: 16px;">
      免责声明
     </span>
    </h1>
   </section>
  </section>
 </section>
</section>
<section style="margin-bottom: 12px; padding-right: 10px; padding-left: 11px; letter-spacing: 0.578px; display: flex;">
 <section style="padding: 39px 20px 14px 25px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
  <section style="background-position: right 34px bottom 0px; background-size: 8px 8px; display: flex;">
   <section style="background-position: right 20px bottom 0px; background-size: 8px 8px; display: flex;">
    <section style="padding-bottom: 32px; background-position: right 6px bottom 0px; background-size: 8px 8px; display: flex;">
     <section style="display: flex; height: 1087.36px;">
      <section style="display: flex;">
       <section>
        <section style="margin-bottom: 22px; display: flex;">
         <section style="display: flex; height: 428.422px;">
          <section style="margin-bottom: 17px; display: flex;">
           <section style="padding-right: 1px; display: flex;">
            <section style="padding-bottom: 4px; border-bottom: 1px solid rgb(224, 190, 117); display: flex;">
             <section>
              <section style="padding-left: 18px; background-position: left 0px bottom 8px; background-size: 10px 10px; display: flex;">
               <h1 style="font-weight: 700; color: rgb(55, 68, 149); line-height: 1.75; text-align: left;">
                <span style="font-size: 16px;">
                 获取方法
                </span>
               </h1>
              </section>
             </section>
            </section>
           </section>
          </section>
          <section style="padding-left: 1px; display: flex;">
           <section style="display: flex; height: 378.422px;">
            <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
             <strong align="" alt="" border="" class="rich_pages wxw-img" height="" hspace="" ismap="" src="" title="" type="block" usemap="" vspace="" width="">
              <span>
               <span style="font-size: 17px;">
                公众号回复
               </span>
              </span>
              <strong style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span>
                <span style="font-size: 17px;">
                 20260418
                </span>
               </span>
              </strong>
              <span>
               <span style="font-size: 17px;">
                获取下载、回复 加群 获取交流群
               </span>
              </span>
             </strong>
            </p>
            <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
             <strong style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
              <span>
               <br />
              </span>
             </strong>
            </p>
           </section>
          </section>
         </section>
        </section>
        <section style="margin-bottom: 22px; display: flex;">
         <section style="display: flex; height: 636.938px;">
          <section style="margin-bottom: 17px; display: flex;">
           <section style="padding-right: 1px; display: flex;">
            <section style="padding-bottom: 4px; border-bottom: 1px solid rgb(224, 190, 117); display: flex;">
             <section>
              <section style="padding-left: 18px; background-position: left 0px bottom 8px; background-size: 10px 10px; display: flex;">
               <h1 style="font-weight: 700; color: rgb(55, 68, 149); line-height: 1.75; text-align: left;">
                <span style="font-size: 16px;">
                 最后必看-免责声明
                </span>
               </h1>
              </section>
             </section>
            </section>
           </section>
          </section>
          <section style="padding-left: 1px; display: flex;">
           <section style="display: flex; height: 586.938px;">
            <p>
             <span style="font-size: 16px;">
              <span>
              </span>
             </span>
             <span style="font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
              <span>
               <span style="font-size: 15px;">
                文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如
               </span>
              </span>
             </span>
             <span style="letter-spacing: 0.578px; color: rgb(62, 62, 62); font-size: 16px; background-color: rgb(248, 248, 248);">
              <span>
               <span style="font-size: 15px;">
                用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。
               </span>
              </span>
             </span>
             <span style="font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
              <span>
               <span style="font-size: 15px;">
                本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。
               </span>
              </span>
              <span style="letter-spacing: 0.578px;">
               <span>
                <span style="font-size: 15px;">
                 如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！
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
   </section>
  </section>
 </section>
</section>
<section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
 <hr />
 <p style="padding-right: 10px; padding-left: 10px; color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
  <span style="font-size: 16px;">
   <br />
  </span>
 </p>
 <section style="margin-bottom: 12px; padding-right: 11px; padding-left: 10px; letter-spacing: 0.578px; display: flex;">
  <section style="padding: 29px 24px 38px 27px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
   <section style="display: flex; height: 227.078px;">
    <section style="margin-bottom: 39px; display: flex;">
     <section>
      <h1 style="font-weight: 700; font-size: 18px; color: rgb(55, 68, 149); line-height: 1.56; text-align: left;">
       <span style="font-size: 16px;">
        往期推荐
       </span>
      </h1>
     </section>
    </section>
    <section style="display: flex;">
     <section>
      <section style="margin-bottom: 12px; display: flex;">
       <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
        <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
         <span style="font-size: 12px;">
          <strong>
           <span>
            1.
            <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497496&amp;idx=2&amp;sn=05fc9eb156cce34fff4a02b7d72092ae&amp;scene=21#wechat_redirect" target="_blank">
             内部VIP知识星球福利介绍V1.5（AI自动化）
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
             CS4.8-CobaltStrike4.8汉化+插件版
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
            <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497566&amp;idx=1&amp;sn=78501521b35b783996e5cd107d53eeda&amp;scene=21#wechat_redirect" target="_blank">
             全新升级BurpSuite2026.2专业(稳定版)
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
            <a class="normal_text_link mp_article_text_link" href="http://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247483882&amp;idx=1&amp;sn=e1bf597eb73ee7881ae132cc99ac0c8e&amp;chksm=cf16a75af8612e4c73eda9f52218ccfc6de72725eb37aff59e181435de095b71e653b446c521&amp;scene=21#wechat_redirect" target="_blank">
             最新xray1.9.11高级版下载Windows/Linux
            </a>
           </span>
          </strong>
         </span>
        </p>
        <p style="margin: 0px 0px 0px 0px; padding: 0px 0px 0px 0px; color: #3E3E3E; font-style: normal; font-weight: 400; font-size: 16px; line-height: 1.75; text-decoration: none; text-align: justify;">
         <span style="font-size: 12px;">
          <strong>
           <span>
            5.
            <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&amp;mid=2247497507&amp;idx=1&amp;sn=5b6961225d8adb6ba8d5e43d4943ef9e&amp;scene=21#wechat_redirect" target="_blank">
             最新HCL AppScan Standard
            </a>
           </span>
          </strong>
         </span>
        </p>
       </section>
       <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
        <span style="font-size: 16px;">
         <br />
        </span>
       </p>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin-bottom: 12px; padding-right: 10px; padding-left: 10px; letter-spacing: 0.578px; display: flex;">
  <section style="padding: 24px 35px 24px 24px; background-color: rgb(248, 248, 248); border-radius: 0%; display: flex;">
   <section style="display: flex; height: 133.094px;">
    <section style="margin-right: 10px; width: 323.688px; display: flex;">
     <section style="display: flex; height: 133.094px;">
      <section style="margin-bottom: 12px; display: flex;">
       <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
        <span style="font-size: 16px; font-weight: 700; text-align: left; letter-spacing: 0.578px;">
         <span>
          <span style="font-size: 14px;">
           渗透安全HackTwo
          </span>
         </span>
        </span>
       </p>
      </section>
      <section style="margin-bottom: 9px; display: flex;">
       <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75; text-align: left;">
        <span style="letter-spacing: 0.578px; font-size: 16px;">
         <span>
          <span style="font-size: 14px;">
           微信号：关注公众号获取
          </span>
         </span>
        </span>
       </p>
       <p style="color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75; text-align: left;">
        <span style="font-size: 16px;">
         <span style="letter-spacing: 0.578px;">
          <span>
           <span style="font-size: 14px; font-weight: normal;">
            后台回复星球加入：
           </span>
          </span>
         </span>
         <span style="letter-spacing: 0.578px; color: rgb(255, 76, 65);">
          <span>
           <span style="font-size: 14px; font-weight: bold;">
            知识星球
           </span>
          </span>
         </span>
        </span>
       </p>
      </section>
      <section style="display: flex;">
       <section style="padding-top: 3px; padding-bottom: 2px; display: flex;">
        <section style="padding-right: 10px; padding-left: 10px; background-color: rgb(55, 68, 149); border-radius: 0%; display: flex;">
         <section>
          <p style="color: rgb(255, 255, 255); font-size: 15px; line-height: 1.87; text-align: left;">
           <span style="font-size: 16px;">
            <span style="font-size: 14px; font-weight: bold;">
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
    <section style="width: 158.812px; display: flex;">
     <section style="padding: 4px 4px 4px 5px; background-color: rgb(224, 190, 117); border-radius: 0%; display: flex;">
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
  <p style="padding-right: 10px; padding-left: 10px; color: rgb(62, 62, 62); font-size: 16px; line-height: 1.75;">
   <span style="font-size: 16px;">
    <br />
   </span>
  </p>
  <section style="padding: 0px; display: flex;">
   <section style="margin: 0px 0px 12px 0px; padding: 0px 0px 0px 0px; display: flex;">
    <section style="margin-bottom: 12px; letter-spacing: 0.578px; display: flex;">
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
<p style="display: none;">
 
 
</p>
