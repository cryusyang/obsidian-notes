---
title: "实测小米MiMo-V2.5-Pro，这可能是目前国内最适合Claude Code的新模型。"
url: "https://mp.weixin.qq.com/s/pUVdEqpvBdpV4FXyUw0jrw"
source: "数字生命卡茲克"
date: 2026-04-24
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 小米正式发布开源大模型MiMo-V2.5及Pro版本，在AA榜与Kimi K2.6并列开源第一，API调用价格具竞争力；作者实测其在复杂工程任务（如搭建公众号数据分析平台、自动部署至企业服务器、对接飞书认证与统一登录中台）中表现优异，远超部分国产模型，接近Opus 4.6水平；模型还成功处理了160万字《甄嬛传》的深度分析与可视化网页生成任务；但前端审美与UI生成能力仍有提升空间。

---

<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   昨天凌晨，没有任何预兆的情况下。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   小米的MiMo-V2.5和
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   上线了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWhia6jrMN47TdryGoNPH1mKjEibehsSg0Rsy045Dz9x7q1GljjdYdTeqEiabg3aO9PMhP8ibjOZ7XDGdT1K7Cib32MiceIABtwmWmgE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 591px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   API也已经正式上线。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最近不知道怎么了，各种大模型真的发的一个赛一个一个猛，上周Claude Opus 4.7，这周Kimi K2.6，昨天
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，还有姚顺雨带队的全新HY3，今天又发了GPT-5.5，估计马上还有DeepSeek V4。。。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个蓬勃的时代啊。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   MiMo的模型我其实一直都比较喜欢，自从罗福莉去了小米之后，肉眼可见小米的大模型水平在直线上升。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然，最关键的原因，还是是因为，我是十二年的米粉，还是喜欢很喜欢小米的设计和硬件的，甚至我全家的所有家电都是小米。。。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   不过在昨天下午试完
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   后，有一说一，这是我觉得，能跟GLM-5.1和Kimi k2.6掰掰手腕的模型，说实话，是有点超出我的预期的。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   正儿八经的可以跻身第一梯队的那种，群里很多开发也都在聊。
  </span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqXzHKriaSicTd5rqqKI2oYYibkTicictriayibOLEEruw6VTIMvZIMfFjia7UJrnADic98T68icwa00IszhpjEDNNcE6SLbpJNrIYO8zG5T8/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="width: 562px !important; height: auto !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还是老规矩，先来放一下跑分，不过也就大概看一眼就行，反而大家都是赢学。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在AA榜上，目前跟Kimi K2.6并列开源第一。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUea1l83e11rWog1cRicOu2hBZMoGTVDhyrb2tl9Ap4NINialpkEic0SczYqDk213pE3CvMuOoYHd0Gxj1B5h9oyUvLAGyIaTOeM4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   成绩很不错，跑分上，也比自家之前进步不少。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUakpZxrKWaicJE8uqBwuF5ztBtibSYvg4VAicEu6SeLTicErCTZ6yibWFsu8Jeuf3p1gFobicPRl6YPG1Er7ibjicP9PYCgy6UgjEVicP0/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后上下文窗口很香，是100万，感觉现在百万的上下文已经成为各大模型的标配了，今天发的GPT-5.5也支持了1M上下文。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后就是价格方面，这块我其实一般都是放在最后提，但是这次，一定得放在前面，因为真的性价比很高，而且估计刚出没有多少人用，接了API之后，那速度是真快啊。。。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   不像有些国产模型，都能干到延迟好几秒。。。
  </span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   通过API key调用的价格是，在0到256k token内，是¥7/¥21每百万token（输入/输出）。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在256k到1M token内是¥14/¥42每百万token（输入/输出）。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXVN51nFAXHCrVJblJXh1SzuYupTicDbl7H7182tsZkjOlc6at0ibygSiaBdpP6qX8Ahs5XFnhgDTJLfmm2p4RwJqg4XmPBlx3mDQ/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Opus 4.6这块，是$5/$25每百万token（输入/输出）。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   大概能便宜60%左右。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   除了API之外，MiMo这次也出了新的Token Plan，也不区分256K和1M上下文，统一收费。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWeiaQp14xmEEkY0v8ZrwlEy7rkzTJGFlXib7J6T5PX1FiaxCrb623qvumoWT9YKiaMMxQhawuOs8xjdnq9YICsg2ARjJ1aRF4cTyo/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=5" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个价格，我坦诚的讲，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   挺良心了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我自己测试下来，其实工具调用和Coding开发能力，意外的还不错，非常像那个味道，而且，说人话。。。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我是在Claude Code里面用的，相信我，Claude Code +
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，是我现在非常非常推荐的国内Agent组合，很多朋友不是抢不到智谱的Coding Plan，用不到GLM-5.1吗，你相信我，此时此刻，用
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   Claude Code +
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   就是我觉得目前效果最好的组合。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   便宜大碗省token，效果还很好，关键现在没啥人用，速度还贼快。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我自己虽然依然还是会选择Coding用Claude Opus 4.7，知识创作用Claude Opus 4.6的组合，但是我知道，并不是每个人都能用上Claude的，甚至GPT都用不上，去装个Claude Code +
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   的组合，非常的丝滑。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   怎么装Claude Code，以及怎么通过cc-switch在Claude Code里接国产大模型，我周一发过
  </span>
  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA==&amp;mid=2647681650&amp;idx=1&amp;sn=ebe9c3f89ede3094c532f47dcd495081&amp;scene=21#wechat_redirect" target="_blank">
   <span style="font-size: 16px;">
    Claude Code国内使用的保姆级教程
   </span>
  </a>
  <span style="font-size: 16px;">
   ，我就不细说了，还没用的朋友可以去翻一下。
  </span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那在周一那篇教程之上，我们想把模型换成这个新的，操作也不复杂。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们双击打开cc-switch。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   在Claude下，点击右上角的加号。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUZaPqiaxBRehayv2fudsiasQRxAugRkUia9u6OZzGbhudWDWvibVP5icGhfKWRatVdfiaD5XhvpflqqJmenUJ3lFRu6Q7CzQ9iaYk1UI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=6" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   供应商选择Xiaomi MiMo，然后填入API Key。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXgTHIzicKDpNEFcHHj60vwQS5SsxO4lfHGWusriaJjHp7fA2mvEQBsY7DibAEIvQHA4kYWfIEicehn8dFZZySBFyzibHT0TKVwEQVY/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=7" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   模型名填上mimo-v2.5-pro。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXjUUuv6U1zhOSQD06LLTzSe9laVczO1q5CRiaRHuzK59JfIpOG336ibE4rDUtyvDVek875tZn48njR7GD4PxW0Nplfpe83O8eCA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=8" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   添加，在首页启用之后，打开Claude Code，就可以直接用上了。
  </span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXkOrCZUI24jicSngr36TLlTRATZKksymrd7avdGaXDgJmsV8AZfqJOy44I2Xy6lM0fQZoLyDx2IzrLS1umPzT5NlDAtTibpu2Xk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=9" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   给大家看一个，我下午测试，自己通过MiMO搓的还挺满意的一个case。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就是我一直有个想法，想自己做一个更好用的公众号文章数据分析平台。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你们知道的，我一直觉得，文章创作不是发出去就完事的，读者的反馈超级无敌至关重要。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   到现在，我们的公众号已经发了612篇文章了，也积累了很多很多的数据反馈。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   虽然公众号后台有现成的数据分析工具，但对我们来说是不够用的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   首当其冲，它给的数据分析指标很有限，肉眼去看只能看个大概趋势。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVWVicp3APAibfT8F6G8jBw5VFGiaSFXBVgazmGSgibGVqtJKDkw2KLhzEIu0yZXupBPUqV5GGTqH1kicYKbRVdR0jrqDkxRicXcicjR8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=10" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们自己也是去抓了更详细的数据，之前也给大家看过，我们的那张数据分析表。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUuPKs79v9xVtayaYZ4e724MicK4TLew8pLoZ66AibkSBkVo94H0zBnYxGriaFTRy13dlzrhvTSlI0DDicUq0mCzpAAZIM2p7tNpiaM/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=11" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但咋说呢，数据的分析和洞察，还是太少了，而且每次看的我头疼，密密麻麻的数据太多了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我一直想的是，能不能有一种更好的方式，把这些数据量化，然后从里面挖出一些可能被我们忽略的趋势，或者信号。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   比如这周一发的Claude Code保姆级教程那一篇，我对他的数据是很看好的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   刚发出来的阅读量和转发率也确实不错。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   一个小时的转发就有近7000次。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但后续的数据显然动力就不足了，增长得相当缓慢。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那我们肯定就需要复盘，除了平台流量的因素之外，还有没有什么原因，才有了这样的问题。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   之前一直就想搓一个这样的网站，直接把飞书多维表格当数据库，然后网页做数据分析，再部署上到我们自己的服务器上，做好企业权限管理，给我们公司的小伙伴一起看。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以正好就借着
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   的发布，看看能做成啥样。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我就直接在Claude Code里直接开着语音输入法直接口喷。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUKPyYKZicN9gchxspMXCBUCUf3kepOE17NWflnrz0RtJRIhKicMrxyrHZyniaEZ4HpYuClCd6obNaA1icnMO951BnAjtLxzk6xbys/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=12" style="width: 572px !important; height: auto !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后他就根据我说的这一堆，开始非常有条理地逐个输出。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   先给了我技术栈，架构设计。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXQoxdpN3icaKnLOUgzssfYXhxSHqC5rMSPrJUt9rcfa8IzS99Zht9iaE9LZyHjcKbVqzItCOySTYrfHcZDAjNW4Xadqk6lBRFVg/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=13" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后是数据分析逻辑，包括我提到的指标体系，转发加速曲线，对比基线。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVPjbRaibUgteIbgicMzasWvHYLrBg2wVNBAO2pXsPhkdMNUPBnYBKZvR9BIolNmHHoZicBbHpYIeD1ASquc9RibUss4abHdW8mUico/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=14" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后又输出了项目结构，页面设计，实现步骤，验证方式和清单等等等等究极详细的方案。。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUILvkJgUKQ23KOGNuZv4X1QiaJ2p1RicUEKJkWE7sd8mSSSicKFO9s0qTQN8l8PrRaoNqiaS93uDjFZrM6aF55SJcW2qBmDZqJT58/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=15" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说真的，我跟
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   对话的时候，莫名其妙的，有一股子Opus 4.6的感觉。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说人话，给图表，真好啊。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后就直接开发了，过程我就不放了，大概就是每天脚本定时请求我们飞书数据库，然后拿到最新的数据，做可视化分析。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最后，出来的是这么个东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为我们的数据分析是要看三日的完整数据来进行分析，所以这里显示的最新的文章还是周一的那一篇。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVBZ2wAoib6NUDGkK59oiaNqTDCLuaOzA28ibJiaGjdJJVhn6mn5u8U18Zp7vxxViakz7myFBbCNLXHadQDCs5OXJxFNNz9kPvfa09g/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=16" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   你能非常快速并且直观地看到这篇文章各项的数据分布。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   那明显这一篇文章的短板数据主要还是在完读率上面，以及它的转发率是很明显到后面动力不足的。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   教程类的文章，转发出去的多，但是真正会看的少，更别提会看完的了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还有他的核心指标的分布。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这篇文章在我们过去所有的核心指标上都有怎样的表现，也是一目了然。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqVfn99zMcOAWhFcdpIia3LzjerRUdQCXr9NR8WvZJ1HjZiclM9ZxVhViaiaUKoN1kHeH4whO2EqmiaJx0kFSWjqcx7z9Ao2e2xJYb64/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=17" style="width: 578px !important; height: auto !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还会生成一篇单独的报告。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWT7wKheibY1085lGzcjgEWjCQTLryiaKia7QUhIC6rBO9lbXE3kQwBiaOcCZv3Iqkicqa8SjwK4ssAgBAQhUmXNN7XM5PbKGibaiaMUI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="height: auto !important; width: 648px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   每篇文章的诊断报告也非常全面，不仅告诉你好的地方在哪，还有不太好的数据背后的原因是什么，以及可以改进的地方是什么。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还有我们的周报看板，展开后是这个样子，能够非常快速地看到过去四周发的每一篇文章的基本数据。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWQI2ATmw3HrjBm97pykI1p94E3ia380eGt1vVm8b2iaQHVKq92IokeT031cLOlOhcSmZ6hicqlebL1ccaZ1ER8ftHPMOh69AQgV4/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=19" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这个任务，到这里还没完。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   因为它还是静态的页面，我们公司的小伙伴，还是没办法访问。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   后面，我还让他调用我自己给公司搓的服务器skill，把这个网站部署到了我们内部的服务器上。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说实话，我这个服务器skill还是比较复杂的，因为跟飞书的认证做了打通，只有公司的小伙伴才能用，还有无数的隔离，让大家的项目要跑在不同的容器里。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说实话，笨一点的模型，这个首次部署流程，都搞不定，我真的试过用一些国产的XX模型，真的，就部署这一步，直接失败了。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   正常走了用户首次的部署逻辑，需要进行认证，跟飞书企业对比，看看是不是我们公司的员工。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqUmRMZlu898LNKzdD65okgFjt67WH3KkQV0fg6wu89Qjz3iaxRepEicl7ia69ecad2VB8HpA5MxncIV3aXq7FROD5T5QVhBmX9jj4/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=20" style="width: 578px !important; height: auto !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   Mimo的理解和调用过程也非常丝滑，我把验证码给他后，按部就班的所有步骤，就成了，非常牛逼。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqU7mAnlLuowm3GyibxicACuvvMQ3BZuHAO9FlEKgnmX4PPiaicM5FmV2nicpRKj3vSwwun16YG4Yo4kDYLZx0CvExoF8gQsTybZ7YBE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=21" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后这一步还是没完，因为上一步卡的是部署权限，但是部署上去的网址，其实所有人都可以公开访问的，这肯定不是我们想要的，应该只有公司员工才能访问才对。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   于是，我又把我Coding的给内部用的统一登录中台，也给它街上，这样就能进行登录权限管控了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXyZiaibDC03hBW4XGcY4bibqf9IVfzmwwnqoaiaJWcIJGkQVmF6uYTX0Y0KTxzIoVicBZ862tIhRRrQ2VABUUWG9rOtHPibTUPLQb28/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=22" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们中台上我放了一个接入文档，因为平时我们小伙伴Coding的乱七八糟的东西太多了，每个人都有部署和管控登录权限的需求，所以我就搞了这么一个文档，他们把文档链接发给Claude Code，就能把这个项目自动接入到我们的统一登录中台里面。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqXQusIafkLMvPUkxmiaKpBy6iaarTHGbXkGernXgGIuEzp8icObff0zWZrhIrdUuQiatvZMhBeUr43lKTMeskz7qJcGl1mSFmcA3Fs/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=23" style="width: 578px !important; height: auto !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这文档东西真的挺多的，因为还分了好多种方式和渠道，还要同步用户信息等等乱七八糟的东西，我们还有三家飞书主体，每个权限还都不一样，笨一点的模型，我在测试的时候，真的经常接出BUG。。。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，一轮，没有任何修改，直接接完了。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVP0aJOkPuWUvC3H5rdRsqibpHyFt6CPGrxYZYHdfJiaKwFGalGibsicKOFHkcousvxgWic9lQIa2mml3icXWFChW9XPMAmX7SfQ6QBE/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=24" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我让同事试了一下，没毛病。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVWKGXvlXfRINsSKWMy7xklibFXaAujw95umZgns9xJ6hoB71O7WBqULa9r6iauuVoAE7UbqcDRFyFlhufIXhGyAD9eAGMQbpibUs/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=25" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUrhYQMMwQjcY6yGlMAD0DKevnB6yqW08mY0JCic9AqTd7piaEFZ02y8pNAZapiapBZRwQVS1iaYia5icJet76FEQKzMghjD2QU9ic5Cc/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=26" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUupSIYHUXYnaRjpyjIpQeVNZemd7URxG3hdicFaiat3O7dzY4CfvhPX9AzYehUmhhiat6bwMQaicX7ic44JZvc23qE1BdG3GmDxO2w/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=27" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  然后，到这一步，我看了一下整体的消耗。
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWZianqRnuarMxje6LibUSicbzCJekw28sHOErDXTqibviaJyoydicg0FFUsuqDDlcok15bEV2Ad2wJHMrJCP3F2l3icvbJtzs5Jar20w/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=28" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   1.2M的输出，157.1K的输出，缓存命中了29.6M，缓存现在还是限时免费，所以消耗还意外的少。
  </span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   说实话，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，是有点东西的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   飞书数据通过飞书CLI一次拿到，正常开发，我的服务器skill一次部署成功，登录中台一次性接入成功，很帅。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我们公司我还搓了一个skills同步平台，因为有很多同时自己都会搞各种各样的skill，也会经常分着用，但是以前的分发效率太低下了，都是在微信上互相穿skill，太呆了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我就搓了个这么个东西，能让大家把skill都上传上去，其他人可以订阅，订阅了以后本地就会安装那个skills，以后线上一更新，订阅者本地就会跟着更新，非常的方便。
  </span>
 </span>
</p>
<section style="text-align: center; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWtzFJr8OOiavZibq0dB2uMws5AQnSwRAcceZwSKicsUZ2wRTyVB8RibmaSniaArVI3Ptkr4DzMHvgXicqv3DHDjPcUM2jKqliadFUs4A/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=29" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   今天其实才第一次正式运行，之前是Opus 4.6开发的有一些BUG我就搁置了，然后，今天这些BUG，都是MiMo V2.5 Pro直接修好的。。。
  </span>
 </span>
</p>
<p style="margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   甚至打标签、加头像之类的各种乱七八糟的功能，也都是我用MiMo V2.5 pro直接开发的。
  </span>
 </span>
</p>
<section style="text-align: center; margin-bottom: 24px; margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVibCvpxOFqlMzTd4wCgTeias8fdvmE4w7UXUz7LfZxXtmNHEOlGqHY2ajAibxUfhBOkZlJyURpDLBdnJQRnY9c5icaiaGWsnR4FoxI/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=30" style="height: auto !important; width: 664px !important;" />
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   是真的有点东西。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   然后还有个很好玩的。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   我把160万字的甄嬛传丢给了
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，让他分析人物关系图，情节线，人物志，最后做了个可交互的网页。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   为了好看，我还让他去搜电视剧演员的剧照换上。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWzrJ0ic1Rgg4AAwm9SrJaRD3HS4f4GFeHicxYmpafdJKPmNVGJ8C97xAnAtsSRUTkntuTvtshCNvf4KQa1jU2JLY141GtFoZwW8/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=31" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最后的网页还挺有意思，你能快速清楚整部剧每个重要角色，每个人物之间的关系。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUDOYNsG374XeyJkq7mFMvxU4EUm5MjfTRHtt3UNl7ZIKMuASRxXfcePmWaEM1icmugAHFXmxg1ichPsmopGO4jFaoSvbL6bia8Sk/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=32" style="height: auto !important; width: 664px !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   还有时间线，各个人物阵营。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/2jjfQoZLoqUoeegeEPK6WblY9GsXmsYiaRJhfXZOffqicX2pL5IkVDgSWdOiaos8we8Q1XOr1ULnhic6X8cOwXzLMRXiahnlqFKGHvWB7GFMgCrM/640?wx_fmt=jpeg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=33" style="width: 578px !important; height: auto !important;" />
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   真的很好玩。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   当然，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro又有个
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   缺点，就是前端审美的能力，确实还没赶上模型其他方面的能力。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   所以一开始在生成页面的时候，会有那么一点劝退。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   出来的视觉效果，说实话就是能用两个字，谈不上什么设计感，还是得配上一些前端设计的Skill，这个点跟GPT-5.4和5.5啥的真的就很像。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   但是我感觉无伤大雅，前端设计有很多能弥补的点，但是很多逻辑类和代码类的东西，这个才是核心。
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   就目前来说，
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   MiMo-V2.5-Pro
  </span>
 </span>
 <span>
  <span style="font-size: 16px;">
   ，确实就是我觉得配合Claude Code的国内最好的模型之一。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   这种窗口期我觉得不会太长，等大家都反应过来了，速度可能就没这么快了，plan计划可能也不一定好买了。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   最后，祝大家。
  </span>
 </span>
</p>
<p style="margin-left: 8px; margin-right: 8px;">
 <span>
  <span style="font-size: 16px;">
   创造愉快。
  </span>
 </span>
</p>
<p>
 <span style="letter-spacing: 0.578px; font-size: 15px;">
  <strong>
   <strong style="letter-spacing: 0.544px;">
    <strong>
     <span>
      <span>
       以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～谢谢你看我的文章，我们，下次再见。
      </span>
     </span>
    </strong>
   </strong>
  </strong>
 </span>
</p>
<p>
 <span>
  <span>
   &gt;/ 作者：卡兹克、tashi
  </span>
 </span>
</p>
<p>
 <span>
  <span>
   &gt;/ 投稿或爆料，请联系邮箱：
  </span>
  <span>
   wzglyay@virxact.com
  </span>
 </span>
</p>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px;">
 <span>
 </span>
</section>
<section style="margin-left: 8px; margin-right: 8px; margin-bottom: 0px;">
 <span>
 </span>
</section>
<p style="display: none;">
 
 
</p>
