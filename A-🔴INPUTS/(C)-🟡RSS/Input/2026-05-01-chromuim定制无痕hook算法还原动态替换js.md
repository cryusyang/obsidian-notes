---
title: "chromuim定制无痕hook算法还原动态替换js"
url: "https://mp.weixin.qq.com/s/X0qF1R53LeRFFo8QO741Pw"
source: "安全狗的自我修养"
date: 2026-05-01
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了基于Chromium和CEF的V8引擎源码定制技术，实现了多项“无痕”能力，包括随机指纹生成、无痕抓包与Hook、自动定位算法等。  
支持动态提取JavaScript参数、定位并获取加密算法代码及返回值，具备运行时dump和替换JS代码的能力。  
还实现了动态dump V8字节码，为逆向分析和算法还原提供底层支持。

---

<div class="image_content" id="js_image_content">
 <h1 class="rich_media_title">
  chromuim定制无痕hook算法还原动态替换js
 </h1>
 <p>
  基于cef跟chromuim的v8源码定制已经实现随机指纹、无痕抓包、无痕hook、无痕自动定位算法、提取参数、获取算法代码定位、获取算法返回值、动态dumpjs代码、动态替换修改js代码、动态dump字节码。
  <img src="http://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/images/pic/pic_blank7db1df.gif" />
  <img src="http://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/images/pic/pic_blank7db1df.gif" />
  <br />
 </p>
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <div>
  <!-- -->
  <div class="wx_bottom_modal_wrp reward_dialog discuss_more_dialog_wrp weui-half-screen-dialog_wrp" tabindex="0">
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
        <!-- -->
        <div>
         <div class="author_profile-info">
          <div class="author_profile-info_avatar">
          </div>
          <div class="author_profile-info_main">
           <div class="author_profile-info_main_nickname" id="reward-dialog_author-main_name">
            名称已清空
           </div>
           <div class="author_profile-info_main_content" id="reward-dialog_author-main_head">
            <!-- -->
            <!-- -->
           </div>
           <div class="author_profile-info_main_content">
           </div>
          </div>
         </div>
         <div class="author_profile-pay_area">
          <span>
           <img />
           <strong>
            微信扫一扫赞赏作者
           </strong>
          </span>
          <div class="author_profile-pay_area_head">
           <span>
            喜欢作者
           </span>
           <a href="" tabindex="0">
            其它金额
           </a>
          </div>
          <div class="author_profile-pay_area_btns">
          </div>
          <div class="author_profile-pay_area_foot">
           <label>
            <div class="author_profile-pay_area_checkbox">
             <input class="weui-check" type="checkbox" />
             <i class="weui-icon-checked">
             </i>
            </div>
            <span>
             赞赏后展示我的头像
            </span>
           </label>
          </div>
         </div>
         <!-- -->
         <div class="author_profile-articles">
          <div class="author_profile-articles_title">
           作品
          </div>
          <div class="author_profile-articles_empty">
           暂无作品
          </div>
         </div>
         <div class="dialog-pay" style="display: none;">
          <div class="dialog-pay_body">
           <div class="dialog-pay_close weui-wa-hotarea">
            <div class="weui-icon-close-thin">
            </div>
           </div>
           <div class="dialog-pay_title">
            喜欢作者
           </div>
           <div class="reward-slider-container">
            <div class="reward-slider">
             <div class="reward-list-wrap">
              <div class="reward-list">
               <div class="dialog-pay__button">
                其它金额
               </div>
              </div>
             </div>
             <div class="reward-custorm">
              <label class="reward-input-area">
               <div class="reward-input-box">
                <span>
                 ¥
                </span>
                <input class="reward-input" style="width: 100px;" />
                <input class="reward-input" readonly="readonly" style="width: 100px; display: none;" />
               </div>
              </label>
              <div class="reward-input-hint">
               最低赞赏 ¥0
              </div>
              <div class="reward-button-wrap">
               <button class="weui-btn weui-btn_primary reward-operation-button weui-btn_disabled">
                确定
               </button>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </div>
       </div>
       <div class="weui-loadmore" style="display: none;">
        <i class="weui-loading">
        </i>
       </div>
      </div>
      <!-- -->
     </div>
     <div class="wx_bottom_modal_group">
      <div class="weui-half-screen-dialog__hd__wrp">
       <div class="weui-half-screen-dialog__hd">
        <div class="weui-half-screen-dialog__hd__side">
         <button class="weui-btn_icon weui-wa-hotarea">
          返回
          <i class="weui-icon-back-arrow-thin">
          </i>
         </button>
        </div>
        <div class="weui-half-screen-dialog__hd__main">
         <strong class="weui-half-screen-dialog__title">
          其它金额
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
        <div class="reward_custom">
         <div class="reward_custom-input_area">
          <div class="reward_custom-input_title">
           赞赏金额
          </div>
          <div class="reward_custom-input">
           <span>
            ¥
           </span>
           <span>
            <span>
            </span>
           </span>
           <span>
           </span>
          </div>
          <div class="reward_custom-tips">
           最低赞赏 ¥0
          </div>
         </div>
         <div class="reward_custom-keyboard">
          <div class="reward_custom-keyboard_number">
           <div class="reward_custom-keyboard_item" tabindex="0">
            1
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            2
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            3
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            4
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            5
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            6
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            7
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            8
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            9
           </div>
           <div class="reward_custom-keyboard_item double" tabindex="0">
            0
           </div>
           <div class="reward_custom-keyboard_item" tabindex="0">
            .
           </div>
          </div>
          <div class="reward_custom-keyboard_control">
           <div class="reward_custom-keyboard_item reward_custom-keyboard_del_btn" tabindex="0">
           </div>
           <div class="reward_custom-keyboard_item reward_custom-keyboard_submit_btn reward_custom-keyboard_submit_btn_disabled" tabindex="0">
           </div>
          </div>
         </div>
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
 </div>
 <!-- -->
 <!-- -->
 <!-- -->
 <!-- -->
 <div class="rich_media_tool">
  <div class="rich_media_info weui-flex policy_tips js_ad_policy_tips tips_global_primary claim_source_block">
   <!-- -->
  </div>
 </div>
 <!-- -->
 <div class="rich_media_meta_list rich_media_meta_list_combine image_rich_media_meta_list show_bottom_border">
  <div class="rich_media_meta_area_primary">
   <!-- -->
   <!-- -->
  </div>
  <div class="rich_media_meta_area_extra">
   <span>
    <span>
     湖南
    </span>
   </span>
   <span>
    ,
   </span>
   <span>
    <span>
     4小时前
    </span>
   </span>
   <span>
    ,
   </span>
   <span style="display: none;">
   </span>
   <!-- -->
  </div>
 </div>
</div>
