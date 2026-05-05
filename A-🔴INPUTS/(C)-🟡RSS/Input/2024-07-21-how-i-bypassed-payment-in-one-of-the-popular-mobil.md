---
title: "How I bypassed payment in one of the popular mobile apk and got free subsciption"
url: "https://medium.com/@deepk007/how-i-bypassed-payment-in-one-of-the-popular-mobile-apk-and-got-free-subsciption-46e94f61c089?source=rss-1646886baef5------2"
source: "DEep"
date: 2024-07-21
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文作者以渗透测试方式发现某款拥有超400万下载量的热门英语对话应用存在严重支付绕过漏洞：通过抓包修改订阅请求中的`actual_amount`参数为极低金额（如1卢比），即可免费获取付费订阅服务。该漏洞源于服务端未对关键支付参数进行校验，安全防护形同虚设。作者强调，即使面对高知名度应用，也不应预设其安全性，主动尝试常能发现被忽视的基础性缺陷。

---

<p>Helloo hackers, I hope you are doing well, in this blog I’m gonna show you how I bypassed the payment in one of the popular talking application. At the time of this writing this applicatoin has over 4M+ downloads. Bypassing payment was quite easy.</p><p>Let’s do this.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/420/0*F0NZLULV_eDMK4aG.gif" /></figure><p>One day I decided to learn speak English. So, I searched on you tube how can I improve my english speaking. There in, one of the video, the guy was sponsoring the talking application obviously I had to pay subsciption fee to talk to the people. That caught my eye.</p><p>Immediatly I went on play store and searched the application. I was astonished by the user it had. I thought, the security of the application would be high. But still I decided to give it a try :)</p><p>As I had my mobile testing setup on NOX. Only thing I had to do is to setup the proxy and download the application.</p><p>All done, Now it’s time for playing with the application. First I tried for the account takeover vulnerability as it’s my one of the favorite vulnerability. But didn’t succeed.</p><p>Immidiatly I moved to the payment functionality, there, I saw subsciption package. I choose random package and start caputring request.</p><p>Request was looked something like the below.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/855/1*E2lxGebapORVfD8YHEqyCw.jpeg" /></figure><p>I just changed the actual_amount to the rupees 1.</p><p>And guess whatttt !! succeed. Quite easy haahhahh.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/496/1*FrkBDvMbuHLQ5mmDiD59Mw.jpeg" /></figure><figure><img alt="" src="https://cdn-images-1.medium.com/max/407/1*9B19Vb-V9wvFNJCJ-pHGHg.jpeg" /></figure><p>Got the payment bypassed. And got the subsciption package ;)</p><p>I never thought such popular application may have such silly mistakes in their application.</p><p>Now I learned one thing is that what we think is not what actually is. In my case If I hadn’t thought of giving a try. I wouldn’t be able to discover this vulnerability.</p><p>I hope you gained some knowledge or learned something new.</p><p>If you wanna connect me to linkedin <a href="https://www.linkedin.com/in/deep-kachhadiya-aa8271310/">here </a>its.</p><p>If this blog add some value in your learning journey don’t forget to hit clapp button👏👏</p><p>Thank you for reading this blog😄😊 see you in the next blog 🙌🙌.</p><p>HAPPY HACKING ❤️❤️</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=46e94f61c089" width="1" />
