---
title: "Gas City"
url: "https://www.dsebastien.net/gas-city/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Gas City 是 Steve Yegge 于2026年4月发布的开源SDK，作为 Gas Town 的继任者，它将单体多智能体平台解构为可组合的“packs”模块，支持开发者按需构建任意拓扑结构的AI协作团队。其核心包括MEOW（以“工作”为一等公民的表达框架）、Dolt（Git版本化的SQL数据库，提供全操作可追溯审计）、声明式可分叉的“Formulas”流程模板，以及强调对抗性团队协作而非单点智能的可靠性设计哲学。平台推动工程师角色从“编码者”转向“牧羊人”，专注于设计代理拓扑、审查机制与工作流，而非手动编写代码。Gas City 还提出“去SaaS化”主张，使小团队能用开源packs重建关键企业级服务，将重复性租金支出转化为自有、可版本控制的基础设施资产，并以Dolt驱动的深度可观测性作为核心差异化优势。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Gas City](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+City?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[Gas City（燃气城）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+City?ref=dsebastien.net)。

Gas City is an SDK and successor to [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net) by [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net), announced April 24, 2026. Where Gas Town shipped a single, opinionated multi-agent platform, Gas City deconstructs the architecture into composable building blocks called "packs" so developers can assemble teams of collaborating AI agents in arbitrary topologies. Yegge frames it as a "light factory"; the autonomous, background work of a dark factory but with the lights kept on (full transparency and observability).

Gas City 是一个 SDK，也是 [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net) 所创 [Gas Town（燃气镇）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net) 的继任者，于 2026 年 4 月 24 日发布。Gas Town 推出的是一个单一、强观点的多智能体平台；而 Gas City 则将该架构解构为可组合的构建模块——称为“packs（组件包）”，使开发者能按任意拓扑结构组装协作式 AI 智能体团队。Yegge 将其定义为一座“明工厂”（light factory）：即暗工厂（dark factory）中那种自主、后台化的工作方式，但全程保持“开灯”——即完全透明且可观测。

## Core Stack

## 核心技术栈

- **MEOW** (Molecular Expression of Work): a [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net)-based framework treating Work as a first-class primitive (epics, molecules, protomolecules, formulas)  
- **MEOW**（工作分子化表达）：一个基于 [Beads（珠链）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net) 的框架，将“工作”视为头等原语（包括史诗级任务、分子、前分子、公式等）  
- [**Dolt**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dolt?ref=dsebastien.net): a Git-versioned SQL database providing a complete, replayable audit trail for everything agents do  
- [**Dolt**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dolt?ref=dsebastien.net)：一个支持 Git 版本控制的 SQL 数据库，为智能体所做的一切提供完整、可重放的审计追踪  
- **Packs**: composable, MIT-licensed building blocks that replace Gas Town's monolithic role hierarchy  
- **组件包（Packs）**：可组合、MIT 许可的构建模块，取代 Gas Town 的单体式角色层级结构  
- **Formulas**: declarative, version-controlled, forkable workflow templates  
- **公式（Formulas）**：声明式、受版本控制、可分叉的工作流模板  

## Design Premise

## 设计前提

Individual agents hallucinate and fail. Reliability emerges from adversarial team structures, not smarter single agents. The platform's tagline could be: "you should never just have one coding agent managing a piece of infrastructure." Reliability is exposed as a dial; layered review systems (planner, builder, reviewer, witness, etc.) trade latency for confidence.

单个智能体易产生幻觉并失败。可靠性并非源于更“聪明”的单个智能体，而是源于对抗式智能体团队结构。该平台的标语或许是：“你绝不应仅靠一个编程智能体来管理某项基础设施。” 可靠性被具象化为一个可调节的旋钮；分层评审系统（规划者、构建者、审查者、见证者等）以延迟为代价换取更高置信度。

## The Shepherd Model

## 牧羊人模型

Engineers move from builders to shepherds; managing flocks of agents rather than writing all the code themselves. Unlike employees, agents have no sick leave, no vet visits, and no organizational overhead. The skill becomes designing the topology, the formulas, and the review gates, not typing every line.

工程师的角色正从“建造者”转向“牧羊人”——转而管理成群的智能体，而非亲力亲为编写每一行代码。与人类员工不同，智能体无需病假、无需兽医就诊，也无任何组织管理开销。核心能力由此转变为设计智能体拓扑结构、工作流公式及评审关卡，而非逐行敲击键盘。

## The 11-Stage AI Adoption Progression

## 11 阶段 AI 采用演进模型

Yegge extends his earlier 8-stage model (see [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)) to 11 stages, culminating in "Factory Builder" status; architects who run orchestrators that handle infrastructure, operations, and business processes autonomously. Gas City targets the upper stages (custom orchestrators, multi-pack management, autonomous business processes).

Yegge 将其早先提出的 8 阶段模型（参见 [Gas Town（燃气镇）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)）扩展至 11 阶段，最终抵达“工厂建造者（Factory Builder）”阶段——即能运行编排器、自主管理基础设施、运维及业务流程的架构师。Gas City 聚焦于高阶阶段（定制化编排器、多组件包协同管理、自主业务流程）。

## De-SaaS-ing the Enterprise

## 企业去 SaaS 化

A central economic argument: [SaaS](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net) is structurally extractive. Customers use roughly 20% of features while subsidizing the other 80%, and payments flow as recurring rent rather than compounding capital assets. Gas City's pitch is that small teams (3–5 engineers) can credibly rebuild critical lower-pyramid SaaS categories in-house using packs + formulas, converting recurring rent into versioned, owned infrastructure. Yegge frames this as repatriating capital that currently funnels into California (the world's fourth-largest economy).

一项核心经济论点是：[SaaS（软件即服务）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net) 在结构上具有掠夺性。客户仅使用约 20% 的功能，却要为其余 80% 埋单；付款形式是持续性租金，而非可复利增长的资本性资产。Gas City 的主张是：小型团队（3–5 名工程师）可切实依托组件包（packs）与公式（formulas），在内部重建关键的底层 SaaS 类别，将重复支付的租金转化为具备版本控制、完全自主拥有的基础设施。Yegge 将此描述为“资本回流”——即将当前持续涌入加州（全球第四大经济体）的资本重新引回本地。

## Observability as the Differentiator

## 可观测性作为差异化优势

Where competing agent platforms pitch raw "autonomy," Gas City's wedge is full auditability via Dolt's git-versioned database. Every action, decision, and tool call is replayable. Yegge claims this audit trail already exceeds most SaaS compliance offerings out of the box.

当竞品智能体平台主打原始的“自主性”时，Gas City 的突破口在于通过 Dolt 的 Git 版本化数据库实现全面可审计性。每一次操作、每一个决策、每一处工具调用均可完整重放。Yegge 声称，这一审计轨迹开箱即用，已超越大多数 SaaS 合规性解决方案。

## Predictions

## 预测

- **Near-term**: engineers deploy custom orchestrators for low-stakes automation, then graduate to multi-pack management  
- **短期**：工程师先部署定制化编排器用于低风险自动化任务，再逐步进阶至多组件包协同管理  
- **Mid-term**: lower tiers of the SaaS pyramid disintegrate as enterprises systematically re-platform capabilities in-house  
- **中期**：随着企业系统性地将能力内迁重构，SaaS 金字塔的底层将瓦解消散  
- **Long-term**: AI-native business processes replace traditional SaaS; "all SaaS needs to be rewritten from the ground up to be fully agentic"  
- **长期**：AI 原生业务流程将取代传统 SaaS；“所有 SaaS 都需彻底重写，方能真正实现全智能体化”

## Why It Matters

## 为何重要

Gas City is the practical articulation of a belief many of us hold but rarely operationalize: agents are not products, they are infrastructure. If the bet pays off, the next generation of business systems will be assembled from packs and formulas rather than purchased as seat licenses, and the durable moat will be the audit trail, not the model.

Gas City 是我们许多人内心认同却罕有付诸实践的一种信念之务实表达：智能体并非产品，而是基础设施。倘若这一判断最终成立，下一代商业系统将由组件包（packs）与公式（formulas）组装而成，而非按席位许可（seat license）采购；持久的竞争护城河将不再是模型本身，而是可审计、可追溯的审计轨迹。

## References

## 参考文献

- Welcome to Gas City (Steve Yegge, 2026-04-24): [https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607?ref=dsebastien.net](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607?ref=dsebastien.net)  
- 《欢迎来到 Gas City》（Steve Yegge，2026 年 4 月 24 日）：[https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607?ref=dsebastien.net](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607?ref=dsebastien.net)  
- Predecessor article (Welcome to Gas Town): [https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04?ref=dsebastien.net](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04?ref=dsebastien.net)  
- 前序文章（《欢迎来到 Gas Town》）：[https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04?ref=dsebastien.net](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04?ref=dsebastien.net)  

## Related

## 相关内容

- [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)  
- [Gas Town（燃气镇）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)  
- [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net)  
- [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net)  
- [AI Agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [AI 智能体](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)  
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)  
- [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net)  
- [Beads（珠链）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net)  
- [Software as a Service (SaaS)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net)  
- [软件即服务（SaaS）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net)
