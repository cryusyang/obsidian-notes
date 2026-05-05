---
title: "0156. Netlify 身份验证令牌在 Mozilla CI 公共日志中泄露"
url: "https://mp.weixin.qq.com/s/ZbRZe6KodkmwjnMmph3B3Q"
source: "Rsec"
date: 2026-04-27
fetched: 2026-05-05
language: zh
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> Mozilla CI 系统的公开日志（live.log）意外泄露了用于 Netlify 平台的身份验证令牌，导致攻击者可获得 Mozilla IT Web SRE 账户的完全访问权限。该令牌可用于篡改或删除关联网站（如 crash-pings.mozilla.org）、窃取敏感配置与环境变量、实施金融欺诈及恶意内容投放等高危操作。问题根源在于 CI/CD 流水线未对敏感凭证进行日志屏蔽，暴露于公共可访问的日志中。建议立即撤销令牌、全面审计日志记录策略，并通过最小权限原则、IP 白名单和 API 行为监控强化令牌安全。

---

<section style="margin-bottom: 0px; margin-top: 0px;">
 <p>
  <span>
   <span style="font-size: 17px; font-weight: bold;">
    来源：Hackerone报告
   </span>
  </span>
  <span>
   <br />
  </span>
 </p>
 <p>
  <span>
   <span style="font-size: 17px; font-weight: bold;">
    编号：2915647
   </span>
  </span>
  <span>
   <span>
    <br />
   </span>
  </span>
 </p>
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   严重程度：Critical (10.0)
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   汇报者：
  </span>
 </span>
 <span>
  <span>
   <span style="font-size: 17px; color: rgb(0, 0, 0);">
    samirsec0x01
   </span>
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span>
   类型：信息泄露
  </span>
 </span>
 <p>
  <span>
   <br />
  </span>
 </p>
 <p>
  <span>
   <span style="font-size: 20px; font-weight: bold;">
    产品介绍（可以先跳过这部分）
   </span>
  </span>
 </p>
 <p>
  <span>
   <br />
  </span>
 </p>
 <p>
  <span>
   <span style="font-size: 17px; font-weight: bold;">
    Mozilla CI
   </span>
  </span>
 </p>
</section>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   Mozilla CI 是 Mozilla 公司为其核心产品（尤其是 Firefox）搭建的一套庞大、高度自动化的持续集成系统，这套系统是确保 Firefox 这类拥有数千万行代码的软件在快速迭代下仍能保持质量与稳定的基石。其规模宏大，每月例行执行超过 700 万个任务，最高可同时处理 35 万个任务。
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   它由几个核心部分组成：
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   🛠️ 任务执行框架: Taskcluster：Mozilla 自主研发的 CI 核心引擎，可根据需求灵活定制任务执行流程，不仅支撑着整个 Firefox CI 的运行，也以开源形式提供。
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   🏗️ 核心实例: Firefox CI：面向 Firefox 等核心产品，由专业的发布工程团队维护，是绝大多数构建和测试任务的实际运行环境。
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   🧩 任务定义器: Taskgraph (Python库)：开发者主要在此通过声明式方式定义 CI 任务，Taskgraph 会将其转为有依赖关系的任务图并提交给 Taskcluster。
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   📊 可视化仪表盘: Treeherder：开发者查看任务状态的“驾驶舱”，用于监控运行状态、分析日志和追踪失败原因。
  </span>
 </span>
</p>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</p>
<p>
 <span>
  <span>
   <span style="font-size: 17px; font-weight: bold;">
    Netlify
   </span>
  </span>
 </span>
</p>
<p>
 <span>
  <span>
   <br />
  </span>
 </span>
</p>
<p>
 <span>
  <span>
   <span style="font-size: 17px;">
    Netlify 是一个为了简化现代 Web 项目部署而生的综合性平台
   </span>
  </span>
 </span>
 <span>
  <span>
   <span style="font-size: 17px;">
    。它将代码从 Git 仓库到线上环境的复杂流程，自动化成简单操作，让开发者可以专注于编码本身，被誉为
   </span>
  </span>
 </span>
 <strong>
  <span>
   <span style="font-size: 17px;">
    JAMstack 架构的先行者和推动者
   </span>
  </span>
 </strong>
</p>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   开始
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span>
   <span style="font-size: 17px;">
    我们发现了一个严重漏洞，该漏洞涉及公开日志中泄露的 Netlify 身份验证令牌。该令牌赋予了
   </span>
  </span>
 </span>
 <code>
  <span>
   <span style="font-size: 17px;">
    Mozilla IT Web SRE
   </span>
  </span>
 </code>
 <span>
  <span style="font-size: 17px;">
   Netlify 账户的完全访问权限，绕过了所有限制。该令牌的权限涵盖了所有者、开发人员、计费管理员、审核员、发布者和内容编辑等角色，从而赋予了对站点管理、部署、计费和内容配置的完全控制权。这个泄露的 API 密钥构成了重大的安全风险，使未经授权的用户能够随意操纵账户及其关联资产。
  </span>
 </span>
</section>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <span style="font-size: 17px;">
    关键信息：
   </span>
  </span>
 </strong>
</h3>
<ul class="list-paddingleft-1">
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     已曝光令牌：
    </span>
   </span>
   <span>
    <span>
     <span style="font-size: 17px;">
     </span>
    </span>
   </span>
   <code>
    <span>
     <span style="font-size: 17px;">
      ███
     </span>
    </span>
   </code>
  </strong>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     暴露来源：
    </span>
   </span>
  </strong>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <strong>
    <span>
     <span style="font-size: 17px;">
      公开网址：
     </span>
    </span>
    <span>
     <br />
    </span>
   </strong>
   <strong>
    <span>
     <span style="font-size: 17px;">
      https://firefox-ci-tc.services.mozilla.com/tasks/d5NRF8FdQamV9XdPO_mTBQ/runs/0/logs/public/logs/live.log
     </span>
    </span>
   </strong>
  </li>
 </ul>
 <ul class="list-paddingleft-1">
  <li>
   <strong>
    <span>
     <span style="font-size: 17px;">
      文件：live.log
     </span>
    </span>
   </strong>
  </li>
 </ul>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     用于验证的 API：
    </span>
   </span>
  </strong>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 17px;">
     Netlify API 文档
    </span>
   </span>
  </section>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     网站面临风险：
    </span>
   </span>
  </strong>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 17px;">
    </span>
   </span>
   <code>
    <span>
     <span style="font-size: 17px;">
      https://crash-pings.mozilla.org
     </span>
    </span>
   </code>
  </section>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     风险账户：
    </span>
   </span>
  </strong>
  <section style="margin-bottom: 0px; margin-top: 0px;">
   <span>
    <span style="font-size: 17px;">
    </span>
   </span>
   <code>
    <span>
     <span style="font-size: 17px;">
      Mozilla IT Web SRE
     </span>
    </span>
   </code>
  </section>
 </li>
</ul>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <span style="font-size: 17px;">
    重现步骤：
   </span>
  </span>
 </strong>
</h3>
<ol class="list-paddingleft-1">
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      访问公共日志：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      在浏览器中打开以下网址： Mozilla CI Logs 。
     </span>
    </span>
   </section>
  </li>
 </ul>
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      找到暴露的令牌：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <font>
    <font>
     <font>
      <span>
       <span style="font-size: 17px;">
        在日志文件中搜索关键字
       </span>
      </span>
      <code>
       <span>
        <span style="font-size: 17px;">
         auth:
        </span>
       </span>
      </code>
     </font>
    </font>
   </font>
  </li>
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      提取 Netlify 令牌（例如
     </span>
    </span>
    <code>
     <span>
      <span style="font-size: 17px;">
       ███
      </span>
     </span>
    </code>
    <span>
     <span style="font-size: 17px;">
      ）。
     </span>
    </span>
   </section>
  </li>
 </ul>
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      验证令牌有效性：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      使用该令牌查询 Netlify API。例如：
     </span>
    </span>
   </section>
  </li>
 </ul>
</ol>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>curl -X GET https://api.netlify.com/api/v1/accounts -H <span>"Authorization: Bearer ████"</span> -s | jq</span></code></pre>
</section>
<ul class="list-paddingleft-1">
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      查看包含有关 Netlify 帐户站点的敏感信息的响应
     </span>
    </span>
   </section>
  </li>
 </ul>
</ul>
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
  <li>
  </li>
  <li>
  </li>
  <li>
  </li>
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>[</span></code><code><span>  {</span></code><code><span>    <span>"name"</span>: <span>"Mozilla IT Web SRE"</span>,</span></code><code><span>    <span>"slug"</span>: <span>"mozilla-it"</span>,</span></code><code><span>    <span>"role"</span>: <span>"Developer"</span>,</span></code><code><span>    ...</span></code><code><span>    ...</span></code><code><span>    <span>"selected_access_site_ids"</span>: [</span></code><code><span>      <span>"5a05c659-aa54-4184-bdbe-7faa4dd497b5"</span></span></code><code><span>    ],</span></code><code><span>    <span>"billing_name"</span>: <span>"it-sre"</span>,</span></code><code><span>    <span>"billing_email"</span>: <span>"it-sre@mozilla.com"</span>,</span></code><code><span>    <span>"billing_details"</span>: <span>null</span>,</span></code><code><span>    ...</span></code><code><span>    ...</span></code><code><span>    <span>"roles_allowed"</span>: [</span></code><code><span>      <span>"Owner"</span>,</span></code><code><span>      <span>"Developer"</span>,</span></code><code><span>      <span>"Billing Admin"</span>,</span></code><code><span>      <span>"Reviewer"</span>,</span></code><code><span>      <span>"Publisher"</span>,</span></code><code><span>      <span>"Content Editor"</span></span></code><code><span>    ],</span></code><code><span>    <span>"created_at"</span>: <span>"2019-06-26T13:57:19.242Z"</span>,</span></code><code><span>    <span>"updated_at"</span>: <span>"2024-07-08T18:56:21.541Z"</span>,</span></code><code><span>    <span>"has_site_password"</span>: <span>false</span>,</span></code><code><span>    <span>"site_sso_login"</span>: <span>false</span>,</span></code><code><span>    <span>"site_sso_login_context"</span>: <span>"all"</span>,</span></code><code><span>    <span>"site_jwt_secret"</span>: <span>null</span>,</span></code><code><span>    <span>"saml_config"</span>: {</span></code><code><span>      <span>"idp_entity_id"</span>: <span>"urn:auth.mozilla.auth0.com"</span>,</span></code><code><span>      <span>"idp_sso_target_url"</span>: <span>"https://auth.mozilla.auth0.com/samlp/hj3jYIhcrgvPWTpnFoHWLPx57t6KKqhA"</span>,</span></code><code><span>      <span>"idp_slo_target_url"</span>: <span>"https://auth.mozilla.auth0.com/samlp/hj3jYIhcrgvPWTpnFoHWLPx57t6KKqhA/logout"</span>,</span></code><code><span>      <span>"idp_cert_fingerprint"</span>: <span>"2F:C4:72:FC:FE:1C:69:A6:6E:8B:A7:FA:72:AA:3D:08:B0:A0:6A:F8"</span></span></code><code><span>    },</span></code><code><span>    <span>"saml_session_expiration"</span>: <span>604800</span>,</span></code><code><span>    <span>"deploy_notifications_per_repo"</span>: <span>true</span>,</span></code><code><span>    <span>"payments_gateway_name"</span>: <span>"zuora_production"</span>,</span></code><code><span>    <span>"lifecycle_state"</span>: <span>"active"</span>,</span></code><code><span>    <span>"lifecycle_state_reason"</span>: <span>null</span>,</span></code><code><span>    <span>"weeks_past_due"</span>: <span>null</span>,</span></code><code><span>    <span>"days_until_disabled"</span>: <span>null</span>,</span></code><code><span>    <span>"current_billing_period_start"</span>: <span>"2024-12-26T00:00:00.000-08:00"</span>,</span></code><code><span>    <span>"next_billing_period_start"</span>: <span>"2025-01-26T00:00:00.000-08:00"</span>,</span></code><code><span>    <span>"current_usage_period_start"</span>: <span>"2024-12-01T00:00:00.000-08:00"</span>,</span></code><code><span>    <span>"next_usage_period_start"</span>: <span>"2025-01-01T00:00:00.000-08:00"</span>,</span></code><code><span>    ...</span></code><code><span>    ...</span></code><code><span>    <span>"type_name"</span>: <span>"Enterprise"</span>,</span></code><code><span>    <span>"type_id"</span>: <span>"58f792a3d6865d698b6879bd"</span>,</span></code><code><span>    <span>"type_slug"</span>: <span>"enterprise"</span>,</span></code><code><span>    <span>"monthly_seats_addon_dollar_price"</span>: <span>"0.0"</span>,</span></code><code><span>    <span>"owner_ids"</span>: [</span></code><code><span>      <span>"60be48126deb9594c56ad4a0"</span>,</span></code><code><span>      <span>"60c285a4fa8ef00f41b7a171"</span>,</span></code><code><span>      <span>"60eda0538f4cf6540569b4b5"</span>,</span></code><code><span>      <span>"62548540b51a811561330ed7"</span>,</span></code><code><span>      <span>"62c5e063fe09d502f8dc2519"</span>,</span></code><code><span>      <span>"62f22a000c27a1187e2be65b"</span>,</span></code><code><span>      <span>"62ffe60780a012285fb7d36f"</span>,</span></code><code><span>      <span>"63b429858592e6679549e622"</span>,</span></code><code><span>      <span>"650deaef51dc692b41f8b3f2"</span>,</span></code><code><span>      <span>"658210e2646ba26e2d050ff4"</span></span></code><code><span>    ],</span></code><code><span>    <span>"saml_enabled"</span>: <span>true</span>,</span></code><code><span>    <span>"org_saml_enabled"</span>: <span>false</span>,</span></code><code><span>    <span>"org_mfa_enabled"</span>: <span>false</span>,</span></code><code><span>    <span>"default"</span>: <span>false</span>,</span></code><code><span>    <span>"cancellable"</span>: <span>false</span>,</span></code><code><span>    <span>"has_builds"</span>: <span>true</span>,</span></code><code><span>    <span>"enforce_saml"</span>: <span>"enforced_strict"</span>,</span></code><code><span>    <span>"team_logo_url"</span>: <span>null</span>,</span></code><code><span>    <span>"can_start_pro_trial"</span>: <span>false</span>,</span></code><code><span>    <span>"on_pro_trial"</span>: <span>false</span>,</span></code><code><span>    <span>"can_start_enterprise_trial"</span>: <span>false</span>,</span></code><code><span>    <span>"on_enterprise_trial"</span>: <span>false</span>,</span></code><code><span>    <span>"security_contacts"</span>: [],</span></code><code><span>    <span>"gitlab_self_hosted_config"</span>: <span>null</span>,</span></code><code><span>    <span>"github_enterprise_config"</span>: <span>null</span>,</span></code><code><span>    <span>"bitbucket_self_hosted_config"</span>: <span>null</span></span></code><code><span>  }</span></code><code><span>]</span></code></pre>
</section>
<ol class="list-paddingleft-1" start="4">
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     确认完全访问权限：
    </span>
   </span>
  </strong>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      执行其他 API 请求，例如部署、删除或修改站点。
     </span>
    </span>
   </section>
  </li>
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      例如，访问敏感日志、环境变量或站点配置。
     </span>
    </span>
   </section>
  </li>
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      您可以在 Netlify API 文档中测试所有端点： https://open-api.netlify.com
     </span>
    </span>
   </section>
  </li>
 </ul>
</ol>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <span style="font-size: 20px; font-weight: bold;">
    建议
   </span>
  </span>
 </strong>
</h3>
<ol class="list-paddingleft-1">
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      撤销令牌：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      立即撤销已泄露的令牌，并通知所有受影响的利益相关者。
     </span>
    </span>
   </section>
  </li>
 </ul>
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      审计日志记录实践：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      检查所有 CI/CD 流水线，确保敏感数据（例如身份验证令牌）已被屏蔽。
     </span>
    </span>
   </section>
  </li>
 </ul>
 <li>
  <p style="margin-bottom: 0px; margin-top: 0px;">
   <strong>
    <span>
     <span style="font-size: 17px;">
      增强令牌安全性：
     </span>
    </span>
   </strong>
  </p>
 </li>
 <ul class="list-paddingleft-1">
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      实施 OAuth 权限范围或 IP 白名单来限制令牌的使用。
     </span>
    </span>
   </section>
  </li>
  <li>
   <section style="margin-bottom: 0px; margin-top: 0px;">
    <span>
     <span style="font-size: 17px;">
      监控可疑的 API 使用情况，以检测可能的漏洞利用。
     </span>
    </span>
   </section>
  </li>
 </ul>
</ol>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</h2>
<h2 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   影响
  </span>
 </span>
</h2>
<p style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px;">
   泄露的身份验证令牌提供了对 Netlify 账户的
  </span>
 </span>
 <strong>
  <span>
   <span style="font-size: 17px;">
    完全访问权限
   </span>
  </span>
 </strong>
 <span>
  <span style="font-size: 17px;">
   ，从而导致以下风险：
  </span>
 </span>
</p>
<ol class="list-paddingleft-1">
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     金融盗窃：修改 billing_email，将所有款项转入攻击者控制的账户。
    </span>
   </span>
  </strong>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     受损网站：修改、删除或部署关联网站（ https://crash-pings.mozilla.org ）上的恶意内容。
    </span>
   </span>
  </strong>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     数据泄露：访问环境变量、日志和其他敏感配置数据。
    </span>
   </span>
  </strong>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     名誉损害：利用被盗用的账户托管恶意内容或发起网络钓鱼攻击。
    </span>
   </span>
  </strong>
 </li>
 <li>
  <strong>
   <span>
    <span style="font-size: 17px;">
     永久失控：删除所有站点和配置，造成不可逆转的损害。
    </span>
   </span>
  </strong>
 </li>
</ol>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <strong>
  <span>
   <br />
  </span>
 </strong>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 20px; font-weight: bold;">
   思考：
  </span>
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   1.获取子域名：
  </span>
  <span style="font-size: 17px;">
   https://firefox-ci-tc.services.mozilla.com，该子域名并不在Mozilla的赏金漏洞范围中，所以要自行挖掘。
  </span>
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   2.发现url：
  </span>
  <span style="font-size: 17px; font-weight: normal;">
   通过扫描、前端代码审计、公开的资源、搜索引擎等方式发现该url。
  </span>
 </span>
</h3>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span><span>https:</span>/<span>/firefox-ci-tc.services.mozilla.com/tasks/d5NRF8FdQamV9XdPO_mTBQ/runs/0/logs/public/logs/live.log</span></span></code></pre>
</section>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   3. 发现令牌
  </span>
  <span style="font-size: 17px;">
   ：如果觉得麻烦，可以喂给AI。担心AI出错，也可以同时使用工具审计。
  </span>
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   4.识别令牌作用
  </span>
  <span style="font-size: 17px;">
   ：并且能实际利用令牌：log文件中应该会提到关键词，有了关键词根据令牌搜索调用方式就可以。
  </span>
 </span>
</h3>
<section>
 <ul class="code-snippet__line-index code-snippet__js">
  <li>
  </li>
 </ul>
 <pre class="code-snippet__js"><code><span>curl -X GET https://api.netlify.com/api/v1/accounts -H <span>"Authorization: Bearer ████"</span> -s | jq</span></code></pre>
</section>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<h2>
 <span>
  <span style="font-size: 17px; font-weight: bold;">
   如果您觉得这篇文章有用，
  </span>
 </span>
 <span>
  <span>
   <span style="font-size: 17px; font-weight: bold;">
    请点个赞👍
   </span>
  </span>
 </span>
</h2>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<h3 style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</h3>
<section style="margin-bottom: 0px; margin-top: 0px;">
 <span>
  <br />
 </span>
</section>
<p style="display: none;">
 
 
</p>
