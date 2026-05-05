---
title: "DeepSeek v4"
url: "https://www.dsebastien.net/deepseek-v4/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> DeepSeek于2026年4月24日发布第四代旗舰模型V4，包含两个开源权重变体：V4-Pro（1.6T总参数/49B激活参数）和V4-Flash（284B总参数/13B激活参数），均采用MoE架构，支持100万token上下文窗口，并首次将专用推理模型R系列整合进统一模型，支持可切换的“思考/非思考”模式。核心创新为DeepSeek稀疏注意力（DSA）与逐token压缩技术，大幅降低计算开销——V4-Pro相较V3.2节省约73%单token FLOPs和90% KV缓存，1M上下文KV缓存仅需约5.7GB（FP8），使长上下文推理在消费级硬件上真正可行。模型具备确定性内核、原生兼容OpenAI与Anthropic API格式，并以显著低于竞品的价格提供高性能推理能力：V4-Pro在数学/STEM/编程基准上超越所有现有开源模型、逼近闭源SOTA；V4-Flash则以极低成本实现接近Pro的推理表现。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)。

Fourth-generation flagship release from [Deepseek](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Deepseek?ref=dsebastien.net) (April 24, 2026). Two open-weight variants — V4-Pro (1.6T total / 49B active parameters) and V4-Flash (284B total / 13B active) — both built on a [MoE](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net) architecture, ship with a 1M-token [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) by default, and fold what was the separate R reasoning line into a single model with switchable Thinking / Non-Thinking modes.

由[Deepseek](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Deepseek?ref=dsebastien.net)发布的第四代旗舰模型（2026年4月24日）。包含两个开源权重变体——V4-Pro（总参数1.6万亿 / 激活参数490亿）与V4-Flash（总参数2840亿 / 激活参数130亿）——二者均基于[混合专家（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)架构，默认搭载100万token的[上下文窗口（Context Window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)，并将原先独立的R系列推理能力整合进单一模型，支持可切换的“思考模式（Thinking）”与“非思考模式（Non-Thinking）”。

V4-Pro is the largest [open weights](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net) model released to date.

V4-Pro 是迄今发布的参数规模最大的[开源权重（open weights）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)模型。

## What's actually new

## 实际上有哪些新特性

- **DeepSeek Sparse Attention (DSA) + token-wise compression.** The headline architectural innovation; a content-based variant of [AI Sparse Attention](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net). V4-Pro uses ~27% of the single-token FLOPs and ~10% of the [KV cache](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net) size of [DeepSeek V3.2](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+V3?ref=dsebastien.net) at the same context length. Against vanilla full attention the gap is far larger (early reader notes on the paper estimate ~1% of native attention FLOPs and KV size, with throughput improvements on the order of ~50× still to be independently validated). This is an efficiency-first release, not a scale-first one.

- **DeepSeek稀疏注意力（DSA）+ 逐token压缩。** 本次发布的标志性架构创新；一种基于内容的[人工智能稀疏注意力（AI Sparse Attention）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net)变体。在相同上下文长度下，V4-Pro 的单token计算量（FLOPs）约为 DeepSeek V3.2 的27%，所需[键值缓存（KV cache）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net)大小约为其10%。相较标准全注意力机制，这一差距更为显著（论文早期读者笔记估算其原生注意力FLOPs与KV缓存大小仅约为全注意力的1%，吞吐量提升约50倍——该数据尚待独立验证）。这是一次以效率为首要目标的发布，而非以规模为首要目标。

- **KV cache footprint that fits on commodity hardware.** A full 1M-token context fits in roughly 5.7 GB of KV cache at FP8. For comparison, a Llama-3-405B-class native-attention model would need on the order of ~500 GB to hold the same context. That is what makes 1M-token inference economically real, not just paper-feasible; practitioners report running V4-Flash fully in GPU RAM at 1M context on setups that previously had to spill V3.2 into system memory at 256k.

- **适配消费级硬件的KV缓存占用量。** 完整的100万token上下文在FP8精度下仅需约5.7 GB KV缓存空间。作为对比，Llama-3-405B级别、采用原生全注意力机制的模型则需约500 GB才能容纳同等上下文。这使得100万token推理真正具备经济可行性，而不仅停留在论文层面；实践者报告称，此前在256K上下文时就不得不将V3.2的部分缓存溢出至系统内存的设备，如今已能在GPU显存中全程运行V4-Flash的100万token推理。

- **Reasoning is no longer a separate model.** The R series is folded into V4 (see [AI Reasoning Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net)). Both Pro and Flash expose a `reasoning_effort`-style toggle.

- **推理能力不再依赖独立模型。** R系列已整合进V4（参见[人工智能推理模型（AI Reasoning Models）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net)）。Pro与Flash两个版本均提供类似`reasoning_effort`的开关式调节功能。

- **Bitwise batch-invariant, deterministic kernels.** Same input → same output across batch sizes. Most frontier labs trade reproducibility for throughput; DeepSeek deliberately doesn't.

- **位级精确、批处理尺寸无关、确定性的计算核（kernels）。** 相同输入 → 在任意批处理尺寸下均产生完全相同的输出。当前多数前沿实验室为追求吞吐量而牺牲结果可复现性；DeepSeek则明确反其道而行之。

- **API surface compatibility.** Native support for both the OpenAI ChatCompletions and [Anthropic](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Anthropic?ref=dsebastien.net) API formats out of the box, lowering migration friction.

- **API接口兼容性。** 开箱即用原生支持OpenAI ChatCompletions与[Anthropic](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Anthropic?ref=dsebastien.net)两种API格式，大幅降低迁移成本。

## Pricing (per million tokens, input / output)

## 定价（每百万token，输入 / 输出）

| Model | Input | Output |
|-------|--------|---------|
| DeepSeek V4-Flash | $0.14 | $0.28 |
| DeepSeek V4-Pro | $1.74 | $3.48 |
| Claude Opus (ref.) | $5 | $25 |
| GPT-5.5 (ref.) | $5 | $30 |

V4-Pro is the cheapest of the larger frontier models by a wide margin; V4-Flash undercuts even OpenAI's cheapest tier. DeepSeek has signalled further reductions once Huawei Ascend deployment lands in mid-2026.

V4-Pro 是目前所有大型前沿模型中价格最具优势的一款，遥遥领先；V4-Flash 的定价甚至低于 OpenAI 最廉价的档位。DeepSeek 已表示，待华为昇腾（Ascend）平台部署于2026年年中落地后，将进一步下调价格。

## Performance positioning

## 性能定位

V4-Pro rivals top closed-source frontier models and beats all current open models on Math / STEM / Coding benchmarks while preserving stronger world knowledge than other open releases. Independent assessments ([Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net), HN practitioners, PicoCreator's reading notes on the paper) consistently place it "between Sonnet and Opus" in feel; ~3–6 months behind absolute SOTA, close enough that the price gap dominates the decision in most agentic / batch workloads. V4-Flash's reasoning capability is reported to closely approach Pro for a fraction of the cost.

V4-Pro 在性能上可媲美顶尖闭源前沿模型，并在数学 / 理工科 / 编程等基准测试中全面超越所有现有开源模型，同时相比其他开源发布版本保有更扎实的通用世界知识。独立评估（[Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)、Hacker News 实践者、PicoCreator 对论文的阅读笔记）一致认为其实际体验“介于 Sonnet 与 Opus 之间”；整体技术水准约落后当前绝对最先进水平（SOTA）3–6个月，但已足够接近，以至于在绝大多数智能体（agentic）或批量任务中，价格差异成为决策主导因素。据报告，V4-Flash 的推理能力以极小一部分成本即可逼近 V4-Pro 的水平。

**Token-economy caveat.** The headline per-token price is the wrong number on its own. On the Artificial Analysis intelligence index, V4-Pro spends ~190M tokens to complete the suite (and [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) ~170M) versus ~45M for GPT-5.5 (high). The 5–15× per-token advantage shrinks (but does not disappear) once you account for verbosity on hard reasoning tasks; the cheaper-per-token model can occasionally cost roughly the same in dollars on the worst cases. The current discount on the official DeepSeek API also makes early comparisons rosier than the steady-state pricing will be; the open-weights release means alternative hosts ([OpenRouter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net), Fireworks, etc.) can fill the gap when official capacity is throttled.

**关于“token经济性”的重要提醒。** 单纯看每token标价是误导性的。在 Artificial Analysis 智能指数测试套件中，V4-Pro 需消耗约1.9亿token（[Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net) 约1.7亿），而 GPT-5.5（高估情形）仅需约4500万。若考虑复杂推理任务中固有的冗长输出（verbosity）问题，原本5–15倍的单token成本优势会收窄（但并未消失）；在最差情况下，单token更便宜的模型有时实际美元支出可能几乎相当。此外，当前 DeepSeek 官方API提供的折扣，也使早期对比显得比长期稳定定价更为乐观；而开源权重的发布，意味着当官方服务能力受限时，第三方托管平台（如[OpenRouter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net)、Fireworks等）可有效填补供给缺口。

## Why this matters

## 为何这至关重要

DeepSeek v4 is the clearest signal yet that the frontier is bifurcating along a cost / quality plane rather than a single capability axis. A 6-month-behind, 5-to-15× cheaper open model is the right tool for almost everything that isn't the absolute hardest reasoning step. The DSA + KV-cache reduction also makes ultra-long-context inference economically realistic, not just technically possible — the [AI Inference](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net) cost curve just shifted.

DeepSeek v4 是迄今最清晰的信号：AI 前沿正沿着“成本/质量”二维平面发生分化，而非沿单一能力轴线演进。一款技术水准落后约6个月、但成本仅为当前主流方案5–15分之一的开源模型，已是除“绝对最难推理步骤”外几乎所有任务的理想选择。DSA 架构与 KV 缓存缩减技术，亦使超长上下文推理真正具备经济可行性，而不仅停留于技术可能性层面——[AI 推理（AI Inference）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)的成本曲线已然发生实质性偏移。

Early practitioner reports back this up. A non-trivial TypeScript codebase audit (multi-file traversal, type analysis, refactor proposal across two prompts) ran end-to-end on V4-Pro for $0.09; the same task is reported to have cost on the order of $9–$13 on Claude Opus before recent price hikes. A full day of refactor work (many subagents, thousands of changed lines) totalled under $1. The cost ratio collapses on the workloads where verbosity bites (see token caveat above), but on the long tail of "good enough" engineering work it is roughly two orders of magnitude.

早期实践者报告印证了这一点。一次颇具规模的 TypeScript 代码库审计（涉及多文件遍历、类型分析、跨两个提示生成重构建议）在 V4-Pro 上端到端完成仅耗资0.09美元；而据报告，同一任务在近期调价前于 Claude Opus 上执行需花费约9–13美元。一整天的重构工作（含多个子智能体协同、数千行代码修改）总成本亦低于1美元。当然，在冗长输出问题突出的工作负载中（参见前述“token经济性”提醒），成本比值会显著收窄；但在海量“够用就好（good enough）”的工程类任务长尾中，成本差距仍达约两个数量级。

The real constraint, on day one, is operational: V4-Pro is hit hard with timeouts and rate limits at launch (including via [OpenRouter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net) at peak hours), so V4-Flash, or a third-party host, is the more reliable choice for iterative agent loops until capacity catches up.

上线首日真正的制约因素在于运维层面：V4-Pro 在发布初期遭遇严重超时与速率限制（包括在高峰时段通过[OpenRouter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net)调用时），因此在算力容量充分释放前，V4-Flash 或第三方托管服务才是迭代式智能体循环（iterative agent loops）更可靠的选择。

## References

## 参考资料

- Official announcement: [https://api-docs.deepseek.com/news/news260424](https://api-docs.deepseek.com/news/news260424)
- Announcement post (X): [https://x.com/deepseek_ai/status/2047516922263285776](https://x.com/deepseek_ai/status/2047516922263285776)
- Model collection: [https://huggingface.co/collections/deepseek-ai/deepseek-v4](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
- Technical report: [https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf)
- Simon Willison's writeup: [https://simonwillison.net/2026/Apr/24/deepseek-v4/](https://simonwillison.net/2026/Apr/24/deepseek-v4/)
- PicoCreator's raw reading notes on the V4 paper (X): [https://x.com/picocreator/status/2047625988125954386](https://x.com/picocreator/status/2047625988125954386)
- Hacker News, launch-day discussions: [https://news.ycombinator.com/item?id=47884971](https://news.ycombinator.com/item?id=47884971) and [https://news.ycombinator.com/item?id=47885014](https://news.ycombinator.com/item?id=47885014)
- Hacker News, V4 in practice (cost, token economy, local deployment): [https://news.ycombinator.com/item?id=47977026](https://news.ycombinator.com/item?id=47977026)
- Artificial Analysis pages: [https://artificialanalysis.ai/models/deepseek-v4-pro](https://artificialanalysis.ai/models/deepseek-v4-pro) and [https://artificialanalysis.ai/models/deepseek-v4-flash](https://artificialanalysis.ai/models/deepseek-v4-flash)

## Related

## 相关主题

- [Deepseek](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Deepseek?ref=dsebastien.net)
- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)
- [AI Mixture of Experts (MoE)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)
- [AI Open Weight Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)
- [AI KV Cache](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net)
- [AI Inference](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)
- [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)
- [Sparse AI Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net)
- [Dense AI Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dense+AI+Models?ref=dsebastien.net)
- [Chain-of-Thought (CoT) prompting](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Chain-of-Thought+(CoT)+prompting?ref=dsebastien.net)
- [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)
- [Claude](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude?ref=dsebastien.net)
- [ChatGPT](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/ChatGPT?ref=dsebastien.net)
- [Anthropic](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Anthropic?ref=dsebastien.net)
- [OpenAI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net)
- [Mistral Small 4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Mistral+Small+4?ref=dsebastien.net)
- [Kimi K2.6](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net)
- [GPT-5](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GPT-5?ref=dsebastien.net)
- [OpenRouter](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net)
- [OpenCode](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenCode?ref=dsebastien.net)
- [Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)
