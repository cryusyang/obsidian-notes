---
title: "Bypassing Email Uniqueness Check: A Logic Flaw Disrupting Password Recovery"
url: "https://medium.com/@0xoroot/bypassing-email-uniqueness-check-a-logic-flaw-disrupting-password-recovery-95464c95b664?source=rss-ef0c2df05c49------2"
source: "0xoroot"
date: 2024-10-20
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 该文章描述了一个网站邮箱重复注册的逻辑缺陷：用户首次修改邮箱为已存在地址时被拒绝，但后续修改请求却意外通过，导致同一邮箱关联多个账户。此问题使“忘记密码”功能完全失效，因后端在发送重置令牌时无法处理重复邮箱而报错。作者认为该漏洞严重性较低，主要影响服务可用性。

---

<p>I wanted to share a bug I found some time ago. This is the first bug I’ll be sharing, but it certainly won’t be the last, inshallah. It was one of the more unusual bugs I’ve encountered. We have a website, and typically, the logic of any website ensures that you can’t create an account with the same email. The site I was testing followed this rule too.</p><p>However, when I tried to change the email, the first attempt was rejected. But when I tried again, surprisingly, it accepted the change. I thought, 'LOL,</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/494/1*27qv6UN-0UhMLLXfmzdajw.png" /></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/645/1*7H73h68gS4Nrn3J_FmX1gg.gif" /></figure><p>let me try again.' The code logic in my mind was that the backend is designed to send a notification only once, that the email already exists, and all subsequent requests pass through normally.</p><p>The impact of this bug is that it prevents a user from requesting a 'forgot password' reset. It fails entirely, as the backend, when trying to send a token to the email, finds two users with the same email. Obviously, it wasn’t designed for that and throws an error.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/772/1*tXOrgew-PqekS6XE1BRMNg.png" /></figure><p>So, this was a simple bug with a low severity, mainly affecting availability.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/220/1*L7Ua9z42WLtDqvP39NoJ3A.gif" /></figure><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=95464c95b664" width="1" />
