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
> OpenAI发布了开源、Apache 2.0许可的轻量级隐私过滤模型Privacy Filter，专用于高效检测和掩码文本中的八类PII（如姓名、邮箱、电话等），适用于高吞吐数据脱敏场景。该模型采用单次前向传播+约束Viterbi解码，支持精度/召回率调节，具备小参数量（50M）、长上下文（128k）和可微调等优势，便于本地部署与领域适配。尽管填补了OpenAI少有开源权重的空白，并提升了自托管隐私防护能力，但它不构成合规保证，且在非英语、非拉丁语系及罕见命名场景下性能下降，高敏感场景仍需人工复核。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI+Privacy+Filter?ref=dsebastien.net"><em>OpenAI Privacy Filter</em></a><em>.</em></p><p>OpenAI Privacy Filter is an open-weight, <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0</a>-licensed token-classification model published by <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a> on <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">HuggingFace</a> for <strong>detecting and masking personally identifiable information (PII) in text</strong>. It is designed for high-throughput data sanitization workflows: feeding LLMs, redacting datasets, on-prem privacy filtering. It is <em>not</em> a compliance guarantee &#x2014; it is one layer in a broader privacy-by-design stack.</p><p>This is a notable release because OpenAI rarely ships open weights, and because privacy filtering is one of the highest-leverage things to add in front of any <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">LLM</a> pipeline that touches user data &#x2014; particularly for anyone running BYOK or local inference setups (see <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)</a>).</p><h2 id="specs">Specs</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Detail</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Developer</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></td>
</tr>
<tr>
<td><strong>License</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 License</a> (permissive)</td>
</tr>
<tr>
<td><strong>Total params</strong></td>
<td>1.5B</td>
</tr>
<tr>
<td><strong>Active params</strong></td>
<td>50M (sparse <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">MoE</a>, 128 experts, top-4)</td>
</tr>
<tr>
<td><strong>Architecture</strong></td>
<td>8 transformer blocks, grouped-query attention, sparse MoE, single-pass</td>
</tr>
<tr>
<td><strong>Context window</strong></td>
<td>128k tokens</td>
</tr>
<tr>
<td><strong>Decoding</strong></td>
<td>Constrained Viterbi over BIOES span labels</td>
</tr>
<tr>
<td><strong>Distribution</strong></td>
<td>HuggingFace (<code>openai/privacy-filter</code>), runs via <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a> or Transformers.js (browser)</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<h2 id="what-it-detects">What it detects</h2><p>Eight PII span categories:</p><ol><li>Account number</li><li>Private address</li><li>Private email</li><li>Private person (name)</li><li>Private phone</li><li>Private URL</li><li>Private date</li><li>Secret</li></ol><p>The model labels all tokens in a single pass (not autoregressive), then runs constrained Viterbi to produce coherent BIOES spans. A runtime threshold tunes the precision/recall tradeoff per use case.</p><h2 id="why-it-matters">Why it matters</h2><ul><li><strong>Open weights from OpenAI is rare.</strong> It also lowers the bar for self-hosted, on-prem privacy filtering.</li><li><strong>Right place in the stack.</strong> PII detection belongs in front of any third-party LLM call, especially for cloud AI APIs that retain inputs by default. See the four data paths in <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)</a>.</li><li><strong>Small, efficient.</strong> 50M active params + 128k context means it can sit in front of a request without dominating latency or cost.</li><li><strong>Fine-tunable.</strong> Domains with their own privacy taxonomies (medical, legal, HR) can extend the label set.</li></ul><h2 id="limitations">Limitations</h2><ul><li>Not a compliance guarantee &#x2014; should be <strong>one layer</strong> in a broader privacy-by-design approach.</li><li>Performance drops on non-English text, non-Latin scripts, and underrepresented naming patterns.</li><li>Failure modes include under-detection of uncommon names and over-redaction of public entities.</li><li>High-sensitivity settings (medical, legal, financial, HR) still require human review.</li></ul><h2 id="use-cases">Use cases</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Use case</th>
<th>How the filter fits</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Pre-prompt sanitization</strong></td>
<td>Strip PII before sending prompts to a third-party LLM API</td>
</tr>
<tr>
<td><strong>Dataset cleaning</strong></td>
<td>Redact PII from training, fine-tuning, or analytics datasets</td>
</tr>
<tr>
<td><strong>On-prem privacy gateway</strong></td>
<td>Filter inbound/outbound text in a self-hosted AI pipeline</td>
</tr>
<tr>
<td><strong>Browser-side filtering</strong></td>
<td>Run via Transformers.js to redact before data ever leaves the device</td>
</tr>
<tr>
<td><strong>Custom redaction policies</strong></td>
<td>Fine-tune for domain-specific PII (medical IDs, legal refs)</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<h2 id="references">References</h2><ul><li><a href="https://huggingface.co/openai/privacy-filter?ref=dsebastien.net">https://huggingface.co/openai/privacy-filter</a></li></ul><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net">AI Privacy</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">Where Your AI Prompts Really Go - A Practical Guide to AI Privacy (Article)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">HuggingFace</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 License</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">AI Mixture of Experts (MoE)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">Large Language Models (LLMs)</a></li></ul>

## 中文译文

这是我的公开笔记中的一则记录。查看权威版本：OpenAI 隐私过滤器（OpenAI Privacy Filter）。

OpenAI 隐私过滤器是一款开源权重、采用 Apache 2.0 许可协议的词元分类模型，由 OpenAI 发布于 Hugging Face 平台，用于检测并屏蔽文本中的个人身份信息（PII）。该模型专为高吞吐量的数据脱敏工作流而设计，适用于向大语言模型（LLM）供入数据、数据集脱敏处理，以及本地部署环境下的隐私过滤。需注意：它**不构成合规性保证**，而仅是“以隐私为本的设计”（privacy-by-design）整体架构中的一环。

此次发布意义重大，原因有二：其一，OpenAI 极少公开发布模型权重；其二，隐私过滤是任何涉及用户数据的 LLM 流程前端最具杠杆效应的安全增强措施之一——尤其对采用自带密钥（BYOK）或本地推理架构的用户而言（参见文章《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》）。

规格说明

可检测的 PII 类型

共八类 PII 文本片段：

- 账户号码  
- 私人地址  
- 私人邮箱  
- 私人姓名（自然人）  
- 私人电话号码  
- 私人网址（URL）  
- 私人日期  
- 密钥/密文等机密信息  

该模型以单次前向传播完成全部词元标注（非自回归式），随后通过带约束的维特比算法（constrained Viterbi）生成连贯的 BIOES 标注序列。运行时可通过阈值调节，按具体应用场景灵活平衡精确率与召回率。

为何重要？

- OpenAI 发布开源权重极为罕见，此举显著降低了用户自托管、本地化部署隐私过滤能力的技术门槛。  
- 定位精准：PII 检测理应置于所有第三方 LLM 调用之前，尤其针对默认保留输入内容的云 AI API。详见《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》一文中所列的四类数据流向。  
- 体积小、效率高：仅含 5000 万活跃参数，支持 128K 上下文长度，可无缝嵌入请求处理链路前端，不会显著增加延迟或成本。  
- 支持微调：医疗、法律、人力资源等垂直领域若已有专属隐私分类体系，可扩展标签集合以适配其特定需求。

局限性

- **不提供合规性保证**：应作为更全面的“以隐私为本的设计”方案中的一环使用。  
- 在非英语文本、非拉丁字母文字系统，以及代表性不足的姓名模式上，性能明显下降。  
- 常见失效情形包括：对生僻姓名漏检，或对公共实体（如知名机构名）误判为敏感信息而过度脱敏。  
- 在高敏感度场景（如医疗、法律、金融、人力资源）中，仍须辅以人工复核。

适用场景

参考资料

https://huggingface.co/openai/privacy-filter

相关主题

- OpenAI  
- 人工智能隐私（AI Privacy）  
- 《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）  
- Hugging Face  
- Apache 2.0 许可协议  
- Transformers 库  
- 人工智能混合专家模型（MoE）  
- 大语言模型（LLMs）
