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
> Gas City 是 Steve Yegge 于2026年4月发布的开源SDK，作为 Gas Town 的继任者，它将单体多智能体平台解构为可组合的“packs”模块，支持开发者按需构建任意拓扑结构的AI协作团队。其核心包括MEOW（以“工作”为一等公民的表达框架）、Dolt（Git版本化的SQL数据库，提供全操作可追溯审计）、声明式可分叉的“Formulas”流程模板，以及强调对抗性团队协作而非单点智能的可靠性设计哲学。平台推动工程师角色从“编码者”转向“牧羊人”，专注于设计代理拓扑、审查机制与工作流，而非直接编写代码。Gas City 还提出“去SaaS化”主张，使小团队能用开源packs重建关键企业服务，将SaaS租金转化为自有、可版本化、可审计的基础设施。

---

> *这是来自我的 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 的一则笔记。查看规范版本：[Gas City](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+City?ref=dsebastien.net)。*

> *这是来自我的 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 的一则笔记。查看规范版本：[Gas City](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+City?ref=dsebastien.net)。*

Gas City 是一个 SDK，也是 Steve Yegge 所提出的 [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net) 的继任者，于 2026 年 4 月 24 日正式发布。Gas Town 推出了一个单一、强观点的多智能体平台；而 Gas City 则将该架构解构为一系列可组合的构建模块（称为“packs”），使开发者能够按需组装具备任意协作拓扑结构的 AI 智能体团队。Yegge 将其定义为一座“亮工厂”（light factory）——即暗工厂（dark factory）中那种自主、后台运行的工作模式，但全程保持“开灯”状态（即完全透明、全程可观测）。

Gas City 是一个 SDK，也是 Steve Yegge 所提出的 [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net) 的继任者，于 2026 年 4 月 24 日正式发布。Gas Town 推出了一个单一、强观点的多智能体平台；而 Gas City 则将该架构解构为一系列可组合的构建模块（称为“packs”），使开发者能够按需组装具备任意协作拓扑结构的 AI 智能体团队。Yegge 将其定义为一座“亮工厂”（light factory）——即暗工厂（dark factory）中那种自主、后台运行的工作模式，但全程保持“开灯”状态（即完全透明、全程可观测）。

## 核心技术栈

## 核心技术栈

- **MEOW**（工作分子化表达，Molecular Expression of Work）：基于 [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net) 的框架，将“工作”（Work）作为头等原语（包括史诗级任务 epic、分子 molecule、原型分子 protomolecule、公式 formula）
- **[Dolt](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dolt?ref=dsebastien.net)**：一个支持 Git 版本控制的 SQL 数据库，为所有智能体行为提供完整、可重放的审计追踪
- **Packs（模块包）**：可组合、MIT 开源许可的构建模块，用以替代 Gas Town 中的单体式角色层级结构
- **Formulas（公式）**：声明式、受版本控制、可分叉的工作流模板

- **MEOW**（工作分子化表达，Molecular Expression of Work）：基于 [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net) 的框架，将“工作”（Work）作为头等原语（包括史诗级任务 epic、分子 molecule、原型分子 protomolecule、公式 formula）
- **[Dolt](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dolt?ref=dsebastien.net)**：一个支持 Git 版本控制的 SQL 数据库，为所有智能体行为提供完整、可重放的审计追踪
- **Packs（模块包）**：可组合、MIT 开源许可的构建模块，用以替代 Gas Town 中的单体式角色层级结构
- **Formulas（公式）**：声明式、受版本控制、可分叉的工作流模板

## 设计前提

## 设计前提

单个智能体会产生幻觉并失败；可靠性并非源于更“聪明”的单体智能体，而是源自对抗性的团队结构。该平台的标语可概括为：“你绝不应仅靠一个编码智能体来管理某项基础设施。” 可靠性被显式地设计为一个可调节的旋钮（dial）：通过分层评审系统（如规划者 planner、构建者 builder、审核者 reviewer、见证者 witness 等）在延迟与置信度之间进行权衡取舍。

单个智能体会产生幻觉并失败；可靠性并非源于更“聪明”的单体智能体，而是源自对抗性的团队结构。该平台的标语可概括为：“你绝不应仅靠一个编码智能体来管理某项基础设施。” 可靠性被显式地设计为一个可调节的旋钮（dial）：通过分层评审系统（如规划者 planner、构建者 builder、审核者 reviewer、见证者 witness 等）在延迟与置信度之间进行权衡取舍。

## 牧羊人模型

## 牧羊人模型

工程师的角色正从“建造者”转向“牧羊人”——他们不再亲自编写全部代码，而是管理一群协同工作的智能体“羊群”。与人类员工不同，智能体无需病假、无需兽医就诊，也无任何组织管理开销。核心技能由此转变为：设计智能体拓扑结构、编写公式（formulas）、设置评审关卡（review gates），而非逐行敲写代码。

工程师的角色正从“建造者”转向“牧羊人”——他们不再亲自编写全部代码，而是管理一群协同工作的智能体“羊群”。与人类员工不同，智能体无需病假、无需兽医就诊，也无任何组织管理开销。核心技能由此转变为：设计智能体拓扑结构、编写公式（formulas）、设置评审关卡（review gates），而非逐行敲写代码。

## 11 阶段 AI 采用演进模型

## 11 阶段 AI 采用演进模型

Yegge 将其早先提出的 8 阶段模型（参见 [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)）进一步扩展至 11 阶段，最终阶段为“工厂建造者”（Factory Builder）：即能够运行自主型编排器（orchestrator）的架构师，该编排器可全自动处理基础设施、运维及业务流程。Gas City 明确聚焦于高阶阶段——定制化编排器、多模块包（multi-pack）协同管理、以及端到端自主业务流程。

Yegge 将其早先提出的 8 阶段模型（参见 [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)）进一步扩展至 11 阶段，最终阶段为“工厂建造者”（Factory Builder）：即能够运行自主型编排器（orchestrator）的架构师，该编排器可全自动处理基础设施、运维及业务流程。Gas City 明确聚焦于高阶阶段——定制化编排器、多模块包（multi-pack）协同管理、以及端到端自主业务流程。

## 企业去 SaaS 化（De-SaaS-ing the Enterprise）

## 企业去 SaaS 化（De-SaaS-ing the Enterprise）

其核心经济论点是：[软件即服务（SaaS）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net) 在结构上具有剥削性。客户实际仅使用约 20% 的功能，却要为其余 80% 功能付费；支付模式是持续性租金，而非形成可复利增长的资本性资产。Gas City 的主张是：小型工程团队（3–5 名工程师）完全有能力借助 packs + formulas，在内部可信地重建关键的底层 SaaS 类别，从而将周期性租金支出，转化为可版本化、可自主掌控的基础设施资产。Yegge 将此过程称为“资本回流”——把当前持续流向加州（全球第四大经济体）的资本重新引回企业自身。

其核心经济论点是：[软件即服务（SaaS）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net) 在结构上具有剥削性。客户实际仅使用约 20% 的功能，却要为其余 80% 功能付费；支付模式是持续性租金，而非形成可复利增长的资本性资产。Gas City 的主张是：小型工程团队（3–5 名工程师）完全有能力借助 packs + formulas，在内部可信地重建关键的底层 SaaS 类别，从而将周期性租金支出，转化为可版本化、可自主掌控的基础设施资产。Yegge 将此过程称为“资本回流”——把当前持续流向加州（全球第四大经济体）的资本重新引回企业自身。

## 可观测性即差异化优势

## 可观测性即差异化优势

相较于竞品平台主打原始的“自主性”（autonomy），Gas City 的突破口在于通过 Dolt 的 Git 版本化数据库实现全链路可观测性。每一次操作、每一项决策、每一次工具调用均可完整重放。Yegge 声称，该审计追踪能力开箱即用，已超越目前绝大多数 SaaS 合规解决方案。

相较于竞品平台主打原始的“自主性”（autonomy），Gas City 的突破口在于通过 Dolt 的 Git 版本化数据库实现全链路可观测性。每一次操作、每一项决策、每一次工具调用均可完整重放。Yegge 声称，该审计追踪能力开箱即用，已超越目前绝大多数 SaaS 合规解决方案。

## 预测

## 预测

- **短期**：工程师率先部署定制化编排器用于低风险自动化任务，随后进阶至多模块包（multi-pack）协同管理  
- **中期**：SaaS 金字塔的底层类别将系统性瓦解，企业将有计划地将能力内迁重构  
- **长期**：AI 原生业务流程将全面取代传统 SaaS；“所有 SaaS 都需从底层彻底重写，方能成为真正意义上的全智能体系统”

- **短期**：工程师率先部署定制化编排器用于低风险自动化任务，随后进阶至多模块包（multi-pack）协同管理  
- **中期**：SaaS 金字塔的底层类别将系统性瓦解，企业将有计划地将能力内迁重构  
- **长期**：AI 原生业务流程将全面取代传统 SaaS；“所有 SaaS 都需从底层彻底重写，方能成为真正意义上的全智能体系统”

## 其重要性何在？

## 其重要性何在？

Gas City 是对一种普遍持有却鲜少落地践行之信念的务实表达：智能体不是产品，而是基础设施。倘若这一判断成立，那么下一代商业系统将不再以席位许可（seat license）形式采购，而是由 packs 和 formulas 组装而成；持久的竞争壁垒将不再是模型本身，而是不可篡改、完整可溯的审计轨迹。

Gas City 是对一种普遍持有却鲜少落地践行之信念的务实表达：智能体不是产品，而是基础设施。倘若这一判断成立，那么下一代商业系统将不再以席位许可（seat license）形式采购，而是由 packs 和 formulas 组装而成；持久的竞争壁垒将不再是模型本身，而是不可篡改、完整可溯的审计轨迹。

## 参考文献

## 参考文献

- 《欢迎来到 Gas City》（Steve Yegge，2026-04-24）：[https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607)  
- 前序文章（《欢迎来到 Gas Town》）：[https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)

- 《欢迎来到 Gas City》（Steve Yegge，2026-04-24）：[https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607](https://steve-yegge.medium.com/welcome-to-gas-city-57f564bb3607)  
- 前序文章（《欢迎来到 Gas Town》）：[https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)

## 相关链接

## 相关链接

- [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)  
- [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net)  
- [AI 智能体（AI Agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)  
- [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net)  
- [软件即服务（SaaS）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net)

- [Gas Town](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gas+Town?ref=dsebastien.net)  
- [Steve Yegge](https://notes.dsebastien.net/30+Areas/36+People/Steve+Yegge?ref=dsebastien.net)  
- [AI 智能体（AI Agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agents?ref=dsebastien.net)  
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)  
- [Beads](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Beads?ref=dsebastien.net)  
- [软件即服务（SaaS）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+as+a+Service+(SaaS)?ref=dsebastien.net)
