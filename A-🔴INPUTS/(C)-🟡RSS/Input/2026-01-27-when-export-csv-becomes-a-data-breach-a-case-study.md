---
title: "When “Export CSV” Becomes a Data Breach: A Case Study of a IDOR in a Crypto Platform"
url: "https://mokhansec.medium.com/when-export-csv-becomes-a-data-breach-a-case-study-of-a-idor-in-a-crypto-platform-ba29149d7c4a?source=rss-ae64c019f634------2"
source: "Mohsin"
date: 2026-01-27
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 研究人员在测试某加密交易平台的导出功能时，发现用户现货和期货订单历史CSV文件被托管在公开静态域名下，且无需身份验证即可访问。这些URL路径包含可预测的纯数字用户ID，攻击者可通过枚举ID批量下载任意用户的完整交易记录，暴露包括交易对、杠杆、时间戳、成交数量、手续费及盈亏等高度敏感财务数据。由于文件完全公开、易被搜索引擎索引，该IDOR（不安全直接对象引用）漏洞存在大规模数据泄露风险。平台确认并修复了该问题，将其评定为P3严重级别，并向报告者发放1000美元赏金。

---

<p>While testing export functionality on a crypto trading platform, I discovered that users’ spot and futures order history CSV files were hosted on a public static domain and could be accessed <strong>without authentication</strong>.</p><p>The export URLs followed a predictable structure and contained <strong>numeric user IDs</strong>, making them trivial to enumerate. By changing the ID in the path, anyone could download another user’s complete trading history — no login, no token, no session required.</p><p><strong>Example pattern (redacted):</strong></p><pre>https://static.example.com/order/{type}/export/file/{YYYYMM}/{USER_ID}/Order_history_{DATE_RANGE}.csv</pre><p>Each CSV file contained highly sensitive financial data such as trading pairs, leverage, order timestamps, filled quantities, fees, and profit/loss values. This effectively exposed users’ full trading strategies and risk profiles.</p><p>Because the URLs were fully public and predictable, the issue could be exploited at scale, potentially allowing mass harvesting of millions of users’ trading histories. Some of these files were also indexed by search engines, increasing discoverability.</p><p>The issue was reported responsibly, validated, and eventually fixed by the platform.</p><p>This case highlights how a <strong>simple IDOR combined with public file hosting</strong> can turn routine export functionality into a severe privacy and security risk — especially for financial and crypto platforms.</p><h3>Bug Severity &amp; User ID Enumeration</h3><p>A key factor in the impact of this issue was <strong>user ID enumeration</strong>. The platform used <strong>purely numeric user IDs</strong> in the export paths, which were easy to predict and sequential. In the report, I demonstrated multiple active records and showed that changing only the numeric ID reliably returned valid trading history files for different users.</p><p>The ability to enumerate a large number of real user records and access sensitive financial data without authentication, the issue was ultimately classified as <strong>P3 severity</strong>. The submission was validated, fixed, and awarded a <strong>$1,000 bounty</strong>.</p><figure><img alt="" src="https://cdn-images-1.medium.com/max/754/1*S9gGS0uUh7OAyqLCLWhtTA.png" /></figure><img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=ba29149d7c4a" width="1" />
