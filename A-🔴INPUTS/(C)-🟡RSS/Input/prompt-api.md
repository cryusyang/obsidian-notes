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
> 本文介绍了W3C正在制定的“Prompt API”标准，旨在让Web开发者通过JavaScript直接调用浏览器或操作系统内置的语言模型，实现完全本地化的AI推理。该API支持有状态会话、流式响应、结构化输出和多模态输入，强调隐私优先（数据不出设备）与模型抽象（无需管理权重）。目前处于实验阶段，Chrome与Edge计划于2026年支持，并作为WebMachineLearning生态的关键组件，上层承接写作辅助API、下层依托WebNN API。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Prompt API](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+API?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[Prompt API](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Prompt+API?ref=dsebastien.net)。

A W3C proposal enabling web developers to access browser-provided or OS-provided language models directly via a JavaScript API. Supports prompt-completion workflows with stateful sessions, streaming, structured outputs, and multimodal inputs — all running on-device with no cloud dependency.

一项由万维网联盟（W3C）提出的提案，旨在使网页开发者能通过 JavaScript API 直接调用浏览器或操作系统内置的语言模型。支持具备状态会话、流式响应、结构化输出和多模态输入的提示-补全工作流——全部在设备本地运行，无需依赖云端服务。

Spec repo: [https://github.com/webmachinelearning/prompt-api](https://github.com/webmachinelearning/prompt-api) Part of the [WebMachineLearning](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net) ecosystem.

规范仓库地址：[https://github.com/webmachinelearning/prompt-api](https://github.com/webmachinelearning/prompt-api)。属于 [WebMachineLearning](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net) 生态系统的一部分。

## Status

## 状态

Experimental in Chrome and Microsoft Edge (2026). Under active W3C development.

目前处于 Chrome 与 Microsoft Edge 浏览器的实验性阶段（预计 2026 年上线）。W3C 正在积极推进该规范的制定工作。

## Core Capabilities

## 核心能力

| Feature | Description |
|---------|-------------|
| Session management | Stateful conversations across multiple prompts |
| Streaming | `promptStreaming()` for real-time token output |
| System prompts | Configurable system context per session |
| Multimodal inputs | Text, images, and audio |
| Structured outputs | JSON Schema or regex constraints on model output |
| Tool calling | Invoke JavaScript functions from model decisions |
| Token tracking | Monitor context usage and handle overflow |
| Abort signal | Cancel in-flight requests |
| Availability check | Detect whether a model is available before using |
| Download progress | Monitor model download state |

| 功能 | 描述 |
|------|------|
| 会话管理 | 跨多个提示的有状态对话 |
| 流式响应 | 使用 `promptStreaming()` 实现实时 token 输出 |
| 系统提示 | 每个会话可配置系统上下文 |
| 多模态输入 | 支持文本、图像和音频 |
| 结构化输出 | 对模型输出施加 JSON Schema 或正则表达式约束 |
| 工具调用 | 根据模型决策调用 JavaScript 函数 |
| Token 追踪 | 监控上下文使用量并处理溢出情况 |
| 中止信号 | 取消进行中的请求 |
| 可用性检查 | 在使用前检测模型是否可用 |
| 下载进度 | 监控模型下载状态 |

## Key Design Principles

## 关键设计原则

- **Local-first**: model inference happens on device; no data transmitted to external servers  
- **Privacy by default**: prompts and responses never leave the machine  
- **Standardized contract**: one API across browsers (once standardized)  
- **Model abstraction**: developers don't manage model weights directly  

- **本地优先**：模型推理完全在设备端执行；不向外部服务器传输任何数据  
- **默认隐私保护**：提示词与响应内容永不离开用户设备  
- **标准化契约**：跨浏览器统一接口（待标准正式确立后）  
- **模型抽象化**：开发者无需直接管理模型权重  

## Usage Pattern

## 使用模式

```js
const session = await ai.languageModel.create({
  systemPrompt: "You are a helpful assistant."
});

const stream = session.promptStreaming("Summarize this text: ...");
for await (const chunk of stream) {
  console.log(chunk);
}
```

```js
const session = await ai.languageModel.create({
  systemPrompt: "你是一位乐于助人的助手。"
});

const stream = session.promptStreaming("请总结以下文本：……");
for await (const chunk of stream) {
  console.log(chunk);
}
```

## Relationship to Sibling APIs

## 与其他同级 API 的关系

- [**WebNN API**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net): lower-level neural network ops; Prompt API builds on top  
- [**Writing Assistance APIs**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net): higher-level task-specific wrappers (Summarizer, Writer, Rewriter)  

- [**WebNN API**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net)：更底层的神经网络运算接口；Prompt API 建立在其基础之上  
- [**写作辅助 API**](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net)：更高层级、面向特定任务的封装接口（如摘要生成器、文案撰写器、改写器等）  

## References

## 参考资料

- [https://github.com/webmachinelearning/prompt-api](https://github.com/webmachinelearning/prompt-api)  
- [https://github.com/webmachinelearning](https://github.com/webmachinelearning)  

- [https://github.com/webmachinelearning/prompt-api](https://github.com/webmachinelearning/prompt-api)  
- [https://github.com/webmachinelearning](https://github.com/webmachinelearning)  

## Related

## 相关主题

- [WebMachineLearning](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net)  
- [Large Language Models (LLMs)](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  
- [AI Inference](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)  
- [AI Privacy](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net)  
- [WebNN API](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net)  
- [Writing Assistance APIs](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net)  
- [Browser-Provided Language Models](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Browser-Provided+Language+Models?ref=dsebastien.net)  
- [On-Device Machine Learning](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/On-Device+Machine+Learning?ref=dsebastien.net)  
- [Gemini Nano](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Nano?ref=dsebastien.net)  
- [LLM Tool Calling](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Tool+Calling?ref=dsebastien.net)  
- [LLM Structured Outputs](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Structured+Outputs?ref=dsebastien.net)  
- [LLM Streaming](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Streaming?ref=dsebastien.net)  
- [Edge AI](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Edge+AI?ref=dsebastien.net)  

- [WebMachineLearning](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebMachineLearning?ref=dsebastien.net)  
- [大语言模型（LLMs）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Large+Language+Models+(LLMs)?ref=dsebastien.net)  
- [AI 推理](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Inference?ref=dsebastien.net)  
- [AI 隐私保护](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/AI+Privacy?ref=dsebastien.net)  
- [WebNN API](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/WebNN+API?ref=dsebastien.net)  
- [写作辅助 API](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Writing+Assistance+APIs?ref=dsebastien.net)  
- [浏览器内置语言模型](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Browser-Provided+Language+Models?ref=dsebastien.net)  
- [设备端机器学习](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/On-Device+Machine+Learning?ref=dsebastien.net)  
- [Gemini Nano](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Gemini+Nano?ref=dsebastien.net)  
- [LLM 工具调用](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Tool+Calling?ref=dsebastien.net)  
- [LLM 结构化输出](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Structured+Outputs?ref=dsebastien.net)  
- [LLM 流式响应](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/LLM+Streaming?ref=dsebastien.net)  
- [边缘 AI（Edge AI）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Edge+AI?ref=dsebastien.net)
