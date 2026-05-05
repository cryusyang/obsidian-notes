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
> 文章指出“重型AI代理”（即大量专用AI代理）是一种反模式，因其带来过高管理成本与认知负担；真正可扩展的架构是减少代理数量，转而构建丰富、可复用、模块化的技能库；技能能保持上下文窗口精简、提升执行确定性，并支持跨代理共享与快速迭代；作者强调应将专业化能力下沉至技能层，而非固化在独立代理中；最后呼吁开发者反思代理列表的复杂度，及时将能力从代理迁移至技能库以实现长期复利。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-05-04+Heavy+AI+Agents+Are+an+Anti-Pattern?ref=dsebastien.net"><em>New article: Heavy AI Agents Are an Anti-Pattern</em></a><em>.</em></p><figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Heavy AI Agents Are an Anti-Pattern: Why Fewer Agents With More Skills Wins</div><div class="kg-bookmark-description">Heavy specialized AI agents are an anti-pattern. Fewer agents with deep skill libraries beat them on every axis that matters: cognitive load, flexibility, context budget, determinism, and maintenance</div><div class="kg-bookmark-metadata"><img alt="alt" class="kg-bookmark-icon" src="https://static.ghost.org/v5.0.0/images/link-icon.svg" /><span class="kg-bookmark-author">S&#xe9;bastien Dubois</span><span class="kg-bookmark-publisher">Sebastien Dubois</span></div></div><div class="kg-bookmark-thumbnail"><img alt="alt" src="https://storage.ghost.io/c/37/42/374202c6-549c-4d6d-829d-4a898a54ae06/content/images/thumbnail/heavy-ai-agents-anti-pattern-cover-1.png" /></div></a></figure><p>The argument in one line: most AI agent rosters are an anti-pattern. People accumulate fifteen specialists, then spend more time managing the roster than actually using AI to get work done. The shape that scales is the opposite &#x2014; fewer agents, with deeper skill libraries.</p><p>A few hard-earned points from the piece:</p><ul><li>Heavy agents create cognitive overhead. Once you cross 5 agents, the roster itself becomes a thing you manage.</li><li>Specialists are brittle. Real tasks straddle boundaries. The &quot;writing&quot; task often needs code; the &quot;research&quot; task often needs a diagram.</li><li>Skills keep the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a> lean. A heavy agent walks into the room half-full. A skill-based agent walks in empty and only loads what the request needs (the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net">Prompt Lazy Loading AI Design Pattern (PLL)</a> applied to capabilities).</li><li>Skills add the determinism AI lacks: templates, scripts, embedded programs. Probabilistic routing, deterministic execution.</li><li>Mental model: <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI Agents</a> = the rules of the game (small, stable). <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net">AI Agent Skills</a> = the toolbox (many, replaceable). Don&apos;t conflate them.</li><li>Update one skill, every agent benefits (see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net">AI Skill Composability</a>). Try that with three deep specialists carrying their own embedded knowledge &#x2014; you can&apos;t.</li></ul><p>The honest steelman: specialization IS real. But it belongs in the SKILL, not the AGENT. A hyper-specific skill that any generalist loads on demand gives you the same precision without the orchestration tax.</p><p>If your agent list makes you tired just looking at it, that&apos;s the signal. Collapse them. Move the actual capability into skills. The skill library compounds. The agents barely change. That&apos;s the win.</p><p>&#x1f517; <a href="https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/">https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/</a></p><h2 id="related">Related</h2><ul><li><a href="https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/">Heavy AI Agents Are an Anti-Pattern - Why Fewer Agents With More Skills Wins (Article)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net">AI Agents</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net">AI Agent Skills</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net">AI Skill Composability</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net">Prompt Lazy Loading AI Design Pattern (PLL)</a></li></ul>

## 中文译文

这是我的公开笔记中的一则记录。查看权威版本：新文章《重型AI智能体是一种反模式》。

一句话概括核心论点：大多数AI智能体组合都属于一种反模式。人们往往堆砌十五个专业型智能体，结果花在管理这些智能体上的时间，远超真正利用AI完成实际工作的时长。而真正具备可扩展性的结构恰恰相反——智能体数量更少，但技能库更深厚。

本文中几条来之不易的洞见：

重型智能体带来认知负担。一旦智能体数量超过五个，智能体组合本身就会变成一项需要专门管理的对象。

专业型智能体过于脆弱。真实任务往往横跨多个领域边界。“写作”任务常需嵌入代码；“研究”任务常需生成图表。

技能有助于保持上下文窗口（Context Window）精简。重型智能体一入场就已“半满”；而基于技能的智能体则空身入场，仅按请求动态加载所需内容（即“提示词懒加载AI设计模式”（PLL）在能力层面的应用）。

技能为AI注入其原本缺乏的确定性：模板、脚本、内嵌程序。路由可以是概率性的，执行却必须是确定性的。

心智模型类比：AI智能体 = 游戏规则（体量小、稳定性高）；AI智能体技能 = 工具箱（种类多、可替换）。切勿混淆二者。

更新一项技能，所有智能体皆可受益（参见《AI技能可组合性》）。若换成三个各自携带专属知识的深度专业型智能体，你根本做不到这一点。

直面最有力的反驳：专业化确实真实存在。但它应存在于“技能”之中，而非“智能体”本身。一个高度特化的技能，可由任一通用型智能体按需调用，既能实现同等精度，又无需承担协调多个智能体的额外开销。

如果你只是看着自己的智能体列表就感到疲惫，这就是明确信号：请合并它们。将实际能力下沉至技能层。技能库具有复利效应；智能体本身却几乎无需变动。这才是真正的胜利。

🔗 https://www.dsebastien.net/heavy-ai-agents-are-an-anti-pattern-why-fewer-agents-with-more-skills-wins/

相关主题

《重型AI智能体是一种反模式——为何更少智能体+更多技能才是制胜之道》（文章）

AI智能体  
AI智能体技能  
AI技能可组合性  
上下文窗口（Context Window）  
提示词懒加载AI设计模式（PLL）
