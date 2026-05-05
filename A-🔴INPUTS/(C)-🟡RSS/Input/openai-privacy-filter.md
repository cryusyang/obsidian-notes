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

<p><em>这是来自我的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>公开笔记</em></a><em> 的一则记录。查看权威版本：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI+Privacy+Filter?ref=dsebastien.net"><em>OpenAI 隐私过滤器</em></a><em>。</em></p>

<p><em>这是来自我的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>公开笔记</em></a><em> 的一则记录。查看权威版本：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI+Privacy+Filter?ref=dsebastien.net"><em>OpenAI 隐私过滤器</em></a><em>。</em></p>

<p>OpenAI 隐私过滤器（OpenAI Privacy Filter）是一款开源权重、采用 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a> 授权的 token 分类模型，由 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a> 发布于 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">Hugging Face</a> 平台，专用于<strong>检测并遮蔽文本中的个人身份信息（PII）</strong>。该模型面向高吞吐量的数据脱敏工作流而设计，例如：为大语言模型（LLM）提供输入数据、对数据集进行脱敏处理、以及在本地部署环境中实施隐私过滤。它<strong>并非合规性保证</strong>——而是“以隐私为本的设计”（privacy-by-design）整体架构中的一环。</p>

<p>OpenAI 隐私过滤器（OpenAI Privacy Filter）是一款开源权重、采用 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a> 授权的 token 分类模型，由 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a> 发布于 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">Hugging Face</a> 平台，专用于<strong>检测并遮蔽文本中的个人身份信息（PII）</strong>。该模型面向高吞吐量的数据脱敏工作流而设计，例如：为大语言模型（LLM）提供输入数据、对数据集进行脱敏处理、以及在本地部署环境中实施隐私过滤。它<strong>并非合规性保证</strong>——而是“以隐私为本的设计”（privacy-by-design）整体架构中的一环。</p>

<p>此次发布意义重大，原因有二：其一，OpenAI 极少开源其模型权重；其二，隐私过滤是任何触及用户数据的 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLM）</a> 流程前端最具杠杆效应的增强措施之一——尤其适用于采用“自带密钥”（BYOK）或本地推理架构的用户（参见：<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a>）。</p>

<p>此次发布意义重大，原因有二：其一，OpenAI 极少开源其模型权重；其二，隐私过滤是任何触及用户数据的 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLM）</a> 流程前端最具杠杆效应的增强措施之一——尤其适用于采用“自带密钥”（BYOK）或本地推理架构的用户（参见：<a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a>）。</p>

<h2 id="specs">技术规格</h2>

<h2 id="specs">技术规格</h2>

<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>方面</th>
<th>详情</th>
</tr>
</thead>
<tbody><tr>
<td><strong>开发者</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></td>
</tr>
<tr>
<td><strong>许可协议</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a>（宽松型）</td>
</tr>
<tr>
<td><strong>总参数量</strong></td>
<td>15 亿（1.5B）</td>
</tr>
<tr>
<td><strong>活跃参数量</strong></td>
<td>5000 万（50M）（稀疏型 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">专家混合模型（MoE）</a>，含 128 个专家，每次激活 Top-4）</td>
</tr>
<tr>
<td><strong>架构</strong></td>
<td>8 层 Transformer 块、分组查询注意力（grouped-query attention）、稀疏 MoE、单次前向传播（single-pass）</td>
</tr>
<tr>
<td><strong>上下文窗口</strong></td>
<td>128K tokens</td>
</tr>
<tr>
<td><strong>解码方式</strong></td>
<td>基于 BIOES 标注体系的约束维特比算法（Constrained Viterbi）</td>
</tr>
<tr>
<td><strong>分发渠道</strong></td>
<td>Hugging Face（模型 ID：<code>openai/privacy-filter</code>），可通过 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a> 库或 Transformers.js（浏览器端）运行</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->

<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>方面</th>
<th>详情</th>
</tr>
</thead>
<tbody><tr>
<td><strong>开发者</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></td>
</tr>
<tr>
<td><strong>许可协议</strong></td>
<td><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a>（宽松型）</td>
</tr>
<tr>
<td><strong>总参数量</strong></td>
<td>15 亿（1.5B）</td>
</tr>
<tr>
<td><strong>活跃参数量</strong></td>
<td>5000 万（50M）（稀疏型 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">专家混合模型（MoE）</a>，含 128 个专家，每次激活 Top-4）</td>
</tr>
<tr>
<td><strong>架构</strong></td>
<td>8 层 Transformer 块、分组查询注意力（grouped-query attention）、稀疏 MoE、单次前向传播（single-pass）</td>
</tr>
<tr>
<td><strong>上下文窗口</strong></td>
<td>128K tokens</td>
</tr>
<tr>
<td><strong>解码方式</strong></td>
<td>基于 BIOES 标注体系的约束维特比算法（Constrained Viterbi）</td>
</tr>
<tr>
<td><strong>分发渠道</strong></td>
<td>Hugging Face（模型 ID：<code>openai/privacy-filter</code>），可通过 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a> 库或 Transformers.js（浏览器端）运行</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->

<h2 id="what-it-detects">检测范围</h2>

<h2 id="what-it-detects">检测范围</h2>

<p>共支持八类 PII 实体跨度（span）识别：</p>

<p>共支持八类 PII 实体跨度（span）识别：</p>

<ol><li>账户号码</li><li>私人住址</li><li>私人邮箱</li><li>私人姓名（自然人）</li><li>私人电话</li><li>私人网址（URL）</li><li>私人日期</li><li>密钥/口令等秘密信息</li></ol>

<ol><li>账户号码</li><li>私人住址</li><li>私人邮箱</li><li>私人姓名（自然人）</li><li>私人电话</li><li>私人网址（URL）</li><li>私人日期</li><li>密钥/口令等秘密信息</li></ol>

<p>该模型以单次前向传播方式对全部 token 进行标注（非自回归式），随后运行约束维特比算法，生成语义连贯的 BIOES 标注跨度。运行时可通过阈值调节，按具体应用场景灵活平衡精确率与召回率。</p>

<p>该模型以单次前向传播方式对全部 token 进行标注（非自回归式），随后运行约束维特比算法，生成语义连贯的 BIOES 标注跨度。运行时可通过阈值调节，按具体应用场景灵活平衡精确率与召回率。</p>

<h2 id="why-it-matters">重要意义</h2>

<h2 id="why-it-matters">重要意义</h2>

<ul><li><strong>OpenAI 开源权重极为罕见。</strong> 此举也显著降低了自托管及本地化隐私过滤的技术门槛。</li><li><strong>部署位置恰到好处。</strong> PII 检测理应置于任何第三方大语言模型调用之前，尤其适用于默认保留用户输入的云 AI API。详见 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a> 中所列的四条数据路径。</li><li><strong>轻量高效。</strong> 仅 5000 万活跃参数 + 128K 上下文窗口，使其可无缝嵌入请求链路前端，而不会显著增加延迟或计算成本。</li><li><strong>支持微调。</strong> 医疗、法律、人力资源等垂直领域可基于自身隐私分类体系，扩展模型标签集合。</li></ul>

<ul><li><strong>OpenAI 开源权重极为罕见。</strong> 此举也显著降低了自托管及本地化隐私过滤的技术门槛。</li><li><strong>部署位置恰到好处。</strong> PII 检测理应置于任何第三方大语言模型调用之前，尤其适用于默认保留用户输入的云 AI API。详见 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a> 中所列的四条数据路径。</li><li><strong>轻量高效。</strong> 仅 5000 万活跃参数 + 128K 上下文窗口，使其可无缝嵌入请求链路前端，而不会显著增加延迟或计算成本。</li><li><strong>支持微调。</strong> 医疗、法律、人力资源等垂直领域可基于自身隐私分类体系，扩展模型标签集合。</li></ul>

<h2 id="limitations">局限性</h2>

<h2 id="limitations">局限性</h2>

<ul><li>不构成合规性保证——应作为更广泛的“以隐私为本的设计”（privacy-by-design）方法论中的<strong>其中一环</strong>。</li><li>在非英语文本、非拉丁字母文字（如中文、阿拉伯文、西里尔文等）以及命名模式代表性不足的语境中，性能明显下降。</li><li>典型失效模式包括：对生僻姓名检测不足，以及对公众实体（如知名机构名、地名）过度脱敏。</li><li>在医疗、法律、金融、人力资源等高敏感度场景中，仍需人工复核。</li></ul>

<ul><li>不构成合规性保证——应作为更广泛的“以隐私为本的设计”（privacy-by-design）方法论中的<strong>其中一环</strong>。</li><li>在非英语文本、非拉丁字母文字（如中文、阿拉伯文、西里尔文等）以及命名模式代表性不足的语境中，性能明显下降。</li><li>典型失效模式包括：对生僻姓名检测不足，以及对公众实体（如知名机构名、地名）过度脱敏。</li><li>在医疗、法律、金融、人力资源等高敏感度场景中，仍需人工复核。</li></ul>

<h2 id="use-cases">典型应用场景</h2>

<h2 id="use-cases">典型应用场景</h2>

<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>应用场景</th>
<th>过滤器如何适配</th>
</tr>
</thead>
<tbody><tr>
<td><strong>提示词预处理脱敏</strong></td>
<td>在将提示词发送至第三方大语言模型 API 前，先行剥离其中的 PII</td>
</tr>
<tr>
<td><strong>数据集清洗</strong></td>
<td>对用于训练、微调或分析的数据集执行 PII 脱敏</td>
</tr>
<tr>
<td><strong>本地化隐私网关</strong></td>
<td>在自托管 AI 流程中，对进出系统的文本流实施实时过滤</td>
</tr>
<tr>
<td><strong>浏览器端过滤</strong></td>
<td>通过 Transformers.js 在浏览器中直接运行，确保数据在离开设备前即完成脱敏</td>
</tr>
<tr>
<td><strong>定制化脱敏策略</strong></td>
<td>针对特定领域（如医疗 ID、法律案号）微调模型，扩展 PII 类型覆盖</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->

<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>应用场景</th>
<th>过滤器如何适配</th>
</tr>
</thead>
<tbody><tr>
<td><strong>提示词预处理脱敏</strong></td>
<td>在将提示词发送至第三方大语言模型 API 前，先行剥离其中的 PII</td>
</tr>
<tr>
<td><strong>数据集清洗</strong></td>
<td>对用于训练、微调或分析的数据集执行 PII 脱敏</td>
</tr>
<tr>
<td><strong>本地化隐私网关</strong></td>
<td>在自托管 AI 流程中，对进出系统的文本流实施实时过滤</td>
</tr>
<tr>
<td><strong>浏览器端过滤</strong></td>
<td>通过 Transformers.js 在浏览器中直接运行，确保数据在离开设备前即完成脱敏</td>
</tr>
<tr>
<td><strong>定制化脱敏策略</strong></td>
<td>针对特定领域（如医疗 ID、法律案号）微调模型，扩展 PII 类型覆盖</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->

<h2 id="references">参考链接</h2>

<h2 id="references">参考链接</h2>

<ul><li><a href="https://huggingface.co/openai/privacy-filter?ref=dsebastien.net">https://huggingface.co/openai/privacy-filter</a></li></ul>

<ul><li><a href="https://huggingface.co/openai/privacy-filter?ref=dsebastien.net">https://huggingface.co/openai/privacy-filter</a></li></ul>

<h2 id="related">相关条目</h2>

<h2 id="related">相关条目</h2>

<ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net">人工智能隐私（AI Privacy）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">Hugging Face</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">人工智能专家混合模型（MoE）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLMs）</a></li></ul>

<ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/OpenAI?ref=dsebastien.net">OpenAI</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net">人工智能隐私（AI Privacy）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.04+Creations/Articles/Where+Your+AI+Prompts+Really+Go+-+A+Practical+Guide+to+AI+Privacy+(Article)?ref=dsebastien.net">《你的 AI 提示词究竟去了哪里？——人工智能隐私实用指南》（文章）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/HuggingFace?ref=dsebastien.net">Hugging Face</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Apache+2.0+License?ref=dsebastien.net">Apache 2.0 许可协议</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Transformers?ref=dsebastien.net">Transformers</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Mixture+of+Experts+(MoE)?ref=dsebastien.net">人工智能专家混合模型（MoE）</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大语言模型（LLMs）</a></li></ul>
