---
title: "How I got my first US Dollar bounty"
url: "https://medium.com/@deepk007/how-i-got-my-first-us-dollar-bounty-4df50ee82fc6?source=rss-1646886baef5------2"
source: "DEep"
date: 2024-05-27
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 作者在参与某VDP（漏洞披露计划）时，通过常规功能测试发现了一个用户邮箱泄露漏洞：在向其他用户发送消息的过程中，后端响应中意外返回了目标用户的注册邮箱。该漏洞通过Burp Suite捕获并重放请求即可复现，属于敏感信息泄露类高危问题。作者提交包含详细复现步骤和POC的报告后，24小时内获得首个1美元赏金。

---

<h3>How I Discovered an Email Leak Vulnerability (and Got Rewarded).</h3><p>Hello hacker, good to see you in my blog 😄. I hope you are well. In this blog I’m gonna share. How I find email leak vulnerability and earned my first US Dollar bounty on VDP program.</p><p><strong><em>Well the story begins.</em></strong></p><p>One day one of my friend gave me this VDP program to try to find out the bug. As I was free. Then I tried to give an hand on that website. The website I was testing had many subdomains. And also, the main website is quite popular in the US. As I can’t disclose their name publically so I will say this site as an example.com. Moreover, the bug I found was email leaking of the user.</p><p><strong><em>How I found this critical bug.</em></strong></p><p>Firstly, I surfaced the website as an normal user. And checked the all functionality within it. What it was doing and where it was redirecting me when I click on specific link like that…</p><p>After looking for the functionality, immediately I moved to test those functionality. So, basically one of the functionality was the following, where I can follow and message the other user.</p><p>That’s where I found my valid bug. As I said I can follow or msg to other user. So, I decided to test that message function.</p><blockquote><strong><em>Steps to reproduce the vulnerability:</em></strong></blockquote><blockquote>&gt; First, follow the user and sent message to them.</blockquote><blockquote>&gt; Second, when you sent the message, capture that request (I used burp here).</blockquote><blockquote>&gt; Third, sent that request to the burp repeater.</blockquote><blockquote>And you will see the email which was leaking in the response.</blockquote><p>POC :-</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/306/1*XvpkCH3jZqnqgZA7SUIEDg.jpeg" /></figure><p>Immediately, I sent this vulnerability report with POC and within 24 hours they reply me and offered me some bounty for that.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*2lAhZuvbKI9HovwcBxj5Mw.jpeg" /></figure><p>Thanks for reading this blog till end 😊. I hope you gained some knowledge from this blog.</p><p>If you liked my blog you can show me some love by hitting clapp button 👏👏👏for as many times as you wish.</p><p>Have a good day. Happy hacking🙌🙌❤️❤️.</p><p>Here is my <a href="https://www.linkedin.com/in/deep-kachhadiya-aa8271310/">Linkedin</a> feel free to connect me.</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=4df50ee82fc6" width="1" />
