---
title: "CPUID 被攻陷！CPU-Z/HWMonitor 被植入木马"
url: "https://mp.weixin.qq.com/s/0WXE98SSbUVG47j51PzcsA"
source: "骨哥说事"
date: 2026-04-13
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文揭露了2024年4月CPUID官网遭黑客入侵、导致官方下载的CPU-Z和HWMonitor被植入STX RAT远控木马的重大供应链攻击事件。攻击者通过篡改官网下载链接（而非伪造签名）、利用DLL侧加载、五阶段内存无文件执行等技术，成功绕过HTTPS、数字签名和传统杀软防护，精准 targeting 运维、安全及IT技术人员等高价值目标。该事件凸显了“可信来源”不再绝对安全，供应链攻击正日趋工业化和隐蔽化，对个人与企业安全构成严重威胁。

---

<h1>
 <span>
  <br />
 </span>
</h1>
<section style="margin-bottom: 0px;">
 <span>
  
  
 </span>
</section>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span style="letter-spacing: 0.544px; background-color: rgb(255, 251, 0);">
  <strong>
   <span>
    <br />
   </span>
  </strong>
 </span>
</p>
<h1>
 <span style="letter-spacing: 0.544px; background-color: rgb(255, 251, 0);">
  <strong>
   <span>
    防走失：
   </span>
  </strong>
  <strong>
   <span style="color: rgb(0, 82, 255);">
    <span>
     https://gugesay.com/
    </span>
   </span>
  </strong>
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   不想错过任何消息？设置星标
  </span>
 </strong>
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   ↓ ↓ ↓
  </span>
 </strong>
</p>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="text-align: center; margin-bottom: 0px;">
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="width: 247px !important; height: auto !important;" />
 </span>
</p>
<section>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgMsSricjKA1JmmIfwKLhTfOib2icLAQll7jk2oNhfARWAFFWG2LYyMlWe2k9vP6uIA3icd6bU4YF5MibqXFB2qAxJBlXy14zeibyuTw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 660px !important;" />
 </section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <br />
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你上一次打开CPU-Z是什么时候？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   查CPU型号、测内存频率、还是装完新机器跑个分？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个工具太常见了——常见到没人会怀疑它。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但就在今年4月，炸锅的事情发生了：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     CPUID官方网站被黑，你从官网下载的CPU-Z和HWMonitor，里面藏着远控木马。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   不是第三方镜像，不是盗版网站。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   是你亲手敲进浏览器、看着HTTPS小锁、没有任何安全警告的
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    官方网站
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   中招的用户里，有你吗？
  </span>
 </p>
 <hr style="height: 1px; margin: 10px 0px; border-width: 1px medium medium; border-style: solid none none; border-color: black currentcolor currentcolor; border-image: none;" />
 <h2 style="padding: 12px 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; margin: 70px 30px 30px; border: 1px solid rgb(0, 0, 0);">
  <span>
   <span>
    官方站点被投毒：一场持续19小时的安全噩梦
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   根据多家安全媒体的报道，事件的经过大致是这样的：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   4月9日深夜，攻击者悄无声息地入侵了CPUID的官网后台。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0px; line-height: 26px; color: black; font-size: 14px;">
  <span>
   接下来的19个小时里，所有从官网下载CPU-Z和HWMonitor的用户，拿到的安装包已经不是“原版”了。
  </span>
 </p>
 <section style="text-align: center;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgyyr8DzWtUgJXUhGziamQkyhicicoCy4k6WoHfvJGicXew2fsJEm4QE9YexFue2AjEZpQukVypomaWKadNictOYnzEkPxFKbxgyWbo/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 660px !important;" />
 </section>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   <br />
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   The Hacker News的报道这样描述：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “攻击者替换了官方下载链接，用户下载到的是包含恶意代码的木马版本。”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   注意一个细节——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    攻击的时间窗口是4月9日到4月10日，大约持续了19小时。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   19个小时。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   按照CPU-Z的下载量估算，这段时间内可能有数万甚至更多用户中招。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   更讽刺的是，这两款工具的用户群体极其特殊——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   运维工程师、系统管理员、硬件发烧友、安全研究员……
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    全是有“高权限”的技术人员。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   黑客不是随便选的武器。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   他们是有目的性的。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    攻击是怎么做到的？拆解供应链攻击的“四步绝杀”
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   很多人觉得，官网被黑这种事离自己很远。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但看完这次攻击的技术细节，你会发现它比想象中更隐蔽、更狡猾。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全公司Cyderes发布了一份详细的技术分析，把攻击链条拆解得清清楚楚。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第一步：绕过“信任防线”——篡改下载接口，不碰签名文件
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   传统的防伪手段是什么？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    数字签名。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   软件发布时用私钥签名，用户下载后验签名，确保“拿到手的和作者发布的是同一个文件”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   很多安全策略基于这个假设：签名没被篡改，就说明软件是安全的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但这次攻击偏偏绕开了这道防线——
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    官方说明中明确指出：
   </span>
   <strong style="font-weight: bold; color: black;">
    <span>
     签名文件本身没有被篡改
    </span>
   </strong>
   <span>
    。
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   攻击者没有动安装包本身。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   他们动的是
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    下载接口
   </span>
  </strong>
  <span>
   ——在后台悄悄替换了下载链接，用户请求时返回的是恶意版本。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    你校验签名，签名是对的。但你校验的，根本不是你要下载的那个文件。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这招釜底抽薪，直接让“信任签名”这个动作本身变成了安慰剂。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第二步：经典DLL侧载——用Windows的“默认规则”藏木马
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   恶意安装包被下载到用户电脑后，并不会直接“露头”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   它用的是一种叫
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    DLL Sideloading
   </span>
  </strong>
  <span>
   的技术。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   具体来说：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     安装目录下被植入了一个恶意的
    </span>
    <code>
     <span>
      cryptbase.dll
     </span>
    </code>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     正常程序启动时，Windows会按特定顺序搜索DLL
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     恶意DLL被优先加载，代码悄然执行
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Tom's Hardware的报道提到了这个技术细节：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “攻击者利用了Windows的DLL搜索顺序机制，在合法程序目录下放置恶意动态链接库，实现隐蔽加载。”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这不是什么高深漏洞——这是Windows用了二十年的“默认行为”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    合法软件、合法路径、合法签名。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    但里面藏着一把刀。
   </span>
  </strong>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第三步：五阶段内存执行——杀软基本“瞎了”
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   如果攻击只是把木马写入硬盘，传统杀软大概率能拦下来。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但攻击者更狠——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   恶意代码分为
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    五个阶段执行
   </span>
  </strong>
  <span>
   ，全部在内存中运行，
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    不落盘
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   什么意思？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你的硬盘扫描、文件系统监控，在这一步完全失效。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   恶意代码像“幽灵”一样穿过系统，等杀软反应过来，攻击者早就完成使命、擦干净痕迹了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   Cyderes的技术报告中专门提到了这一点：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “多阶段执行的恶意代码全程驻留于内存，传统终端防护产品难以检测。”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    没有文件就没有特征码。没有特征码，AI模型也抓瞎。
   </span>
  </strong>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   第四步：STX RAT上线——你的机器彻底失控
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   经过前几步的铺垫，木马终于露出真面目。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   它加载的是一款叫
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    STX RAT
   </span>
  </strong>
  <span>
   的远程控制木马——这玩意儿能干的事情太多了：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     窃取浏览器保存的密码（Chrome、Edge、Firefox……全中）
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     截取Cookie，
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      绕过双因素认证登录你的账号
     </span>
    </strong>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     扫描本地加密货币钱包地址
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     抓取VPN、FTP、SSH凭证
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     远程控制，上传下载文件，执行任意命令
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   用一句话总结：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     一旦中招，你电脑里的所有秘密、所有权限、所有资产，攻击者都可以染指。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这不是普通的病毒——这是一把能开你家所有门的万能钥匙。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    为什么说本次事件“极其严重”？三个原因
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   技术细节说完了，为什么这件事值得你认真对待？
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   1️⃣ 命中“高价值人群”——攻击者不傻
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   CPU-Z和HWMonitor的用户是什么人？
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     运维工程师
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     安全研究员
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     硬件工程师
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     IT管理人员
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这群人有一个共同特点：
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    他们的电脑里往往有服务器凭证、VPN权限、数据库密码、业务后台……
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   普通用户中招，顶多丢个游戏账号。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   技术人员中招，可能直接威胁到
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    整个公司的基础设施
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全公司Cyderes的分析明确指出：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “攻击者的目标群体非常明确——就是冲着技术人员来的。”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这不是随机扫射，是精准狙击。
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   2️⃣ 传播路径“无法规避”——常识防线失效
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   我们从小被教育：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “不要去乱七八糟的网站下载软件” “只从官方网站下载” “看HTTPS小锁”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这些建议在过去是对的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但这次事件里，攻击者直接攻破了
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    官方网站
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   HTTPS？小锁。官方域名？完全正确。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    你的所有“常识防线”，在这条攻击链面前全部失效。
   </span>
  </strong>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   3️⃣ 签名被绕过——最后一道心理防线也没了
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   很多人信任数字签名，就像信任“官方认证”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但这次攻击告诉我们：
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    签名可以绕过。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   因为攻击者没有伪造签名，而是直接替换了下载文件本身。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你验证的签名永远是“对的”——因为它本来就是真的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但你下载的东西，已经不是原来那个了。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    “可信来源”不再是安全的前提假设。
   </span>
  </strong>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    这不是孤例：供应链攻击正在“工业化”
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   如果你觉得“这种事不会轮到我”，我给你列几个近年发生的事：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      7-Zip假官网投毒
     </span>
    </strong>
    <span>
     ：攻击者搭建高仿官网，诱导用户下载恶意版本
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      Notepad++更新渠道被劫持
     </span>
    </strong>
    <span>
     ：正当软件更新时偷偷植入后门
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      主流JavaScript库被污染
     </span>
    </strong>
    <span>
     ：npm生态中多个热门库被植入窃密代码
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   趋势已经非常清晰了：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     攻击终端用户太难了——不如攻击软件的“上游”。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   你费尽心思培训员工安全意识、打补丁、做演练……
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   结果软件供应商一个漏洞，防线全部归零。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    供应链攻击的本质是：用一次攻击，撬动整个生态。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   攻击者不需要攻进你的网络——他们只需要攻进
  </span>
  <strong style="font-weight: bold; color: black;">
   <span>
    给你提供工具的那个人的网络
   </span>
  </strong>
  <span>
   。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    最可怕的结论：我们还能信任谁？
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   回到这次CPUID事件。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   它给我们上了一课：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     你无法完全信任任何软件分发链。
    </span>
   </strong>
  </p>
 </blockquote>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     官方网站？可能已被攻陷
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     数字签名？可能被绕过
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     杀毒软件？可能检测不到内存马
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     开源软件？依赖链可能有毒
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这听起来很悲观——难道什么都不用了吗？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   当然不是。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    悲观是放弃，谨慎是生存。
   </span>
  </strong>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    实战指南：如果你“中招”了，现在该怎么做
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   先别慌，按顺序做这几件事：
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   🔍 第一步：检查是否暴露
  </span>
 </h3>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   回想一下：
  </span>
 </p>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     4月9日到10日之间，你是否从官网下载过CPU-Z或HWMonitor？
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     你的电脑上是否出现过异常的
    </span>
    <code>
     <span>
      cryptbase.dll
     </span>
    </code>
    <span>
     文件？
    </span>
   </section>
  </li>
 </ul>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   如果答案是“是”——
  </span>
 </p>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   🔐 第二步：立即强制重置
  </span>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      重置所有重要账号的密码
     </span>
    </strong>
    <span>
     （尤其是浏览器记住的那些）
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      注销所有登录会话
     </span>
    </strong>
    <span>
     （强制踢掉所有设备的登录状态）
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      检查VPN、SSH、远程桌面
     </span>
    </strong>
    <span>
     等工具的凭证是否异常
    </span>
   </section>
  </li>
 </ul>
 <h3 style="margin-top: 30px; margin-bottom: 15px; font-weight: bold; background-color: #000; color: #fff; padding: 2px 10px; width: fit-content; font-size: 17px; margin: 60px auto 10px;">
  <span>
   🛡️ 第三步：建立长期防御机制
  </span>
 </h3>
 <ul class="list-paddingleft-1" style="margin-top: 8px; margin-bottom: 8px; padding-left: 25px; color: black;">
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <strong style="font-weight: bold; color: black;">
     <span>
      不要再把“来源=可信”作为安全假设
     </span>
    </strong>
    <span>
     。下载任何工具后，有条件的话做Hash校验
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     企业用户建议建立
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      软件白名单机制
     </span>
    </strong>
    <span>
     ，禁止员工随意从外网下载工具
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     重要系统启用
    </span>
    <strong style="font-weight: bold; color: black;">
     <span>
      硬件密钥或TOTP二次验证
     </span>
    </strong>
    <span>
     ，让Cookie窃取无法直接登入账号
    </span>
   </section>
  </li>
  <li>
   <section style="margin-top: 5px; margin-bottom: 5px; line-height: 26px; text-align: left; color: rgb(1,1,1); font-weight: 500;">
    <span>
     关注供应商安全通报，CPUID已在官网发布说明，持续跟踪后续
    </span>
   </section>
  </li>
 </ul>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    一个更深的思考：安全工具的“信任悖论”
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这件事最讽刺的地方在哪？
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    我们用来保护自己的工具，可能正是攻击我们的入口。
   </span>
  </strong>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   CPU-Z、HWMonitor、7-Zim、Notepad++……
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这些工具被安全社区信任了十几年。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但信任本身，就是一种风险。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   安全圈有句话：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <span>
    “永远不要相信你无法验证的东西。”
   </span>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这句话以前是说病毒的。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   现在，连软件分发链本身都不可信了。
  </span>
 </p>
 <hr style="height: 1px; margin: 0; margin-top: 10px; margin-bottom: 10px; border: none; border-top: 1px solid black;" />
 <h2 style="margin-top: 30px; margin-bottom: 15px; padding: 0px; font-size: 22px; text-align: center; font-weight: bold; color: black; line-height: 1.1em; padding-top: 12px; padding-bottom: 12px; margin: 70px 30px 30px; border: 1px solid #000;">
  <span>
   <span>
    写在最后
   </span>
  </span>
 </h2>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   CPUID事件给我们的真正教训，不是“别用CPU-Z了”。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   而是：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     你最信任的软件，才是最危险的盲区。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   未来的安全战场，不再是“防止下载恶意软件”这么简单。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   而是：
  </span>
 </p>
 <blockquote>
  <p style="padding-top: 8px; padding-bottom: 8px; font-size: 14px; margin: 0px; color: black; line-height: 26px;">
   <strong style="font-weight: bold; color: black;">
    <span>
     如何确保你使用的“合法软件”，不会在某一天变成攻击你的武器。
    </span>
   </strong>
  </p>
 </blockquote>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   这个问题没有完美的答案。
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <span>
   但有一点是确定的——
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    保持怀疑，保持验证，保持更新你的安全假设。
   </span>
  </strong>
 </p>
 <h2>
  <span>
   <span>
    参考资料
   </span>
  </span>
 </h2>
 <p>
  <span>
   https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
  </span>
 </p>
 <p>
  <span>
   来源：The Hacker News — 核心事件报道
  </span>
 </p>
 <p>
  <span>
   https://www.cyderes.com/howler-cell/how-cpuids-hwmonitor-supply-chain-was-hijacked-to-deploy-stx-rat
  </span>
 </p>
 <p>
  <span>
   来源：Cyderes — 技术分析（DLL劫持 &amp; 内存执行）
  </span>
 </p>
 <p>
  <span>
   https://www.tomshardware.com/tech-industry/cyber-security/hwmonitor-and-cpu-z-developer-cpuid-breached-by-unknown-attackers-cyberattack-forced-users-to-download-malware-instead-of-valid-apps-for-approximately-six-hours
  </span>
 </p>
 <p>
  <span>
   来源：Tom’s Hardware — 影响范围与攻击细节
  </span>
 </p>
 <p>
  <span>
   https://www.pcgamer.com/software/security/cpuids-download-page-has-been-hacked-with-its-popular-processor-and-pc-info-tools-replaced-with-links-to-files-containing-malware/
  </span>
 </p>
 <p>
  <span>
   来源：PC Gamer — 攻击方式与社区发现
  </span>
 </p>
 <p style="padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black; font-size: 14px;">
  <strong style="font-weight: bold; color: black;">
   <span>
    <br />
   </span>
  </strong>
 </p>
 <span style="font-size: 15px; display: block; text-align: center; margin-top: 50px; color: #999; border-bottom: 1px solid #eee;">
  <span>
   - END -
  </span>
 </span>
</section>
<p style="margin-bottom: 32px; border-width: 0px; border-color: initial; line-height: inherit; vertical-align: baseline; letter-spacing: normal; text-align: left;">
 <strong>
  <span style="font-size: 18px;">
   <span>
    <span style="font-weight: bold;">
     感谢阅读，如果觉得还不错的话，动动手指给个三连吧～
    </span>
   </span>
  </span>
 </strong>
</p>
<p style="display: none;">
 
 
</p>
