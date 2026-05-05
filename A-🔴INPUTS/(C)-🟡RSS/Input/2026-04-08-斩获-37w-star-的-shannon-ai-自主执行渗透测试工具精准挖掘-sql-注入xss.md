---
title: "斩获 37W Star 的 Shannon AI 自主执行渗透测试工具，精准挖掘 SQL 注入、XSS 等 OWASP 高危漏洞"
url: "https://mp.weixin.qq.com/s/8VbLFvxwJ2zkIKGtaZJdag"
source: "渗透安全HackTwo"
date: 2026-04-08
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Shannon 是由 Keygraph 开发的白盒 AI 渗透测试工具，主打自主运行、代码感知与动态验证结合，可精准识别并利用 SQL 注入、XSS、SSRF 等 OWASP 高危漏洞。其采用多智能体架构，分五阶段（预备侦察、侦察、漏洞分析、漏洞利用、报告生成）全自动完成测试，支持双因素认证绕过、浏览器自动化及并行漏洞验证，并仅报告已复现的漏洞以降低误报率。工具分为开源版 Shannon Lite（AGPL-3.0）和商业版 Shannon Pro，依赖 Docker、Node.js 及 Anthropic 等 AI 模型凭证，支持 npx 一键部署。

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
           Shannon 是由 Keygraph 开发的一款自主运行的白盒 AI 渗透测试工具，斩获 37W Star，专为 Web 应用程序和 API 设计。它可分析源代码、识别攻击向量，主动执行真实漏洞利用（如 SQL 注入、XSS 等 OWASP 高危漏洞），验证漏洞有效性，一键完成安全审计，填补常规年度渗透测试的安全缺口，避免漏洞流入生产环境。
          </span>
         </span>
        </span>
       </span>
      </span>
     </span>
    </p>
    <section style="text-align: center;">
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVlcnzbv0ibPFdIKEjeG6iaKvE3qk5TRVPR9DibiaqeWs74QY421m4brojNEXl058Sbk3nPH1DoPWM5eBn3C2pgtUOeucrsar9obU0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
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
    ✨
   </span>
   核心功能特性
  </span>
 </p>
 <span>
 </span>
</section>
<ul class="list-paddingleft-1">
</ul>
<section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
 <section>
  <section style="margin-top: 16px; margin-bottom: 16px; text-align: left;">
   <section>
    <ul class="list-paddingleft-1">
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         完全自主运行
        </span>
       </span>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         ：
        </span>
        <span style="font-size: 16px;">
         只需一条命令即可启动完整渗透测试，自动处理双因素认证/TOTP 登录（含单点登录）、浏览器导航、漏洞利用及报告生成，无需人工干预。
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWWZyxnZ55oUMpDS5j43eOYlXZutC1eK0sxONRemSZw39aZZ3xpbNQiaiayKiaNgwZqbeuickqfibxxRO9GeSXwdweI4yVF6qdA7vI0/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          可复现的概念验证漏洞利用
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：最终报告仅包含已证实可利用的漏洞，并提供可直接复制粘贴的概念验证代码，无法利用的漏洞不予报告，最大限度降低误报率。
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWuZ5NYoIY98kAndKdLYicLBnT8HdIdWQM22ewRsv8WVQEWLibgw7ooyfGhDmcODgibI11ZqNH0EFmj6PsOtshUn0TyKcXWUahibN4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 680px !important;" />
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          OWASP 漏洞覆盖
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：可识别并验证注入攻击、XSS、SSRF（服务器端请求伪造）、身份验证/授权失效等高危漏洞，更多漏洞类别正在开发中。
        </span>
       </span>
      </p>
     </li>
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          代码感知动态测试
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：先分析源代码以指导攻击策略，再通过实时浏览器和基于命令行的漏洞利用程序，对运行中的应用程序进行验证，兼顾代码深度与实战性。
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWj9IO0IIBnmXnx79sRsfiaECuf0ESXm5vEam7sFve5pRHDfjnyp1Juf3sXd4CJic5fbtYM7F5cSTeBicJKlWr3GQZLBedHUcwrUo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 680px !important;" />
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          集成安全工具
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：在侦察和发现阶段集成 Nmap、Subfinder、WhatWeb 和 Schemathesis 等主流安全工具，提升攻击面扫描的全面性。
        </span>
       </span>
      </p>
     </li>
     <li style="font-size: 16px;">
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          并行处理
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：漏洞分析和利用阶段可在所有攻击类别中同时运行，大幅提升测试效率。
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWCGiabAPicqaA0I46hicN8ibEJsrQwKnz6zQ5icgXZYn2f9zqxKGxGRWONLXUjJCAY8txLiaRO0fBCcNOth8sqBYQtJehyFMsB6JXKM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 680px !important;" />
     </span>
    </p>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       🔥
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       产品线区分
      </span>
     </span>
    </h3>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span style="font-size: 16px;">
       Shannon 分为两个版本，适配不同使用场景，核心差异如下：
      </span>
     </span>
    </p>
    <table style="border: none; border-collapse: collapse; width: 500px;">
     <thead>
      <tr style="height: 39px;">
       <th style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top; font-weight: 500; background-color: rgb(242, 243, 245);">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           版本
          </span>
         </span>
        </p>
       </th>
       <th style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top; font-weight: 500; background-color: rgb(242, 243, 245);">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           许可证
          </span>
         </span>
        </p>
       </th>
       <th style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top; font-weight: 500; background-color: rgb(242, 243, 245);">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           最适合场景
          </span>
         </span>
        </p>
       </th>
      </tr>
     </thead>
     <tbody>
      <tr style="height: 39px;">
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           Shannon Lite（开源版）
          </span>
         </span>
        </p>
       </td>
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           AGPL-3.0
          </span>
         </span>
        </p>
       </td>
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           本地测试自己的应用程序，适合个人开发者
          </span>
         </span>
        </p>
       </td>
      </tr>
      <tr style="height: 39px;">
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           Shannon Pro
          </span>
         </span>
        </p>
       </td>
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           商业许可
          </span>
         </span>
        </p>
       </td>
       <td style="border: 1px solid rgb(222, 224, 227); font-size: 10pt; padding: 8px; vertical-align: top;">
        <p style="margin-bottom: 16px; margin-top: 16px;">
         <span>
          <span style="font-size: 16px;">
           需要单一应用安全平台
          </span>
         </span>
        </p>
       </td>
      </tr>
     </tbody>
    </table>
    <section style="margin-bottom: 16px; margin-top: 16px;">
     <span style="width: 680px !important; height: 395px !important; overflow: hidden;">
      <div id="page-content">
       <!--S 全屏播放 full_screen_mv-->
       <div id="js_mpvedio_wrapper_wxv_4462306371631267842" style="height: 100%;">
        <div class="add_bg_color appmsg_video">
         <div class="video_tail_module video_screen_half" id="js_video_tail_panel_wxv_4462306371631267842" style="display: none;">
          <div class="video_tail_module__hd" id="js_video_tail_hd">
           <div class="account_info_wrp">
            <div class="profile_info_wrp js_go_profile">
             <img />
             <div class="account_name" id="js_tail_panel_account_name">
             </div>
             <div class="subscription_info subscription_success">
              <div class="account_subscription_tips js_subscription_success" id="js_subscription_success" style="display: none;">
               已关注
              </div>
              <i class="account_link_icon js_profile_icon" id="js_profile_icon">
              </i>
             </div>
            </div>
            <div class="btn_account_subscription js_btn_account_subscription" id="js_btn_account_subscription" style="display: none;">
             关注
            </div>
           </div>
           <div class="opr_wrp">
            <span>
             <i class="opr_item refresh_icon">
             </i>
             <span>
              重播
             </span>
            </span>
            <span style="display: none;">
             <i class="opr_item share_icon">
             </i>
             <span>
              分享
             </span>
            </span>
            <!--点赞后 加className selected-->
            <span style="display: none;">
             <i class="opr_item like_icon">
             </i>
             <span>
              赞
             </span>
            </span>
            <!-- <span class="opr_item_wrp recommend_item_wrp" id="js_tail_channel_button"               style="display: none;">               <i class="opr_item video-logo_icon"></i>               <span class="opr_item_text">随便看看</span>             </span> -->
           </div>
          </div>
          <!-- 有拓展内容 -->
          <div class="have_expand" id="js_expand_area">
          </div>
          <!-- 广告内容 -->
          <div class="ad_area" id="js_tail_video_ad_area">
          </div>
         </div>
        </div>
        <div class="feed-wrapper">
         <div class="wx_bottom_modal_wrp player_relate_video_dialog weui-half-screen-dialog_fold" style="display: none;" tabindex="0">
          <div class="wx_bottom_modal_mask_fixed">
          </div>
          <div class="weui-mask wx_bottom_modal_mask">
          </div>
          <div class="weui-half-screen-dialog wx_bottom_modal">
           <div class="wx_bottom_modal_group_container">
            <div class="wx_bottom_modal_group">
             <div class="weui-half-screen-dialog__hd__wrp">
              <div class="weui-half-screen-dialog__hd">
               <div class="weui-half-screen-dialog__hd__side">
                <button class="weui-btn_icon weui-wa-hotarea">
                 关闭
                 <i class="weui-icon-half-screen-close">
                 </i>
                </button>
               </div>
               <div class="weui-half-screen-dialog__hd__main">
                <strong class="weui-half-screen-dialog__title">
                 观看更多
                </strong>
               </div>
               <div class="weui-half-screen-dialog__hd__side">
                <!-- -->
                <button class="weui-btn_icon weui-wa-hotarea" style="display: none;">
                 更多
                 <i class="weui-icon-more">
                 </i>
                </button>
               </div>
              </div>
             </div>
             <div class="weui-half-screen-dialog__bd" id="contentAreaWrp">
              <div class="weui-loadmore" style="display: none;">
               <i class="weui-loading">
               </i>
              </div>
              <div class="wx_bottom_modal_msg_wrp" style="display: none;">
               <div class="wx_bottom_modal_msg">
                <i class="weui-loading">
                </i>
               </div>
              </div>
              <div class="weui-loadmore weui-loadmore_line weui-loadmore_dot" style="display: none;">
               <span>
               </span>
              </div>
              <div class="">
               <ul class="player_relate_video_list" id="js_player_relate_video_list">
               </ul>
               <div class="weui-loadmore weui-loadmore_default weui-loadmore_line weui-loadmore_dot player_video_list_end_line">
                <span>
                </span>
               </div>
              </div>
              <div class="weui-loadmore" style="display: none;">
               <i class="weui-loading">
               </i>
              </div>
             </div>
             <!-- -->
            </div>
           </div>
          </div>
         </div>
         <div class="js_video_fullscreen_profile video_full-screen__head video_full-screen__head_fixed">
          <div class="video_full-screen__head__inner">
           <div class="video_full-screen__head__body">
            <div class="js_video_fullscreen_profile_exit video_full-screen__head__item">
             <div class="video_full-screen__article-title">
              <button class="weui-wa-hotarea js_video_fullscreen_profile_exit reset_btn video_close_fullscreen_btn">
               <i class="weui-icon-close">
                退出全屏
               </i>
              </button>
             </div>
            </div>
           </div>
           <div class="video_full-screen__head__ft">
            <a class="video_menu_more js_video_fullscreen_menu_more weui-wa-hotarea_before" href="">
             <i class="weui-icon-outlined-more">
             </i>
            </a>
           </div>
          </div>
         </div>
         <div class="infinity-list__wrapper" style="height: 383px;">
          <div class="" style="height: 383px; overflow: visible;">
           <div class="infinity-list__page destory-enter-to" style="height: 383px;">
            <div class="mp-video-player" style="height: 100%;">
             <div class="js_mpvedio page_video_wrapper" id="js_mpvedio_1777687144563_563111259567">
              <div class="js_page_video page_video ratio_primary align_upper_center page_video_without-control page_video_skin-normal" style="display: block; width: 100%; height: 383px;">
               <svg class="border_filler border_filler_lefttop" height="4px" viewBox="0 0 2 2" width="4px" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.85.005A2 2 0 000 2V0h2z" fill="#ffffff" fill-rule="evenodd">
                </path>
               </svg>
               <svg class="border_filler border_filler_righttop" height="4px" viewBox="0 0 2 2" width="4px" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.85.005A2 2 0 000 2V0h2z" fill="#ffffff" fill-rule="evenodd">
                </path>
               </svg>
               <svg class="border_filler border_filler_rightbot" height="4px" viewBox="0 0 2 2" width="4px" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.85.005A2 2 0 000 2V0h2z" fill="#ffffff" fill-rule="evenodd">
                </path>
               </svg>
               <svg class="border_filler border_filler_leftbot" height="4px" viewBox="0 0 2 2" width="4px" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.85.005A2 2 0 000 2V0h2z" fill="#ffffff" fill-rule="evenodd">
                </path>
               </svg>
               <div class="js_video_fullscreen_profile video_full-screen__head" style="display: none;">
                <div class="video_full-screen__head__inner">
                 <div class="video_full-screen__head__body">
                  <div class="js_video_fullscreen_profile_exit video_full-screen__head__item">
                   <div class="video_full-screen__article-title">
                    <button class="weui-wa-hotarea js_video_fullscreen_profile_exit reset_btn video_close_fullscreen_btn" style="display: none;">
                     <i class="weui-icon-back-arrow">
                      切换到竖屏全屏
                     </i>
                    </button>
                    <button class="weui-wa-hotarea js_video_fullscreen_profile_exit reset_btn video_close_fullscreen_btn" style="display: none;">
                     <i class="weui-icon-close">
                      退出全屏
                     </i>
                    </button>
                    <div class="video_full-screen__account" style="display: none;">
                     <div class="video_full-screen__account-info">
                      <span>
                      </span>
                      <span>
                       渗透安全HackTwo
                      </span>
                      <button class="reset_btn video_profile_follow_btn weui-wa-hotarea" style="display: none;" type="button">
                       已关注
                      </button>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                 <div class="video_full-screen__head__ft">
                  <a class="video_menu_more js_video_fullscreen_menu_more weui-wa-hotarea_before" href="" style="display: none;">
                   <i class="weui-icon-outlined-more">
                   </i>
                  </a>
                 </div>
                </div>
               </div>
               <div class="js_share_btn_contain top_screen_opr video_share_opr" style="display: none;">
                <div class="wx_video_share_area">
                 <button class="js_share_btn wx_video_share_btn weui-wa-hotarea" type="button">
                  分享视频
                 </button>
                </div>
               </div>
               <div class="wrp_loading js_loading" style="display: none;">
                <span>
                 <span>
                 </span>
                </span>
               </div>
               <div class="poster_cover">
               </div>
               <div class="full_screen_opr wx_video_play_opr">
                <button class="mid_play_box reset_btn" type="button">
                 <i class="pic_mid_play">
                 </i>
                 <span>
                  ，时长
                 </span>
                 <span>
                  00:16
                 </span>
                </button>
               </div>
               <!-- -->
               <div class="top_screen_opr wx_video_flow_wrap" style="display: none;">
                <div class="wx_video_flow">
                 <p>
                 </p>
                </div>
               </div>
               <div class="mid_opr fast_pre_next" style="display: none;">
                <div class="video_processor_bar">
                 <div class="processor_bar_inner js_forward_bar" style="width: 0%;">
                 </div>
                </div>
                <p>
                 <span>
                  0
                 </span>
                 <span>
                  /
                 </span>
                 <span>
                  0
                 </span>
                </p>
               </div>
               <div class="wx_video_progress_msg full_screen_opr" style="display: none;">
                <div class="wx_video_progress_msg_inner">
                 <span>
                  00:00
                 </span>
                 <span>
                  /
                 </span>
                 <span>
                  00:16
                 </span>
                </div>
               </div>
               <div class="video_fullscreen_mask" style="display: none;">
               </div>
               <div class="video_screen_mode_switch">
                <button class="reset_btn video_screen_mode_switch_btn weui-wa-hotarea" type="button">
                 切换到横屏模式
                </button>
               </div>
               <div class="full_screen_opr wx_video_pause_full_mod" style="display: none;">
                <button class="reset_btn wx_video_pause_full_btn" type="button">
                 继续播放
                </button>
               </div>
               <input class="aria_hidden_abs" title="显示工具栏" type="checkbox" />
               <div class="js_control video_opr video_opr_normal padding_play_bar">
                <div class="opr_inner">
                 <div class="opr_inner_fl">
                  <div class="js_play_bar_wrapper wrp_play_bar wrp_play_bar_hide_speed-dot" style="display: none;">
                   <div class="js_progress_bar wrp_progress" style="padding-top: 6px; padding-bottom: 0px;">
                    <div class="progress_bar">
                     <div class="background_bar">
                     </div>
                     <div class="js_played_bar played_bar" style="width: 0%;" title="按住可调">
                      <span>
                       进度条，百分之0
                      </span>
                     </div>
                     <div class="js_buffer_bar buffer_bar" style="width: 0%;">
                     </div>
                     <!-- -->
                     <div class="weui-wa-hotarea js_played_speed_cnt wrp_speed_dot">
                      <i class="speed_dot">
                      </i>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
               <div class="js_control video_opr video_opr_sns" style="display: none;">
                <div class="opr_inner">
                 <div class="opr_inner_fl">
                  <div class="js_switch weui-wa-hotarea switch switch_on">
                   <a class="btn_opr" href="">
                    播放
                   </a>
                  </div>
                  <div>
                   <div class="played_time js_now_play_time">
                    00:00
                   </div>
                   <span>
                    /
                   </span>
                   <div class="total_time js_total_time">
                    00:16
                   </div>
                  </div>
                  <!-- -->
                  <div class="total_time js_total_time" style="display: none;">
                   00:16
                  </div>
                 </div>
                 <div class="opr_inner_fr">
                  <!-- -->
                  <!-- -->
                  <!-- -->
                  <div class="weui-wa-hotarea js_full_screen_control screenSize_control full">
                   <i class="icon_control">
                    全屏
                   </i>
                  </div>
                 </div>
                </div>
               </div>
               <div class="js-toast weui-toast weui-toast_text" style="display: none;">
                <p>
                </p>
               </div>
               <div class="full_screen_opr video_quick_play_context" style="display: none;">
                <div class="video_quick_play_msg">
                 <i class="icon_video_quick_play">
                 </i>
                 倍速播放中
                </div>
               </div>
               <div class="js_sub_setting video_full-screen__footer video_full-screen__footer__sub-setting hide">
                <div class="video_full-screen__sub-setting video_full-screen__sub-setting__speed js_playback_mode_select" style="display: none;">
                 <a class="video_full-screen__sub-setting__item js_playback_0" href="">
                  0.5倍
                 </a>
                 <a class="video_full-screen__sub-setting__item js_playback_1" href="">
                  0.75倍
                 </a>
                 <a class="video_full-screen__sub-setting__item current js_playback_2" href="">
                  1.0倍
                 </a>
                 <a class="video_full-screen__sub-setting__item js_playback_3" href="">
                  1.5倍
                 </a>
                 <a class="video_full-screen__sub-setting__item js_playback_4" href="">
                  2.0倍
                 </a>
                </div>
                <div class="video_full-screen__sub-setting video_full-screen__sub-setting__ratio js_play_mode_select" style="display: none;">
                 <a class="video_full-screen__sub-setting__item current js_resolution_0" href="">
                  超清
                 </a>
                 <a class="video_full-screen__sub-setting__item js_resolution_1" href="">
                  流畅
                 </a>
                </div>
               </div>
               <div class="js_inner inner not_fullscreen">
                <div class="js_video_poster video_poster">
                 <div class="video_mask">
                 </div>
                 <video class="video_fill" poster="http://mmbiz.qpic.cn/mmbiz_jpg/ibrevicNauKAU867bExdians12k6RQvoT4nJiaxSFWW0xm3eQoDfbLOicibkmVTRUqG6qtbYfX3TvSVXFOf71V1hGbiaCLrcfHJz3iczicniaeLEC6fOY/0?wx_fmt=jpeg&amp;wxfrom=16" preload="metadata" src="https://mpvideo.qpic.cn/0bc3eqcgmaaeluajq2wqcruvijgdmysaizqa.f10102.mp4?dis_k=829d6155c4a14001c767b9260f796f21&amp;dis_t=1777687141&amp;play_scene=10120&amp;auth_info=TsSP3ZspYlhwl6qowXEmRUlvNmBMODdLP0pJfTxQBUN0bDMJOAB5FQcyYGQUHitlXWU=&amp;auth_key=7ad8d5e41036f01dc3e6ab924a50ed9b&amp;vid=wxv_4462306371631267842&amp;format_id=10102&amp;support_redirect=0&amp;mmversion=false" style="display: block; width: 680px; height: 383px;">
                  您的浏览器不支持 video 标签
                 </video>
                </div>
                <div class="video_poster__info__play" style="display: none;">
                 <i class="">
                 </i>
                </div>
                <div class="video_poster__info" style="display: none;">
                 <p style="font-size: 17px;">
                  继续观看
                 </p>
                 <p style="font-size: 12px;">
                  斩获 37W Star 的 Shannon AI 自主执行渗透测试工具，精准挖掘 SQL 注入、XSS 等 OWASP 高危漏洞
                 </p>
                </div>
                <div class="video_poster__info__mask" style="width: 100%; display: none;">
                </div>
               </div>
               <div class="video_profile_area" style="display: none;">
                <div>
                 <button class="reset_btn video_profile_relate_video_btn js_wx_tap_highlight wx_tap_link" style="display: none;">
                  观看更多
                  <i class="weui-icon-filled-arrow video_profile_relate_video_btn_arrow">
                  </i>
                 </button>
                </div>
                <div style="width: fit-content;" tabindex="0">
                 <div class="weui-wa-hotarea video_profile_desc_wrp">
                  <div class="icon_appmsg_tag_wrp" style="display: none;">
                   <div class="icon_appmsg_tag">
                    转载
                   </div>
                  </div>
                  <div class="weui-hidden_abs">
                   ,
                  </div>
                  <div class="video_profile_desc">
                   斩获 37W Star 的 Shannon AI 自主执行渗透测试工具，精准挖掘 SQL 注入、XSS 等 OWASP 高危漏洞
                  </div>
                  <i class="weui-icon-outlined-arrow video_profile_desc_arrow">
                  </i>
                 </div>
                </div>
                <div class="video_profile_wrp weui-flex">
                 <div class="video_profile weui-flex weui-flex__item">
                  <span>
                  </span>
                  <span>
                   渗透安全HackTwo
                  </span>
                  <button class="reset_btn video_profile_follow_btn weui-wa-hotarea" style="display: none;" type="button">
                   已关注
                  </button>
                 </div>
                 <div class="video_sns_context" style="display: none;">
                  <button class="video_sns_btn video_sns_btn_share" style="display: none;" type="button">
                   <span>
                    分享
                   </span>
                  </button>
                  <button class="video_sns_btn video_sns_btn_praise" title="" type="button">
                   <span>
                    点赞
                   </span>
                  </button>
                  <button class="video_sns_btn video_sns_btn_love" title="" type="button">
                   <span>
                    在看
                   </span>
                  </button>
                 </div>
                 <div class="like_comment_wrp" style="display: none;">
                  <div class="like_comment_inner">
                   <div class="like_comment_bd">
                    <div class="like_comment_tips">
                     <i class="weui-icon-success">
                     </i>
                     <i class="icon-success-primary">
                     </i>
                     已同步到看一看
                     <a class="like_comment_share_link weui-wa-hotarea_before" href="">
                      写下你的评论
                     </a>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
              </div>
             </div>
             <div style="display: none;">
              <div class="weui-mask_transparent">
              </div>
              <div class="weui-toast">
               <i class="weui-icon-success-no-circle weui-icon_toast">
               </i>
               <p>
               </p>
              </div>
             </div>
             <div class="fullscreen-screenshot__layer" style="background-color: rgb(0, 0, 0); display: none;">
             </div>
             <div class="fullscreen-screenshot__layer">
             </div>
            </div>
           </div>
          </div>
         </div>
         <!-- -->
        </div>
       </div>
       <!--E 视频播放器-->
       <!-- S 视频社交-->
       <div class="interact_video" id="bottom_bar" style="display: none; height: 35px;">
        <div class="inter_opr">
         <a class="access_original" href="" id="video_detail_btn" target="_blank">
          视频详情
         </a>
        </div>
       </div>
      </div>
     </span>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       🧠
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       架构优势
      </span>
     </span>
    </p>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span style="font-size: 16px;">
       Shannon 采用多智能体架构，结合白盒源代码分析与动态漏洞利用，分五个阶段完成渗透测试，确保测试深度与准确性：
      </span>
     </span>
    </p>
    <ol class="list-paddingleft-1" start="1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          预备侦察
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：使用 Nmap、Subfinder、WhatWeb 进行外部扫描，获取目标基础设施和技术栈指纹；同时执行源代码分析，识别应用框架、入口点和潜在攻击面。
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          侦察
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：基于预备侦察结果构建全面的攻击面地图，通过浏览器自动化探索应用程序，关联代码级洞察与实际运行行为，梳理所有入口点、API 端点和身份验证机制。
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          漏洞分析
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：5个并发代理并行工作，针对不同 OWASP 漏洞类别（注入、XSS、身份验证等）搜索潜在漏洞，生成可利用路径假设。
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          漏洞利用
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：专用漏洞利用代理尝试对假设路径执行真实攻击，严格遵循“无法利用则不报告”原则，排除误报。
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <strong>
        <span>
         <span style="font-size: 16px;">
          报告生成
         </span>
        </span>
       </strong>
       <span>
        <span style="font-size: 16px;">
         ：汇总所有已验证漏洞，生成专业可操作的报告，包含可复现的概念验证代码，聚焦已证实的安全风险。
        </span>
       </span>
      </p>
     </li>
    </ol>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWIteSSIgAUehvF5sxPhTVRgINicBibZxpwvflMW6Bc8B4QaWGsMNpGlNofcviad0K7sYEVL2knxqDd3EMCujcdVojVjK8YlMEkfQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 680px !important;" />
     </span>
    </p>
    <ol class="list-paddingleft-1" start="1">
    </ol>
    <h2>
     <span>
      <br />
     </span>
     <span>
     </span>
    </h2>
    <section>
     <p>
      <span>
       <span>
        <span>
         <br />
        </span>
       </span>
      </span>
     </p>
     <p style="border-bottom: 1px solid rgb(227, 227, 227); height: 32px; line-height: 18px;">
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
    <pre class="code-snippet__js"><code><span>新增 npx CLI，支持 monorepo、CI/CD 集成和临时工作节点架构，简化部署与使用流程。</span></code><code><span>添加 claude-<span>code</span>-router 支持，可对接多模型测试（实验性），支持 OpenAI、OpenRouter、DeepSeek 等替代 AI 提供商。</span></code><code><span>新增可配置输出目录（<span>--output</span> 参数），支持自定义报告保存路径。</span></code><code><span>支持可配置的管道重试和并发设置，适配不同 AI 订阅计划的速率限制。</span></code><code><span>新增自定义基础 URL 支持，可对接任何与 Anthropic 兼容的端点（代理、网关等）。</span></code><code><span>新增 Google Vertex AI 支持，可通过 GCP 服务账号授权使用，同时完善 AWS Bedrock 集成，支持多 AI 提供商切换。</span></code><code><span>新增命名工作区和工作区列表功能，支持中断测试的恢复，无需重新运行已完成的代理。</span></code><code><span>扩展注入分析范围，覆盖 LFI/RFI（本地/远程文件包含）、SSTI（服务器端模板注入）、路径遍历、反序列化等漏洞。</span></code></pre>
   </section>
   <section style="margin-bottom: 16px; text-align: left; margin-top: 16px;">
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
          安装流程
         </span>
        </span>
       </span>
      </p>
     </section>
    </section>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        1.前提条件（必须先安装）
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        Docker
       </span>
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       （必装）
      </span>
     </span>
    </p>
    <ol class="list-paddingleft-1">
     <ul class="list-paddingleft-1">
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           官方下载：
          </span>
         </span>
        </span>
        <span>
         <span>
          <span style="font-size: 16px;">
           https://www.docker.com/products/docker-desktop
          </span>
         </span>
        </span>
       </p>
      </li>
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           Windows / macOS 用 Docker Desktop，Linux 用 Docker Engine。
          </span>
         </span>
        </span>
       </p>
      </li>
     </ul>
    </ol>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        Node.js 18 或更高版本
       </span>
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       （npx 方式必备）
      </span>
     </span>
    </p>
    <ol class="list-paddingleft-1">
     <ul class="list-paddingleft-1">
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           推荐使用 nvm 或官网安装最新 LTS 版。
          </span>
         </span>
        </span>
       </p>
      </li>
     </ul>
    </ol>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        pnpm
       </span>
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       （仅本地克隆构建时需要）
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>npm install -<span>g</span> pnpm</span></code></pre>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        AI 模型凭证
       </span>
      </span>
     </span>
     <span>
      <span style="font-size: 16px; font-weight: bold;">
       （必须有一个）
      </span>
     </span>
    </p>
    <ol class="list-paddingleft-1">
     <ul class="list-paddingleft-1">
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           Claude Code OAuth Token
          </span>
         </span>
        </span>
       </p>
      </li>
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           AWS Bedrock
          </span>
         </span>
        </span>
       </p>
      </li>
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           Google Vertex AI
          </span>
         </span>
        </span>
       </p>
      </li>
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           （实验性）OpenAI / OpenRouter
          </span>
         </span>
        </span>
       </p>
      </li>
     </ul>
     <ul class="list-paddingleft-1">
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <strong>
          <span>
           <span>
            <span style="font-size: 16px;">
             推荐
            </span>
           </span>
          </span>
         </strong>
        </span>
        <span>
         <span>
          <span style="font-size: 16px;">
           ：Anthropic API Key（Claude 系列模型） 在
          </span>
         </span>
        </span>
        <span>
         <span>
          <span style="font-size: 16px;">
           https://console.anthropic.com/
          </span>
         </span>
        </span>
        <span>
         <span>
          <span style="font-size: 16px;">
           获取
          </span>
         </span>
        </span>
       </p>
      </li>
      <li>
       <p style="margin-bottom: 16px; margin-top: 16px;">
        <span>
         <span>
          <span style="font-size: 16px;">
           其他支持：
          </span>
         </span>
        </span>
       </p>
      </li>
     </ul>
    </ol>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        2. 最推荐方式：使用 npx 一键安装运行（无需克隆仓库）
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        这是官方最推荐、最简单的方式。
       </span>
      </span>
     </span>
    </p>
    <h4 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        步骤 1：配置凭证（只需做一次）
       </span>
      </span>
     </span>
    </h4>
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
     <pre class="code-snippet__js"><code><span><span># 交互式向导（推荐）</span></span></code><code><span>npx @keygraph/shannon setup</span></code><code><span><span># 或者直接设置环境变量</span></span></code><code><span><span>export</span> ANTHROPIC_API_KEY=sk-ant-你的密钥</span></code></pre>
    </section>
    <h4 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        步骤 2：启动渗透测试
       </span>
      </span>
     </span>
    </h4>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
      <li>
      </li>
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span><span>npx</span> <span>@keygraph</span>/shannon start \</span></code><code><span>  -u https://你的目标网址 \</span></code><code><span>  -r /绝对路径/到/你的代码仓库</span></code></pre>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          示例
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>npx <span>@keygraph</span><span>/shannon start -u http://localhost:3000 -r /</span><span>Users</span><span>/你的用户名/</span>project<span>/</span>my<span>-</span>app</span></code></pre>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          本地开发环境常用写法
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        （Docker 容器无法直接访问 localhost）：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>npx <span>@keygraph</span><span>/shannon start -u http://host.docker.internal:3000 -r /</span>path<span>/to/</span>your<span>-</span>repo</span></code></pre>
    </section>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        3. 高级方式：克隆仓库本地构建（适合想修改代码或离线使用）
       </span>
      </span>
     </span>
    </h3>
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
     <pre class="code-snippet__js"><code><span><span># 1. 克隆仓库</span></span></code><code><span>git <span>clone</span> https://github.com/KeygraphHQ/shannon.git</span></code><code><span><span>cd</span> shannon</span></code><code><span><span># 2. 配置凭证（两种方式任选其一）</span></span></code><code><span><span># 方式A：创建 .env 文件</span></span></code><code><span><span>cat</span> &gt; .<span>env</span> &lt;&lt; <span>'EOF'</span></span></code><code><span>ANTHROPIC_API_KEY=你的密钥</span></code><code><span>CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000</span></code><code><span>EOF</span></code><code><span><span># 方式B：直接导出环境变量</span></span></code><code><span><span>export</span> ANTHROPIC_API_KEY=<span>"你的密钥"</span></span></code><code><span><span>export</span> CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000</span></code></pre>
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
    </ul>
    <pre class="code-snippet__js"><code><span><span># 3. 安装依赖并构建</span></span></code><code><span><span>pnpm</span> install</span></code><code><span>pnpm build</span></code><code><span><span># 4. 启动测试</span></span></code><code><span>./shannon start -u https://你的目标网址 -r /你的代码仓库路径</span></code></pre>
   </section>
   <section style="margin-bottom: 16px; text-align: left; margin-top: 16px;">
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        4. 常用命令（npx 方式）
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
            <span style="font-size: 14px;">
             功能
            </span>
           </span>
          </span>
         </span>
        </th>
        <th>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             命令
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
            <span style="font-size: 14px;">
             查看日志
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon logs
            </span>
           </span>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             &lt;workspace&gt;
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
            <span style="font-size: 14px;">
             查看状态
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon status
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
            <span style="font-size: 14px;">
             打开监控界面
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             浏览器打开
            </span>
           </span>
          </span>
          <span>
           <span>
            <span style="font-size: 14px;">
             http://localhost:8233
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
            <span style="font-size: 14px;">
             停止运行
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon stop
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
            <span style="font-size: 14px;">
             彻底清理
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon stop --clean
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
            <span style="font-size: 14px;">
             卸载
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon uninstall
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
            <span style="font-size: 14px;">
             列出所有工作区
            </span>
           </span>
          </span>
         </span>
        </td>
        <td>
         <span>
          <span>
           <span>
            <span style="font-size: 14px;">
             npx @keygraph/shannon workspaces
            </span>
           </span>
          </span>
         </span>
        </td>
       </tr>
      </tbody>
     </table>
    </figure>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        5. 工作区（Workspace）与断点续跑
       </span>
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          每次运行都会自动创建一个工作区（例如 example-com_shannon-1771007534808）
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          想
         </span>
        </span>
       </span>
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            断点续跑
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          只需加上 -w 工作区名称
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          示例：
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
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
    <pre class="code-snippet__js"><code><span><span># 首次运行（命名）</span></span></code><code><span>npx @keygraph/shannon start -u https://example.com -r ./repo -w 我的审计项目</span></code><code><span><span># 以后继续运行相同任务（自动跳过已完成部分）</span></span></code><code><span>npx @keygraph/shannon start -u https://example.com -r ./repo -w 我的审计项目</span></code></pre>
   </section>
   <section style="margin-bottom: 16px; text-align: left; margin-top: 16px;">
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        6. 高级配置（推荐创建配置文件）
       </span>
      </span>
     </span>
    </h3>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        复制模板：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span><span>cp</span> configs/example-config.yaml ./my-config.yaml</span></code></pre>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        编辑 my-config.yaml（支持登录、2FA、黑白名单等）：
       </span>
      </span>
     </span>
    </p>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        YAML
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
     <pre class="code-snippet__js"><code><span><span># Optional: describe your target environment (max 500 chars)</span></span></code><code><span>description: <span>"Next.js e-commerce app on PostgreSQL. Local dev environment — .env files contain local-only credentials, not deployed to production."</span></span></code><code><span>authentication:</span></code><code><span>  login_type: form</span></code><code><span>  login_url: <span>"https://your-app.com/login"</span></span></code><code><span>  credentials:</span></code><code><span>    username: <span>"test@example.com"</span></span></code><code><span>    password: <span>"yourpassword"</span></span></code><code><span>    totp_secret: <span>"LB2E2RX7XFHSTGCK"</span>  <span># Optional for 2FA</span></span></code><code><span>  login_flow:</span></code><code><span>    - <span>"Type </span><span><span>$username</span></span><span> into the email field"</span></span></code><code><span>    - <span>"Type </span><span><span>$password</span></span><span> into the password field"</span></span></code><code><span>    - <span>"Click the 'Sign In' button"</span></span></code><code><span>  success_condition:</span></code><code><span>    <span>type</span>: url_contains</span></code><code><span>    value: <span>"/dashboard"</span></span></code><code><span>rules:</span></code><code><span>  avoid:</span></code><code><span>    - description: <span>"AI should avoid testing logout functionality"</span></span></code><code><span>      <span>type</span>: path</span></code><code><span>      url_path: <span>"/logout"</span></span></code><code><span>  focus:</span></code><code><span>    - description: <span>"AI should emphasize testing API endpoints"</span></span></code><code><span>      <span>type</span>: path</span></code><code><span>      url_path: <span>"/api"</span></span></code></pre>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        使用配置文件运行：
       </span>
      </span>
     </span>
    </p>
    <section>
     <ul class="code-snippet__line-index code-snippet__js">
      <li>
      </li>
     </ul>
     <pre class="code-snippet__js"><code><span>npx @keygraph/shannon start -u https://example.com -r ./repo -c ./my-config.yaml</span></code></pre>
    </section>
    <section style="text-align: left;">
     <h3 style="margin-bottom: 16px; margin-top: 16px;">
      <span>
       <span>
        <span style="font-size: 16px; font-weight: bold;">
         7. 平台特殊说明
        </span>
       </span>
      </span>
     </h3>
    </section>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Windows 用户
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          强烈推荐使用
         </span>
        </span>
       </span>
       <span>
        <strong>
         <span>
          <span>
           <span style="font-size: 16px;">
            WSL2 + Ubuntu
           </span>
          </span>
         </span>
        </strong>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          （最稳定）
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          或者用 Git  + Docker Desktop
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          macOS / Linux
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          直接使用即可。
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          测试本地应用
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          用
         </span>
        </span>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          http://host.docker.internal
         </span>
        </span>
       </span>
       <span>
        <span>
         <span style="font-size: 16px;">
          :端口 代替 localhost
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          Windows Defender 误报
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        ：
       </span>
      </span>
     </span>
    </p>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          报告里的 PoC 代码可能被杀毒软件误报，建议把 Shannon 目录加入排除列表。
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <h3 style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px; font-weight: bold;">
        8. 输出位置
       </span>
      </span>
     </span>
    </h3>
    <ul class="list-paddingleft-1">
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          npx 方式：~/.shannon/workspaces/
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          本地构建方式：./workspaces/
         </span>
        </span>
       </span>
      </p>
     </li>
     <li>
      <p style="margin-bottom: 16px; margin-top: 16px;">
       <span>
        <span>
         <span style="font-size: 16px;">
          最终报告文件：deliverables/comprehensive_security_assessment_report.md
         </span>
        </span>
       </span>
      </p>
     </li>
    </ul>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <span>
       <span style="font-size: 16px;">
        完成测试后，报告里只包含
       </span>
      </span>
     </span>
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          已成功利用
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        的漏洞，并附带可直接复制的 PoC。
       </span>
      </span>
     </span>
    </p>
    <p style="margin-bottom: 16px; margin-top: 16px;">
     <span>
      <strong>
       <span>
        <span>
         <span style="font-size: 16px;">
          安装完成！
         </span>
        </span>
       </span>
      </strong>
     </span>
     <span>
      <span>
       <span style="font-size: 16px;">
        现在你可以直接运行第一条命令开始渗透测试了：
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
     </ul>
     <pre class="code-snippet__js"><code><span><span>npx</span> <span>@keygraph</span>/shannon setup</span></code><code><span>npx <span>@keygraph</span>/shannon start -u http://你的网址 -r /你的代码路径</span></code></pre>
    </section>
    <section style="text-align: left; margin-top: 16px; margin-bottom: 16px;">
     <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUqHEK60FaaoCXLQTwLu5SIETgffmTT49oBUXeLyibkaC2qwtzLa1rpN86DuiciadKulXGn3x99ShxmLibPcqHibsgYeAYDlh6JG9Ls/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 680px !important;" />
    </section>
    <section>
     <span>
      <br />
     </span>
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
             2026POC更新至5832+
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
            🤙截止目前已有2700+多位师傅选择加入
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
                 20260408
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
      <img src="https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAU4ZkjJvWUibxdPYrmw6yu1YbAEzdcrbaJ2q7wuia4JzJM0Q5NUJ0vJZlAKxibia7Ca8WSMFP8kbjJYFUPd2rAtiaEHLY4fLV06icXxE/640?wx_fmt=png&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="letter-spacing: 0.578px; background-color: rgb(222, 175, 74); width: 149.796875px !important; overflow: hidden; display: block; height: auto !important;" />
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
