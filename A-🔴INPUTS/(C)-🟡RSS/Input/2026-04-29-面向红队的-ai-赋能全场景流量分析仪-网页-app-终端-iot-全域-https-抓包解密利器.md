---
title: "面向红队的 AI 赋能全场景流量分析仪 网页 / APP / 终端 / IoT 全域 HTTPS 抓包解密利器"
url: "https://mp.weixin.qq.com/s/g4xtj_WwAN4klDxhuCMc9Q"
source: "渗透安全HackTwo"
date: 2026-04-29
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Anything Analyzer是一款面向红队实战的AI赋能型全场景流量分析工具，支持内嵌浏览器CDP捕获与MITM代理双模式，可统一采集网页、APP、IoT等多端HTTPS流量。其核心优势在于AI智能分析引擎，能自动过滤噪声、逆向JS加密逻辑、识别API接口，并提供API逆向、安全审计等5种分析模式。工具还深度集成MCP生态，支持作为AI Agent的抓包插件被Claude Desktop、Cursor等调用。操作上支持证书自动管理、流式报告输出与多轮追问，兼顾合规性与易用性，显著提升渗透测试与协议分析效率。

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
    <p>
     <strong style="font-weight: 600;">
      <span>
       <span style="font-weight: normal;">
        Anything Analyzer是一款面向红队实战、AI深度赋能的全场景流量分析仪，专为渗透测试、协议逆向与安全审计打造全域HTTPS抓包解密利器。工具整合内嵌浏览器CDP捕获与MITM中间人代理双重模式，全面覆盖网页、APP、终端脚本、IoT设备等多端流量采集需求，自动统一流量会话管理。依托AI智能分析引擎，可自动过滤冗余噪声、深度解析加密请求与JS加密逻辑，快速完成接口逆向、敏感风险排查与协议梳理工作。内置合规证书管理与MCP生态对接能力，轻量化易部署、操作简单高效，助力红队人员简化流量研判流程，高效开展资产梳理、漏洞筛查与业务协议深度分析工作。
       </span>
      </span>
     </strong>
    </p>
    <span>
    </span>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUD9luzy1lDvCEoYLcCT2icMIiacTVfYRUHMPek98QHM1AYHCCxG6icWoeNJE7niaEbYTK8FCoQZ1w97I2s6jqtqobqvKVQl5rI0Os/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
    </section>
    <span>
    </span>
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
    ✨主要功能
   </span>
  </span>
 </p>
</section>
<ul class="list-paddingleft-1">
</ul>
<section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
 <section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <h2 dir="auto" style="margin-top: 16px;" tabindex="-1">
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       为什么用 Anything Analyzer？
      </span>
     </span>
    </h2>
    <p>
     <span>
      <span style="font-size: 16px;">
       传统工具各管一摊：DevTools 只看浏览器、Fiddler/Charles 只做代理、Wireshark 看不了 HTTPS。抓完包还得自己翻几百条请求，手动分析。
      </span>
     </span>
    </p>
    <p>
     <strong style="font-weight: 600;">
      <span>
       <span style="font-size: 16px;">
        Anything Analyzer 不一样 —— 全场景抓包 + AI 自动分析：
       </span>
      </span>
     </strong>
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
     <pre class="code-snippet__js"><code><span>  网页          桌面应用         终端            脚本          手机/IoT</span></code><code><span>  Chrome       Postman         <span>curl</span>/<span>wget</span>      Python        App / 小程序</span></code><code><span>    │          Electron          │             Node.js          │</span></code><code><span>    │            │               │               │              │</span></code><code><span>    ▼            ▼               ▼               ▼              ▼</span></code><code><span> ┌──────────┐ ┌─────────────────────────────────────────────────────┐</span></code><code><span> │ 内嵌浏览器 │ │              MITM 代理 (端口 <span>8888</span>)                   │</span></code><code><span> │   (CDP)   │ │   系统代理 / 手动指定 / Wi<span>-Fi</span> 代理                    │</span></code><code><span> └─────┬─────┘ └──────────────────────┬──────────────────────────────┘</span></code><code><span>       │                              │</span></code><code><span>       └──────────┬───────────────────┘</span></code><code><span>                  ▼</span></code><code><span>        ┌─────────────────┐</span></code><code><span>        │  统一会话 Session  │  ← 所有来源的请求汇入同一个会话</span></code><code><span>        └────────┬────────┘</span></code><code><span>                 ▼</span></code><code><span>        ┌─────────────────┐</span></code><code><span>        │   AI 智能分析     │  ← 一键生成协议逆向 / 安全审计 / 加密分析报告</span></code><code><span>        └─────────────────┘</span></code></pre>
    </section>
    <h2 dir="auto" style="margin-bottom: 16px;" tabindex="-1">
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       三大核心能力
      </span>
     </span>
    </h2>
    <h3 dir="auto" tabindex="-1">
     <span>
      <span style="font-size: 16px;">
       1. 全场景抓包 — Anything，不止浏览器
      </span>
     </span>
    </h3>
    
     <table style="border-spacing: 0px; border-collapse: collapse; width: max-content; display: block; overflow: auto;">
      <thead>
       <tr>
        <th style="padding: 6px 13px; font-weight: 600; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            抓包对象
           </span>
          </span>
         </section>
        </th>
        <th style="padding: 6px 13px; font-weight: 600; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            怎么抓
           </span>
          </span>
         </section>
        </th>
        <th style="padding: 6px 13px; font-weight: 600; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            典型场景
           </span>
          </span>
         </section>
        </th>
       </tr>
      </thead>
      <tbody>
       <tr>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            网页
           </span>
          </span>
         </strong>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            内嵌浏览器直接操作
           </span>
          </span>
         </section>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            网站 API 逆向、OAuth 登录、前端加密
           </span>
          </span>
         </section>
        </td>
       </tr>
       <tr>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            桌面应用
           </span>
          </span>
         </strong>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            MITM 代理 + 系统代理
           </span>
          </span>
         </section>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            Postman、Electron 应用、游戏客户端
           </span>
          </span>
         </section>
        </td>
       </tr>
       <tr>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            终端命令
           </span>
          </span>
         </strong>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            MITM 代理 + 环境变量
           </span>
          </span>
         </section>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            curl、wget、httpie
           </span>
          </span>
         </section>
        </td>
       </tr>
       <tr>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            脚本程序
           </span>
          </span>
         </strong>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            MITM 代理 + 代码配置
           </span>
          </span>
         </section>
        </td>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <section>
          <span>
           <span style="font-size: 14px;">
            Python requests、Node.js fetch、Go http
           </span>
          </span>
         </section>
        </td>
       </tr>
       <tr>
        <td style="padding: 6px 13px; border: 1px solid rgb(209, 217, 224);">
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            手机 / 平板
           </span>
          </span>
         </strong>
        </td>
        <td>
         <section>
          <span>
           <span style="font-size: 14px;">
            MITM 代理 + Wi-Fi 代理
           </span>
          </span>
         </section>
        </td>
        <td>
         <section>
          <span>
           <span style="font-size: 14px;">
            iOS/Android App、小程序、H5
           </span>
          </span>
         </section>
        </td>
       </tr>
       <tr>
        <td>
         <strong style="font-weight: 600;">
          <span>
           <span style="font-size: 14px;">
            IoT / 其他设备
           </span>
          </span>
         </strong>
        </td>
        <td>
         <section>
          <span>
           <span style="font-size: 14px;">
            MITM 代理 + 网关代理
           </span>
          </span>
         </section>
        </td>
        <td>
         <section>
          <span>
           <span style="font-size: 14px;">
            智能家居、嵌入式设备的 HTTP 通信
           </span>
          </span>
         </section>
        </td>
       </tr>
      </tbody>
     </table>
    
    <p>
     <span>
      <span style="font-size: 16px;">
       所有来源的请求
      </span>
     </span>
     <strong style="font-weight: 600;">
      <span>
       <span style="font-size: 16px;">
        统一汇入同一个 Session
       </span>
      </span>
     </strong>
     <span>
      <span style="font-size: 16px;">
       ，AI 分析时一并处理。
      </span>
     </span>
    </p>
    <h3 dir="auto" tabindex="-1">
     <span>
      <span style="font-size: 16px;">
       2. AI 智能分析 — 不只是抓包，是自动理解协议
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            两阶段分析
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — Phase 1 智能过滤噪声请求 → Phase 2 聚焦深度分析
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
            5 种分析模式
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 自动识别 / API 逆向 / 安全审计 / 性能分析 / JS 加密逆向
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
            JS Hook 注入
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 自动拦截 fetch、XHR、crypto.subtle、CryptoJS、SM2/3/4 等加密调用
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
            加密代码提取
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 从 JS 文件中自动提取加密相关代码片段
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
            流式输出 + 多轮追问
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 报告实时流式显示，可继续追问细节
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 dir="auto" tabindex="-1">
     <span>
      <span style="font-size: 16px;">
       3. MCP 生态集成 — AI Agent 的抓包工具
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            MCP Client
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 接入外部 MCP Server（stdio + StreamableHTTP），扩展 AI 分析能力
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
            内置 MCP Server
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          — 将抓包和分析能力暴露为 MCP 工具，可被 Claude Desktop、Cursor 等直接调用
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h2 dir="auto" style="margin-top: 16px;" tabindex="-1">
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       使用场景
      </span>
     </span>
    </h2>
    <table>
     <thead>
      <tr>
       <th>
        <section>
         <span>
          <span style="font-size: 14px;">
           场景
          </span>
         </span>
        </section>
       </th>
       <th>
        <section>
         <span>
          <span style="font-size: 14px;">
           流量来源
          </span>
         </span>
        </section>
       </th>
       <th>
        <section>
         <span>
          <span style="font-size: 14px;">
           你能得到什么
          </span>
         </span>
        </section>
       </th>
      </tr>
     </thead>
     <tbody>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           逆向网站 API
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           内嵌浏览器
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           API 端点文档 + 鉴权流程 + Python 复现代码
          </span>
         </span>
        </section>
       </td>
      </tr>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           逆向 App 协议
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           手机 Wi-Fi 代理
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           App 的隐藏 API + 请求签名逻辑
          </span>
         </span>
        </section>
       </td>
      </tr>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           JS 加密逆向
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           内嵌浏览器 + JS Hook
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           加密算法识别 + 流程还原 + Python 实现
          </span>
         </span>
        </section>
       </td>
      </tr>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           安全审计
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           浏览器 + 代理混合
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           Token 泄露、CSRF/XSS 漏洞、敏感数据暴露
          </span>
         </span>
        </section>
       </td>
      </tr>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           调试 CLI 工具
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           终端 curl/httpie
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           完整请求/响应记录 + AI 解读每一步
          </span>
         </span>
        </section>
       </td>
      </tr>
      <tr>
       <td>
        <strong style="font-weight: 600;">
         <span>
          <span style="font-size: 14px;">
           调试微服务
          </span>
         </span>
        </strong>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           脚本 + 环境变量代理
          </span>
         </span>
        </section>
       </td>
       <td>
        <section>
         <span>
          <span style="font-size: 14px;">
           服务间调用链路 + 认证流转分析
          </span>
         </span>
        </section>
       </td>
      </tr>
     </tbody>
    </table>
    <p>
     <strong style="font-weight: 600;">
      <span>
       <br />
      </span>
     </strong>
    </p>
    <p style="border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px;">
     <span>
      <span style="border-style: none;">
       0x03 更新介绍
      </span>
     </span>
    </p>
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
    </ul>
    <pre class="code-snippet__js"><code><span><span>macOS</span> 自动更新签名校验失败 — 修复 mac 发布链路中更新包签名/校验缺失的问题，避免 </span></code><code><span>ShipIt 在更新时提示“代码对象根本未签名”并导致新版本无法正确安装</span></code><code><span>AI / MCP 多轮追问上下文丢失 — 修复重新分析后聊天历史未正确重置、MCP 追问缺少初始上下文的问题，提升继续追问时的分析准确性</span></code><code><span>聊天失败状态残留 — 发送追问失败时会回滚乐观插入的用户消息，避免 UI 中残留无效消息</span></code></pre>
   </section>
   <section>
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
      <p style="text-indent: 0px; margin-bottom: 16px;">
       <span>
        <span>
         <span style="font-size: 16px; font-weight: bold;">
          📦Anything Analyzer 详细设置、快捷操作与常见问题全套说明
         </span>
        </span>
       </span>
      </p>
      <span>
      </span>
      <section>
       <ul class="code-snippet__line-index code-snippet__js">
        <li>
        </li>
        <li>
        </li>
        <li>
        </li>
       </ul>
       <pre class="code-snippet__js"><code><span><span>Anything</span> Analyzer是面向红队实战、AI赋能的全场景流量分析抓包工具，适配Windows、macOS、Linux全平台，无需复杂编译配置，开箱即用，可一站式实现网页、手机APP、终端脚本、IoT设备全域HTTPS流量抓包解密与协议智能分析。</span></code><code><span>安装无需额外环境依赖，直接前往项目Releases页面，对应电脑系统下载匹配版本安装包，双击完成常规安装即可，全程无捆绑、无多余配置。首次使用需基础简单配置，第一步在工具设置面板填入兼容OpenAI、Anthropic等大模型的API密钥与接口地址，完成AI模型对接；第二步按需启用内置MITM中间人代理，安装本地可信CA证书，默认<span>8888</span>端口即可正常抓包解密HTTPS流量。</span></code><code><span>使用操作简单便捷，支持两种抓包模式，一是内嵌浏览器直接访问目标站点，新建专属会话后一键启停抓包，自动捕获网页全量请求与JS加密调用记录；二是配置系统、终端、手机WiFi代理，捕获外部应用、脚本及IoT设备流量。抓包完成后，可筛选目标请求，一键触发AI智能分析，自动过滤冗余噪声，快速完成API逆向、安全审计、加密逻辑解析，生成结构化分析报告，支持多轮追问研判与报告、请求数据导出，适配红队协议逆向、渗透测试、安全审计全实战场景。</span></code></pre>
      </section>
      <p style="text-indent: 0px; margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span>
          <span style="font-weight: bold;">
           下载对应平台安装包
          </span>
         </span>
        </span>
       </span>
      </p>
      <table>
       <thead>
        <tr>
         <th>
          <section>
           <span>
            <span style="font-size: 14px;">
             平台
            </span>
           </span>
          </section>
         </th>
         <th>
          <section>
           <span>
            <span style="font-size: 14px;">
             文件
            </span>
           </span>
          </section>
         </th>
        </tr>
       </thead>
       <tbody>
        <tr>
         <td>
          <section>
           <span>
            <span style="font-size: 14px;">
             Windows
            </span>
           </span>
          </section>
         </td>
         <td>
          <code>
           <span>
            <span style="font-size: 14px;">
             Anything-Analyzer-Setup-x.x.x.exe
            </span>
           </span>
          </code>
         </td>
        </tr>
        <tr>
         <td>
          <section>
           <span>
            <span style="font-size: 14px;">
             macOS (Apple Silicon)
            </span>
           </span>
          </section>
         </td>
         <td>
          <code>
           <span>
            <span style="font-size: 14px;">
             Anything-Analyzer-x.x.x-arm64.dmg
            </span>
           </span>
          </code>
         </td>
        </tr>
        <tr>
         <td>
          <section>
           <span>
            <span style="font-size: 14px;">
             macOS (Intel)
            </span>
           </span>
          </section>
         </td>
         <td>
          <code>
           <span>
            <span style="font-size: 14px;">
             Anything-Analyzer-x.x.x-x64.dmg
            </span>
           </span>
          </code>
         </td>
        </tr>
        <tr>
         <td>
          <section>
           <span>
            <span style="font-size: 14px;">
             Linux
            </span>
           </span>
          </section>
         </td>
         <td>
          <code>
           <span>
            <span style="font-size: 14px;">
             Anything-Analyzer-x.x.x.AppImage
            </span>
           </span>
          </code>
         </td>
        </tr>
       </tbody>
      </table>
     </section>
    </section>
   </section>
   <span>
    <span>
     <span style="font-size: 16px; font-weight: bold;">
      抓网页 — 内嵌浏览器
     </span>
    </span>
   </span>
  </section>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          配置 LLM
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        — Settings → LLM，填入 API Key（支持 OpenAI / Anthropic / 任何兼容 API）
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
          新建 Session
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        — 输入名称和目标 URL
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
          操作抓包
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        — 在内嵌浏览器中操作网站，点击 Start Capture
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
          AI 分析
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        — 停止捕获，点击 Analyze，选择分析模式
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
  <h3 dir="auto" tabindex="-1">
   <span>
    <span style="font-size: 16px;">
     抓应用/终端/手机 — MITM 代理
    </span>
   </span>
  </h3>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        Settings → MITM 代理 →
       </span>
      </span>
     </span>
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          安装 CA 证书
         </span>
        </span>
       </span>
      </strong>
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
          启用代理
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        （默认端口
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px;">
         8888
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        根据场景配置代理：
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
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
   </ul>
   <pre class="code-snippet__js"><code><span><span># ---- 终端命令 ----</span></span></code><code><span>curl -<span>x</span> http:<span>//</span><span>127.0</span>.<span>0</span>.<span>1</span>:<span>8888</span> https:<span>//api</span>.example.com/data</span></code><code><span><span># ---- Python 脚本 ----</span></span></code><code><span>proxies = {<span>"http"</span>: <span>"http://127.0.0.1:8888"</span>, <span>"https"</span>: <span>"http://127.0.0.1:8888"</span>}</span></code><code><span>requests.get(<span>"https://api.example.com/data"</span>, proxies=proxies)</span></code><code><span><span># ---- Node.js ----</span></span></code><code><span>HTTP_PROXY=http:<span>//</span><span>127.0</span>.<span>0</span>.<span>1</span>:<span>8888</span> HTTPS_PROXY=http:<span>//</span><span>127.0</span>.<span>0</span>.<span>1</span>:<span>8888</span> node app.js</span></code><code><span><span># ---- 系统全局（桌面应用自动走代理）----</span></span></code><code><span><span># Settings 中一键开启「设为系统代理」</span></span></code><code><span><span># ---- 手机 / 平板 ----</span></span></code><code><span><span># Wi-Fi 设置 → HTTP 代理 → 手动 → 填入电脑 IP + 端口 8888</span></span></code><code><span><span># 然后用手机浏览器访问代理地址下载并安装 CA 证书</span></span></code></pre>
  </section>
  <p style="margin-top: 16px;">
   <span>
    <span>
     <span style="font-size: 16px;">
      新建 Session（URL 可留空）→ Start Capture → 外部应用流量自动汇入
     </span>
    </span>
   </span>
  </p>
  <p style="margin-top: 16px;">
   <span>
    <span>
     <span style="font-size: 16px; font-weight: bold;">
      CA 证书详细说明
     </span>
    </span>
   </span>
  </p>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        证书存储：
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px;">
         %APPDATA%/anything-analyzer/certs/
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        （Windows）/
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px;">
         ~/Library/Application Support/anything-analyzer/certs/
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        （macOS）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        首次安装需管理员权限（Windows UAC / macOS 密码）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        Settings 中可随时卸载、重新生成或导出证书
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        根 CA 有效期 10 年，子证书 825 天（符合 Apple 要求）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        MITM 代理为
       </span>
      </span>
     </span>
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          只读捕获
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ，不修改请求/响应内容
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        WebSocket 流量隧道转发，不做解密
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        单个 body 上限 1MB，二进制内容自动跳过
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
  <h2 dir="auto" style="margin-top: 16px;" tabindex="-1">
   <span>
    <span style="font-size: 16px; font-weight: bold;">
     全部功能
    </span>
   </span>
  </h2>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <span>
    <strong>
     <span>
      <span style="font-size: 16px;">
       抓包引擎
      </span>
     </span>
    </strong>
   </span>
  </section>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        全量网络捕获 — CDP Fetch 拦截，所有 HTTP 请求/响应（含 headers、body）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        MITM 代理 — 内置 HTTPS 中间人代理，自动签发 TLS 证书，按域名 LRU 缓存
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        双通道捕获 — 浏览器 CDP + MITM 代理，统一汇入同一会话
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        SSE / WebSocket 识别 — 自动检测流式通信和 WebSocket 升级请求
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        存储快照 — 定时采集 Cookie、localStorage、sessionStorage 变化
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        Domain 过滤 — 请求列表按域名分组过滤，支持部分匹配搜索
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        请求来源标记 — 区分「CDP」和「代理」来源
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        导出请求 — 原始请求数据导出为 JSON 文件
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <span>
    <strong>
     <strong>
      <span>
       <span style="font-size: 16px;">
        AI 分析
       </span>
      </span>
     </strong>
    </strong>
   </span>
  </section>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        两阶段分析 — Phase 1 智能过滤 → Phase 2 深度分析，AI 按需查看请求详情
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        手动多选分析 — 勾选指定请求直接分析，跳过预过滤
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        自定义 Prompt 模板 — 内置多种模板，支持自定义
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        流式输出 + 追问 — 报告实时显示，支持多轮对话
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <span>
    <strong>
     <strong>
      <span>
       <span style="font-size: 16px;">
        系统
       </span>
      </span>
     </strong>
    </strong>
   </span>
  </section>
  <ul class="list-paddingleft-1">
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        系统代理集成 — 一键设为系统代理（Windows 注册表 / macOS networksetup / Linux gsettings）
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        CA 证书管理 — 安装 / 卸载 / 重新生成 / 导出，跨平台支持
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        全局代理 — 支持 SOCKS5/HTTP/HTTPS 代理
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        自动更新 — 内置 electron-updater
       </span>
      </span>
     </span>
    </p>
   </li>
   <li>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        暗色主题 — 基于 Ant Design 的现代界面
       </span>
      </span>
     </span>
    </p>
   </li>
  </ul>
 </section>
</section>
<section>
 <section>
  <section style="letter-spacing: 0.578px;">
   <section>
    <h2 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        设置
       </span>
      </span>
     </span>
    </h2>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        点击左下角齿轮图标打开设置面板，包含以下选项卡：
       </span>
      </span>
     </span>
    </p>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        通用
       </span>
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          语言选择：中文 / English
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          主题选择：深色 / 浅色
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          自动更新检查
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        LLM
       </span>
      </span>
     </span>
    </h3>
    <figure>
     <table>
      <thead>
       <tr>
        <th>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             配置项
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             说明
            </span>
           </span>
          </span>
         </span>
        </th>
       </tr>
      </thead>
      <tbody>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             Provider
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             OpenAI / Anthropic / 自定义
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             API Type
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             Chat Completions / Responses API（OpenAI）
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             Base URL
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             API 地址（如
            </span>
           </span>
          </span>
          <span>
           <code>
            <span>
             <span style="font-size: 16px;">
              https://api.openai.com/v1
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 16px;">
             ）
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             API Key
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             你的 API 密钥
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             Model
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             模型名称（如
            </span>
           </span>
          </span>
          <span>
           <code>
            <span>
             <span style="font-size: 16px;">
              gpt-4o
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 16px;">
             、
            </span>
           </span>
          </span>
          <span>
           <code>
            <span>
             <span style="font-size: 16px;">
              claude-sonnet-4-20250514
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 16px;">
             ）
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             Max Tokens
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             最大输出 token 数
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
      </tbody>
     </table>
    </figure>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        Prompt 模板
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        管理 AI 分析的 Prompt 模板：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          内置多种模板（API 逆向、安全审计、性能分析、加密逆向）
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          支持自定义模板：编辑 System Prompt 和分析要求
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          可修改内置模板，也可重置为默认
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        MCP 客户端
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        配置外部 MCP Server，扩展 AI 分析能力：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          支持 stdio 和 StreamableHTTP 两种传输方式
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          AI 分析时可自动调用 MCP 工具
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        MCP 服务端
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        将 Anything Analyzer 的抓包和分析能力暴露为 MCP 工具：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          可被 Claude Desktop、Cursor 等 AI 工具直接调用
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          配置监听端口
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        代理
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        配置 Anything Analyzer 自身的出站代理：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          支持 HTTP / HTTPS / SOCKS5
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          用于内嵌浏览器和 AI API 请求
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        MITM 代理
       </span>
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          启用/禁用 MITM 代理
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          配置监听端口
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          CA 证书管理（安装/卸载/重新生成/导出）
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          系统代理开关
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
   </section>
   <section>
    <h2 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        常见问题
       </span>
      </span>
     </span>
    </h2>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        AI 分析失败
       </span>
      </span>
     </span>
    </h3>
    <figure>
     <table>
      <thead>
       <tr>
        <th>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             错误提示
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             解决方案
            </span>
           </span>
          </span>
         </span>
        </th>
       </tr>
      </thead>
      <tbody>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             DNS 解析失败
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             检查 API 地址拼写是否正确
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             连接被拒绝
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             确认 API 服务已启动（本地中转时常见）
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             网络请求失败
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             检查网络连接，可能需要代理/VPN
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             连接超时
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             API 服务响应慢，检查网络或更换节点
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             SSL 证书错误
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             检查 API 地址是否正确，代理是否干扰
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
       <tr>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             LLM provider not configured
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 16px;">
             先在设置中配置 LLM
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
      </tbody>
     </table>
    </figure>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        MITM 代理无法抓到 HTTPS
       </span>
      </span>
     </span>
    </h3>
    <ol class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          确认已安装 CA 证书
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          确认应用使用系统代理（部分应用需手动配置）
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          证书固定（Certificate Pinning）的应用无法被 MITM 代理捕获
         </span>
        </span>
       </span>
      </p>
     </li>
    </ol>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        请求列表为空
       </span>
      </span>
     </span>
    </h3>
    <ol class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          确认已点击「开始」按钮
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          确认在正确的会话下操作
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          内嵌浏览器操作时确认页面已加载
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          MITM 代理模式确认外部应用已配置代理
         </span>
        </span>
       </span>
      </p>
     </li>
    </ol>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        追问回答不准确
       </span>
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          AI 追问时已自动携带请求摘要上下文
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          追问时 AI 可以通过工具查看任意请求的完整详情
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          建议追问时指明具体的请求序号（如「请查看
         </span>
         <a class="wx_topic_link" href="" style="color: #576B95 !important;">
          <span style="font-size: 16px;">
           #5
          </span>
         </a>
         <span style="font-size: 16px;">
          请求的响应体」）
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p>
     <span>
      <span>
       <br />
      </span>
     </span>
    </p>
    <p>
     <span>
      <span>
       <br />
      </span>
     </span>
    </p>
    <p style="border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px;">
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
             2026POC更新至5841+
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
<p style="margin-bottom: 0px; letter-spacing: 0.578px;">
 <span style="font-size: 16px;">
  <br />
 </span>
</p>
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
             <strong style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
              <span>
               <span style="font-size: 17px;">
                公众号回复
               </span>
              </span>
              <strong style="color: rgb(62, 62, 62); font-size: 16px; letter-spacing: 0.578px; background-color: rgb(248, 248, 248);">
               <span>
                <span style="font-size: 17px;">
                 20260429
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
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
