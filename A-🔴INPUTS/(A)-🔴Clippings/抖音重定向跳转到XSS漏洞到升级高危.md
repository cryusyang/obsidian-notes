### 正文

在 TikTok 上搜索时，我发现了一个常规的登录页面。我首先看了链接，没有找到任何有趣的参数。你正确登录以猜测重定向，然后将请求传递给入侵者以猜测重定向。

最终，我得到了一个不同的响应，是的，我发现了一个开放的重定向漏洞！

由于开放重定向的影响较低，我想要利用它达到更多的目的…… 是的，我知道你们在想着 XSS 漏洞。是的，你们猜对了，就是 XSS。

Payload 就像这样：

```
1javascript:alert(1)
```

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfQmwVficpLtib2jTLXu0ibgbkCmm4CibBd8C9W09RrgWiaamOyWicoIvrbA0w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

你以为我会停在这里吗！！！你错了，我总是尽力获取最高风险。继续搜索吧。

是的，我还发现了泄露敏感账户信息的端点，例如 user_info。这通常是一个包含账户信息的页面。

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfur9Y9HZ2tTVxab5T6qicrq8pTqNpgoJs0ZlngUL3KuiaibbIXcMhyNs0Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

例如，我们发现该端点在响应中检索到敏感信息。是的，我坐在那里思考着如何利用这个！我能获取这些信息吗？发送到我的服务器！

是的，是的，是的！我获取了所有这些信息，还遗漏了一些非常敏感的端点。

我们现在从跨站脚本攻击转向账户劫持，

我编写了一个 payload，使受害者访问端点，将页面内容保存在一个名为 data 的变量中，然后将其重定向到我的服务器，并附带数据。

这就是最终的利用过程：

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfLZqYua1LUjNBF0qdc61rU1RiaWichK2t1utNG7KwIvp2IPOwRKPibmc6A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfI7nGMTHmbUCKMT1PpJiaNibqGdshzIaiaYjo4593G97NI1mkO9x3RzczA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

漏洞利用的解释：

想象一下，它将受害者引导到端点，从而泄露了他的账户名，然后将其保存在一个名为 data 的变量中，然后将其带着数据重定向到你的服务器，你就可以成功捕获它。

所有的账户数据都已经被获取并完全被接管。

举例来说，这是一个泄露账户名的端点。正如你所见，它成功地捕获了数据。别忘了，我找到了一些非常敏感的端点，我不想透露它们。

这些是一些被捕获数据的图片，如你所见：

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfk7McuHjDUs4lFXb39YOq9SibPdJv9QMHaVmsbSFagkTldGtIyicWsEcA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

这里我在命令提示符上收到了 JSON 数据，正如你所见，一切都变得混乱了，因为命令提示符无法读取一些代码，所以我将使用本地主机。

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWf3wCq6JycibtPhMmfQzveTDhfxibJLib2k21cgmSicI0UZQHKyySmrdZeog/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWf3wCq6JycibtPhMmfQzveTDhfxibJLib2k21cgmSicI0UZQHKyySmrdZeog/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

![Image](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMogKV1gqHQt9YR1COMX5qWf3wCq6JycibtPhMmfQzveTDhfxibJLib2k21cgmSicI0UZQHKyySmrdZeog/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

我已经获取了包含所有参数的 Cookie，现在我可以入侵这个账户了 ^-^ 希望你喜欢这个故事，你已经看到了结局。感谢阅读。

我因此被奖励了 5000 美元。

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMogKV1gqHQt9YR1COMX5qWfDLSTtzNPETQnTnWBibwT9l6unrZtjjOjZqHibVf9sLwNkxV4nyYkdIibg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

Thanks for  source from
https://medium.com/@them7x/open-redirect-to-xss-and-account-takeover-ato-7ccd3a41d2a0

### 看法

你没看错，国内最好的奖励225RMB的反射XSS漏洞去到国外变成5000¥=3w5人民币，你在国内做这种漏洞利用极大可能还是当作反射XSS处理，之前某东SRC就有过能拿到姓名的反射XSS，所以平时很多时候自己并不会考虑去做这类利用，但是挖洞这种东西，都要试，遇到一个好的审核多一点是一点，自己也能学到东西。
