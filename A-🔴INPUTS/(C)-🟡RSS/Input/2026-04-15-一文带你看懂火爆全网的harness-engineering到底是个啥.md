---
title: "一文带你看懂，火爆全网的Harness Engineering到底是个啥。"
url: "https://mp.weixin.qq.com/s/yI1rQHVwJqszdpadzAe_4A"
source: "数字生命卡茲克"
date: 2026-04-15
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章提出“Harness Engineering”（驾驭工程）是AI工程发展的第三阶段，核心在于为强大的AI Agent构建一套安全、可控、自动化的约束与反馈系统，类比为给“野马”套上缰绳。它超越了早期的Prompt Engineering（人机对话）和Context Engineering（提供上下文），强调通过前馈控制（如规范文档、架构约束）和反馈机制（如自动校验、CI/CD监控）实现Agent的自主、可靠运行。作者指出，Harness并非取代前两层，而是将其嵌入更高维的系统性框架中；其思维本质是普适的控制论思想——不依赖实时干预，而靠设计规则、检查点与闭环反馈让AI在无人监督时仍能正确行事。

---

<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最近这个词实在是太火了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Harness Engineering。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我刷推刷到，朋友圈刷到，群里也在聊，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   微信指数又莫名其妙一根穿云箭了。
  </span>
 </span>
 <span>
  <br />
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   几乎每隔两三天就有人来问我，卡兹克你能不能讲讲这个
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Harness
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   到底是什么。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以想了想，我还是尽我可能，花了将近一整天的时间，给大家写一下我理解的
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Harness Engineering
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   到底是个啥。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大家其实不要觉得AI行业喜欢造概念或者喜欢搞抽象，主要还是AI这玩意实在变得太快了，很多东西也都是随着时间和行业的发展不断的前进的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一个东西在24年可能还满足当时的语境，但是25年可能就不够了，因为模型的进步速度太快了，于是25年大家只能用一个新的词来解释，结果，26年，这个词又不够用了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个大概就是如今的现状。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   跟AI跟的比较久的朋友，可能已经能猜到我上面说的是哪几个词了。
  </span>
 </span>
</section>
<section style="text-align: left; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Prompt Engineering，Context Engineering。
  </span>
 </span>
</section>
<section style="text-align: left; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   还有今天的Harness Engineering。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这三个词，几乎完美地标记了我们跟AI协作方式的三次进化。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而我恰好，这三个阶段都亲身经历过。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   从2023年大家都在研究怎么写一个好Prompt，到2025年开始研究怎么给AI更好的塞上下文，到现在2026年，大家开始聊，怎么给AI设置马具。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   三年。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说短不短，说长也不长。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但回头看，这三次变化，其实都映射的，是我们人类对AI的认知。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   打个游戏玩家都能秒懂的例子吧。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <strong>
  <span>
   <span style="font-size: 16px;">
    第一阶段，就是你在玩《只狼》这种动作游戏。
   </span>
  </span>
 </strong>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   也就是每一招格挡、每一次见切都得你手搓，按一下键它出一招。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一招没按对，屏幕上就会出现巨大的死。你就是AI唯一的操作者，AI每一个动作都得你亲自按键下令，动一下回一下，也就是我们传统的ChatBot。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <strong>
  <span>
   <span style="font-size: 16px;">
    第二阶段，就是你在玩类似《金铲铲之战》这种自走棋。
   </span>
  </span>
 </strong>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你其实可以不用再自己手搓每一个动作了，你的活其实全在前期配置。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   选英雄、凑羁绊、配装备、排站位。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   配完了，棋子就自己上场打回合，你只能吃瓜看戏。而决定胜负的，全靠你前期把信息和资源喂得对不对。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这一个阶段，就是模型能力还不够强的时候的前Agent时代。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <strong>
  <span>
   <span style="font-size: 16px;">
    第三阶段，就类似是你在玩《全面战争》这种即时战略游戏。
   </span>
  </span>
 </strong>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   场上几千个单位自己在跑，你根本摇不过来每一个兵，只能靠编队、阵型、AI指令、战场规则去驾驭整盘战局。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   单位越聪明、越自主，你越得靠一整套系统去约束它们的行为。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   从操作一个角色，到带一个小队，再到指挥一整支军队。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   玩家的控制粒度越来越粗，AI的自主度越来越高，你需要的约束方式也越来越系统。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而这三个阶段，我觉得就对应了Prompt Engineering、Context Engineering、Harness Engineering的三次跃迁。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，聊
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Harness Engineer到底是什么，我觉得最重要的，就是你要知道这一路的跃迁究竟是什么样的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   想理解现在，最好的方式，就是读懂历史。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，今天这篇文章，我就希望能真的让你明白Harness Engineering到底是个啥，它的来龙去脉，以及他能解决的问题。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   如果你是技术大佬，希望能给你提供一些新的思考角度，如果你是非技术的小白用户，我也会尽量让你看得明白。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   话不多说，我们开始。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   先从头捋。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   先把时间倒回到2023年。
  </span>
 </span>
</section>
<section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   2022年底到2023年，ChatGPT横空出世，整个世界炸了。
  </span>
 </span>
</section>
<section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我还记得23年的春节，春节回来之后，所有人都在聊ChatGPT，而那之后，那段时间最火的一个词。
  </span>
 </span>
</section>
<section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就是Prompt Engineer，提示词工程师。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当时硅谷可以给Prompt Engineer开出了年薪30万美金的offer。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后国内也是，23年的图，大家肯定都见过。
  </span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqURFaDterLbJOxsicXicqDbzhcicAtB05cKnCDA25bmEkicB0CptusnLFloZY4vAaafbrDgjrgqyGx0KVJT8jiaBhsEibyugyvxU1POE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后当时有无数的Prompt框架出现，因为彼时模型智能水平不够，所以很多时候，模型的输出不稳定，我那时候还在做AI产品，这里可以提一嘴，国内金融领域的第一个算法备案是我拿的
  </span>
  <img src="https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png" />
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们每天做的最多的事，其实就是在Prompt上做约束，怎么设计好Prompt，能让模型输出更稳定的json格式，从而跟我的数据库进行交互。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然，也有另一部分，就是写好Prompt约束，让模型生成更好更稳定的回答。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那个年代，同一个问题，你换一种问法，AI给你的答案质量就可能会天差地别。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如你直接问ChatGPT“帮我写一篇关于AI的文章”，它给你吐出来的东西大概率是一坨正确的废话。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但你如果说“你是一个科技领域的资深记者，风格偏口语化，擅长用类比来解释复杂概念，现在需要写一篇3000字的文章，主题是AI对普通人生活的影响，要有具体案例，语气不要太正式”，那出来的东西就完全不一样了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以你看，Prompt Engineering那个年代，做的最多的事就是怎么设计Prompt，能让AI给你最好的回答。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这事儿在2023年确实是有价值的，因为那时候大模型刚出来，输出也确实不稳定，大家都还在摸索跟它交流的方式。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   谁能把问题问得更好，谁把Prompt约束的更好，就能从AI那里榨出更多价值，这个技能差异是真实存在的。
  </span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但问题来了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   2024年下半年开始，一个趋势越来越明显，就是模型越来越聪明了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你不用再像伺候大爷一样去精心构造Prompt了，Claude 3.5 Sonnet出来的时候，你随便跟它说句话，它都能理解你的意思，那个时候我记得我还写了李继刚的汉语新解，也算是一代风潮。
  </span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUyD2LCI73kSaosCXdP9uMTBrmxqG9srq56v1YXibtU4SkebxdwtJ5hAG1ZQicwGq9NA1FicpbWALiaePVsJBf6qibfAgHWCUpr5IAY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那个时代，Prompt技巧的边际收益在急速下降。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为人们发现，当模型足够聪明的时候，你怎么问已经没那么重要了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   重要的是，你问的时候，它手里有没有关于你问题的足够且合适体量的信息，在有限的性能之下，来给你一个好答案。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以我后来甚至都发了一篇文章，我觉得那些Prompt技巧真的没啥用，核心的是6个心法：
  </span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&amp;mid=2647678476&amp;idx=1&amp;sn=1e7c408367fec1e41b8f882d182e05f2&amp;scene=21#wechat_redirect" target="_blank">
   <span style="font-size: 16px;">
    分享6个平时我最常用的Prompt心法。
   </span>
  </a>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   至此，这就引出了第二个阶段。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   2025年年中，Andrej Karpathy转发了一条推，大概意思是说，赞同把
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Context Engineering放在Prompt Engineering之上。
  </span>
 </span>
 <span>
  <br />
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWHZe5tpvHGLYz0RFyNjkj9ciaZCm2ibh6Wywd3PWIicDfE36s8WSia7tYPkJV0k8EbDTdapf0QiajMqn1tHkWmibibqrTHrvHng33LNQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 586px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为在实际的工业级AI应用里，真正的活不是在那雕花一个Prompt，是需要更多的考虑工程化，要精心设计AI的上下文窗口里到底该塞什么信息。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为那个年代，上下文窗口真的太小了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Karpathy的原话是，Context Engineering是“填充上下文窗口的精妙艺术与科学”。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   于是，Context Engineering，上下文工程，这个概念在2025年下半年迅速成为了所有做AI应用的人的共识。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为他确实切中了当时行业人们的痛点。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   在这里我还是想再次表达一下，很多时候，造词这事分两种情况，有一种我觉得就是为了炒概念，比如xxx 4.0，而有的时候，真的只是行业太快，人们更需要一个精准的表达。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   词语，从来都是为表达而服务的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Context Engineering解决的问题，就类似于你让AI帮你改一段代码，如果你只给它这段代码本身，它可能改得乱七八糟。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但如果你同时给它这段代码所在的文件、相关的依赖、项目的技术栈说明、团队的代码规范，它改出来的东西质量会高几个量级。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而如何优雅的、省Token的给出最精准的信息，就是真正的
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Context Engineering。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里我依然觉得，让我学到的最多，还是Manus的25年7月18号发的那篇文章。
  </span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVpV2dTveOjpInGU56xniaDBGv9TFykGHgntJAsL6x3dHx26InPgDficz4MlwoVDlue0t6XMMcaaHiazkloOI4ttY9b2ibicT6W0eSw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   到这里，其实已经比Prompt Engineering进了一大步了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   人们开始研究的是，从怎么约束单个Prompt，变成了如何在有限的上下文空间里，尽可能的给模型精准的信息。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就这样，过了又将近8个月的时间。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    Harness Engineering正式登上了属于它的舞台。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    如果是我自己印象中，第一次在AI领域看到关于
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    Harness的描述，应该是去年11月
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    Anthropic发的blog。
   </span>
  </span>
 </section>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVradzheiaBicZAwEyl5BT7WxC6N6GD6UicxGMYxayficwJN8QqQxXjpZU1f4AeoPmV3UYfXCKRP1zku43D2jTvoLyrFmoERyib9jXs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 648px !important;" />
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    这篇报告解决的核心问题是，就是如何让Agent跨越多个上下文窗口有效工作而不丢失状态。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    他们把他们的Claude Agent SDK称为，"一个强大的通用Agent Harness"。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    不过他们并没有用
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    Harness Engineering这样的描述。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    直到2026年2月，OpenAI的一篇Blog，把
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    Harness Engineering写在了巨大的标题上，于是，
   </span>
  </span>
  <span>
   <span style="font-size: 16px;">
    Harness开始正式进入大众视野。
   </span>
  </span>
 </section>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU6CqUStXf0h4Oy4B0TXzMJC9GTxVFGooxgwDkU8JbZCvqqLRG4PcY28z6Sb2qgnv3sucjscV3nN4Y3FPnvKamfOmqeNVGZcOk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 648px !important;" />
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    这篇也是有价值内容极多的一篇文章。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    大概说的就是，OpenAI内部有一个团队，用了五个月的时间，用Codex搭了一个将近一百万行代码的产品。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    其中人类手写的代码量，是0行。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    所有代码都是Codex Agent生成的，人类工程师全程没有写一行代码。
   </span>
  </span>
 </section>
 <section style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    人类工程师做的工作，就是一直在做Harness Engineering。
   </span>
  </span>
 </section>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    他们在设计架构边界，制定依赖规则，写自动化测试，配置lint规则，搭建CI/CD流水线，设计反馈循环机制。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    他们在建一个笼子，一个让AI Agent能在里面安全、高效、可控地干活的笼子。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px; font-weight: bold;">
    这个笼子，就叫Harness。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    Harness这个词，来源于马具，就是马鞍、缰绳、嚼子那一整套东西。
   </span>
  </span>
 </p>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqVPIaCwxCCHONZ8VQo8fKB18nJpVSiaibsOsProic9OaPCUk3C5FwWUBGsTkkmAwrFibamriaf9lguW6EiblSRsxIy2Qkgj1bTicwyY9s/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 648px !important;" />
 </section>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    马是一种非常强大的动物，速度快、力量大，但如果你不给它套上缰绳，它大概率会跑偏，甚至把你甩下来。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    就像那句著名的台词：
   </span>
  </span>
 </p>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUGYXZZNAhd9o7AUS1Z42PtaZhGvu2Ts4ZWic2OmyxWU8Nqwmxu29MHj4IzZFNXyb2SNO5ibJda3m2jGmGMicsxdsAgplLtChAJz4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 648px !important;" />
 </section>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    Harness的作用，就是把这股野蛮的力量，引导到你需要的方向上。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    AI Agent就是那匹马。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    模型现在本身的能力已经极其强大了，它能写代码、能做分析、能跟外部工具交互、能自主决策。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    但如果你不给它套上Harness，它就会跑偏，会犯错，会在你不知道的地方搞出幺蛾子。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px; font-weight: bold;">
    所以，Agent = Model + Harness。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    这个公式是LangChain在博客上提出来的，我觉得这可能是2026年到目前为止，关于AI工程最精辟的一句话。
   </span>
  </span>
 </p>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqX7ia277ntK8GbGJOdzMWIaO86GxEWyAia4UZsdU0OibmU8Nl6fiaicfC5L9qRiaTqHXgT3BicnoMhArVv9iavbsajxeEjBTmIk2g6oaaQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 648px !important;" />
 </section>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    虽然Birgitta Böckeler说这个定义很泛，但是我觉得还是很形象的。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    模型是马，Harness是缰绳，光有马不行，你还得有一整套驾驭它的系统。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    昨天我发的文章，其实一直在强调一个理念，叫约束先行。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    其实这就是Harness Engineering中很重要的一环。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    而一个真正的Harness到底长啥样呢，Birgitta我觉得写的框架我觉得还是比较清晰的。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    她分成了两类控制机制。
   </span>
  </span>
 </p>
 <section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUV5z2JibDPu6GnjkDEBYhaaKyJ282CmMVxto1UCibQRfPMCzXGuodhNvTKUO909fI1FpA9xRT0ic88cHedCSr8zj6su8qoR8xnJc/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 648px !important;" />
 </section>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px; font-weight: bold;">
    第一类叫Guides(feedforward controls) ，引导。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    就是在AI行动之前，提前给它设好规则，让它沿着正确的方向走。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    这有点像高速公路上的护栏，你不需要每一秒都去纠正司机别开到山沟沟里，因为只要护栏在那里，车就几乎不会开到山沟沟里面去。
   </span>
  </span>
 </p>
 <p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
  <span>
   <span style="font-size: 16px;">
    CLAUDE.md文件就是一种Guide，代码规范文档也是，架构决策记录也是，这些东西在AI动手之前就已经在那了，它们是前馈控制。
   </span>
  </span>
 </p>
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   第二类叫Sensors (feedback controls) ，检测器。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就是在AI做完事之后，用各种手段去检测它做的对不对。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   自动化测试是Sensor，代码lint是Sensor，CI流水线也是Sensor，它们是反馈控制。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   好的Harness，是Guides和Sensors的组合，前者防患于未然，后者亡羊补牢，两个加在一起，形成一个闭环。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   而每当你发现Agent犯了一个错误，你就花时间去设计一个方案，让它永远不可能再犯同样的错误。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这就是Harness Engineer的日常。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   从来都不只是在写代码，最重要的工作，其实都是在设计一个让Agent如何不再放错的系统。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就像我昨天那篇文章里面聊得，就是Claude Code的规则体系怎么从全局CLAUDE.md一层一层穿透到项目级、再到文件夹级的事，约束从上往下走，一层管着一层。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个其实虽然非常的简单，但是底层逻辑，其实跟OpenAI在那个百万行代码项目里做的事是一模一样的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   他们强制定义了一套分层架构，Types → Config → Repo → Service → Runtime → UI，六层，每一层只能依赖它下面的层，不能反向依赖。
  </span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWO9vibAnGxkGwH1xdkHzToBl08E8OX04RQROUTiczjVuYznSEPC9GsZEh0m5iaUUM3KVM7s0exad8pmv71AZP69LpLOpTmH0otkk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span>
   <span style="font-size: 16px;">
    有了约束，速度才不会下降，架构才不会漂移。
   </span>
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   规则从来不是靠口头约定，是靠自动化测试来强制执行的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   如果你非要我给
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Harness Engineering定一个最核心的概念。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那我还是想用我昨天说的那4个字。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   约束先行。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   就像我们所设计的权限系统，你可以给AI Agent设置不同级别的权限，有些操作它可以自己做，有些操作它必须先问你，有些操作它绝对不能碰。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   比如读文件可以它自己来，删文件必须先问，而像格式化硬盘这种操作，你永远想都别想。
  </span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以你其实回过头来看，这三个阶段的演变很有意思。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Prompt Engineering的时代，AI是一个聊天机器人。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你跟它的交互方式是一轮对话，你说一句，它回一句。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在这个模式下，你唯一能影响输出的杠杆，就是你的Prompt，所以大家拼命研究怎么写Prompt。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Context Engineering的时代，AI变成了一个助手。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它不再只是回答问题，它开始帮你做事了，它要读你的文档，理解你的项目，调用你的工具，在这个模式下，光靠Prompt不够了，你还需要给它提供充足的上下文。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Harness Engineering的时代，AI变成了一个自主行动的Agent。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它不是在等你的指令，它可以自己在那跑，它自己写代码，自己测试，自己提交，自己部署。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在这个模式下，Context也不够了，因为Agent是自主运行的，你没法一直盯着它。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你需要一个系统来约束它、监控它、在它犯错的时候自动纠正它。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以这三个阶段的演变，对应的其实是AI角色的三次升级。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   聊天机器人 → AI助手 → 自主Agent。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而你，跟它的关系也变了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   其实我上个月也写过一篇短文，叫
  </span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&amp;mid=2647680643&amp;idx=1&amp;sn=b717e3587060f26c2f13bd4d0a6725e1&amp;scene=21#wechat_redirect" target="_blank">
   <span style="font-size: 16px;">
    能用脚本就别用Agent
   </span>
  </a>
  <span style="font-size: 16px;">
   ，讲的就是脚本→Skill→Agent这个金字塔。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个思路其实也跟Harness Engineering的理念差不多，能用确定性规则约束的地方就用规则，能用自动化检测的地方就用检测，只有那些真正需要判断力的部分，才留给Agent自由发挥。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你不会用大炮打蚊子，同样的道理，你也不该在可以用确定性规则解决的地方引入不确定性。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以啊，其实3个时代的
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Engineering，从来都不是什么替代关系，而是一层一层升维、随着时代前进的嵌套关系。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Harness Engineer需要懂Context Engineering，因为给AI提供正确的上下文信息本身就是Harness的一部分。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Context Engineer也需要懂Prompt Engineering，因为最终跟AI沟通的单元还是一条条的Prompt。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   每一层都没有过时，只是被更大的框架包裹住了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那我知道，看到最后，你可能会问了，我又不是程序员，Harness Engineering跟我有什么关系？
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这是个好问题，我也知道很多看我文章的朋友不是技术背景。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我自己更不是程序员出身，我是用户体验设计师。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   坦率的讲，Harness Engineer这个角色，目前确实主要出现在软件开发领域，因为现如今，AI Agent目前最成熟的落地场景，那就是写代码、开发产品。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但我觉得，Harness Engineering的思维方式，其实是普适的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如很多朋友现在用AI做任何稍微复杂一点的事情，可能都会遇到这种问题，比如AI有时候莫名其妙就跑偏了，你得反复纠正它。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这就是缺少Harness。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如你能不能给AI设一些规则，让它在这些规则的框架内干活？比如你让AI帮你写邮件，你能不能事先告诉它，「永远不要用感叹号结尾」「收件人是老板的时候语气要正式」「涉及数字的时候要double check」。这就是你的Harness。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如你能不能设计一些检查点，在AI输出之后自动验证？比如你让AI帮你做数据分析，能不能设一个规则让它每次算完都自己验算一遍？这也是Harness。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   20世纪的伟大科学成就之一，控制论，里面最核心的一个思想，就是任何复杂系统的稳定运行，都依赖于反馈机制。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   恒温器之所以能保持房间温度恒定，从来都不是因为它知道应该是多少度，是因为它有一个传感器能感知当前温度，然后跟目标温度做比较，然后不断的进行调整。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这些思维方式，就是Harness Engineering的内核，从来不是说，让你直接做技术去写代码，是需要你思考清楚，怎么让AI在我不盯着的时候也能干好活，是如何设计一个系统，能让你不用盯着的时候，这个系统也能自己运行起来。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   其实我们驯服AI的过程，真的跟人类驯服大自然的历史，也有着极高的相似度。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最早人类学会用火，你得小心翼翼地喂它柴火，火太小不行，太大也不行。这是Prompt Engineering，你的每一次输入都直接决定输出。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   后来人类学会了建炉子，你把火关在一个结构里，通过调节进气口和烟囱来控制火势。这是Context Engineering，你通过设计上下文来影响火的行为。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   再后来人类发明了蒸汽机，火不再是你直接操控的对象了，它在一个精密的系统里自动运行，有锅炉、有气缸、有调节阀、有安全阀，你无需再管火怎么烧，你管的是这套系统怎么设计。这是Harness Engineering。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   从火焰到蒸汽机，人类花了几千年。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   从Prompt Engineering到Harness Engineering，AI只花了三年。
  </span>
 </span>
</p>
<p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   甚至我觉得，如何使用AI演变到最后，其实就是人类历史上出现的那一门一门的古老的学科。
  </span>
 </span>
</p>
<p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Harness就是控制论。
  </span>
 </span>
</p>
<p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Skill其实就是分类学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Prompt其实就是语言学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Context其实就是信息科学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Reasoning其实就是认知心理学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   多Agent协同其实就是管理学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，很多人天天说什么文科已死，我每次都会说这是放屁，从来没有什么文科已死理科已死的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这世界就不应该再分文理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   两端融合，才是真正的王道。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   多学科融合背景，有理工科的严谨，有文科的审美。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   有结构化的理性，也有人文的洞察。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这样的人，在未来十年里，我才觉得会是整个社会里，能把AI、Agent用的最牛逼，同时也是未来最稀缺的那批人。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，根本不要焦虑。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Harness Engineering根本不是什么新词。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   它就是人类几千年来一直在做的那一件老事。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   就是怎么把一股更快、更强、更不受控的力量，安全地、持续地、可复制地，引导到我们想要的方向上去。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   火是这样，蒸汽是这样，电是这样，核能也是这样。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   从我们学会用火开始，那几十万年的历史。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   从来都是这样。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   只不过，这一次，轮到AI了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   仅此而已。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当一个东西比你更快、比你更强、比你更自主的时候，你怎么还能让它，为你所用。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这件事，你的祖先做过，你的父辈做过。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   只是现在。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   轮到你了。
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
   &gt;/ 作者：卡兹克
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
<p style="display: none;">
 
 
</p>
