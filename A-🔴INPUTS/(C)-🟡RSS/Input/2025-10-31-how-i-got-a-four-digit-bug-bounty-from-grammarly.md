---
title: "How I Got a Four-Digit Bug Bounty From Grammarly"
url: "https://hexaphp.medium.com/how-i-got-a-four-digit-bug-bounty-from-grammarly-187038396843?source=rss-c4f7ec62144d------2"
source: "Aland Dlshad (HexaPhp)"
date: 2025-10-31
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 研究人员在测试Grammarly文档上传功能时，发现服务端仅凭`blobId`（文件唯一标识）返回文件内容，未校验用户所有权，导致任意账户均可通过已知`blobId`访问他人文件，构成IDOR（不安全直接对象引用）漏洞。该漏洞被及时上报，Grammarly在约一个月内修复，并向报告者发放了四位数奖金。案例凸显了服务端必须强制校验资源访问权限的重要性。

---

<p>Sometimes, big bugs hide in the simplest places. While testing Grammarly’s document upload feature, I noticed a tiny detail in the upload response, a parameter called blobId. Naturally, my curiosity kicked in: <em>what happens if I change it?</em></p><h3>The Test</h3><p>I uploaded a document from my account, and Grammarly returned a blobId, basically the file’s secret ID. Here’s what the request looked like:</p><pre>POST /xxxxxx/xxxxx/xxx<br />Host: xxx.grammarly.com<br />Content-Type: application/json<br /><br />{<br />  &quot;blobId&quot;: &quot;bl-5geoz6PRk-&quot;,<br />  &quot;fileName&quot;: &quot;test.docx&quot;<br />}</pre><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*DZR2UX3fzk7QZyE2qepmog.png" /></figure><p>Curious, I opened a new browser session with a different account and sent the same blobId. And then boom, the server returned the file. No questions asked. No ownership check. Just the file, like it was saying, <em>“Here you go, enjoy!”</em></p><figure><img alt="" src="https://cdn-images-1.medium.com/max/936/1*8J_la-5y1W-Q0s35rap15g.png" /></figure><h3>What Happened</h3><p>The system trusted the blobId alone instead of checking who owned the file. This is called an <strong>IDOR (Insecure Direct Object Reference)</strong>. In simple words: if someone knows a file’s ID, they could access someone else’s file.</p><h3>Takeaway</h3><p>Always check ownership and never blindly trust file IDs. And sometimes, a little curiosity can pay off literally.</p><p>Thanks to Grammarly for quickly addressing the issue and acknowledging my report with a four-digit $$$$ bounty. It was a great reminder that curiosity, when combined with responsible reporting, can lead to positive outcomes.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*UZR-UUHS8_9u1wVlXs8FQQ.png" /></figure><p><strong>Reported on:</strong> September 14, 2025<br /><strong>Fixed on:</strong> October 9, 2025</p><p>https://hexaphp.com</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=187038396843" width="1" />
