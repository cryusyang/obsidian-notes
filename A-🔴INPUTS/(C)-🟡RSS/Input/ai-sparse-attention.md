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
> 本文介绍了稀疏注意力（Sparse Attention）机制，它通过仅计算部分token对之间的交互，突破了传统Transformer中全连接自注意力O(n²)的计算复杂度瓶颈。稀疏注意力分为三类：基于固定模式（如滑动窗口、局部+全局）、基于内容学习（如LSH、路由聚类、DSA）以及近似/线性化方法（如Performer、Linformer），分别在效率、质量与实现路径上做出权衡。该技术显著降低训练和推理时的计算量与KV缓存内存占用，使百万级上下文窗口在经济与工程层面真正可行，并常与MoE等其他稀疏技术协同使用以进一步提升效率。但其局限在于可能丢失关键长程依赖信息，影响内容敏感型长程任务的表现。

---

<em>这是来自我的 </em>[<em>公开笔记</em>](https://notes.dsebastien.net/?ref=dsebastien.net)<em> 的一则笔记。查看权威版本：</em>[<em>AI 稀疏注意力</em>](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net)<em>。</em>

这是一种**注意力机制家族**，仅计算部分词元对（token pairs）之间的交互，而非全部词元对，从而打破全量自注意力（full self-attention）的 O(n²) 计算复杂度。标准 **Transformer** 中所用的稠密注意力强制每个词元关注所有其他词元；而稀疏注意力则通过**结构化方式**（如固定模式）或**内容驱动方式**（如学习路由）限制该交互图谱，在建模能力上仅承受微小损失，却换来极显著的速度与内存开销下降。

稀疏注意力是使百万级词元的**上下文窗口**在经济上可行的关键架构演进——无论是在训练阶段（FLOPs 消耗），还是在推理阶段（**KV 缓存**大小）。

## 为何重要

全量注意力的计算复杂度为 O(n²)，每层 KV 缓存空间复杂度为 O(n)。当上下文长度达 100 万词元时，这两项开销将完全主导整个系统。稀疏注意力同时优化这两个维度：

- **计算开销**：每个词元仅关注 k ≪ n 个邻近词元，因此单层计算成本从 O(n²) 下降至接近 O(n·k) 或 O(n·log n)；
- **内存开销**：仅需在缓存中保留被选中的键（key）与值（value）；某些方案甚至会对缓存本身进行压缩。

其权衡在于：被跳过的词元对若本应重要，则会造成信息损失。整个设计空间的核心问题即是：“**哪些词元对可以安全地跳过？**”

## 三大类别

- **基于模式的稀疏（固定稀疏度）**：每个词元以确定性方式关注某一子集，例如滑动窗口（Longformer）、局部+全局地标（BigBird）、步幅/扩张采样（Sparse Transformer）、分块对角线结构。成本低、可预测性强，但对内容不敏感；
- **基于内容的稀疏（学习型稀疏度）**：模型自主学习哪些词元对真正重要。例如：Routing Transformer 对词元聚类；Reformer 使用局部敏感哈希（LSH）；Native Sparse Attention 与 DeepSeek 稀疏注意力（DSA，参见 [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)）在词元粒度上实现压缩与路由。每层逻辑开销更高，但在相同稀疏率下质量远优于模式型方案；
- **近似化 / 线性化注意力**：Performer、Linformer 和 Linear Attention 通过对 softmax 进行核函数近似或低秩投影，将注意力计算重写为 O(n)。严格意义上并非“稀疏”，但目标一致——绕过二次方瓶颈，只是选择了另一条技术路径。

## 与 MoE 的关系

稀疏注意力与 **MoE（专家混合）** 同属 **稀疏 AI 模型** 的范畴，但作用于不同维度：  
MoE 在 **参数维度** 上稀疏——每个词元仅激活少数几个专家；  
稀疏注意力则在 **序列维度** 上稀疏——每层仅允许少数词元对发生交互。  
当前前沿开源大模型（如 DeepSeek v4、Native Sparse Attention 模型、Kimi K2）正将二者叠加使用——既稀疏化专家，又稀疏化注意力——以复利式放大效率增益。

## 这一技术解锁的能力

- 百万级词元上下文窗口——此前虽在技术上支持，却因成本过高而难以实用；
- 小规模部署即可支撑长上下文 **AI 推理**，因为 KV 缓存不再占据压倒性 GPU 显存；
- **开源权重模型** 相较闭源前沿 API 实现更优的“成本 / 质量”定位——DeepSeek v4 的大部分价格优势，根源即在于 DSA（DeepSeek 稀疏注意力）。

## 局限性

- 在长程、强内容依赖型任务（例如在 50 万词元上下文中进行多跳检索）上的表现可能落后于全量注意力；RULER 和 InfiniteBench 等基准测试可暴露此类差距；
- 若预设的模式结构与实际数据分布不匹配，基于模式的方案性能将明显下降；
- 基于内容的方案会增加训练复杂度，且负载均衡难度较高，类似于 MoE 中路由失败的典型问题。

## 参考文献

-  

## 相关主题

- [AI 注意力](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net)  
- [Transformer](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net)  
- [AI KV 缓存](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net)  
- [上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [AI 专家混合（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)  
- [稀疏 AI 模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net)  
- [稠密 AI 模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dense+AI+Models?ref=dsebastien.net)  
- [AI 推理](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)  
- [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  
- [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)
