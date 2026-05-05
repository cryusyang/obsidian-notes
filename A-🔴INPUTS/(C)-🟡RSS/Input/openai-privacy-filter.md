---
title: "OpenAI Privacy Filter"
url: "https://www.dsebastien.net/openai-privacy-filter/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> OpenAI发布了开源、Apache 2.0许可的轻量级隐私过滤模型Privacy Filter，用于高效识别和掩码文本中的八类PII（如姓名、邮箱、电话等），适用于LLM输入前置过滤、数据脱敏及本地化隐私保护。该模型采用单次token分类+约束Viterbi解码，支持精度/召回率调节，仅50M参数且兼容128k上下文，便于嵌入高吞吐流水线。尽管具备可微调性与自托管优势，但它不构成合规保证，对非英语、非拉丁语系及罕见命名模式效果有限，高敏感场景仍需人工复核。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [OpenAI Privacy Filter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI+Privacy+Filter?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[OpenAI 隐私过滤器](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI+Privacy+Filter?ref=dsebastien.net)。

OpenAI Privacy Filter is an open-weight, [Apache 2.0](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)-licensed token-classification model published by [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net) on [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net) for **detecting and masking personally identifiable information (PII) in text**. It is designed for high-throughput data sanitization workflows: feeding LLMs, redacting datasets, on-prem privacy filtering. It is *not* a compliance guarantee — it is one layer in a broader privacy-by-design stack.

OpenAI 隐私过滤器是一款开源权重、采用[Apache 2.0 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)的词元分类模型，由[OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net)在[HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)上发布，专用于**检测和屏蔽文本中的个人身份信息（PII）**。它面向高吞吐量的数据净化工作流而设计，例如为大语言模型（LLM）提供输入、对数据集进行脱敏处理、以及本地部署的隐私过滤。它**并非合规性保证**——而是更广泛的“以隐私为本”（privacy-by-design）架构中的一环。

This is a notable release because OpenAI rarely ships open weights, and because privacy filtering is one of the highest-leverage things to add in front of any [LLM](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) pipeline that touches user data — particularly for anyone running BYOK or local inference setups (see [Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net)).

此次发布意义重大，一方面因为 OpenAI 极少开源模型权重；另一方面，隐私过滤是任何触及用户数据的[大语言模型（LLM）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)流水线前端最具杠杆效应的增强措施之一——尤其适用于采用“自带密钥”（BYOK）或本地推理部署的用户（参见文章：[你的 AI 提示词究竟去了哪里？——AI 隐私实用指南](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net)）。

## Specs

## 规格

| Aspect | Detail |
|--------|--------|
| **Developer** | [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net) |
| **License** | [Apache 2.0 License](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net) (permissive) |
| **Total params** | 1.5B |
| **Active params** | 50M (sparse [MoE](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net), 128 experts, top-4) |
| **Architecture** | 8 transformer blocks, grouped-query attention, sparse MoE, single-pass |
| **Context window** | 128k tokens |
| **Decoding** | Constrained Viterbi over BIOES span labels |
| **Distribution** | HuggingFace (`openai/privacy-filter`), runs via [Transformers](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net) or Transformers.js (browser) |

| 方面 | 详情 |
|------|------|
| **开发者** | [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net) |
| **许可证** | [Apache 2.0 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)（宽松型） |
| **总参数量** | 15 亿（1.5B） |
| **活跃参数量** | 5000 万（50M）（稀疏型[专家混合模型（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)，含 128 个专家，每次激活 Top-4） |
| **架构** | 8 层 Transformer 块、分组查询注意力（grouped-query attention）、稀疏 MoE、单次前向传递（single-pass） |
| **上下文窗口** | 128K 词元 |
| **解码方式** | 在 BIOES 实体跨度标签上执行受约束的维特比（Viterbi）算法 |
| **分发方式** | HuggingFace（模型 ID：`openai/privacy-filter`），可通过 [Transformers](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net) 库或 Transformers.js（浏览器端）运行 |

## What it detects

## 检测内容

Eight PII span categories:

八类 PII 实体跨度：

1. Account number  
2. Private address  
3. Private email  
4. Private person (name)  
5. Private phone  
6. Private URL  
7. Private date  
8. Secret  

1. 账户号码  
2. 私人住址  
3. 私人邮箱  
4. 私人姓名（自然人）  
5. 私人电话  
6. 私人网址（URL）  
7. 私人日期  
8. 密钥/密文（Secret）

The model labels all tokens in a single pass (not autoregressive), then runs constrained Viterbi to produce coherent BIOES spans. A runtime threshold tunes the precision/recall tradeoff per use case.

该模型以单次前向传递（非自回归式）方式为所有词元打标签，再通过受约束的维特比算法生成连贯的 BIOES 实体跨度标注。运行时阈值可根据具体应用场景灵活调节精确率与召回率的权衡。

## Why it matters

## 为何重要

- **Open weights from OpenAI is rare.** It also lowers the bar for self-hosted, on-prem privacy filtering.  
- **Right place in the stack.** PII detection belongs in front of any third-party LLM call, especially for cloud AI APIs that retain inputs by default. See the four data paths in [Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net).  
- **Small, efficient.** 50M active params + 128k context means it can sit in front of a request without dominating latency or cost.  
- **Fine-tunable.** Domains with their own privacy taxonomies (medical, legal, HR) can extend the label set.  

- **OpenAI 开源权重极为罕见。** 同时也大幅降低了自托管、本地化隐私过滤的技术门槛。  
- **在技术栈中位置关键。** PII 检测理应置于任何调用第三方大语言模型（LLM）的请求之前，尤其是默认保留输入数据的云 AI API。详见文章《[你的 AI 提示词究竟去了哪里？——AI 隐私实用指南](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net)》中所述的四条数据路径。  
- **轻量、高效。** 仅 5000 万活跃参数 + 128K 上下文窗口，使其可无缝嵌入请求链路前端，而不会显著增加延迟或成本。  
- **支持微调。** 医疗、法律、人力资源等具有专属隐私分类体系的领域，可扩展其标签集以适配特定需求。

## Limitations

## 局限性

- Not a compliance guarantee — should be **one layer** in a broader privacy-by-design approach.  
- Performance drops on non-English text, non-Latin scripts, and underrepresented naming patterns.  
- Failure modes include under-detection of uncommon names and over-redaction of public entities.  
- High-sensitivity settings (medical, legal, financial, HR) still require human review.  

- 并非合规性保证——仅应作为更全面的“以隐私为本”架构中的**其中一环**。  
- 在非英语文本、非拉丁字母文字（如中文、阿拉伯文、西里尔文等）及低频命名模式上的性能明显下降。  
- 典型失效场景包括：对罕见姓名识别不足，以及对公共实体（如知名机构、地名）过度脱敏。  
- 在高敏感度场景（医疗、法律、金融、人力资源）中，仍需人工复核。

## Use cases

## 使用场景

| Use case | How the filter fits |
|----------|---------------------|
| **Pre-prompt sanitization** | Strip PII before sending prompts to a third-party LLM API |
| **Dataset cleaning** | Redact PII from training, fine-tuning, or analytics datasets |
| **On-prem privacy gateway** | Filter inbound/outbound text in a self-hosted AI pipeline |
| **Browser-side filtering** | Run via Transformers.js to redact before data ever leaves the device |
| **Custom redaction policies** | Fine-tune for domain-specific PII (medical IDs, legal refs) |

| 使用场景 | 过滤器的适用方式 |
|----------|------------------|
| **提示词预处理脱敏** | 在将提示词发送至第三方大语言模型（LLM）API 前，剥离其中的 PII 信息 |
| **数据集清洗** | 从训练、微调或分析所用数据集中脱敏 PII 信息 |
| **本地化隐私网关** | 在自托管 AI 流水线中，对进出文本实施过滤 |
| **浏览器端过滤** | 通过 Transformers.js 在设备本地运行，确保数据在离开终端前即完成脱敏 |
| **定制化脱敏策略** | 微调模型以识别特定领域的 PII（如医疗编号、法律案号等） |

## References

## 参考资料

- [https://huggingface.co/openai/privacy-filter](https://huggingface.co/openai/privacy-filter)

- [https://huggingface.co/openai/privacy-filter](https://huggingface.co/openai/privacy-filter)

## Related

## 相关链接

- [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net)  
- [AI Privacy](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net)  
- [Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net)  
- [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)  
- [Apache 2.0 License](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)  
- [Transformers](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net)  
- [AI Mixture of Experts (MoE)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)  
- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  

- [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net)  
- [AI 隐私](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net)  
- [你的 AI 提示词究竟去了哪里？——AI 隐私实用指南（文章）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net)  
- [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)  
- [Apache 2.0 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net)  
- [Transformers 库](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net)  
- [AI 专家混合模型（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)  
- [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)
