---
title: "Qwen3.6-27B"
url: "https://www.dsebastien.net/qwen3-6-27b/"
source: "Sebastien Dubois"
date: 2026-05-01
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Qwen3.6-27B是阿里云推出的270亿参数稠密型原生多模态大模型，于2026年4月22日开源，专为单块高端消费级GPU部署设计。它在各项代理式编程基准测试中全面超越前代397B总参数/17B激活参数的MoE模型（如Qwen3.5-397B-A17B），体积仅为其约1/14，且支持128K原生上下文与文本、图像、视频统一理解。该模型采用纯稠密架构，避免MoE路由复杂性，Q4_K_M量化后仅16.8GB，可在24GB显存GPU或最新Apple Silicon设备上高效运行，实现本地化旗舰级编程代理能力。

---

This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Qwen3.6-27B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-27B?ref=dsebastien.net).

这是我来自[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则记录。查看权威版本：[Qwen3.6-27B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-27B?ref=dsebastien.net)。

Qwen3.6-27B is a **dense, natively multimodal** 27B-parameter open-weight [LLM](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net) from the [Qwen](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen?ref=dsebastien.net) family (Alibaba Cloud), released on 2026-04-22. It targets the "flagship-quality model that fits on a single high-end consumer GPU" slot in the lineup, sitting alongside the smaller MoE [Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net) and the API-only Qwen3.6-Plus / Qwen3.6-Max-Preview. The headline result: it surpasses the previous-generation MoE flagship Qwen3.5-397B-A17B (397B total / 17B active) on every major agentic coding benchmark while being ~14× smaller on disk.

Qwen3.6-27B 是阿里巴巴云旗下 [Qwen](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen?ref=dsebastien.net) 系列推出的 **稠密型、原生多模态** 大语言模型（LLM），参数量为 270 亿，权重开源。该模型于 2026 年 4 月 22 日发布，定位为“可在单块高端消费级 GPU 上运行的旗舰级模型”，在产品线中与更小的 MoE 模型 [Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net) 及仅提供 API 接口的 Qwen3.6-Plus / Qwen3.6-Max-Preview 并列。其最引人注目的成果是：在所有主流智能体编程（agentic coding）基准测试中全面超越上一代 MoE 旗舰模型 Qwen3.5-397B-A17B（总参数量 3970 亿 / 每次激活 170 亿），同时磁盘占用体积缩小约 14 倍。

## Architecture

## 架构

- Dense 27B-parameter transformer (not [MoE](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)). Every parameter is active per token, unlike the 35B-A3B sibling.

- 稠密型 270 亿参数 Transformer 架构（非 [MoE](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)）。每个 token 均激活全部参数，不同于其 MoE 同胞模型 35B-A3B。

- **Natively multimodal**: single unified checkpoint that handles text, images, and video; supports vision-language reasoning, document understanding, and VQA.

- **原生多模态**：单一统一检查点，可同时处理文本、图像与视频；支持视觉-语言联合推理、文档理解及视觉问答（VQA）。

- Switchable thinking and non-thinking modes (in line with the convergence pattern documented in [AI Reasoning Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net)); supports the `preserve_thinking` feature for keeping reasoning traces across turns in agentic tasks.

- 可切换的“思考模式”与“非思考模式”（符合 [AI 推理模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net) 中记载的收敛趋势）；支持 `preserve_thinking` 功能，可在智能体任务的多轮交互中保留推理过程痕迹。

- Native [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net): 128k (131,072 tokens) per the official deployment configs; benchmark runs go up to 256k context.

- 原生 [上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)：依据官方部署配置为 128K（即 131,072 个 token）；基准测试中可扩展至 256K 上下文长度。

- Default max output: 16,384 tokens.

- 默认最大输出长度：16,384 个 token。

- Open weights, distributed via [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net) and ModelScope.

- 权重开源，通过 [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net) 和 ModelScope 分发。

## Why it matters

## 其重要性何在？

- **Compression of the frontier into 27B dense.** Beats the 397B-total / 17B-active predecessor on *every* major agentic coding benchmark, at ~55.6 GB vs 807 GB on disk per [Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)'s comparison.

- **将前沿能力压缩进 270 亿稠密模型**。据 [Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net) 的对比数据，其在 *所有* 主流智能体编程基准测试中均超越总参数量 3970 亿 / 激活 170 亿的前代模型，磁盘占用仅为约 55.6 GB，远低于前代的 807 GB。

- **No MoE routing complexity.** Dense architecture is straightforward to deploy and serve with any standard inference stack; no expert-routing tuning, no auxiliary balancing, no host-memory choreography.

- **无 MoE 路由复杂性**。稠密架构可直接使用任意标准推理栈进行部署与服务；无需专家路由调优、无需辅助负载均衡、无需主机内存协调调度。

- **Local agentic coding becomes practical.** The Q4_K_M quantization is 16.8 GB, small enough to run on a single 24 GB consumer GPU or recent Apple Silicon, while still delivering "flagship-level agentic coding performance" per Simon's testing.

- **本地智能体编程真正可行**。经 Q4_K_M 量化后模型体积仅 16.8 GB，足以在单块 24 GB 显存的消费级 GPU 或最新款 Apple Silicon 芯片上运行，且仍能提供 Simon 测试所验证的“旗舰级智能体编程性能”。

- **Dense vs MoE tradeoff revisited.** HN discussion noted that dense models like 27B suffer more context-length degradation past 32–64k tokens than MoE variants of similar quality. The 27B is the right pick when you want maximum quality per active parameter on short-to-medium contexts; the 35B-A3B sibling is the right pick when active-compute budget matters more.

- **稠密模型与 MoE 的权衡再审视**。Hacker News 讨论指出，类似 27B 的稠密模型在上下文长度超过 32–64K token 后，性能衰减程度高于同质量 MoE 变体。当您追求短至中等上下文（short-to-medium contexts）下每个激活参数所能提供的最高质量时，27B 是更优选择；而当活跃计算预算（active-compute budget）更为关键时，则应选用 35B-A3B 同胞模型。

## Official benchmarks

## 官方基准测试结果

From the Qwen team's release post (vs Qwen3.5-27B, Qwen3.5-397B-A17B, [Gemma4-31B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net), Claude 4.5 Opus, [Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net)):

Qwen 团队发布帖中的数据（对比对象：Qwen3.5-27B、Qwen3.5-397B-A17B、[Gemma4-31B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net)、Claude 4.5 Opus、[Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net)）：

**Coding agent (where it wins decisively)**

**编程智能体（其优势极为显著）**

- SWE-bench Verified: **77.2** (vs 76.2 for the 397B predecessor)  
- SWE-bench Verified：**77.2**（前代 397B 模型为 76.2）

- SWE-bench Pro: **53.5** (vs 50.9)  
- SWE-bench Pro：**53.5**（前代为 50.9）

- SWE-bench Multilingual: **71.3** (vs 69.3)  
- SWE-bench 多语言版：**71.3**（前代为 69.3）

- Terminal-Bench 2.0: **59.3** (vs 52.5; ties Claude 4.5 Opus)  
- Terminal-Bench 2.0：**59.3**（前代为 52.5；与 Claude 4.5 Opus 并列）

- SkillsBench Avg5: **48.2** (vs 30.0; the largest jump in the table)  
- SkillsBench Avg5：**48.2**（前代为 30.0；为表中提升幅度最大者）

- NL2Repo: 36.2; QwenWebBench: 1487 (Elo)  
- NL2Repo：36.2；QwenWebBench：1487（Elo 分数）

- Claw-Eval Pass^3: **60.6** (highest in the table, beats Claude 4.5 Opus 59.6)  
- Claw-Eval Pass^3：**60.6**（表中最高分，超越 Claude 4.5 Opus 的 59.6）

**STEM and reasoning**

**STEM 与推理能力**

- GPQA Diamond: 87.8  
- GPQA Diamond：87.8

- AIME26: 94.1  
- AIME26：94.1

- HMMT Feb 25 / Nov 25 / Feb 26: 93.8 / 90.7 / 84.3  
- HMMT 2025 年 2 月 / 2025 年 11 月 / 2026 年 2 月：93.8 / 90.7 / 84.3

- LiveCodeBench v6: 83.9  
- LiveCodeBench v6：83.9

- IMOAnswerBench: 80.8  
- IMOAnswerBench：80.8

- HLE: 24.0  
- HLE：24.0

**Knowledge**

**知识能力**

- MMLU-Pro: 86.2; MMLU-Redux: 93.5; SuperGPQA: 66.0; C-Eval: 91.4  
- MMLU-Pro：86.2；MMLU-Redux：93.5；SuperGPQA：66.0；C-Eval：91.4

**Vision-language**

**视觉-语言能力**

- MMMU: 82.9; MMMU-Pro: 75.8; MathVista mini: 87.4; DynaMath: 85.6; VlmsAreBlind: 97.0  
- MMMU：82.9；MMMU-Pro：75.8；MathVista mini：87.4；DynaMath：85.6；VlmsAreBlind：97.0

- RealWorldQA: 84.1; MMStar: 81.4; MMBench EN-DEV-v1.1: 92.3  
- RealWorldQA：84.1；MMStar：81.4；MMBench EN-DEV-v1.1：92.3

The general pattern: Qwen3.6-27B leads or ties dense peers and the 397B MoE predecessor on agentic coding, stays close to Claude 4.5 Opus on coding while trailing it on knowledge/HLE-style hard reasoning.

总体趋势：Qwen3.6-27B 在智能体编程任务上领先或持平于其他稠密模型及 397B MoE 前代模型；编程能力接近 Claude 4.5 Opus，但在知识类与 HLE 风格的高难度推理任务上略逊一筹。

## Local performance ([Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)'s measurements)

## 本地性能（[Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net) 实测数据）

Tested with the Q4_K_M Unsloth quant via `llama-server` (`llama.cpp`), reasoning mode on, 65,536-token context:

使用 `llama-server`（基于 `llama.cpp`）配合 Q4_K_M Unsloth 量化，在启用推理模式、上下文长度为 65,536 token 条件下测试：

- Reading: 54.32 tokens/s  
- 读取（prefill）速度：54.32 token/s

- Generation: ~25 tokens/s  
- 生成（decode）速度：约 25 token/s

Other reported numbers from HN:

Hacker News 上报告的其他数据：

- RTX 5090 at Q6_K, 123k context: ~50 tokens/s.  
- RTX 5090，Q6_K 量化，123K 上下文：约 50 token/s。

- M-series Macs at 8-bit quantization: 8–11 tokens/s.  
- M 系列 Mac，8-bit 量化：8–11 token/s。

Q4_K_M shows ~1–3% perplexity increase versus full precision while halving memory; widely treated as the default sweet spot for this model.

Q4_K_M 相比全精度仅带来约 1–3% 的困惑度（perplexity）上升，同时将显存占用减半；被广泛视为该模型的默认最佳量化方案。

## Quantization landscape

## 量化方案全景

- Q4_K_M (~16.8 GB): default sweet spot, minimal quality loss.  
- Q4_K_M（约 16.8 GB）：默认最佳方案，质量损失极小。

- Q6_K: noticeably better quality, fits in 24 GB cards with reduced context.  
- Q6_K：质量明显更优，可在 24 GB 显卡上运行（需缩减上下文长度）。

- Q8_0: near-full quality for quality-critical workloads.  
- Q8_0：适用于对质量要求严苛的任务，接近全精度表现。

- 3-bit variants: viable for severely memory-constrained setups, with measurable quality loss.  
- 3-bit 变体：适用于内存极度受限的环境，但存在可衡量的质量损失。

## Deployment

## 部署方式

- **Self-hosting**: weights on Hugging Face and ModelScope; runs on `llama.cpp`, vLLM, LM Studio, Ollama, etc.  
- **自托管**：权重已发布于 Hugging Face 与 ModelScope；兼容 `llama.cpp`、vLLM、LM Studio、Ollama 等主流推理框架。

- **Hosted API**: Alibaba Cloud Model Studio (DashScope endpoints in Beijing / Singapore / US-Virginia).  
- **托管 API**：阿里云模型平台（DashScope，节点位于北京 / 新加坡 / 美国弗吉尼亚州）。

- **API protocols**: OpenAI-compatible chat completions, plus an Anthropic-compatible endpoint at `https://dashscope-intl.aliyuncs.com/apps/anthropic`.  
- **API 协议**：兼容 OpenAI 的聊天补全接口，另提供 Anthropic 兼容端点：`https://dashscope-intl.aliyuncs.com/apps/anthropic`。

- **Coding-agent integrations**: OpenClaw (formerly Moltbot/Clawdbot), [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net) (via the Anthropic protocol; set `ANTHROPIC_MODEL=qwen3.6-27b`), Qwen Code (`@qwen-code/qwen-code` npm package).  
- **编程智能体集成**：OpenClaw（原 Moltbot/Clawdbot）、[Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)（通过 Anthropic 协议；设置 `ANTHROPIC_MODEL=qwen3.6-27b`）、Qwen Code（npm 包 `@qwen-code/qwen-code`）。

- **Try interactively**: Qwen Studio.  
- **交互式体验**：Qwen Studio。

## Reception and caveats

## 社区反响与注意事项

- Simon Willison calls the local results "an outstanding result for a 16.8GB local model", validated through the recurring SVG-generation tests (pelican on a bicycle, opossum on an e-scooter) where the model produced both technically correct and creatively detailed output.  
- Simon Willison 称其本地运行效果为“一款 16.8GB 本地模型所取得的卓越成果”，该结论已通过反复进行的 SVG 生成测试（如“骑自行车的鹈鹕”、“骑电动滑板车的负鼠”）得到验证——模型输出既技术准确，又富有创意细节。

- Hacker News discussion flagged two concerns worth keeping in mind:  
- Hacker News 讨论中指出了两个值得关注的问题：

  - **Goodhart on viral benchmarks.** The "pelican on a bicycle" test has become well-known enough that frontier models may now be implicitly tuned for it; treat single-prompt vibe checks as anecdotes, not evidence.  
  - **病毒式基准测试的古德哈特定律陷阱**。“骑自行车的鹈鹕”测试已广为人知，前沿模型可能已被隐式调优以适配该测试；请将单提示词的氛围检验（vibe check）视作轶事佐证，而非确凿证据。

  - **Context decay.** Dense 27B models degrade past 32–64k tokens more than MoE variants; for very-long-context work, prefer MoE-based options like [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net) or the 35B-A3B sibling.  
  - **上下文衰减**。稠密型 27B 模型在上下文长度超过 32–64K token 后，性能下降幅度大于同质量 MoE 变体；对于超长上下文任务，建议优先选用基于 MoE 的方案，例如 [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net) 或 35B-A3B 同胞模型。

- Compared favorably to [Gemma 4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net) (Gemma4-31B) on coding tasks (e.g., 77.2 vs 52.0 on SWE-bench Verified), with the usual caveat about training-set leakage on coding benchmarks.  
- 在编程任务上显著优于 [Gemma 4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net)（Gemma4-31B）（例如 SWE-bench Verified 得分：77.2 对比 52.0），但需注意编程类基准测试普遍存在训练集泄露（training-set leakage）这一常规局限。

- One HN tester reported it competitive with [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net) (a much larger model) on certain tasks, "1/88 the size".  
- 一位 Hacker News 测试者报告称，该模型在某些任务上可与更大得多的 [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net) 模型相媲美，而体积仅为后者的“1/88”。

## When to reach for it

## 何时选用该模型？

- Local agentic coding on a single 24 GB GPU or M-series Mac.  
- 在单块 24 GB 显存 GPU 或 M 系列 Mac 上运行本地智能体编程任务。

- Multimodal workloads (image/video reasoning, document understanding) where you need a dense model rather than running a separate VLM.  
- 多模态任务（图像/视频推理、文档理解），当您需要一个统一的稠密模型，而非分别部署专用视觉语言模型（VLM）时。

- Drop-in upgrade from Qwen3.5-397B-A17B for coding agents — same family, smaller, faster, better benchmarks.  
- 编程智能体从 Qwen3.5-397B-A17B 的即插即用升级方案——同属 Qwen 家族，体积更小、运行更快、基准测试更优。

- Short-to-medium context tasks (under ~32k tokens) where dense-model behavior is preferred.  
- 短至中等上下文长度任务（约 <32K token），且偏好稠密模型行为特性时。

- Use the 35B-A3B sibling instead when active-compute efficiency matters; use V4-class MoE models for very long contexts.  
- 若活跃计算效率（active-compute efficiency）更为关键，请改用 35B-A3B 同胞模型；若需处理超长上下文，请选用 DeepSeek v4 级别的 MoE 模型。

## References

## 参考资料

- Official announcement: [https://qwen.ai/blog?id=qwen3.6-27b](https://qwen.ai/blog?id=qwen3.6-27b)  
- 官方公告：[https://qwen.ai/blog?id=qwen3.6-27b](https://qwen.ai/blog?id=qwen3.6-27b)

- Simon Willison's write-up: [https://simonwillison.net/2026/Apr/22/qwen36-27b/](https://simonwillison.net/2026/Apr/22/qwen36-27b/)  
- Simon Willison 的深度解析：[https://simonwillison.net/2026/Apr/22/qwen36-27b/](https://simonwillison.net/2026/Apr/22/qwen36-27b/)

- Hacker News discussion: [https://news.ycombinator.com/item?id=47863217](https://news.ycombinator.com/item?id=47863217)  
- Hacker News 讨论：[https://news.ycombinator.com/item?id=47863217](https://news.ycombinator.com/item?id=47863217)

- Qwen on HuggingFace: [https://huggingface.co/Qwen](https://huggingface.co/Qwen)  
- Qwen 在 HuggingFace：[https://huggingface.co/Qwen](https://huggingface.co/Qwen)

- ModelScope: [https://www.modelscope.cn/organization/qwen](https://www.modelscope.cn/organization/qwen)  
- ModelScope：[https://www.modelscope.cn/organization/qwen](https://www.modelscope.cn/organization/qwen)

## Related

## 相关内容

- [Qwen](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen?ref=dsebastien.net)  
- [Qwen](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen?ref=dsebastien.net)

- [Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net)  
- [Qwen3.6-35B-A3B](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Qwen3.6-35B-A3B?ref=dsebastien.net)

- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  
- [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)

- [AI Open Weight Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)  
- [AI 开源权重模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net)

- [AI Mixture of Experts (MoE)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)  
- [AI 混合专家（MoE）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net)

- [AI Reasoning Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net)  
- [AI 推理模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Reasoning+Models?ref=dsebastien.net)

- [Context Window](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)  
- [上下文窗口](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Context+Window?ref=dsebastien.net)

- [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)  
- [HuggingFace](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net)

- [Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)  
- [Simon Willison](https://notes.dsebastien.net/30+Areas/36+People/Simon+Willison?ref=dsebastien.net)

- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)  
- [Claude Code](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Code?ref=dsebastien.net)

- [Claude Opus 4.7](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Opus+4.7?ref=dsebastien.net)  
- [Claude Opus 4.7](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Claude+Opus+4.7?ref=dsebastien.net)

- [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)  
- [DeepSeek v4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net)

- [Gemma 4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net)  
- [Gemma 4](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemma+4?ref=dsebastien.net)

- [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net)  
- [GLM-5.1](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net)
