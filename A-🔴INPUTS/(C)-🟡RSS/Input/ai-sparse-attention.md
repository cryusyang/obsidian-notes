---
title: "AI Sparse Attention"
url: "https://www.dsebastien.net/ai-sparse-attention/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了稀疏注意力（Sparse Attention）机制，它通过仅计算部分token对之间的交互来突破传统Transformer中O(n²)的计算复杂度瓶颈。稀疏注意力分为三类：基于固定模式（如滑动窗口、块对角）、基于内容学习（如路由、LSH、DSA）以及近似/线性化方法（如Performer、Linformer），分别在效率与建模能力间权衡。该技术显著降低训练和推理时的计算量与KV缓存内存占用，使百万级上下文窗口具备经济可行性，并常与MoE等其他稀疏技术协同使用以进一步提升效率。但其局限在于可能丢失关键长程依赖信息，影响内容敏感型长距离任务的表现。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [AI Sparse Attention](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[AI 稀疏注意力（Sparse Attention）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net)。

A family of [attention](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net) mechanisms that compute interactions between only a subset of token pairs instead of every pair, breaking the O(n²) cost of full self-attention. The dense attention used in vanilla [Transformers](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net) forces every token to attend to every other token; sparse attention restricts that interaction graph by structure (fixed patterns) or by content (learned routing), trading a small drop in modelling power for very large gains in speed and memory.

一类[注意力（attention）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net)机制，仅计算部分词元（token）对之间的交互，而非全部词元对，从而突破完整自注意力（full self-attention）的 O(n²) 计算复杂度。标准[Transformer](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net)中使用的稠密注意力强制每个词元关注所有其他词元；而稀疏注意力则通过结构（固定模式）或内容（学习式路由）限制该交互图，以建模能力的微小下降为代价，换取速度与内存占用的极大提升。

Sparse attention is the architectural move that makes million-token [context windows](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net) economically viable — both at training time (FLOPs) and at inference time ([KV cache](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net) size).

稀疏注意力是一项架构层面的关键改进，使百万级词元的[上下文窗口（context window）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)在经济上真正可行——无论是在训练阶段（FLOPs 消耗），还是推理阶段（[KV 缓存（KV cache）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net)大小）。

## Why it matters

## 为何重要

Full attention scales O(n²) in compute and O(n) in KV cache per layer. At a 1M-token context, those costs dominate everything else. Sparse attention attacks both axes:

完整注意力的计算复杂度为每层 O(n²)，KV 缓存空间开销为每层 O(n)。当上下文长度达 100 万词元时，这两项开销将压倒其余所有成本。稀疏注意力同时针对这两个维度进行优化：

- **Compute**: each token attends to k ≪ n neighbours, so per-layer cost drops from O(n²) toward O(n·k) or O(n·log n).  
- **Memory**: only the kept keys/values need to live in the cache; in some schemes the cache itself is compressed.

- **计算**：每个词元仅关注 k ≪ n 个邻居词元，因此单层计算成本从 O(n²) 下降至接近 O(n·k) 或 O(n·log n)。  
- **内存**：仅需将被保留的键（key）与值（value）存入缓存；在某些方案中，缓存本身还可进一步压缩。

The trade-off is information loss when the dropped pairs would have mattered. The whole design space is "which pairs can I safely skip?"

其权衡在于：当被跳过的词元对本应承载关键信息时，会造成信息损失。“哪些词元对可以安全跳过？”——这正是整个稀疏注意力设计空间的核心问题。

## Three families

## 三大类别

- **Pattern-based (fixed sparsity)**. Each token attends to a deterministic subset: sliding window (Longformer), local + global landmarks (BigBird), strided / dilated (Sparse Transformer), block-diagonal. Cheap and predictable but blind to content.  
- **Content-based (learned sparsity)**. The model learns which pairs matter. Routing transformers cluster tokens; Reformer uses LSH; Native Sparse Attention and DeepSeek Sparse Attention (DSA, see [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)) compress and route at the token level. More expensive logic per layer, but far better quality at the same sparsity ratio.  
- **Approximated / linearised attention**. Performer, Linformer, and Linear Attention rewrite the softmax so attention becomes O(n) via kernel approximation or low-rank projection. Technically not "sparse" but pursues the same goal — drop the quadratic — through a different door.

- **基于模式（固定稀疏性）**：每个词元关注一个确定性的子集，例如滑动窗口（Longformer）、局部+全局地标（BigBird）、跨步/膨胀采样（Sparse Transformer）、分块对角线结构。成本低廉、行为可预测，但对内容不敏感。  
- **基于内容（学习式稀疏性）**：模型自主学习哪些词元对真正重要。路由型 Transformer 对词元聚类；Reformer 使用局部敏感哈希（LSH）；原生稀疏注意力（Native Sparse Attention）与 DeepSeek 稀疏注意力（DSA，参见[DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)）则在词元粒度上执行压缩与路由。每层逻辑开销更高，但在相同稀疏率下质量显著更优。  
- **近似化 / 线性化注意力**：Performer、Linformer 和线性注意力（Linear Attention）通过核函数近似或低秩投影重写 softmax 运算，使注意力计算复杂度降为 O(n)。严格来说并非“稀疏”，但目标一致——消除二次方复杂度——只是选择了另一条技术路径。

## Relationship to MoE

## 与 MoE 的关系

Sparse attention and [MoE](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net) are both forms of [sparsity](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net) but operate on different axes. MoE is sparse in the **parameter** dimension: only a few experts fire per token. Sparse attention is sparse in the **sequence** dimension: only a few token pairs interact per layer. Modern frontier open models (DeepSeek v4, Native Sparse Attention models, Kimi K2) stack the two — sparse experts plus sparse attention — to compound the efficiency gains.

稀疏注意力与[混合专家（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)同属[稀疏性（sparsity）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net)的不同实现形式，但作用于不同维度：MoE 在**参数**维度上稀疏——每个词元仅激活少数专家；稀疏注意力则在**序列**维度上稀疏——每层仅有少量词元对发生交互。当前前沿开源大模型（如 DeepSeek v4、原生稀疏注意力模型、Kimi K2）将二者叠加使用——稀疏专家 + 稀疏注意力——以叠加式放大效率增益。

## What this unlocks

## 这一技术解锁的能力

- Million-token contexts that were technically supported but economically impractical.  
- Long-context [inference](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net) on smaller deployments, because the KV cache stops dominating GPU memory.  
- Better cost / quality positioning for [open-weights models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net) vs closed frontier APIs — most of DeepSeek v4's price advantage traces back to DSA.

- 原本在技术上已支持、却因成本过高而无法落地的百万词元上下文。  
- 在资源受限的部署环境中实现长上下文[推理（inference）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)，因为 KV 缓存不再主导 GPU 显存占用。  
- 提升[开源权重模型（open-weights models）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)相较闭源前沿 API 的性价比——DeepSeek v4 的大部分价格优势正源于其 DSA（DeepSeek Sparse Attention）技术。

## Limitations

## 局限性

- Quality on long-range, content-dependent tasks (multi-hop retrieval over a 500K-token context) can lag full attention; benchmarks like RULER and InfiniteBench expose this.  
- Pattern-based schemes underperform when the structure is wrong for the data.  
- Content-based schemes add training complexity and can be hard to load-balance, similar to MoE routing failure modes.

- 在长程、依赖内容的任务（例如在 50 万词元上下文中执行多跳检索）上，性能可能落后于完整注意力；RULER 和 InfiniteBench 等基准测试可暴露此类短板。  
- 当预设结构与数据特性不匹配时，基于模式的方案表现欠佳。  
- 基于内容的方案会增加训练复杂度，且负载均衡难度较大，类似于 MoE 中的路由失效问题。

## References

## 参考文献

  

## Related

## 相关主题

- [AI Attention](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net)  
- [Transformers](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net)  
- [AI KV Cache](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net)  
- [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [AI Mixture of Experts (MoE)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)  
- [Sparse AI Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net)  
- [Dense AI Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dense+AI+Models?ref=dsebastien.net)  
- [AI Inference](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)  
- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  
- [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)
