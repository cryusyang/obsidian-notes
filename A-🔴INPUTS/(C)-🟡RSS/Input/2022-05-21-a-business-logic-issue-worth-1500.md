---
title: "A business Logic issue worth $1500"
url: "https://mokhansec.medium.com/a-business-logic-issue-worth-1500-a0f1a0b76570?source=rss-ae64c019f634------2"
source: "Mohsin"
date: 2022-05-21
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文作者Mohsin Khan（网名Tabaahi_）披露了一个在私有Bug Bounty项目（代称redirect.com）中发现的安全漏洞：该平台的“设备封禁”功能在Android应用上存在失效问题——当用户账户在后台被封禁某Android设备后，该设备上的App仍保持登录状态且可继续使用，而iOS和桌面端则正常登出。作者通过对比多端行为、查阅文档并复现验证，确认该漏洞源于Android端安全逻辑实现缺陷。漏洞已提交给厂商并修复，作者呼吁安全研究人员关注类似具备设备管理功能的程序。

---

<p>Hello everyone,</p><p>Its me Mohsin khan AKA <a href="https://twitter.com/tabaahi_">tabaahi_</a>.Today I would like to talk about one of my recent findings.</p><p>It was a private bug crowd program. The issue is resolved now. But I don’t have permission from the program so will call it <strong>redirect.com</strong>.</p><p>The program has a website, android, IOS app, and desktop app in the scope. Started with a Web application, and I found the block device option.</p><p>After reading docs (related to block devices) I understand User can log in to his/her account in android, IOS apps, and desktop apps. And devices will show on the device option.</p><p>If I click on the blocked device the account of the user will log out from the device, and the User will not be able to login to the application (on the blocked device) until I unblock the device.</p><p>So I installed android, IOS app, and desktop app. And login to the application. I notice IOS app and desktop app working fine. But when I blocked the <strong>android application</strong> login, The user is still logged in. Security implementation for the android app is not working properly.</p><p>I reported to them</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*4SX9MRII7Ov_3rSzJuJtJQ.png" /></figure><p>There are so many programs that allow block device features. Go and try now :)</p><p>Thank you for reading! And don’t forget to follow me on <a href="https://twitter.com/tabaahi_">Twitter</a>.</p><p><a href="https://twitter.com/tabaahi_"><strong>Tabaahi_</strong></a></p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=a0f1a0b76570" width="1" />
