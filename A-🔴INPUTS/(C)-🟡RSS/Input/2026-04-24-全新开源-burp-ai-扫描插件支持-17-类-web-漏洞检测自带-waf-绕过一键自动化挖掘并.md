---
title: "全新开源 Burp AI 扫描插件、支持 17 类 Web 漏洞检测，自带 WAF 绕过，一键自动化挖掘并智能验证漏洞"
url: "https://mp.weixin.qq.com/s/4cEKtpLcK3VbaZ3dv0JzOA"
source: "渗透安全HackTwo"
date: 2026-04-24
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Zack-AI-Scanner 是一款基于大语言模型（LLM）的开源 Burp Suite 插件，支持 17 类高频 Web 漏洞的智能扫描与高置信度验证（≥90%）。其核心能力包括 AI 驱动的流量分析、动态 Payload 生成、内置 WAF 绕过策略（50%载荷专为绕过设计），以及兼容主流 AI 接口的灵活部署。插件提供 HTML/Markdown 多格式报告导出，并具备实时日志、请求响应查看和任务管理功能。使用流程简单：配置 AI API 后，右键 HTTP 请求即可启动智能或定向扫描。

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
        全新开源 Zack-AI-Scanner 是一款搭载大语言模型的 Burp Suite 漏洞扫描扩展，全面覆盖 17 类高频 Web 漏洞检测。内置多种 WAF 绕过策略与优质攻击载荷，依托 AI 引擎智能分析流量特征、动态生成测试 Payload，自动完成漏洞挖掘与高置信度核验。兼容市面主流 AI 接口，操作简单易部署，支持 HTML、Markdown 多格式报告导出，高效赋能日常授权渗透与安全检测工作。
       </span>
      </span>
     </strong>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUBPlzrwvjreBLgE0QwcvMDC0xlf7jKeoibRJ0MyV0RemY6Ogdrr07G1LEdEaSfT4OSblvWlpn0vFznvZ8SiajURhvlq4AWMmxWs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
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
   <section>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-top: 16px;">
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            AI 智能扫描
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          : 内置 Skills 利用 LLM 自动分析请求并制定测试策略
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
            多漏洞类型支持
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          : 支持 17 种常见 Web 漏洞类型的检测
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
            WAF 绕过能力
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          : 内置 Prompt 多种 WAF 绕过技术，50% 载荷为绕过载荷
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
            实时结果验证
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          : AI 二次验证确保漏洞真实性（置信度阈值 ≥90%）
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
            多格式报告导出
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          : 支持 HTML 和 Markdown 格式的渗透测试报告
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWW2W3GpINJY3ca0QAdxjmuic4y6sVJtBEJ4RKredyDIvZ1icqkMiayrmaJn9U6ibIwQt1M0qToict8iaQmc24u4Wic84W3PjCmB2crQ8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span>
        <span>
         <span style="font-size: 16px;">
          日志统计窗口可实时查看扫描信息：
         </span>
        </span>
       </span>
      </span>
     </span>
    </h3>
   </section>
   <section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWwLGa1eOddIgibzicqN01eC6tnseHL8KyicONZ9rlgOxbHO3JvJIaHFhpflsy0KNtMX9K3RicBl5bBK2uI4dE86RJe0ZeYKj3KN6M/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span>
        <span>
         <span style="font-size: 16px;">
          请求与响应详情窗口可以查看实时的扫描流量：
         </span>
        </span>
       </span>
      </span>
     </span>
    </h3>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUULB91dJhNRbhOzhX4DAzTPrTS4SYxAj2ygHSvG5fZ0AhpoSwbDkymwRvHcdsXgbsq89zGSf9sxm1QAB1OAyBS6Z6hbbQ63Q4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span>
        <span style="font-size: 16px;">
         在任务列表窗口可以查看所有扫描任务和状态，扫描结束导出漏洞报告，支持 HTML 和 Markdown 格式：
        </span>
       </span>
      </span>
     </span>
    </h3>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWAibLFiaUeDib3PyNCZdMgy69lUSYuwjcv9GT5k0IWQ0LAdn8VB3mJiaibjeib5icxkWbM003ibc4DVicm6BdKX1PshkRTzgcNiakOTqia68/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 680px !important;" />
    </section>
   </section>
   <section>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUOTfibTqIicPeLUwX6pHMO95d3fO0tribSia0Isp9tzMgDbzb69XJlsCJw40y3F0D7zMtopcuNl6wzs3icu0eh0dJSENKMqtldMJRQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 style="margin-top: 16px;">
     <span>
      <span>
       <span>
        <span>
         <span style="font-size: 16px;">
          HTML 和 Markdown 格式报告内容：
         </span>
        </span>
       </span>
      </span>
     </span>
    </h3>
    <section style="margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWJlZuXlAYPDR0PpRveeWzkpSsicEwwuQXMfrkZUbia4ibbtEHbicv47FqZDwnSSyasWvLlgTwvO3Z60jV0o4jOoxYtfIibfc14LEEo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 680px !important;" />
    </section>
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
   <h3 style="margin-top: 16px;">
    <span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       配置
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
         点击 "配置" 按钮打开配置中心
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
         选择 AI 服务提供商并输入 API Key
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
         点击 "获取模型" 按钮获取可用模型列表
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
         保存配置后即可开始使用
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
       使用
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
         在 Burp Suite 的 Proxy 或其他模块中选择 HTTP 请求
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
         右键点击，选择 "Zack-AI-Scanner" 菜单
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
         选择扫描模式（AI 智能扫描或特定漏洞类型）
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
         在主面板查看扫描进度和结果
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
         导出漏洞报告
        </span>
       </span>
      </span>
     </p>
    </li>
   </ol>
   <h2 dir="auto" tabindex="-1">
    <span>
     <span style="font-size: 16px;">
      插件使用实例
     </span>
    </span>
   </h2>
   <span>
    <span>
     <span style="font-size: 16px;">
      配置大模型API Key信息：
     </span>
    </span>
   </span>
  </section>
  <section style="text-align: left; margin-bottom: 16px; margin-top: 16px;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXnXUX2m4UibJOkH7o6X3iaMAMJqbibKDYYnOgTQLSVnicvGu2Rib60qJRkWZ76L5jP6CxdXkCVGDrLjE7LuYKpViaeibLP1U4gGguvp4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 680px !important;" />
  </section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <span>
    <span>
     <span>
      <span style="font-size: 16px;">
       右击请求包-&gt;拓展-&gt;Zack-AI-Scanner调用工具，可选择AI智能扫描和单漏洞扫描：
      </span>
     </span>
    </span>
   </span>
  </section>
  <section style="text-align: left; margin-bottom: 16px; margin-top: 16px;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU45Ym7OKcyNq469oMntW1QQnzJnicjYfIp55VdGNT31eBCQkzRzictnwag7r80tQxz4a3t0lD71TficIyjiaSjuOmBveQiaLmEiaKCQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 680px !important;" />
  </section>
  <section style="text-align: left; margin-bottom: 16px; margin-top: 16px;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUwconYz0tjA8XfbpVE3aUMgzbOq8HK0ib3owcCbT99WiagWiaIsI1AVI5gI77W3XGibica3hvLnjYtHc8unnXEuEL4TZGvsrWjAiahc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 680px !important;" />
  </section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <section>
    <span>
     <span>
      <br />
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
                 20260424
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
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
