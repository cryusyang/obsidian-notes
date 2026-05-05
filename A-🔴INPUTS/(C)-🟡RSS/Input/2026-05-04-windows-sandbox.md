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
> Windows Sandbox 是 Windows 10/11 Pro/Enterprise/Education 内置的轻量级、一次性虚拟化环境，基于 Hyper-V 实现内核级隔离，但不依赖完整 Windows 镜像，而是动态复用宿主机系统文件，兼具 VM 级安全性与容器级启动速度和资源效率。其架构融合容器与虚拟机特性，支持内存共享、动态内存回收、WDDM GPU 虚拟化及电池状态透传等优化。默认启用网络、剪贴板和音频输入，禁用视频输入和打印重定向，关闭即彻底清除所有数据；可通过 .wsb XML 配置文件或 Windows 11 24H2+ 新增的 `wsb` 命令行工具实现可复现、可脚本化的沙盒部署。

---

<p><em>This is a note from my </em><a href="https://notes.dsebastien.net/?ref=dsebastien.net"><em>public notes</em></a><em>. View the canonical version: </em><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Windows+Sandbox?ref=dsebastien.net"><em>Windows Sandbox</em></a><em>.</em></p><p>Windows Sandbox (WSB) is a disposable, hypervisor-isolated desktop environment built into Windows 10/11 Pro, Enterprise, and Education editions. It launches in seconds, runs a full Windows desktop in a separate kernel, and wipes everything on close. It is Microsoft&apos;s answer to &quot;I want to test this random <code>.exe</code> without burning a VM.&quot;</p><p>The defining trick: WSB is not a regular VM. It uses <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net">Hyper-V</a> for kernel-level isolation, but it does <strong>not</strong> ship a Windows image. Instead, it boots from a dynamically constructed image assembled from the host&apos;s already-installed Windows files &#x2014; making it closer to a <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net">container</a> than to a traditional virtual machine.</p><h2 id="architecture-container%E2%80%93vm-hybrid">Architecture: container&#x2013;VM hybrid</h2><ul><li><strong>Dynamic Base Image</strong> &#x2014; most Windows OS files are immutable; the sandbox shares them directly with the host. Only the small mutable subset is shipped as a pristine package: 30 MB compressed &#x2192; 500 MB on disk after install. No second copy of Windows.</li><li><strong>Direct map memory sharing</strong> &#x2014; when <code>ntdll.dll</code> (and other binaries) load inside the sandbox, the sandbox is mapped to the same physical memory pages as the host&apos;s copy. No duplication, no leakage of host secrets.</li><li><strong>Dynamic memory reclamation</strong> &#x2014; host can reclaim sandbox memory under pressure, like it would from a process. Traditional VMs allocate statically and can&apos;t give it back.</li><li><strong>WDDM GPU virtualization</strong> &#x2014; graphics inside the sandbox compete with host apps for the real GPU (requires WDDM 2.5+). Falls back to WARP CPU-rendering on incompatible systems.</li><li><strong>Battery pass-through</strong> &#x2014; the sandbox sees the host battery state and tunes power accordingly.</li><li><strong>Hardware-rooted isolation</strong> &#x2014; runs on the Microsoft hypervisor with a separate kernel; the host kernel is not exposed.</li></ul><p>The result: VM-grade isolation with container-grade footprint and start time.</p><h2 id="default-behavior">Default behavior</h2><ul><li>Networking: <strong>on</strong> (via Hyper-V default switch &#x2014; exposes guest to internal network)</li><li>Clipboard redirection: <strong>on</strong></li><li>Audio input: <strong>on</strong>, video input: <strong>off</strong></li><li>vGPU: <strong>on</strong> (non-Arm64)</li><li>Printer redirection: <strong>off</strong></li><li>Memory cap: <strong>4 GB</strong></li><li>Single instance only &#x2014; no parallel sandboxes from the GUI</li><li>Closing the window deletes all software, files, and state. No persistence across sessions (reboots <em>within</em> a session do persist, since Windows 11 22H2)</li></ul><h2 id="configuration-wsb-files">Configuration: <code>.wsb</code> files</h2><p>Sandboxes are declared as XML in <code>.wsb</code> files. Double-click to launch. This makes one-off sandboxes reproducible and scriptable.</p><pre><code class="language-xml">&lt;Configuration&gt;
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
</code></pre><p>Configurable knobs: <code>vGPU</code>, <code>Networking</code>, <code>MappedFolders</code> (with read-only flag), <code>LogonCommand</code>, <code>AudioInput</code>, <code>VideoInput</code>, <code>ProtectedClient</code> (runs sandbox inside AppContainer for an extra isolation boundary, restricts copy/paste), <code>PrinterRedirection</code>, <code>ClipboardRedirection</code>, <code>MemoryInMB</code> (auto-bumped to 2048 minimum). Default sandbox user is <code>WDAGUtilityAccount</code>.</p><h2 id="cli-wsb-windows-11-24h2">CLI (<code>wsb</code>, Windows 11 24H2+)</h2><p>A command-line interface turns the sandbox into something scriptable from CI, automation, or AI agents:</p><ul><li><code>wsb start [--config &quot;&lt;XML&gt;&quot;]</code> &#x2014; launches a sandbox, returns its ID</li><li><code>wsb list</code> &#x2014; running sandboxes (table or <code>--raw</code> JSON)</li><li><code>wsb exec --id &lt;id&gt; -c &lt;cmd&gt; -r &lt;ExistingLogin|System&gt;</code> &#x2014; run a command inside (no stdout capture; requires active session for user context)</li><li><code>wsb share --id &lt;id&gt; -f &lt;host&gt; -s &lt;sandbox&gt; [--allow-write]</code> &#x2014; mount a folder after launch</li><li><code>wsb connect --id &lt;id&gt;</code> &#x2014; RDP into the sandbox window</li><li><code>wsb stop --id &lt;id&gt;</code> &#x2014; terminate</li><li><code>wsb ip --id &lt;id&gt;</code> &#x2014; get the sandbox IP</li></ul><p>This collapses a long-standing gap: pre-CLI, the only way to drive WSB was the GUI launcher and a <code>LogonCommand</code>.</p><h2 id="when-to-reach-for-it">When to reach for it</h2><ul><li>Detonating untrusted installers, email attachments, or random <code>.exe</code> files</li><li>Browsing sketchy URLs without polluting the host browser profile</li><li>Testing software that &quot;totally won&apos;t&quot; leave registry keys / scheduled tasks behind</li><li>Per-project dev environments (different Python/Node versions, isolated dependency trees)</li><li>Quick reproductions where spinning up a real VM is overkill</li></ul><p>Not the right tool for: long-running workloads, anything you want to keep, multi-VM scenarios, or Windows Home users (use <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net">Docker</a> / a real VM / <strong>LXC</strong> instead).</p><h2 id="limitations">Limitations</h2><ul><li>Pro/Enterprise/Education only &#x2014; <strong>not on Windows Home</strong></li><li>Single sandbox at a time from the GUI</li><li>Networking on by default &#x2014; easy footgun for malware analysis (always disable in <code>.wsb</code> for that use case)</li><li>No process I/O capture from <code>wsb exec</code> &#x2014; fire-and-forget only</li><li><code>MappedFolders</code> with write enabled persist after the sandbox is destroyed</li><li>Sandbox window size is not configurable</li></ul><h2 id="open-source-surface">Open source surface</h2><ul><li>The sandbox engine itself ships with Windows and is closed-source</li><li>The <a href="https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net">microsoft/Windows-Sandbox</a> GitHub repo is <a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net">MIT</a>-licensed and hosts community add-ons, sample <code>.wsb</code> files, GUI utilities (e.g., &quot;Run in Sandbox&quot; context menu, PyWinSandbox), and issue tracking &#x2014; not the core code</li></ul><h2 id="references">References</h2><ul><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions</a></li><li><a href="https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot?ref=dsebastien.net">https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot</a></li><li><a href="https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net">https://github.com/microsoft/Windows-Sandbox</a></li></ul><h2 id="related">Related</h2><ul><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net">Hyper-V</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net">Containerization</a></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net">Docker</a></li><li><strong>LXC (Linux Containers)</strong></li><li><a href="https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net">MIT License</a></li></ul>

## 中文译文

这是我的公开笔记中的一则说明。查看权威版本：Windows 沙盒（Windows Sandbox）。

Windows 沙盒（WSB）是一种一次性、基于虚拟机监控程序（hypervisor）隔离的桌面环境，内置于 Windows 10/11 专业版、企业版和教育版中。它可在数秒内启动，在独立内核中运行完整的 Windows 桌面，并在关闭时彻底清除所有内容。这是微软对“我想测试这个来路不明的 .exe 文件，又不想费力部署一台虚拟机”这一需求的直接回应。

其核心设计亮点在于：WSB 并非传统意义上的虚拟机（VM）。它利用 Hyper-V 实现内核级隔离，但并不自带 Windows 镜像；相反，它从宿主机已安装的 Windows 文件动态构建启动镜像——因此，其本质更接近容器（container），而非传统虚拟机。

架构：容器–虚拟机混合体

动态基础镜像（Dynamic Base Image）——绝大多数 Windows 系统文件为只读且不可变；沙盒直接与宿主机共享这些文件。仅需分发体积很小的可变部分，以纯净包形式提供：压缩后约 30 MB，解压后占用磁盘空间约 500 MB。无需额外复制一份完整的 Windows 系统。

内存直映共享（Direct map memory sharing）——当 ntdll.dll（及其他二进制文件）在沙盒中加载时，沙盒将被映射至与宿主机副本相同的物理内存页上。既无内存冗余拷贝，也不会泄露宿主机敏感信息。

动态内存回收（Dynamic memory reclamation）——在内存压力下，宿主机可像回收普通进程内存一样，主动回收沙盒所占内存。而传统虚拟机通常采用静态内存分配，无法动态释放。

WDDM GPU 虚拟化（WDDM GPU virtualization）——沙盒内的图形渲染与宿主机应用共同竞争真实 GPU 资源（需 WDDM 2.5 或更高版本）；在不兼容的系统上自动回退至 WARP（Windows Advanced Rasterization Platform）CPU 渲染。

电池状态透传（Battery pass-through）——沙盒可感知宿主机的电池状态，并据此动态调节功耗策略。

硬件根植型隔离（Hardware-rooted isolation）——运行于微软虚拟机监控程序之上，拥有独立内核；宿主机内核不会暴露给沙盒。

最终效果：兼具虚拟机级别的安全隔离能力，同时拥有容器级别的轻量足迹与极速启动性能。

默认行为

网络连接：启用（通过 Hyper-V 默认交换机——使沙盒接入内部网络）

剪贴板重定向：启用

音频输入：启用；视频输入：禁用

虚拟 GPU（vGPU）：启用（Arm64 架构除外）

打印机重定向：禁用

内存上限：4 GB

仅支持单实例运行——图形界面（GUI）下无法并行启动多个沙盒

关闭窗口即彻底删除所有软件、文件及运行状态。各会话之间完全无持久化（但在同一会话内重启系统仍保留状态，自 Windows 11 22H2 版本起生效）

配置方式：.wsb 文件

沙盒配置以 XML 格式声明于 .wsb 文件中，双击即可启动。该机制使得一次性使用的沙盒具备可复现性与可脚本化能力。

可配置参数包括：vGPU、Networking（网络）、MappedFolders（映射文件夹，支持只读标志）、LogonCommand（登录后执行命令）、AudioInput（音频输入）、VideoInput（视频输入）、ProtectedClient（启用后，沙盒将在 AppContainer 中运行，提供额外隔离层，并限制剪贴板复制/粘贴）、PrinterRedirection（打印机重定向）、ClipboardRedirection（剪贴板重定向）、MemoryInMB（内存限制，单位 MB；若设置过低，系统将自动提升至最低 2048 MB）。默认沙盒用户账户为 WDAGUtilityAccount。

命令行接口（CLI，wsb 命令，Windows 11 24H2 及更新版本支持）

命令行接口使沙盒可被持续集成（CI）、自动化流程或 AI 代理调用，大幅拓展其适用场景：

wsb start [--config "<XML>"] —— 启动沙盒，返回其唯一 ID  
wsb list —— 列出当前正在运行的沙盒（支持表格格式或 --raw 输出 JSON 格式）  
wsb exec --id <id> -c <cmd> -r <ExistingLogin|System> —— 在指定沙盒中执行命令（不捕获标准输出；需处于活跃会话中，方可获取用户上下文）  
wsb share --id <id> -f <host> -s <sandbox> [--allow-write] —— 启动后挂载宿主机文件夹至沙盒  
wsb connect --id <id> —— 使用远程桌面协议（RDP）连接至沙盒窗口  
wsb stop --id <id> —— 终止指定沙盒  
wsb ip --id <id> —— 获取指定沙盒的 IP 地址  

此举填补了长期存在的空白：在 CLI 功能推出前，驱动 WSB 的唯一方式仅为 GUI 启动器配合 LogonCommand。

何时选用 Windows 沙盒？

- 运行不受信任的安装程序、电子邮件附件或来源不明的 .exe 文件（即“引爆”可疑程序）  
- 访问可疑网址，避免污染宿主机浏览器配置文件  
- 测试那些声称“绝不会”在注册表或计划任务中留下痕迹的软件  
- 按项目建立开发环境（例如不同 Python/Node.js 版本、彼此隔离的依赖树）  
- 快速复现问题场景，此时启动完整虚拟机显得过于繁重  

不适用于以下场景：长时间运行的任务、需要保留数据的工作流、多虚拟机协同场景，以及 Windows 家庭版用户（建议改用 Docker、完整虚拟机或 LXC 等替代方案）。

局限性

- 仅限 Windows 专业版、企业版与教育版；Windows 家庭版不支持  
- 图形界面下仅允许单个沙盒实例运行  
- 网络默认启用——进行恶意软件分析时易构成风险（务必在 .wsb 配置文件中显式禁用）  
- wsb exec 不支持捕获进程的标准输入/输出（I/O），仅支持“触发即忘”（fire-and-forget）模式  
- 启用写权限的 MappedFolders（映射文件夹）在沙盒销毁后仍保留在宿主机上  
- 沙盒窗口尺寸不可调节  

开源情况

- 沙盒引擎本身随 Windows 系统分发，为闭源组件  
- GitHub 上的 microsoft/Windows-Sandbox 仓库采用 MIT 许可证，托管社区贡献的扩展插件、示例 .wsb 配置文件、GUI 工具（如“在沙盒中运行”右键菜单、PyWinSandbox）、问题追踪等——但**不包含核心引擎代码**

参考资料

https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions  
https://learn.microsoft.com/zh-cn/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot  
https://github.com/microsoft/Windows-Sandbox  

相关技术

Hyper-V  
容器化（Containerization）  
Docker  
LXC（Linux Containers）  
MIT 许可证
