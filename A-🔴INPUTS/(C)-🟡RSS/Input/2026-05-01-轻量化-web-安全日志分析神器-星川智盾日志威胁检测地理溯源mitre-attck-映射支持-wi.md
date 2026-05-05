---
title: "轻量化 Web 安全日志分析神器 星川智盾日志威胁检测、地理溯源、MITRE ATT&CK 映射，支持 Windows/macOS/Linux"
url: "https://mp.weixin.qq.com/s/y345Z62SYZwt4fheoRoufQ"
source: "渗透安全HackTwo"
date: 2026-05-01
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 「星川智盾」是一款跨平台（Windows/macOS/Linux）轻量级Web安全日志分析工具，集成AI智能分析与130+条本地安全规则，可精准检测SQL注入、XSS、WebShell等30类攻击，并支持IP地理溯源、MITRE ATT&CK战术映射及多维度可视化分析。工具提供开箱即用体验，支持多种日志格式导入，自动生成中文DOCX/PDF报告，并具备攻击会话、路径、地理等深度溯源面板。文章还介绍了详细安装使用流程及配套VIP知识星球资源，但强调所有工具仅限合法授权的安全研究与学习用途。

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
        轻量化 Web 安全日志分析神器「星川智盾」，适配 Windows/macOS/Linux 全平台。集成 AI 智能分析与本地 130 + 条安全规则，覆盖 SQL 注入、XSS、WebShell 等 30 类攻击。支持日志威胁精准检测、IP 地理溯源、MITRE ATT&amp;CK 战术映射，提供可视化面板与 DOCX/PDF 报告导出。赛博朋克界面，低误报、开箱即用，助力快速完成 Web 日志安全审计与攻防溯源。
       </span>
      </span>
     </strong>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVZpsqAsuc1yAjcLEzbgrOUFh9Nd2GiaiaDeXKuUEL7xnIeE5M62ichXATtO0laoniau6oFgEeiaicmfW7WlphLR9Z5mERzZzOwLtvpY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
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
    ✨主要功能、
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    双引擎驱动 · 8 大 AI 平台
   </span>
  </span>
 </p>
</section>
<ul class="list-paddingleft-1">
</ul>
<section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
 <section>
  <section style="margin-bottom: 16px;">
   <section style="text-align: left; margin-top: 16px;">
    <h2 style="text-align: center;">
     <span>
      <code>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ◈
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        为什么选择星川智盾？
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ◈
        </span>
       </span>
      </code>
     </span>
    </h2>
    <figure>
     <table>
      <thead>
       <tr>
        <th>
         <span>
          <span>
           <span>
            <span>
             <img src="https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5ltPy9parAvTqLyPUPOVFDQ5f3iawq4oTBicXvq6bzPp98dSJ5Uh0TTYF4md8iaIaibv808Fap1KVicuwN5qvV7QHpIGXFWhao9hjhibIx7HlfvmRg/640?wx_fmt=svg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 115.75px !important;" />
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               AI 智能分析
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             深度语义理解
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               本地规则引擎
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             65+ 条 OWASP 规则 两种模式独立运行，互不干扰。
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span>
             <img src="https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM63l2pD8hBDaXoexQs9ysW3rZytd3Z99tGKQbJa4FhDoGC3rEvLGQqJYea3hp8yw6xwzfmbcBmiaUMZpMenMkRHQUYo5EskKJITQpf7wzgvGdA/640?wx_fmt=svg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 117px !important;" />
            </span>
           </span>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             DeepSeek · 通义千问 · 智谱 Kimi · 文心 · OpenAI Ollama · LM Studio（本地部署）。
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span>
             <img src="https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5GAibTMWlVOwfrLFXSK2JcM7x183D3iaNx2DePciaiak155bk79Ahe7630IWLoFv2MCfiaQLNPxtVXaOlrspyIFBLiclHFlpfBBhsagrBkp5gg2JsA/640?wx_fmt=svg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 124px !important;" />
            </span>
           </span>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             威胁检测 · 攻击会话 路径分析 · 地理定位 10 种科技感可视化图表 AIIP 全球地理定位溯源。
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span>
             <img src="https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM45a7J5LSt6RIpUJ2ESJouJNMTsx9wZKMPpz1BNBGYMtoaicz9Tia0IrYpKPy0nj9XXkIOpiczqdOaHNSNNHwHy7I6YDKNYjqXwiaOojWy1JhfcUw/640?wx_fmt=svg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 127px !important;" />
            </span>
           </span>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             DOCX Word 模板 PDF 完美中文渲染 一键导出，即用即发，拿来就能合规存档工作汇报。
            </span>
           </span>
          </span>
         </span>
        </th>
       </tr>
      </thead>
     </table>
    </figure>
    <h2 style="text-align: center;">
     <span>
      <code>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ◈
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        功能全景
       </span>
      </span>
     </span>
     <span>
      <code>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ◈
        </span>
       </span>
      </code>
     </span>
    </h2>
    <figure>
     <table>
      <thead>
       <tr>
        <th>
         <span>
          <span>
           <code>
            <span>
             <span style="font-size: 14px;">
              ⟁
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             分析引擎
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               AI 智能分析
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 深度语义理解，生成专业安全报告
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               本地规则引擎
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 65+ 条 OWASP CRS 规则，离线可用
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               双模式独立
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — AI 与本地分析互不干扰，独立报告
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               智能采样
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 按威胁评分优先选取样本，控制 Token 用量。
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <code>
            <span>
             <span style="font-size: 14px;">
              ⟁
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             数据分析面板
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               威胁检测面板
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — MITRE ATT&amp;CK 战术映射、CWE 漏洞关联
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               攻击会话面板
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 按 IP 分组攻击序列，展开查看原始日志
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               路径分析面板
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — URL 路径排行、攻击热力图、HTTP 方法分布
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               地理分析面板
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — GeoIP 世界地图、国家分布、IP 地理定位。
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
           <code>
            <span>
             <span style="font-size: 14px;">
              ⟁
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             可视化 &amp; 导出
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               ECharts 科技感图表
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 10 种图表，自适应缩放
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               攻击时间线
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 基于实际时间戳，自动格式化
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               DOCX 报告导出
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 专业 Word 模板，彩色风险标签
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               PDF 报告导出
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 完美中文渲染，自动分页。
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <code>
            <span>
             <span style="font-size: 14px;">
              ⟁
             </span>
            </span>
           </code>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             体验优化
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               7 种赛博朋克主题
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — Cyber 青 / 能量紫 / 矩阵绿 ...
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               字体大小可调
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 独立控制日志/报告/图表/面板字号
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               图表自适应
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — 字体缩放时图表自动调整尺寸和坐标
            </span>
           </span>
          </span>
          <span>
           <strong>
            <span>
             <span>
              <span style="font-size: 14px;">
               跨平台支持
              </span>
             </span>
            </span>
           </strong>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             — Windows / macOS / Linux 全平台覆盖。
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
      </tbody>
     </table>
    </figure>
    <h3 style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <span>
      <code>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ⬡
        </span>
       </span>
      </code>
     </span>
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        开屏界面
       </span>
      </span>
     </span>
    </h3>
   </section>
   <section style="text-align: left; margin-top: 16px;">
    <h3 style="margin-bottom: 0px; margin-top: 16px;">
     <span>
      <span>
       <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVicP5gEgaZfl3tFFJic3vaTKvXhfBuCanOdvHiceBVSO3JGE9FQ5g6QN7B1gUVdU7hSJAoB4bAOQH3IpdlPn9mEaKSPfnrhHR1iaQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 680px !important;" />
      </span>
     </span>
    </h3>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       AI 分析过程
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWrQs5Pvd67jicrSuAPZ2VpBwtuywTrYePb6erwx59Sl04MJKqmJo4HseutFmGLybfEX8r3xqCavudq8F28knYwWeUnv8rSGnBg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 680px !important;" />
    </section>
   </section>
   <section style="text-align: left; margin-top: 16px;">
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       AI 安全分析报告
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUrwKyU02Ttia4E3MIxab2Hz4IO6UrNxWKnB75vdQo7SE61tmf4WEPXvIPulomIy1X1E5zWEJ2hOEunxdb3CCK54n8K3muQpxMk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       本地规则分析
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXuNVdQJsaSgbTWvweW0EDrlf4iaciaP61jAhpdG51v8rRG7NOR3dtSJUGHzShbq8yxqFMnWE9omNdSJG3ZNRg2FYF4n0BTvTvlg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       本地分析报告
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAULRQv9kSAic6uqCEWQ33JWwMp2MeLibAZvrrAbqku3NcRHOKLAicseuOXzjRhSUc6qMY2kHgcF1l6LEOhzoibnM6nUu9FGUwGWWek/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       攻击分析面板
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXNGotYwYF4icVqcd7dXseYIIFATJicxakRLbGRvvJcXvQ8nFoaCyykMcj0Hib5r5dxwz6ASursfESRECr9u1fUezn8sxLiaJsRL7o/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       威胁检测面板
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWRPoiag6UXp9DzQd7klnq6GtFBxrIlUoeSaWHLvQ6mcDgF0fiasdL6ydGiczSiayX4Fzx8b1L8QAolSAxr8tT6TvtYagNqib9Ub9fM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       攻击会话面板
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXzHAUQh587JqrYjTqqD5vr7gx0B3WOk9ev68ZibNNByH7L810Ugicg5rWF1ufcUoDRUp1VDudU3iaMPQACIZW66zznyoTAYbWHdw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       可视化图表
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVW02Dwq1WzyH6pcXzBWKokrM7mlwBgfadRicTbZy6anic0ep15KOJ1pbLRcqdpcVQCTIEgiciaOFnTjjdNPNLJyukAfoibkXKc8nro/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       路径分析面板
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXxRQ5PkQDlF8Xiae5aicCKgpRRm6mcsW146ly2VoT8QsBiauibt0a1gqKYic12EfNGJDwL67GWUjX0ovzc52xPERhfUD3O96qWPia3E/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <code>
      <span>
       <span style="font-size: 16px;">
        ⬡
       </span>
      </span>
     </code>
     <span>
      <span style="font-size: 16px;">
       地理分析面板
      </span>
     </span>
    </h3>
    <section style="text-align: center; margin-bottom: 0px; margin-top: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXD0g3AhdrexicCicpTEyASurk1gia0Ag1bvNmTAx2NNhuH9MatAXHlkv971tMXDmmr51wlNwlPdOUDia7J1tRnwocLnrjNVia39wVc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="height: auto !important; width: 680px !important;" />
    </section>
    <h3 dir="auto" tabindex="-1">
     <span>
      <br />
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
    <pre class="code-snippet__js"><code><span>规则总数从 <span>52</span> 条扩展到 <span>130</span>+ 条，覆盖 <span>30</span> 个攻击类别</span></code><code><span>新增 <span>12</span> 个攻击类别：NoSQL 注入、LDAP 注入、XXE 注入、PHP 代码注入、Java 代码注入、GraphQL 注入、原型污染、会话固定、HTTP_PROXY 注入、XML-RPC 滥用、缓存投毒、HTTP 方法覆盖</span></code><code><span>SQL 注入规则增强至 <span>20</span> 条，覆盖 MySQL/MSSQL/PostgreSQL/SQLite 特有语法、WAF 绕过、认证绕过等</span></code><code><span>XSS 规则增强至 <span>15</span> 条，覆盖 CSS 表达式、<span>HTML</span> 实体绕过、mutation XSS、Cookie 窃取等</span></code><code><span>命令注入规则增强至 <span>15</span> 条，覆盖 Windows 命令、Base64 编码执行、Shellshock CVE-<span>2014</span>-<span>6271</span> 等</span></code><code><span>所有规则基于 OWASP CRS v4 标准，MITRE ATT&amp;CK 和 CWE 自动映射更新至 <span>2025</span> 版</span></code></pre>
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
    <section style="text-align: left; margin-top: 16px;">
     <section>
      <p style="text-indent: 0px; text-align: left; margin-bottom: 0px; margin-top: 0px;">
       <span>
        <span>
         <span style="font-size: 16px; font-weight: bold;">
          📦
         </span>
         <span style="font-size: 16px; font-weight: normal;">
          超详细安装与配置指南：从零到运行
         </span>
        </span>
       </span>
      </p>
      <h2>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         一、安装步骤
        </span>
       </span>
      </h2>
      <ul class="list-paddingleft-1">
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           根据你的系统下载 Windows /macOS/ Linux 对应安装包。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           Windows 直接双击安装；macOS 拖拽安装；Linux 运行 AppImage 即可打开，无需复杂配置。
          </span>
         </span>
        </section>
       </li>
      </ul>
      <h2>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         二、使用流程
        </span>
       </span>
      </h2>
      <ul class="list-paddingleft-1">
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           打开软件，点击导入日志，支持 log、txt、csv、json、ndjson 等常见日志格式。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           可选配置 AI 模型接口密钥，也可直接使用
          </span>
         </span>
         <strong>
          <span>
           <span style="font-size: 16px;">
            本地规则引擎
           </span>
          </span>
         </strong>
         <span>
          <span style="font-size: 16px;">
           离线检测。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           选择 AI 智能分析 或 本地规则分析，一键开始检测。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           自动生成分析报告、攻击时间线与各类可视化图表。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           支持 DOCX、PDF 一键导出报告，中文渲染完美，直接用于复盘和归档。
          </span>
         </span>
        </section>
       </li>
       <li>
        <section style="margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           可进入威胁、会话、路径、地理等数据分析面板，深度溯源攻击行为。
          </span>
         </span>
        </section>
       </li>
      </ul>
      <h2 dir="auto" style="margin-top: 16px; margin-bottom: 16px;" tabindex="-1">
       <span>
        <span style="font-weight: bold;">
         示例数据
        </span>
       </span>
      </h2>
      <table>
       <thead>
        <tr>
         <th align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             攻击类型
            </span>
           </span>
          </section>
         </th>
         <th align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             示例 Payload
            </span>
           </span>
          </section>
         </th>
         <th align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             OWASP 分类
            </span>
           </span>
          </section>
         </th>
        </tr>
       </thead>
       <tbody>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             SQL 注入
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <code>
           <span>
            <span style="font-size: 14px;">
             UNION SELECT
            </span>
           </span>
          </code>
          <section>
           <span>
            <span style="font-size: 14px;">
             , 盲注, 时间盲注
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A03
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             XSS 攻击
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             反射型, DOM 型, SVG 注入
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A03
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             目录遍历
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <code>
           <span>
            <span style="font-size: 14px;">
             ../../etc/passwd
            </span>
           </span>
          </code>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A01
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             命令注入
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <code>
           <span>
            <span style="font-size: 14px;">
             ; cat /etc/passwd
            </span>
           </span>
          </code>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A03
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             SSRF 攻击
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             内网元数据,
            </span>
           </span>
           <code>
            <span>
             <span style="font-size: 14px;">
              file://
             </span>
            </span>
           </code>
           <span>
            <span style="font-size: 14px;">
             协议
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A10
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             WebShell
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             蚁剑, 一句话木马
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A08
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             暴力破解
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             Hydra, 字典攻击
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A07
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             扫描探测
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             Nikto, sqlmap, Nmap
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             A05
            </span>
           </span>
          </section>
         </td>
        </tr>
        <tr>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             正常流量
            </span>
           </span>
          </section>
         </td>
         <td align="left">
          <section>
           <span>
            <span style="font-size: 14px;">
             搜索引擎蜘蛛, 正常用户访问
            </span>
           </span>
          </section>
         </td>
         <td align="center">
          <section>
           <span>
            <span style="font-size: 14px;">
             —
            </span>
           </span>
          </section>
         </td>
        </tr>
       </tbody>
      </table>
      <h2 style="text-align: left;">
       <span>
        <code>
         <span>
          <br />
         </span>
        </code>
       </span>
      </h2>
     </section>
    </section>
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
             2026POC更新至5932+
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
                 20260501
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
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
