---
title: "基于chromuim的源码定制的无痕hook定位算法"
url: "https://mp.weixin.qq.com/s/ImskjTZJgaygXXIfGT7aOw"
source: "安全狗的自我修养"
date: 2026-04-30
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了一种基于Chromium和CEF源码定制的无痕Hook定位算法，可实现无痕抓包、自动函数定位、参数提取及算法代码定位。该方案深度结合V8引擎源码进行改造，具备较高隐蔽性与精准性。作者指出当前实现已基本可用，但后续处理VMProtect等强混淆样本可能需更高算力支持，普通设备难以胜任。

---

<div class="image_content" id="js_image_content">
 <h1 class="rich_media_title">
  基于chromuim的源码定制的无痕hook定位算法
 </h1>
 <p>
  基于cef跟chromuim的v8源码定制的无痕抓包无痕hook、无痕自动定位算法、提取参数、获取算法代码定位。算ok了，还是不能偷懒得搞台服务器来干这个活。后面还有混淆 vmp的估计一般电脑干不动了。
  <img src="http://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/images/pic/pic_blank7db1df.gif" />
  <img src="http://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/images/pic/pic_blank7db1df.gif" />
  <img src="http://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/images/pic/pic_blank7db1df.gif" />
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
     昨天 18:02
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
