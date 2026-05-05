---
title: "How I accessed Admin panel by just one payload."
url: "https://medium.com/@deepk007/how-i-found-sql-injection-vulnerability-in-admin-panel-b0356fac260c?source=rss-1646886baef5------2"
source: "DEep"
date: 2024-04-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 该文章是一名网络安全初学者Deep分享的首次发现高危漏洞并获得赏金的经历。他通过在目标网站URL后直接添加“/admin”路径意外访问到未授权的管理员后台，再结合Wappalyzer识别出MySQL数据库，尝试基础SQL注入（如`admin' OR 1 --`）成功绕过登录验证。随后他在后台获取了用户手机号和邮箱等敏感信息，并向相关组织提交漏洞报告，最终获得2500卢比的赏金奖励。

---

<h3>How I accessed admin panel and got my first bounty 😁</h3><p>HIii there, My name is Deep. I’m a cybersecurity student. This is my first blog. In my writeup if there is any mistakes so pls let me know.</p><p><em>Story of how I found bug</em></p><p>One day I was just scrolling in this site where I found my critical bug. And I thought let looks for vulnerability. So I decided to look in register. There I throw some xss payload. But I could’t find anything there :(. Then, after few minutes I decided to look for admin panel. And I just type /admin after the site url and I got admin panel.</p><p>Then, I looked for the database the site was using by wappalyzer. And the site was using mysql database.</p><p>Moving forward, immediately I put simple and easy sql payload just besides the admin like this (admin' OR 1 --)in the password field whatever you like to enter.</p><p>POC</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*fV8JZxsuVH678yfDWmR5Hw.png" /></figure><p>And by chance I got admin panel :). There I found the users mobile no. and email information.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*puCRSyR0YTLZ8yohJdpSvw.png" /></figure><p>Immediately I decided to report to the organization. However this site was not included in any bb platform. But, bcz of my work and this critical vulnerability I got ₹2500(Rupees) as a bounty.</p><p>I hope you like this blog ! You can show me some love by hitting clap button. Thanks for reading this till to the end.</p><p>Here is my <a href="https://www.linkedin.com/in/deep-kachhadiya-aa8271310/">linkedin</a> profile feel free to connect me.</p><p>If you wanna support me so you can buy me a coffee 😋 by clicking the below link.</p><figure><a href="https://www.buymeacoffee.com/dEEpPatTel"><img alt="" src="https://cdn-images-1.medium.com/max/170/1*h3Jkg0WDTlsp7rUCPfWp0g.png" /></a></figure><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=b0356fac260c" width="1" />
