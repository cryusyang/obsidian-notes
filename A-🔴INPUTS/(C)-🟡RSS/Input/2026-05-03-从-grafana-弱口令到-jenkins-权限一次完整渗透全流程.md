---
title: "从 Grafana 弱口令到 Jenkins 权限，一次完整渗透全流程"
url: "https://mp.weixin.qq.com/s/wnYHHcw61BxbYfIGCp3hfw"
source: "神农Sec"
date: 2026-05-03
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文是一篇结合实战案例与课程推广的技术文章：首先以渗透测试中通过Grafana弱口令→目录遍历→AKSK泄露→Jenkins备份包获取→credentials.xml密码解密为线索，详细复盘了Jenkins凭据破解的完整链路与Java解密实现方法；其次重点推介“神农SRC漏洞挖掘实战课”，涵盖SRC、CNVD、EDUSRC等平台漏洞挖掘、红蓝对抗、JS逆向、代码审计等内容，强调真实项目驱动、永久回看、社群支持等特色；最后附有知识星球资源更新、往期技术干货回顾及合法合规声明。

---

<section>
 <section style="color: rgb(62, 62, 62); font-size: 16px; background-color: rgb(255, 255, 255); margin-bottom: 0px;">
  <section style="padding-right: 10px; padding-left: 10px; line-height: 1.6;">
   <section>
    <section style="padding-right: 30px; padding-left: 30px; line-height: 1.6;">
     <p>
      <span>
       <br />
      </span>
     </p>
    </section>
   </section>
  </section>
 </section>
 <section style="color: rgb(62, 62, 62); background-color: rgb(255, 255, 255); margin-bottom: 0px;">
  <section>
   <section>
    <section style="padding-right: 10px; padding-left: 10px; line-height: 1.6;">
     <section>
      <section>
       <section>
        <section>
         <section>
          <section>
           <p>
            <span>
             课程培训
            </span>
           </p>
          </section>
          <section>
           <p>
            <span>
             扫码咨询
            </span>
           </p>
          </section>
         </section>
         <section>
          <p>
           <span>
            <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwdGRmjj1FjibCj8Ay917FPEXPpqUjZjpF13feHYK8qnmRL1dteolSmvRQ/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" />
           </span>
          </p>
         </section>
        </section>
       </section>
       <section>
        <section>
         <span>
          <img src="https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp#imgIndex=1" />
         </span>
        </section>
       </section>
      </section>
     </section>
     <section>
      <section>
       <section>
        <section>
         <section>
          <section>
           <section>
            <section>
             <span>
              <br />
             </span>
            </section>
           </section>
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
     <h1>
      <span>
       <br />
      </span>
     </h1>
     <p>
      <span>
       专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。
      </span>
     </p>
     <h1>
      <span>
       <br />
      </span>
     </h1>
     <section style="padding-right: 10px; padding-left: 10px; line-height: 1.6;">
      <p>
       <span>
        <span>
         文章作者：大反派
        </span>
       </span>
      </p>
      <p>
       <span>
        <span>
         文章来源：
        </span>
        <span>
         https://zone.huoxian.cn/d/2873-jenkins
        </span>
       </span>
      </p>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section style="margin-bottom: 16px; margin-top: 16px;">
  <section style="display: flex; padding-right: 12px; padding-left: 12px;">
   <section style="display: flex;">
    <section>
     <p style="font-weight: bold; font-size: 16px; color: rgb(255, 255, 255); line-height: 38px;">
      <span style="font-size: 18px;">
       <span>
        01
       </span>
      </span>
     </p>
    </section>
    <section style="width: 100%; text-align: center; font-weight: bold; font-size: 18px; color: rgb(51, 51, 51);">
     <span style="font-size: 18px;">
      <span>
       0x1 从 Grafana 弱口令到 Jenkins 权限，一次完整渗透全流程
      </span>
     </span>
    </section>
   </section>
  </section>
 </section>
 <section>
  <h3 style="margin: 30px 0px 15px; padding: 0px; display: flex;">
   <span style="font-size: 20px; color: rgb(53, 179, 120); line-height: 1.5em; letter-spacing: 0em; font-weight: bold; display: block;">
    <span>
     0x01 背景描述
    </span>
   </span>
  </h3>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin: 0px; padding: 8px 0px;">
   <span>
    在一次渗透测试过程中，首先发现了Grafana弱口令，登录进去发现了存在存储桶目录，访问存储桶发现存在目录遍历，里面发现存在jar包，打开jar包，发现存在AKSK，通过AKSK获取存储桶权限，通过存储桶信息收集，发现存在Jenkins备份包。
   </span>
  </p>
  <h3 style="margin: 30px 0px 15px; padding: 0px; display: flex;">
   <span style="font-size: 20px; color: rgb(53, 179, 120); line-height: 1.5em; letter-spacing: 0em; font-weight: bold; display: block;">
    <span>
     0x02 信息收集
    </span>
   </span>
  </h3>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin: 0px; padding: 8px 0px;">
   <span>
    下载源码
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJHAZAhyNVOkzPjq1nibwicX40hIbUuXxPe5uyDXLbXaDZdws2CcmlMkbg/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=3" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin: 0px; padding: 8px 0px;">
   <span>
    通过在网上搜索信息，发现credentials.xml存放密码文件 打开发现
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJR90lBVwbXktSUWwbupdibCnpL8t3Diaf0dnXRj7zgk7vlRzBv5bHkWwQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=4" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJAQypEsQa7Xp32IqxzS58pL0SHtov7UNfcib6ocZiarVYSOJnZhaaVUrg/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=5" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    确实存在一行加密的密码字段。
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    然后理所应当的就思考，思考尝试解密
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    “遇事不决，可问春风”
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ1IvWPX82OaL7bMTRJFUgJw1gdYBXy3ak577acNGqfXCHpcgyT3u5Sg/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=6" style="display: block; margin: 0px auto; height: auto !important; width: 192px !important;" />
    然后根据网上找到的策略
   </span>
  </p>
  <h3 style="margin-top: 30px; margin-bottom: 15px; margin-left: 0px; margin-right: 0px; padding-top: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; display: flex;">
   <span style="font-size: 20px; color: rgb(53, 179, 120); line-height: 1.5em; letter-spacing: 0em; font-weight: bold; display: block;">
    <span>
     0x03 方法策略
    </span>
   </span>
  </h3>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <strong>
    <span>
     1.搭建环境，通过脚本命令行，进行查看所有凭据。
    </span>
   </strong>
  </p>
  <pre><code><span>com.cloudbees.plugins.credentials.SystemCredentialsProvider.getInstance().getCredentials().forEach{ it.properties.each { prop, val -&gt; println(prop + </span><span style="color: #98c379; line-height: 26px;"><span>' = "'</span></span><span> + val + </span><span style="color: #98c379; line-height: 26px;"><span>'"'</span></span><span>) } println(</span><span style="color: #98c379; line-height: 26px;"><span>"-----------------------"</span></span><span>) }</span><br /></code></pre>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    借用网上的图，这一步我自己搭建的环境有问题哈哈哈
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ74rQJt1VkMlammxkWrzrmn4vIRKhLWD4nfiaJMbChVwEnPA6Q6VjgfQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=7" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    或者可以手动获取凭据
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJRBpxeiafoJiavddZrvhfdhkKQ7N5BzRbGqSeY9pccrJBHZpt67azZUFw/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=8" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    然后通过脚本命令行进行解密
   </span>
  </p>
  <pre><code><span>println(hudson.util.Secret.fromString(</span><span style="color: #98c379; line-height: 26px;"><span>"{刚刚复制的加密密码}"</span></span><span>).getPlainText())</span><br /></code></pre>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJHXRafvOCWmf8nsRDzBZ31NLXibaRWOGj8qHcicZEvhg4zEzOpkcTAOXQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=9" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    但是实际搭建环境，运行出错,这里思考两点，可能版本不对，但是我换了3个版本出错，有明白的大佬，欢迎评论指出，向大佬学习。
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJicmKfoVwtAWtEo5Cms8GA30OLwF47TuoYPhQpOib6qtdR5Oc1HZ4JUVw/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=10" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJK6UxlbnUTHZH2m9IA9MNXOXXlIicT5IhzM54MfQFvPV2zjsST3KsShQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=11" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <strong>
    <span>
     2.然后就开始了换一种方式，编写解密代码，进行解密
    </span>
   </strong>
   <span>
    首先我们要搞清楚需要那些文件
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    通过上面1进行解密的语句，已经网上查找，都是通过调用credentials.xml、masterkey 、shudson.util.Secret这三个文件
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    credentials.xml，存放密码hash的地方 masterkey，需要key存放，进行匹配 shudson.util.Secret，组件调用
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    进行idea选择项目，选择mvean项目
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJB9OEHwDSM1nMJBeThzWHUTjChDEdkvX1SLvljUYVqsBibTibhKHNO0bg/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=12" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    然后运行会发现缺少依赖包，在pom.xml，查看是否写入依赖
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJKAJLTrOtibedwVr7Rl3M5nGEK7MFcNHJHkQqOzLtIIsLhKYaMvGtfgQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=13" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJqvheNByBZHLDoM7wnNHZdf69wmy2H6AFvKdXw2iclhmQZXpOUVs6G7g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=14" style="display: block; margin: 0px auto; height: auto !important; width: 380px !important;" />
   </span>
  </p>
  <pre><code><span>package com.Jenkins;</span><br /><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> org.apache.commons.io.IOUtils;</span><br /><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.BadPaddingException;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.Cipher;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.CipherInputStream;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.SecretKey;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.spec.IvParameterSpec;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> javax.crypto.spec.SecretKeySpec;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.io.*;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.nio.charset.StandardCharsets;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.nio.file.Files;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.security.GeneralSecurityException;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.security.MessageDigest;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.security.NoSuchAlgorithmException;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.security.SecureRandom;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.util.Arrays;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>import</span></span><span> java.util.Base64;</span><br /><br /><span>importstatic java.nio.charset.StandardCharsets.UTF_8;</span><br /><br /><br /><br /><span>publicclassTestMain {</span><br /><br /><span>privatestaticfinalStringKEY_ALGORITHM=</span><span style="color: #98c379; line-height: 26px;"><span>"AES"</span></span><span>;</span><br /><span>privatestaticfinalStringALGORITHM=</span><span style="color: #98c379; line-height: 26px;"><span>"AES/CBC/PKCS5Padding"</span></span><span>;</span><br /><span>privatefinalStringrootDir=</span><span style="color: #98c379; line-height: 26px;"><span>"C:\\Users\\xxx\\JenkinsDecode\\secrets"</span></span><span>;//目录</span><br /><br /><span>privatestaticfinalbyte[] MAGIC = </span><span style="color: #98c379; line-height: 26px;"><span>"::::MAGIC::::"</span></span><span>.getBytes();</span><br /><span>// 密文密码</span><br /><span>privatestaticfinalStringdata=</span><span style="color: #98c379; line-height: 26px;"><span>"{密码文本就是credentials.xml中的}"</span></span><span>;</span><br /><br /><span style="color: #61aeee; line-height: 26px;"><span>@org.junit.Test</span></span><br /><span>publicvoiddecrypt() {</span><br /><span>byte[] payload;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>try</span></span><span> {</span><br /><span>            payload = Base64.getDecoder().decode(data.substring(</span><span style="color: #d19a66; line-height: 26px;"><span>1</span></span><span>, data.length()</span><span style="color: #d19a66; line-height: 26px;"><span>-1</span></span><span>));</span><br /><span>        } catch (IllegalArgumentException e) {</span><br /><span style="color: #c678dd; line-height: 26px;"><span>return</span></span><span>;</span><br /><span>        }</span><br /><span>switch (payload[</span><span style="color: #d19a66; line-height: 26px;"><span>0</span></span><span>]) {</span><br /><span>case1:</span><br /><span>// For PAYLOAD_V1 we use this byte shifting model, V2 probably will need DataOutput</span><br /><span>intivLength= ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>1</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>24</span></span><span>)</span><br /><span>                        | ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>2</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>16</span></span><span>)</span><br /><span>                        | ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>3</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>8</span></span><span>)</span><br /><span>                        | (payload[</span><span style="color: #d19a66; line-height: 26px;"><span>4</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>);</span><br /><span>intdataLength= ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>5</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>24</span></span><span>)</span><br /><span>                        | ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>6</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>16</span></span><span>)</span><br /><span>                        | ((payload[</span><span style="color: #d19a66; line-height: 26px;"><span>7</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>) &lt;&lt; </span><span style="color: #d19a66; line-height: 26px;"><span>8</span></span><span>)</span><br /><span>                        | (payload[</span><span style="color: #d19a66; line-height: 26px;"><span>8</span></span><span>] &amp; </span><span style="color: #d19a66; line-height: 26px;"><span>0xff</span></span><span>);</span><br /><span style="color: #c678dd; line-height: 26px;"><span>if</span></span><span> (payload.length != </span><span style="color: #d19a66; line-height: 26px;"><span>1</span></span><span> + </span><span style="color: #d19a66; line-height: 26px;"><span>8</span></span><span> + ivLength + dataLength) {</span><br /><span>// </span><span style="color: #c678dd; line-height: 26px;"><span>not</span></span><span> valid v1</span><br /><span style="color: #c678dd; line-height: 26px;"><span>return</span></span><span>;</span><br /><span>                }</span><br /><span>byte[] iv = Arrays.copyOfRange(payload, </span><span style="color: #d19a66; line-height: 26px;"><span>9</span></span><span>, </span><span style="color: #d19a66; line-height: 26px;"><span>9</span></span><span> + ivLength);</span><br /><span>byte[] code = Arrays.copyOfRange(payload, </span><span style="color: #d19a66; line-height: 26px;"><span>9</span></span><span>+ivLength, payload.length);</span><br /><span>                String text;</span><br /><span style="color: #c678dd; line-height: 26px;"><span>try</span></span><span> {</span><br /><span>                    text = newString(decrypt(iv).doFinal(code), UTF_8);</span><br /><span>                    System.out.println(</span><span style="color: #98c379; line-height: 26px;"><span>"密码明文:"</span></span><span> + text);</span><br /><span>                } catch (GeneralSecurityException e) {</span><br /><span>                    System.out.println(</span><span style="color: #98c379; line-height: 26px;"><span>"1111111111111"</span></span><span>);</span><br /><span>// it</span><span style="color: #98c379; line-height: 26px;"><span>'s v1 which cannot be historical, but not decrypting</span><br /><span>return;</span><br /><span>                }</span><br /><span>//                return new Secret(text, iv);</span><br /><span>default:</span><br /><span>return;</span><br /><span>        }</span><br /><span>    }</span><br /><br /><span>public Cipher decrypt(byte[] iv) {</span><br /><span>try {</span><br /><span>Ciphercipher= getCipher(ALGORITHM);</span><br /><span>            cipher.init(Cipher.DECRYPT_MODE, getKey(), newIvParameterSpec(iv));</span><br /><span>return cipher;</span><br /><span>        } catch (Exception e) {</span><br /><span>thrownewAssertionError(e);</span><br /><span>        }</span><br /><span>    }</span><br /><br /><span>privatesynchronized SecretKey getKey()throws Exception {</span><br /><span>SecretKeysecret=null;</span><br /><span>try {</span><br /><span>byte[] payload = load();</span><br /><span>if (payload == null) {</span><br /><span>                payload = randomBytes(256);</span><br /><span>//                    store(payload);</span><br /><span>            }</span><br /><span>// Due to the stupid US export restriction JDK only ships 128bit version.</span><br /><span>            secret = newSecretKeySpec(payload, 0, 128 / 8, KEY_ALGORITHM);</span><br /><span>        } catch (IOException e) {</span><br /><span>throw e;</span><br /><span>        }</span><br /><span>return secret;</span><br /><span>    }</span><br /><br /><span>protectedbyte[] load() throws Exception {</span><br /><span>try {</span><br /><span>Filef=newFile(rootDir,"hudson.util.Secret");</span><br /><span>if (!f.exists())</span><br /><span>returnnull;</span><br /><span>Ciphersym= getCipher("AES");</span><br /><span>            sym.init(Cipher.DECRYPT_MODE, getMasterKey());</span><br /><span>try (InputStream fis= Files.newInputStream(f.toPath());</span><br /><span>CipherInputStreamcis=newCipherInputStream(fis, sym)) {</span><br /><span>byte[] bytes = IOUtils.toByteArray(cis);</span><br /><span>return verifyMagic(bytes);</span><br /><span>            }</span><br /><span>        } catch (Exception x) {</span><br /><span>if (x.getCause() instanceof BadPaddingException) {</span><br /><span>throw x; // broken somehow</span><br /><span>            } else {</span><br /><span>throw x;</span><br /><span>            }</span><br /><span>        }</span><br /><span>    }</span><br /><br /><span>publicstatic Cipher getCipher(String algorithm)throws GeneralSecurityException {</span><br /><span>return Cipher.getInstance(algorithm);</span><br /><span>    }</span><br /><br /><span>private SecretKey getMasterKey()throws Exception {</span><br /><span>Filefile=newFile(rootDir,"master.key");</span><br /><span>SecretKeymasterKey= toAes128Key(read(file).trim());</span><br /><br /><span>return masterKey;</span><br /><span>    }</span><br /><br /><span>public String read(File file)throws Exception {</span><br /><span>StringWriterout=newStringWriter();</span><br /><span>PrintWriterw=newPrintWriter(out);</span><br /><span>BufferedReaderin= Files.newBufferedReader(file.toPath(), StandardCharsets.UTF_8);</span><br /><span>        String line;</span><br /><span>while ((line = in.readLine()) != null)</span><br /><span>            w.println(line);</span><br /><span>return out.toString();</span><br /><span>    }</span><br /><br /><span>publicbyte[] randomBytes(int size) {</span><br /><span>byte[] random = newbyte[size];</span><br /><span>newSecureRandom().nextBytes(random);</span><br /><span>return random;</span><br /><span>    }</span><br /><br /><span>privatebyte[] verifyMagic(byte[] payload) {</span><br /><span>intpayloadLen= payload.length-MAGIC.length;</span><br /><span>if (payloadLen&lt;0)   returnnull;    // obviously broken</span><br /><br /><span>for (int i=0; i&lt;MAGIC.length; i++) {</span><br /><span>if (payload[payloadLen+i]!=MAGIC[i])</span><br /><span>returnnull;    // broken</span><br /><span>        }</span><br /><span>byte[] truncated = newbyte[payloadLen];</span><br /><span>        System.arraycopy(payload,0,truncated,0,truncated.length);</span><br /><span>return truncated;</span><br /><span>    }</span><br /><br /><span>publicstatic String toHexString(byte[] bytes) {</span><br /><span>intstart=0;</span><br /><span>intlen= bytes.length;</span><br /><br /><span>StringBuilderbuf=newStringBuilder();</span><br /><span>for( int i=0; i&lt;len; i++ ) {</span><br /><span>intb= bytes[start+i]&amp;0xFF;</span><br /><span>if(b&lt;16)    buf.append('</span></span><span style="color: #d19a66; line-height: 26px;"><span>0</span></span><span style="color: #98c379; line-height: 26px;"><span>');</span><br /><span>            buf.append(Integer.toHexString(b));</span><br /><span>        }</span><br /><span>return buf.toString();</span><br /><span>    }</span><br /><br /><span>publicstatic SecretKey toAes128Key(String s) {</span><br /><span>try {</span><br /><span>// turn secretKey into 256 bit hash</span><br /><span>MessageDigestdigest= MessageDigest.getInstance("SHA-256");</span><br /><span>            digest.reset();</span><br /><span>            digest.update(s.getBytes(StandardCharsets.UTF_8));</span><br /><br /><span>// Due to the stupid US export restriction JDK only ships 128bit version.</span><br /><span>returnnewSecretKeySpec(digest.digest(),0,128/8, "AES");</span><br /><span>        } catch (NoSuchAlgorithmException e) {</span><br /><span>thrownewError(e);</span><br /><span>        }</span><br /><span>    }</span><br /><br /><span>}</span><br /></span></code></pre>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    这段代码使用了Java的加密库进行解密操作。它包含了以下几个重要方法：
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    decrypt(): 这个方法根据所传入的密文数据进行解密操作。它首先解码密文数据，并根据数据的第一个字节确定数据的版本。然后，根据不同的版本格式进行解析，并在解密完成后将明文输出到控制台。
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    getCipher(): 这个静态方法返回一个指定算法的Cipher对象。 getKey(): 这个方法根据存储的密文数据加载或生成密钥对象。 load(): 这个方法从文件中加载存储的密文数据，并进行解密操作。 getMasterKey(): 这个方法从master.key文件中读取并转换为AES密钥对象。 toAes128Key(): 这个静态方法将字符串形式的密钥转换为128位的AES密钥对象。 所有都准备完毕，单击运行!!!
   </span>
  </p>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJaVvGTUHQk9o3ib21XibILC3qPMasJINxOqb5OUGBlxDL8BTw5QTPObgQ/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=15" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
    使用破解的密码进行登录，通过脚本命令行获取命令执行权限
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJVicedrydTazn2SM5VxWVFb77rMCibKa5V4bR7uvg5joTuYIP2JatThww/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=16" style="display: block; margin: 0px auto; height: auto !important; width: 636px !important;" />
   </span>
  </p>
  <h3 style="margin-top: 30px; margin-bottom: 15px; margin-left: 0px; margin-right: 0px; padding-top: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; display: flex;">
   <span style="font-size: 20px; color: rgb(53, 179, 120); line-height: 1.5em; letter-spacing: 0em; font-weight: bold; display: block;">
    <span>
     0x04 思考总结
    </span>
   </span>
  </h3>
  <p style="color: rgb(89, 89, 89); font-size: 15px; line-height: 1.8em; letter-spacing: 0.04em; text-align: left; text-indent: 0em; margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; padding-top: 8px; padding-bottom: 8px; padding-left: 0px; padding-right: 0px;">
   <span>
    1.遇见信息泄露，慢慢翻，慢慢看 2.思考如何利用已知的东西，进行深入 3.”遇事不决，可问春风“！！
   </span>
  </p>
  <section style="color: rgb(62, 62, 62); font-size: 16px;">
   <section style="padding-right: 10px; padding-left: 10px; line-height: 1.6;">
    <section>
     <section style="padding-right: 30px; padding-left: 30px; line-height: 1.6;">
      <section>
       <section style="margin-top: 16px; margin-bottom: 16px;">
        <section style="padding-right: 12px; padding-left: 12px; display: flex;">
         <section style="display: flex;">
          <section>
           <p style="font-weight: bold; font-size: 16px; color: rgb(255, 255, 255); line-height: 38px;">
            <span style="font-size: 18px;">
             <span>
              02
             </span>
            </span>
           </p>
          </section>
          <section style="width: 506.172px; text-align: center; font-weight: bold; font-size: 18px; color: rgb(51, 51, 51);">
           <span>
            0x2 培训课程介绍
           </span>
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
   <section>
    <section>
     <section>
      <section>
       <section>
        <section>
         <section>
          <p>
           <span>
            26
           </span>
          </p>
         </section>
        </section>
       </section>
       <section>
        <section>
         <p>
          <strong>
           <span>
            SRC漏洞挖掘培训课程
           </span>
          </strong>
         </p>
        </section>
       </section>
       <section>
        <section>
         <section>
          <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWntMzgEX5Cg3eMeMYyMicjFelJ9hKMWHZB8C8F6biaJnibBdRibt76K0fkDKjxqPEibWdwTtrr4UxFbzESSdggD0yuos5bLIvveg1Q/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;watermark=1&amp;tp=webp#imgIndex=4" />
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
   <section>
    <section>
     <section>
      <section>
       <section>
        <section>
         <section>
          <p>
           <span>
            <br />
           </span>
          </p>
         </section>
        </section>
       </section>
      </section>
     </section>
     <section>
      <section>
       <section>
        <section>
         <section>
          <p>
           <strong>
            <span>
             <span>
              1.课程价格目前是475（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！
             </span>
            </span>
           </strong>
          </p>
          <p>
           <strong>
            <span>
             <span>
              2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨
             </span>
            </span>
           </strong>
          </p>
          <p>
           <strong>
            <span style="color: rgb(123, 12, 0);">
             3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️
            </span>
           </strong>
          </p>
          <p>
           <strong>
            <span style="color: rgb(123, 12, 0);">
             4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！
            </span>
           </strong>
          </p>
          <p>
           <strong>
            <span style="color: rgb(123, 12, 0);">
             <span>
              5.上课结束后，会把视频录播+课件笔记一起打包发直播群！
             </span>
            </span>
           </strong>
          </p>
          <p>
           <strong>
            <span style="color: rgb(123, 12, 0);">
             <span>
              6.哔哩哔哩SRC课程公开课，链接🔗直达：
             </span>
            </span>
           </strong>
          </p>
          <p>
           <span style="text-decoration: underline;">
            <strong>
             <span>
              <span style="color: rgb(123, 12, 0); text-decoration: underline;">
               https://space.bilibili.com/642258933
              </span>
             </span>
            </strong>
           </span>
          </p>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
 <section>
  <p>
   <span>
    <span>
     SRC课程详情🔎：
     <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247505805&amp;idx=1&amp;sn=d3bb65bef6d6021bb923516b585abc06&amp;scene=21#wechat_redirect" target="_blank">
      神农SRC 漏洞挖掘实战课：从 0 到 1 成
     </a>
    </span>
    <span style="display: none; line-height: 0px;">
     <span>
      <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247505805&amp;idx=1&amp;sn=d3bb65bef6d6021bb923516b585abc06&amp;scene=21#wechat_redirect" target="_blank">
       ‍
      </a>
     </span>
    </span>
    <span>
     <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247505805&amp;idx=1&amp;sn=d3bb65bef6d6021bb923516b585abc06&amp;scene=21#wechat_redirect" target="_blank">
      为赏金猎人
     </a>
    </span>
   </span>
  </p>
  <section>
   <span>
    内部小圈子知识星球详情🔎：
    <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247504561&amp;idx=1&amp;sn=c2cd5f397b84ab059dd36e19fe31d428&amp;scene=21#wechat_redirect" target="_blank">
     强烈推荐一个永久的SRC挖掘、渗透攻防内部知识库
    </a>
   </span>
  </section>
  <section>
   <span>
    <span>
     欢迎关注微信公众号：神农Sec，报名咨询添加微信：
    </span>
    <span>
     <span>
      routing_love
     </span>
    </span>
   </span>
  </section>
  <section>
   <span>
    <span>
     <img src="https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QUvSBhpC6JhFAqdrGasexh04noxBGEmeLIpQlD6Fv7CYUYHWEEdN0zhkDw9Isu5TEUe5ADjtJXu10Es6Ypha0WNibzMDr4vvibcg/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=6" />
    </span>
   </span>
  </section>
  <section>
   <span>
    开课三个月时间左右
   </span>
   <span>
    <span>
     ，课程目前已经
    </span>
   </span>
   <span>
    累计加入了664个学员
   </span>
   <span>
    <span>
     了，课程培训招生任火热持续中，师傅们
    </span>
   </span>
   <span>
    <span>
     对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名
    </span>
   </span>
   <span>
    <span>
     。
    </span>
   </span>
   <span style="text-align: center; letter-spacing: 0.034em;">
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVCaRNXrEhlzeFrMQw5ywiaS96MXAzUBD7ZbDicINicotpHwhNbz58WiasjaPiaWwPzP1JtRDONz3wYb4ZDxQDzTs6UKAiaceIfMdiaWk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=18" style="height: auto !important; width: 632px !important;" />
   </span>
  </p>
  <section>
   <span>
    课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家
    <span style="background-color: rgb(255, 251, 0);">
     交流氛围很好
    </span>
    ！
   </span>
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QU9v2xct94514W9NKvbWvDUagnooSLHxEYmvNq4MPicxgLGDGNuumP4fQQ8iatd1H8OxFfR8lkAcQFlIibZzPCVmjyVVlRdYYrjrg/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=18" />
  </section>
  <section>
   <span>
    课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪怕是课件笔记都没有的，我这里都是下课第一时间把
    <span style="background-color: rgb(255, 251, 0);">
     录播+笔记
    </span>
    打包发给大家！
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVhfiaB0CTupQOeqIz9prmqTMQ1RxW3KTjLT2BRhyxeYYEaibmtNB0z0RoFaG3xmwRGqU1Q1mibWfSw3gWfUCofx3Zn2daRicrJQbE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=20" style="height: auto !important; width: 632px !important;" />
   </span>
  </p>
  <section>
   <span>
    平常也都会给学员进行一些项目发布，包括后面的
    <span style="background-color: rgb(255, 251, 0);">
     工作、护网内推
    </span>
    等，经常上麦交流，大家互相学习，简历优化等。
   </span>
  </section>
  <section>
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWk53sibBzE8ZA4ibE9ib51tRSRPlg6akhNsYELOFtPAwMphMHBnoibiauj0t8jQC7ovVzv2h49TfoAZFX8WhtW7LibCsrp7PtRalX94/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=20" />
   </span>
  </section>
  <section>
   <span>
    <span>
     SRC漏洞挖掘课程培训已经两个星期了，期间也是创建了
     <span style="background-color: rgb(255, 251, 0);">
      “回本小群”
     </span>
     ，希望学员回本越来越多，创建这个群主要是鼓励学员学习进步，以及不定时发小项目！
    </span>
   </span>
  </section>
  <p>
   <span>
    <span>
     最后也是希望大家都可以赚钱，找到好工作🎉
    </span>
   </span>
  </p>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWdM3sY0h7vAyNWvMOncW5DLj9MFq32wz2bB5mqTIy9TDmwDQb4SHmCKUytrbngznZyKFzbibpJ5KV4TyHickRRPNH28WkYlZiaXc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=22" style="height: auto !important; width: 632px !important;" />
   </span>
  </p>
  <section>
   <span>
    培训时间不长，感谢🙏师傅们的
   </span>
   <span>
    <span>
     喜报
    </span>
   </span>
   <span>
    ，很开心看到师傅们给我分享自己的成果，
   </span>
   <span>
    <span>
     希望师傅们越来越强！
    </span>
   </span>
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWwO4dHVOg5icypiayskiamLkRHMkphVbH6EnGOfMJD42Iu4gmSk9nf9nLicH8Rytqkj897Y4bap4DEgtibj1uibcIkwojKCTFUqCCwQ/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=22" />
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVHSvhy6ib3STPv1ojMISexeMdGzxIhJhXIxe3DEB1rLbloGSl0ZdaneiaMrXt3BbkQWTmgASX2iaR8xWlafKicO0OOvLfnQvMFsZ8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=24" style="height: auto !important; width: 632px !important;" />
   </span>
  </p>
  <section>
   <span>
    <br />
   </span>
  </section>
  <section>
   <span>
    平常也会分享项目，下面是一些
   </span>
   <span>
    <span>
     学员项目成果
    </span>
   </span>
   <span>
    ，群里报课的学员都是不抽成的，主要是帮助学员进行
   </span>
   <span>
    <span>
     回本
    </span>
   </span>
   <span>
    ，
   </span>
   <span>
    <span>
     让大家都可以进步！
    </span>
   </span>
  </section>
  <section>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QULyrm18wkZfgzKexpR72ocoraossY0sV8Dhsc3mblwuTzicNafx0T4K3uibfEXgTwkofymJOdYlY7zXJSrUBIJYoIFvMh5oGJnI/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=23" />
  </section>
  <p style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px; width: 100%;">
   <span style="text-decoration: underline;">
    <span>
     上课结束后，会把
    </span>
    <span style="text-decoration: underline; background-color: rgb(255, 251, 0);">
     <span>
      视频录播+课件笔记
     </span>
    </span>
    <span>
     一起打包发直播群
    </span>
   </span>
  </p>
  <p>
   <strong>
    <span>
     <span>
      「神农安全」
     </span>
    </span>
   </strong>
   <span>
    <span>
     知识星球目前已经
     <span style="background-color: rgb(255, 251, 0); font-weight: bold; text-decoration: underline;">
      累计2000+
     </span>
     网络安全爱好者的加入！
    </span>
    <span>
     <br />
    </span>
   </span>
  </p>
  <p>
   <span>
    后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想着给大家教下src漏洞挖掘思路，所以自己花了很长时间做了✨
    <span style="font-weight: bold;">
     课件和课表
    </span>
    ，都是纯自己手搓的，大家也可以看下课表的内容。
   </span>
  </p>
  <section style="text-align: center;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwdeMaEjjraFy3Gtk4wIfs8X3ARPfaoQ0vDLdWFZPSZGOXuORPwAdnibTA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=26" style="background-color: transparent; height: auto !important; width: 632px !important;" />
  </section>
  <section style="text-align: left;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV5nozwxnKfmkQ32ssaeFATDicPkYRrEickJJbB75L9DsFGSf883VLicvV2iaKBWKvmNzO01mmr0micPZt8NXC5sY3ST7FtoNpC9yrE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=27" style="letter-spacing: 0.034em; text-align: center; height: auto !important; width: 632px !important;" />
  </section>
  <section style="width: 100%; background-position: 0% 0%; background-size: 375px 198px; padding: 2px 12px;">
   <section style="margin-bottom: 16px; margin-top: 16px;">
    <section style="display: flex; padding-right: 12px; padding-left: 12px;">
     <section style="display: flex;">
      <section>
       <p style="font-weight: bold; font-size: 16px; color: #FFFFFF; line-height: 38px;">
        <span style="font-size: 18px;">
         <span>
          03
         </span>
        </span>
       </p>
      </section>
      <section style="width: 100%; text-align: center; font-weight: bold; font-size: 18px; color: rgb(51, 51, 51);">
       <span>
        0x3 课程特色
       </span>
      </section>
     </section>
    </section>
   </section>
  </section>
  <p>
   <span style="font-size: 15px;">
    课程
    <span style="font-weight: bold;">
     主打真实
    </span>
    ，
    <span style="font-weight: bold;">
     一线SRC漏洞挖掘
    </span>
    师傅是如何学习和挖掘SRC漏洞的，让你真正了解SRC漏洞挖掘，助力在岗人员和大学生的能力提升，掌握新的技能树，为下一次
    <span style="font-weight: bold;">
     跳槽涨薪
    </span>
    做好准备。本
    <span style="font-weight: bold;">
     课程内容
    </span>
    覆盖企业
    <span style="background-color: rgb(255, 251, 0); font-weight: bold;">
     SRC、众测项目挖掘、护网HVV红蓝攻防技巧、CVE、CNVD、EDUSRC
    </span>
    等平台通杀案例技巧挖掘方法。
   </span>
  </p>
  <p style="text-align: center;">
   <span style="font-size: 15px;">
    <span style="font-weight: bold;">
     <span>
      本课程
     </span>
    </span>
    <span style="color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
     <span>
      适合人群
     </span>
    </span>
    <span style="font-weight: bold; background-color: rgb(255, 251, 0);">
     <span>
      （光看不挖啥也不会）
     </span>
    </span>
   </span>
  </p>
  <section>
   <ul class="code-snippet__line-index code-snippet__js">
    <li>
    </li>
    <li>
    </li>
    <li>
    </li>
   </ul>
   <pre class="code-snippet__js"><code><span>1、想从0转行入行的大学生或自学者</span></code><code><span>2、想从CTF比赛/Web或SRC进阶到项目实战的选手</span></code><code><span>3、想参与项目/找工作/提高收入的转型者</span></code></pre>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px; color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
    课程价格：475元
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px; font-weight: bold;">
    报课成功的师傅们直接免费送内部小圈：一个知识星球+内部小圈子交流群
   </span>
  </section>
  <section>
   <ul class="code-snippet__line-index code-snippet__js">
    <li>
    </li>
    <li>
    </li>
    <li>
    </li>
    <li>
    </li>
   </ul>
   <pre class="code-snippet__js"><code><span><span>1</span>、课程价格真心实惠，绝不割韭菜</span></code><code><span><span>2</span>、两三百的课程价格让你体会大几千的培训课程内容</span></code><code><span><span>3</span>、带着大家从0到1，本人上课坚持手搓课件（实战案例+知识体系）</span></code><code><span><span>4</span>、拒绝使用PPT演讲模式（无实操，很枯燥）</span></code></pre>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px; color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
    直播培训教学方式
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <span style="font-size: 15px;">
    课程
    <span style="background-color: rgb(255, 251, 0); font-weight: bold;">
     一周1-2节课
    </span>
    ，课程特色涵盖直播多人上麦活跃回答，直播过程中有问题随时解决或私信我。
    <span style="font-weight: bold;">
     拉微信群：一个知识星球内部小圈子交流群+课程培训直播通知群
    </span>
    。有项目/工作/护网第一时间内推报课的师傅，
    <span style="font-weight: bold;">
     一对一简历优化
    </span>
    ，助力在岗人员和大学生的能力提升。
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <span style="font-size: 15px;">
    <span style="background-color: rgb(255, 251, 0);">
     一次报名每期均可永久学习
    </span>
    ，并且赠送内部「神农安全」知识星球，一对一永久解答、无保留教学！
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px;">
    <span>
     欢迎关注微信公众号：神农Sec，报名咨询添加微信：
    </span>
    <span style="color: rgb(255, 76, 65); font-weight: bold; font-size: 16px;">
     <span>
      routing_love
     </span>
    </span>
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px;">
    <span>
     课程均为线上交付，报名成功后
    </span>
    <span style="color: rgb(255, 76, 65); font-weight: bold; font-size: 16px;">
     <span>
      不支持退款
     </span>
    </span>
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px;">
    <span style="color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
     内部小圈子
    </span>
    <span style="font-weight: bold; text-decoration: underline;">
     （知识星球+内部小圈子交流群+知识库）
    </span>
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <span style="font-size: 15px;">
    对内部小圈子感兴趣的师傅们也可以看下下面的这个
    <span style="background-color: rgb(255, 251, 0); font-weight: bold;">
     跳转链接
    </span>
    ，里面有对小圈子的详细介绍，报名课程成功的师傅们直接免费送一个（直接点击下面直接可以跳转）。
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <span>
    <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247501608&amp;idx=1&amp;sn=5eb836122ac222ca9767a7bbc3c4521b&amp;scene=21#wechat_redirect" target="_blank">
     <span style="background-color: rgb(255, 251, 0);">
      强烈推荐一个永久的SRC挖掘、渗透攻防内部知
     </span>
    </a>
   </span>
   <span style="display: none; line-height: 0px;">
    <span>
     <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247501608&amp;idx=1&amp;sn=5eb836122ac222ca9767a7bbc3c4521b&amp;scene=21#wechat_redirect" target="_blank">
      <span style="background-color: rgb(255, 251, 0);">
       ‍
      </span>
     </a>
    </span>
   </span>
   <span>
    <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247501608&amp;idx=1&amp;sn=5eb836122ac222ca9767a7bbc3c4521b&amp;scene=21#wechat_redirect" target="_blank">
     <span style="background-color: rgb(255, 251, 0);">
      识库
     </span>
    </a>
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXibesoNgoI04vDm8Kop2y7N6geicKajUcVHkhf9c4K4vPG2jib4nBL78PeofkYBt3utI2DsAmetYz0V8DOIia27VhThV3CjX1gUSk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=28" style="height: auto !important; width: 632px !important;" />
   </span>
  </p>
  <p style="text-align: center;">
   <span style="font-size: 16px; color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
    讲师介绍
   </span>
  </p>
  <p style="text-align: center;">
   <span style="font-size: 15px; font-weight: bold; font-style: italic;">
    id：一个想当文人的黑客
   </span>
  </p>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwdAOFx9We2Z1icUT3iblm1eWyCujwz1F2uKzIzBVlMfqwj9tRzBFbMpzpQ/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=29" style="height: auto !important; width: 632px !important;" />
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="font-size: 15px;">
    <span>
     欢迎关注微信公众号：神农Sec，报名咨询添加微信：
    </span>
    <span style="color: rgb(255, 76, 65); font-weight: bold; font-size: 16px;">
     <span>
      routing_love
     </span>
    </span>
   </span>
  </section>
  <section style="margin-bottom: 16px; margin-top: 16px; text-align: center;">
   <span style="color: rgb(255, 76, 65); font-weight: bold; font-size: 16px;">
    <span>
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwdGRmjj1FjibCj8Ay917FPEXPpqUjZjpF13feHYK8qnmRL1dteolSmvRQ/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=30" />
    </span>
   </span>
  </section>
  <section style="width: 100%; background-position: 0% 0%; background-size: 375px 198px; padding: 2px 12px;">
   <section style="margin-bottom: 16px; margin-top: 16px;">
    <section style="display: flex; padding-right: 12px; padding-left: 12px;">
     <section style="display: flex;">
      <section>
       <p style="font-weight: bold; font-size: 16px; color: #FFFFFF; line-height: 38px;">
        <span style="font-size: 18px;">
         <span>
          04
         </span>
        </span>
       </p>
      </section>
      <section style="width: 100%; text-align: center; font-weight: bold; font-size: 18px; color: rgb(51, 51, 51);">
       <span>
        0x4 第一期挖洞培训课表内容
       </span>
      </section>
     </section>
    </section>
   </section>
  </section>
  <section style="text-align: center;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwdCYyJ1XhJxqtcDOMYxlEiaeXWibTb9eia0liciaFfwQy3HHFCACIcAT0ibdqg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=31" style="width: 554px !important; height: auto !important;" />
  </section>
  <section style="text-align: center;">
   <section style="display: inline-block; vertical-align: top; width: auto; height: auto;">
    <section>
     <section>
      <span>
       <br />
      </span>
     </section>
     <section>
      <span>
       <br />
      </span>
     </section>
     <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 25px; height: auto;">
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp#imgIndex=32" style="vertical-align: middle; width: 25px !important; height: auto !important;" />
     </section>
    </section>
   </section>
   <section style="padding-right: 10px; padding-left: 10px; display: inline-block; vertical-align: middle; width: auto; height: auto;">
    <section style="margin-top: 10px; margin-bottom: 10px;">
     <section style="display: inline-block; vertical-align: top;">
      <section>
       <p>
        <span style="font-size: 20px;">
         <strong>
          <span style="font-size: 18px;">
           <span>
            内部圈子介绍
           </span>
           <span style="color: rgb(255, 76, 65);">
            <span>
             （报课赠送）
            </span>
           </span>
          </span>
         </strong>
        </span>
       </p>
      </section>
      <section style="width: 135.986px; height: 10px; background-color: rgb(255, 216, 216);">
       <svg viewBox="0 0 1 1" xmlns="http://www.w3.org/2000/svg">
       </svg>
      </section>
     </section>
    </section>
   </section>
   <section style="display: inline-block; vertical-align: bottom; width: auto; height: auto;">
    <section style="line-height: 0;">
     <section style="vertical-align: middle; display: inline-block; line-height: 0; width: 30px; height: auto;">
      <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp#imgIndex=33" style="vertical-align: middle; width: 30px !important; height: auto !important;" />
     </section>
    </section>
    <section style="line-height: 0;">
     <span>
      <br />
     </span>
    </section>
    <section style="line-height: 0;">
     <span>
      <br />
     </span>
    </section>
    <section style="line-height: 0;">
     <span>
      <br />
     </span>
    </section>
   </section>
  </section>
  <p>
   <span style="font-size: 15px;">
    <strong>
     <span>
      <span>
       圈子专注于更新
      </span>
     </span>
     <span>
      <span>
       src/红蓝攻防
      </span>
     </span>
     <span>
      <span>
       相关：
      </span>
     </span>
    </strong>
   </span>
  </p>
  <section style="letter-spacing: 0.578px;">
   <section>
    <ul class="code-snippet__line-index code-snippet__js">
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
     <li>
     </li>
    </ul>
    <pre class="code-snippet__js"><code><span>1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例</span></code><code><span>2、知识星球专属微信“小圈子交流群”</span></code><code><span>3、微信小群一起挖洞</span></code><code><span>4、内部团队专属EDUSRC证书站漏洞报告</span></code><code><span>5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）</span></code><code><span>6、分享src挖掘技巧tips</span></code><code><span>7、不定期有众测、渗透测试项目（一起挣钱）</span></code><code><span>8、不定期有工作招聘内推（工作/护网内推）</span></code><code><span>9、送全国职业技能大赛环境+WP解析（比赛拿奖）</span></code><code><span>10、十个专栏会持续更新~提前续费有优惠，好用不贵很实惠</span></code><code><span>11、每日内部资料分享，内部圈子资料1000+</span></code><code><span>12、联系圈主获取：内部漏洞知识库+圈子使用手册+内部圈子交流群</span></code><code><span>13、VX：routing_love，技术交流+疑问解决</span></code></pre>
   </section>
   <p>
    <span>
     <br />
    </span>
   </p>
  </section>
  <p style="letter-spacing: 0.578px; text-align: center;">
   <span style="font-size: 18px;">
    <strong>
     <span>
      内部圈子
     </span>
    </strong>
   </span>
   <span style="font-size: 18px; text-decoration: underline; color: rgb(255, 76, 65);">
    <strong>
     <span>
      专栏介绍
     </span>
    </strong>
   </span>
  </p>
  <p style="letter-spacing: 0.578px; text-align: center;">
   <span style="font-size: 15px;">
    <span>
     知识星球内部共享资料截屏详情如下
    </span>
   </span>
  </p>
  <p style="letter-spacing: 0.578px; text-align: center;">
   <span style="font-size: 15px;">
    <span>
     （只要没有特殊情况，每天都保持更新）
    </span>
   </span>
  </p>
  <section style="clear: both; text-align: center;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXW4rg28schFP5MQU8U9icwduCoowVw4ZdkMlIQKWdMkEibjmfJKD4vUib3Uia8blEibRdiajHdN3QUcWfw/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=34" style="height: auto !important; width: 632px !important;" />
  </section>
  <section style="clear: both; text-align: center;">
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWGaAUXovAf4ZRQFibbxRdJWVUicibE46ic1XqEibeiawaOPLx27lm14pvOFBibc8mWGrNRicnlic8gicaJrsvbiaFvFOUibmTjU8PvlczIkfc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=35" style="font-family: Optima-Regular, PingFangTC-light; letter-spacing: 0.578px; text-align: center; background-color: rgb(255, 255, 255); height: auto !important; width: 632px !important;" />
  </section>
 </section>
 <section>
  <section style="margin-bottom: 16px; margin-top: 16px;">
   <section style="display: flex; padding-right: 12px; padding-left: 12px;">
    <section style="display: flex;">
     <section>
      <p style="font-weight: bold; font-size: 16px; color: #FFFFFF; line-height: 38px;">
       <span style="font-size: 18px;">
        <span>
         05
        </span>
       </span>
      </p>
     </section>
     <section style="width: 100%; text-align: center; font-weight: bold; font-size: 18px; color: rgb(51, 51, 51);">
      <span>
       0x5
      </span>
      <span style="letter-spacing: 0.578px; float: none; display: inline !important;">
       <span>
        优秀学员报喜
       </span>
      </span>
     </section>
    </section>
   </section>
  </section>
  <section style="letter-spacing: 0.578px; text-align: left;">
   <span style="font-size: 15px;">
    下面是最近两个月培训期间，很多
    <span style="font-weight: bold; text-decoration: underline;">
     优秀学员进行报喜
    </span>
    ，看到师傅们有收获，也是感到很开心的！
    <span style="background-color: rgb(255, 251, 0);">
     拉回本小群
    </span>
    ，就是为了促进大家学习，在群里发学员成果，也是为了让大家学习优秀的师傅们。
   </span>
  </section>
  <section style="letter-spacing: 0.578px;">
   <span style="font-size: 15px; color: rgb(255, 76, 65); font-weight: bold; text-decoration: underline;">
    加油，你我皆是黑马！
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QULyrm18wkZfgzKexpR72ocoraossY0sV8Dhsc3mblwuTzicNafx0T4K3uibfEXgTwkofymJOdYlY7zXJSrUBIJYoIFvMh5oGJnI/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=23" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWeBH2XUxySpZmYIbBABuZSJZKyVhezWmhOyficAIer9HWiaBanmkDN4ia6h3LrXKIcmNQRDDdicSDJe3S381Cia1e6yDj3asEOwWhU/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=37" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QU4icyoqiblesXM6R7s9fYrm1gnPR4OiaxQfBzQb7urF9UB4LOGACqCxTyyTyAZRE4nBwAQky1ooyYSxnjyFkIN7ulsMSo6xrk5x8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=38" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWVciboHxIP1Lp3fbYc0H9PNDd43vlj9NlhcsMaKs51PnXe5W6l11UK4apC3Yq4pUyOVDvE98gDX26FickoGGNvKHunOJAFP4tgg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=39" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWuFwcsgTxA2q7oDRvQMia5CMt9aIyTFwGSpClwLSUc11669VJK5V3SLnrkTiaM7eLAGzpynv2ukRDelt1GzQQv7hhpfQAlsXbbk/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=40" />
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVW2DuLKQGvVzZicFSXP2ot4QwhXG31nEib8m9NlF1rV6iatN3fI30myIWl2sPz4jicLBULSNBHBWtMjc04JRgYT88nYS0Q2HF7ibk8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=41" />
   </span>
  </p>
  <p style="text-align: center;">
   <span>
    <br />
   </span>
  </p>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXndoMOgITS3yvJZCSIw3PSicic6It740RSYULOqa6NGv3UFdyibbZUca2J6odF01JEia9Mb8Xc03cxDByZbOMS74F50vsPibHeGDEs/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=42" />
   </span>
  </p>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVwHvOpvbuG4rOcktNiarHaDmYLK8EEicVA9eRhMrQ9YavGjm2UpDdfOhQCT7tyQcibn8PJ9gtg2HibemibB6Rqdv0WUS85W35bwBK4/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=43" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUhZOChrw7b0E4xvRVbIHEp8auQ6DndCibPoBrrnXhtibXibcuficR5a9IyAsRz9mt37BdTSaftJ2YPXDePAL2VhmrWRSaxun9xVxM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=44" />
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUK5ad0uW5nap0nftIcnC1iaMtgeDjfVhPJAxC8oEeJ6XzvPN1qhpWuR2xY4xiasCKuedlkhKibiaf7D0H7BSecE7FnrrrTmcluJM8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=45" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUmRvEAajoBGKKOh1PFnHudiaicv5jkckfPjg0d9bc6SKhJsQHRDYwOcIMrPNibOKnQAnOReEJUKusYZea3zFUrcOlDLpSjYic2IHM/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=46" />
   </span>
  </section>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUyDGEpXVHho53tliccXeOvJXvML9iadNYyJDNY5FG658iaqQGJRBfhLxHiaDUzkptsmgwlU4jY9okenaevWAibeXuDdbTohO4ib7Y9Q/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=47" />
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV0epFsicbJrNPgGwNXcXRCDrC1sGQySI2ylkfs2Hdic6d6unjwqNiby5DfhtfT6ezabX13bNeR53pOW3BUqLaZrIvPM8Z4IsBpgI/640?wx_fmt=png&amp;from=appmsg#imgIndex=48" />
   </span>
  </p>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXRMLib7hwarma7KgEntjVdFEw3cibKGaWckjCTKKEZopwkALuzDOgTRZSibfkhDNJdfxia0Iz4x4r5gn9BZ8xghhC7mAZ8bQPWdv8/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=49" />
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXXFDmlUtpJ2SWXlHIKBzM67uezQyGgjbxOQsia6TlnRddGzIz5hLS1GSFviaqezbU76toSM5fpbnlJqicQOdxfbdLfXAXGNG70AE/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=50" />
   </span>
  </p>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXiaKGBEDawQianoUyDia2D47b0yV30NnWfUG3gbh5BhN5cPR8aYLMynkN7d3oibiazykJgpsrkRL27eSHN8wfCyVBpqddq33QZhVss/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=51" />
   </span>
  </section>
  <p style="text-align: center;">
   <span>
    <img src="https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUDwL44R20Lv23VCY6vrwSkKGicUj2MR4Tibd5fBe67iazCVplHkItgiaXqjvkJGDqg6JYFmAIMHDWffHrC0SKXmuWe3o5EkfnGPUc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=52" />
   </span>
  </p>
  <section style="font-size: 15px; margin-bottom: 16px; color: rgb(51, 51, 51); margin-top: 16px; letter-spacing: 1px;">
   <span>
    <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWen7StpAV6mVjjn4N5m6hwWiclp3sJ1ZMFAfTdN1TW35JH1B1V5a09Ya8oh7SrLmEE0uhxupTfo96Z7EUbKbjdicd1PeOfd5oibg/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1#imgIndex=53" />
   </span>
  </section>
 </section>
 <section style="margin-bottom: 0px; letter-spacing: 0.578px;">
  <span>
   <br />
  </span>
 </section>
 <section>
  <strong>
   <strong>
    <span>
     <span>
      神农安全公开交流群
     </span>
    </span>
   </strong>
  </strong>
 </section>
 <p style="margin-bottom: 0px; text-align: center;">
  <span style="font-size: 15px;">
   <span>
    有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）
   </span>
  </span>
 </p>
 <section style="margin-bottom: 0px; clear: both; text-align: center;">
  <img src="https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QUd23Espg2uNOBfRiblEZW8BZkOviasKxpcuN2zBI1ibxe1xOCONIwDOvWBtcLYIZvL8S5dOwW8vSEG7ft2HB5ZhXy2ROx0iahgNGk/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=54" style="height: auto !important; width: 399px !important;" />
 </section>
 <p style="text-align: center;">
  <span>
   <img src="https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QWIXJFAJx1tH06wDvYl2iaRBcqDumcW2btVINd6uxz9L9eDS6Qb4r8muMYZY8os04tFANsJhjhEoianvFIWsNocdDt6LAyVugQKw/640?wx_fmt=jpeg&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=55" style="width: 366px !important; height: auto !important;" />
  </span>
 </p>
 <pre><section><section><section><section><section><p><span><span>申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，</span></span></p><p><span><span>所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.</span></span></p></section></section></section></section></section><p><span><br /></span></p></pre>
 <section>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=56" style="margin-right: auto; margin-bottom: 25px; margin-left: auto; height: auto !important; letter-spacing: 0.578px; color: rgb(74, 74, 74); display: block; border-radius: 4px; width: 239px !important;" />
 </section>
 <section style="margin-bottom: 0px; letter-spacing: 0.578px;">
  <span>
   <br />
  </span>
 </section>
 <section style="letter-spacing: 0.578px;">
  <section>
   <section style="padding-right: 8px; padding-bottom: 8px; padding-left: 8px;">
    <section style="display: flex;">
     <section>
      <section style="height: 1px; line-height: 1px; border-top: 1px solid rgb(224, 233, 255);">
       <span>
        <br />
       </span>
      </section>
     </section>
     <section style="margin-right: 10px; margin-left: 10px;">
      <section style="display: inline-block; vertical-align: middle; width: 15px; line-height: 15px; font-size: 0px;">
       <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;tp=webp&amp;wx_lazy=1#imgIndex=57" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
      </section>
      <section>
       <section style="padding-right: 5px; padding-left: 5px; color: rgb(103, 162, 235); letter-spacing: 1px; line-height: 24px;">
        <p style="font-size: 14px;">
         <strong>
          <span style="font-size: 20px;">
           <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp#imgIndex=58" style="vertical-align: middle; color: rgb(62, 62, 62); letter-spacing: 0.578px; text-align: center; background-color: rgb(255, 255, 255); width: 25px !important; height: auto !important;" />
           往期回顾
           <img src="https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;tp=webp#imgIndex=59" style="vertical-align: middle; color: rgb(62, 62, 62); letter-spacing: 0.578px; text-align: center; background-color: rgb(255, 255, 255); width: 25px !important; height: auto !important;" />
          </span>
         </strong>
        </p>
       </section>
      </section>
      <section>
       <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;tp=webp&amp;wx_lazy=1#imgIndex=60" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
      </section>
     </section>
     <section>
      <section style="height: 1px; line-height: 1px; border-top: 1px solid rgb(224, 233, 255);">
       <span>
        <br />
       </span>
      </section>
     </section>
    </section>
    <section style="margin-top: 15px; padding: 15px 15px 10px; border-radius: 10px;">
     <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
      <section>
       <section style="padding-left: 10px; color: rgb(103, 162, 235); letter-spacing: 1px; line-height: 24px;">
        <section>
         <section style="padding-left: 10px; line-height: 24px;">
          <section style="padding-bottom: 7px; display: flex;">
           <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
            <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=61" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
           </section>
           <section>
            <section style="padding-left: 10px; line-height: 24px;">
             <p style="font-size: 14px; text-align: left;">
              <span>
               <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247495361&amp;idx=1&amp;sn=48283073b325e360823da8dec27a7508&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                手把手js逆向断点调试&amp;js逆向前端加密对抗&amp;企业SRC实战分享
               </a>
              </span>
             </p>
            </section>
           </section>
          </section>
          <section>
           <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
            <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
             <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=62" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
            </section>
            <section>
             <section style="padding-left: 10px; line-height: 24px;">
              <p style="font-size: 14px; text-align: left;">
               <span>
                <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247489731&amp;idx=1&amp;sn=c3a5ef01648fad496ecda36b653b6e21&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                 浅谈src漏洞挖掘中容易出洞的几种姿势
                </a>
               </span>
              </p>
             </section>
            </section>
           </section>
          </section>
          <section>
           <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
            <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
             <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=63" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
            </section>
            <section>
             <section style="padding-left: 10px; line-height: 24px;">
              <p style="font-size: 14px; text-align: left;">
               <span>
                <span>
                 <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247488672&amp;idx=1&amp;sn=493bb70011a02eb971ff1b74c733f1d9&amp;scene=21#wechat_redirect" target="_blank">
                  HVV护网行动 | 分享最近攻防演练HVV漏洞复盘
                 </a>
                </span>
               </span>
              </p>
             </section>
            </section>
           </section>
          </section>
          <section>
           <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
            <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
             <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=64" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
            </section>
            <section>
             <section style="padding-left: 10px; line-height: 24px;">
              <p style="font-size: 14px; text-align: left;">
               <span>
                <span>
                 <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247492377&amp;idx=1&amp;sn=a94ad30e30e08bd96e888dad744e9814&amp;scene=21#wechat_redirect" target="_blank">
                  攻防演练｜分享最近一次攻防演练RTSP奇特之旅
                 </a>
                </span>
               </span>
              </p>
             </section>
            </section>
           </section>
           <section>
            <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
             <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
              <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=65" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
             </section>
             <section>
              <section style="padding-left: 10px; line-height: 24px;">
               <p style="font-size: 14px; text-align: left;">
                <span>
                 <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247492315&amp;idx=1&amp;sn=88991e98058a277e267a9a79b8518e16&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                  JS漏洞挖掘｜分享使用FindSomething联动的挖掘思路
                 </a>
                </span>
               </p>
              </section>
             </section>
            </section>
           </section>
           <section>
            <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
             <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
              <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=66" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
             </section>
             <section>
              <section style="padding-left: 10px; line-height: 24px;">
               <p style="font-size: 14px; text-align: left;">
                <span>
                 <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247493292&amp;idx=1&amp;sn=611fd43361089a30e5f7bcda21274b95&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                  渗透测试 ｜ 从jeecg接口泄露到任意管理员用户接管+SQL注入漏洞
                 </a>
                </span>
               </p>
              </section>
             </section>
            </section>
            <section>
             <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
              <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
               <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=67" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
              </section>
              <section>
               <section style="padding-left: 10px; line-height: 24px;">
                <p style="font-size: 14px; text-align: left;">
                 <span>
                  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247485439&amp;idx=1&amp;sn=3fd7e4cef57edca8e73104f8af38fc05&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                   分享SRC中后台登录处站点的漏洞挖掘技巧
                  </a>
                 </span>
                </p>
               </section>
              </section>
             </section>
            </section>
            <section>
             <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
              <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
               <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=68" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
              </section>
              <section>
               <section style="padding-left: 10px; line-height: 24px;">
                <p style="font-size: 14px; text-align: left;">
                 <span>
                  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247492839&amp;idx=1&amp;sn=b9781f60580c1da8e2151166f0494ba5&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                   企业SRC支付漏洞&amp;EDUSRC&amp;众测挖掘思路技巧操作分享
                  </a>
                 </span>
                </p>
               </section>
              </section>
             </section>
            </section>
            <section>
             <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
              <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
               <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=69" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
              </section>
              <section>
               <section style="padding-left: 10px; line-height: 24px;">
                <p style="font-size: 14px; text-align: left;">
                 <span>
                  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247493495&amp;idx=1&amp;sn=791bebc6faa651cc3c585c2f5f481d21&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                   渗透测试 ｜ 分享某次项目上的渗透测试漏洞复盘
                  </a>
                 </span>
                </p>
               </section>
              </section>
             </section>
             <section style="padding-bottom: 7px; display: flex;">
              <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
               <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=70" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
              </section>
              <section>
               <section style="padding-left: 10px; line-height: 24px;">
                <hr />
                <p style="font-size: 14px; text-align: left;">
                 <span>
                  <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247494877&amp;idx=1&amp;sn=2d00c0f651fd7375e881be86638e53ce&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                   【宝典】分享云安全浪潮src漏洞挖掘技巧
                  </a>
                 </span>
                </p>
               </section>
              </section>
             </section>
             <section>
              <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
               <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
                <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=71" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
               </section>
               <section>
                <section style="padding-left: 10px; line-height: 24px;">
                 <p style="font-size: 14px; text-align: left;">
                  <span>
                   <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247494468&amp;idx=1&amp;sn=f0da4b4ff7763cbb83b858fb5a8964f9&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                    实战SRC挖掘｜微信小程序渗透漏洞复盘
                   </a>
                  </span>
                 </p>
                </section>
               </section>
              </section>
             </section>
             <section>
              <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
               <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
                <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=72" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
               </section>
               <section>
                <section style="padding-left: 10px; line-height: 24px;">
                 <p style="font-size: 14px; text-align: left;">
                  <span>
                   <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247493749&amp;idx=1&amp;sn=d2e0febcdcf9dcd8aa44be0d43b51936&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                    综合资产测绘 | 手把手带你搞定信息收集
                   </a>
                  </span>
                 </p>
                </section>
               </section>
              </section>
             </section>
             <section>
              <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
               <section style="padding-top: 5px; width: 15px; height: 15px; line-height: 15px; font-size: 0px; text-align: left;">
                <img src="https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&amp;from=appmsg&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=73" style="vertical-align: middle; width: 15px !important; height: auto !important;" />
               </section>
               <section>
                <section style="padding-left: 10px; line-height: 24px;">
                 <p style="font-size: 14px; text-align: left;">
                  <span>
                   <a class="normal_text_link mp_article_text_link" href="https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&amp;mid=2247493489&amp;idx=1&amp;sn=d3ef10a1ae3b8c161d7174cb42702fac&amp;scene=21#wechat_redirect" style="color: rgb(61, 170, 214); font-size: 16px;" target="_blank">
                    【宝典】针对若依系统nday的常见各种姿势利用
                   </a>
                  </span>
                 </p>
                </section>
               </section>
              </section>
             </section>
            </section>
           </section>
          </section>
         </section>
        </section>
       </section>
      </section>
     </section>
    </section>
   </section>
  </section>
  <section>
   <section>
    <section style="padding-top: 7px; padding-bottom: 7px; display: flex; border-top: 1px dashed rgb(224, 233, 255);">
     <section>
      <section style="padding-left: 10px; color: rgb(103, 162, 235); letter-spacing: 1px; line-height: 24px;">
       <p style="font-size: 14px; text-align: left;">
        <span>
         <br />
        </span>
       </p>
      </section>
     </section>
    </section>
   </section>
  </section>
 </section>
</section>
<p style="display: none;">
 
 
</p>
