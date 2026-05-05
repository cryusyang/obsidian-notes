---
title: "AI Open Weight Models"
url: "https://www.dsebastien.net/ai-open-weight-models/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了“开放权重（open weight）”AI模型的概念，强调其核心是公开发布训练后的模型权重，允许自由下载、运行、微调和部署，但通常不包含训练代码或数据，因此比“开源”更准确。文章列举了当前主流的开放权重模型家族，如Llama、Mistral、Gemma、Qwen、Phi、DeepSeek v4（目前最大，1.6万亿总参数）、GLM-5.1、Kimi K2系列及Granite等。指出开放权重显著促进了AI民主化、本地/私有化部署、降低厂商锁定，并支持社区协作优化，但也带来安全挑战——一旦发布便无法撤回，加剧滥用风险。

---

> *This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [AI Open Weight Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net).*

> 这是我个人 [公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net) 中的一则记录。查看权威版本：[AI 开放权重模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)。

AI models whose trained weights are publicly released, allowing anyone to download, run, fine-tune, and deploy them. "Open weight" is more precise than "open source" because most releases don't include training code or data.

AI 模型若将其训练完成的权重参数（trained weights）向公众开放发布，即允许任何人下载、运行、微调及部署该模型，则属于“开放权重”（open weight）模型。“开放权重”这一表述比“开源”（open source）更为准确，因为绝大多数此类发布并不包含训练代码或训练数据。

Key families: Llama (Meta), Mistral/Mixtral (Mistral AI), Gemma ([Google DeepMind](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+DeepMind?ref=dsebastien.net)), Qwen (Alibaba), Phi (Microsoft), DeepSeek (see [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net) — currently the largest open-weights model at 1.6T total / 49B active params), [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net) ([Zhipu AI (Z.ai)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)), Kimi K2 ([Moonshot AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net), see [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) and [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)), [Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite+4.1?ref=dsebastien.net) (IBM — dense, enterprise-targeted, [Apache 2.0](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)).

主要模型家族包括：Llama（Meta）、Mistral / Mixtral（Mistral AI）、Gemma（[Google DeepMind](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+DeepMind?ref=dsebastien.net)）、Qwen（阿里巴巴）、Phi（微软）、DeepSeek（参见 [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)——当前规模最大的开放权重模型，总参数量达 1.6 万亿，活跃参数量为 490 亿）、[GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net)（[智谱 AI（Z.ai）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)）、Kimi K2（[月之暗面（Moonshot AI）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net)，参见 [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) 和 [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)）、[Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite+4.1?ref=dsebastien.net)（IBM——稠密架构、面向企业场景、采用 [Apache 2.0 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)）。

Significance: democratizes AI access, enables local/private deployment, reduces vendor lock-in, enables community fine-tuning. Tension with safety: open weights can't be un-released, making misuse harder to prevent.

重要意义在于：推动人工智能普惠化（民主化获取），支持本地化或私有化部署，降低对特定供应商的依赖（减少厂商锁定），并赋能社区开展协作式微调。但与此同时亦存在安全张力：一旦权重开放发布便不可撤回，因而难以遏制潜在的滥用行为。

## Open-weight model notes

## 开放权重模型笔记

Auto-populated from notes carrying `ai/open_weight`. Tag a note rather than editing this list to add a model.

本列表由所有带有 `ai/open_weight` 标签的笔记自动聚合生成。如需新增模型，请直接为对应笔记添加该标签，而非手动编辑此列表。

- [2026-04-21 Kimi K2.6, Qwen, and Gemma 4 - Local AI Is Catching Up](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-04-21+Kimi+K2.6,+Qwen,+and+Gemma+4+-+Local+AI+Is+Catching+Up?ref=dsebastien.net)
- [Baichuan](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Baichuan?ref=dsebastien.net)
- [Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite?ref=dsebastien.net)
- [Hermes](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hermes?ref=dsebastien.net)
- [Kimi](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi?ref=dsebastien.net)
- [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)
- [Moonshot AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net)
- [Nous Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Nous+Research?ref=dsebastien.net)
- [Stability AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Stability+AI?ref=dsebastien.net)
- [Zhipu AI (Z.ai)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)

- [2026-04-21 Kimi K2.6、Qwen 与 Gemma 4——本地 AI 正在迎头赶上](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-04-21+Kimi+K2.6,+Qwen,+and+Gemma+4+-+Local+AI+Is+Catching+Up?ref=dsebastien.net)
- [百川（Baichuan）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Baichuan?ref=dsebastien.net)
- [Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite?ref=dsebastien.net)
- [Hermes](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hermes?ref=dsebastien.net)
- [Kimi](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi?ref=dsebastien.net)
- [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)
- [月之暗面（Moonshot AI）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net)
- [Nous Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Nous+Research?ref=dsebastien.net)
- [Stability AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Stability+AI?ref=dsebastien.net)
- [智谱 AI（Zhipu AI，Z.ai）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)

## References

## 参考文献

## Related

## 相关主题

- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)
- [Knowledge Distillation](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Knowledge+Distillation?ref=dsebastien.net)
- [Low Rank Adapter (LoRA)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Low+Rank+Adapter+(LoRA)?ref=dsebastien.net)
- [Atropos](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Atropos?ref=dsebastien.net)
- [Tinker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tinker?ref=dsebastien.net)
- [Axolotl](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Axolotl?ref=dsebastien.net)

- [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)
- [知识蒸馏（Knowledge Distillation）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Knowledge+Distillation?ref=dsebastien.net)
- [低秩适配器（LoRA）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Low+Rank+Adapter+(LoRA)?ref=dsebastien.net)
- [Atropos](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Atropos?ref=dsebastien.net)
- [Tinker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tinker?ref=dsebastien.net)
- [Axolotl](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Axolotl?ref=dsebastien.net)
