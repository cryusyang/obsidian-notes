---
title: "How I Got My First Critical Bug ## Easy Bug"
url: "https://medium.com/@0xoroot/how-i-got-my-first-critical-bug-easy-bug-fb5d1631bcd4?source=rss-ef0c2df05c49------2"
source: "0xoroot"
date: 2025-01-06
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 该文章描述了一位安全测试人员发现的一个高危漏洞：在“忘记密码”功能的响应中，系统直接返回了用户的密码（而非重置链接或提示），导致攻击者可轻易获取并接管账户。作者通过常规功能测试发现了这一严重安全问题，并确认该漏洞此前未被报告。尽管漏洞原理简单，但危害极大，最终成功提交并获得认可。

---

<p>Hi,</p><p>Today, I would like to share my first critical bug. Let’s gooooooo!<br />First, when I go into any program, I create an account and test the “Forgot Password” function. However, when I tested it, I noticed that in the response, when I reviewed it, the recovery forgot password was reflected in the response.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/757/1*oiSqeiYDyc1gPoZI97ydgg.png" /></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/412/1*LzMrWMYSsK-7Ov12mIDHmQ.png" /><figcaption>This is a screenshot from my email</figcaption></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/220/1*dHnDq-_oofWvRY_79S3XlA.gif" /></figure><p>At first, I was really shocked.<br />Why?<br />Because how could someone make this mistake, which leads to anyone being able to take over the account?</p><p>In the end, I was very successful with this bug, even though it was easy. There was no duplicate.<br />This is a short write-up. Thanks for reading! :)</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=fb5d1631bcd4" width="1" />
