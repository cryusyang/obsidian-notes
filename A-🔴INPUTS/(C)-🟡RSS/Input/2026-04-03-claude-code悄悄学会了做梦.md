---
title: "Claude Code悄悄学会了做梦。"
url: "https://mp.weixin.qq.com/s/CljajqS3x3ETOe4tPubQzw"
source: "数字生命卡茲克"
date: 2026-04-03
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Anthropic为Claude Code推出的Auto Dream功能，是一种在后台自动整理项目记忆的“反思性扫描”机制，需满足24小时未整理且积累5条对话两个条件才触发；它与默认开启的Auto Memory（自动记录用户偏好、项目信息等）协同工作，解决长期使用后记忆冗余、矛盾、过期和时间模糊等导致AI“变蠢”的核心问题；Auto Dream通过定向、信号搜集、巩固更新、修剪索引四步，精简并结构化MEMORY.md及关联记忆文件，显著提升记忆准确性和可用性；该过程严格隔离于代码目录，仅读写记忆文件，保障安全性与稳定性。

---

<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我的Claude Code，学会做梦了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px; text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUEibfIlhykEVkRkleEiaCK0kQLg3HJw3ota9pmH88X5CKjGgDgBOQPQ8Fm0XZP5Bf4AIrpRURsCsquChKX21xHKCn51HATxQpibI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说真的，我打这行字的时候自己都觉得有点离谱。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   事情是这样的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就在前些日子，Anthropic新出了一个功能叫Auto Dream，字面意思，让Agent在休息的时候，自动做梦。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在3月底开始灰度这个功能，目前还没有全量放开，但已经有不少人用上了，比如我。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWFvNcIicJ5PvibW6TAAPDBQPzbmlTfM5K15u61GtSg5xWtjPSG49PQWpR6s4JJr5DamLVibSibGzVpwkoZoWsp57yNX4JtEFguTNU/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大家也可以试试，在Claude Code里输入
  </span>
 </span>
 <code>
  <span>
   <span style="font-size: 16px;">
    /memory
   </span>
  </span>
 </code>
 <span>
  <span style="font-size: 16px;">
   ，看看有没有auto-dream这个选项，如果有的话就可以打开。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   打开之后它也不是随时都在做梦的，得同时满足两个条件才会自动触发。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一是距离上次整理已经过了24小时，二是中间至少积累了5个对话记录。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后当你打开一个Claude Code对话开始干活的时候，系统会在后台检查是不是满足了上面的两个触发条件。如果满足了，它就会在后台单独起一个子代理来做整理，完全不影响你当前的对话。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你该敲代码敲代码，该改bug改bug，做梦的事情它自己会在后台默默处理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，实际上，Claude不是真的意义上，在你睡觉的时候和你一起做梦，是在你下次打开它干活的时候，趁你不注意，在后台做梦。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然，如果按照Claude Code的代码来看的话，他们命名为
  </span>
 </span>
 <span>
  <span>
   <span style="font-size: 16px;">
    Kairos和
   </span>
  </span>
  <span>
   <span>
    <span style="font-size: 16px;">
     Daemon
    </span>
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    的小龙虾模式上线以后，那是真的，可能能做到跟你一起做梦。
   </span>
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span>
   <span style="font-size: 16px;">
    当然，如果不想等自动触发，也可以手动让它强行做梦。
   </span>
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span>
   <span style="font-size: 16px;">
    我自己就是31分钟之前被整理了一下，我都不知道。
   </span>
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVHUp2T1k670sCwOUjAduiagqOibTushZJuenGBhJoMprhtSDRrUlnG1GwdxMTNL0Qt7Y6flwlgibPvPPbFGr7pRa3jSNPdHRv0ias/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   不过因为现在是灰度状态，所以手动的时候经常会出问题。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如说你按官方的推荐指令/dream去输入的话，就很有可能会出现这个：
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Unknown skill: dream
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXYsth9PpWofO5PI2S70n6NF9GA0YJgpL6tNWl9VibpFqicib0Gicsuadm5hNoxISAVicagliccwtjucZ0rTTqBzFL9t5soWib9SnjDR0/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   显示找不到Dream的skill。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是这个做梦系统，我还是觉得可以聊聊的，因为这个机制真的非常非常有趣。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为它要解决的，是AI领域一个老大难的问题。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   AI的记忆。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在正式聊Auto Dream之前，我觉得首先要说一下，跟其对应的另一个功能，就是Auto Memory。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个是今年2月上线的一个全自动的记忆系统，默认开启。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   也就是Claude Codo会在跟你协作的过程中，自动把它觉得需要记录的东西记下来。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXrpVdDg4G1UpNI8tBYTCte83mog55ibyT4lmLdqHFkPwTANibElDcERyXQFm1jO2iaiaE9Ba0eMKBhnWNsaox2KQxoE71VVTEURiaA/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 597px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你用什么框架、你喜欢什么代码风格、你项目的架构长什么样，它都会自己记。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这些笔记存在 ~/.claude/projects/你的项目名/memory/ 这个目录下面。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这是按项目隔离的，每个项目有自己独立的一套记忆文件。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你在项目A里积累的记忆不会跑到项目B去。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个目录里面的结构大概长这样（我的是已经被整理过的了，之前的会非常恐怖）。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXoEnoibfiaU5DzFsABPRxhichSqS5DlIddto1JpvoWZTbUENm2Zh5kUO7VtMD1z6fbaaCG250fIbh2NVhezaP7p7uN3HO0dJlxGE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   MEMORY.md是索引，是大目录。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUm5kNyePoWRXV7gE6f10KKPTqvNQIrdA2PBvXRHzewkiaWX4h49rAuzj8D6RULus0Jx2Cn8EpJZkntS8JrIVj2dliaI5pRh1v9g/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   里面一般包含4种文档：
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   user：你这个人的信息。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   feedback：
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   你对Claude的纠正或肯定。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   project：
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   项目进展、决策、背景。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   reference（我的里面没有）：
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   外部资源的指引。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   每次新对话启动的时候，Claude会自动读取索引文件也就是Memory.md它的前200行。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXL8MqIk75bVj2fJ0lxbn8c7Tdn3kMzfbekVIpr6KV7aQVBZ1E5mXmoo1cmmrxxSWgK4faPVmRx7EpAdhM7r4gdr0rn3dntw1g/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   其他的文件，会被Claude读取文件的标题和描述，根据你的这次问题来判断再调用哪些来处理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Auto Memory的记忆是按项目隔离的，每个项目一套。
  </span>
 </span>
 <strong>
  <span>
   <br />
  </span>
 </strong>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <strong>
  <span>
   <span style="font-size: 16px;">
    而Auto Dream的作用，就是处理当前项目的这套memory记忆文件。
   </span>
  </span>
 </strong>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <strong>
  <span>
   <span style="font-size: 16px; font-weight: normal;">
    因为这些记忆好是好，但是还是有个巨大的痛点，就是一旦多了之后，你的记忆系统就会爆炸了。
   </span>
  </span>
 </strong>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   大家可能没看过你的Agent记忆系统有多爆炸，这块其实小龙虾是最爆炸的，你用的多的话，去看看记忆系统你就懂了，有的时候，越用越聪明，其实是个谎言= =
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   我给大家举个例子。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   就比如说，你是老板，你有个工作助理，叫小呆逼。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   他贼勤快，
  </span>
  <span style="font-size: 16px;">
   每天帮你干活的时候都在备忘录上随手记笔记。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   “老板喜欢方案A的方向”， “下周五之前要交初稿”，“这个项目的数据放在飞书多维表格里”。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大概就是这样的东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是问题来了，很有可能，过了几天，老板改主意了，说方案B更好，但是他没直接说，方案A我们不要了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   于是，你那个勤快的小呆逼助理，就勤勤勉勉的记下来了，可是旧的那条“老板喜欢方案A”的记忆，他并不会自己删掉，还是放在那了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   这就像Claude Code，或者说，现在绝大多数的Agent一样，于是你的记忆文件里，方案A和方案B并存。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Claude每次开新对话读到这两条，一脸懵逼，不知道该信哪个。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最恶心的我不知道大家有没有遇到过，其实，是时间。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Auto Memory在记笔记的时候，经常会写“昨天决定把交付日期推迟到下周”这种相对日期。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但，尼玛的过了一个月之后，所谓“昨天”是哪个昨天？“下周”是哪个下周？鬼才知道，Claude也不知道。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   再加上一些早就完结了的项目的笔记、已经被推翻的方案、过期了的deadline。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你就会发现，本来是为了让Claude更懂你的记忆系统，几十次上百次对话之后，反而变成了让Claude更蠢的噪音库。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这就是Auto Dream要解决的事。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在它的系统提示词里，第一句话就写着，你正在做一个梦，一次对你记忆文件的反思性扫描。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUTatialZMuh30nMNnUoA8opjqInbvlIqhDzOyOXyc7kg8toxTdQgXibmXgCPVZY4cZ4TeYxkwKJKar5Dt8PoW2rN9O74kiaSRK6I/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我当时是真的觉得这个命名还挺浪漫的，完美的戳在我的审美上。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一家做AI的公司，把一个记忆整理功能叫做做梦。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   为了给大家看看它到底在做什么，我把我们公司的小伙伴找了一个遍，终于找到一个，能手动触发/dream做梦权限的人。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   以为内如果是自动触发的话，你其实什么都看不到的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   整个做梦过程分四步。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第一步，Orient，定向。Claude先读一遍自己的整个记忆目录，搞清楚现在都记了些什么，有哪些文件，文件之间什么关系。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就像你早上醒来，先回忆一下昨天干了什么。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXgmaWaMJ2A4XicAKM4FVSvA5yKcE00UiclTEOZ1wmQLCbJBicsIas9RGXJoCrfjRP1e8adx4xU5icyh1icsefn0pEuwJ6by2IMibNyg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第二步，搜集信号。它会去翻之前的对话记录，但不是很傻的全读一遍，会根据特定目标去搜索。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   重点找的是你纠正它的地方、你让它记住的东西、反复出现的东西、还有重要的决策。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUOkekwzhrXObe2SpPb9ClNom9Kftibn17yTlibt1HGMvlfjia102HwibF0BhZe4iccQUyhEicSuPOpJ9endOe02yAYVFZ6qfaPxYdhE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第三步，巩固。这是核心环节。它会把翻到的信号跟现有的记忆文件逐个比对，看看有没有需要更新或者补充的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如把重复的信息合并，矛盾的信息解决掉，写对的日期，再把已经没用的信息清掉。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVFNssADmVTZ0BR4gI0103Ij9L4R6FpIfGhzBYwjStZlM9BlxfzMp7xF20SXWfmQQ6osmAvEKouibCUH66qeMicgoybdGVWqKdWs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第四步，修剪和索引。最后再过一遍，把多余的、冗余的、占着位置但没什么蛋用的信息都删了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWYR1niaAPAUUC1L72A00QRyIveia9ZJgvbcV0dcFz5p7anibzHBJqiaaXq1woYs7Vlb9kPMqiabPDyiaK7DXGvHswMBibNsJBn4McCp4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最后它给了一个整理结果报告。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我这个小伙伴的这个记忆不是很多，整个过程，花了1分19秒。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUICY78Klvq8kpscymeGGqxhWUXibiaCsS2attvMkNYewYZysWYHZQq7kpStPyDQuETickLaq3snKibHQnh0vBSaEtKSUw6t1tAy94/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是，如果你是用的久的大佬那就不一样了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   社区之前提过一个夸张的案例，913个对话积累的记忆，Auto Dream大概花了8到9分钟整理。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWLb72Y94EAyFY0nHBLia2sJHcaxEMOqN8xylVIUScUeoxwRicBMI4Krwcw9QPrzL1v8nm34FiaiakJjkFCl2lIw1Xkia720ImW8LD8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   做梦之前，30多个对话积累下来的记忆目录，MEMORY.md已经膨胀到280行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   里面躺着3条互相矛盾的API错误记录。Yesterday出现了6次，没有一个带日期，等等等等各种问题。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUrdqBS3MoutXAQWO9obMic0Yjcmvy6u0MNZQiaUA8iaPAzu2ggZv3XtNgDc7sjYICpiaDqwGFUwBdfjDT3Y2Wia27PtFMVAG3reN9o/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   做梦之后，MEMORY.md从280行瘦身到142行，干净的索引加上指向各个主题文件的链接。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   矛盾的记录被解决了，过时的框架名被更新了，所有的日期都变成了真实日期，相当牛逼。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUTcNFEx5UsJCfAxhsib4HzkjaSna2OX2npQALtAcRf6TFeyny5cfETeQxszIfhlXLUI0IPIHXXuoC8adoFhKhC3bh1I3YqH63E/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="height: auto !important; width: 664px !important;" />
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这才是Auto Dream真正的威力。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Auto Dream在做梦的时候，你的项目代码是只读的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   也就是说它只能写记忆文件，但碰不了你的源代码，整个做梦过程被严格隔离在记忆目录里面。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而且如果你同时开了两个Claude Code窗口在同一个项目上，只有一个能跑Auto Dream。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   有一说一，Anthropic做产品，整体还是想得比较周到。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   至今为止，Claude Code现在有了四层记忆。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这四层各司其职。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXZx2lgaj4pjY6A8MUOVI4n4PwLZIqmGrY1bMqnGzOUMqkhXuBbKcJg6thhjFriahSgmMElFQibTxIG09OEy0ZmCic1rbDod8VDnU/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第一层，CLAUDE.md。你手写的指令文件。项目规范、编码标准等等，这些是你主动教给Claude的东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   目前的最高权限。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第二层，Auto Memory。Claude在工作过程中自己记的笔记。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第三层，Session Memory。单次对话内的上下文记忆。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就是标准的上下文窗口，你跟它当前这轮对话里说的所有东西，对话结束就没了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWPa6zB6onfMPyIIljQYDkZ8RMOluLXEH807yia5gTJJjHkhtyFkibCfYtXkpbwrrb54y0RO37313CjP7oibVCQEibl9yNzAJHpLP4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但对话的原始记录会以JSONL日志文件的形式留在了本地。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX2wH0OiclsxIdwQ1nqOLKiaEcEjoQYGrtluP5cjUxBpdpz1V3IhlTiaRibokJVuwMh1FlbPXwjGhciceGYPgdNFOibzVPPNAfGniabnY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=19" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Claude平时不会去读这些日志，但Auto Dream做梦的时候会去翻它们，从里面捞有价值的信息出来。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW3q43OYwPs4wHXGBibnAW7x5Lia4Rljzrsf23GDpsQPFJCz1BSFGjaxicEiab4N6c0Ro6rqCEVfzLLbIwKIRiaf632ia31ziciaPGxFJs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=20" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第四层，Auto Dream。后台的记忆巩固层。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   定期清理、整理、优化Auto Memory积累的所有笔记。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说真的，现在Agent的记忆架构，越来越完整，也越来越像人了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而我当年做交互设计的时候，学的认知心理学的知识，总感觉又快死灰复燃了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为这套架构，真的跟人类大脑的运作方式几乎是同构的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你肯定有过这种经历，比如考试前一晚临时抱佛脚，背了一堆东西，当时觉得脑子里全是，绝逼完蛋。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   结果第二天早上起来再看一遍，诶，居然记住了不少。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这其实不是你天赋异禀，纯属于是你的大脑在你睡觉的时候替你干活了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里需要铺垫一个小知识。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   人的记忆其实分三个层次。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第一层，感官记忆，也叫瞬时记忆。你眼睛扫过一个东西，耳朵听到一个声音，这些信息会在大脑里停留几秒钟，然后就没了。绝大部分的信息都死在了这一步。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第二层，短期记忆。从感官记忆里被你注意到的信息，会进入短期记忆。但这里的容量很小，大概只能同时装7±2个左右的东西，而且不反复念叨的话大概只能撑15到30秒。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你刚看到一个验证码，走到电脑前就忘了，就是这个道理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第三层，长期记忆。理论上容量无限，可以保持很久很久。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你二十年前的事还记得，就是长期记忆在干活。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWGZmLFS9XANXQnsQTRJCibnwGKuywCZo8Ric6U7eMekkYyDica8pKUpIiboD5hxXgfClFzqD0C3csdc16xBkaW5VQWsXNW4N4QeIU/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=21" style="height: auto !important; width: 552px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   信息要从短期记忆变成长期记忆，中间必须经过一个叫编码和巩固的过程。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而这个巩固过程，很大程度上就是在睡眠中完成的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   神经科学里把这个叫记忆巩固，大致的机制是这样的。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXINL8fbkFLibkzy2twRL7qZJNRfGUibWicvhrCO9zKXArw2CCJWfIjnsqicba5FP7MnEgPTiaS93JA79aQsgJD8aK06Jm0YQhy1W3E/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=22" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你白天经历的事情，先被快速存储在海马体里，这是大脑的临时缓存区，容量有限，写入速度快，但不稳定。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你可以把它理解成auto memory记录的记忆，随手记，但容易乱。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   到了晚上你进入睡眠，大脑会经历好几个周期的非快速眼动睡眠和快速动眼睡眠交替。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大概每个周期90分钟左右，一晚上跑四到六轮。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqU6CBvv5YjaxkIouRrHMSZxicqf2AGRcDlfs3SsS6T1MmZ16sAWHicBymb7eWwF89kYMPyow1l2fgAmWJvziapdo4SUfsFMJeuicZU/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=23" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在深度睡眠阶段，海马体会把白天存的信息重新激活，一遍一遍的回放给大脑皮层。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大脑皮层是负责长期存储的地方，这个过程叫做记忆重放。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后到了快速动眼睡眠，也就是我们做梦最活跃的阶段，大脑会做更精细的处理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   把这些回放过的信息跟你已有的知识网络做整合，加强有意义的连接，弱化不重要的，把零散的碎片重新编织成结构化的长期记忆。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   整个过程就像是，海马体是你的草稿纸，白天随手记。晚上非快速眼动睡眠阶段把草稿纸上的内容叽啦呱啦的再回放给大脑皮层。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   快速动眼睡眠阶段大脑皮层再把这些内容，分门别类的归档到对应的位置。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   是不是跟Auto Dream那四步流程，长得几乎一模一样？
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   所以当你熬夜的时候不只是身体累，记忆巩固也会受影响，记忆力变得越来越差。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我现在就能明显的感觉到这一点。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而且非常关键的是，大脑在梦里做的一件很重要的事，不只是加强记忆，还有遗忘。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   有选择性的遗忘。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   好的记忆，从来不是记住所有东西，而是记住该记的，忘掉该忘的。Auto Dream做的也是同一件事。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但这个过程中，AI比人类有一个优势。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   人类忘了就是真忘了，但Claude不是。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Claude的原始对话记录，那些对话的JSONL文件，是一直保留在本地的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Auto Dream整理的时候，只是从记忆文件里删掉了过时的内容，原始的对话记录并没有被碰。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   如果你哪天真的需要翻旧账，那些被遗忘的信息其实还在。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这不就是选择性遗忘的究极进化版吗？
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   既享受了遗忘带来的好处，又保留了随时翻旧账的能力。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，不管你是碳基的还是硅基的，都得做梦。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然了，Claude Code不会梦见电子羊，不会做噩梦被bug追着跑，也不会在梦里灵光一现想出一个算法。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它做的只是最基础的记忆整理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但它意味着，AI开始有了自己的时间感。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   开始有了过去，有了对过去的整理，并且从过去中提炼出的理解。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   笛卡尔当年，写下了我思故我在。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我不确定Claude整理记忆，算不算严格意义上的思。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但它确实在凌晨三点，趁我不注意的时候，悄悄给我整了个活。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   回顾过去，然后让自己变得更好。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   反正，我自己是没做到每天睡前整理当天的笔记。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这么一想，Claude好像比我自律多了。。。
  </span>
 </span>
</p>
<p>
 <span style="letter-spacing: 0.578px; font-size: 15px;">
  <strong>
   <strong style="letter-spacing: 0.544px;">
    <strong>
     <span>
      <span>
       以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。
      </span>
     </span>
    </strong>
   </strong>
  </strong>
 </span>
</p>
<p>
 <span>
  <span>
   &gt;/ 作者：卡兹克、可达
  </span>
 </span>
</p>
<p>
 <span>
  <span>
   &gt;/ 投稿或爆料，请联系邮箱：
  </span>
  <span>
   wzglyay@virxact.com
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px; margin-bottom: 0px;">
 <span>
 </span>
</section>
<p style="display: none;">
 
 
</p>
