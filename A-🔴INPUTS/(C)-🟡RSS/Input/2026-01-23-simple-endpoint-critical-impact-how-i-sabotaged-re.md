---
title: "Simple Endpoint, Critical Impact: How I Sabotaged Refunds"
url: "https://medium.com/@xelcezeri/simple-endpoint-critical-impact-how-i-sabotaged-refunds-1cd0ac7a4cb2?source=rss-51d79a0d79bb------2"
source: "elcezeri"
date: 2026-01-23
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文讲述了一位安全研究员在长期运行的电商网站Target上发现一个关键IDOR（不安全直接对象引用）漏洞的过程。他通过深入理解业务逻辑，聚焦于“退货与退款”功能，在拦截返回请求时发现rorderID参数为可预测的整型ID，并能通过枚举ID访问他人退货页面。利用该漏洞，攻击者可未经授权取消任意用户的退款请求，造成实质性经济损失。该漏洞在提交后24小时内被确认并获得高额赏金。

---

<p>When hunting in programs that have been active for years, many researchers fear “duplicates.” However, bugs often hide in specific functional workflows that others might overlook. Today, I’ll share how I found a simple but impactful IDOR vulnerability on a well-established e-ommerce site.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/786/1*ElDgo17_1uO3AnzEGHu74A.png" /></figure><h3>The Strategy: Understanding the Flow</h3><p>I spent 1–2 hours just browsing target.com without sending complex payloads. My goal was simple: Understand how the business logic works. After testing price manipulation and common business logic flaws without success, I decided to test the <strong>Return &amp; Refund</strong> system.</p><h3>The Discovery: Intercepting the Return Request</h3><p>I made a legitimate purchase and then initiated a return request while the order was still in the “preparation” phase. When I clicked the return button, I intercepted the following request: <a href="https://www.target.com/return/rorderID=1123">https://www.target.com/return/rorderID=1123</a></p><h3>The Attack: Disrupting the Refund Process</h3><p>I noticed the rorderID was a simple integer. I quickly tested the previous IDs:</p><ul><li>.../return/rorderID=1122</li><li>.../return/rorderID=1121</li></ul><p><strong>The Result:</strong> I successfully accessed the return pages of other users. While I couldn’t see their private PII (Personally Identifiable Information), the page gave me a critical option: <strong>“Cancel Refund Request.”</strong></p><p>By simply changing the ID, I could cancel any user’s refund, preventing them from getting their money back. This is a classic example of an IDOR leading to unauthorized functional manipulation.</p><h3>Conclusion &amp; Reward</h3><p>I reported the finding immediately. Despite the program being two years old, this specific endpoint had been overlooked.</p><ul><li><strong>Timeline:</strong> Reported and accepted within 24 hours.</li><li><strong>Bounty:</strong> $$$.</li></ul><h3>Stay Connected</h3><ul><li><strong>X (Twitter):</strong> <a href="https://x.com/xelcezeri">@xelcezeri</a></li><li><a href="https://www.linkedin.com/in/xsametyigit/"><strong>LinkedIn:</strong> Samet Yiğit</a></li></ul><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=1cd0ac7a4cb2" width="1" />
