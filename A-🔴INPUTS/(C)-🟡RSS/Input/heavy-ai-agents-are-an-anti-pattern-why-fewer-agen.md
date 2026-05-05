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
> 文章批判了当前流行的“多而专”的AI代理（agent）设计模式，指出其导致认知负担重、系统脆弱、维护成本高。作者主张采用“少而精”的代理架构：每个代理仅负责规则与流程控制，而将具体能力封装为可复用、按需加载的技能（skills），形成深度技能库。这种分离使系统更灵活、确定性强、上下文更精简，并支持技能的跨代理复用与独立演进，从而实现长期可扩展性。

---

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-cover-1.png)

AI系统稳健演化的形态是：精简的智能体、深厚的技能库，以及规则与工具之间清晰的分离。

这篇文章旨在说服你：当前大多数人正在构建的AI智能体阵容，本质上是一种反模式（anti-pattern）。真正具备可扩展性的架构恰恰相反——更少的智能体，却拥有更丰富的技能。下文将解释原因，并分享我在自身系统中如何实践这一理念。

## 引言

每周，我都会看到有人全力投入AI领域，并自豪地宣布自己新组建的十五个高度专业化的智能体阵容：一个研究智能体、一个写作智能体、一个审阅智能体、一个规划智能体、“资深工程师”智能体、一位爱挑剔的批评家、一位原始人……等等。

接着，他们花在挑选该用哪一个智能体上的时间，远超实际利用AI完成工作的时长。

这绝不仅仅是一个效率问题，而是一个设计问题。随着我持续深入使用[AI智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)和[AI智能体技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)，我愈发确信：臃肿、高度专业化的智能体不应成为默认选择。绝大多数杠杆效应，恰恰来自反其道而行之的方向。

## 一句话总结（TL;DR）

在所有关键维度上——认知负荷、灵活性、[上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)、确定性、可维护性——“更少的智能体 + 丰富的技能库”全面胜过“臃肿的专业化智能体阵容”。智能体应承载游戏规则；技能则应作为工具。二者演化速度截然不同，若混为一谈，将催生脆弱系统，终将被弃用。

- 庞大的智能体带来额外的认知负担：智能体阵容本身便成了需要管理的对象。
- 专家型智能体极为脆弱：真实任务往往横跨多个边界。
- 技能按需加载，使[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)保持聚焦与精简。
- 技能弥补了概率模型所欠缺的确定性：模板、脚本、嵌入式程序等皆可封装其中。
- 技能描述可自动触发加载，确保上下文始终切题。
- 不同提示词会调用不同技能：同一智能体，输出结果各异。
- 智能体 = 游戏规则；技能 = 工具箱。
- 更新一项技能，所有调用它的智能体即刻受益（参见[AI技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)）。
- 专家型智能体阵容割裂上下文，迫使进行多智能体切换。
- 精简的智能体搭配深厚的技能库，才是经得起时间考验的稳健架构。

## “智能体动物园”问题

以智能体为中心的设计，首要问题在于人为因素，而非技术限制。

一旦智能体数量超过五六个，整个阵容本身便成为一项待管理对象：你需要记住每个智能体的功能、何时启用、它与邻近智能体的差异，以及当初为何认为它值得独占一席之地。更糟的是，专业化智能体会把你推向多智能体协同流程：启动研究智能体 → 复制结果至写作智能体 → 再交由审阅智能体处理 → 祈祷信息未在传递中丢失。

某一天，你不再用AI来工作，而是开始管理AI来工作——当这一刻到来时，实在令人唏嘘。

## 专业化即脆弱

专业化智能体的卖点在于领域知识使其更优。的确如此，但仅限于它被专门调优的那一小块任务切片。

问题在于：真实任务从不尊重这些人为切片。“写作”任务可能突然需要写代码；“研究”任务可能需要绘制图表；“代码审查”任务可能要求重构。专家型智能体很快触达能力边界——此时，你只能在切换至另一智能体，或眼睁睁看着它笨拙地模仿其他角色之间二选一。

而一个配备深厚技能库的通用智能体则无此困扰。它能在对话展开过程中按需调取所需能力（即智能体自身成为编排层）。其灵活性源于会话的起始方式：你开启对话的方式、你定义问题的角度，自然牵引出不同的技能组合。同一智能体，不同提问框架，激活不同工具链，产出不同结果——这不是权宜之计，而是核心特性。

## 技能让智能体保持精简

臃肿的智能体在上下文开销上代价高昂。智能体定义中每一行人格设定、指令说明和内嵌知识，都在任何实质性工作开始前就已占据[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)空间。一个臃肿的智能体甫一登场，上下文已半满。

技能则彻底扭转这一局面。智能体从轻量起步；仅当请求内容与技能描述匹配时，相关技能才被动态加载。这正是[提示词懒加载AI设计模式（Prompt Lazy Loading AI Design Pattern, PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)在能力层面的应用：一切延迟至实际使用那一刻。

结果是：[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)不再是一个为“以防万一”而塞满能力的杂物箱，而成为一个专注的工作空间。

## 技能赋予确定性

AI本质上是概率性的。对创造性工作而言，这恰是其魅力所在；但对任何需要可靠性的任务，这却成为隐患。

技能正是我们夺回确定性的手段。一项技能可以是一个模板、一段脚本、一个小型嵌入式程序，或一份精准检查清单（其描述中已内嵌“当X发生时使用此技能”的条件）。模型仍决定是否调用某项技能，但一旦调用，该技能的执行即具有一致性。

概率化路由，确定性执行——正是这一组合，让该方案在实践中切实可行，而不仅停留在演示阶段。

## 智能体是规则，技能是工具

我迄今发现最清晰的心智模型如下：

- [AI智能体身份（AI Agent Identity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net)承载游戏规则：行为准则、需强制执行的事项、需监控的要点、所珍视的价值观。这些规则应精简且稳定。
- 技能则是智能体伸手可及的工具箱：数量可众多，更新频率可达每周，增删改写均无需复制或分叉任一智能体。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-mental-model-1.png)
<span style="white-space: pre-wrap;">请求抵达。智能体体积小且稳定，仅含规则与身份；技能库则广博浩瀚。仅与请求匹配的技能被点亮，其余保持休眠。一张图即完整呈现整个运行时逻辑。</span>

这一分离最纯粹的体现，是[接待员AI设计模式（Receptionist AI Design Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net)：一个智能体的全部身份仅是一条规则（将请求路由至正确的处理器），其主体不包含任何内嵌功能。所有功能性内容均存在于技能中，或存在于按需调用的其他智能体里。仅此而已。如果一个近乎空壳的智能体仅凭路由即可驱动整套系统，那么你的“研究专家”智能体，很可能也无需硬编码五百行操作手册。接待员模式正是“智能体=规则”这一理念的可行性验证：将规则不断精简，智能体几近消隐，而其周边系统依然高效运转。

更新一项技能，所有调用它的智能体即时获益。尝试对三个各自携带独立内嵌知识的深度专家型智能体做同样操作？你做不到。

## 我自己的系统配置

这对我而言并非纸上谈兵。我的个人AI系统正基于这一架构运行。

我拥有一组数量有限的智能体（撰稿人Ghostwriter、教练Coach、战略师Strategist、运维工人Maintenance Worker，外加若干审阅小组）。每个智能体均轻量化：一份SOUL.md文件定义其身份、决策框架与边界；一份MEMORY.md记录累积经验；一份DEPENDENCIES.md列出该智能体可调用的技能类别。

真正的“重头戏”在于技能库：数百项技能，按命名空间组织，依描述实现懒加载。撰稿人Ghostwriter并不“知道”如何撰写通讯简报；当对话明确提及“通讯简报”时，它才加载相应技能。同一智能体可撰写文章、推文线程、书籍章节或电子邮件，每次均自动激活对应能力。

当我需要新增功能时，我编写一项技能，而非创建一个智能体；当我需要调整行为时，我更新相关技能，而非分别修改三个可能逻辑雷同、也可能彼此迥异的智能体。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-split-1.png)
<span style="white-space: pre-wrap;">同一角色，两种设计。右侧智能体按需调用能力，始终保持认知成本低廉。</span>

这就像拥有一把功能强大的多功能工具（附带优质配件），而非抽屉里一堆你总在急需时找不到的单功能小工具。

## 那么专业化呢？

专业化智能体在单一任务切片上表现卓越，且在处理正交并行工作时极具优势。“审查Python微服务”智能体确实比通用型智能体更敏锐。协同运作的多智能体团队可在更短时间内交付更多成果。

但依我之见，专业化理应体现在**技能**层面，而非**智能体**层面。你可以拥有一项高度专业化的“审查Python微服务”技能，由通用型智能体在任务需要时加载调用。

至于并行化需求，当我真正需要时，我倾向采用两个共享同一技能库的通用智能体，而非十个定制化的专家型智能体。技能库始终是唯一可信源；智能体仅是轻量级的执行器/“控制器”。

## 结论

如果你正盯着一长串智能体列表，仅是看一眼便感到莫名疲惫——这就是信号。

请合并它们。保留一两个规则清晰、稳定的核心智能体。将实际能力迁移至技能中。让智能体的行为随你开启对话的方式而变，而非取决于你点击了哪个图标。久而久之，技能库将产生复利效应，而智能体几乎无需变更——这才是真正的胜利。

更少的智能体，更多的技能。其余一切水到渠成。

今日分享到此结束！ ✨

附注：我每周都会在DeveloPassion通讯简报中深入探讨此类主题。欢迎订阅 https://dsebastien.net/newsletter 跟踪阅读。

## 相关延伸

如欲深入探索，可参考以下关联概念：

- [AI智能体（AI Agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)
- [AI智能体技能（AI Agent Skills）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)
- [AI技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)
- [AI智能体身份（AI Agent Identity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net)
- [AI智能体路由（AI Agent Routing）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net)
- [AI智能体分发（AI Agent Distribution）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Distribution?ref=dsebastien.net)
- [AI智能体权限（AI Agent Permissions）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Permissions?ref=dsebastien.net)
- [上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)
- [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)
- [提示词懒加载AI设计模式（PLL）（Prompt Lazy Loading AI Design Pattern (PLL)）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)
- [上下文工程（Context Engineering）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Engineering?ref=dsebastien.net)
- [接待员AI设计模式（Receptionist AI Design Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net)
- [我的内容策略（My Content Strategy）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Strategy?ref=dsebastien.net)
- [我的内容类型（My Content Types）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Types?ref=dsebastien.net)
