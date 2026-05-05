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
> 本文介绍了稀疏注意力（Sparse Attention）机制，它通过仅计算部分token对之间的交互，突破了传统Transformer中全连接自注意力O(n²)的计算与内存瓶颈。稀疏注意力分为三类：基于固定模式（如滑动窗口、局部+全局）、基于内容学习（如Routing Transformer、Reformer、DeepSeek DSA）以及近似/线性化方法（如Performer、Linformer），分别在效率、质量与实现复杂度上权衡。该技术与MoE（专家混合）协同使用，可显著降低百万级token上下文的训练与推理成本，提升开源模型的经济可行性与部署灵活性，但可能在长程、强依赖内容的任务上存在性能损失。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net"><em>AI Sparse Attention</em></a><em>.</em></p><p>A family of <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net">attention</a> mechanisms that compute interactions between only a subset of token pairs instead of every pair, breaking the O(n&#xb2;) cost of full self-attention. The dense attention used in vanilla <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a> forces every token to attend to every other token; sparse attention restricts that interaction graph by structure (fixed patterns) or by content (learned routing), trading a small drop in modelling power for very large gains in speed and memory.</p><p>Sparse attention is the architectural move that makes million-token <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">context windows</a> economically viable &#x2014; both at training time (FLOPs) and at inference time (<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net">KV cache</a> size).</p><h2 id="why-it-matters">Why it matters</h2><p>Full attention scales O(n&#xb2;) in compute and O(n) in KV cache per layer. At a 1M-token context, those costs dominate everything else. Sparse attention attacks both axes:</p><ul><li><strong>Compute</strong>: each token attends to k &#x226a; n neighbours, so per-layer cost drops from O(n&#xb2;) toward O(n&#xb7;k) or O(n&#xb7;log n).</li><li><strong>Memory</strong>: only the kept keys/values need to live in the cache; in some schemes the cache itself is compressed.</li></ul><p>The trade-off is information loss when the dropped pairs would have mattered. The whole design space is &quot;which pairs can I safely skip?&quot;</p><h2 id="three-families">Three families</h2><ul><li><strong>Pattern-based (fixed sparsity)</strong>. Each token attends to a deterministic subset: sliding window (Longformer), local + global landmarks (BigBird), strided / dilated (Sparse Transformer), block-diagonal. Cheap and predictable but blind to content.</li><li><strong>Content-based (learned sparsity)</strong>. The model learns which pairs matter. Routing transformers cluster tokens; Reformer uses LSH; Native Sparse Attention and DeepSeek Sparse Attention (DSA, see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net">DeepSeek v4</a>) compress and route at the token level. More expensive logic per layer, but far better quality at the same sparsity ratio.</li><li><strong>Approximated / linearised attention</strong>. Performer, Linformer, and Linear Attention rewrite the softmax so attention becomes O(n) via kernel approximation or low-rank projection. Technically not &quot;sparse&quot; but pursues the same goal &#x2014; drop the quadratic &#x2014; through a different door.</li></ul><h2 id="relationship-to-moe">Relationship to MoE</h2><p>Sparse attention and <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">MoE</a> are both forms of <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net">sparsity</a> but operate on different axes. MoE is sparse in the <strong>parameter</strong> dimension: only a few experts fire per token. Sparse attention is sparse in the <strong>sequence</strong> dimension: only a few token pairs interact per layer. Modern frontier open models (DeepSeek v4, Native Sparse Attention models, Kimi K2) stack the two &#x2014; sparse experts plus sparse attention &#x2014; to compound the efficiency gains.</p><h2 id="what-this-unlocks">What this unlocks</h2><ul><li>Million-token contexts that were technically supported but economically impractical.</li><li>Long-context <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">inference</a> on smaller deployments, because the KV cache stops dominating GPU memory.</li><li>Better cost / quality positioning for <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net">open-weights models</a> vs closed frontier APIs &#x2014; most of DeepSeek v4&apos;s price advantage traces back to DSA.</li></ul><h2 id="limitations">Limitations</h2><ul><li>Quality on long-range, content-dependent tasks (multi-hop retrieval over a 500K-token context) can lag full attention; benchmarks like RULER and InfiniteBench expose this.</li><li>Pattern-based schemes underperform when the structure is wrong for the data.</li><li>Content-based schemes add training complexity and can be hard to load-balance, similar to MoE routing failure modes.</li></ul><h2 id="references">References</h2><ul><li></li></ul><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Attention?ref=dsebastien.net">AI Attention</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net">AI KV Cache</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">Context Window</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">AI Mixture of Experts (MoE)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net">Sparse AI Models</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dense+AI+Models?ref=dsebastien.net">Dense AI Models</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">AI Inference</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">Large Language Models (LLMs)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net">DeepSeek v4</a></li></ul>

## 中文译文

这是我的公开笔记中的一则记录。查看权威版本：《AI 稀疏注意力》。

一类注意力机制，仅计算部分词元对之间的交互，而非全部词元对，从而突破全量自注意力的 O(n²) 计算复杂度。标准 Transformer 中所用的稠密注意力强制每个词元都需关注其他所有词元；而稀疏注意力则通过结构化方式（固定模式）或内容驱动方式（学习路由）限制该交互图谱，在建模能力上仅承受小幅下降，却换来速度与内存占用上的巨大提升。

稀疏注意力这一架构选择，使得百万级词元上下文窗口在训练（FLOPs）和推理（KV 缓存大小）两方面均具备经济可行性。

为何重要？

全量注意力的计算开销为 O(n²)，每层 KV 缓存占用为 O(n)。当上下文长度达 100 万词元时，这两项开销将远超其余所有成本。稀疏注意力同时优化这两个维度：

计算：每个词元仅关注 k ≪ n 个邻近词元，因此单层计算成本从 O(n²) 下降至接近 O(n·k) 或 O(n·log n)。

内存：仅需将被保留的键（Key）与值（Value）存入缓存；某些方案甚至进一步压缩缓存本身。

其权衡在于：当被舍弃的词元对本应具有信息价值时，会造成信息损失。整个设计空间的核心问题即：“哪些词元对可以安全跳过？”

三大类别

基于模式的稀疏（固定稀疏度）：每个词元关注一个确定性子集，例如滑动窗口（Longformer）、局部+全局地标点（BigBird）、跨步/膨胀采样（Sparse Transformer）、分块对角线结构。成本低、可预测性强，但对输入内容无感知。

基于内容的稀疏（学习型稀疏度）：模型自主学习哪些词元对真正重要。路由式 Transformer 对词元进行聚类；Reformer 使用局部敏感哈希（LSH）；原生稀疏注意力（Native Sparse Attention）与 DeepSeek 稀疏注意力（DSA，参见 DeepSeek v4）则在词元粒度上执行压缩与路由。每层逻辑开销更高，但在同等稀疏率下质量显著更优。

近似/线性化注意力：Performer、Linformer 和线性注意力（Linear Attention）通过核函数近似或低秩投影等方式重写 softmax，使注意力计算复杂度降为 O(n)。严格而言并非“稀疏”，但目标一致——消除平方级增长——只是经由另一条技术路径实现。

与 MoE 的关系

稀疏注意力与混合专家（MoE）同属“稀疏性”范畴，但作用于不同维度：MoE 在参数维度稀疏——每个词元仅激活少数几个专家；稀疏注意力则在序列维度稀疏——每层仅允许少量词元对发生交互。当前主流开源前沿模型（如 DeepSeek v4、原生稀疏注意力模型、Kimi K2）将二者叠加使用——既采用稀疏专家，又采用稀疏注意力——以复利式放大效率增益。

由此解锁的能力

此前虽在技术上支持、却因成本过高而难以落地的百万级词元上下文。

更小规模部署下的长上下文推理能力，因为 KV 缓存不再主导 GPU 内存占用。

开源权重模型相较于闭源前沿 API 在“成本/质量”定位上的优势——DeepSeek v4 的大部分价格优势正源于其 DSA 技术。

局限性

在长程、强内容依赖型任务（例如在 50 万词元上下文中进行多跳检索）上，性能可能落后于全量注意力；RULER 和 InfiniteBench 等基准测试可清晰暴露此类差距。

当预设模式与实际数据结构不匹配时，基于模式的方案表现会明显下降。

基于内容的方案增加了训练复杂度，且负载均衡难度较高，其路由失败模式与 MoE 类似。

参考文献

相关主题

AI 注意力机制  
Transformer  
AI KV 缓存  
上下文窗口  
AI 混合专家（MoE）  
稀疏 AI 模型  
稠密 AI 模型  
AI 推理  
大语言模型（LLM）  
DeepSeek v4
