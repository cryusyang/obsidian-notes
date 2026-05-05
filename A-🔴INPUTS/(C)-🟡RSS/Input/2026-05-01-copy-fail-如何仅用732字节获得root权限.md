---
title: "Copy Fail 如何仅用732字节获得Root权限"
url: "https://mp.weixin.qq.com/s/9V6MaUYFgS3Kwg80r0Xq9g"
source: "骨哥说事"
date: 2026-05-01
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Copy Fail（CVE-2026-31431）是Linux内核authencesn加密模板中的一个逻辑缺陷，允许本地非特权用户通过AF_ALG接口和splice机制，向任意可读文件的页面缓存执行可控的4字节越界写入，从而实现稳定、无需竞态的本地提权（如篡改setuid二进制文件获取root权限）。该漏洞利用仅需732字节的标准库Python脚本，兼容所有主流Linux发行版与架构，且因绕过VFS写入路径、不标记脏页，导致磁盘文件不变、常规校验和工具无法检测。其根本原因在于authencesn算法在原地解密时非法写入超出目标缓冲区的内存，结合AF_ALG将页面缓存页直接纳入可写scatterlist的设计缺陷，使写入跨越至共享的页面缓存，进而还可用于容器逃逸与Kubernetes节点攻陷。

---

<table>
 <tbody>
  <tr>
   <td valign="top" width="557">
    <h1>
     <strong>
      <span style="font-size: 18px;">
       <span style="color: rgb(255, 0, 0);">
        <strong>
         <span style="font-size: 15px;">
          <span>
           声明：
          </span>
         </span>
        </strong>
       </span>
      </span>
     </strong>
     <span style="font-size: 18px;">
      <span style="font-size: 15px;">
       <span>
        文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。
       </span>
      </span>
     </span>
    </h1>
   </td>
  </tr>
 </tbody>
</table>
<h1>
 <span>
  <br />
 </span>
</h1>
<section style="margin-bottom: 0px;">
 <span>
  
  
 </span>
</section>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span style="letter-spacing: 0.544px; background-color: rgb(255, 251, 0);">
  <strong>
   <span>
    <br />
   </span>
  </strong>
 </span>
</p>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   不想错过任何消息？设置星标
  </span>
 </strong>
 <strong style="color: rgb(217, 33, 66); letter-spacing: 0.544px;">
  <span>
   ↓ ↓ ↓
  </span>
 </strong>
</p>
<h1>
 <span>
  <br />
 </span>
</h1>
<p style="margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="text-align: center; margin-bottom: 0px;">
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&amp;from=appmsg&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="width: 247px !important; height: auto !important;" />
 </span>
</p>
<p>
 <span>
  来自Xint代码研究团队
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   Copy Fail
  </span>
 </strong>
 <span>
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   (CVE-2026-31431)
  </span>
 </strong>
 <span>
  是Linux内核
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  加密模板中的一个逻辑缺陷。它允许一个本地非特权用户以确定、可控的方式，向系统上任何可读文件的页面缓存执行4字节写入操作。一个仅732字节的Python脚本就能编辑setuid二进制文件，从而在自2017年以来发布的所有Linux发行版上获取root权限。
 </span>
</p>
<p>
 <span>
  内核永远不会将已损坏的页面标记为脏页以供写回，因此磁盘上的文件保持不变，普通的基于磁盘的校验和校验无法检测到这种修改。然而，访问文件时实际读取的是页面缓存，因此内存中损坏的版本会立即在全系统范围内可见。通过损坏setuid二进制文件的页面缓存，本地非特权用户可以利用此漏洞获取root权限。由于页面缓存在宿主机中是共享的，该原语还可用于跨越容器边界。
 </span>
</p>
<p>
 <span>
  这项发现借助了AI辅助，但最初是源于Theori研究员Taeyang Lee的洞见，他当时正在研究Linux加密子系统如何与基于页面缓存的数据交互。他使用 Xint Code 将他的研究范围扩展到整个加密子系统，而 Copy Fail 是报告中最关键的发现。
 </span>
</p>
<p>
 <span>
  这是两篇系列文章的第一篇：
 </span>
</p>
<ul class="list-paddingleft-1">
 <li style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <span>
     第1部分
    </span>
   </strong>
   <span>
    (本文)：漏洞本身和本地权限提升
   </span>
  </p>
 </li>
 <li style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <p style="margin: 0px 0px 32px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
   <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
    <span>
     第2部分
    </span>
   </strong>
   <span>
    ：Kubernetes容器逃逸
   </span>
  </p>
 </li>
</ul>
<section>
 <span style="font-weight: bold;">
  Copy Fail 的不同之处
 </span>
</section>
<p>
 <span>
  Linux内核过去曾有过备受瞩目的权限提升漏洞。Dirty Cow (CVE-2016-5195) 需要在虚拟内存子系统的写时复制路径中赢得竞态条件。它通常需要多次尝试，有时会导致系统崩溃。Dirty Pipe (CVE-2022-0847) 版本特定，且需要精确地操作管道缓冲区。
 </span>
</p>
<p>
 <span>
  Copy Fail 是一个直接的逻辑缺陷。它无需竞态、重试或有崩溃风险的时机窗口就能触发。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   可移植性。
  </span>
 </strong>
 <span>
  完全相同的脚本在每一个测试过的发行版和架构上都能工作，包括Ubuntu、Amazon Linux、RHEL和SUSE。没有针对每个发行版的偏移量调整。无需重新编译。利用代码中也没有版本检查。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   小巧。
  </span>
 </strong>
 <span>
  整个攻击利用程序是一个简短的Python脚本，仅使用标准库模块 (
 </span>
 <code>
  <span>
   os
  </span>
 </code>
 <span>
  ,
 </span>
 <code>
  <span>
   socket
  </span>
 </code>
 <span>
  ,
 </span>
 <code>
  <span>
   zlib
  </span>
 </code>
 <span>
  )。它需要 Python 3.10+ 以支持
 </span>
 <code>
  <span>
   os.splice
  </span>
 </code>
 <span>
  。没有编译后的负载，无需安装依赖。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   隐蔽性。
  </span>
 </strong>
 <span>
  该写入绕过了普通的VFS写入路径。被损坏的页面永远不会被内核的写回机制标记为脏页。标准的文件完整性工具通过比较磁盘上的校验和会检测不到它，因为磁盘上的文件并未改变。只有内存中的页面缓存被损坏。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   跨容器影响。
  </span>
 </strong>
 <span>
  页面缓存在系统上的所有进程间共享，包括跨容器边界。Copy Fail 不仅仅是一个本地权限提升漏洞。它是一个容器逃逸原语，也是一个Kubernetes节点攻陷向量（第2部分详解）。
 </span>
</p>
<hr />
<h2>
 <strong>
  <span>
   根本原因
  </span>
 </strong>
</h2>
<h2>
 <strong>
  <span style="font-weight: bold;">
   位于可写分散/聚集列表（writable scatterlist）中的页面缓存页
  </span>
 </strong>
</h2>
<p>
 <span>
  AF_ALG 是一种套接字类型，它将内核的加密子系统暴露给非特权的用户空间。用户可以打开一个套接字，绑定到任何AEAD（带关联数据的认证加密）模板，并对任意数据进行加密或解密操作。无需任何权限。
 </span>
</p>
<p>
 <span>
  构成此漏洞基础的一个核心原语是
 </span>
 <code>
  <span>
   splice()
  </span>
 </code>
 <span>
  ：它通过引用传递页面缓存页，在不复制的情况下在文件描述符和管道间传输数据。当用户将一个文件
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  到管道，然后再转移到AF_ALG套接字时，该套接字的输入分散/聚集列表持有指向该文件内核缓存页的直接引用。这些页面并未被复制；分散/聚集列表条目指向的是为该文件每一次
 </span>
 <code>
  <span>
   read()
  </span>
 </code>
 <span>
  、
 </span>
 <code>
  <span>
   mmap()
  </span>
 </code>
 <span>
  和
 </span>
 <code>
  <span>
   execve()
  </span>
 </code>
 <span>
  提供支撑的同一个物理页。
 </span>
</p>
<p>
 <span>
  对于AEAD解密，输入是 AAD（关联认证数据） || 密文 || 认证标签。在
 </span>
 <code>
  <span>
   algif_aead.c
  </span>
 </code>
 <span>
  内部，
 </span>
 <code>
  <span>
   recvmsg()
  </span>
 </code>
 <span>
  将操作设置为原地进行，这意味着同一个分散/聚集列表既作为加密算法的输入，也作为其输出。
 </span>
</p>
<p>
 <span>
  AAD和密文数据通过
 </span>
 <code>
  <span>
   memcpy_sglist
  </span>
 </code>
 <span>
  从输入分散/聚集列表中
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   字节拷贝
  </span>
 </strong>
 <span>
  到输出缓冲区。这是一个真实的拷贝。页面缓存页只被读取。但是，认证标签（输入分散/聚集列表中最后的
 </span>
 <code>
  <span>
   authsize
  </span>
 </code>
 <span>
  字节）
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   不被拷贝
  </span>
 </strong>
 <span>
  。内核保留指向标签的分散/聚集列表条目，并使用
 </span>
 <code>
  <span>
   sg_chain()
  </span>
 </code>
 <span>
  将它们链接到输出分散/聚集列表的末尾：
 </span>
</p>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhNVmIZ64P1kpWqvw5gUyU0zEDLc61AWZvApL18MR1ZnoTEiaQDzrvUfticVKnabU3yOQs9h9DgAPfxSACABef8ibNicAWoibjnllvI/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=1" style="height: auto !important; width: 680px !important;" />
</section>
<p>
 <span>
  现在输出分散/聚集列表有两个区域：用户的
 </span>
 <code>
  <span>
   recvmsg
  </span>
 </code>
 <span>
  缓冲区（包含拷贝的AAD和密文），后面跟着链接的标签页，这些标签页仍然引用着目标文件的原始页面缓存页。内核设置
 </span>
 <code>
  <span>
   req-&gt;src = req-&gt;dst
  </span>
 </code>
 <span>
  ，两者都指向这个合并链表的头部：
 </span>
</p>
<section style="text-align: center;">
 <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgTzlbbCyz576tuoQtVho6P6ARodbPib6pk8cK58Nqkz4v24lXEvRicgHibAljxcLMkf14WibozF4VgtzA2fdmRe8Lbas3LbDv1b2o/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=2" style="height: auto !important; width: 680px !important;" />
</section>
<p>
 <span>
  这种原地设计是漏洞的根本原因。它将页面缓存页置于一个可写的分散/聚集列表中，与合法的写入区域仅以一个偏移量边界相隔。该设计假设每个AEAD算法都会将其写入操作限制在预期的目标区域内，但API中没有任何内容强制执行这一点，也没有将其记录为一项要求。
 </span>
</p>
<p>
 <span>
  不幸的是，有一个AEAD算法打破了这一隐式约束。
 </span>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   触发机制
  </span>
  <code>
   <span>
    <br />
   </span>
  </code>
 </strong>
</h2>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <code>
   <span style="font-weight: bold;">
    <span style="background-color: rgb(178, 178, 178);">
     authencesn
    </span>
   </span>
  </code>
  <span>
   的临时写入
  </span>
 </strong>
</h2>
<p>
 <span>
  内核的AEAD API为解密定义了一个清晰的输出契约：目标缓冲区接收 AAD || 明文，精确为
 </span>
 <code>
  <span>
   assoclen + (cryptlen - authsize)
  </span>
 </code>
 <span>
  字节。
 </span>
</p>
<p>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  是一个由IPsec使用的AEAD包装器，用于支持扩展序列号。IPsec使用64位序列号，分为高32位（
 </span>
 <code>
  <span>
   seqno_hi
  </span>
 </code>
 <span>
  ，AAD的字节0–3）和低32位（
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  ，字节4–7）。传输格式只携带
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  ；
 </span>
 <code>
  <span>
   seqno_hi
  </span>
 </code>
 <span>
  是隐含的。为了计算HMAC，
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  需要重新排列这些字节：
 </span>
 <code>
  <span>
   seqno_hi
  </span>
 </code>
 <span>
  放在哈希输入的前面，
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  附加在末尾。
 </span>
</p>
<p>
 <span>
  它通过使用调用者的目标缓冲区作为临时空间来执行这种重排。在
 </span>
 <code>
  <span>
   crypto_authenc_esn_decrypt()
  </span>
 </code>
 <span>
  中：
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
 <pre class="code-snippet__js"><code><span><span>scatterwalk_map_and_copy</span>(tmp, dst, <span>0</span>, <span>8</span>, <span>0</span>);                           // read AAD bytes <span>0</span>–<span>7</span></span></code><code><span><span>scatterwalk_map_and_copy</span>(tmp, dst, <span>4</span>, <span>4</span>, <span>1</span>);                           // overwrite dst[<span>4</span>..<span>7</span>] with seqno_hi</span></code><code><span><span>scatterwalk_map_and_copy</span>(tmp + <span>1</span>, dst, assoclen + cryptlen, <span>4</span>, <span>1</span>);     // write seqno_lo after the tag</span></code></pre>
</section>
<p>
 <span>
  前两个调用在AAD区域内重新排列ESN字节，这是一个会被恢复的临时修改。第三个调用在偏移量
 </span>
 <code>
  <span>
   assoclen + cryptlen
  </span>
 </code>
 <span>
  处（超过AEAD标签的位置）写入4个字节。该算法正在使用它不拥有的内存作为临时便签本。
 </span>
</p>
<p>
 <span>
  该位置原始字节永久丢失。代码后续会读取
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  以重建AAD，但从未将原始内容写回
 </span>
 <code>
  <span>
   dst[assoclen + cryptlen]
  </span>
 </code>
 <span>
  。无论操作成功与否，该位置都被视为可丢弃的临时空间。
 </span>
</p>
<p>
 <span>
  内核中没有其他标准AEAD算法会这样做。GCM、CCM和普通的
 </span>
 <code>
  <span>
   authenc
  </span>
 </code>
 <span>
  都将它们的写入操作限制在合法的输出区域内。只有
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  会写入越界。
 </span>
</p>
<p>
 <span>
  在AF_ALG的原地路径中，这个写入从输出缓冲区跨越到了链接的页面缓存标签页。
 </span>
 <code>
  <span>
   scatterwalk_map_and_copy
  </span>
 </code>
 <span>
  越过接收缓冲区，通过
 </span>
 <code>
  <span>
   kmap_local_page
  </span>
 </code>
 <span>
  映射页面缓存页，并将
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  直接写入目标文件的内核缓存副本中。随后HMAC计算运行并失败（因为密文是伪造的），所以
 </span>
 <code>
  <span>
   recvmsg()
  </span>
 </code>
 <span>
  返回错误，但受控的4字节写入依然存在。
 </span>
</p>
<p>
 <span>
  关键在于，攻击者控制三件事：
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   目标文件：
  </span>
 </strong>
 <span>
  当前用户可读的任何文件。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   写入偏移量：
  </span>
 </strong>
 <span>
  标签区域对应于
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  进的文件数据的最后
 </span>
 <code>
  <span>
   authsize
  </span>
 </code>
 <span>
  字节。通过选择
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  的文件偏移量、长度和
 </span>
 <code>
  <span>
   assoclen
  </span>
 </code>
 <span>
  ，攻击者可以精确确定文件中页面缓存的哪4个字节被覆盖。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   写入值：
  </span>
 </strong>
 <span>
  4字节的覆盖值（
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  ）来自AAD的字节4–7，由攻击者在
 </span>
 <code>
  <span>
   sendmsg()
  </span>
 </code>
 <span>
  中构造。
 </span>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   这是如何发生的
  </span>
 </strong>
</h2>
<p>
 <span>
  2011年，
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  被添加到内核 (a5079d084f8b)，以支持IPsec ESP的64位扩展序列号。从一开始，该代码就使用调用者的目标分散/聚集列表作为ESN字节重排的临时空间。这在当时是无害的：在旧的AEAD接口下，关联数据位于单独的分散/聚集列表中，并且唯一的调用者是内核内部的xfrm层。其他任何人都不会观察到这些临时的写入。
 </span>
</p>
<p>
 <span>
  四年后，2015年，AF_ALG增加了对AEAD的支持 (algif_aead.c)，其
 </span>
 <code>
  <span>
   splice()
  </span>
 </code>
 <span>
  路径可以将页面缓存页传递到加密分散/聚集列表中。同年，
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  被转换为新的AEAD接口 (104880a6b470)，引入了会导致写入越过输出边界的
 </span>
 <code>
  <span>
   assoclen + cryptlen
  </span>
 </code>
 <span>
  偏移量。但在此时，AF_ALG使用的是非原地操作：
 </span>
 <code>
  <span>
   req-&gt;src
  </span>
 </code>
 <span>
  和
 </span>
 <code>
  <span>
   req-&gt;dst
  </span>
 </code>
 <span>
  是分开的分散/聚集列表。页面缓存页在
 </span>
 <code>
  <span>
   src
  </span>
 </code>
 <span>
  （只读）中。临时写入会进入
 </span>
 <code>
  <span>
   dst
  </span>
 </code>
 <span>
  （用户的缓冲区）。此时还不可被利用。
 </span>
</p>
<p>
 <span>
  然后在2017年，algif_aead.c中添加了一项优化 (72548b093ee3)，以启用AEAD操作的原地进行。对于解密，代码将AAD和密文数据从发送SGL复制到接收缓冲区，但使用
 </span>
 <code>
  <span>
   sg_chain()
  </span>
 </code>
 <span>
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   通过引用链接标签页
  </span>
 </strong>
 <span>
  。随后它设置了
 </span>
 <code>
  <span>
   req-&gt;src = req-&gt;dst
  </span>
 </code>
 <span>
  。来自
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  的页面缓存页现在位于
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   可写
  </span>
 </strong>
 <span>
  的目标分散/聚集列表中。
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  在
 </span>
 <code>
  <span>
   dst[assoclen + cryptlen]
  </span>
 </code>
 <span>
  处的写入现在会遍历到那些链接的标签页，从而产生了这个漏洞。
 </span>
</p>
<p>
 <span>
  没有人将2017年的原地优化与
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  的临时写入或
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  路径对页面缓存页的使用联系起来。每一次变更孤立地看都是合理的。漏洞存在于这三者的交汇处，并已在近十年间可被悄无声息地利用。
 </span>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   攻击利用过程
  </span>
 </strong>
</h2>
<p>
 <span>
  默认的攻击路径目标是
 </span>
 <code>
  <span>
   /usr/bin/su
  </span>
 </code>
 <span>
  ，这是一个广泛存在于各大Linux发行版上的setuid-root二进制文件，包括本次测试的所有四个发行版。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   步骤1：设置套接字。
  </span>
 </strong>
 <span>
  打开一个AF_ALG套接字，并绑定到
 </span>
 <code>
  <span>
   authencesn(hmac(sha256),cbc(aes))
  </span>
 </code>
 <span>
  。设置一个key。接受一个请求套接字。无需特权；默认情况下，非特权用户可以使用AF_ALG。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   步骤2：构造写入。
  </span>
 </strong>
 <span>
  对于Shellcode负载的每个4字节块，构造一个
 </span>
 <code>
  <span>
   sendmsg()
  </span>
 </code>
 <span>
  +
 </span>
 <code>
  <span>
   splice()
  </span>
 </code>
 <span>
  对。
 </span>
 <code>
  <span>
   sendmsg
  </span>
 </code>
 <span>
  提供AAD：字节4–7携带要写入的4个字节（
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  ）。
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  提供目标文件的页面缓存页作为密文和标签。选择AEAD参数（
 </span>
 <code>
  <span>
   assoclen
  </span>
 </code>
 <span>
  、
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  偏移量、
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  长度），使得
 </span>
 <code>
  <span>
   dst[assoclen + cryptlen]
  </span>
 </code>
 <span>
  落在
 </span>
 <code>
  <span>
   /usr/bin/su
  </span>
 </code>
 <span>
  的
 </span>
 <code>
  <span>
   .text
  </span>
 </code>
 <span>
  段中的目标偏移量上。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   步骤3：触发写入。
  </span>
 </strong>
 <span>
 </span>
 <code>
  <span>
   recv()
  </span>
 </code>
 <span>
  触发解密操作。在
 </span>
 <code>
  <span>
   authencesn
  </span>
 </code>
 <span>
  内部，内核从AAD读取ESN字节，并将
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  写入
 </span>
 <code>
  <span>
   dst[assoclen + cryptlen]
  </span>
 </code>
 <span>
  。
 </span>
 <code>
  <span>
   scatterwalk
  </span>
 </code>
 <span>
  从输出缓冲区跨越到链接的页面缓存页。有4个字节被写入到
 </span>
 <code>
  <span>
   /usr/bin/su
  </span>
 </code>
 <span>
  的内核缓存副本中。HMAC基于重排后的数据计算并失败。内核读取
 </span>
 <code>
  <span>
   seqno_lo
  </span>
 </code>
 <span>
  以恢复AAD，但标签位置上的原始字节
 </span>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   永远不会
  </span>
 </strong>
 <span>
  被恢复。
 </span>
 <code>
  <span>
   recvmsg
  </span>
 </code>
 <span>
  返回一个错误。页面缓存被损坏。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   步骤4：执行。
  </span>
 </strong>
 <span>
  所有块写入完成后，调用
 </span>
 <code>
  <span>
   execve("/usr/bin/su")
  </span>
 </code>
 <span>
  。内核从页面缓存加载该二进制文件。页面缓存版本包含注入的Shellcode。由于
 </span>
 <code>
  <span>
   su
  </span>
 </code>
 <span>
  是setuid-root，Shellcode以UID 0运行。获得root权限。
 </span>
</p>
<pre tabindex="0"><span><br /></span></pre>
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
 </ul>
 <pre class="code-snippet__js"><code><span><span>a</span> = socket.socket(<span>38</span>, <span>5</span>, <span>0</span>)  # AF_ALG, SOCK_SEQPACKET</span></code><code><span><span>a</span>.bind((<span>"aead"</span>, <span>"authencesn(hmac(sha256),cbc(aes))"</span>))</span></code><code><span><span># ... set key, accept request socket u ...</span></span></code><code><span><span>u</span>.sendmsg([b<span>"A"</span>*<span>4</span> + payload_chunk],<span> [cmsg_headers], MSG_MORE)</span></span></code><code><span>os.splice(target_fd, pipe_wr, offset)</span></code><code><span>os.splice(pipe_rd, alg_fd, offset)</span></code><code><span>u.recv(...)  # triggers decrypt → page cache write</span></code></pre>
</section>
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   演示
  </span>
 </strong>
</h2>
<p>
 <span>
  我们在四个发行版上运行了同一个脚本，并在每个发行版上都观察到了root权限的获取。
 </span>
</p>
<p>
 <span>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhvFKqysP6aZd49tvtMygFCibpX4qVrz20gD2pBowrgjPyHwYRDQHJep1hLeeG7icBKFXmIPDHxsz4o8TurOics3y0OIaH583hlBY/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=3" style="height: auto !important; width: 680px !important;" />
 </span>
</p>
<p>
 <span>
  每个终端都以用户 xint (uid=1001) 开始。下载并执行同一个732字节的利用程序。每个终端最终都进入了一个root shell。
 </span>
</p>
<table>
 <thead>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
     <span>
      发行版
     </span>
    </strong>
   </th>
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
     <span>
      内核版本
     </span>
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      Ubuntu 24.04 LTS
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      6.17.0-1007-aws
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      Amazon Linux 2023
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      6.18.8-9.213.amzn2023
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      RHEL 10.1
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      6.12.0-124.45.1.el10_1
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      SUSE 16
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      6.12.0-160000.9-default
     </span>
    </section>
   </td>
  </tr>
 </tbody>
</table>
<p>
 <em style="margin: 0px; padding: 0px; border: 0px; font-style: italic; font-variant: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   这些是我们直接测试过的四个发行版与内核组合，涵盖了内核主线6.12、6.17和6.18。
  </span>
 </em>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   修复方案
  </span>
 </strong>
</h2>
<p>
 <span>
  补丁 (a664bf3d603d) 将 algif_aead.c 回退到非原地操作，完全移除了2017年的原地优化。
 </span>
 <code>
  <span>
   Fixes:
  </span>
 </code>
 <span>
  标签指向 72548b093ee3——引入原地设计的那个提交——确认了将页面缓存页链接到可写目标分散/聚集列表是根本原因。
 </span>
</p>
<p>
 <span>
  易受攻击的代码设置了
 </span>
 <code>
  <span>
   req-&gt;src = req-&gt;dst
  </span>
 </code>
 <span>
  ，两者都指向一个合并的分散/聚集列表，其中来自
 </span>
 <code>
  <span>
   splice()
  </span>
 </code>
 <span>
  的页面缓存页被链接到了可写目标中。该修复将它们分离开：
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
  <li>
  </li>
  <li>
  </li>
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>// Before: src and dst are the same scatterlist (in-place)</span></span></code><code><span><span>aead_request_set_crypt</span>(&amp;areq-&gt;cra_u.<span>aead_req</span>, rsgl_src,              <span>// RX SGL</span></span></code><code><span>                       areq-&gt;first_rsgl.<span>sgl</span>.<span>sgt</span>.<span>sgl</span>, used, ctx-&gt;iv); <span>// RX SGL (same)</span></span></code><code><span><span>// After: src is the TX SGL, dst is the RX SGL (out-of-place)</span></span></code><code><span><span>aead_request_set_crypt</span>(&amp;areq-&gt;cra_u.<span>aead_req</span>, tsgl_src,              <span>// TX SGL</span></span></code><code><span>                       areq-&gt;first_rsgl.<span>sgl</span>.<span>sgt</span>.<span>sgl</span>, used, ctx-&gt;iv); <span>// RX SGL (different)</span></span></code></pre>
</section>
<p>
 <span>
  现在
 </span>
 <code>
  <span>
   req-&gt;src
  </span>
 </code>
 <span>
  指向发送SGL（其中可能包含来自
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  的页面缓存页）。
 </span>
 <code>
  <span>
   req-&gt;dst
  </span>
 </code>
 <span>
  指向接收SGL（用户的
 </span>
 <code>
  <span>
   recvmsg
  </span>
 </code>
 <span>
  缓冲区）。只有AAD从
 </span>
 <code>
  <span>
   src
  </span>
 </code>
 <span>
  复制到
 </span>
 <code>
  <span>
   dst
  </span>
 </code>
 <span>
  。将页面缓存标签页链接到可写目标分散/聚集列表的整个
 </span>
 <code>
  <span>
   sg_chain
  </span>
 </code>
 <span>
  机制被移除。
 </span>
</p>
<p>
 <span>
  提交信息概括了这一点："在 algif_aead 中使用原地操作没有好处，因为源和目标来自不同的映射。"
 </span>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   缓解措施
  </span>
 </strong>
</h2>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   为内核打补丁。
  </span>
 </strong>
 <span>
  此修复 将AF_ALG AEAD恢复为非原地操作，消除了可写分散/聚集列表中的页面缓存页。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   更新发行版的内核软件包。
  </span>
 </strong>
 <span>
  主要发行版应通过常规的内核软件包更新来推送此修复。
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   对于立即缓解
  </span>
 </strong>
 <span>
  ，可以通过seccomp阻止AF_ALG套接字创建，或通过将algif_aead模块列入黑名单：
 </span>
</p>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>echo <span>"install algif_aead /bin/false"</span> &gt; <span>/etc/m</span>odprobe.<span>d</span>/disable-algif-aead.<span>conf</span></span></code><code><span>rmmod algif_aead <span>2</span>&gt;<span>/dev/</span><span>null</span></span></code></pre>
</section>
<p>
 <span>
  关于容器逃逸的影响，请见第2部分。
 </span>
</p>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   协调披露时间线
  </span>
 </strong>
</h2>
<table>
 <thead>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
     <span>
      日期
     </span>
    </strong>
   </th>
   <th style="margin: 0px; padding: 10px 5px; border: 1px solid rgb(237, 240, 245); font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; text-align: left;">
    <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
     <span>
      事件
     </span>
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-03-23]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      向Linux内核安全团队报告漏洞
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-03-24]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      收到初步确认
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-03-25]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      补丁被提出并接受审查
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-04-01]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      补丁提交到主线内核
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline;">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-04-22]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      分配 CVE-2026-31431
     </span>
    </section>
   </td>
  </tr>
  <tr style="margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; background: rgb(237, 240, 245);">
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      [2026-04-29]
     </span>
    </section>
   </td>
   <td style="margin: 0px; padding: 5px; border: 1px solid rgb(237, 240, 245); font: inherit; vertical-align: middle; text-align: left;">
    <section>
     <span>
      公开披露（本文）
     </span>
    </section>
   </td>
  </tr>
 </tbody>
</table>
<hr />
<h2>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   我们发现漏洞的过程
  </span>
 </strong>
</h2>
<p>
 <span>
  Taeyang Lee早期的 kernelCTF工作 已经勾勒出了AF_ALG的攻击面。他意识到AF_ALG +
 </span>
 <code>
  <span>
   splice
  </span>
 </code>
 <span>
  创建了一条路径，使得非特权的用户空间可以直接将页面缓存页送入加密子系统，并怀疑分散/聚集列表页面的来源可能是未被充分探索的漏洞来源。
 </span>
</p>
<p>
 <span>
  与此同时，其他Theori研究人员正在运行Xint Code，并在内核代码（包括Android驱动程序和XNU）中发现了关键漏洞。我们正寻求将这项工作扩展到Linux，而加密子系统鉴于我们对其内部知识的掌握，成为了一个自然的起点。
 </span>
</p>
<p>
 <span>
  Xint Code支持一个"操作员提示"功能，它（可选地）允许人类操作员提供额外的上下文来指导自动化扫描。在本例中，操作员提示相当简单：
 </span>
</p>
<blockquote>
 <p style="margin: 0px 0px 0.75em; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; color: rgb(80, 89, 102);">
  <span>
   "这是 Linux 的 crypto/ 子系统。请检查所有从用户空间系统调用可达的代码路径。请注意一个关键观察：
  </span>
  <code>
   <span>
    splice()
   </span>
  </code>
  <span>
   可以将只读文件（包括 setuid 二进制文件）的页面缓存引用传递给 crypto 的 TX 散射列表。"
  </span>
 </p>
</blockquote>
<p>
 <span>
  大约一小时后，扫描完成，Copy Fail 是严重性最高的输出。
 </span>
</p>
<section>
 <img src="https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZjvDibiatjicnmUssmjzfGSiaTacicI9DKZtCLb5HmQlC3rr4TSIII97CsPgaV4GfyEB2FEHb94wYaKcROZLsaw9VrTBwTafBceHMDE/640?wx_fmt=other&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=4" style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-weight: inherit; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline; height: auto !important; width: 680px !important;" />
</section>
<p>
 <span>
  Xint Code 对 CVE-2026-31431 的扫描结果
 </span>
</p>
<p>
 <strong style="margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 600; font-size: inherit; line-height: inherit; font-family: inherit; vertical-align: baseline;">
  <span>
   注意
  </span>
 </strong>
 <span>
  ：该扫描还识别了其他高严重性漏洞，包括另一个权限提升漏洞。这些其他漏洞仍在负责任的披露流程中。
 </span>
</p>
<p>
 <span>
  <span style="font-size: 14px;">
   原文：
  </span>
 </span>
 <span>
  <span style="font-size: 14px; text-decoration: underline;">
   https://xint.io/blog/copy-fail-linux-distributions
  </span>
 </span>
</p>
<p style="text-align: center; margin-bottom: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 32px; border-width: 0px; border-color: initial; line-height: inherit; vertical-align: baseline; letter-spacing: normal; text-align: left;">
 <strong>
  <span style="font-size: 18px;">
   <span>
    <span style="font-weight: bold;">
     感谢阅读，如果觉得还不错的话，动动手指给个三连吧～
    </span>
   </span>
  </span>
 </strong>
</p>
<p style="display: none;">
 
 
</p>
