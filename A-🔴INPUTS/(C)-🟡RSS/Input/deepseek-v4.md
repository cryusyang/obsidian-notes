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
> DeepSeek于2026年4月24日发布第四代旗舰模型V4，包含两个开源权重变体：V4-Pro（1.6万亿总参数/490亿激活参数）和V4-Flash（2840亿总参数/130亿激活参数），均采用MoE架构，原生支持100万token上下文窗口，并将原先独立的R系列推理模型整合进统一模型，支持可切换的“思考/非思考”模式。核心创新是DeepSeek稀疏注意力（DSA）与逐token压缩技术，大幅降低计算开销——V4-Pro相较V3.2仅需27%单token算力和10% KV缓存，在FP8精度下100万token上下文仅需约5.7GB显存，首次实现百万级上下文在消费级硬件上的经济可行推理。模型还具备确定性内核、多API格式原生兼容及极具竞争力的定价，V4-Pro为当前最大开源模型且性价比最优，V4-Flash则以极低成本逼近Pro级推理能力；独立评测显示其综合性能介于Claude Sonnet与Opus之间，数学/STEM/编程能力超越所有现有开源模型，略落后于闭源SOTA但价格优势显著。

---

<p><em>本文摘自我公开的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>笔记库</em></a><em>。查看权威原文版本：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net"><em>DeepSeek v4</em></a><em>。</em></p>

<p>这是 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Deepseek?ref=dsebastien.net">DeepSeek</a> 推出的第四代旗舰模型（发布于 2026 年 4 月 24 日）。包含两个开源权重变体——V4-Pro（总参数量 1.6 万亿 / 激活参数 490 亿）与 V4-Flash（总参数量 2840 亿 / 激活参数 130 亿），二者均基于 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">混合专家（MoE）</a> 架构；默认搭载 100 万 token 的 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">上下文窗口</a>；并将原先独立的 R 系列推理模型整合进单一模型，支持在“思考模式”与“非思考模式”之间动态切换。</p>

<p>V4-Pro 是迄今发布的参数规模最大、完全开源权重的模型。</p>

## 实际上有哪些新特性？

- **DeepSeek 稀疏注意力（DSA） + 逐 token 压缩**：核心架构创新，是 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Sparse+Attention?ref=dsebastien.net">AI 稀疏注意力</a> 的一种基于内容的变体。在相同上下文长度下，V4-Pro 相较于 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+V3?ref=dsebastien.net">DeepSeek V3.2</a>，单 token 计算所需 FLOPs 约降低 73%，<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net">KV 缓存</a> 占用空间约减少 90%。相较于标准全注意力机制，性能优势更为显著（早期论文阅读笔记估算其 FLOPs 和 KV 缓存大小仅为原生全注意力的约 1%，吞吐量提升可达约 50 倍，但该数据尚待独立验证）。这是一次以效率为优先、而非单纯追求规模的发布。

- **KV 缓存占用可适配消费级硬件**：在 FP8 精度下，完整 100 万 token 上下文仅需约 5.7 GB KV 缓存。作为对比，Llama-3-405B 这类采用原生全注意力机制的模型，要容纳同等上下文则需约 500 GB 缓存。正因如此，100 万 token 的推理才真正具备经济可行性，而不仅停留在论文层面；实践者报告称，V4-Flash 可在先前连 V3.2 都需将 256k 上下文溢出至系统内存的设备上，全程运行于 GPU 显存中完成 100 万 token 推理。

- **推理能力不再依赖独立模型**：R 系列模型已完全整合进 V4（参见 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net">AI 推理模型</a>）。V4-Pro 与 V4-Flash 均提供类似 `reasoning_effort` 的开关式控制选项。

- **位级批处理无关、确定性内核**：同一输入在不同 batch size 下始终产生完全一致的输出。当前多数前沿实验室为换取吞吐量而牺牲结果可复现性；DeepSeek 则刻意反其道而行之。

- **API 接口兼容性**：开箱即支持 OpenAI ChatCompletions 与 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Anthropic?ref=dsebastien.net">Anthropic</a> 两种主流 API 格式，大幅降低迁移成本。

## 定价（每百万 token，输入 / 输出）

| 模型 | 输入 | 输出 |
|------|------|------|
| DeepSeek V4-Flash | $0.14 | $0.28 |
| DeepSeek V4-Pro | $1.74 | $3.48 |
| Claude Opus（参考） | $5 | $25 |
| GPT-5.5（参考） | $5 | $30 |

V4-Pro 是目前所有大型前沿模型中价格最低的，领先幅度巨大；V4-Flash 甚至低于 OpenAI 最便宜的档位。DeepSeek 已表示，待华为昇腾（Ascend）平台部署于 2026 年年中落地后，将进一步下调价格。

## 性能定位

V4-Pro 在性能上可媲美顶级闭源前沿模型，并在数学 / STEM / 编程等基准测试中全面超越所有现有开源模型，同时保留比其他开源模型更强的世界知识。独立评估（<a href="https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net">Simon Willison</a>、Hacker News 实践者、PicoCreator 对论文的阅读笔记）普遍认为其实际体验“介于 Sonnet 与 Opus 之间”；技术先进性约落后于绝对最前沿（SOTA）3–6 个月，但价格差距之大，足以在绝大多数智能体（agentic）或批量任务中成为主导性决策因素。V4-Flash 的推理能力据报亦极为接近 V4-Pro，却仅需后者一小部分成本。

**关于 Token 经济性的提醒**：单 token 标价本身并非决定性指标。在 Artificial Analysis 智能指数测试套件中，V4-Pro 完成全部评测需消耗约 1.9 亿 tokens（<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net">Kimi K2.6</a> 约 1.7 亿），而 GPT-5.5（高分档）仅需约 4500 万。这意味着原本高达 5–15 倍的单 token 成本优势，在考虑复杂推理任务中固有的冗长输出（verbosity）后会明显收窄（但并未消失）；在最不利场景下，单 token 更便宜的模型有时实际美元花费可能相差无几。此外，DeepSeek 官方 API 当前的折扣价也使初期对比显得比长期稳定定价更乐观；而开源权重的发布意味着第三方托管平台（如 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net">OpenRouter</a>、Fireworks 等）可在官方容量受限时及时填补缺口。

## 为何此事意义重大

DeepSeek v4 是迄今最清晰的信号：AI 前沿正沿着“成本 / 质量”二维平面发生分化，而非单一能力轴线上的线性演进。一款技术上落后约半年、但成本低至 5–15 倍的开源模型，恰恰是绝大多数非极致难度推理任务的理想工具。DSA 架构与 KV 缓存缩减技术，更使得超长上下文推理从纯技术可行，跃升为真正具备经济可行性的现实选择——<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">AI 推理</a> 的成本曲线已然重塑。

早期实践者报告印证了这一点：一次非平凡的 TypeScript 代码库审计任务（含多文件遍历、类型分析、跨两轮提示的重构建议）在 V4-Pro 上端到端执行仅耗资 $0.09；而同类任务在近期调价前，使用 Claude Opus 的成本约为 $9–$13。一整天的重构工作（含多个子智能体、数千行代码变更）总成本亦低于 $1。当然，在 verbosity 成为主要负担的工作负载中（见前述 token 提醒），成本比率会显著坍缩；但在大量“足够好”的工程任务长尾中，成本差距仍达约两个数量级。

上线首日真正的瓶颈在于运维层面：V4-Pro 在发布初期遭遇严重超时与速率限制（包括高峰时段通过 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net">OpenRouter</a> 的访问），因此对需高频迭代的智能体循环而言，V4-Flash 或第三方托管服务仍是更可靠的选择，直至整体服务能力跟上需求。

## 参考资料

- 官方公告：<a href="https://api-docs.deepseek.com/news/news260424?ref=dsebastien.net">https://api-docs.deepseek.com/news/news260424</a>
- X 平台公告帖：<a href="https://x.com/deepseek_ai/status/2047516922263285776?ref=dsebastien.net">https://x.com/deepseek_ai/status/2047516922263285776</a>
- 模型合集（Hugging Face）：<a href="https://huggingface.co/collections/deepseek-ai/deepseek-v4?ref=dsebastien.net">https://huggingface.co/collections/deepseek-ai/deepseek-v4</a>
- 技术报告：<a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf?ref=dsebastien.net">https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf</a>
- Simon Willison 的解读：<a href="https://simonwillison.net/2026/Apr/24/deepseek-v4/">https://simonwillison.net/2026/Apr/24/deepseek-v4/</a>
- PicoCreator 对 V4 论文的原始阅读笔记（X）：<a href="https://x.com/picocreator/status/2047625988125954386?ref=dsebastien.net">https://x.com/picocreator/status/2047625988125954386</a>
- Hacker News 发布日讨论：<a href="https://news.ycombinator.com/item?id=47884971&amp;ref=dsebastien.net">https://news.ycombinator.com/item?id=47884971</a> 与 <a href="https://news.ycombinator.com/item?id=47885014&amp;ref=dsebastien.net">https://news.ycombinator.com/item?id=47885014</a>
- Hacker News 关于 V4 实际应用（成本、token 经济性、本地部署）：<a href="https://news.ycombinator.com/item?id=47977026&amp;ref=dsebastien.net">https://news.ycombinator.com/item?id=47977026</a>
- Artificial Analysis 页面：<a href="https://artificialanalysis.ai/models/deepseek-v4-pro?ref=dsebastien.net">https://artificialanalysis.ai/models/deepseek-v4-pro</a> 与 <a href="https://artificialanalysis.ai/models/deepseek-v4-flash?ref=dsebastien.net">https://artificialanalysis.ai/models/deepseek-v4-flash</a>

## 相关主题

- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Deepseek?ref=dsebastien.net">Deepseek</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大型语言模型（LLMs）</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">AI 混合专家（MoE）</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net">AI 开源权重模型</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+KV+Cache?ref=dsebastien.net">AI KV 缓存</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">AI 推理</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net">上下文窗口</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Sparse+AI+Models?ref=dsebastien.net">稀疏 AI 模型</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Dense+AI+Models?ref=dsebastien.net">稠密 AI 模型</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Chain-of-Thought+(CoT)+prompting?ref=dsebastien.net">思维链（CoT）提示</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">HuggingFace</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude?ref=dsebastien.net">Claude</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/ChatGPT?ref=dsebastien.net">ChatGPT</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Anthropic?ref=dsebastien.net">Anthropic</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Mistral+Small+4?ref=dsebastien.net">Mistral Small 4</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net">Kimi K2.6</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GPT-5?ref=dsebastien.net">GPT-5</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenRouter?ref=dsebastien.net">OpenRouter</a>
- <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenCode?ref=dsebastien.net">OpenCode</a>
- <a href="https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net">Simon Willison</a>
