---
title: "全新 AI 赋能网安平台 基于 Mitmproxy 流量分析自动化资产挖、轻量化综合渗透工具箱"
url: "https://mp.weixin.qq.com/s/sHbg9a48arEvmGpAm1tRHA"
source: "渗透安全HackTwo"
date: 2026-04-28
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Facai 是一款基于 Mitmproxy 的轻量化 AI 网络安全平台，主打全量 HTTP 流量捕获、资产自动测绘、被动爬虫与无害化漏洞检测（如 XSS/SQLi/SSRF/RCE），支持 DNSlog 盲打、请求重放及编码解码等红队常用功能。工具以 JSON 格式标准化处理 HTTP 请求与响应，兼顾人工可读性与 AI-Agent 自动化调度需求，实现站点识别、子域名解析、HTML/JS/接口数据深度采集与结构化资产梳理。系统低依赖、易部署，提供可视化操作界面，强调“零侵入”扫描与浏览器代理联动，适用于渗透测试与自动化安全运营场景。

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
        Facai 是一款全新 AI 赋能的轻量化网安平台，基于 Mitmproxy 实现全量 HTTP 流量捕获与深度分析，集成资产测绘、被动爬虫与无害化漏洞检测能力。可自动抓取浏览器及应用流量，智能分离站点、子域名与请求数据，完成资产梳理与漏洞初筛（XSS/SQL/SSRF/RCE）。内置端口扫描、请求重放、编码解码等实用工具，支持 DNSlog 盲打与自定义 payload，适配红队日常与自动化运营场景。系统低依赖、易部署，全程可视化操作，让安全测试更高效便捷。
       </span>
      </span>
     </strong>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVBC18YOlgkOibFpjhg7sjENtLeMiad8j0dWVeSvGNVQtyUEIpiaibibS63WPxqcPN6qEU5pW1ictjp8NGyADXIoml7aAU0ejibmy8mF8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
    </section>
    <blockquote>
     <p>
      <span>
       发财网安工具，都发财，谁用谁发财，你只负责点点点，其他都交给它。
      </span>
     </p>
    </blockquote>
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
   <section style="margin-top: 16px;">
    <p>
     <span>
      <span style="font-size: 16px;">
       如今已然迈入 AI 时代，传统安全的运作模式早已跟不上发展节奏，这已是行业现状。正如过往内容所表达的核心观点：当下数字化环境里，核心服务对象只有两类 —— 人类与 AI。
      </span>
     </span>
    </p>
    <p>
     <span>
      <br />
     </span>
    </p>
    <p>
     <span>
      <span style="font-size: 16px;">
       因此在工具设计层面，必须兼顾双向适配，做到人机可读、人机通用。
      </span>
     </span>
    </p>
    <p>
     <span>
      <br />
     </span>
    </p>
    <p>
     <span>
      <span style="font-size: 16px;">
       而 JSON 作为通用轻量化数据格式，兼容性极强，既能被人类快速阅读理解，也完美适配 AI-Agent 自动化调度标准。
      </span>
     </span>
    </p>
    <p>
     <span>
      <br />
     </span>
    </p>
    <p>
     <span>
      <span style="font-size: 16px;">
       本工具便以此为核心设计理念，全程围绕 HTTP 请求处理，统一采用 JSON 标准化格式进行数据交互与流转。
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
      <li>
      </li>
      <li>
      </li>
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span><span>{</span></span></code><code><span>  <span>"url"</span><span>:</span> <span>"https://a.molun.com/auth/getAuthCodeInfoByCode"</span><span>,</span></span></code><code><span>  <span>"headers"</span><span>:</span> <span>{</span></span></code><code><span>    <span>"accept"</span><span>:</span> <span>"application/json, text/plain, */*"</span><span>,</span></span></code><code><span>    <span>"content-type"</span><span>:</span> <span>"application/x-www-form-urlencoded"</span><span>,</span></span></code><code><span>    <span>"user-agent"</span><span>:</span> <span>"Mozilla/5.0..."</span><span>,</span></span></code><code><span>    <span>"cookie"</span><span>:</span> <span>"auth_sid=20000"</span></span></code><code><span>  <span>},</span></span></code><code><span>  <span>"method"</span><span>:</span> <span>"POST"</span><span>,</span></span></code><code><span>  <span>"body"</span><span>:</span> <span>"code=1&amp;client_id=65407"</span><span>,</span></span></code><code><span>  <span>"time"</span><span>:</span> <span>"2025-11-14 17:20:26"</span><span>,</span></span></code><code><span>  <span>"website"</span><span>:</span> <span>"http://a.molun.com/"</span><span>,</span></span></code><code><span>  <span>"status"</span><span>:</span> <span>0</span><span>,</span></span></code><code><span>  <span>"scaner_status"</span><span>:</span><span>0</span><span>,</span></span></code><code><span>  <span>"source"</span><span>:</span> <span>0</span>  <span>// 0=流量捕捉, 1=url生成</span></span></code><code><span><span>}</span></span></code></pre>
    </section>
    <p>
     <span>
      <span style="font-size: 16px;">
       平台以
      </span>
     </span>
     <strong>
      <span>
       <span style="font-size: 16px;">
        HTTP 请求处理
       </span>
      </span>
     </strong>
     <span>
      <span style="font-size: 16px;">
       为核心标准，通过抓取全网流量数据，自动解析拆分站点、子域名等关键资产；同步完成子域名 DNS 解析、请求响应抓取，深度采集 HTML、JS、接口报文等各类资源数据，实现全维度业务信息沉淀与结构化梳理。
      </span>
     </span>
    </p>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWIbfAzfbG7XBSZuNuQbqGFPI69wqh6hqAaF4ibZWauqCcKPaV6WoyUpTTYabfmfULuE7lsCLPtX9sjaNE0WvpqMyvZj9YupXCE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
    </section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWsQRvJUws3ibp2Y3um6u1X4k78raus9T57EPTaeN6r7x0xibkicJgBtW7T4UWAlAI620YxwvFXHakEl4tuHAycq9g7ribCjX6Libo0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 680px !important;" />
    </section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUfX5Vy2k9MxNWqjicU2jwaHLSqewVwpJ5stjsAoBxCh7PlKyANtRrCn7XxG60eibwriaGQ5zLP8AzWQicBMttRQa2PdxqX3Fe5Eqk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 680px !important;" />
    </section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUXfdNrGf64pcUGnQaUe6YNclv22R9U5lyfPxicUX8nM8JLo6Ix8iceKdLPpVTdMkyB5icicy7MzgGkibm046WK7L5icFExrNKkmficG4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 680px !important;" />
    </section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUpx5SW6NJaIXseAXfTZenOKuYkudBFCrWibsLlafYFwdfQEfEmJsNMY9ujib8ZJplXRrNJ1auOrFJSlVXgEP8w0ZXiaeUsJuIj98/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 680px !important;" />
    </section>
    <p>
     <span>
      <span style="font-size: 16px;">
       支持对http请求进行处理分离，并且处理读取html，还会对http进行漏洞扫描，并且扫描是无害化，不打任何payload，虽然有不少误报，但将就能用。
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <section style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         资产管理工具
        </span>
       </span>
      </section>
     </li>
     <li>
      <section style="margin-top: 16px;">
       <span>
        <span style="font-size: 16px;">
         被动漏洞扫描器
        </span>
       </span>
      </section>
     </li>
    </ul>
   </section>
   <section>
    <h3>
     <span>
      <span>
       <span>
        <br />
       </span>
      </span>
     </span>
    </h3>
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
    </ul>
    <pre class="code-snippet__js"><code><span><span>Full</span> Changelog</span></code></pre>
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
      <p style="text-indent: 0px;">
       <span>
        <span>
         <span style="font-size: 16px; font-weight: bold;">
          📦基础使用流程
         </span>
        </span>
       </span>
      </p>
     </section>
    </section>
   </section>
   <strong>
    <span>
     <span style="font-size: 16px; font-weight: normal;">
      安装依赖
     </span>
    </span>
   </strong>
  </section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <section>
    <ul class="code-snippet__line-index code-snippet__js">
     <li>
     </li>
    </ul>
    <pre class="code-snippet__js"><code><span>pip install -<span>r</span> requirements<span>.txt</span></span></code></pre>
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span>
      <strong>
       <span>
        <span style="font-size: 16px; font-weight: normal;">
         配置文件
        </span>
       </span>
      </strong>
      <span>
       <span>
        <span style="font-size: 16px; font-weight: normal;">
         config.json
        </span>
       </span>
      </span>
     </span>
    </span>
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
    </ul>
    <pre class="code-snippet__js"><code><span>{</span></code><code><span>    <span>"flask_port"</span>:<span>5001</span>,</span></code><code><span>    <span>"chrome_path"</span>: <span>"C:</span><span><span>\\</span></span><span>Program Files</span><span><span>\\</span></span><span>Google</span><span><span>\\</span></span><span>Chrome</span><span><span>\\</span></span><span>Application</span><span><span>\\</span></span><span>chrome.exe"</span>,</span></code><code><span>    <span>"burp_path"</span>: <span>"D:</span><span><span>\\</span></span><span>hack_tools</span><span><span>\\</span></span><span>burp</span><span><span>\\</span></span><span>"</span>,</span></code><code><span>    <span>"chrome_cdp_port"</span>: <span>19227</span>,</span></code><code><span>    <span>"chrome_spider_cdp_port"</span>: <span>19228</span>,</span></code><code><span>    <span>"mitmproxy_port"</span>: <span>18081</span>,</span></code><code><span>    <span>"burp_port"</span>:<span>8080</span>,</span></code><code><span>    <span>"mongodb"</span>: {</span></code><code><span>        <span>"ip"</span>: <span>"127.0.0.1"</span>,</span></code><code><span>        <span>"port"</span>: <span>27017</span>,</span></code><code><span>        <span>"dbname"</span>: <span>"facai"</span>,</span></code><code><span>        <span>"username"</span>: <span>""</span>,</span></code><code><span>        <span>"password"</span>: <span>""</span></span></code><code><span>    },</span></code><code><span>    <span>"AI_model"</span>:{</span></code><code><span>        <span>"model_name"</span>:<span>""</span>,</span></code><code><span>        <span>"API"</span>:<span>""</span>,</span></code><code><span>        <span>"API_KEY"</span>: <span>""</span></span></code><code><span>    }</span></code><code><span>}</span></code></pre>
   </section>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span>
      <span style="font-size: 16px;">
       这里的burp_path有个前提，我burp是破解版的，如果你不是，你可以不用填写，burp_path、burp_port。
      </span>
     </span>
    </span>
   </p>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVvibp1J3WwVZiaHAa2PzvW2c9fLIzMwERVD4S6ZlGle2OGmWicPYeMwibFLPFib14kYYbgSmgZpBKvWyMwLz9d5XxfjRtJcghLdia2A/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 680px !important;" />
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span>
      <span>
       <span style="font-size: 16px;">
        如图自行打开，然后设置burp转发端口，指向为mitmproxy_port端口。
       </span>
      </span>
     </span>
    </span>
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span>
      <strong>
       <span>
        <span style="font-size: 16px; font-weight: normal;">
         启动
        </span>
       </span>
       <span>
        <br />
       </span>
      </strong>
     </span>
    </span>
   </section>
   <section>
    <ul class="code-snippet__line-index code-snippet__js">
     <li>
     </li>
    </ul>
    <pre class="code-snippet__js"><code><span>start.bat</span></code></pre>
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <strong>
      <span>
       <span style="font-size: 16px; font-weight: normal;">
        添加项目
       </span>
      </span>
     </strong>
    </span>
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAW47YDpQQVtDlORUjZNnFfDguibVffzb2obWGUHRqPhcMEmxglAdFdynrWg0q8ESblkI4weau9buCvM4nHwpWFEEao53jLNpcuQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 680px !important;" />
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXLsDibXic3jrERx61No85jy1BxECRiaia1QaMZtPtxzNibUu3X8XFB3CRNTkjlknib2sBg7cLedeHpTgjGh2NTPzvu6fAa9pnFbTtok/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 680px !important;" />
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
    <pre class="code-snippet__js"><code><span>{</span></code><code><span>    <span>"Project"</span>: <span>"test"</span>,</span></code><code><span>    <span>"Project_Name"</span>: <span>"molun"</span>,</span></code><code><span>    <span>"Description"</span>: <span>"描述"</span>,</span></code><code><span>    <span>"domain_list"</span>: [</span></code><code><span>        <span>"lulun.com"</span>,</span></code><code><span>        <span>"molun.com"</span></span></code><code><span>    ],</span></code><code><span>    <span>"port_target"</span>: <span>"21,22,80-89,443,1080,1433,1521,3000,3306,3389,5432,5900,6379,7001,8000,8069,8080-8099,8161,8888,9080,9081,9090,9200,9300,10000-10002,11211,11434,27016-27018,36000,50000,50070"</span>,</span></code><code><span>    <span>"clipboard_text"</span>: [</span></code><code><span>        <span>"'</span><span><span>\"</span></span><span>"</span>,<span>"javascript:alert``//"</span>,<span>""</span></span></code><code><span>    ],</span></code><code><span>    <span>"dnslog_domain"</span>:<span>"{hash}.www.dnslog.com"</span>,</span></code><code><span>    <span>"dnslog_url"</span>:<span>"http://www.dnslog.com/{hash}"</span>,</span></code><code><span>    <span>"browser_thread"</span>: <span>10</span>,</span></code><code><span>    <span>"http_thread"</span>: <span>10</span>,</span></code><code><span>    <span>"user_agent"</span>: <span>"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"</span>,</span></code><code><span>    <span>"timeout"</span>: <span>8</span>,</span></code><code><span>    <span>"service_lock"</span>: {</span></code><code><span>      <span>"spider_service"</span>: <span>1</span>,</span></code><code><span>      <span>"monitor_service"</span>: <span>0</span>,</span></code><code><span>      <span>"scaner_service"</span>: <span>1</span></span></code><code><span>    },</span></code><code><span>    <span>"dns_server"</span>: [</span></code><code><span>        [</span></code><code><span>            <span>"119.29.29.29"</span>,</span></code><code><span>            <span>"119.28.28.28"</span></span></code><code><span>        ],</span></code><code><span>        [</span></code><code><span>            <span>"180.76.76.76"</span>,</span></code><code><span>            <span>"180.76.76.76"</span></span></code><code><span>        ],</span></code><code><span>        [</span></code><code><span>            <span>"180.184.1.1"</span>,</span></code><code><span>            <span>"180.184.2.2"</span></span></code><code><span>        ],</span></code><code><span>        [</span></code><code><span>            <span>"114.114.114.114"</span>,</span></code><code><span>            <span>"114.114.115.115"</span></span></code><code><span>        ],</span></code><code><span>        [</span></code><code><span>            <span>"223.5.5.5"</span>,</span></code><code><span>            <span>"223.6.6.6"</span></span></code><code><span>        ]</span></code><code><span>    ],</span></code><code><span>    <span>"file_type"</span>: [<span>".php"</span>, <span>".asp"</span>, <span>".aspx"</span>, <span>".asa"</span>, <span>".assh"</span>, <span>".jsp"</span>, <span>".jspx"</span>, <span>".do"</span>, <span>".action"</span>, <span>".py"</span>, <span>".cgi"</span>, <span>".htm"</span>, <span>".html"</span>, <span>".fcg"</span>, <span>".fcgi"</span>, <span>".xhtml"</span>, <span>".shtml"</span>, <span>".shtm"</span>, <span>".rhtml"</span>, <span>".rhtm"</span>, <span>".jhtml"</span>, <span>".jhtm"</span>, <span>".pl"</span>, <span>".php3"</span>, <span>".php4"</span>, <span>".php5"</span>, <span>".phtml"</span>, <span>".pht"</span>, <span>".phar"</span>, <span>".phpt"</span>, <span>".phs"</span>, <span>".ph7"</span>],</span></code><code><span>    <span>"file_type_disallowed"</span>: [<span>".3g2"</span>, <span>".3gp"</span>, <span>".7z"</span>, <span>".aac"</span>, <span>".abw"</span>, <span>".aif"</span>, <span>".aifc"</span>, <span>".aiff"</span>, <span>".arc"</span>, <span>".au"</span>, <span>".avi"</span>, <span>".azw"</span>, <span>".bin"</span>, <span>".bmp"</span>, <span>".bz"</span>, <span>".bz2"</span>, <span>".cmx"</span>, <span>".cod"</span>, <span>".csh"</span>, <span>".css"</span>, <span>".csv"</span>, <span>".doc"</span>, <span>".docx"</span>, <span>".eot"</span>, <span>".epub"</span>, <span>".gif"</span>, <span>".gz"</span>, <span>".ico"</span>, <span>".ics"</span>, <span>".ief"</span>, <span>".jar"</span>, <span>".jfif"</span>, <span>".jpe"</span>, <span>".jpeg"</span>, <span>".jpg"</span>, <span>".m3u"</span>, <span>".mid"</span>, <span>".midi"</span>, <span>".mjs"</span>, <span>".mp2"</span>, <span>".mp3"</span>, <span>".mp4"</span>, <span>".mpa"</span>, <span>".mpe"</span>, <span>".mpeg"</span>, <span>".mpg"</span>, <span>".mpkg"</span>, <span>".mpp"</span>, <span>".mpv2"</span>, <span>".odp"</span>, <span>".ods"</span>, <span>".odt"</span>, <span>".oga"</span>, <span>".ogv"</span>, <span>".ogx"</span>, <span>".otf"</span>, <span>".pbm"</span>, <span>".pdf"</span>, <span>".pgm"</span>, <span>".png"</span>, <span>".pnm"</span>, <span>".ppm"</span>, <span>".ppt"</span>, <span>".pptx"</span>, <span>".ra"</span>, <span>".ram"</span>, <span>".rar"</span>, <span>".ras"</span>, <span>".rgb"</span>, <span>".rmi"</span>, <span>".rtf"</span>, <span>".snd"</span>, <span>".svg"</span>, <span>".swf"</span>, <span>".tar"</span>, <span>".tif"</span>, <span>".tiff"</span>, <span>".ttf"</span>, <span>".vsd"</span>, <span>".wav"</span>, <span>".weba"</span>, <span>".webm"</span>, <span>".webp"</span>, <span>".woff"</span>, <span>".woff2"</span>, <span>".xbm"</span>, <span>".xls"</span>, <span>".xlsx"</span>, <span>".xpm"</span>, <span>".xul"</span>, <span>".xwd"</span>, <span>".zip"</span>, <span>".exe"</span>, <span>".apk"</span>, <span>".msi"</span>, <span>".dmg"</span>, <span>".rpm"</span>, <span>".deb"</span>, <span>".pkg"</span>, <span>".ios"</span>, <span>".iso"</span>, <span>".txt"</span>, <span>".m3u8"</span>, <span>".tgz"</span>, <span>".md"</span>, <span>".xml"</span>, <span>".dll"</span>],</span></code><code><span>    <span>"personal_info"</span>:{<span>"id_card_number"</span>:<span>"110105199503151234"</span>,<span>"passport_number"</span>:<span>"E12345678"</span>,<span>"marital_status"</span>:<span>"未婚"</span>,<span>"account"</span>:<span>"zhangsan_2024"</span>,<span>"password"</span>:<span>"P@ssw0rd!2024"</span>,<span>"name"</span>:<span>"张三"</span>,<span>"nickname"</span>:<span>"三儿"</span>,<span>"gender"</span>:<span>"男"</span>,<span>"age"</span>:<span>28</span>,<span>"birthday"</span>:<span>"1995-03-15"</span>,<span>"signature"</span>:<span>"热爱编程与旅行"</span>,<span>"email"</span>:<span>"zhangsan@example.com"</span>,<span>"phone"</span>:<span>"13800138000"</span>,<span>"landline"</span>:<span>"010-12345678"</span>,<span>"address"</span>:<span>"北京市朝阳区建国路88号SOHO现代城A座1001室"</span>,<span>"postal_code"</span>:<span>"100022"</span>,<span>"website_url"</span>:<span>"https://zhangsan.github.io"</span>,<span>"emergency_contact"</span>:{<span>"name"</span>:<span>"张建国"</span>,<span>"relationship"</span>:<span>"父亲"</span>,<span>"phone"</span>:<span>"13900139000"</span>},<span>"school"</span>:<span>"北京大学"</span>,<span>"education_level"</span>:<span>"硕士"</span>,<span>"major"</span>:<span>"计算机科学"</span>,<span>"graduation_time"</span>:<span>"2019-07-01"</span>,<span>"company"</span>:<span>"膜沦科技有限公司"</span>,<span>"occupation"</span>:<span>"软件工程师"</span>,<span>"position"</span>:<span>"高级开发工程师"</span>,<span>"industry"</span>:<span>"互联网"</span>,<span>"work_experience_years"</span>:<span>5</span>,<span>"country"</span>:<span>"中国"</span>,<span>"province"</span>:<span>"北京市"</span>,<span>"city"</span>:<span>"北京市"</span>,<span>"district"</span>:<span>"朝阳区"</span>,<span>"hobbies"</span>:[<span>"编程"</span>,<span>"旅行"</span>,<span>"摄影"</span>],<span>"languages"</span>:[<span>"中文"</span>,<span>"英语"</span>],<span>"avatar"</span>:<span>"https://example.com/avatars/zhangsan.jpg"</span>,<span>"social_media"</span>:{<span>"wechat"</span>:<span>"zhangsan_2024"</span>,<span>"qq"</span>:<span>"123456789"</span>,<span>"weibo"</span>:<span>"@张三的微博"</span>,<span>"linkedin"</span>:<span>"linkedin.com/in/zhangsan"</span>},<span>"agreed_to_terms"</span>:<span>true</span>,<span>"subscription_preferences"</span>:{<span>"receive_marketing_emails"</span>:<span>false</span>,<span>"receive_sms_notifications"</span>:<span>true</span>}}</span></code><code><span>    <span>"status_code"</span>: <span>1</span>,</span></code><code><span>    <span>"created_at"</span>: <span>"2026-01-16 16:54:25"</span>,</span></code><code><span>    <span>"updated_at"</span>: <span>"2026-02-25 16:21:12"</span></span></code><code><span>}</span></code></pre>
   </section>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span style="font-size: 16px;">
      1. Project为项目标识，必须纯英文。
     </span>
    </span>
   </p>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span style="font-size: 16px;">
      2. domain_list为目标范围，必须域名。
     </span>
    </span>
   </p>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span style="font-size: 16px;">
      3. dnslog_domain、dnslog_url为rce与ssrf盲打的测试url，你可以自行填写，hash是标识符，方便到时候查询是哪个请求打的。
     </span>
    </span>
   </p>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span style="font-size: 16px;">
      4. personal_info自行更改，之后爬虫会用到。
     </span>
    </span>
   </p>
   <p style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <span>
     <span style="font-size: 16px; font-weight: normal;">
      启动项目后则可用，因为流量表里没数据，得开浏览器代理指向代理端口往里面写数据，或者在资产管理、资产管理配置导入子域名或者url，写初始启动数据。
     </span>
    </span>
   </p>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXn6lNlKDTAdwPMVI3RA0T8cKTxPIhZfatM0kuKAbzRRP4w5OqdapBzVtia79qPLDn1mSnRxaxugDvRDX5nTMOZ6ZAgriagTwDag/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 680px !important;" />
   </section>
   <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWGZSsIUT9qfeEZRKcIl5jfiaqTRQ8ibibyyGB2er4FLGHFkHQJYjWoNkKSnYV4WZIiaWH4eM4uc5KyiaqQnHIsk0PpkkGriaYmWSQqE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 680px !important;" />
   </section>
   <p style="margin-bottom: 16px;">
    <strong>
     <span>
      <span style="font-size: 16px; font-weight: normal;">
       资产管理功能介绍
      </span>
     </span>
    </strong>
   </p>
   <section style="text-align: center; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUZ3U0gsuEziaVluJ0sE397k5dC7tWa8h308a0I3s0L6YtQxcNXqu6hiapzaXiaibb10dicwdQfRQAhDHCEspH2SywZMZmbvOchjMVw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 680px !important;" />
   </section>
   <p>
    <span>
     <span style="font-size: 16px;">
      也就是子域名、网站、http请求、html文件、重点资产这些比较常规的显示。
     </span>
    </span>
   </p>
   <p>
    <strong style="font-weight: 600;">
     <span>
      <span style="font-size: 16px; font-weight: normal;">
       资产管理配置
      </span>
     </span>
    </strong>
   </p>
   <section style="text-align: center; margin-bottom: 16px;">
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWBxsQONKicHdibMic0C1NvWtWkGZ5DOyXdePQBfAJxfOAaJXvLdKckVRIqzcsKDhibZkdibQ0IjekWvvY9E4CWwSaO4vhjnfHjT1KY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="height: auto !important; width: 680px !important;" />
   </section>
   <ol class="list-paddingleft-1">
   </ol>
   <section style="margin-top: 16px; text-align: left;">
    <section>
     <section style="margin-top: 16px; text-align: left;">
      <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
       <span>
        <span>
         <strong>
          <strong>
           <span>
            <span style="font-size: 16px; font-weight: normal;">
             盲打日志
            </span>
           </span>
          </strong>
         </strong>
        </span>
       </span>
      </section>
      <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
       <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXWatECH0bJia6R12Fj0TH6Aq7GN2mvGqsGjvfloicYFwHHkvkCE9jXGfrLhJq94vScfLick6WRLTARYtxluXTTPVoibeGnsVmYdjo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="height: auto !important; width: 680px !important;" />
      </section>
     </section>
    </section>
   </section>
   <section>
    <span>
     <span>
      <strong>
       <span>
        <br />
       </span>
      </strong>
     </span>
    </span>
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
                 20260428
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
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
