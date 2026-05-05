---
title: "Obsidian插件：Pandoc Extended Markdown 为 Obsidian 加入更多标记语法"
url: "https://mp.weixin.qq.com/s/_tmGNpDuLWsrGww5PwDmMA"
source: "PKMer知识社区"
date: 2026-03-14
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了Obsidian插件“Pandoc Extended Markdown”（作者ErrorTzy，版本1.4.9），该插件在Obsidian中实现了Pandoc扩展语法的部分功能，显著增强Markdown排版能力。主要特性包括：支持上标/下标、多种列表标识符（字母、罗马数字等）及自动重编号、可交叉引用的示例列表、定义列表、自定义标签（含占位符编号与跳转），以及集成式总览侧边栏（分类展示标签、示例列表、定义列表等内容并支持复制与定位）。所有功能需通过插件设置启用，部分高级功能（如自定义标签导出）还需配合Pandoc Lua Filter使用。

---

<section style="color: rgb(57, 57, 57); letter-spacing: 1px; padding-left: 15px; padding-right: 15px; line-height: 1.75; font-size: 14px; font-style: normal; font-weight: 400; text-align: justify; margin-bottom: 0px;">
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 100%;">
   <img src="https://mmbiz.qpic.cn/mmbiz_gif/dibCdrCystEVba6L4G4LqbCxqYVMJaMic1ZkbmmqEolq3axLyZZXGjVJdDo9a42RcpV8rFOpkXHBmhlN6k7GChTpUic7DGVSRgtTDjcWURMiccE/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <section>
  <section>
   <section style="text-align: justify; font-size: 12px; color: rgb(160, 160, 160); width: 100%;">
    <p style="white-space: normal; margin: 0px; padding: 0px;">
     <span>
      由于微信限制，
     </span>
     <span style="color: rgb(52, 54, 60); font-size: 14px;">
      <span>
       公众号文章内无法添加可跳转的外部链接
      </span>
     </span>
     <span>
      ，如果想要了解文内提到的更多信息，请点击文末的
     </span>
     <span>
      <span>
       阅读原文
      </span>
     </span>
     <span>
      ，查看本期内容
     </span>
    </p>
   </section>
  </section>
 </section>
 <section style="display: flex; text-align: left; margin: 10px 0px 20px;">
  <section style="display: inline-block; vertical-align: top; width: 5%; height: auto;">
   <section style="margin: 0px 0%; text-align: center; display: flex;">
    <section style="display: inline-block; width: 17px; vertical-align: top; height: auto; line-height: 0; background-color: rgb(57, 57, 57); border-width: 0px;">
     <section style="margin: 0px 0%; line-height: 0;">
      <section style="vertical-align: middle; display: inline-block; line-height: 0;">
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEVHdghCQVB1QOb4USNLtXdmxujrqLnVFCjXYM6Xh3JiaC1uYaaiaNYib75j6jC4OzPQT0u9Egx2SXkONBynJaj6oonDCTlONexex4/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(62, 62, 62); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section>
   <section style="font-size: 11px; color: rgb(252, 186, 101); text-align: center; line-height: 1; letter-spacing: 0px; padding: 0px 20px;">
    <p style="margin: 0px; padding: 0px;">
     <span>
      PKMer
     </span>
    </p>
   </section>
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(62, 62, 62); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0px 0%;">
    <section style="background-color: rgb(57, 57, 57); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: top; width: 4%; height: auto;">
   <section style="margin: 0px 0%; text-align: center; display: flex;">
    <section style="display: inline-block; width: 17px; vertical-align: top; height: auto; line-height: 0; background-color: rgb(57, 57, 57); border-width: 0px;">
     <section style="margin: 0px 0%; line-height: 0;">
      <section style="vertical-align: middle; display: inline-block; line-height: 0;">
       <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEWogl2VWFxUa7KPNgXUjoFFRbhf9g7Ds0mVmERFk3yibdJwQWWHPl8DouiaIqQSVERSISRsMRDNKnyIFaGoVj5wVVjKqjNhjKsJU/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="vertical-align: middle; width: 17px !important; height: auto !important;" />
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="text-align: center; font-size: 18px; color: rgb(169, 152, 255);">
  <p style="margin: 0px; padding: 0px;">
   <span>
    Obsidian插件：Pandoc Extended Markdown 为 Obsidian
   </span>
  </p>
  <p style="margin: 0px; padding: 0px;">
   <span>
    加入更多标记语法
   </span>
  </p>
 </section>
 <section style="margin-top: 10px; margin-bottom: 10px; text-align: center;">
  <section style="padding: 1px 0px;">
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
   <section>
    <section style="width: 100%; border: 1px solid rgb(160, 160, 160); padding: 10px;">
     <section style="text-align: justify; color: rgb(47, 200, 255);">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <span>
        插件信息
       </span>
      </p>
     </section>
     <section style="text-align: justify;">
      <ul class="list-paddingleft-2" style="padding-left: 20px;">
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件名称：Pandoc Extended Markdown
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件作者：ErrorTzy
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件版本：1.4.9（截止至26年3月14日）
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件概述：由 Pandoc 拓展的 Markdown 语法对 Markdown 语法来说可谓是一次巨大的加强，Pandoc Extended Markdown插件在 Obsidian 内实现了部分拓展语法，以期获得更丰富的排版体验。
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          插件项目地址：
         </span>
         <span style="text-decoration: underline 2px rgb(40, 102, 186); color: rgb(40, 102, 186);">
          <span>
           点我跳转
          </span>
         </span>
        </p>
       </li>
       <li>
        <p style="margin: 0px; padding: 0px;">
         <span>
          国内下载地址：
         </span>
         <span style="color: rgb(40, 102, 186); text-decoration: underline 2px rgb(40, 102, 186);">
          <span>
           下载安装
          </span>
         </span>
        </p>
       </li>
      </ul>
     </section>
    </section>
   </section>
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left-width: 5px; border-left-style: solid; border-left-color: rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <b>
     <span>
      基本用法
     </span>
    </b>
   </p>
  </section>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     实时预览模式：列表会政策渲染，除非光标正好位于某列表内，则该列表会处于源码状态
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     阅读模式：列表会完全渲染
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     源码模式：没有任何渲染
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     在 Strict Pandoc Mode 下，只有完全符合 Pandoc 规范的列表会被渲染
    </span>
   </p>
  </li>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     上标和下标
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    上标和下标在段落、列表以及定义列表中都可使用
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     语法示例
    </span>
   </strong>
   <span>
    ：
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
  <pre class="code-snippet__js"><code><span>水的分子式是 <span>H</span>~<span>2</span>~O，它是生命所必须的物质</span></code><code><span>爱因斯坦方程式 E = mc^<span>2</span>^ 给物理学带来了革命</span></code><code><span>化学反应式: Ca^<span>2</span>+^ + SO~<span>4</span>~^<span>2</span>-^ → CaSO~<span>4</span>~</span></code><code><span>如果要在上下标中加入空格，需要加入转义符， 下标空格示例： P~a\ <span>cat</span>~</span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    实现效果
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEUtqWysQZQ3GWX6WlqkBR6PeAkGW9PibeMDMIz7aB91DiaVibesr3icYlbZeHcHJ260pFCykFhQRuzhWagB2F4jBrgotkRvltORyTY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="font-size: 15px; color: rgb(47, 200, 255);">
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     加强列表
    </span>
   </strong>
  </p>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    可替换有序列表的默认标识符1. 2. 3.，按回车可按顺序自动补全标识符，如在插件设置中启用Auto-renumber lists，则当在列表中间按回车键时，会自动为标识符重新编号，仅对同一级别的列表生效，对缩进列表的上下级不生效
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     语法示例
    </span>
   </strong>
   <span>
    ：
   </span>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      大写字母：A. B. C.，如在插件设置中启用Strict Pandoc mode，则每个序号后要空两格
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      小写字母：a) b) c)
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      罗马数字：I. II. III.或i) ii) iii)
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      可以在源码模式中将#. 作为标识符，会被渲染成数字
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     实现效果
    </span>
   </strong>
   <span>
    ：
   </span>
  </p>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 50%; height: auto;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEXWBnee7GAT0qT7AkzF4aD6njjKr31rvzWxqNlGuBOGeZVCNJ2RVGxstLGxNLVQ2PhDKpjAanyqyCr8fTl5ericx8BOtFp8PMPE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="vertical-align: middle; width: 325px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      可交叉引用的示例列表
     </span>
    </span>
   </strong>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    按照格式创建示例列表后，后文只需录入括号及其内标签，鼠标悬停其上，即可查看引注的内容
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     语法示例
    </span>
   </strong>
   <span>
    ：
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
  <pre class="code-snippet__js"><code><span>(<span>@good</span>) 这是一个好例子。</span></code><code><span>(<span>@bad</span>) 这是一个坏例子。</span></code><code><span><br /></span></code><code><span>在后文中这样写即可引用： (<span>@good</span>) 和 (<span>@bad</span>)</span></code></pre>
 </section>
 <section>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在同一笔记文件内，括号中的标签将被自动替换为数字
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      注意：示例列表中要用英文括号，并在后半个括号后空一格，才会正确识别并渲染
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     实现效果
    </span>
   </strong>
   <span>
    ：
   </span>
  </p>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEWPN5GuoE2K8KrLBaHNOX8vBV9OsMvawmMGvFMkg8tw8qfJcVIt4U7z7RV1XSKa6BCO4oEuz8j3QrQ3ibvPrIVkk8mj4Wht7pjM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="vertical-align: middle; width: 567px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      定义列表
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在
     </span>
     <span>
      <span>
       :
      </span>
     </span>
     <span>
      或
     </span>
     <span>
      <span>
       ~
      </span>
     </span>
     <span>
      标识符后回车，下一行会自动补全与上一行相同的标识符
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在定义语句内，可以使用上标、下标、加粗（
     </span>
     <span>
      <span>
       **例**
      </span>
     </span>
     <span>
      ）和斜体（
     </span>
     <span>
      <span>
       *例*
      </span>
     </span>
     <span>
      ）
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     语法示例
    </span>
   </strong>
   <span>
    ：
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
   <li>
   </li>
   <li>
   </li>
  </ul>
  <pre class="code-snippet__js"><code><span>词目 1</span></code><code><span>:   词目 1 的定义 1，可以直接写在词目的下一行，不需要空行</span></code><code><span>    带缩进的段落也是定义 1 的一部分，在侧边栏列表中与上一行空一格接续</span></code><code><span><br /></span></code><code><span>词目 2</span></code><code><span><br /></span></code><code><span>~   波浪线也可作为定义列表的标识符</span></code><code><span>~   可包括多项定义，每项独立定义前都要加标识符</span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    实现效果
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWVVlCrhUXNiadzRgykmj9b4iblkflbWCDlcv0KcpdVoEroX6Z77ogic6SI1OmA0G7qWgI0MdKLicCQfeeD41cbNbrNhiciaibG2s6FpI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      自定义标签
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      本功能为插件特殊语法，需要在插件设置中启用
     </span>
     <span>
      <span>
       More extended syntax
      </span>
     </span>
     <span>
      ，此标签非彼标签（tag），插件文档原文用的是“label”
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在 Obsidian 内部可正确渲染，如果要使用 pandoc 进行转换，则需要在插件 github 仓库下
     </span>
     <span>
      <span>
       /lua_filter/CustomLabelList.lua
      </span>
     </span>
     <span>
      在 pandoc 中应用
     </span>
     <span>
      <span>
       lua filter
      </span>
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span>
     语法示例
    </span>
   </strong>
   <span>
    ：
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
  </ul>
  <pre class="code-snippet__js"><code><span>{::P} 人都是会死的。</span></code><code><span>{::Q} 苏格拉底是人。</span></code><code><span>{::R} 所以苏格拉底是会死的。</span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    实现效果
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEWctPIBlgssiaoahML2umHRSUyLqjz0JbHia2HCfiaBiceNicGtYEiabNRMGuicsAOOnZmW9Od2mIktpE6tCpaJKzohhIm2FN52O37nPc/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="vertical-align: middle; width: 462px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   每个自定义标签都支持通过占位符进行重新编号，例：(#name)，每个独一无二的占位符都会获得一个连续编码
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    语法示例
   </span>
  </strong>
  <span>
   ：
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
  </ul>
  <pre class="code-snippet__js"><code><span>{<span>::P</span>(<span>#first)} First premise</span></span></code><code><span>{<span>::P</span>(<span>#second)} Second premise  </span></span></code><code><span>{<span>::P</span>(<span>#first)'} Variation of first premise</span></span></code><code><span><br /></span></code><code><span><span>From</span> {<span>::P</span>(<span>#first)} and {::P(#second)}, we derive...</span></span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    实现效果
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEWeynLVUOicmh3g6R0iaDVUhrN4IULicKM8IKO2QYngaHOhRnIXibOm6tM5q7zrl1BxSaVSl9cUdCMvCGKJK0cBqJQE0YuIITBiaiaGw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="vertical-align: middle; width: 532px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   还可以使用纯占位符表达：
  </span>
 </p>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    语法示例
   </span>
  </strong>
  <span>
   ：
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
  </ul>
  <pre class="code-snippet__js"><code><span>{::(#premise)} <span>A</span> premise</span></code><code><span>{::(#conclusion)} <span>A</span> conclusion</span></code><code><span>{::(#premise)+(#conclusion)} Combined expression</span></code></pre>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <strong>
   <span>
    实现效果
   </span>
  </strong>
  <span>
   ：
  </span>
 </p>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEXbuWTRn8sFKVTcNfFEoY6tZy2tuWewCyJlBjRGicuxsPGXeo3DqoggwIJqIFRmfxzyHQSId76WmGGGGDeOWhXecFkUxXS3tRok/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="vertical-align: middle; width: 294px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      总览侧边栏
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    本插件可创建侧边栏页面，对当前笔记文件中存在的全部自定义标签、示例列表、定义列表和脚注进行列举以便总揽全局，类似于核心插件脚注列表的效果，但要更加丰富
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <br />
   </span>
  </p>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      自定义标签列表
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      展示当前笔记文件中的所有自定义标签
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      双栏布局：同时展示标签及其内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击标签，可复制标签及其内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击内容，可跳转至其在编辑器中所处的位置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      鼠标悬浮后文的标签上，则可显示精简过的全部内容
     </span>
    </p>
   </li>
  </ul>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEWHw695Ek7bBIrExiaF59icQVl72DbvstcINwnN2Lb5fiaj41REOLWmWZoC9wByQ0jkP7BP3GZFRZLYo032jTD5UfZdPJr7IQOFC8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      示例列表
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      展示当前笔记文件中的所有示例列表
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      三栏布局：同时展示编号、未经处理的标签及其内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      编号将按文中先后顺序排列，最多三位
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击标签，可复制标签，例：(good)
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击内容，可跳转至其在编辑器中所处的位置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      鼠标悬浮后文的标签上，则可显示精简过的全部内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      内容栏支持数学内容
     </span>
    </p>
   </li>
  </ul>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEU0DLFHOmEb6ke4DNagyYAwkcha7EFt76IVm91FRBrcCC7vv4qfqOjMkaCPHHbU67j8W7M891icGrace5YM9xIPjs3Od9Pxmm7A/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      定义列表
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      展示当前笔记文件中的所有定义列表
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      双栏布局：同时展示词目及其内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      定义支持 md 语法
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      同一词目下的多项定义将各自在最开始由圆点引导
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击定义，可跳转至词目在编辑器中所处的位置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      词目最多包含 100 个字符，定义最多包含 300 个字符
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      鼠标悬浮后文的定义上，则可显示精简过的全部内容
     </span>
    </p>
   </li>
  </ul>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEXenmRI296M0T2SUt2jZeeKOoQP9UX06cCABP5yzcjBGH8jXqGbbJzg1TdzQRRszOtfX0xsZVzs7RPXnyTfLTnTiatULZbUN98E/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <strong>
    <span style="font-size: 15px; color: rgb(47, 200, 255);">
     <span>
      脚注列表
     </span>
    </span>
   </strong>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      展示当前笔记文件中的所有脚注
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      双栏布局：同时展示脚注编号及其内容
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击脚注编号，可跳转至脚注编号在编辑器中所处的位置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      在侧边栏中点击定义，可跳转至脚注内容在编辑器中所处的位置
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      脚注列表使用和主编辑器一样的渲染逻辑：如果脚注包含 Markdown 语法，同样会被渲染，而不是显示为源码
     </span>
    </p>
   </li>
  </ul>
 </section>
 <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
  <section style="vertical-align: middle; display: inline-block; line-height: 0;">
   <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEUhYHYxruQTngBicVX5WEFDGVszibhiatv2K4SbNlibz1VHPHYb5UbTpAXMz2GZrLxlsFPYfrcxIejqW2ibSF2JpXsic7EqQ2dkeib3ibw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="vertical-align: middle; width: 650px !important; height: auto !important;" />
  </section>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      设置说明
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <span>
     Strict Pandoc Mode
    </span>
   </span>
   <span>
    ：如启用，则必须严格遵循 Pandoc 语法规范
   </span>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      列表前后必须空行
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      大写字母后必须空两格
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      不符合负规范的列表将不会被渲染，而是以纯文本的形式展示
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <span>
     Auto-renumber lists
    </span>
   </span>
  </p>
  <ul class="list-paddingleft-2" style="padding-left: 20px;">
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      如启用，则在列表中间插入新列表项时，会自动重排之后的标识符编号
     </span>
    </p>
   </li>
   <li>
    <p style="margin: 0px; padding: 0px;">
     <span>
      加强列表的标识符编号也会被重排，但仅影响英文字母和罗马字母，对#.或实例列表不生效
     </span>
    </p>
   </li>
  </ul>
  <p style="white-space: normal; margin: 0px; padding: 0px;">
   <span>
    <span>
     More extended syntax
    </span>
   </span>
   <span>
    ：如启用，则启用插件特殊语法，[[#自定义标签|详见上文]]
   </span>
  </p>
 </section>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="text-align: left; display: flex; margin: 15px 0px; width: 100%; border-left: 5px solid rgb(108, 171, 255); padding: 0px 0px 0px 8px; height: auto;">
  <section style="font-size: 16px; color: rgb(108, 171, 255); width: 100%;">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      快捷命令
     </span>
    </strong>
   </p>
  </section>
 </section>
 <ul class="list-paddingleft-2" style="padding-left: 20px;">
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Check pandoc formatting
     </span>
    </span>
    <span>
     : 扫描当前笔记文件，报告任何存在的语法错误
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Format document to pandoc standard
     </span>
    </span>
    <span>
     : 自动将当前笔记文件中的列表转换成符合 Pandoc 规范的形式
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Toggle definition list bold style
     </span>
    </span>
    <span>
     : 将当前笔记文件中定义列表的条目在加粗和不加粗之间进行切换
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Toggle definition list underline style
     </span>
    </span>
    <span>
     : 将当前笔记文件中定义列表的条目在下划线和无下划线之间进行切换
    </span>
   </p>
  </li>
  <li>
   <p style="margin: 0px; padding: 0px;">
    <span>
     <span>
      Open list panel
     </span>
    </span>
    <span>
     ：打开总览侧边栏
    </span>
   </p>
  </li>
 </ul>
 <p style="white-space: normal; margin: 0px; padding: 0px;">
  <span>
   <br />
  </span>
 </p>
 <section style="margin-top: 10px; margin-bottom: 10px; text-align: center;">
  <section style="padding: 1px 0px;">
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
   <section>
    <section style="width: 100%; border: 1px solid rgb(160, 160, 160); padding: 10px;">
     <section style="text-align: justify; color: rgb(47, 200, 255);">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <span>
        讨论
       </span>
      </p>
     </section>
     <section style="text-align: justify;">
      <p style="white-space: normal; margin: 0px; padding: 0px;">
       <span>
        若阁下有独到的见解或新颖的想法，诚邀您在文章下方留言，与大家共同探讨。
       </span>
      </p>
     </section>
    </section>
   </section>
   <section style="width: 100%; height: 3px;">
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section>
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
    <section style="clear: both;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
 </section>
 <section style="margin: 15px 0px 20px;">
  <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
   <p style="margin: 0px; padding: 0px;">
    <strong>
     <span>
      - THE END -
     </span>
    </strong>
   </p>
  </section>
 </section>
 <section style="display: flex; width: 100%;">
  <section style="height: auto;">
   <section>
    <section style="display: inline-block; width: auto; vertical-align: bottom; height: auto; padding: 0px 0px 0px 4px;">
     <section style="display: grid; width: 100%; overflow: hidden; line-height: 1.6; font-size: 16px; letter-spacing: 0px; color: rgb(0, 0, 0);">
      <section>
       <section>
        <section style="display: inline-block; width: 100%; vertical-align: middle; border-style: dashed; border-width: 0px 0px 2px; border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(57, 57, 57); height: auto;">
         <section style="margin: 0px 0%;">
          <section style="border-top: 1px dashed transparent;">
           <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
           </svg>
          </section>
         </section>
        </section>
       </section>
      </section>
      <section style="display: flex;">
       <svg height="100%" viewBox="0  0 349 31" width="100%" xmlns="http://www.w3.org/2000/svg">
        <svg height="61.15%" width="45.1776%" x="-5.55034%" xmlns="http://www.w3.org/2000/svg" y="26.7512222195471%">
         <foreignObject height="100%" width="100%">
          <section style="font-size: 7px; height: 100%;">
           <section style="font-size: 12px; color: rgb(52, 54, 60); text-align: center;">
            <p style="margin: 0px; padding: 0px;">
             <span style="color: rgb(255, 202, 0);">
              <span>
               //
              </span>
             </span>
             <span style="color: rgb(255, 202, 0);">
              <span>
              </span>
             </span>
             <span>
              <span>
               长按二维码·加入我们
              </span>
             </span>
            </p>
           </section>
          </section>
         </foreignObject>
        </svg>
       </svg>
      </section>
      <section style="padding-top: 9%;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
     <section style="display: flex;">
      <section style="display: inline-block; vertical-align: middle; width: 25%; height: auto; border-style: dashed solid dashed dashed; border-width: 0px;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/dibCdrCystEWuLsiaBEF1oznurveWEWicnx2AF5iaZMnadB8v2LNeRXjusxNmf0AreqypJBnEPMYU4FA7msIYwcJ605gqrCmbvHI9HjKR3V2nWA/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
        </section>
       </section>
       <section>
        <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
         <p style="margin: 0px; padding: 0px;">
          <span>
           QQ群
          </span>
         </p>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: top; width: 2%; height: auto;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 25%; height: auto;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/dibCdrCystEXEYOrJBGvah0IYDBOvXNhA8Zvh4nLMYNIic1ibDCnj8rXre5PcjFvrhrHMl6xH65ZkicLricRPgJSt0fkPnwkib1jt7myAdB06QWkw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="vertical-align: middle; width: 161.5px !important; height: auto !important;" />
        </section>
       </section>
       <section>
        <section style="text-align: center; font-size: 12px; color: rgb(160, 160, 160);">
         <p style="margin: 0px; padding: 0px;">
          <span>
           微信群
          </span>
         </p>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 5%; height: auto;">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: auto; height: auto; padding: 0px 0px 0px 16px;">
       <section style="text-align: center; margin-top: 10px; margin-bottom: 10px; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0;">
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/dibCdrCystEVnZpZ4v8FhWkuM4ibNpCGrJVzvaJSKziaO6Z6ATzMI2bILSevKzXzPnKpXfmRJN8lxjQouIV6yjrMvChBmDRG2kA02Rww6st39Y/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="vertical-align: middle; width: 261.796875px !important; height: auto !important;" />
        </section>
       </section>
      </section>
     </section>
     <section>
      <section style="display: inline-block; vertical-align: middle; width: 49%; border-style: dashed; border-width: 0px 0px 2px; border-color: rgb(0, 0, 0) rgb(0, 0, 0) rgb(57, 57, 57); height: auto;">
       <section style="margin: 0px 0%;">
        <section style="border-top: 1px dashed transparent;">
         <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
         </svg>
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 17%; height: auto;">
       <section style="text-align: center; margin: 0px 0%; line-height: 0;">
        <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 61%; height: auto;">
         <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/dibCdrCystEWFsdPoDaRzdXrgEI9v1p2PLIJeggiaLiaQI7eLNU0f49npIdOAvQwQBFrcxnp5GeeEsqdovFAiaQtBsR4rJIutlqAahd4LKcMBec/640?wx_fmt=gif&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="vertical-align: middle; width: 66.984375px !important; height: auto !important;" />
        </section>
       </section>
      </section>
      <section style="display: inline-block; vertical-align: middle; width: 31%; border-width: 0px 0px 2px; border-style: dashed; border-bottom-color: rgb(57, 57, 57); height: auto;">
       <section style="margin: 0px 0%;">
        <section style="border-top: 1px dashed transparent;">
         <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
         </svg>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section>
  <section style="display: grid; width: 100%; overflow: hidden; line-height: 1.6; font-size: 16px; letter-spacing: 0px; color: rgb(0, 0, 0);">
   <section style="display: flex;">
    <svg height="100%" viewBox="0  0 353 68" width="100%" xmlns="http://www.w3.org/2000/svg">
     <svg height="84.43%" width="42.1123%" x="57.3167%" xmlns="http://www.w3.org/2000/svg" y="-1.91416364471241%">
      <foreignObject height="100%" width="100%">
       <section style="height: 100%; font-size: 13px;">
        <section style="font-size: 12px; color: rgb(160, 160, 160); text-align: center;">
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong style="letter-spacing: 0px;">
           <span>
            作者
           </span>
          </strong>
          <span style="letter-spacing: 0px;">
           <span>
            ：血海狂屠
           </span>
          </span>
         </p>
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong>
           <span>
            来源
           </span>
          </strong>
          <span>
           ：PKMer.cn
          </span>
         </p>
         <p style="text-align: left; margin: 0px; padding: 0px;">
          <strong>
           <span style="letter-spacing: 0px;">
            <span>
             排版
            </span>
           </span>
          </strong>
          <span style="letter-spacing: 0px;">
           <span>
            ：Wis_Ocean
           </span>
          </span>
         </p>
        </section>
       </section>
      </foreignObject>
     </svg>
    </svg>
   </section>
   <section>
    <section style="text-align: center; line-height: 0; font-size: 9px; height: 100%;">
     <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 85%; height: auto;">
      <img src="https://mmbiz.qpic.cn/mmbiz_png/dibCdrCystEVOsHnejVcCm32wicdWWa3K3UMXT744xesM0jEv2bh2vXUFqcticEicicg3zxpsnrhxIRSD2GVH6Q5AmS1IBb3aCRkLdjXcKuYrmYw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="vertical-align: middle; width: 256.90625px !important; height: auto !important;" />
     </section>
    </section>
   </section>
   <section>
    <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
    </svg>
   </section>
  </section>
 </section>
 <section style="margin: 0px 0%;">
  <section style="border-top: 1px dashed transparent;">
   <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
   </svg>
  </section>
 </section>
 <section style="text-align: left; display: flex; margin: 0px 0px 10px;">
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="display: flex;">
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(227, 163, 92);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center; margin: 0px;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(255, 222, 110);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
    <section style="display: inline-block; vertical-align: top; width: auto; height: auto; padding: 0px 3px; line-height: 0;">
     <section style="text-align: center;">
      <section style="display: inline-block; width: 10px; height: 10px; vertical-align: top; overflow: hidden; border-width: 0px; border-radius: 100%; border-style: none; border-color: rgb(57, 57, 57); background-color: rgb(255, 236, 196);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto; padding: 0px 10px;">
   <section style="font-size: 10px; letter-spacing: 2px; color: rgb(57, 57, 57);">
    <p style="margin: 0px; padding: 0px;">
     <span>
      点击阅读原文查看更多
     </span>
    </p>
   </section>
  </section>
  <section style="display: inline-block; vertical-align: middle; width: auto; height: auto;">
   <section style="margin: 0.5em 0px;">
    <section style="background-color: rgb(57, 57, 57); height: 1px;">
     <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
     </svg>
    </section>
   </section>
  </section>
 </section>
</section>
<p style="display: none;">
 
 
</p>
