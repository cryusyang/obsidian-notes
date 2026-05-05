---
title: "Hidden in the Source: Discovering Reflected XSS via Manual Code Review"
url: "https://medium.com/@xelcezeri/hidden-in-the-source-discovering-reflected-xss-via-manual-code-review-c2a697d9d8c1?source=rss-51d79a0d79bb------2"
source: "elcezeri"
date: 2026-01-17
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文讲述了作者通过手动源码审查，在一个受保护的登录页面上发现反射型XSS漏洞的过程。面对自动化扫描失效和范围受限的情况，作者未放弃，转而查看页面源代码，意外发现一个内部搜索路径存在参数未过滤直接反射的问题。通过构造`"><script>`和`<img onerror>`等Payload，成功触发了XSS并执行任意JavaScript代码。文章强调：在漏洞挖掘中，人工阅读源码（如Ctrl+U）往往能发现自动化工具遗漏的关键漏洞。

---

<figure><img alt="" src="https://cdn-images-1.medium.com/max/682/1*vviHX7g90DnsvJhzq8EUTw.png" /></figure><p>In bug bounty hunting, when automated scanners fail and the scope is narrow, your best weapon is your own eyes. Today, I’ll share how I discovered a Reflected XSS vulnerability on a protected login page by simply digging into the application’s source code.</p><h3>The Hunt Begins</h3><p>While browsing a VDP program on HackerOne, I encountered a login screen reserved for company members. It was a simple interface requiring an ID and a password. I tried standard attacks like SQL Injection, Default Credentials, and Request Manipulation, but the application was solid.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/837/1*ScN3R-h7pIH8UKHm7Pqz-g.png" /></figure><h3>The Discovery: Reading Between the Lines</h3><p>Instead of moving on, I decided to perform a <strong>Manual Source Code Review</strong>. While inspecting the page’s source, I discovered an interesting path used for internal search functionality.</p><p>The path took two parameters and seemed to be used for filtering data. I copied the path and immediately started testing for input reflection: https://target.com/inc/search_xxxx?xxxx=”123&lt;&gt;</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/772/1*nN48Ua71mfWkJnP6sGEd5Q.png" /></figure><p>When I saw that the characters &lt;&gt; were reflected directly into the page without any sanitization, I knew I had found a potential entry point.</p><h3>Exploitation: From HTML to Javascript</h3><p>First, I confirmed <strong>HTML Injection</strong> was possible.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*tzJXTebkm_Ghy5CKE0mKqQ.png" /></figure><p>Then, I took it a step further to achieve <strong>Cross-Site Scripting (XSS)</strong>. I tried the following payloads:</p><ol><li>”&gt;&lt;script&gt;alert(“cezeri”)&lt;/script&gt;</li><li>“&gt;&lt;img src/onerror=prompt(document.cookie)&gt;</li></ol><p><strong>The Result:</strong> Both payloads executed perfectly. The application was rendering the xxxx parameter directly into the DOM, allowing for full client-side code execution.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*C7W4cQYQ6qVoTiLxecuGHQ.png" /></figure><p><strong>The Lesson:</strong> Never underestimate the power of Ctrl+U. Automated tools are great, but manual source code analysis can uncover vulnerabilities hidden in plain sight.</p><h3>Stay Connected</h3><ul><li><strong>X (Twitter):</strong> <a href="https://x.com/xelcezeri">@xelcezeri</a></li><li><a href="https://www.linkedin.com/in/xsametyigit/"><strong>LinkedIn:</strong> Samet Yiğit</a></li></ul><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=c2a697d9d8c1" width="1" />
