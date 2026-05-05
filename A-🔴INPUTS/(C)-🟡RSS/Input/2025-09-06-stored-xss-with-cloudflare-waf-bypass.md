---
title: "Stored XSS with Cloudflare WAF Bypass"
url: "https://hexaphp.medium.com/stored-xss-with-cloudflare-waf-bypass-420c99aba97b?source=rss-c4f7ec62144d------2"
source: "Aland Dlshad (HexaPhp)"
date: 2025-09-06
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 文章描述了一次针对Cloudflare防护网站的存储型XSS测试过程：作者首先通过HTML标签确认输入未被前端正确编码，随后发现Cloudflare WAF拦截了标准XSS载荷，但通过大小写混用和重复事件属性等简单混淆技巧成功绕过WAF，触发了弹窗。核心问题在于后端未对用户输入进行输出编码，导致恶意脚本在页面渲染时执行。结论强调：再强大的WAF也无法弥补后端缺乏输入验证和输出编码的安全缺陷。

---

<p>While testing a site protected by <strong>Cloudflare</strong>, I came across some input fields that appeared to be storing user data. Naturally, I wanted to check if the stored data was being rendered unsanitized in the frontend.</p><p>So, I started simple — a basic HTML injection to confirm output was being reflected. I submitted:</p><p><strong>&lt;u&gt;Aland Dlshad&lt;/u&gt;</strong></p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*q1NMaHdlCLl6boflAaX07Q.png" /></figure><p>And sure enough, it rendered just like that. ✅<br /> This told me the input wasn’t being properly encoded or sanitized before being displayed — definitely a red flag.</p><p>Next, I tried a classic stored XSS payload:</p><p><strong>&lt;img src=x onerror=alert(1)&gt;</strong></p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*ynkR6W4jJP7y-YaQ01Hc_A.png" /></figure><p>But this time, <strong>Cloudflare’s WAF blocked the request</strong>, showing a 403 error. So I knew I’d need to get creative if I wanted to bypass it.</p><p>After trying a few different obfuscation techniques, I landed on this payload:</p><p><strong>&lt;img src=OnErRor OnErRor=(alert)(“Aland_Dlshad__HexaPhp”)&gt;</strong></p><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*5qOGyAnS9Dumm8b63as1WA.png" /></figure><p>To my surprise — it worked.</p><p>No WAF block, and the alert popped clean when the stored input was rendered. ✅<br /> Looks like the mixed casing and duplicated onerror attributes confused Cloudflare's WAF, allowing the payload to slip through. The backend didn't sanitize the data, so the browser just executed it.</p><h3>💡 Takeaway</h3><p>Cloudflare caught the obvious stuff — but <strong>it doesn’t matter how strong your WAF is if your backend blindly trusts user input</strong>. Stored XSS was possible because of poor output encoding, and the WAF was bypassed with minor tweaks.</p><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=420c99aba97b" width="1" />
