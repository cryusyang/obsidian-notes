---
title: "Windows Sandbox"
url: "https://www.dsebastien.net/windows-sandbox/"
source: "Sebastien Dubois"
date: 2026-05-04
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Windows Sandbox 是 Windows 10/11 Pro/Enterprise/Education 内置的轻量级、一次性虚拟化环境，基于 Hyper-V 实现内核级隔离，但不依赖完整 Windows 镜像，而是动态复用宿主机系统文件，兼具 VM 级安全性与容器级启动速度和资源效率。其架构融合容器与虚拟机特性，支持内存共享、动态内存回收、WDDM GPU 虚拟化及硬件根隔离等优化。默认启用网络、剪贴板和音频输入，禁用视频和打印重定向，关闭即彻底清除所有数据；通过 `.wsb` XML 配置文件或 Windows 11 24H2+ 新增的 `wsb` 命令行工具，可实现沙盒的声明式创建、自动化部署与脚本化管理。

---

<p><em>本文摘自我公开的 </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>笔记库</em></a><em>。查看权威原文：</em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Windows+Sandbox?ref=dsebastien.net"><em>Windows Sandbox</em></a><em>。</em></p>

<p>Windows Sandbox（WSB）是一种一次性、基于虚拟机监控程序（hypervisor）隔离的桌面环境，内置于 Windows 10/11 专业版、企业版和教育版中。它可在数秒内启动，在独立内核中运行完整的 Windows 桌面，并在关闭时彻底清除所有内容。这是微软对“我想测试这个来路不明的 <code>.exe</code> 文件，但又不想费力搭建一台虚拟机”这一需求的直接回应。</p>

<p>其核心奥秘在于：WSB 并非传统意义上的虚拟机。它利用 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net">Hyper-V</a> 实现内核级隔离，但**并不自带** Windows 镜像；相反，它从宿主机已安装的 Windows 文件动态构建启动镜像——这使其更接近于一种 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net">容器（container）</a>，而非传统虚拟机。</p>

<h2 id="architecture-container%E2%80%93vm-hybrid">架构：容器–虚拟机混合体</h2>

<ul>
<li><strong>动态基础镜像（Dynamic Base Image）</strong> —— 大多数 Windows 系统文件为只读不可变；沙盒直接与宿主机共享这些文件。仅将少量可变文件以纯净包形式分发：压缩后约 30 MB → 解压后磁盘占用约 500 MB。无需额外复制一份 Windows 系统。</li>
<li><strong>内存页直映射共享（Direct map memory sharing）</strong> —— 当 <code>ntdll.dll</code>（及其他二进制文件）在沙盒内加载时，沙盒被映射至与宿主机副本相同的物理内存页。既无冗余复制，亦不会泄露宿主机敏感信息。</li>
<li><strong>动态内存回收（Dynamic memory reclamation）</strong> —— 宿主机可在内存压力下主动回收沙盒所占内存，方式与回收普通进程内存一致。而传统虚拟机通常静态分配内存且无法归还。</li>
<li><strong>WDDM GPU 虚拟化（WDDM GPU virtualization）</strong> —— 沙盒内的图形渲染与宿主机应用共享真实 GPU（需 WDDM 2.5 或更高版本）。在不兼容系统上自动回退至 WARP CPU 渲染。</li>
<li><strong>电池状态透传（Battery pass-through）</strong> —— 沙盒可感知宿主机电池状态，并据此智能调节功耗策略。</li>
<li><strong>硬件根植隔离（Hardware-rooted isolation）</strong> —— 运行于微软虚拟机监控程序之上，拥有独立内核；宿主机内核本身不向沙盒暴露。</li>
</ul>

<p>最终效果：兼具虚拟机级别的安全隔离，同时拥有容器级别的资源占用与启动速度。</p>

<h2 id="default-behavior">默认行为</h2>

<ul>
<li>网络连接：<strong>启用</strong>（通过 Hyper-V 默认交换机实现 —— 使客户机暴露于内部网络）</li>
<li>剪贴板重定向：<strong>启用</strong></li>
<li>音频输入：<strong>启用</strong>；视频输入：<strong>禁用</strong></li>
<li>虚拟 GPU（vGPU）：<strong>启用</strong>（Arm64 架构除外）</li>
<li>打印机重定向：<strong>禁用</strong></li>
<li>内存上限：<strong>4 GB</strong></li>
<li>单实例限制 —— GUI 界面下无法并行运行多个沙盒</li>
<li>关闭窗口即删除所有软件、文件及运行状态，会话间无持久化（但 Windows 11 22H2 起，同一沙盒会话内的重启操作仍保留状态）</li>
</ul>

<h2 id="configuration-wsb-files">配置方式：<code>.wsb</code> 文件</h2>

<p>沙盒配置以 XML 格式声明于 <code>.wsb</code> 文件中，双击即可启动。此举使得一次性沙盒具备可复现性与可脚本化能力。</p>

<pre><code class="language-xml">&lt;Configuration&gt;
  &lt;vGPU&gt;Disable&lt;/vGPU&gt;
  &lt;Networking&gt;Disable&lt;/Networking&gt;
  &lt;MappedFolders&gt;
    &lt;MappedFolder&gt;
      &lt;HostFolder&gt;C:\Suspicious&lt;/HostFolder&gt;
      &lt;SandboxFolder&gt;C:\Users\WDAGUtilityAccount\Desktop\Suspicious&lt;/SandboxFolder&gt;
      &lt;ReadOnly&gt;true&lt;/ReadOnly&gt;
    &lt;/MappedFolder&gt;
  &lt;/MappedFolders&gt;
  &lt;LogonCommand&gt;
    &lt;Command&gt;C:\Users\WDAGUtilityAccount\Desktop\Suspicious\run.cmd&lt;/Command&gt;
  &lt;/LogonCommand&gt;
  &lt;MemoryInMB&gt;8192&lt;/MemoryInMB&gt;
  &lt;ProtectedClient&gt;Enable&lt;/ProtectedClient&gt;
  &lt;ClipboardRedirection&gt;Disable&lt;/ClipboardRedirection&gt;
&lt;/Configuration&gt;
</code></pre>

<p>可配置参数包括：<code>vGPU</code>、<code>Networking</code>、<code>MappedFolders</code>（支持只读标记）、<code>LogonCommand</code>、<code>AudioInput</code>、<code>VideoInput</code>、<code>ProtectedClient</code>（在 AppContainer 中运行沙盒，提供额外隔离层并限制剪贴板操作）、<code>PrinterRedirection</code>、<code>ClipboardRedirection</code>、<code>MemoryInMB</code>（若设值低于 2048，则自动提升至该最小值）。沙盒默认用户为 <code>WDAGUtilityAccount</code>。</p>

<h2 id="cli-wsb-windows-11-24h2">命令行接口（CLI，<code>wsb</code>，Windows 11 24H2 及以上版本）</h2>

<p>命令行接口将沙盒转变为 CI 流水线、自动化脚本乃至 AI 代理均可调用的工具：</p>

<ul>
<li><code>wsb start [--config &quot;&lt;XML&gt;&quot;]</code> —— 启动沙盒，返回其唯一 ID</li>
<li><code>wsb list</code> —— 列出当前运行中的沙盒（表格格式或 <code>--raw</code> JSON 格式）</li>
<li><code>wsb exec --id &lt;id&gt; -c &lt;cmd&gt; -r &lt;ExistingLogin|System&gt;</code> —— 在沙盒内执行命令（不捕获标准输出；需处于活跃会话中以获取用户上下文）</li>
<li><code>wsb share --id &lt;id&gt; -f &lt;host&gt; -s &lt;sandbox&gt; [--allow-write]</code> —— 启动后挂载指定文件夹</li>
<li><code>wsb connect --id &lt;id&gt;</code> —— 通过 RDP 连入沙盒桌面窗口</li>
<li><code>wsb stop --id &lt;id&gt;</code> —— 终止指定沙盒</li>
<li><code>wsb ip --id &lt;id&gt;</code> —— 获取沙盒 IP 地址</li>
</ul>

<p>此举填补了长期存在的空白：在 CLI 出现前，驱动 WSB 的唯一途径仅有 GUI 启动器和 <code>LogonCommand</code>。</p>

<h2 id="when-to-reach-for-it">适用场景</h2>

<ul>
<li>运行不受信任的安装程序、邮件附件或来源不明的 <code>.exe</code> 文件（即“引爆”分析）</li>
<li>访问可疑网址，避免污染宿主机浏览器配置文件</li>
<li>测试声称“绝不会”遗留注册表项或计划任务的软件</li>
<li>按项目构建开发环境（例如不同 Python/Node.js 版本、相互隔离的依赖树）</li>
<li>快速复现问题场景，此时启动完整虚拟机显得大材小用</li>
</ul>

<p>以下情形请勿使用：需长期运行的工作负载、需要保留数据的任务、多虚拟机协同场景，或 Windows 家庭版用户（此时应改用 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net">Docker</a> / 真实虚拟机 / <strong>LXC</strong>）。</p>

<h2 id="limitations">局限性</h2>

<ul>
<li>仅限专业版、企业版与教育版 —— <strong>不支持 Windows 家庭版</strong></li>
<li>GUI 界面下一次仅能运行一个沙盒</li>
<li>网络功能默认开启 —— 对恶意软件分析而言易构成“误触陷阱”（该用途下务必在 <code>.wsb</code> 中显式禁用）</li>
<li><code>wsb exec</code> 不支持捕获进程 I/O —— 仅支持“发射即遗忘”（fire-and-forget）模式</li>
<li>启用写权限的 <code>MappedFolders</code> 在沙盒销毁后仍保留在宿主机上</li>
<li>沙盒窗口尺寸不可自定义</li>
</ul>

<h2 id="open-source-surface">开源表面</h2>

<ul>
<li>沙盒引擎本身随 Windows 发布，属闭源组件</li>
<li><a href="https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net">microsoft/Windows-Sandbox</a> GitHub 仓库采用 <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net">MIT 许可证</a>，托管社区贡献的附加组件、示例 <code>.wsb</code> 文件、GUI 工具（如“在沙盒中运行”右键菜单、PyWinSandbox）及问题追踪系统 —— 但**不含核心引擎代码**</li>
</ul>

<h2 id="references">参考文献</h2>

<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot</a></li>
<li><a href="https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net">https://github.com/microsoft/Windows-Sandbox</a></li>
</ul>

<h2 id="related">相关主题</h2>

<ul>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net">Hyper-V</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net">容器化（Containerization）</a></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net">Docker</a></li>
<li><strong>LXC（Linux 容器）</strong></li>
<li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net">MIT 许可证</a></li>
</ul>
