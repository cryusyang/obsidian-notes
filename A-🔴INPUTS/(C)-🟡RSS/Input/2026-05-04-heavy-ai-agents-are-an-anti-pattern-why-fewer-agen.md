---
title: "Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins"
url: "https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文批判当前流行的“AI代理动物园”设计模式，指出构建大量高度专业化代理反而导致认知负担重、系统脆弱、维护困难等问题。作者主张采用“精简代理+深度技能库”的架构：代理仅负责规则与流程控制，而技能作为可按需加载的工具，具备确定性、复用性和上下文聚焦性。这种分离设计提升了灵活性、可维护性与长期可持续性，使AI系统真正服务于工作而非成为管理负担。

---

<img alt="Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins" src="https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-cover-1.png" /><p>The shape of an AI system that holds up: lean agents, deep skill libraries, and a clear separation between rules and tools.</p><p>In this article, I want to convince you that the AI agent rosters most people are building today are an anti-pattern. The shape that actually scales is the opposite: fewer agents, with more skills. Let me explain why, and how I think about this in my own setup.</p><h2 id="introduction">Introduction</h2><p>Every week, I see someone go all-in on AI and proudly announce their new lineup of fifteen specialized agents. A research agent. A writing agent. A reviewer agent. A planning agent. A &quot;senior engineer&quot; agent. A grumpy critic, a caveman, etc.</p><p>Then they spend more time choosing which one to use than actually using AI to get work done.</p><p>This is NOT just a productivity problem. It&apos;s a design problem. And the longer I work with <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI Agents</a> and <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net">AI Agent Skills</a>, the more convinced I am that heavy, deeply specialized agents are the wrong default. Most of the leverage comes from going the other way.</p><h2 id="tldr">TL;DR</h2><p>Fewer agents, paired with rich skill libraries, beat heavy specialized rosters on every axis that matters: cognitive load, flexibility, <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net">Context Budget</a>, determinism, and maintenance. Agents should hold the rules of the game. Skills should be the tools. The two evolve at very different rates, and conflating them creates fragile systems you eventually stop using.</p><ul><li>Heavy agents create cognitive overhead. The roster itself becomes a thing you manage.</li><li>Specialists are brittle. Real tasks straddle boundaries.</li><li>Skills load on demand, keeping the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a> focused and lean.</li><li>Skills add the determinism that probabilistic models lack: templates, scripts, embedded programs.</li><li>Skill descriptions auto-trigger loading based on the request, so context stays relevant.</li><li>Different prompts pull different skills into play. Same agent, different result.</li><li>Agents = rules of the game. Skills = the toolbox.</li><li>Updating one skill improves every agent that uses it (see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net">AI Skill Composability</a>).</li><li>Rosters of specialists fragment context and force multi-agent shuffles.</li><li>Lean agents plus deep skill libraries are the shape that holds up over time.</li></ul><h2 id="the-agent-zoo-problem">The agent zoo problem</h2><p>The first issue with agent-heavy designs is human, not technical.</p><p>Once you cross five or six agents, the roster itself becomes a thing you manage. You have to remember what each one does, when to reach for it, how it differs from its neighbors, and why past-you thought it deserved its own slot. Worse, specialized agents push you into multi-agent shuffles. Spin up the research agent. Copy the result into the writing agent. Hand that to the reviewer. Pray nothing got lost in translation.</p><p>At some point, you stop using AI to do work. You start managing AI to do work. And it&apos;s quite SAD when that happens.</p><h2 id="specialization-is-brittle">Specialization is brittle</h2><p>The pitch for specialized agents is that domain knowledge makes them better. It does, at exactly the slice of work they were tuned for.</p><p>The problem is that real tasks don&apos;t respect those slices. The &quot;writing&quot; task turns out to need code. The &quot;research&quot; task turns out to need a diagram. The &quot;code review&quot; task turns out to need a refactor. A specialist hits its edge fast, and when it does, you either context-switch to another agent or watch the specialist do an awkward impression of one.</p><p>A general agent with a deep skill library doesn&apos;t have this problem. It picks up what it needs as the conversation unfolds (i.e., the agent itself becomes the orchestration layer). The flexibility comes from how a session begins. The way you open the conversation, the way you frame the problem, naturally pulls different skills into play. Same agent, different framing, different toolchains activated, different outcomes. That&apos;s not a workaround; that&apos;s the feature.</p><h2 id="skills-keep-agents-lean">Skills keep agents lean</h2><p>Heavy agents are expensive in context. Every line of personality, instructions, and embedded knowledge inside an agent&apos;s definition takes up space in the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a> before any actual work begins. A heavy agent walks into the room already half-full.</p><p>Skills flip this around. The agent starts lean. Only the skills relevant to the current request get loaded, triggered by their descriptions matching what you&apos;ve actually asked for. This is exactly the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net">Prompt Lazy Loading AI Design Pattern (PLL)</a> applied to capabilities: defer everything until the moment of use.</p><p>The result: the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a> stops being a bin you stuff capabilities into &quot;just in case&quot; and becomes a focused workspace.</p><h2 id="skills-add-the-determinism">Skills add the determinism</h2><p>AI is probabilistic at heart. For creative work, that&apos;s the whole point. For anything that needs to be reliable, it&apos;s a liability.</p><p>Skills are how you claw determinism back. A skill can be a template. A script. A small embedded program. A precise checklist with &quot;use this when X&quot; baked into the description. The model still picks WHETHER to invoke a skill, but once invoked, the skill itself executes consistently.</p><p>Probabilistic routing, deterministic execution. That&apos;s the combination that makes this work in practice, not just in demos.</p><h2 id="agents-are-the-rules-skills-are-the-tools">Agents are the rules. Skills are the tools.</h2><p>The cleanest mental model I&apos;ve found:</p><ul><li>An <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net">AI Agent Identity</a> holds the rules of the game. How to behave, what to enforce, what to watch for, what it values. These rules should be small and stable.</li><li>Skills are the toolbox the agent reaches into. They can be many. They can change weekly. They can be added, removed, or rewritten without forking a single agent.</li></ul><figure class="kg-card kg-image-card kg-card-hascaption"><img alt="Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins" class="kg-image" height="768" src="https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-mental-model-1.png" width="1376" /><figcaption><span style="white-space: pre-wrap;">A request comes in. The agent is small and stable, just rules and identity. The skill library is wide. Only the skills that match the request light up; the rest stay dormant. That&apos;s the whole runtime story in one picture.</span></figcaption></figure><p>The purest expression of this split is the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net">Receptionist AI Design Pattern</a>: an agent whose entire identity is one rule (route the request to the right handler) and whose body holds zero embedded capability. Everything functional lives in skills or other agents that get pulled in on demand. That&apos;s it. If a near-empty agent can run a whole system through routing alone, your &quot;research specialist&quot; probably doesn&apos;t need a five-hundred-line manual baked in either. The receptionist is the proof-of-concept for &quot;agents = rules&quot;: strip the rules down far enough and the agent almost disappears, while the system around it keeps working.</p><p>Updating one skill instantly improves every agent that uses it. Try doing that with three deep specialists who each carry their own embedded knowledge. You can&apos;t.</p><h2 id="my-own-setup">My own setup</h2><p>This isn&apos;t theory for me. My personal AI system runs on this shape.</p><p>I have a small set of agents (Ghostwriter, Coach, Strategist, Maintenance Worker, plus a few panels of reviewers). Each one is light: a SOUL.md that defines identity, decision framework, and boundaries; a MEMORY.md for accumulated lessons; a DEPENDENCIES.md that lists which skill categories the agent can pull from.</p><p>The skill library is the heavy part. Hundreds of skills, organized by namespace, lazily loaded by description. The Ghostwriter doesn&apos;t &quot;know&quot; how to write a newsletter. It pulls in the newsletter skill when the conversation says newsletter. The same agent can write an article, a thread, a book chapter, or an email, and the right capability lights up each time.</p><p>When I want to add a new capability, I write a skill, not an agent. When I want to change behavior, I update the relevant skill, not three different agents that might or might not have the same logic.</p><figure class="kg-card kg-image-card kg-card-hascaption"><img alt="Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins" class="kg-image" height="768" src="https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-split-1.png" width="1376" /><figcaption><span style="white-space: pre-wrap;">The same role, two designs. The agent on the right pulls capabilities on demand and stays cognitively cheap.</span></figcaption></figure><p>It&apos;s the difference between owning a single multi-tool with great attachments and a drawer full of single-purpose gadgets you can never find when you need them.</p><h2 id="what-about-specialization">What about specialization?</h2><p>Specialized agents excel at one slice and parallelize beautifully when you have orthogonal work. A &quot;review Python microservices&quot; agent really is sharper than a generalist. Multi-agent teams that work in parallel can ship more in less time.</p><p>But IMHO, specialization really belongs in the SKILLS, not the AGENT. You can have a deeply specialized &quot;review Python microservices&quot; skill that the generalist agent loads when the task calls for it.</p><p>As for parallelization, when I genuinely need it, I prefer two general agents sharing one skill library over ten bespoke specialists. The skill library stays the source of truth. The agents are just lightweight runners/&quot;controllers&quot;.</p><h2 id="conclusion">Conclusion</h2><p>If you&apos;re staring at a list of agents and feeling vaguely tired just looking at it, that&apos;s the signal.</p><p>Collapse them. Keep one or two with clear, stable rules. Move the actual capability into skills. Let the agent&apos;s behavior change based on how you open the conversation, not based on which icon you clicked. Over time, the skill library compounds. The agents barely change. That&apos;s the win.</p><p>Fewer agents. More skills. The rest follows.</p><p>That&apos;s it for today! &#x2728;</p><p>PS: I write more on these every week in DeveloPassion&apos;s Newsletter. Subscribe at https://dsebastien.net/newsletter to follow along.</p><h2 id="related">Related</h2><p>If you want to go deeper, look at related ideas:</p><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI Agents</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net">AI Agent Skills</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net">AI Skill Composability</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net">AI Agent Identity</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net">AI Agent Routing</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Distribution?ref=dsebastien.net">AI Agent Distribution</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Permissions?ref=dsebastien.net">AI Agent Permissions</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net">Context Budget</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net">Prompt Lazy Loading AI Design Pattern (PLL)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Engineering?ref=dsebastien.net">Context Engineering</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net">Receptionist AI Design Pattern</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Strategy?ref=dsebastien.net">My Content Strategy</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Types?ref=dsebastien.net">My Content Types</a></li></ul>

## 中文译文

一种经得起考验的AI系统架构：精简型智能体、深厚的技能库，以及规则与工具之间清晰的界限。

本文中，我想说服你：当下多数人正在构建的AI智能体阵容，其实是一种反模式。真正具备可扩展性的架构恰恰相反——智能体数量更少，但每个智能体所掌握的技能更加丰富。接下来，我将解释原因，并分享我在自身AI系统中如何实践这一思路。

引言

每周，我都会看到有人全力投入AI领域，并自豪地宣布自己新组建的十五个高度专业化的智能体阵容：研究智能体、写作智能体、审阅智能体、规划智能体、“资深工程师”智能体、刻薄批评家、原始人……等等。

结果却是：他们花在挑选该用哪一个智能体上的时间，远超真正利用AI完成工作的时长。

这绝不仅仅是一个效率问题，而是一个设计问题。我与AI智能体及AI智能体技能打交道的时间越久，就越确信：臃肿、高度特化的智能体不应成为默认选项；真正的杠杆效应，恰恰来自反向路径。

一句话总结（TL;DR）

在所有关键维度上——认知负荷、灵活性、上下文预算（Context Budget）、确定性（determinism）与可维护性——“少量智能体 + 丰富技能库”的组合，全面优于“臃肿专业化智能体阵容”。智能体应承载游戏规则；技能则应作为工具存在。二者演化节奏截然不同，若将其混为一谈，终将构建出脆弱不堪、最终被弃用的系统。

臃肿智能体带来认知负担：智能体阵容本身反而成了需要管理的对象。

专业型智能体过于脆弱：真实任务天然跨越边界。

技能按需加载，使上下文窗口保持聚焦与精简。

技能弥补了概率模型固有的不确定性缺陷：模板、脚本、嵌入式程序皆可提供确定性保障。

技能描述可自动触发加载，确保上下文始终切题。

不同提示语会激活不同技能：同一智能体，产出迥异结果。

智能体 = 游戏规则；技能 = 工具箱。

更新一项技能，即可即时提升所有调用它的智能体（参见《AI技能可组合性》）。

专业化智能体阵容割裂上下文，并被迫频繁进行多智能体切换。

精简型智能体搭配深厚技能库，才是经得起时间检验的架构形态。

“智能体动物园”困境

以智能体为中心的设计，首要问题在于人为因素，而非技术限制。

一旦智能体数量超过五六个，这个阵容本身便成了你需要主动管理的对象：你得记住每个智能体的功能、适用场景、彼此差异，以及当初为何要为它单独开辟一个席位。更糟的是，专业化智能体会把你推向多智能体轮转的泥潭——先启动研究智能体，再把结果复制给写作智能体，接着交由审阅智能体处理，最后祈祷信息在传递中没有丢失或扭曲。

到某个临界点，你不再使用AI来工作，而是开始管理AI来工作。那一刻，实在令人唏嘘。

专业化是脆弱的

专业化智能体的理念在于：领域知识使其更出色。确实如此——但仅限于它被精准调优的那一小块任务切片。

问题在于：真实任务从不尊重这些人为划定的切片。“写作”任务中途可能突然需要插入代码；“研究”任务可能临时要求生成示意图；“代码审查”任务或许又演变为重构需求。专业型智能体很快便会触达能力边界；此时，你只能要么切换至另一智能体，要么眼睁睁看着它笨拙地模仿其他角色。

而一个配备深厚技能库的通用型智能体，则无此困扰。它能随对话自然展开，动态拾取所需能力（即智能体自身成为编排层）。其灵活性源于会话的开启方式：你如何发起对话、如何界定问题，会自然触发不同技能的调用。同一智能体，因提问视角不同，激活的工具链各异，输出结果亦随之变化。这不是权宜之计，而是核心特性。

技能让智能体保持精简

臃肿智能体在上下文开销上代价高昂。智能体定义中每一行人格设定、指令说明与内嵌知识，都会在实际工作开始前就占据上下文窗口的空间。一个臃肿智能体刚“走进房间”，上下文窗口已近半满。

技能则逆转了这一局面。智能体初始状态轻量；仅当请求内容与某项技能描述匹配时，该技能才被加载。这正是“提示语懒加载AI设计模式（Prompt Lazy Loading, PLL）”在能力层面的应用：一切延后至实际调用时刻。

结果是：上下文窗口不再是一个为“以防万一”而塞满能力的杂物箱，而成为一个专注高效的工作空间。

技能赋予确定性

AI本质上是概率性的。对创造性工作而言，这恰是魅力所在；但对任何需要可靠性的任务，这却成了隐患。

技能，正是我们夺回确定性的手段。一项技能可以是一个模板、一段脚本、一个微型嵌入式程序，或是一份精确的检查清单——其描述中已明确嵌入“当X发生时启用此技能”的逻辑。大模型仍负责判断“是否调用技能”，但一旦调用，技能自身执行过程则高度一致。

概率化路由 + 确定性执行——这才是该模式在实践中真正奏效、而不止于演示的关键组合。

智能体是规则，技能是工具

我迄今发现最清晰的心智模型如下：

AI智能体身份（Agent Identity）承载着“游戏规则”：如何行为、需强制执行什么、应关注哪些信号、重视何种价值。这些规则应当精炼且稳定。

技能则是智能体伸手可及的工具箱：数量可多，更新可频（甚至每周迭代），增删改写均无需分叉任一智能体。

请求抵达时，智能体本身轻量而稳定，仅含规则与身份；技能库则宽广多元。唯有与请求匹配的技能被点亮，其余全部处于休眠状态。这便是整个运行时逻辑的全景图。

这一分工最纯粹的体现，是“接待员AI设计模式（Receptionist AI Design Pattern）”：其智能体身份仅含一条规则（将请求路由至恰当处理者），且其主体不内嵌任何功能能力。所有功能性逻辑均存于技能或其他按需调用的智能体中。仅此而已。倘若一个近乎空载的智能体单靠路由机制就能驱动整套系统，那么你的“研究专家”智能体，也未必需要内置五百行操作手册。接待员模式正是“智能体=规则”这一理念的可行性验证：将规则压缩至极致，智能体几近隐去，而系统依然稳健运转。

更新一项技能，即可立即惠及所有调用它的智能体。而若换成三个各自携带独立内嵌知识的专业化智能体，你根本无法做到这一点。

我的个人实践

这并非纸上谈兵。我的个人AI系统，正是基于这一架构运行。

我仅维护少量智能体（Ghostwriter文稿助手、Coach教练、Strategist战略师、Maintenance Worker运维员，外加若干审阅小组面板）。每个智能体均极为轻量：一份SOUL.md文件定义其身份、决策框架与行为边界；一份MEMORY.md记录累积经验；一份DEPENDENCIES.md列出该智能体可调用的技能类别。

真正厚重的部分是技能库：数百项技能，按命名空间组织，依描述实现懒加载。Ghostwriter并不“知道”如何撰写通讯简报；当对话中出现“通讯简报”字眼时，它才加载相应技能。同一智能体可撰写文章、推文线程、图书章节或电子邮件，每次均自动激活最匹配的能力。

当我需要新增能力时，我编写一项技能，而非创建一个新智能体；当我希望调整行为逻辑时，我更新相关技能，而非分别修改三四个可能逻辑重复的智能体。

同一角色，两种设计。右侧智能体按需调用能力，始终保持极低的认知成本。

这就像拥有一把功能强大的多功能工具钳， versus 抽屉里塞满一堆单功能小工具，每次要用时却总找不到。

那专业化呢？

专业化智能体在单一任务切片上表现卓越，且当面对正交并行任务时，其并行能力尤为突出。“Python微服务审查”智能体的确比通用型智能体更锐利；协同工作的多智能体团队，往往能在更短时间内交付更多成果。

但依我之见，专业化理应属于“技能”层级，而非“智能体”层级。你可以构建一项高度专业化的“Python微服务审查”技能，由通用型智能体在任务需要时动态加载。

至于并行化需求，当我真正需要时，我倾向采用两个共享同一技能库的通用型智能体，而非十个定制化专业智能体。技能库始终是唯一可信源；智能体只是轻量级运行器/控制器。

结语

如果你盯着一长串智能体列表，光是看一眼就感到隐隐疲惫——这就是警示信号。

请精简它们。只保留一两个规则清晰、稳定可靠的智能体；将实际能力全部移入技能库。让智能体的行为随你开启对话的方式而变，而非取决于你点击了哪个图标。久而久之，技能库持续复利增长，智能体本身却几乎无需改动——这才是真正的胜利。

智能体越少，技能越多，其余一切水到渠成。

今日分享到此为止！✨

附注：我每周都会在《DeveloPassion通讯》中深入探讨此类主题。欢迎订阅：https://dsebastien.net/newsletter

延伸阅读

如欲进一步探索，可参考以下相关概念：

AI智能体  
AI智能体技能  
AI技能可组合性  
AI智能体身份  
AI智能体路由  
AI智能体分发  
AI智能体权限  
上下文预算（Context Budget）  
上下文窗口（Context Window）  
提示语懒加载AI设计模式（PLL）  
上下文工程（Context Engineering）  
接待员AI设计模式（Receptionist AI Design Pattern）  
我的内容策略  
我的内容类型
