---
title: "使用 Python 和 Jython 编写自定义 Burp 扩展程序进行自动化渗透测试"
url: "https://mp.weixin.qq.com/s/S5BIXfYiNR46BkgZ0YS0Zg"
source: "安全狗的自我修养"
date: 2026-04-17
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文介绍了如何使用Jython开发高效、稳定且UI驱动的Burp Suite扩展，以提升漏洞测试与渗透测试中的自动化效率。文章强调了Jython相比纯Java的优势：无需编译、可直接调用Java UI库和Burp API、迭代开发速度快。详细阐述了六大关键环节：Jython环境配置、核心Burp接口（IBurpExtender、ITab、IContextMenuFactory等）实现原理、Swing/ AWT界面构建方法、事件分发线程（EDT）安全编程技巧、扩展主类结构设计，以及Burp内建调试机制。最终目标是帮助安全研究人员摆脱重复性手工操作，构建高度定制化、生产就绪的测试工具。

---

<h1 class="js_darkmode__0">
 <span>
  <span style="color: rgb(255, 0, 0);">
   官网：
  </span>
 </span>
 <span>
  <span style="color: rgb(255, 0, 0);">
   http://securitytech.cc
  </span>
 </span>
</h1>
<section>
 <span>
  <br />
 </span>
</section>
<section style="margin-bottom: 0px;">
 <span>
  <img src="https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsF7nv8hjIgeAYkSW6rAYwQQ9a2Vice0NXWSg7T6A9kWbn7h4DPt0zo8SbZvSyJQ7PlPtZ7NvcboO9dNwOmdwwPPkyicAcqVfaPA/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1#imgIndex=0" style="height: auto !important; width: 680px !important;" />
 </span>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     如果你认真从事漏洞赏金或渗透测试，你肯定深有体会。你最终会一遍又一遍地重复相同的流程，手动编码有效载荷，然后眼睁睁地看着宝贵的时间白白流逝，简直让人抓狂。手动测试在初始发现阶段固然有效，但重复性的工作却令人精疲力竭。你发现了一个奇怪的注入向量，突然间，你需要测试 500 个自定义编码的有效载荷变体。在 Repeater 中手动完成这些工作，很快就会让你精疲力竭。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     摆脱这种困境的最佳方法是编写自定义的 Burp Suite 扩展，使其完全符合您的开发方法。您可以用纯 Java 编写，但如果您想快速开发，Jython 是最佳选择。它允许您编写可读性极高的 Python 代码，同时还能直接调用 Java 强大的 UI 库和 Burp 丰富的 API。无需编译步骤，也无需庞大的 IDE。您只需编写脚本，将其加载到 Burp 中，即可立即迭代。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     以下是构建一个强大的、UI驱动的Jython扩展的深度蓝图，该扩展不会导致环境崩溃。
    </span>
   </font>
  </font>
 </p>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     1. 执行环境：设置 Jython
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     首先，Burp 是基于 Java 构建的，它本身并不原生支持 Python。为了弥补这一差距，我们使用了 Jython——一个用 Java 编写的 Python 实现。
    </span>
   </font>
  </font>
 </p>
 <ol class="list-paddingleft-1" style="margin: 0px; padding: 0px;">
  <li>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      请从 Jython 官方发布页面下载独立的 JAR 文件。您需要的是
     </span>
    </font>
   </font>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       独立
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      版本，因为它包含了所有必要的标准库。
     </span>
    </font>
   </font>
  </li>
  <li>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      打开 Burp Suite，转到
     </span>
    </font>
   </font>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       “扩展”&gt;“选项”
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      ，并将“Python 环境”设置直接指向您刚刚下载的 JAR 文件。
     </span>
    </font>
   </font>
  </li>
  <li>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      从那里，您可以将 Python 脚本直接加载到扩展程序选项卡中。
     </span>
    </font>
   </font>
  </li>
 </ol>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     这种设置的优点在于迭代速度快。修改
    </span>
   </font>
  </font>
  <code>
   <span>
    .py
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     文件后，只需在“扩展程序”选项卡中点击“重新加载”即可。更改会立即生效。
    </span>
   </font>
  </font>
 </p>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     2. 架构蓝图：核心接口
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     在编写 UI 代码之前，我们需要了解 Burp 如何与我们的脚本交互。Burp 扩展程序高度依赖接口。您的主类需要实现特定的 Java 接口才能接入 Burp 的内部事件循环。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     基于我们的基础架构，我们引入了 Burp 接口和 Java 组件的混合方案：
    </span>
   </font>
  </font>
  <span>
   <br />
  </span>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Python
    </span>
   </font>
  </font>
 </p>
 <pre><span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>from</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> burp </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>import </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>IBurpExtender</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>ITab</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>IContextMenuFactory</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>IMessageEditorController</span></font></font></span></span></pre>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     让我们来详细了解一下这些功能在底层是如何运作的：
    </span>
   </font>
  </font>
 </p>
 <ul class="list-paddingleft-1" style="margin: 0px; padding: 0px;">
  <li>
   <code>
    <strong style="font-weight: 700; font-family: inherit;">
     <span>
      IBurpExtender
     </span>
    </strong>
   </code>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       （必不可少）：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      你必须导入这个库。它是 Burp 的起始点。当 Burp 加载你的脚本时，它会专门实例化一个名为 `&lt;class_name&gt;` 的类
     </span>
    </font>
   </font>
   <code>
    <span>
     BurpExtender
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      并调用它的
     </span>
    </font>
   </font>
   <code>
    <span>
     registerExtenderCallbacks
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      方法。如果没有这个库，你的脚本就无法运行。
     </span>
    </font>
   </font>
  </li>
  <li>
   <code>
    <strong style="font-weight: 700; font-family: inherit;">
     <span>
      ITab
     </span>
    </strong>
   </code>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       （视觉锚点）：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      如果您正在构建自定义界面，则需要用到它。实现此功能
     </span>
    </font>
   </font>
   <code>
    <span>
     ITab
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      会告诉 Burp：“我有一个自定义 JPanel，请将其绘制在 Proxy 和 Repeater 选项卡旁边。” 您需要提供选项卡名称和要渲染的实际 UI 组件。
     </span>
    </font>
   </font>
  </li>
  <li>
   <code>
    <strong style="font-weight: 700; font-family: inherit;">
     <span>
      IContextMenuFactory
     </span>
    </strong>
   </code>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       （右键魔法）：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      此界面可让您的工具出现在 Burp 的右键菜单中。想将 HTTP 历史记录中经过 base64 编码的特殊参数直接发送到您的自定义解码器选项卡吗？这就是实现这一目标的方法。
     </span>
    </font>
   </font>
  </li>
  <li>
   <code>
    <strong style="font-weight: 700; font-family: inherit;">
     <span>
      IMessageEditorController
     </span>
    </strong>
   </code>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       （上下文提供程序）：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      如果您的用户界面包含自定义请求/响应查看器，则此接口至关重要。它告诉 Burp 用户当前正在查看或交互的自定义选项卡中的哪个特定 HTTP 消息。
     </span>
    </font>
   </font>
  </li>
 </ul>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     3. 组装用户界面：导入 Swing 和 AWT
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Java 的 UI 框架叫做 Swing。它以冗长著称，但一旦你理解了布局管理器，就会发现它功能极其强大。由于 Jython 可以桥接 Python 和 Java，我们可以将 Java 的 Swing 组件直接导入到 Python 脚本中。
    </span>
   </font>
  </font>
 </p>
 <p>
  
   <span>
    <br />
   </span>
  
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Python
    </span>
   </font>
  </font>
 </p>
 <pre><span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>from</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> java.awt </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>import </span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span><font dir="auto" style="vertical-align: inherit;"><span>BorderLayout</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>GridLayout</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>Color </span></font></span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><span>from</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> javax.swing </span></font></font><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>import </span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span><font dir="auto" style="vertical-align: inherit;"><span>JPanel</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JSplitPane</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JButton</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JTextArea</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JScrollPane</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JTextField</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>JLabel</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> , </span></font><span><font dir="auto" style="vertical-align: inherit;"><span>SwingUtilities</span></font></span></font><span><br /></span></span></pre>
 <ul class="list-paddingleft-1" style="margin: 0px; padding: 0px;">
  <li>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       容器：
      </span>
     </font>
    </font>
   </strong>
   <section>
    <span>
    </span>
    <code>
     <span>
      JPanel
     </span>
    </code>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       是你的空白画布。所有内容都放在一个面板中。
      </span>
     </font>
    </font>
    <code>
     <span>
      JSplitPane
     </span>
    </code>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       非常适合分割屏幕（例如，请求在左侧，响应在右侧，或者控件在顶部，日志在底部）。
      </span>
     </font>
    </font>
   </section>
  </li>
  <li>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       交互元素：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      我们引入
     </span>
    </font>
   </font>
   <code>
    <span>
     JButton
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      执行触发器、
     </span>
    </font>
   </font>
   <code>
    <span>
     JTextArea
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      多行日志或有效载荷输出以及
     </span>
    </font>
   </font>
   <code>
    <span>
     JTextField
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      单行用户输入。
     </span>
    </font>
   </font>
  </li>
  <li>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       布局管理器：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      Java 默认不使用绝对定位。您可以使用诸如
     </span>
    </font>
   </font>
   <code>
    <span>
     BorderLayout
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      （北、南、东、西、中心）之类的属性，以便
     </span>
    </font>
   </font>
   <code>
    <span>
     GridLayout
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      在用户调整 Burp 窗口大小时自动调整组件大小。
     </span>
    </font>
   </font>
  </li>
 </ul>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     4. 危险区域：掌握事件分发线程 (EDT)
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     如果添加自定义界面，线程管理就会成为最大的敌人。90% 的 Burp 自定义扩展都失败于此。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     在 Java Swing 中，视觉更新
    </span>
   </font>
  </font>
  <em style="font-style: italic;">
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      必须
     </span>
    </font>
   </font>
  </em>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     在称为事件分发线程 (EDT) 的特定线程上进行。Burp Suite 会执行大量异步工作。当 HTTP 请求完成时，回调通常会在后台工作线程上执行。如果在
    </span>
   </font>
  </font>
  <code>
   <span>
    JTextArea
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     工具正在处理数据时尝试从该后台线程更新视图，Burp Suite 可能会冻结、抛出并发修改异常，甚至直接崩溃。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     最简单的解决方法是创建一个线程安全的辅助类。查看我们的基础代码，我们创建了一个名为 `ThreadSafe` 的类，
    </span>
   </font>
  </font>
  <code>
   <span>
    RunInEDT
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     该类实现了 Java 的 `
    </span>
   </font>
  </font>
  <code>
   <span>
    Runnable
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     ThreadSafe` 接口。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Python
    </span>
   </font>
  </font>
 </p>
 <pre><span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>class </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>RunIn</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> EDT(Runnable): </span></font></font><span><br /></span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>def </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>__init__</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ( </span></font></font><span style="color: rgb(92, 38, 153);"><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , func, *args, **kwargs</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ): </span></font></font><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self.func</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = func </span></font></font><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self.args</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = args </span></font></font><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self.kwargs</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = kwargs</span></font></font></span></pre>
 <pre><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>    def run(self): </span></font></font><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        self.func(*self.args, **self.kwargs)</span></font></font></span></pre>
 <p>
  <strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      工作原理：
     </span>
    </font>
   </font>
  </strong>
 </p>
 <ol class="list-paddingleft-1" style="margin: 0px; padding: 0px;">
  <li>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       包装器：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      该
     </span>
    </font>
   </font>
   <code>
    <span>
     __init__
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      方法只是简单地存储你要运行的 Python 函数及其所需的任何参数。
     </span>
    </font>
   </font>
  </li>
  <li>
   <strong>
    <font dir="auto" style="vertical-align: inherit;">
     <font dir="auto" style="vertical-align: inherit;">
      <span>
       执行：
      </span>
     </font>
    </font>
   </strong>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      该
     </span>
    </font>
   </font>
   <code>
    <span>
     run
    </span>
   </code>
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      方法是 Java 在线程启动时实际执行的代码。它会解包这些参数并触发你的函数。
     </span>
    </font>
   </font>
  </li>
 </ol>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     为了安全地使用此功能，您需要将 UI 更新逻辑封装起来，并将其传递给 Swing 的调用队列：
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Python
    </span>
   </font>
  </font>
 </p>
 <pre><span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span># 假设你有一个名为 'update_log' 的函数</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><span><font dir="auto" style="vertical-align: inherit;"><span>SwingUtilities.invokeLater(RunInEDT</span></font></span></font><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ( </span></font><font dir="auto" style="vertical-align: inherit;"><span>self.update_log </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>,</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> "</span></font><span style="color: rgb(92, 38, 153);"><font dir="auto" style="vertical-align: inherit;"><span>有效</span></font></span><font dir="auto" style="vertical-align: inherit;"><span>载荷</span></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><span>注入成功！"</span></font></span><font dir="auto" style="vertical-align: inherit;"><span> ))</span></font></font></span></pre>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     这段代码告诉 Java：
    </span>
   </font>
  </font>
  <em style="font-style: italic;">
   <font dir="auto" style="vertical-align: inherit;">
    <font dir="auto" style="vertical-align: inherit;">
     <span>
      “嘿，一旦 UI 线程有空闲的一毫秒，请执行此更新。”
     </span>
    </font>
   </font>
  </em>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     它会将 UI 更改安全地排队，而你的繁重测试逻辑则可以在后台继续安全运行。
    </span>
   </font>
  </font>
 </p>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     5. 构建扩展类
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     最后，所有内容都会整合到你的主类中。你需要定义
    </span>
   </font>
  </font>
  <code>
   <span>
    class BurpExtender
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     它并让它继承我们讨论过的接口。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     对于功能齐全的扩展，您的类定义如下所示：
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     Python
    </span>
   </font>
  </font>
 </p>
 <pre><span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>class </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>BurpExtender</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> (IBurpExtender, ITab, IContextMenuFactory, IMessageEditorController): </span></font></font><span><br /></span><span style="color: rgb(170, 13, 145);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>def </span></font></font></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>registerExtenderCallbacks</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ( </span></font></font><span style="color: rgb(92, 38, 153);"><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> , callbacks</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ): </span></font></font><span><br /></span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span># 1. 保存回调对象。它是你访问 Burp API 的关键。self._callbacks </span></font></font></span><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>=</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> callbacks </span></font></font><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self._helpers</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> = callbacks.getHelpers() </span></font></font><span><br /></span><span><br /></span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span># 2. 设置扩展名称</span></font></font></span><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        callbacks.setExtensionName( </span></font></font><span style="color: rgb(196, 26, 22);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>"自定义工作流自动化"</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ) </span></font></font><span><br /></span><span><br /></span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span># 3. 构建 UI </span></font></font></span><span><br /></span><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self.build_ui</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> () </span></font></font><span><br /></span><span><br /></span><span style="color: rgb(0, 116, 0);"><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span># 4. 注册接口</span></font></font></span><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        callbacks.addSuiteTab( </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> ) </span></font></font><span><br /></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>        callbacks.registerContextMenuFactory( </span></font></font><span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span>self</span></font></font></span><font dir="auto" style="vertical-align: inherit;"><font dir="auto" style="vertical-align: inherit;"><span> )</span></font></font></span></pre>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     在内部
    </span>
   </font>
  </font>
  <code>
   <span>
    build_ui()
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     ，您可以构建自己的组件
    </span>
   </font>
  </font>
  <code>
   <span>
    JPanel
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     、配置组件
    </span>
   </font>
  </font>
  <code>
   <span>
    BorderLayout
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     ，并为按钮添加操作监听器。例如，点击按钮可能会创建一个新的 Python 线程（使用
    </span>
   </font>
  </font>
  <code>
   <span>
    threading
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     我们导入的模块）来遍历有效负载列表，并使用 HTTP 请求发送请求
    </span>
   </font>
  </font>
  <code>
   <span>
    self._callbacks.makeHttpRequest()
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     。每个请求返回后，您可以使用我们的
    </span>
   </font>
  </font>
  <code>
   <span>
    RunInEDT
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     类将结果安全地推送到自定义表格或文本区域中。
    </span>
   </font>
  </font>
 </p>
 <section>
  <span>
   <br />
  </span>
 </section>
 <h2>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     6. 调试和迭代
    </span>
   </font>
  </font>
 </h2>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     当程序出错时（而出错是必然的），Jython 错误不会在简洁的 IDE 终端中显示。你需要密切关注 Burp 中的“扩展程序”选项卡。选择你的扩展程序，然后查看“错误”面板。你的 Python 代码抛出的任何异常，或者
    </span>
   </font>
  </font>
  <code>
   <span>
    print()
   </span>
  </code>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     你用于调试的任何标准语句，都会显示在此处的“输出”和“错误”面板中。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     一旦这个框架搭建完成，可能性就无穷无尽了。你可以构建自定义右键菜单，快速注入恶意代码。你可以编写脚本来拦截特定请求，实时解码各种复杂的专有格式，修改数据，重新编码，然后发送出去。你无需再与用户界面较劲，而是让你的自定义代码来完成繁重的工作。
    </span>
   </font>
  </font>
 </p>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     密切关注错误日志，谨慎管理线程，祝您编程愉快。
    </span>
   </font>
  </font>
 </p>
 <ul class="list-paddingleft-1">
  <li>
   <p>
    <span>
     公众号:安全狗的自我修养
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     vx:2207344074
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     <span>
      http://
     </span>
    </span>
    <span>
     gitee.com/haidragon
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     <span>
      http://
     </span>
    </span>
    <span>
     github.com/haidragon
    </span>
   </p>
  </li>
  <li>
   <p>
    <span>
     bilibili:haidragonx
    </span>
   </p>
  </li>
 </ul>
 <p>
  <span>
   <br />
  </span>
 </p>
 <p>
  <span>
   <br />
  </span>
 </p>
 <section>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvJXGah2vOMRI6Zb4dNNfPugKkQiacw4PxDAWce5uTkhbVnWU8Rqvr9wiceeqarMa0oxcOSia9hw2vwOibric31PUiaPJPLic6MkElO7M/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=5" />
 </section>
 <section>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnssmE9DkmQYx2gRFfcX5kRuYkPnTiaHPymTq2BzvAiahicu5B6HHSHYJCqp6nNwktKhuomL2UHTMetYjBhRLoDkm4hgEOzibria7NXc/640?wx_fmt=png&amp;from=appmsg&amp;watermark=1&amp;wxfrom=5&amp;wx_lazy=1&amp;tp=webp#imgIndex=7" />
 </section>
 <section>
  <span>
   <br />
  </span>
 </section>
 <section>
  <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=z84f6pb5&amp;tp=webp#imgIndex=5" />
 </section>
 <p>
  <span>
   <br />
  </span>
 </p>
 <p>
  <span>
   <br />
  </span>
 </p>
 <ul class="list-paddingleft-1">
  <ul class="list-paddingleft-1">
   <li>
    <section>
     <img src="https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1&amp;randomid=omk5zkfc&amp;tp=webp#imgIndex=5" />
    </section>
   </li>
  </ul>
 </ul>
 <p>
  <font dir="auto" style="vertical-align: inherit;">
   <font dir="auto" style="vertical-align: inherit;">
    <span>
     <br />
    </span>
   </font>
  </font>
 </p>
</section>
<p style="display: none;">
 
 
</p>
