---
title: "New article: Heavy AI Agents Are an Anti-Pattern"
url: "https://www.dsebastien.net/new-article-heavy-ai-agents-are-an-anti-pattern/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章指出“重型AI代理”（即大量专用代理）是一种反模式，因其带来过高的认知负荷和管理成本。作者主张采用“轻量代理+丰富技能库”的架构：代理应精简、稳定，而具体能力则封装为可复用、可更新的技能，以降低上下文开销、提升确定性和可维护性。技能的模块化设计支持跨代理共享与组合，避免重复嵌入知识。核心结论是：专业化应体现在技能层而非代理层，通过技能复用实现精度与效率的统一。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [New article: Heavy AI Agents Are an Anti-Pattern](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-05-04+Heavy+AI+Agents+Are+an+Anti-Pattern?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[新文章：重型 AI Agent 是一种反模式](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-05-04+Heavy+AI+Agents+Are+an+Anti-Pattern?ref=dsebastien.net)。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/thumbnail/heavy-ai-agents-anti-pattern-cover-1.png)

![重型 AI Agent 是一种反模式：为何更少的 Agent 搭配更丰富的技能更胜一筹](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/thumbnail/heavy-ai-agents-anti-pattern-cover-1.png)

The argument in one line: most AI agent rosters are an anti-pattern. People accumulate fifteen specialists, then spend more time managing the roster than actually using AI to get work done. The shape that scales is the opposite — fewer agents, with deeper skill libraries.

核心论点一句话概括：大多数 AI Agent 阵容本身就是一种反模式。人们堆砌十五个专业型 Agent，结果花在管理这些 Agent 上的时间，远超真正用 AI 完成工作的时长。真正可扩展的形态恰恰相反——Agent 数量更少，但每个 Agent 具备更深厚、更全面的技能库。

A few hard-earned points from the piece:

本文提炼出几条历经实践验证的关键洞见：

- Heavy agents create cognitive overhead. Once you cross 5 agents, the roster itself becomes a thing you manage.  
- 重型 Agent 带来认知负担。一旦 Agent 数量超过 5 个，光是维护这个阵容本身就成了你需要专门管理的对象。

- Specialists are brittle. Real tasks straddle boundaries. The "writing" task often needs code; the "research" task often needs a diagram.  
- 专业型 Agent 脆弱僵化。真实任务往往横跨多个领域边界：“写作”任务常需嵌入代码；“研究”任务常需生成图表。

- Skills keep the [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) lean. A heavy agent walks into the room half-full. A skill-based agent walks in empty and only loads what the request needs (the [Prompt Lazy Loading AI Design Pattern (PLL)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net) applied to capabilities).  
- 技能（Skills）让[上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)保持精简。重型 Agent 进场时已“半载负荷”；而基于技能的 Agent 则空载入场，仅按请求动态加载所需能力（即把[提示词懒加载 AI 设计模式（PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)应用于能力层面）。

- Skills add the determinism AI lacks: templates, scripts, embedded programs. Probabilistic routing, deterministic execution.  
- 技能弥补了 AI 所欠缺的确定性：模板、脚本、内嵌程序——路由过程或具概率性，但执行过程绝对确定。

- Mental model: [AI Agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) = the rules of the game (small, stable). [AI Agent Skills](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net) = the toolbox (many, replaceable). Don't conflate them.  
- 心智模型：[AI Agent](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net) = 游戏规则（体量小、高度稳定）；[AI Agent 技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net) = 工具箱（数量多、可灵活替换）。二者切勿混淆。

- Update one skill, every agent benefits (see [AI Skill Composability](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)). Try that with three deep specialists carrying their own embedded knowledge — you can't.  
- 更新一项技能，所有 Agent 均同步受益（参见[AI 技能可组合性](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)）。若换成三个各自携带专属内嵌知识的深度专家型 Agent？你根本做不到这一点。

The honest steelman: specialization IS real. But it belongs in the SKILL, not the AGENT. A hyper-specific skill that any generalist loads on demand gives you the same precision without the orchestration tax.

诚恳的最强反驳（steelman）观点：专业化的确真实存在——但它应扎根于“技能”（SKILL），而非“Agent”（AGENT）本身。一个高度特化的技能，可被任一通用型 Agent 按需加载，既能实现同等精度，又规避了复杂的编排开销（orchestration tax）。

If your agent list makes you tired just looking at it, that's the signal. Collapse them. Move the actual capability into skills. The skill library compounds. The agents barely change. That's the win.

如果你光是看到自己的 Agent 列表就感到疲惫，这就是明确信号。请合并精简它们。将实际能力下沉至技能层。技能库具备复利效应；而 Agent 本身几乎无需变动——这才是真正的胜利。

🔗 [https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)

🔗 [https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)

## Related  
## 相关

- [Heavy AI Agents Are an Anti-Pattern - Why Fewer Agents With More Skills Wins (Article)](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)  
- [重型 AI Agent 是一种反模式——为何更少的 Agent 搭配更丰富的技能更胜一筹（文章）](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)

- [AI Agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [AI Agent](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)

- [AI Agent Skills](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)  
- [AI Agent 技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)

- [AI Skill Composability](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)  
- [AI 技能可组合性](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)

- [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)

- [Prompt Lazy Loading AI Design Pattern (PLL)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)  
- [提示词懒加载 AI 设计模式（PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)
