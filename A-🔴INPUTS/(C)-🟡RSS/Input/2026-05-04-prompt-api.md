---
title: "Prompt API"
url: "https://www.dsebastien.net/prompt-api/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了W3C正在制定的“Prompt API”提案，旨在为Web开发者提供统一的JavaScript接口，直接调用浏览器或操作系统内置的语言模型，实现完全本地化的AI推理。该API支持有状态会话、流式响应、结构化输出和多模态输入，强调隐私优先（数据不出设备）和模型抽象（无需管理权重）。目前处于实验阶段，Chrome与Edge计划于2026年支持，是WebMachineLearning生态的关键组件，上层承接写作辅助类API，底层依托WebNN等低级AI能力。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+API?ref=dsebastien.net"><em>Prompt API</em></a><em>.</em></p><p>A W3C proposal enabling web developers to access browser-provided or OS-provided language models directly via a JavaScript API. Supports prompt-completion workflows with stateful sessions, streaming, structured outputs, and multimodal inputs &#x2014; all running on-device with no cloud dependency.</p><p>Spec repo: <a href="https://github.com/webmachinelearning/prompt-api?ref=dsebastien.net">https://github.com/webmachinelearning/prompt-api</a> Part of the <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net">WebMachineLearning</a> ecosystem.</p><h2 id="status">Status</h2><p>Experimental in Chrome and Microsoft Edge (2026). Under active W3C development.</p><h2 id="core-capabilities">Core Capabilities</h2>
<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody><tr>
<td>Session management</td>
<td>Stateful conversations across multiple prompts</td>
</tr>
<tr>
<td>Streaming</td>
<td><code>promptStreaming()</code> for real-time token output</td>
</tr>
<tr>
<td>System prompts</td>
<td>Configurable system context per session</td>
</tr>
<tr>
<td>Multimodal inputs</td>
<td>Text, images, and audio</td>
</tr>
<tr>
<td>Structured outputs</td>
<td>JSON Schema or regex constraints on model output</td>
</tr>
<tr>
<td>Tool calling</td>
<td>Invoke JavaScript functions from model decisions</td>
</tr>
<tr>
<td>Token tracking</td>
<td>Monitor context usage and handle overflow</td>
</tr>
<tr>
<td>Abort signal</td>
<td>Cancel in-flight requests</td>
</tr>
<tr>
<td>Availability check</td>
<td>Detect whether a model is available before using</td>
</tr>
<tr>
<td>Download progress</td>
<td>Monitor model download state</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->
<h2 id="key-design-principles">Key Design Principles</h2><ul><li><strong>Local-first</strong>: model inference happens on device; no data transmitted to external servers</li><li><strong>Privacy by default</strong>: prompts and responses never leave the machine</li><li><strong>Standardized contract</strong>: one API across browsers (once standardized)</li><li><strong>Model abstraction</strong>: developers don&apos;t manage model weights directly</li></ul><h2 id="usage-pattern">Usage Pattern</h2><pre><code class="language-js">const session = await ai.languageModel.create({
  systemPrompt: &quot;You are a helpful assistant.&quot;
});

const stream = session.promptStreaming(&quot;Summarize this text: ...&quot;);
for await (const chunk of stream) {
  console.log(chunk);
}
</code></pre><h2 id="relationship-to-sibling-apis">Relationship to Sibling APIs</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net"><strong>WebNN API</strong></a>: lower-level neural network ops; Prompt API builds on top</li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net"><strong>Writing Assistance APIs</strong></a>: higher-level task-specific wrappers (Summarizer, Writer, Rewriter)</li></ul><h2 id="references">References</h2><ul><li><a href="https://github.com/webmachinelearning/prompt-api?ref=dsebastien.net">https://github.com/webmachinelearning/prompt-api</a></li><li><a href="https://github.com/webmachinelearning?ref=dsebastien.net">https://github.com/webmachinelearning</a></li></ul><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net">WebMachineLearning</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">Large Language Models (LLMs)</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">AI Inference</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net">AI Privacy</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net">WebNN API</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net">Writing Assistance APIs</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Browser-Provided+Language+Models?ref=dsebastien.net">Browser-Provided Language Models</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/On-Device+Machine+Learning?ref=dsebastien.net">On-Device Machine Learning</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Nano?ref=dsebastien.net">Gemini Nano</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Tool+Calling?ref=dsebastien.net">LLM Tool Calling</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Structured+Outputs?ref=dsebastien.net">LLM Structured Outputs</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Streaming?ref=dsebastien.net">LLM Streaming</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Edge+AI?ref=dsebastien.net">Edge AI</a></li></ul>

## 中文译文

这是我的公开笔记中的一则备注。查看权威版本：Prompt API。

一项由万维网联盟（W3C）提出的规范草案，旨在使网页开发者能够通过 JavaScript API 直接调用浏览器或操作系统内置的语言模型。该 API 支持基于提示词的补全工作流，具备有状态会话、流式响应、结构化输出及多模态输入等能力——所有运算均在设备端完成，无需依赖云端服务。

规范仓库地址：https://github.com/webmachinelearning/prompt-api  
本项目属于 WebMachineLearning 生态系统的一部分。

当前状态

Chrome 与 Microsoft Edge 浏览器中处于实验性阶段（预计于2026年启用）。目前正由 W3C 积极推进标准化工作。

核心能力

关键设计原则

以本地为先（Local-first）：模型推理完全在设备端执行，不向外部服务器传输任何数据；  
默认隐私保护（Privacy by default）：提示词与响应内容永不离开用户设备；  
标准化接口（Standardized contract）：一旦完成标准化，将在各浏览器中提供统一的 API；  
模型抽象化（Model abstraction）：开发者无需直接管理模型权重。

使用模式

与相关 API 的关系

WebNN API：提供更底层的神经网络算子支持；Prompt API 建立在其基础之上；  
写作辅助类 API（Writing Assistance APIs）：面向具体任务的高层封装（如摘要生成器 Summarizer、文本撰写器 Writer、文本改写器 Rewriter）。

参考资料

https://github.com/webmachinelearning/prompt-api  
https://github.com/webmachinelearning  

相关主题

WebMachineLearning  
大语言模型（LLMs）  
AI 推理（AI Inference）  
AI 隐私保护（AI Privacy）  
WebNN API  
写作辅助类 API（Writing Assistance APIs）  
浏览器内置语言模型（Browser-Provided Language Models）  
设备端机器学习（On-Device Machine Learning）  
Gemini Nano  
大语言模型工具调用（LLM Tool Calling）  
大语言模型结构化输出（LLM Structured Outputs）  
大语言模型流式响应（LLM Streaming）  
边缘 AI（Edge AI）
