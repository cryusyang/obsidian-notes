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
> Windows Sandbox 是 Windows 10/11 Pro、企业版和教育版内置的轻量级、一次性、基于 Hyper-V 的隔离桌面环境，启动迅速且关闭即销毁全部数据。它并非传统虚拟机，而是采用“容器–VM 混合架构”：复用宿主机的只读系统文件，仅加载约30 MB压缩的可写层，并通过内存共享、动态内存回收和硬件级隔离实现高安全性与低资源开销。默认启用网络、剪贴板和音频输入，禁用视频和打印重定向，支持通过 `.wsb` XML 配置文件或 Windows 11 24H2+ 的 `wsb` 命令行工具进行定制化与自动化部署。

---

*This is a note from my [public notes](https://notes.dsebastien.net/?ref=dsebastien.net). View the canonical version: [Windows Sandbox](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Windows+Sandbox?ref=dsebastien.net).*

这是来自我的[公开笔记](https://notes.dsebastien.net/?ref=dsebastien.net)的一则备注。查看权威版本：[Windows 沙盒](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Windows+Sandbox?ref=dsebastien.net)。

Windows Sandbox (WSB) is a disposable, hypervisor-isolated desktop environment built into Windows 10/11 Pro, Enterprise, and Education editions. It launches in seconds, runs a full Windows desktop in a separate kernel, and wipes everything on close. It is Microsoft's answer to "I want to test this random `.exe` without burning a VM."

Windows 沙盒（WSB）是一种可随时丢弃、由虚拟机监控程序（hypervisor）隔离的桌面环境，内置于 Windows 10/11 专业版、企业版和教育版中。它可在数秒内启动，在独立内核中运行完整的 Windows 桌面，并在关闭时彻底清除所有内容。它是微软对“我想测试这个来路不明的 `.exe` 文件，又不想为此专门部署一台虚拟机”这一需求的回应。

The defining trick: WSB is not a regular VM. It uses [Hyper-V](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net) for kernel-level isolation, but it does **not** ship a Windows image. Instead, it boots from a dynamically constructed image assembled from the host's already-installed Windows files — making it closer to a [container](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net) than to a traditional virtual machine.

其核心设计精妙之处在于：WSB 并非传统意义上的虚拟机。它利用[Hyper-V](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net) 实现内核级隔离，但**并不自带** Windows 镜像；相反，它从宿主机已安装的 Windows 文件动态构建并启动镜像——这使其更接近于[容器](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net)，而非传统虚拟机。

## Architecture: container–VM hybrid

## 架构：容器–虚拟机混合体

- **Dynamic Base Image** — most Windows OS files are immutable; the sandbox shares them directly with the host. Only the small mutable subset is shipped as a pristine package: 30 MB compressed → 500 MB on disk after install. No second copy of Windows.

- **动态基础镜像**：大多数 Windows 系统文件为只读；沙盒直接与宿主机共享这些文件。仅将少量可变文件以纯净包形式分发：压缩后约 30 MB → 安装后占用磁盘空间约 500 MB。无需额外复制一份 Windows。

- **Direct map memory sharing** — when `ntdll.dll` (and other binaries) load inside the sandbox, the sandbox is mapped to the same physical memory pages as the host's copy. No duplication, no leakage of host secrets.

- **直接内存页映射共享**：当 `ntdll.dll`（及其他二进制文件）在沙盒中加载时，沙盒被映射至与宿主机副本相同的物理内存页。无内存冗余，亦无宿主机敏感信息泄露风险。

- **Dynamic memory reclamation** — host can reclaim sandbox memory under pressure, like it would from a process. Traditional VMs allocate statically and can't give it back.

- **动态内存回收**：宿主机可在内存压力下像回收普通进程内存一样回收沙盒内存。传统虚拟机则采用静态内存分配，无法主动释放。

- **WDDM GPU virtualization** — graphics inside the sandbox compete with host apps for the real GPU (requires WDDM 2.5+). Falls back to WARP CPU-rendering on incompatible systems.

- **WDDM 图形驱动虚拟化**：沙盒内的图形应用与宿主机应用共同竞争真实 GPU 资源（需 WDDM 2.5 或更高版本）；在不兼容系统上自动回退至 WARP（Windows Advanced Rasterization Platform）CPU 渲染。

- **Battery pass-through** — the sandbox sees the host battery state and tunes power accordingly.

- **电池状态透传**：沙盒可感知宿主机电池状态，并据此相应调节功耗策略。

- **Hardware-rooted isolation** — runs on the Microsoft hypervisor with a separate kernel; the host kernel is not exposed.

- **硬件级根隔离**：运行于微软虚拟机监控程序之上，拥有独立内核；宿主机内核完全不对外暴露。

The result: VM-grade isolation with container-grade footprint and start time.

最终效果：兼具虚拟机级别的隔离强度，以及容器级别的资源占用与启动速度。

## Default behavior

## 默认行为

- Networking: **on** (via Hyper-V default switch — exposes guest to internal network)

- 网络：**启用**（通过 Hyper-V 默认交换机实现——使沙盒可接入内部网络）

- Clipboard redirection: **on**

- 剪贴板重定向：**启用**

- Audio input: **on**, video input: **off**

- 音频输入：**启用**，视频输入：**禁用**

- vGPU: **on** (non-Arm64)

- 虚拟 GPU（vGPU）：**启用**（Arm64 架构除外）

- Printer redirection: **off**

- 打印机重定向：**禁用**

- Memory cap: **4 GB**

- 内存上限：**4 GB**

- Single instance only — no parallel sandboxes from the GUI

- 仅支持单实例——图形界面不支持并行运行多个沙盒

- Closing the window deletes all software, files, and state. No persistence across sessions (reboots *within* a session do persist, since Windows 11 22H2)

- 关闭窗口即删除全部软件、文件及状态。会话间无持久化（但自 Windows 11 22H2 起，同一会话内的重启操作仍保留数据）

## Configuration: `.wsb` files

## 配置：`.wsb` 文件

Sandboxes are declared as XML in `.wsb` files. Double-click to launch. This makes one-off sandboxes reproducible and scriptable.

沙盒通过 `.wsb` 文件中的 XML 格式定义。双击即可启动。此举使得一次性沙盒具备可复现性与可脚本化能力。

```xml
<Configuration>
  <vGPU>Disable</vGPU>
  <Networking>Disable</Networking>
  <MappedFolders>
    <MappedFolder>
      <HostFolder>C:\Suspicious</HostFolder>
      <SandboxFolder>C:\Users\WDAGUtilityAccount\Desktop\Suspicious</SandboxFolder>
      <ReadOnly>true</ReadOnly>
    </MappedFolder>
  </MappedFolders>
  <LogonCommand>
    <Command>C:\Users\WDAGUtilityAccount\Desktop\Suspicious\run.cmd</Command>
  </LogonCommand>
  <MemoryInMB>8192</MemoryInMB>
  <ProtectedClient>Enable</ProtectedClient>
  <ClipboardRedirection>Disable</ClipboardRedirection>
</Configuration>
```

可配置项包括：`vGPU`、`Networking`、`MappedFolders`（支持只读标记）、`LogonCommand`、`AudioInput`、`VideoInput`、`ProtectedClient`（在 AppContainer 中运行沙盒，提供额外隔离层并限制剪贴板操作）、`PrinterRedirection`、`ClipboardRedirection`、`MemoryInMB`（若设置过低将自动提升至最低 2048 MB）。沙盒默认用户为 `WDAGUtilityAccount`。

## CLI (`wsb`, Windows 11 24H2+)

## 命令行接口（`wsb`，Windows 11 24H2 及更高版本）

A command-line interface turns the sandbox into something scriptable from CI, automation, or AI agents:

命令行接口让沙盒可被持续集成（CI）、自动化流程或 AI 代理调用：

- `wsb start [--config "<XML>"]` — launches a sandbox, returns its ID

- `wsb start [--config "<XML>"]` — 启动沙盒，并返回其唯一 ID

- `wsb list` — running sandboxes (table or `--raw` JSON)

- `wsb list` — 列出正在运行的沙盒（表格格式或 `--raw` 输出 JSON）

- `wsb exec --id <id> -c <cmd> -r <ExistingLogin|System>` — run a command inside (no stdout capture; requires active session for user context)

- `wsb exec --id <id> -c <cmd> -r <ExistingLogin|System>` — 在沙盒内执行命令（不捕获标准输出；需处于活跃会话中以获取用户上下文）

- `wsb share --id <id> -f <host> -s <sandbox> [--allow-write]` — mount a folder after launch

- `wsb share --id <id> -f <host> -s <sandbox> [--allow-write]` — 启动后挂载文件夹

- `wsb connect --id <id>` — RDP into the sandbox window

- `wsb connect --id <id>` — 通过远程桌面协议（RDP）连接沙盒窗口

- `wsb stop --id <id>` — terminate

- `wsb stop --id <id>` — 终止沙盒

- `wsb ip --id <id>` — get the sandbox IP

- `wsb ip --id <id>` — 获取沙盒 IP 地址

This collapses a long-standing gap: pre-CLI, the only way to drive WSB was the GUI launcher and a `LogonCommand`.

此举弥合了长期存在的空白：在 CLI 出现之前，驱动 WSB 的唯一方式只有图形界面启动器和 `LogonCommand`。

## When to reach for it

## 何时选用 Windows 沙盒

- Detonating untrusted installers, email attachments, or random `.exe` files

- 运行不可信的安装程序、邮件附件或任意 `.exe` 文件（即“引爆”分析）

- Browsing sketchy URLs without polluting the host browser profile

- 访问可疑网址，且不污染宿主机浏览器配置文件

- Testing software that "totally won't" leave registry keys / scheduled tasks behind

- 测试那些声称“绝不会”在注册表或计划任务中遗留痕迹的软件

- Per-project dev environments (different Python/Node versions, isolated dependency trees)

- 按项目划分的开发环境（不同 Python/Node 版本、相互隔离的依赖树）

- Quick reproductions where spinning up a real VM is overkill

- 快速复现问题场景，此时部署完整虚拟机显得过于繁重

Not the right tool for: long-running workloads, anything you want to keep, multi-VM scenarios, or Windows Home users (use [Docker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net) / a real VM / **LXC** instead).

但以下场景**不适用**：需长期运行的工作负载、任何你希望保留的数据、多虚拟机协同场景，或 Windows 家庭版用户（请改用 [Docker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net) / 真实虚拟机 / **LXC（Linux 容器）**）。

## Limitations

## 局限性

- Pro/Enterprise/Education only — **not on Windows Home**

- 仅适用于专业版、企业版及教育版 — **Windows 家庭版不支持**

- Single sandbox at a time from the GUI

- 图形界面一次仅允许运行一个沙盒

- Networking on by default — easy footgun for malware analysis (always disable in `.wsb` for that use case)

- 网络默认启用 — 对恶意软件分析而言易成“陷阱”（该场景下务必在 `.wsb` 配置中禁用）

- No process I/O capture from `wsb exec` — fire-and-forget only

- `wsb exec` 不支持进程 I/O 捕获 — 仅支持“发射即忘”模式

- `MappedFolders` with write enabled persist after the sandbox is destroyed

- 启用写权限的 `MappedFolders` 在沙盒销毁后仍保留其内容

- Sandbox window size is not configurable

- 沙盒窗口尺寸不可调整

## Open source surface

## 开源表层

- The sandbox engine itself ships with Windows and is closed-source

- 沙盒引擎本身随 Windows 发布，属闭源软件

- The [microsoft/Windows-Sandbox](https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net) GitHub repo is [MIT](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net)-licensed and hosts community add-ons, sample `.wsb` files, GUI utilities (e.g., "Run in Sandbox" context menu, PyWinSandbox), and issue tracking — not the core code

- [microsoft/Windows-Sandbox](https://github.com/microsoft/Windows-Sandbox?ref=dsebastien.net) GitHub 仓库采用[MIT 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net)，托管社区扩展工具、示例 `.wsb` 配置文件、图形界面工具（如右键菜单“在沙盒中运行”、PyWinSandbox）及问题追踪系统——但**不包含核心引擎代码**

## References

## 参考资料

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-architecture)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-install)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-sample-configuration)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-cli)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-versions)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot)

- [https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-troubleshoot)

- [https://github.com/microsoft/Windows-Sandbox](https://github.com/microsoft/Windows-Sandbox)

- [https://github.com/microsoft/Windows-Sandbox](https://github.com/microsoft/Windows-Sandbox)

## Related

## 相关主题

- [Hyper-V](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net)

- [Hyper-V](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Hyper-V?ref=dsebastien.net)

- [Containerization](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net)

- [容器化（Containerization）](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Containerization?ref=dsebastien.net)

- [Docker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net)

- [Docker](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/Docker?ref=dsebastien.net)

- **LXC (Linux Containers)**

- **LXC（Linux 容器）**

- [MIT License](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net)

- [MIT 许可证](https://notes.dsebastien.net/30+Areas/33+Permanent+notes/33.02+Content/MIT+License?ref=dsebastien.net)
