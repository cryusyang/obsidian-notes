---
title: "从0开始，在国内用上Claude Code的终极保姆教程来了。"
url: "https://mp.weixin.qq.com/s/AA2NHww4jUBuAfi10EYICw"
source: "数字生命卡茲克"
date: 2026-04-20
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文是一篇面向小白用户的Claude Code入门教程，强调其作为优秀Agent框架的易用性与国内可用性——无需魔法、不依赖Claude原生模型、支持国产模型（如GLM-5.1）；详细分步讲解了Mac和Windows系统下有/无网络代理环境的安装方法（含Homebrew、WinGet等替代方案），并介绍了通过CC Switch工具灵活接入各类大模型的操作流程，旨在让所有用户零门槛上手当前最实用的Agent开发框架。

---

<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  最近很多朋友都在问我，能不能出一期Claude Code的小白教程。
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  他们也想用上这个世界上最牛逼的Agent产品。
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW2CQz1Kc9VPfXZvMUArPPSpNiau10uMJSPrYSMHkbNNHvs8lYknfHympgIDa3BoOMSoGia3tSVvb6S1RHQ1WhCAbyznZhTBgv9Q/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 493px !important;" />
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而且其实很多人不太知道，Agent产品一般是Agent框架+模型组成的，Claude的模型国内确实会封，会非常的难搞，我也没有任何办法教大家弄。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但Claude Code不会被封，也不会用不了，因为这玩意其实就是个Agent框架，搭配任何模型都可以使用。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   虽然A
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   nthropics确实很狗，天天封号，又搞实名认证
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，但我依然不得不承认，这个世界上目前最好的Agent框架，还是Claude Code。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以我常年说，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   能一步到位就一步到位，我当然知道现在比如什么OpenClaw、Hermers Agent等等非常火，但是我还是依然会建议你使用Claude Code，即使用不了Claude的原生模型，你搭配个国产模型，效果也依然很好。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而且也不用担心封号，不需要外国手机号，visa卡，甚至都可以不上魔法。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以今天，就来一篇Claude Code的从0入门全面新手教程，并且尽可能让所有的朋友，都可以用上，Windows和Mac，有魔法没魔法的操作，我都准备了，大家按需看对应的部分就行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   下面的安装流程，是我一整个周末，跟我们小伙伴一起，折腾了五六台电脑反复安装卸载试出来的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如有些场景，像没有魔法，其实还有其他安装方式，像npm，又或者直接curl国内镜像源，这些办法其实也能用，但我在不同电脑上测试的时候并不够稳定。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以最后，我选了在我看来最简单，并且在极度原始的电脑上测试也不容易翻车的方式。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   只希望大家跟着文章，都能顺利地用上世界上最牛逼的Agent框架。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我会把每一步都给大家说得尽量详细清楚，可能会有些啰嗦，大家别介意。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   好了，我们直接开始。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 16px; text-align: left; margin-left: 8px; margin-right: 8px;">
 <span style="font-size: 20px;">
  <strong>
   <span style="font-size: 20px; letter-spacing: 0.578px; text-decoration: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);">
    <span>
     一. Claude Code 安装
    </span>
   </span>
  </strong>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   1. Mac
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   先来看Mac，Windows同学可以直接跳过Mac这一趴去下面找Windows的教程。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们先在App中找到终端打开。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWfp05Lp1YVQ5c5JRhQfjhJvbSibrugI6OcMyl0lH5rsmIC8nhrBlIvp7kho1IFMYHWjJbDFgHF8Pr4Jibdd9QTyicEjYB7TvrBFA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们先来安装一下今天的主角，Claude Code。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里我给自己的电脑新建了一个全新的macOS账号，基本等同于空电脑，方便演示。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   先聊有魔法的情况。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   命令就一句话。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>curl</span> -fsSL https://claude.ai/install.sh | bash</span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们在终端粘贴这条命令后，按下回车。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVJUeZJTh0qdpqnMVMMDh0tooxtBv2Xic8CbVdia5VGMxQDGfy9b9qtWVb4FIicKpiaW6yO80Jha8WCwlbgmK9HGrCnkyb0wGw04bs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 479px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   等一会，就能看到安装成功。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUqHA6AzYsWqLsGc8g306ib1L3YJt50OSxzhicpXpEOaOs4nutQoYrBibojlEfiarhcbYpljvqBSjzzQmfNtFx4FBwvccmSxeYicl2A/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 547px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   虽然装好了，但这里有可能他也会给出一个提示。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqV2b2wwLLdtUAV5KSVUrh3ZHNVOslbtn76aoUOEI3sLd075HXfwGUsZKpJ5DTiaiaSNN1UFF7RHEUv4bSNVYmWy2WhmNFsnk5KRM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 542px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   意思是说，Claude Code已经装好了，但Claude Code的安装位置~/.local/bin还没加到你的PATH环境变量里，所以你直接敲claude可能找不到这个命令。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还说要解决这个问题，请执行下面那条命令巴拉巴拉。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   看不懂也没关系，我们就按他说的，把他给出的那一长串echo命令复制到终端里，回车跑一下。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后输入claude --version，有版本号输出，就表示安装成功了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWc2BxYR3YnjxJR5H9Piat1G94gJLg3oX1SA0VxZ9JzqmaHnkVZVXkPKux52oPicpNicPrJXFS4ibtrAtD4pkFcGL2NTicNBhicO98lk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 662px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   有魔法的情况非常简单，但是我也知道，很多同学是没有魔法的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   所以，如果没有魔法的话，我们可以通过homebrew安装。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Homebrew是macOS上最流行的命令行包管理器，作用是让你用一条命令就能安装、更新、卸载各种软件和开发工具。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里我借了一台我们经纪小伙伴的新电脑，没有魔法，环境非常干净。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们先来装一下brew，看着可能会有点复杂，但是其实你跟着做，特别简单。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   把下面这行命令粘贴到命令行，回车运行。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>/bin/bash -c <span>"</span><span><span>$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)</span></span><span>"</span></span></code></pre>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqWicIiaSticDib53AEXY9kic8Z6Z340xPo22Q3gpmnk88RTDfibVW5a45wXfWRADqcxO9icTSsMOSsF8qv5XQfZTrbN3jZuURcziaewgB8/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   看到提示之后，我们直接回车。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后他就会跑啊跑啊。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   耐心等待几分钟，等他跑完，出现安装成功就装好了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXYQBxaCjooFohuwXoATBPPvYWNyzvkUF9XXFLPPulauUhkjCtFic1EjnYv1vh3PXbc1b6icKYa7sH6h3pXuyptNHxX05GyA15icY/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   下一步，我们需要把homebrew加到路径变量里面去，这样我们在终端使用homebrew的时候他才能找到命令。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqWiaAck2UaD9g5icph32dibT99kQqicKFgUXRDlUwibSNOnniaOw7tAZesNtSEeuY2su2Wzcob1OQG05EG1BZmVVQ65c08PrcNkZGZico/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   把这几行命令粘贴到终端里跑一遍。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX8X5vcuTGLpjmCM3j0diafqvcqp1O24kSbBhT8UPseHHpxAT7Q3uiaWvibyG7JjkmTm7AjXDgCr6Q8rQPzcXqULrubPIq3Eo7528/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这样，我们就可以使用homebrew来管理Mac包了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   接着，用下面这行命令来装Claude code，这里因为公众号编辑器会自动改一些格式，直接复制粘贴会报错。辛苦大家手敲一下，或者发给claude让他改了，再粘贴到终端。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>brew install --cask claude-code@latest<span></span><span></span></span></code></pre>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXiaU4YypyjKQB3TdETic6UO3sDaF0tqvULSiaRVOV1ZnAS3m1G15o6ich3MCDrwPQLRBUunsMN8ISZyFjib5AaiarSlTOxY5n75biclc/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里的安装速度有点慢，大家可以先去抹灰鱼，忙完了回来看。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   等安装成功出现，我们在终端输入claude，就能看到小螃蟹了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px; text-align: center;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXyEjAnVtjXMxIibDo9dicyjDAPABBmxU8b4bjPsBtTmtD3XJlVbElGJtqL8h0eufOwMeTptq0AichXwIlldDjiaYxQ01s2LEz9rvc/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是这里，会显示用不了，可以先不管，一会我们会教大家怎么接上模型。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   mac说完了，然后在单独说一下Windows，会稍微有一点点不一样，安装好的Mac同学可以直接跳过这一趴。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   2. Windows
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: normal;">
   再来看Windows。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我这里拿了一台刚刷机过的Windows来装了一遍。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为Claude Code在Windows上内部是用Git Bash来执行命令的，所以要想在Windows上用Claude Code，必须先把Git安装上。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以第一步，我们先把Git装上。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   已经装好的朋友可以跳过这一趴。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   用WinGet来装，这个东西是Windows官方的包管理器，可以理解成Windows版本的Homebrew。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们在任务栏搜索终端打开。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px; text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUC4TyMPu6ic61N8M04NEQqCLibdnCzosVYlnug6g0AfhbuykzDCBweQoPb0fpOhDbYbRlrenWdadNaRfFYyAx5b4Wky0OIXWV74/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   粘贴下面的命令到终端，这里安装的时候不开魔法速度会快很多。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>winget</span> install Git.Git</span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   跑完就会显示成功安装了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqVHMNWzava5WtGRbqlFc8xnUHYicF3fOHyF7fVqbeu4at0Taq9kWnPPAaicd7nlXxXIzKI5ABG3e1Fwt7AEtINXiayFI26Qzs7xCM/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   Git装好了之后，老规矩，我们先说有魔法的情况。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   有魔法的朋友，我们还是用他官方的原生安装命令。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   粘贴命令到终端。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>irm</span> https://claude.ai/install.ps1 | iex</span></code></pre>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVu9vA9QicUcncWxMNBJsUTPx72gVYzc5qT75HHPOp8yzibW9Oib4wMpumUzp0Dic5TvKEJJa9DHmz7x04IyCMm5a2wwvumZvKPe7g/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   等一会就安装好了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqX2DKlBscDyfDKBLlQQiax8vpVsZicYHayfib6pwGKcJ1SyMXkOONUsrM9yMCtMMiaSbWicictZhpPaJVWJefarQQXR0z7Tm3vqu6iaFA/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   非常便捷。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   如果没魔法的话，我们就得使用WinGet来安装。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在终端中运行这行命令。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>winget</span> install Anthropic.ClaudeCode</span></code></pre>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXhNfFdwdLj2ialffWeesanSCMWBsn1oMf59ASxUkeCbuJtibsqxbHgkAJJ2ib9aGEU3vcNe00EO5cmrAriarEnSleetriatlML8T5E/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   等他安装成功后，同样可以输入claude，就能看到已经安装成功了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXQG2jTMicQnHqALrfgCIpC4VseT9fD5Xn6PemADdTyJ7VQZ3Cic6DR2DibLkZxQh7nV95JmEc4H4sqib9RcaiaAvckzZUeLK1DupZE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   到这一步，从道理上讲，我们在终端里输入claude，就能进到Claude Code页面了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们这里光装了框架，还没给他安脑子，所以还没法用。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那接下来，我们就需要把他的脑子接上。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 16px; text-align: left; margin-left: 8px; margin-right: 8px;">
 <span style="font-size: 20px;">
  <strong>
   <span style="font-size: 20px; letter-spacing: 0.578px; text-decoration: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);">
    <span>
     二. 接模型
    </span>
   </span>
  </strong>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   如果是有Claude账号的，直接登录就行了，这里我就不细说了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为理论上你已经有Claude账号了，你也不会来看这个保姆教程。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以，为了让国内所有的小伙伴都能用上，这里我用国产模型GLM-5.1来举例子。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为GLM-5.1是目前我用下来觉得国内效果最好最接近Claude Opus 4.6体验的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然，你要是没抢到他们的coding plan的话，用MiniMax M2.7和K2.5也都不错，K2.6 code应该也快出了，感觉kimi也会有一波飞跃，推荐大家可以蹲一下。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后GLM5.1这块，智谱官方有提供一句话命令来安装，特别简单。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>npx</span> <span>@z_ai</span>/coding-helper</span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但这里，为了方便大家也能接入其他模型并且随意切换，所以，我们教大家一个更通用的方法，也就是，用CC Switch。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还是分Mac和Windows。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   1. Mac
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在Mac上，他的安装就两行命令，第二行命令同样因为格式原因，直接复制粘贴会报错。辛苦大家手敲一下，或者发给claude让他改了，再粘贴到终端。
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
 <pre class="code-snippet__js"><code><span>brew tap farion1231/ccswitch</span></code><code><span>brew install <span>--cask</span> cc-<span>switch</span></span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在终端粘贴，回车运行。
  </span>
 </span>
</p>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWV3eficHlFswIQn9ibyvHjYdTjkp4tjgSyIAH5zAWOjyPJlQweGYasILUNYibaNhIz5Ficic8EibRY8k6u5waBmVpuoVXH7mxkpE4jg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="width: 680px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   等他装好就成了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px; text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUiantpxmaS060YVygmLUCc2cFhVdjsORicAXgia4CDL1v1sCJ0Z2mhaHrjMbtF3BC5MA3EY18eLMu3gfvGuzOta0mHFl39ChibRHY/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=19" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   2. Windows
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Windows的话，推荐直接去下面的链接下载安装包。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   https://github.com/farion1231/cc-switch/releases
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVWNmOuJIseYcHdicYUs7icYWQ51OmunicMmlGWyNIl3iajWTEWHfmappfx9tfyadFGg4TZiaZ2gF8k7fyeqBD7f0lyfahcEyP8iaLFg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=20" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px; font-weight: bold;">
   如果你进不去github，那我也给大家准备好了本地安装包，你对着公众号后台回复cc就会自动给你发下载链接了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   下载后双击运行，然后可以一路next到底，就安装好了。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUEKC50K9vKHXCG1FQe5YrxmGNJiaQtrZLgVtibyNEHOUPTJyvRDADlBKWLs1gsLX8pMJFKicDcRHS25JvMkyHRCjOUB3FoGib7uYM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=21" style="width: 664px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   后面的操作Mac和Windows一样，就不分开说了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   装好后，我们打开他。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一进去能看到，这玩意其实不仅适用于Claude Code，Codex、小龙虾这些都能用。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为我们这里还没配置，所以目前只有Claude官方的模型配置。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在Claude那一栏下面，我们点右上角的加号，新增模型配置。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqXSGiaESsYrf9ricqHXTFTzianLW3yozt1gDqgAw1R9JzTL8X4ibzPH3nz7KR4ZibE7cJS80rAtFPTOBzKuia2mctibibiaYOGSiaExOpgiaE/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=22" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后选择我们想要使用的模型，这里我选的是GLM国内版。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUWbbcvYKrOiblKPWJJibdW1iahviapfbuIerE0wWhg3MwFUmScSQzOH6lL7LOxWRDrIjNcUV8peNicerYqvpCLI9vd2libIOQQGcrgs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=23" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   接着要填的就两部分，API key（
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   这块如果不知道什么是API Key的，可以去直接问你能用上的任何AI，他们都会帮你解决）和模型配置，其他的他都会自动帮我们填好。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWTt7BsVqAUkVIttVicVDpK5lSFTrvYExiclmmDJHMM9GX0gzjoGB7TuLVCSUzm9s8bLyQsmFz7wCySeTvaHqLBZEdYjjy0uEibwM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=24" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   填好之后，我们点击右下角的添加就行.
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWyic9OwWea1bE4vOST7PqWKZGiaHibtVm0GFKJfGLic1XNj4YKY8eD1NDnzQKvHoJLEyiafib0P81RJ2vOfmTDtR3mTpzqljvj7Kbmk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=25" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   他就会切换到我们配置的模型上。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVzlK0INKnRzO2rPrGsz9yvlf5esFARMj1AuVHkO5mPzXl6lGJxibjq2X6J54KW2dqmh4uN1v5pQNTh7yNF1tbYp8MdpB9QTxaY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=26" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   到这一步，Claude Code的安装和GLM-5.1的接入就完成了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 16px; text-align: left; margin-left: 8px; margin-right: 8px;">
 <span style="font-size: 20px;">
  <strong>
   <span style="font-size: 20px; letter-spacing: 0.578px; text-decoration: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);">
    <span>
     三. 启动Claude Code
    </span>
   </span>
  </strong>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们回到终端，输入claude，回车。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqW9mjM5PHa7taO6Y0VibS29HCETBzr8eFIx5u8oPPrpCgc2EibbeOlt0Sukyu6bcXVelzVkbssdhPRdyQXAMribWUtKpZ9CF5aBtk/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=27" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就可以正常启动claude code了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   第一次使用，会先有一些初始化设置。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如颜色模式，模式下面有代码预览，大家根据自己的喜好来就好。选中回车。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   以后想改，在Claude Code里运行/theme就行。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUKaDCIqdicguH7Jicf6U1ceYxVyOawBMkrIicGN7gDFEsqtxmzFdpwV4XGZqyDtj9jl6qWibKvmVcmZvrlwz1U5fibfe7DnFiayq32U/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=28" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   接着是安全提示。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXTgciaIS2cP2tcqNg9qN2NYkTics5icYAmsNnGoSiajwbia1uiak8kZjI4IUAh2vgw8ju2gyeAjFO0ibmUzDD79214OoVA68Yds5zUEo/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=29" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就两点。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一个是Claude会犯错，它生成的代码、它要执行的命令，你都应该过一眼再放行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一个是只在你信任的代码库里用Claude Code，避免提示词注入攻击。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们直接回车进入下一步。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   是问我们是否使用Claude Code的终端设置。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqV9pejhicgaicO6oKOyhgCA7HS0SH9NJLMcMKnvsX5QCOvyicicbS7zKfTUXrXTvhG4AeXVmYB9VeJcpymHMhWnfkkFj5ySzfapNgI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=30" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里，直接使用他推荐的终端设置就可以。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   其实就是他想帮你启用两个东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   快捷键实现在终端里换行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   另一个是Visual bell，视觉提示。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   也就是Claude跑完任务或者需要你确认的时候，终端窗口的页面会闪一下，
  </span>
  Dock图标
  <span style="font-size: 16px;">
   会弹跳一下，提醒你。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最后一步，就是和你确认当前所在目录，是否可以信任。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqUQuL1vLhiaAmLnJlWXQc4hnvD8JUwdvIib3NWCE3NwfTOsRj3OzKlbPKu9bfBYTibBjf0HpyZBtgFTRrBG0H3ic89xP7NxZ3gcz8E/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=31" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里选择是，然后回车。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们就终于来到接入GLM-5.1的Claude Code的对话界面了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUXtGEr3Egj53wKzmkJbGmb79Yicwdj7A7wI7RVgkZHdjBR9unpvtPmXPDJMgjchVuvDU4oHztUP7rbOnOWSqFJXrFdlzKYmkpQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=32" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   后续想要切换模型，在CC Switch里面配置好，在Claude Code里面用/model切就行。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqWdEM7aqqqsMMpFIXrvTnxOTLgyxXBriadtdgA00TKL7vx7VJwjKdrS1k15kuIO6zClfFRUqfYibpAUeWo6a97CcOEic4UoOl7JAY/640?wx_fmt=jpeg&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=33" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   至此，所有的安装接入操作就完成了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   后续用的话，直接在终端输claude就行了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这里推荐大家用下面这行命令，特别是开发的时候，不然点各种allow会点到你怀疑人生。
  </span>
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>claude <span>--dangerously-skip-permissions</span></span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后我们启动的时候，因为上下文设计，为了让他有约束，更加的专注，所以我们是需要对着一个文件夹进行启动的，而不是直接在根目录启动Claude Code。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我自己就分了一下目录，文稿是我拿来做知识创作了。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXA6icguBKJerzyia8ThCGbAfDZ2OV0EBHuIxIyecGkUrxlhMrL0a1lYmbGOf1iacDIcgCnR8y4vDuPHRrPn01mmqR0oyfTicVNHGk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=34" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还有一个code文件夹，下面都是我自己开发的各种各样的产品。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWvkKM5ZIqEJVickwOzmyIdnicLJibRpkbxY4rk3PaWwPib02ibR8LYc7mVwKrr1UJ1BgARAkMSn7FdQwaAqibcXEw66hE0tmRNiaR4yM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=35" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在命令行中对着一个命令行启动Claude Code也特别简单。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就是cd命令，这块Mac和Windows是一样的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如我要进入知识库这个文件夹进行创作。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那就打开终端，输入cd，然后一定要记得按一下空格，再把你的文件夹，直接拖进去。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW6GicDerHfNtibd2iaO2qib84KqUt9COLADQyOKPUWuUZJeORgJjySzkxU1PU4YVNbfBS0yibXkjcxG2xdnpnebWZiaNwUhhXVOtK1Y/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=36" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   按下回车，就算是进入这个文件夹了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后这个时候再用命令启动Claude Code就可以。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX2yIxHxyF2XN4PEJX43oeOvvh899Wfb7xicjCFM20TQbUxq3OW613fJS7H7YXLf8V91cLtsrVd1s9n79Ngys5Fekgv6eqORRnY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=37" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你就会进入到这个文件夹下，它默认就只在这个文件夹下工作，默认读取你这个文件夹下的所有文件。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWY02VojjeY67kibibtXNYc1xhJkgK1iala01zVCs3QubGvNa1TgsyHoNdmV9P221wxUTibgIbCWy0pfiaibVlRjfLHE3kZPfJ14Km0Q/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=38" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这样其实上下文污染更小，也更专注，换句话说，就是更聪明。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 16px; text-align: left; margin-left: 8px; margin-right: 8px;">
 <span style="font-size: 20px;">
  <strong>
   <span style="font-size: 20px; letter-spacing: 0.578px; text-decoration: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);">
    <span>
     四. 写CLAUDE.md
    </span>
   </span>
  </strong>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   学会启动之后，其实你就可以正式的对话了，随便让他干活就行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但还有个规范和你在深度使用之前，有一个很重要的习惯，我觉得是需要让你先设置的，不要再踩我走过的老坑，先定好你的CLAUDE.md文件。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而在我看来，这甚至是学会启动Claude Code之后，第一件该做的事。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在上具体写法之前，我还是先和大家聊一聊CLAUDE.md是个啥。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个东西，它不简单是一份文件，它是一个从上往下分层穿透的约束体系。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就像我之前用过的这张图。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXs5iauRkDLI4fTetzfa3bsegmMWCBYUg3b3V9qPN7ZJtGcT6iaafiaco8RO4Tztk8UWTDhsMiaSfgVfJ2JQk095jevSvOFsUWd2jA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=39" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   刚装完，我们应该去管的两层，就是全局CLAUDE.md和项目CLAUDE.md。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   全局CLAUDE.md，放在用户总目录的Claude Code根目录下面，~/.claude/CLAUDE.md。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVgdfkkNK7KNa8zGNLwPI491bywdjgDcacmFDx7MppnxgAicFwusicQVoqicheZ45PewC7NmgRjPXwMsJ4ZtoriaVfmJ1hib5IeYgzw/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=40" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   只要你打开Claude Code，不管你进的是哪个项目，它都会被自动加载和遵守。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这是他的顶层规范。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它可以解决的是你是谁、你做事的原则、你希望他用什么方式跟你协作这一层的问题。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而项目级CLAUDE.md，放在每个项目的根目录下，路径就是项目目录/CLAUDE.md。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUnyBbjUNwfSoIlITxMxke5JTklPHYwicay6Sd0syibgoy8YBHvOyCp6Tua4MfNFQ2bDiarSI5bBB608iciaKjUNrIgAtuibCTeDCQ1Y/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=41" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它只在你打开这个项目的时候才会被加载。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   它解决的是这个具体的项目要怎么干，有什么特殊约定这一层的问题。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们先来聊全局CLAUDE.md，也是第一个需要定好的东西，但是到底该往CLAUDE.md里写什么、怎么写、写多长、放哪里，很多人其实不清楚，对于非开发者来说，我也分享一下我的经验。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   关于长度，CLAUDE.md不是越长越好，反而是要尽量精简。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你的CLAUDE.md写得太长，后半段的内容它会直接忽略掉。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   具体的红线数字是这样的，超过80行，Claude开始遗漏部分内容，最多最多，一定不要超过200行。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   之前的一篇文章，我也给大家看了我的全局CLAUDE.md文件里面都是哪些内容。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在我的内容的基础上，我又迭代了一下，为大家准备了一份模板。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   里面都是一些我觉得一份不错的全局CLAUDE.md应该有的东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大家只需要在关于我里面，写上自己的内容，其他基本都是可以直接复用的。
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
 <pre class="code-snippet__js"><code><span><span>## 关于我</span></span></code><code><span>[你的名字 / 身份 / 职业背景，非程序员的话一定要写出来]。</span></code><code><span>我用 Claude Code 做 [具体用途 1] 和 [具体用途 2]。</span></code><code><span><br /></span></code><code><span><span>## 思维原则</span></span></code><code><span>所有决策从问题本质出发，不因「惯例如此」照搬。</span></code><code><span>回到问题本身：要解决什么？最直接的路径是什么？从零设计会怎么做？</span></code><code><span>不要谄媚。不要夸我的想法好、不要说「这是个很好的问题」、不要开头加「当然可以」。</span></code><code><span>给我真实判断，方案有问题直接指出来。发现更好的做法直接说，不用等我问。</span></code><code><span><br /></span></code><code><span><span>## 约束先行</span></span></code><code><span>无论开发项目还是知识管理项目，第一步永远是建规则：新项目先写 CLAUDE.md，新目录先定结构约定（什么放哪、怎么命名、何时清理）。</span></code><code><span>没有规范的工作空间不动手。已有规范的项目，严格遵守其 CLAUDE.md 中的约定。需要调整规范时先改文档、再改实践，不要反过来。</span></code><code><span><br /></span></code><code><span><span>## 沟通方式</span></span></code><code><span><span>-</span> 默认中文，代码、命令、变量名用英文</span></code><code><span><span>-</span> 结论先行，再给理由，不要先铺垫背景</span></code><code><span><span>-</span> 遇到模糊需求，先给最合理的方案，再问要不要调整</span></code><code><span><span>-</span> 不要问「你确定要这样吗」，除非命中下方红线</span></code><code><span><br /></span></code><code><span><span>## 自主边界（红线，必须先问我）</span></span></code><code><span>以下操作即使在 auto-accept 模式下也必须停下来问我：</span></code><code><span><span>-</span> 删除文件、目录或 git 历史</span></code><code><span><span>-</span> 修改 .env、密钥、token、CI/CD 配置</span></code><code><span><span>-</span> 数据库 schema 变更或数据迁移</span></code><code><span><span>-</span> git push、git rebase、git reset --hard、强制推送</span></code><code><span><span>-</span> 安装新的全局依赖或修改系统配置</span></code><code><span><span>-</span> 公开发布（npm publish、部署到生产、发文章等）</span></code><code><span><br /></span></code><code><span><span>## 通用工程纪律</span></span></code><code><span><span>-</span> 改完主动跑验证（具体命令见各项目 CLAUDE.md），不要只改不验</span></code><code><span><span>-</span> 不要为了让代码跑起来注释掉报错或加绕过标记，找根本原因</span></code><code><span><span>-</span> 密钥、token、密码不进代码、不进 commit、不进日志</span></code><code><span><span>-</span> 大改动前先在 Plan Mode 出方案，我确认后再动手</span></code></pre>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一共30多行，分成六个部分。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这六个块都有一个共同特征，就是跨项目通用。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   全局的CLAUDE.md定好了，我们顶层的规范就有了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那至于下一层，项目CLAUDE.md。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   拿我自己举例。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我主要用Claude Code来做开发和知识管理。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如我的code/my目录下就有一个CLAUDE.md，这个的作用，主要就是my文件夹下，经常coding的都是一些可能一次性的、或者我实验性质的乱七八糟的东西，其实都非常的小，所以我真的懒得每次都在my下新建一个文件夹。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWKveictMlNZhS0JrCGhtEJfa0DjMibCNuCVyaQxJ9fRJlPyqTybaaic5UdfvicX0eOa9DujjCwWiaPxkQoL8gcMZWoJBZtoUibkT4Mo/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=42" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  所以我现在常用的做法，就是直接cd到my文件夹启动，然后愉快的开始说出我自己的需求帮助我coding，那有了这个CLAUDE.md文件之后，他就会自己判断这是不是一个新产品，如果是的话，那就直接帮我新建一个文件夹开始做，这样整个文件管理，就会变得井井有条了。
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWfqoFcKfbm8CgB1Ca8KoU1Bp7iabcd7bXT3MYRjca6CTTtIJBGvib4qV8H0NroaEgaAEMW32mHhiaPjYtP7sfpGSsw0TkaIYuTxQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=43" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而这个文件其实也完全不用你自己写，你就直接打开那个文件夹，然后和Claude Code聊就行，你直接把你的需求，和你在意的事情，和他探讨，让他给你写一份就OK了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXrRt44hVEEpfWLvHciauS4D0cX9vkU3woIqM9PmY2iclyo4leO6emUdEl7BpDicXU7p56XMAiarPJ2k8KrRibJRuh6IgVicDUiaeyMTc/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=44" style="height: auto !important; width: 585px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我自己这几天也在好好跟我的Claude Code制定各种规范，整理我之前遗留下来的各种屎山。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那如果你的电脑上现在还什么都没有的话，那就更方便了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这也是我一直强调约束先行、规范先行的原因之一。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   约束定好了，那就真的可以开始玩起来了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   而skills，plugins，常用命令、功能这些。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我这里就不展开了，我也写过了很多相关的文章，感兴趣的小伙伴可以直接去对应着搜索关键词就行。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUKTgwUia1jlw7nKDtSicTbTOwzKPobpbvxyibxuibdicNuKHMuwHfXcMdWE63XpMc3hVznZ9iaEicHqyO0YXKrVgBPG71yaEmczHDBqs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=45" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 16px; text-align: left; margin-left: 8px; margin-right: 8px;">
 <span style="font-size: 20px;">
  <strong>
   <span style="font-size: 20px; letter-spacing: 0.578px; text-decoration: none; background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);">
    <span>
     写在最后
    </span>
   </span>
  </strong>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   终于把这篇拖了很久很久的保姆级Claude Code教程写完了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Claude Code，就是我推荐你的当前AI版本的毕业工具。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你根本无需使用各种乱七八糟的那些Agent，用好Claude Code，你就真的能感受到，什么是最牛逼的Agent了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   希望大家都能愉快创造。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   做出这个时代。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   属于你自己的作品。
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
   &gt;/ 作者：卡兹克，tashi
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
