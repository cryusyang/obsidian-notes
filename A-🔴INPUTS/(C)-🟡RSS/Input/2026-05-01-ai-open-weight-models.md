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
> 本文介绍了“开放权重（open-weight）AI模型”的概念，即公开发布训练后模型权重、允许自由下载、运行、微调和部署的AI模型，强调其比“开源”更准确，因通常不包含训练代码或数据。文中列举了多个主流开放权重模型系列，如Llama、Mistral、Gemma、Qwen、Phi、DeepSeek v4（当前最大，1.6万亿总参数）、GLM-5.1、Kimi K2系列及Granite等。这类模型有助于推动AI民主化、支持本地/私有化部署、降低厂商锁定风险，并促进社区协作微调；但也带来安全挑战，因权重一旦发布便无法撤回，增加了滥用风险。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Open+Weight+Models?ref=dsebastien.net"><em>AI Open Weight Models</em></a><em>.</em></p><p>AI models whose trained weights are publicly released, allowing anyone to download, run, fine-tune, and deploy them. &quot;Open weight&quot; is more precise than &quot;open source&quot; because most releases don&apos;t include training code or data.</p><p>Key families: Llama (Meta), Mistral/Mixtral (Mistral AI), Gemma (<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Google+DeepMind?ref=dsebastien.net">Google DeepMind</a>), Qwen (Alibaba), Phi (Microsoft), DeepSeek (see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/DeepSeek+v4?ref=dsebastien.net">DeepSeek v4</a> &#x2014; currently the largest open-weights model at 1.6T total / 49B active params), <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/GLM-5.1?ref=dsebastien.net">GLM-5.1</a> (<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net">Zhipu AI (Z.ai)</a>), Kimi K2 (<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net">Moonshot AI</a>, see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.6?ref=dsebastien.net">Kimi K2.6</a> and <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net">Kimi K2.5</a>), <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite+4.1?ref=dsebastien.net">Granite</a> (IBM &#x2014; dense, enterprise-targeted, <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0</a>).</p><p>Significance: democratizes AI access, enables local/private deployment, reduces vendor lock-in, enables community fine-tuning. Tension with safety: open weights can&apos;t be un-released, making misuse harder to prevent.</p><h2 id="open-weight-model-notes">Open-weight model notes</h2><p>Auto-populated from notes carrying <code>ai/open_weight</code>. Tag a note rather than editing this list to add a model.</p><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/News/2026-04-21+Kimi+K2.6,+Qwen,+and+Gemma+4+-+Local+AI+Is+Catching+Up?ref=dsebastien.net">2026-04-21 Kimi K2.6, Qwen, and Gemma 4 - Local AI Is Catching Up</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Baichuan?ref=dsebastien.net">Baichuan</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Granite?ref=dsebastien.net">Granite</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hermes?ref=dsebastien.net">Hermes</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi?ref=dsebastien.net">Kimi</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Kimi+K2.5?ref=dsebastien.net">Kimi K2.5</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Moonshot+AI?ref=dsebastien.net">Moonshot AI</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Nous+Research?ref=dsebastien.net">Nous Research</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Stability+AI?ref=dsebastien.net">Stability AI</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Zhipu+AI+(Z.ai)?ref=dsebastien.net">Zhipu AI (Z.ai)</a></li></ul><h2 id="references">References</h2><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">Large Language Models (LLMs)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Knowledge+Distillation?ref=dsebastien.net">Knowledge Distillation</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Low+Rank+Adapter+(LoRA)?ref=dsebastien.net">Low Rank Adapter (LoRA)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Atropos?ref=dsebastien.net">Atropos</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Tinker?ref=dsebastien.net">Tinker</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Axolotl?ref=dsebastien.net">Axolotl</a></li></ul>

## 中文译文

这是我的公开笔记中的一则备注。查看权威版本：AI 开源权重模型。

指那些已将训练完成的模型权重公开发布的 AI 模型，允许任何人下载、运行、微调和部署。“开源权重”（open weight）比“开源”（open source）更为准确，因为绝大多数发布版本并不包含训练代码或训练数据。

主要模型系列：Llama（Meta）、Mistral / Mixtral（Mistral AI）、Gemma（Google DeepMind）、Qwen（阿里巴巴）、Phi（微软）、DeepSeek（参见 DeepSeek v4——当前参数量最大的开源权重模型，总参数达 1.6 万亿，激活参数为 490 亿）、GLM-5.1（智谱 AI（Z.ai））、Kimi K2（月之暗面 AI，参见 Kimi K2.6 和 Kimi K2.5）、Granite（IBM——稠密架构、面向企业应用、采用 Apache 2.0 许可证）。

重要意义：推动 AI 技术普惠化，支持本地化/私有化部署，降低厂商锁定风险，并赋能社区开展模型微调。但与安全目标存在张力：一旦权重公开便无法撤回，使得潜在滥用行为更难防范。

开源权重模型备注

本列表由标注了 ai/open_weight 标签的笔记自动填充生成。如需新增模型，请为对应笔记添加标签，而非直接编辑本列表。

2026 年 4 月 21 日：Kimi K2.6、Qwen 与 Gemma 4 —— 本地 AI 正在迎头赶上

百川  
Granite  
Hermes  
Kimi  
Kimi K2.5  
月之暗面 AI（Moonshot AI）  
Nous Research  
Stability AI  
智谱 AI（Z.ai）

参考文献  
相关主题  
大语言模型（LLMs）  
知识蒸馏（Knowledge Distillation）  
低秩适配器（LoRA）  
Atropos  
Tinker  
Axolotl
