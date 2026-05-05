---
title: "AI Skill Composability"
url: "https://www.dsebastien.net/ai-skill-composability/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了AI技能可组合性（AI Skill Composability）的概念，即通过模块化、可复用的细粒度AI技能（如“读取笔记”“搜索内容”）替代单一大型提示词，由AI代理动态编排以构建复杂能力。文章阐述了其核心价值：提升复用性、可维护性、可测试性与灵活性，并总结了技能链式调用、选择、分层、上下文加载及按需懒加载（PLL）等典型组合模式。同时指出实践中的挑战，包括依赖冲突、上下文长度超限、执行顺序敏感和版本兼容性问题，并强调遵循单一职责、清晰接口、低耦合与渐进式披露等设计原则。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [AI Skill Composability](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[AI技能可组合性（AI Skill Composability）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Composability?ref=dsebastien.net)。

The ability to build complex AI agent capabilities by combining smaller, reusable [AI Agent Skills](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net). Instead of writing monolithic prompts, composable skills are modular: each does one thing well, and agents orchestrate them together.

通过组合更小、可复用的[AI智能体技能（AI Agent Skills）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)，构建复杂AI智能体能力的能力。与编写庞大单一的提示词不同，可组合的技能是模块化的：每个技能专注做好一件事，而智能体则负责协同调用它们。

## Why composability matters

## 为何可组合性至关重要

- **Reuse**: a skill for "read vault note" can be used by a ghostwriter agent, a researcher agent, and a maintenance agent  
- **复用性**：一项“读取知识库笔记”的技能，可被代笔智能体、研究智能体和维护智能体共同使用  

- **Maintainability**: updating one skill improves every agent that uses it  
- **可维护性**：更新某一项技能，即可提升所有使用该技能的智能体  

- **Testability**: small skills are easier to verify than large monolithic prompts  
- **可测试性**：小型技能比庞大单一的提示词更容易验证  

- **Flexibility**: new agents can be created by combining existing skills in new ways, without writing from scratch  
- **灵活性**：可通过以新方式组合现有技能来创建新型智能体，无需从零编写  

## Composition patterns

## 组合模式

- **Skill chaining**: one skill's output feeds into another (e.g., "search notes" → "summarize results" → "write draft")  
- **技能链式调用（Skill chaining）**：一个技能的输出作为下一个技能的输入（例如：“搜索笔记” → “总结结果” → “撰写草稿”）  

- **Skill selection**: the agent picks which skill to use based on the task ([AI Agent Routing](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net) at the skill level)  
- **技能选择（Skill selection）**：智能体根据任务需求自主选择调用哪项技能（即在技能层级实现的[AI智能体路由（AI Agent Routing）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net)）  

- **Skill layering**: a higher-level skill orchestrates several lower-level skills (e.g., a "publish newsletter" skill that calls "write content", "optimize images", "upload to Ghost")  
- **技能分层（Skill layering）**：高层级技能协调调度若干低层级技能（例如：“发布通讯简报”技能会依次调用“撰写内容”、“优化图片”、“上传至Ghost平台”等子技能）  

- **Context loaders**: non-executable skills that provide context to other skills (e.g., loading writing style before the ghostwriter skill runs)  
- **上下文加载器（Context loaders）**：不可执行的技能，专用于为其他技能提供上下文信息（例如：在代笔智能体技能运行前，预先加载写作风格设定）  

- [**Prompt Lazy Loading AI Design Pattern (PLL)**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net): loading skills on demand rather than upfront, preserving [Context Budget](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  
- [**提示词懒加载AI设计模式（Prompt Lazy Loading AI Design Pattern, PLL）**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)：按需加载技能而非预先全部加载，从而节省并保护[上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  

## Current approaches

## 当前实践方法

- **Skill manifests**: agents declare which skills they use in a DEPENDENCIES.md file  
- **技能清单（Skill manifests）**：智能体在 `DEPENDENCIES.md` 文件中声明其依赖使用的技能  

- **Skill dependencies**: skills can reference other skills (e.g., "load osk-note-writer skill first")  
- **技能依赖（Skill dependencies）**：技能可显式引用其他技能（例如：“优先加载 osk-note-writer 技能”）  

- **Agent-as-composer**: the agent itself is the orchestration layer, choosing which skills to invoke based on the task  
- **智能体即编排者（Agent-as-composer）**：智能体自身即为编排层，依据具体任务动态决定调用哪些技能  

- **Plugin systems**: [Claude Code Plugins](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code+Plugins?ref=dsebastien.net) provide structured skill packaging with dependency metadata  
- **插件系统（Plugin systems）**：[Claude代码插件（Claude Code Plugins）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code+Plugins?ref=dsebastien.net) 提供结构化技能封装，并附带依赖关系元数据  

## Design principles

## 设计原则

- **Single responsibility**: each skill does one thing well  
- **单一职责**：每项技能只专注做好一件事  

- **Clear interfaces**: skills declare what input they need and what output they produce  
- **清晰接口**：技能明确声明所需输入及所产出输出  

- **Minimal coupling**: skills should work independently, not assume other skills are loaded  
- **低耦合性**：技能应能独立运行，不预设其他技能已被加载  

- **Progressive disclosure**: start with a summary, load details only when needed (PLL)  
- **渐进式披露**：先呈现摘要，仅在需要时才加载详细内容（即PLL模式）  

## The composability challenge

## 可组合性挑战

As skill libraries grow, composition introduces complexity:  

随着技能库规模扩大，组合使用将引入新的复杂性：

- **Dependency conflicts**: two skills may assume incompatible context or conventions  
- **依赖冲突**：两项技能可能基于互不兼容的上下文或约定  

- **Token explosion**: composing many skills can exceed the [Context Budget](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  
- **Token爆炸**：组合调用过多技能可能导致超出[上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  

- **Ordering sensitivity**: skill load order can affect behavior  
- **顺序敏感性**：技能加载顺序可能影响整体行为  

- **Version compatibility**: updating one skill may break agents that compose it with others  
- **版本兼容性**：更新某一项技能，可能导致与其组合使用的智能体出现故障  

## References

## 参考文献

  

## Related

## 相关主题

- [AI Agent Skills](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)  
- [AI智能体技能（AI Agent Skills）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Skills?ref=dsebastien.net)  

- [AI Skill Distribution](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Distribution?ref=dsebastien.net)  
- [AI技能分发（AI Skill Distribution）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Skill+Distribution?ref=dsebastien.net)  

- [AI Agent Distribution](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Distribution?ref=dsebastien.net)  
- [AI智能体分发（AI Agent Distribution）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Distribution?ref=dsebastien.net)  

- [AI Agent Routing](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net)  
- [AI智能体路由（AI Agent Routing）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Agent+Routing?ref=dsebastien.net)  

- [Prompt Lazy Loading AI Design Pattern (PLL)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)  
- [提示词懒加载AI设计模式（Prompt Lazy Loading AI Design Pattern, PLL）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+Lazy+Loading+AI+Design+Pattern+(PLL)?ref=dsebastien.net)  

- [Context Budget](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  
- [上下文预算（Context Budget）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Budget?ref=dsebastien.net)  

- [Claude Code Plugins](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code+Plugins?ref=dsebastien.net)  
- [Claude代码插件（Claude Code Plugins）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code+Plugins?ref=dsebastien.net)  

- [Agentic Engineering](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Agentic+Engineering?ref=dsebastien.net)  
- [智能体工程（Agentic Engineering）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Agentic+Engineering?ref=dsebastien.net)  

- [Agent System Engineering](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Agent+System+Engineering?ref=dsebastien.net)  
- [智能体系统工程（Agent System Engineering）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Agent+System+Engineering?ref=dsebastien.net)  

- [Atomicity](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Atomicity?ref=dsebastien.net)  
- [原子性（Atomicity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Atomicity?ref=dsebastien.net)  

- [Composition over Inheritance](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Composition+over+Inheritance?ref=dsebastien.net)  
- [组合优于继承（Composition over Inheritance）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Composition+over+Inheritance?ref=dsebastien.net)  

- [Barrel Pattern](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Barrel+Pattern?ref=dsebastien.net)  
- [桶模式（Barrel Pattern）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Barrel+Pattern?ref=dsebastien.net)  

- [SOLID Principles](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/SOLID+Principles?ref=dsebastien.net)  
- [SOLID原则（SOLID Principles）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/SOLID+Principles?ref=dsebastien.net)  

- [Software Design Patterns for AI Skills and Agents](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+Design+Patterns+for+AI+Skills+and+Agents?ref=dsebastien.net)  
- [面向AI技能与智能体的软件设计模式（Software Design Patterns for AI Skills and Agents）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Software+Design+Patterns+for+AI+Skills+and+Agents?ref=dsebastien.net)
