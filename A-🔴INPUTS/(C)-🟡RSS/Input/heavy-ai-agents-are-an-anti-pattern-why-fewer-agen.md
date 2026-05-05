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
> 文章批判了当前流行的“多专用AI代理”设计模式，指出其导致认知负担重、系统脆弱、维护成本高。作者主张采用“精简代理+深度技能库”的架构：代理仅负责规则制定，技能作为可按需加载的工具，二者分离以提升灵活性、确定性和可维护性。这种设计能避免多代理协作中的上下文碎片化和信息丢失，使AI系统更可持续演进。

---

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-cover-1.png)

AI 系统真正稳健的形态是：精简的智能体（agents）、深厚的技能库（skill libraries），以及规则与工具之间清晰的界限。

AI 系统真正稳健的形态是：精简的智能体（agents）、深厚的技能库（skill libraries），以及规则与工具之间清晰的界限。

在这篇文章中，我想说服你：当下大多数人正在构建的 AI 智能体“阵容”（roster）本质上是一种反模式（anti-pattern）。真正具备可扩展性的架构恰恰相反：更少的智能体，但每个都掌握更丰富的技能。接下来我将解释原因，并分享我在自己系统中是如何思考和实践这一理念的。

在这篇文章中，我想说服你：当下大多数人正在构建的 AI 智能体“阵容”（roster）本质上是一种反模式（anti-pattern）。真正具备可扩展性的架构恰恰相反：更少的智能体，但每个都掌握更丰富的技能。接下来我将解释原因，并分享我在自己系统中是如何思考和实践这一理念的。

## 引言

## 引言

每周，我都会看到有人全力投入 AI 领域，并自豪地宣布自己新组建的由十五个高度专业化智能体组成的阵容：一个研究智能体、一个写作智能体、一个评审智能体、一个规划智能体、“资深工程师”智能体、一个爱发牢骚的批评家、一个原始人……等等。

每周，我都会看到有人全力投入 AI 领域，并自豪地宣布自己新组建的由十五个高度专业化智能体组成的阵容：一个研究智能体、一个写作智能体、一个评审智能体、一个规划智能体、“资深工程师”智能体、一个爱发牢骚的批评家、一个原始人……等等。

然后，他们花在挑选该用哪一个智能体上的时间，远超实际使用 AI 完成工作的时长。

然后，他们花在挑选该用哪一个智能体上的时间，远超实际使用 AI 完成工作的时长。

这绝不仅仅是一个效率问题——它是一个设计问题。随着我持续深入使用 [AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) 和 [AI 智能体技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)，我愈发确信：臃肿、高度专业化的智能体并非合理默认选择。真正的杠杆效应，恰恰来自反向路径。

这绝不仅仅是一个效率问题——它是一个设计问题。随着我持续深入使用 [AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) 和 [AI 智能体技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)，我愈发确信：臃肿、高度专业化的智能体并非合理默认选择。真正的杠杆效应，恰恰来自反向路径。

## 一句话总结（TL;DR）

## 一句话总结（TL;DR）

更少的智能体，搭配更丰富的技能库，在所有关键维度上均优于臃肿的专业化阵容：认知负荷、灵活性、[上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)、确定性（determinism）以及维护成本。智能体应承载“游戏规则”，而技能则应作为“工具”。二者演进速度截然不同；若将其混为一谈，便会催生脆弱系统，终将被弃用。

更少的智能体，搭配更丰富的技能库，在所有关键维度上均优于臃肿的专业化阵容：认知负荷、灵活性、[上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)、确定性（determinism）以及维护成本。智能体应承载“游戏规则”，而技能则应作为“工具”。二者演进速度截然不同；若将其混为一谈，便会催生脆弱系统，终将被弃用。

- 庞大的智能体阵容带来额外的认知负担：阵容本身便成了需要管理的对象。  
- 专家型智能体极为脆弱：真实任务往往横跨多个领域边界。  
- 技能按需加载，使 [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 始终聚焦且轻量。  
- 技能弥补了概率模型固有的不确定性：它们可以是模板、脚本或嵌入式小程序，提供可预测的执行结果。  
- 技能描述会自动触发其加载——请求内容即上下文相关性的保障。  
- 不同提示（prompt）可调用不同技能：同一智能体，产出结果却各不相同。  
- 智能体 = 游戏规则；技能 = 工具箱。  
- 更新某一项技能，即可同步提升所有调用它的智能体（参见 [AI 技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)）。  
- 专家型智能体阵容割裂上下文，迫使系统频繁进行多智能体切换。  
- 精简的智能体 + 深厚的技能库，才是经得起时间考验的稳健架构。

- 庞大的智能体阵容带来额外的认知负担：阵容本身便成了需要管理的对象。  
- 专家型智能体极为脆弱：真实任务往往横跨多个领域边界。  
- 技能按需加载，使 [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 始终聚焦且轻量。  
- 技能弥补了概率模型固有的不确定性：它们可以是模板、脚本或嵌入式小程序，提供可预测的执行结果。  
- 技能描述会自动触发其加载——请求内容即上下文相关性的保障。  
- 不同提示（prompt）可调用不同技能：同一智能体，产出结果却各不相同。  
- 智能体 = 游戏规则；技能 = 工具箱。  
- 更新某一项技能，即可同步提升所有调用它的智能体（参见 [AI 技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)）。  
- 专家型智能体阵容割裂上下文，迫使系统频繁进行多智能体切换。  
- 精简的智能体 + 深厚的技能库，才是经得起时间考验的稳健架构。

## “智能体动物园”问题

## “智能体动物园”问题

以智能体为中心的设计所面临的首要问题，是人性的，而非技术的。

以智能体为中心的设计所面临的首要问题，是人性的，而非技术的。

一旦智能体数量超过五六个，这个“阵容”本身便成了你需要主动管理的对象：你得记住每个智能体的职责、何时启用它、它与邻近智能体有何区别，以及当初为何认为它值得独占一个席位。更糟的是，专业化智能体会把你推向多智能体协同流程：先启动研究智能体，再把结果复制给写作智能体，再转交评审智能体，最后祈祷过程中没有信息丢失。

一旦智能体数量超过五六个，这个“阵容”本身便成了你需要主动管理的对象：你得记住每个智能体的职责、何时启用它、它与邻近智能体有何区别，以及当初为何认为它值得独占一个席位。更糟的是，专业化智能体会把你推向多智能体协同流程：先启动研究智能体，再把结果复制给写作智能体，再转交评审智能体，最后祈祷过程中没有信息丢失。

在某个临界点，你不再使用 AI 来完成工作——你开始管理 AI 来完成工作。当这种情况发生时，实在令人唏嘘。

在某个临界点，你不再使用 AI 来完成工作——你开始管理 AI 来完成工作。当这种情况发生时，实在令人唏嘘。

## 专业化是脆弱的

## 专业化是脆弱的

专业化智能体的卖点在于：领域知识使其表现更优。的确如此，但它仅在为其精确调优的那一小块任务切片上才真正出色。

专业化智能体的卖点在于：领域知识使其表现更优。的确如此，但它仅在为其精确调优的那一小块任务切片上才真正出色。

问题是：真实任务从不尊重这些人为划分的切片。“写作”任务最终可能需要嵌入代码；“研究”任务可能需要生成图表；“代码评审”任务可能需要重构建议。专家型智能体很快就会触达能力边界；一旦如此，你只能在“切换至另一智能体”与“眼睁睁看着该专家笨拙地模仿其他角色”之间二选一。

问题是：真实任务从不尊重这些人为划分的切片。“写作”任务最终可能需要嵌入代码；“研究”任务可能需要生成图表；“代码评审”任务可能需要重构建议。专家型智能体很快就会触达能力边界；一旦如此，你只能在“切换至另一智能体”与“眼睁睁看着该专家笨拙地模仿其他角色”之间二选一。

而一个拥有深厚技能库的通用型智能体则无此困扰。它会随对话展开，动态调取所需能力（即智能体自身成为编排层）。灵活性源于会话的开启方式：你如何发起对话、如何界定问题，自然会触发不同技能的调用。同一智能体，不同提问视角，激活不同工具链，产出不同结果。这不是权宜之计，而是核心特性。

而一个拥有深厚技能库的通用型智能体则无此困扰。它会随对话展开，动态调取所需能力（即智能体自身成为编排层）。灵活性源于会话的开启方式：你如何发起对话、如何界定问题，自然会触发不同技能的调用。同一智能体，不同提问视角，激活不同工具链，产出不同结果。这不是权宜之计，而是核心特性。

## 技能让智能体保持精简

## 技能让智能体保持精简

臃肿的智能体在上下文（context）层面代价高昂。智能体定义中每一行人格设定、指令说明与内嵌知识，都在任何实质性工作开始前，就已占据 [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 的宝贵空间。一个臃肿的智能体尚未开工，上下文窗口已近半满。

臃肿的智能体在上下文（context）层面代价高昂。智能体定义中每一行人格设定、指令说明与内嵌知识，都在任何实质性工作开始前，就已占据 [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 的宝贵空间。一个臃肿的智能体尚未开工，上下文窗口已近半满。

技能机制则彻底扭转这一局面。智能体初始状态轻量简洁；仅当请求内容与某项技能描述匹配时，该技能才被加载——这正是 [提示词懒加载 AI 设计模式（Prompt Lazy Loading AI Design Pattern, PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net) 在能力层面的应用：一切皆延迟至真正使用那一刻。

技能机制则彻底扭转这一局面。智能体初始状态轻量简洁；仅当请求内容与某项技能描述匹配时，该技能才被加载——这正是 [提示词懒加载 AI 设计模式（Prompt Lazy Loading AI Design Pattern, PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net) 在能力层面的应用：一切皆延迟至真正使用那一刻。

结果是：[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 不再是“以防万一”而塞满能力的杂货箱，而成为一个专注高效的工作空间。

结果是：[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) 不再是“以防万一”而塞满能力的杂货箱，而成为一个专注高效的工作空间。

## 技能赋予确定性

## 技能赋予确定性

AI 本质上是概率性的。对创造性工作而言，这恰是其魅力所在；但对任何需要可靠性的任务，这却成了致命缺陷。

AI 本质上是概率性的。对创造性工作而言，这恰是其魅力所在；但对任何需要可靠性的任务，这却成了致命缺陷。

技能正是我们夺回确定性的手段。一项技能可以是一个模板、一段脚本、一个微型嵌入式程序，或是一份精准检查清单——其中明确写着“当 X 发生时，请使用此技能”。模型仍自主决定是否调用某项技能，但一旦调用，该技能本身将稳定、一致地执行。

技能正是我们夺回确定性的手段。一项技能可以是一个模板、一段脚本、一个微型嵌入式程序，或是一份精准检查清单——其中明确写着“当 X 发生时，请使用此技能”。模型仍自主决定是否调用某项技能，但一旦调用，该技能本身将稳定、一致地执行。

概率化路由 + 确定性执行——这才是该范式能在实践中落地、而不仅限于演示的关键组合。

概率化路由 + 确定性执行——这才是该范式能在实践中落地、而不仅限于演示的关键组合。

## 智能体是规则，技能是工具

## 智能体是规则，技能是工具

我迄今发现最清晰的心智模型如下：

我迄今发现最清晰的心智模型如下：

- [AI 智能体身份（AI Agent Identity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net) 承载“游戏规则”：如何行为、需强制执行什么、需警惕什么、重视何种价值。这些规则应精简且稳定。  
- 技能则是智能体随时调用的工具箱：数量可众多，更新频率可高达每周一次，增删改写均无需分叉（fork）任一智能体。

- [AI 智能体身份（AI Agent Identity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net) 承载“游戏规则”：如何行为、需强制执行什么、需警惕什么、重视何种价值。这些规则应精简且稳定。  
- 技能则是智能体随时调用的工具箱：数量可众多，更新频率可高达每周一次，增删改写均无需分叉（fork）任一智能体。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-mental-model-1.png)
<span style="white-space: pre-wrap;">请求抵达。智能体本身小巧而稳定，仅含规则与身份；技能库则宽广丰富。仅与请求匹配的技能被激活，其余保持休眠。整套运行时逻辑，尽在此图之中。</span>

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-mental-model-1.png)
<span style="white-space: pre-wrap;">请求抵达。智能体本身小巧而稳定，仅含规则与身份；技能库则宽广丰富。仅与请求匹配的技能被激活，其余保持休眠。整套运行时逻辑，尽在此图之中。</span>

这一分离原则最纯粹的体现，便是 [接待员 AI 设计模式（Receptionist AI Design Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net)：其智能体身份仅包含一条规则（将请求路由至恰当处理者），其主体不嵌入任何功能能力。所有功能性逻辑均存于技能或其他按需调用的智能体中。仅此而已。倘若一个近乎空白的智能体仅凭路由机制就能驱动整个系统，那么你的“研究专家”智能体大概率也无需内置五百行操作手册。接待员模式正是“智能体 = 规则”这一理念的原理验证：将规则不断精简，智能体几近消失，而其周边系统依然高效运转。

这一分离原则最纯粹的体现，便是 [接待员 AI 设计模式（Receptionist AI Design Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net)：其智能体身份仅包含一条规则（将请求路由至恰当处理者），其主体不嵌入任何功能能力。所有功能性逻辑均存于技能或其他按需调用的智能体中。仅此而已。倘若一个近乎空白的智能体仅凭路由机制就能驱动整个系统，那么你的“研究专家”智能体大概率也无需内置五百行操作手册。接待员模式正是“智能体 = 规则”这一理念的原理验证：将规则不断精简，智能体几近消失，而其周边系统依然高效运转。

更新某一项技能，即可即时提升所有调用它的智能体。试着对三个各自携带独立内嵌知识的深度专家型智能体做同样操作？你做不到。

更新某一项技能，即可即时提升所有调用它的智能体。试着对三个各自携带独立内嵌知识的深度专家型智能体做同样操作？你做不到。

## 我自己的实践架构

## 我自己的实践架构

这对我而言绝非纸上谈兵。我的个人 AI 系统正是基于这一架构运行。

这对我而言绝非纸上谈兵。我的个人 AI 系统正是基于这一架构运行。

我拥有一组数量精简的智能体（Ghostwriter 文稿助手、Coach 教练、Strategist 战略师、Maintenance Worker 维护工，外加若干评审小组）。每个智能体都极为轻量：一份 SOUL.md 文件定义其身份、决策框架与边界；一份 MEMORY.md 记录累积经验；一份 DEPENDENCIES.md 列出该智能体可调用的技能类别。

我拥有一组数量精简的智能体（Ghostwriter 文稿助手、Coach 教练、Strategist 战略师、Maintenance Worker 维护工，外加若干评审小组）。每个智能体都极为轻量：一份 SOUL.md 文件定义其身份、决策框架与边界；一份 MEMORY.md 记录累积经验；一份 DEPENDENCIES.md 列出该智能体可调用的技能类别。

技能库才是真正的重头戏：数百项技能，按命名空间组织，依描述按需懒加载。Ghostwriter 并不“知晓”如何撰写通讯简报；当对话中出现“通讯简报”字样时，它才加载对应技能。同一智能体可撰写文章、推文线程、书籍章节或邮件——每次都能精准激活相应能力。

技能库才是真正的重头戏：数百项技能，按命名空间组织，依描述按需懒加载。Ghostwriter 并不“知晓”如何撰写通讯简报；当对话中出现“通讯简报”字样时，它才加载对应技能。同一智能体可撰写文章、推文线程、书籍章节或邮件——每次都能精准激活相应能力。

当我需要新增一项能力时，我编写的是技能，而非智能体；当我需要调整行为时，我更新的是相关技能，而非三个可能逻辑重复、也可能彼此迥异的智能体。

当我需要新增一项能力时，我编写的是技能，而非智能体；当我需要调整行为时，我更新的是相关技能，而非三个可能逻辑重复、也可能彼此迥异的智能体。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-split-1.png)
<span style="white-space: pre-wrap;">同一角色，两种设计。右侧智能体按需调用能力，始终保持认知成本低廉。</span>

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/2026/05/heavy-ai-agents-anti-pattern-split-1.png)
<span style="white-space: pre-wrap;">同一角色，两种设计。右侧智能体按需调用能力，始终保持认知成本低廉。</span>

这就像拥有一个配备优质附件的多功能工具，而非一个塞满单功能小工具、却总在急需时找不到的抽屉。

这就像拥有一个配备优质附件的多功能工具，而非一个塞满单功能小工具、却总在急需时找不到的抽屉。

## 关于专业化的问题

## 关于专业化的问题

专业化智能体在特定细分任务上确实卓越，并且当面对正交（互不重叠）工作流时，并行能力极强。“审查 Python 微服务”智能体的确比通用型智能体更敏锐。采用并行协作的多智能体团队，能在更短时间内交付更多成果。

专业化智能体在特定细分任务上确实卓越，并且当面对正交（互不重叠）工作流时，并行能力极强。“审查 Python 微服务”智能体的确比通用型智能体更敏锐。采用并行协作的多智能体团队，能在更短时间内交付更多成果。

但依我拙见，专业化理应存在于“技能”之中，而非“智能体”本身。你可以拥有一个深度专业化的“审查 Python 微服务”技能，供通用型智能体在任务需要时加载调用。

但依我拙见，专业化理应存在于“技能”之中，而非“智能体”本身。你可以拥有一个深度专业化的“审查 Python 微服务”技能，供通用型智能体在任务需要时加载调用。

至于并行化需求：当我真正需要时，我更倾向部署两个共享同一技能库的通用型智能体，而非十个定制化专家。技能库始终是唯一真相源（source of truth）；智能体则只是轻量级执行器/“控制器”。

至于并行化需求：当我真正需要时，我更倾向部署两个共享同一技能库的通用型智能体，而非十个定制化专家。技能库始终是唯一真相源（source of truth）；智能体则只是轻量级执行器/“控制器”。

## 结论

## 结论

如果你正盯着一长串智能体列表，仅仅看一眼就感到莫名疲惫——那这就是信号。

如果你正盯着一长串智能体列表，仅仅看一眼就感到莫名疲惫——那这就是信号。

合并它们。保留一两个规则清晰、稳定可靠的智能体。将实际能力全部移入技能库。让智能体的行为取决于你如何开启对话，而非你点击了哪个图标。久而久之，技能库将持续复利增长；智能体本身却几乎无需变更。这才是真正的胜利。

合并它们。保留一两个规则清晰、稳定可靠的智能体。将实际能力全部移入技能库。让智能体的行为取决于你如何开启对话，而非你点击了哪个图标。久而久之，技能库将持续复利增长；智能体本身却几乎无需变更。这才是真正的胜利。

更少的智能体，更多的技能——其余一切，水到渠成。

更少的智能体，更多的技能——其余一切，水到渠成。

今日分享就到这里！ ✨

今日分享就到这里！ ✨

附注：我每周都会在 DeveloPassion 通讯简报中深入探讨此类主题。欢迎订阅 https://dsebastien.net/newsletter 跟踪阅读。

附注：我每周都会在 DeveloPassion 通讯简报中深入探讨此类主题。欢迎订阅 https://dsebastien.net/newsletter 跟踪阅读。

## 相关延伸

## 相关延伸

如欲深入探索，可参考以下关联概念：

如欲深入探索，可参考以下关联概念：

- [AI 智能体（AI Agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [AI 智能体技能（AI Agent Skills）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)  
- [AI 技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)  
- [AI 智能体身份（AI Agent Identity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Identity?ref=dsebastien.net)  
- [AI 智能体路由（AI Agent Routing）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net)  
- [AI 智能体分发（AI Agent Distribution）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Distribution?ref=dsebastien.net)  
- [AI 智能体权限（AI Agent Permissions）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Permissions?ref=dsebastien.net)  
- [上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  
- [上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [提示词懒加载 AI 设计模式（PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)  
- [上下文工程（Context Engineering）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Engineering?ref=dsebastien.net)  
- [接待员 AI 设计模式（Receptionist AI Design Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Receptionist+AI+Design+Pattern?ref=dsebastien.net)  
- [我的内容策略（My Content Strategy）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Strategy?ref=dsebastien.net)  
- [我的内容类型（My Content Types）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/My+Content+Types?ref=dsebastien.net)
