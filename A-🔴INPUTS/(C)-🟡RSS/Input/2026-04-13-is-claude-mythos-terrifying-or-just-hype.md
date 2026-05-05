---
title: "Is Claude Mythos “Terrifying” or Just Hype?"
url: "https://calnewport.com/is-claude-mythos-terrifying-or-just-hype/"
source: "Cal Newport"
date: 2026-04-13
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章批判性地审视了《纽约时报》专栏作家托马斯·弗里德曼对Anthropic新AI模型Claude Mythos的恐慌式报道，指出其所谓“突破性”漏洞挖掘能力并非新现象，而是自2024年GPT-4起就已被安全界广泛关注和研究。Anthropic限制Mythos公开发布的理由是其强大的代码安全缺陷识别能力，但作者强调该能力属于现有大模型演进的自然结果，而非突兀跃升。文章呼吁公众理性看待AI新闻，避免被夸大叙事误导，尤其需区分真实技术进展与媒体焦虑渲染。

---

<p>Last week, millions of <em>New York Times</em> readers were subjected to <a href="https://www.nytimes.com/2026/04/07/opinion/anthropic-ai-claude-mythos.html">​an alarming column​</a> by Thomas Friedman. “Normally right now I would be writing about the geopolitical implications of the war with Iran,” Friedman begins, before soon continuing, “but I want to interrupt that thought to highlight a stunning advance in artificial intelligence — one that arrived sooner than expected and that will have equally profound geopolitical implications.”</p>



<p>The “stunning advance” was the release of Anthropic&#8217;s new LLM, named Claude Mythos. In a lengthy <a href="https://www.anthropic.com/glasswing">​press release​</a>, Anthropic announced that the model would be made available to a consortium of business partners, but not to the general public. To justify this decision, Anthropic cited their concerns about its effectiveness at finding security vulnerabilities in source code, noting: “AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.”</p>



<p>They go on to explain that Mythos “has already found thousands of high-severity vulnerabilities, including some in <em>every major operating system and web browser</em>.<em>”</em></p>



<p>This announcement clearly rattled Friedman, who called Anthropic’s decision not to release the model a “terrifying warning sign,” writing:</p>



<p>“Holy cow! Superintelligent A.I. is arriving faster than anticipated, at least in this area…If this A.I. tool were, indeed, to become widely available, it would mean the ability to hack any major infrastructure system — a hard and expensive effort that was once essentially the province only of private-sector experts and intelligence organizations — will be available to every criminal actor, terrorist organization and country, no matter how small.”</p>



<p>Friedman was far from alone in this concern. Many major news outlets expressed similar unease about this scary new development, including <a href="https://finance.yahoo.com/video/is-anthropics-claude-mythos-an-ai-nightmare-waiting-to-happen-203000700.html">​one particularly anxiety-provoking headline​</a> that asked if Mythos was an “AI nightmare waiting to happen?”</p>



<p>So, what’s really going on here?</p>



<p>I thought it was worth taking a moment to look closer, not just to address the specific worries about Mythos, but also to help recalibrate, more generally, how those of us seeking depth in a distracted world should consume AI news.</p>



<p class="has-text-align-center">~~~</p>



<p>When I talked to people who were spooked by Friedman’s column, they tended to be under the impression that this ability to find and exploit security vulnerabilities was a new phenomenon; a skill that emerged unexpectedly in Mythos, &#8220;terrifying&#8221; those who studied it.</p>



<p>In reality, security researchers have been worried about using LLMs for this purpose since the beginning of consumer LLMs.</p>



<p>Back in 2024, for example, IBM researchers published <a href="https://arxiv.org/abs/2404.08144">​a splashy study​</a> about using GPT-4 to attack security vulnerabilities. They found that GPT-4 successfully exploited 87% of the vulnerabilities that it was presented, as compared to close to 0% for GPT 3.5. “Our findings raise questions around the widespread deployment of highly capable LLM agents,” they concluded.</p>



<p>To be fair, in the case of GPT-4, researchers were assessing whether an LLM could write code to exploit a known vulnerability. Mythos, however, can also find these vulnerabilities from scratch. But this isn’t new either.</p>



<p>Accompanying the release notes for Anthropic’s earlier Opus 4.6 LLM was <a href="https://www.reddit.com/r/Anthropic/comments/1r05i5g/opus_46_found_over_500_exploitable_0days_some_of/">​the observation​</a> that Anthropic’s security team used the model to find “over 500 exploitable 0-day [vulnerabilities], some of which are decades old.” This is almost word-for-word what Anthropic said last week about Mythos, the main difference being that they replaced 500 with “thousands.”</p>



<p>We are not, therefore, talking about a new capability, but rather one that has been around for multiple years.</p>



<p>The relevant question then becomes, how much better is Mythos at finding vulnerabilities? It’s hard to tell for sure because Anthropic has kept their new model private. They did, however, release that Mythos scored 83.1% on a well-known cybersecurity benchmark. For comparison, Opus 4.6 scored 66.6% on this same test.</p>



<p>In general, benchmark results should be taken with a grain of salt as they represent specific (often narrow) tests that researchers can tune their models to pass. But even if we accept that this particular measure is useful, a sixteen percentage point increase seems to represent solid incremental progress more than a nightmarish leap.</p>



<p>When we turn our attention to actual results, the waters become even murkier. In a recent Substack post (<a href="https://garymarcus.substack.com/p/three-reasons-to-think-that-the-claude">​which is worth reading​</a>), Gary Marcus rounds up responses from security researchers who took a closer look at the specific exploits that Anthropic reported that Mythos discovered. They were not impressed.</p>



<ul class="wp-block-list">
<li>Philo Groves, for example, <a href="https://x.com/philogroves/status/2042195139477557499?s=61">​noted​</a> that Mythos’s attention-grabbing attack on the Firefox browser required certain common security features to be disabled, and it built on results previously discovered by Opus. (“Shocker,” he concludes sardonically.)</li>



<li>The CEO of the AI company HuggingFace then <a href="https://x.com/clementdelangue/status/2041953761069793557?s=61">​reported​</a> that they took all of the specific vulnerabilities that Anthropic highlighted and “ran them through small, cheap, open-weight models.” What did they find? “Those models recovered much of the same analysis.”</li>
</ul>



<p>Since Marcus published his essay, I’ve come across several more similar findings:</p>



<ul class="wp-block-list">
<li>The AI security expert Stanislav Fort ran <a href="https://x.com/stanislavfort/status/2041922370206654879">​an experiment​</a> to see if existing, cheap open-weight models could find the same vulnerability in FreeBSD (an open-source operating system) that Anthropic touted as evidence of Mythos’s scary abilities to uncover bugs that had been hiding for decades. The result: all eight existing models they tested discovered the same issue.</li>



<li>Meanwhile, the renowned security researcher Bruce Schneier <a href="https://www.youtube.com/watch?v=PsKVSHjres4">​weighed in​</a>, similarly concluding: “You don’t need Mythos to find the vulnerabilities they found.”</li>
</ul>



<p>And of course, it doesn’t help that a week before Anthropic released this supposedly super-powered vulnerability detector, they accidentally leaked the Claude Code source, and security researchers immediately found <a href="https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/">​serious vulnerabilities​</a>. (I guess Anthropic forgot to use Mythos to clean up their own software…)</p>



<p class="has-text-align-center">~~~</p>



<p>What’s really happening?</p>



<p>It’s fair to say that LLMs have created <em>significant</em> cybersecurity concerns that researchers have been scrambling to address in recent years. It’s also fair to say, however, that we don’t yet have evidence that Claude Mythos significantly changed this reality. If anything, some of the early independent testing by security researchers implies that Mythos might be better understood as a version of Opus 4.6 tuned to perform better on a handful of benchmarks. And yet, many still took Anthropic at their word and covered this model’s release as a catastrophic event.</p>



<p>In a <a href="https://www.youtube.com/watch?v=mcN1VTTIjQs">​recent video​</a>, the AI commentator Mo Bitar compared Anthropic’s model rollouts to Apple iPhone launches, where every year they resell you the same product with minor improvements. “Except here,” he adds, “the product is existential dread.”</p>



<p>And we keep falling for it.</p>



<p>I think we’ve entered a stage where we need to almost entirely discount any claims made by the AI companies themselves <em>until</em> we can independently verify what’s actually going on.</p>
<p>The post <a href="https://calnewport.com/is-claude-mythos-terrifying-or-just-hype/">Is Claude Mythos “Terrifying” or Just Hype?</a> appeared first on <a href="https://calnewport.com">Cal Newport</a>.</p>

## 中文译文

上周，数百万《纽约时报》读者读到了托马斯·弗里德曼（Thomas Friedman）一篇令人警觉的专栏文章。文章开篇写道：“通常此刻，我本该撰写有关美伊战争地缘政治影响的评论”，随即话锋一转：“但我希望暂时中断这一思路，来重点强调一项人工智能领域的惊人突破——它比预期更早到来，且将同样深刻地重塑地缘政治格局。”

这项“惊人突破”，指的是Anthropic公司新发布的大型语言模型（LLM）——“克劳德·神话”（Claude Mythos）。在一份冗长的新闻稿中，Anthropic宣布该模型将仅向一个由企业合作伙伴组成的联盟开放，而不会面向公众发布。为解释这一决定，Anthropic援引了其对模型在源代码中发现安全漏洞能力的深切忧虑，指出：“人工智能模型的编码能力已达到如此高度，以至于在发现并利用软件漏洞方面，它们已超越除极少数顶尖人类专家之外的所有人。”

该公司进一步解释称，“神话”模型“已发现数千个高危漏洞，涵盖所有主流操作系统与网络浏览器”。

这一公告显然令弗里德曼深感震动。他将Anthropic拒绝公开发布该模型的决定称为“一个令人恐惧的危险信号”，并写道：

“天哪！超级智能人工智能的到来速度，远超我们此前预期——至少在这一领域是如此……倘若这款人工智能工具真的被广泛获取，那么攻破任何重大基础设施系统的能力——过去这是一项耗时耗力、成本高昂的工作，几乎仅为私营部门顶尖专家与情报机构所专有——将落入每一个犯罪分子、恐怖组织乃至无论大小的国家手中。”

弗里德曼绝非孤例。众多主流媒体亦表达了类似的不安情绪，其中一则尤为令人焦虑的标题甚至发问：神话模型是否正是一场“一触即发的人工智能噩梦”？

那么，事情的真相究竟如何？

我认为，值得花点时间深入探究一番——不仅为厘清围绕“神话”模型的具体担忧，更旨在帮助我们这些身处纷扰世界、渴求深度思考的人，重新校准自己消费人工智能新闻的方式。

~~~

当我与那些被弗里德曼专栏吓到的人交谈时，他们普遍误以为：这种发现并利用安全漏洞的能力是一种全新现象，是“神话”模型意外涌现的一项技能，令研究者们“不寒而栗”。

事实上，自消费级大语言模型问世之初起，安全研究人员就已开始担忧其被用于此类目的。

例如，早在2024年，IBM研究人员便发表了一项引人注目的研究，探讨如何利用GPT-4攻击安全漏洞。他们发现，GPT-4成功利用了其所面对漏洞中的87%，而GPT-3.5的对应成功率则接近于零。“我们的研究结果引发了人们对部署能力极强的大语言模型代理的广泛质疑”，他们最终总结道。

公允而言，在GPT-4案例中，研究人员评估的是：大语言模型能否编写出利用已知漏洞的代码；而“神话”模型则不仅能利用已知漏洞，还能从零开始自主发现漏洞。但这一能力本身也并非新鲜事物。

就在Anthropic早前发布的Opus 4.6大语言模型更新说明中，就附有一段观察性评述：“Anthropic的安全团队曾利用该模型发现了500多个可利用的‘零日漏洞’（0-day vulnerabilities），其中一些漏洞甚至已潜伏数十年。”这段描述与Anthropic上周关于“神话”模型的声明几乎一字不差，唯一的区别在于，数字从“500”换成了“数千”。

因此，我们谈论的并非一种全新能力，而是一项早已存在多年的技术。

真正关键的问题于是变成：相比此前模型，“神话”在发现漏洞方面究竟强了多少？由于Anthropic将这款新模型严格保密，我们很难确切判断。不过，他们确实公布了“神话”在一项广为人知的网络安全基准测试中取得了83.1%的分数；作为对照，Opus 4.6在同一测试中得分为66.6%。

一般来说，基准测试结果需谨慎看待，因为它们往往代表特定（且常属狭窄）的测试场景，研究人员完全可以有针对性地调优模型以通过测试。即便我们姑且承认这一指标确有价值，十六个百分点的提升，也更应被理解为稳健的渐进式进步，而非一场令人毛骨悚然的飞跃。

当我们转向实际成果时，情况则愈发扑朔迷离。在近期一篇值得细读的Substack文章中，加里·马库斯（Gary Marcus）汇总了多位安全研究人员对Anthropic所宣称的“神话”模型具体攻击案例的深入分析。他们的反应并不热烈。

例如，菲尔洛·格罗夫斯（Philo Groves）指出，“神话”模型对Firefox浏览器那场夺人眼球的攻击，需以禁用若干常见安全功能为前提，且其技术基础实为Opus此前已发现的结果。（他略带讽刺地总结道：“真令人震惊啊。”）

HuggingFace这家人工智能公司的首席执行官随后报告称，他们将Anthropic所重点列出的所有具体漏洞全部提取出来，“交由一批小型、廉价、开源权重的模型进行复现”。结果如何？“这些模型重现了其中大部分相同的分析结论。”

自马库斯发表这篇评论以来，我又陆续接触到更多类似发现：

人工智能安全专家斯坦尼斯拉夫·福特（Stanislav Fort）开展了一项实验，检验现有廉价开源权重模型能否像Anthropic所吹嘘的那样，独立发现FreeBSD（一款开源操作系统）中那个“潜伏数十年之久”的漏洞——而Anthropic正是以该漏洞作为“神话”模型恐怖能力的佐证。实验结果是：他们测试的全部八款现有模型，无一例外都成功识别出了同一问题。

与此同时，著名安全研究员布鲁斯·施奈尔（Bruce Schneier）也公开发表观点，得出相似结论：“你根本不需要‘神话’模型，就能找到他们所声称发现的那些漏洞。”

当然，以下事实更削弱了Anthropic的可信度：就在该公司发布这款所谓“超能漏洞探测器”的一周前，他们竟不慎泄露了Claude Code的源代码；安全研究人员立刻从中揪出了若干严重漏洞。（看来Anthropic忘了先用“神话”模型帮自家软件“打扫卫生”……）

~~~

那么，真实状况究竟是什么？

我们可以说，大语言模型的确引发了严峻的网络安全关切，近年来研究人员一直在争分夺秒地应对；但同样公平的是，目前尚无确凿证据表明“克劳德·神话”显著改变了这一现实。相反，部分早期独立测试结果暗示，“神话”或许更应被理解为Opus 4.6的一个优化版本——仅在少数几项基准测试中表现更佳。然而，仍有许多人轻信Anthropic的说辞，并将此次模型发布渲染成一场灾难性事件。

在最近一段视频中，人工智能评论员莫·比特尔（Mo Bitar）将Anthropic的模型发布策略比作苹果iPhone的年度发布会：每年都在兜售几乎相同的产品，仅附带微小改进。“只不过这一次，”他补充道，“产品本身就成了‘生存性恐惧’。”

而我们却一再上当。

我认为，我们已步入这样一个阶段：在能够独立验证实际情况之前，我们几乎应全盘搁置人工智能公司自身所作的一切声明。

《克劳德·神话：是“令人恐惧”，还是纯属炒作？》一文首发于卡尔·纽波特（Cal Newport）个人网站。
