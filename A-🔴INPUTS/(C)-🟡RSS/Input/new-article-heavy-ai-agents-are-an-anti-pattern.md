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
> 文章指出“重型AI代理”（即大量专用代理）是一种反模式，因其带来过高的认知负荷和管理成本。作者主张采用“轻量代理+丰富技能库”的架构：代理应保持精简、稳定，而具体能力则通过可复用、可组合的技能实现。技能能按需加载、降低上下文开销、增强执行确定性，并支持单点更新、全局生效。核心思想是将专业化沉淀在技能层而非代理层，从而提升系统可维护性与扩展性。

---

> 这是我 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 中的一则笔记。查看原始版本：[新文章：重型 AI 智能体是一种反模式](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-05-04+Heavy+AI+Agents+Are+an+Anti-Pattern?ref=dsebastien.net)。

![Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins](https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/thumbnail/heavy-ai-agents-anti-pattern-cover-1.png)

> **重型 AI 智能体是一种反模式：为何更少的智能体 + 更丰富的技能才胜出**  
> 重型专业化 AI 智能体是一种反模式。在所有关键维度上——认知负荷、灵活性、上下文预算、确定性与可维护性——具备深厚技能库的更少智能体，均优于前者。  
> **作者**：Sébastien Dubois　**发布者**：Sebastien Dubois

核心论点一句话概括：大多数 AI 智能体阵容本身就是一种反模式。人们堆砌十五个专业智能体，结果花在管理这支“队伍”上的时间，远超真正用 AI 完成工作的时长。而真正可扩展的形态恰恰相反——智能体数量更少，但每个都配备更深厚、更灵活的技能库。

本文提炼出若干来之不易的关键洞见：

- 重型智能体带来显著的认知负担。一旦智能体数量超过 5 个，“智能体清单”本身就会变成一个需要持续维护和协调的对象。  
- 专业型智能体极其脆弱。真实任务天然跨越边界：“写作”任务常需嵌入代码；“研究”任务常需生成图表。单一职能难以覆盖实际需求。  
- 技能有助于保持 **[上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)** 的精简高效。重型智能体一入场就已“半载”上下文；而基于技能的智能体则空载入场，仅按请求动态加载所需能力（即应用于能力层面的 **[提示词懒加载 AI 设计模式（PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)**）。  
- 技能为 AI 弥补了其固有的不确定性：模板、脚本、内嵌程序等结构化组件，实现了“概率化路由 + 确定性执行”的组合优势。  
- 心智模型需厘清：**[AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)** = 游戏规则（体积小、高度稳定）；**[AI 智能体技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)** = 工具箱（数量多、可替换、可复用）。二者不可混淆。  
- 更新一项技能，所有智能体即时受益（参见 **[AI 技能可组合性](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)**）。若换成三个各自携带专属知识库的深度专家型智能体？你根本做不到这一点。

诚恳的“最强反驳”（steelman）是：专业化的确真实存在——但它应扎根于 **技能（SKILL）**，而非 **智能体（AGENT）** 本身。一项高度特化的技能，可由任意通用型智能体按需加载，如此既能获得同等精度，又完全规避了智能体编排带来的额外开销。

如果你光是看着自己的智能体列表就感到疲惫，这就是最清晰的信号：该合并了。把真正的能力下沉到技能层。技能库会持续复利增长；智能体本身却几乎无需变更——这才是真正的胜利。

🔗 [https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)

## 相关内容

- [重型 AI 智能体是一种反模式——为何更少的智能体 + 更丰富的技能才胜出（原文）](https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/)  
- [AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [AI 智能体技能](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)  
- [AI 技能可组合性](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)  
- [上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [提示词懒加载 AI 设计模式（PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)
