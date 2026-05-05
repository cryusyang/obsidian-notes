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
> 本文介绍了“开放权重（open weight）”AI模型的概念，即公开发布训练后模型权重，允许用户自由下载、运行、微调和部署，但通常不包含训练代码或数据，因此比“开源”更准确。文中列举了多个主流开放权重模型家族，如Llama、Mistral、Gemma、Qwen、Phi、DeepSeek（当前最大，达1.6万亿总参数）、GLM-5.1、Kimi K2系列及IBM的Granite等。开放权重模型的意义在于促进AI民主化、支持本地/私有部署、降低厂商锁定风险，并推动社区协作微调；但也带来安全挑战，因权重一旦发布便无法撤回，增加了滥用风险。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [AI Open Weight Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[AI 开放权重模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)。

AI models whose trained weights are publicly released, allowing anyone to download, run, fine-tune, and deploy them. "Open weight" is more precise than "open source" because most releases don't include training code or data.

其训练后的权重参数被公开发布的 AI 模型，允许任何人下载、运行、微调和部署。“开放权重”（open weight）比“开源”（open source）更为准确，因为大多数发布版本并不包含训练代码或训练数据。

Key families: Llama (Meta), Mistral/Mixtral (Mistral AI), Gemma ([Google DeepMind](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+DeepMind?ref=dsebastien.net)), Qwen (Alibaba), Phi (Microsoft), DeepSeek (see [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net) — currently the largest open-weights model at 1.6T total / 49B active params), [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net) ([Zhipu AI (Z.ai)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)), Kimi K2 ([Moonshot AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net), see [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) and [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)), [Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite+4.1?ref=dsebastien.net) (IBM — dense, enterprise-targeted, [Apache 2.0](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)).

主要模型家族包括：Llama（Meta）、Mistral / Mixtral（Mistral AI）、Gemma（[Google DeepMind](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+DeepMind?ref=dsebastien.net)）、Qwen（阿里巴巴）、Phi（微软）、DeepSeek（参见 [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)——当前参数量最大的开放权重模型，总参数达 1.6 万亿，活跃参数为 490 亿）、[GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net)（[智谱 AI（Z.ai）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)）、Kimi K2（[月之暗面 AI（Moonshot AI）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net)，参见 [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) 和 [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)）、[Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite+4.1?ref=dsebastien.net)（IBM——稠密架构、面向企业应用、采用 [Apache 2.0 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)）。

Significance: democratizes AI access, enables local/private deployment, reduces vendor lock-in, enables community fine-tuning. Tension with safety: open weights can't be un-released, making misuse harder to prevent.

重要意义在于：推动 AI 技术的普惠化；支持本地化或私有化部署；降低厂商锁定风险；赋能社区开展协作式微调。但与安全性存在张力：一旦权重开放发布便无法撤回，使得潜在滥用行为更难防范。

## Open-weight model notes

## 开放权重模型备注

Auto-populated from notes carrying `ai/open_weight`. Tag a note rather than editing this list to add a model.

该列表由标注了 `ai/open_weight` 标签的笔记自动填充。如需新增模型，请为对应笔记添加标签，而非直接编辑本列表。

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

- [2026-04-21 Kimi K2.6、Qwen 与 Gemma 4 —— 本地 AI 正在迎头赶上](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-04-21+Kimi+K2.6,+Qwen,+and+Gemma+4+-+Local+AI+Is+Catching+Up?ref=dsebastien.net)
- [百川（Baichuan）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Baichuan?ref=dsebastien.net)
- [Granite](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite?ref=dsebastien.net)
- [Hermes](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hermes?ref=dsebastien.net)
- [Kimi](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi?ref=dsebastien.net)
- [Kimi K2.5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net)
- [月之暗面 AI（Moonshot AI）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net)
- [Nous Research](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Nous+Research?ref=dsebastien.net)
- [Stability AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Stability+AI?ref=dsebastien.net)
- [智谱 AI（Z.ai）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net)

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
