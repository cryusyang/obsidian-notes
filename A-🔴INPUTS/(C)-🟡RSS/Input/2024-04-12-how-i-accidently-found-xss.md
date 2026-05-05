---
title: "How I accidently found XSS"
url: "https://medium.com/@deepk007/how-i-accidently-find-xss-b349a0721ec9?source=rss-1646886baef5------2"
source: "DEep"
date: 2024-04-12
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文记录了一名网络安全研究员（Deep）意外发现某网站搜索参数存在反射型XSS漏洞的过程：他在尝试挖掘IDOR漏洞时，注意到URL中`cm=`参数的值会直接反射回页面，进而成功注入XSS payload并触发弹窗（如显示cookie）；进一步测试表明，该站点完全未对用户输入进行过滤或转义，甚至可嵌入任意HTML内容（如YouTube视频iframe）；作者强调了输入反射与缺乏输出编码是导致该漏洞的关键原因。

---

<p>HIII HACKERS, My name is Deep and I’m cybersecurity researcher and bug hunter. In this blog I’m gonna show you how I accidently find XSS(cross site-scripting)vulnerability in search parameter.</p><p>So let’s get started.</p><p>As I was surfing the site. That time my only motive was to look for the IDOR vulnerability. As we know there is also possibility of finding IDOR in the URL parameter by changing some key words like(ID=1,2). So I’ve done the same. I tried to change the number in the URL. But it didn’t work. Then I saw this cm=(it was in the URL) there I tried putting some random stuff like ‘hello’ or ‘testing’. So, those words was reflecting back to the page!!.</p><p>Then you know guys the game. I put XSS payload there and yeahh I got alert!</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*zMY9GHLrDV7SsOVXKR5PsQ.png" /><figcaption>XSS alert showing cookie</figcaption></figure><p>As I know this page was affected to XSS, so I tried some another types of payload to see how the application react. You can get all types of XSS payload from below link.</p><p><a href="https://github.com/payloadbox/xss-payload-list">GitHub - payloadbox/xss-payload-list: 🎯 Cross Site Scripting ( XSS ) Vulnerability Payload List</a></p><p>There I tried to test this payload to see how it was reacting.</p><p><strong>Payload:- </strong><strong>&quot;&gt;&lt;h1&gt;&lt;iframe width=&quot;420&quot; height=&quot;315&quot; src=&quot;http://www.youtube.com/embed/sxvccpasgTE&quot; frameborder=&quot;0&quot; allowfullscreen&gt;&lt;/iframe&gt;123&lt;/h1&gt;</strong></p><p>The payload is about adding youtube video in the site.</p><p>In the payload you can the change the width and height of the video as you like.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*XM39ZALvdlppc-EmC4-5Nw.png" /></figure><p>And yeahh, as you can see in the page I was able to add youtube video. It means that the site was not sanitizing user input at all.</p><p>So that’s it guys. If I’ve made any mistakes in my writing so let me know or if you have any question feel free to ask me.</p><p>Here is my <a href="https://www.linkedin.com/in/deep-kachhadiya-aa8271310/">linkedin</a> profile feel free to connect me.</p><p>If you like this blog you can show some love by hitting clap buttoooon or you can support me by buying me a coffee😋😋.</p><figure><a href="https://www.buymeacoffee.com/dEEpPatTel"><img alt="" src="https://cdn-images-1.medium.com/max/170/1*h3Jkg0WDTlsp7rUCPfWp0g.png" /></a></figure><p>Byy, happy hacking🙌</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=b349a0721ec9" width="1" />
