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
> 本文介绍了W3C正在制定的Prompt API标准，旨在让Web开发者通过JavaScript直接调用浏览器或操作系统内置的语言模型，实现完全本地化的AI推理。该API支持有状态会话、流式响应、结构化输出和多模态输入，强调“本地优先”与“隐私默认”，所有数据均不离开设备。目前处于实验阶段，Chrome和Edge计划于2026年支持。它位于WebMachineLearning生态中，上承Writing Assistance等高层API，下依赖WebNN等底层神经网络接口，是对设备端大模型能力的标准化抽象。

---

<p><em>这是来自我的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>公开笔记</em></a><em> 的一条记录。查看权威版本：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+API?ref=dsebastien.net"><em>Prompt API</em></a><em>。</em></p>

<p>这是一项由 W3C 提出的标准草案，旨在让网页开发者能通过 JavaScript API 直接调用浏览器或操作系统内置的语言模型。该 API 支持基于状态会话的提示补全（prompt-completion）工作流，具备流式响应、结构化输出和多模态输入能力——所有计算均在设备本地完成，无需依赖云端服务。</p>

<p>规范仓库：<a href="https://github.com/webmachinelearning/prompt-api?ref=dsebastien.net">https://github.com/webmachinelearning/prompt-api</a>，属于 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net">WebMachineLearning</a> 生态系统的一部分。</p>

<h2 id="status">当前状态</h2>

<p>Chrome 与 Microsoft Edge 浏览器中处于实验性阶段（预计 2026 年启用），W3C 正在积极推进其标准化进程。</p>

<h2 id="core-capabilities">核心能力</h2>

<!--kg-card-begin: html-->
<table>
<thead>
<tr>
<th>功能</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>会话管理</td>
<td>支持跨多个提示的有状态对话</td>
</tr>
<tr>
<td>流式响应</td>
<td>通过 <code>promptStreaming()</code> 实现实时 token 输出</td>
</tr>
<tr>
<td>系统提示词</td>
<td>每个会话可配置独立的系统上下文</td>
</tr>
<tr>
<td>多模态输入</td>
<td>支持文本、图像与音频输入</td>
</tr>
<tr>
<td>结构化输出</td>
<td>通过 JSON Schema 或正则表达式约束模型输出格式</td>
</tr>
<tr>
<td>工具调用</td>
<td>根据模型决策触发 JavaScript 函数调用</td>
</tr>
<tr>
<td>Token 使用追踪</td>
<td>监控上下文长度并处理溢出情况</td>
</tr>
<tr>
<td>中止信号</td>
<td>取消正在进行中的请求</td>
</tr>
<tr>
<td>可用性检测</td>
<td>使用前可预先判断模型是否可用</td>
</tr>
<tr>
<td>模型下载进度</td>
<td>监控本地模型的下载状态</td>
</tr>
</tbody></table>
<!--kg-card-end: html-->

<h2 id="key-design-principles">关键设计原则</h2>

<ul>
<li><strong>本地优先（Local-first）</strong>：模型推理完全在设备端执行，不向外部服务器传输任何数据</li>
<li><strong>默认隐私保护（Privacy by default）</strong>：提示词与响应内容永不离开用户设备</li>
<li><strong>标准化契约（Standardized contract）</strong>：一旦标准化，将提供统一的跨浏览器 API 接口</li>
<li><strong>模型抽象（Model abstraction）</strong>：开发者无需直接管理模型权重等底层细节</li>
</ul>

<h2 id="usage-pattern">典型使用模式</h2>

<pre><code class="language-js">const session = await ai.languageModel.create({
  systemPrompt: &quot;你是一位乐于助人的助手。&quot;
});

const stream = session.promptStreaming(&quot;请总结以下文本：...&quot;);
for await (const chunk of stream) {
  console.log(chunk);
}
</code></pre>

<h2 id="relationship-to-sibling-apis">与其他同级 API 的关系</h2>

<ul>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net"><strong>WebNN API</strong></a>：更底层的神经网络运算接口；Prompt API 建立在其基础之上</li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net"><strong>写作辅助类 API</strong></a>：更高层级、面向具体任务的封装（如摘要生成器、文案撰写器、改写器等）</li>
</ul>

<h2 id="references">参考资料</h2>

<ul>
<li><a href="https://github.com/webmachinelearning/prompt-api?ref=dsebastien.net">https://github.com/webmachinelearning/prompt-api</a></li>
<li><a href="https://github.com/webmachinelearning?ref=dsebastien.net">https://github.com/webmachinelearning</a></li>
</ul>

<h2 id="related">相关主题</h2>

<ul>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net">WebMachineLearning</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net">大型语言模型（LLMs）</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net">AI 推理</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net">AI 隐私保护</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net">WebNN API</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net">写作辅助类 API</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Browser-Provided+Language+Models?ref=dsebastien.net">浏览器内置语言模型</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/On-Device+Machine+Learning?ref=dsebastien.net">设备端机器学习</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Nano?ref=dsebastien.net">Gemini Nano</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Tool+Calling?ref=dsebastien.net">大语言模型工具调用</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Structured+Outputs?ref=dsebastien.net">大语言模型结构化输出</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Streaming?ref=dsebastien.net">大语言模型流式响应</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Edge+AI?ref=dsebastien.net">边缘 AI（Edge AI）</a></li>
</ul>
