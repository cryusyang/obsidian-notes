---
title: "Taxonomies in the Age of AI: Evolving Your Strategy"
url: "https://enterprise-knowledge.com/taxonomies-in-the-age-of-ai-evolving-your-strategy/"
source: "Enterprise Knowledge"
date: 2026-04-15
fetched: 2026-05-05
language: en
read: false
archived: false
tags: []
---

> [!example] AI 摘要
> 本文探讨了在大语言模型（LLM）快速发展的背景下，传统主题分类法（topic taxonomy）是否仍具价值。文章指出，尽管结构化、语义丰富的分类体系仍是AI解决方案的重要知识基础，但主题分类法在搜索增强、内容推荐等场景中的核心作用正被LLM的语义理解与生成能力所削弱。作者基于多年语义建模经验，分析了LLM如何通过检索增强与上下文学习替代部分人工构建的层级分类功能，并呼吁组织重新评估和调整语义建模策略，转向更轻量、动态、与AI协同的分类实践。

---

<h1><span style="font-weight: 400;">The Topic Taxonomy: An Outdated Artifact?</span></h1>
<p><span style="font-weight: 400;">As knowledge workers continue to navigate constantly evolving priorities in developing effective AI solutions that complement organizational priorities, semantics have maintained their value—but not without shifts that deserve our attention. </span></p>
<p><span style="font-weight: 400;">Broadly speaking, one reliable tenet holds true: taxonomies, as structured, hierarchical representations of a domain of content enriched with semantic context, provide a prime source of knowledge in a format that AI-powered solutions are built to digest. This hasn’t changed. That said, there are nuances around </span><i><span style="font-weight: 400;">which </span></i><span style="font-weight: 400;">taxonomies provide the most value. As semantic modelers with years of combined experience, we will focus on some essential taxonomies and how their value in the age of AI has shifted, with actionable recommendations on how to adapt </span><i><span style="font-weight: 400;">your</span></i><span style="font-weight: 400;"> semantic modeling strategy accordingly. </span></p>
<p><span style="font-weight: 400;">We’ll start our exploration of different taxonomies and their value for AI solutions with the </span><b>topic taxonomy</b><span style="font-weight: 400;">. Topic taxonomies refer to the hierarchical classification systems that organize knowledge assets into topics and subtopics, describing the “aboutness” of the corpus they represent. They can be developed to represent any domain of knowledge, and provide coverage for any range of knowledge assets. While other taxonomies (product taxonomies, regional taxonomies, site navigation, etc.) warrant discussion, topic taxonomies in particular exemplify the overlap between most historically in-demand from our clients and most impacted by advancements in AI-powered solutions. </span></p>
<p><span style="font-weight: 400;">Experienced Enterprise Knowledge modelers report that, for over a decade, topic taxonomies were some of the most valuable, in-demand semantic models from organizations in a range of industries. Topic taxonomies played a vital role in supporting: </span></p>
<ul>
<li style="font-weight: 400;"><b>Query expansion</b><span style="font-weight: 400;"> for improved search, particularly for highly-regulated and complex domains like healthcare and scientific research; </span></li>
<li style="font-weight: 400;"><b>Faceted</b><span style="font-weight: 400;"> search and filtering;</span></li>
<li style="font-weight: 400;"><b>Discovery </b><span style="font-weight: 400;">and recommendation of relevant content within a domain; and</span><b> </b></li>
<li style="font-weight: 400;"><b>Categories</b><span style="font-weight: 400;"> to wrangle unwieldy content.</span></li>
</ul>
<p><span style="font-weight: 400;">However, with rapid advancements in Large Language Model (LLM) capabilities, the following question emerges: <em>ar</em></span><i><span style="font-weight: 400;">e topic taxonomies still relevant or valuable?</span></i><span style="font-weight: 400;"> To answer that, let’s first review how LLMs work.</span></p>
<p>&nbsp;</p>
<h1><span style="font-weight: 400;">LLMs vs. Taxonomies: An Updated Landscape  </span></h1>
<h3><span style="font-weight: 400;">How LLMs Work  </span></h3>
<p><span style="font-weight: 400;">When a user submits a query to an AI-powered search or summarization tool, the system retrieves relevant content from the organization&#8217;s dataset and passes it to an LLM, which generates a natural-language summary drawing on both the retrieved content and the linguistic patterns it learned during training.</span></p>
<p><span style="font-weight: 400;">The quality of that summary depends on how well the retrieved content maps to the user&#8217;s intent and how unambiguous the underlying content is. We’ve observed that LLM-powered summaries have dramatically improved in quality and accuracy, even in the past year. </span></p>
<p><span style="font-weight: 400;">Keeping that in mind, let’s consider cases where an LLM produces reliable answers </span><i><span style="font-weight: 400;">without</span></i><span style="font-weight: 400;"> taxonomy, and then we’ll explore the cases where taxonomy </span><i><span style="font-weight: 400;">does</span></i><span style="font-weight: 400;"> make a significant difference.</span></p>
<h3><span style="font-weight: 400;">Where LLMs Thrive </span><i><span style="font-weight: 400;">Without </span></i><span style="font-weight: 400;">Topic Taxonomies </span></h3>
<p><span style="font-weight: 400;">While taxonomists may be reluctant to admit it, there are some instances where developing a topic taxonomy may not be the best way to dedicate modeling resources to a taxonomy project. This is not to say that taxonomies aren’t valuable; rather, these are areas where we suggest deprioritizing </span><i><span style="font-weight: 400;">topic taxonomies </span></i><span style="font-weight: 400;">in favor of developing different kinds of taxonomies. </span></p>
<h4><span style="font-weight: 400;">Foundational Content </span></h4>
<p><span style="font-weight: 400;">LLMs perform reasonably well with foundational content; content covering fundamental topics that would apply to most comparable organizations. Examples of such content include generic Human Resources topics (new hire onboarding, payroll, benefits information) or common customer support topics (setting up an account, changing a username, etc.). That said, foundational content does benefit heavily from taxonomies when representing a range of geographical regions where policies may differ—but we will get to that. </span></p>
<h4><span style="font-weight: 400;">Structured Content </span></h4>
<p><span style="font-weight: 400;">We know that LLMs perform better when digesting structured content; research consistently shows that content adhering to structured formats improves LLM retrieval and response quality. For example, a study on retrieval granularity found that breaking content into self-contained, structured units improved QA accuracy by </span><strong><a href="https://chentong0.github.io/factoid-wiki/" rel="noopener" target="_blank">5–7 percentage points</a></strong><span style="font-weight: 400;"> over arbitrarily segmented passages.</span></p>
<p><span style="font-weight: 400;">While “structured content” often implies “tagged with taxonomy,” it can also refer to content adhering to a content model, tabular data, code repositories, and more; essentially, any formal and consistent approach to transform content or data from an unstructured state to a structured format. Structuring content is particularly valuable for LLMs because it explicitly indicates where content can be broken into meaningful sections, as opposed to risking being chopped up into arbitrary pieces. This gives LLMs more information per token budget, which improves tool accuracy, efficiency, and effectiveness. The following visual illustrates how LLMs parse unstructured vs. structured content, and indicates how imposing structure improves the response. </span></p>
<p><img alt="If an item is written as: employees receive 15 days of PTO annually, the PTO policy was updated in January, remote workers follow different rules depending on state, California employees accrue PTO at 1.25 days/month, and tax implications vary by jurisdiction, then this is implementing arbitrary chunk boundaries and chunks split mid-topic to get the LLM response that is incomplete and missing content. But if you add semantic chunk boundaries (e.g. General PTO Policy - 15 days annually with accrual rules, Remote Worker Policy = state-specific variations, and California specifics: 1.25 days/month accrual), then each chunk is self contained, making the LLM response accurate and contextualized. " class="aligncenter size-full wp-image-26819" height="720" src="https://enterprise-knowledge.com/wp-content/uploads/2026/04/unnamed-36.png" width="960" /></p>
<h4><span style="font-weight: 400;">Straightforward Content </span></h4>
<p><span style="font-weight: 400;">Content written in plain, literal, and descriptive language tends to be adequately summarized by LLMs without taxonomic support. When the text says exactly what it means, the model has less room to misinterpret it. The retrieval system can match queries to content based on straightforward lexical and semantic similarity, and the summarization layer can synthesize it without confusion. This also applies to well-transcribed conversational content in transcripts. </span></p>
<h4><span style="font-weight: 400;">Abundant Content </span></h4>
<p><span style="font-weight: 400;">Many domains (software engineering, general medicine, consumer finance, and more) boast enormous representation in LLM training data, meaning that the model already has a strong baseline source for the terminology and concepts involved. As long as the content itself is well-written and doesn’t directly contradict most sources on the subjects therein, the AI agent can retrieve it, interpret it, and summarize it accurately without a taxonomy providing additional semantic guardrails.</span></p>
<p><span style="font-weight: 400;">For these kinds of content, developing a topic taxonomy may not deliver as much value, but there are other kinds of taxonomies that can provide far greater value and mitigate risk. Let’s dive in. </span></p>
<p>&nbsp;</p>
<h1><span style="font-weight: 400;">Where Taxonomies Serve As Differentiators </span></h1>
<p><span style="font-weight: 400;">Despite advancements in the capabilities of LLMs, taxonomies continue to provide heightened value by providing semantic context and accuracy for the following areas:</span></p>
<h3><span style="font-weight: 400;">Organization-Specific Terminology </span></h3>
<p><span style="font-weight: 400;">Highly organization-specific terminology grounded in business function is one area where taxonomies continue to provide enhanced value, where relying on LLMs alone leaves users vulnerable to inaccurate, inadequately contextualized, insufficient responses. Taxonomies prioritizing unique, specific elements about an organization that would otherwise be incomplete or absent from generic training data are highly valuable for providing context that may otherwise be locked up in inaccessible formats, like tacit knowledge held by seasoned employees. </span><strong><a href="https://enterprise-knowledge.com/the-role-of-product-taxonomies-in-the-age-of-ai/" rel="noopener">Product taxonomies</a></strong><span style="font-weight: 400;"> in particular exemplify where putting in the extra effort to capture your organization’s specific context is an effort that won’t go wasted, as opposed to letting an LLM parse together assumptions about products from product pages and internal documentation that often have multiple versions, overlapping information, or competing sources of truth. </span></p>
<h3><span style="font-weight: 400;">Taxonomies for Disambiguation </span></h3>
<p><span style="font-weight: 400;">Similar to taxonomies covering organization-specific terminology, areas where disambiguation is necessary to avoid overlapping meanings retain a high level of value for LLM-powered solutions. Here, allowing for some overlap between the value provided by both taxonomies and business glossaries, modeling a clarification between PTO (Paid Time Off) and PTO (Patent and Trademark Office) can provide a key distinction where knowledge assets may represent both concepts equally. </span></p>
<p><span style="font-weight: 400;">Think of using Google to research an acronym that sees broad as well as highly niche usage; letting LLMs loose on niche documentation without similarly niche contextualization may result in unsatisfactory outcomes. For example, imagine an engineer at a manufacturing firm asking an internal AI assistant, “What are our EPS requirements?” expecting information about Emergency Power Supply specs for their facility. Without disambiguation, the LLM (trained more on financial content than facilities engineering) might return a summary about Earnings Per Share targets from the company’s investor relations documents. The engineer wastes time, loses trust in the tool, and might miss a critical safety specification.</span></p>
<p><span style="font-weight: 400;">To explore another example of taxonomy’s utility for disambiguation, consider organizations where the same essential concept has both customer-facing and internal-facing terms: without explicit contextualization, an LLM would risk conflating the two, surfacing the wrong term to the wrong audience. For example, a bank’s customer may know a feature as “overdraft protection,&#8221; while internal teams track it under a regulatory label like “Reg E courtesy pay.” </span></p>
<h3><span style="font-weight: 400;">Taxonomies for Risk Mitigation and Permission Management </span></h3>
<p><span style="font-weight: 400;">Building upon the example of customer-facing vs. internal-facing terms, the realm of compliance and permissions highlights another area where investing time and resources in taxonomy development still holds great value – and should still be considered essential rather than optional. Developing a detailed taxonomy highlighting audiences or permissions provides LLMs with structured, contextualized guidelines, particularly when taxonomy concepts are applied as tags to the knowledge assets that need to be accessible by certain audiences and not others. </span></p>
<h3><span style="font-weight: 400;">Taxonomies for Assigning Value </span></h3>
<p><span style="font-weight: 400;">Tangential to the audience and permission management use case, taxonomies can also be valuable for assigning greater weight to knowledge assets that should be treated as a source of truth or higher priority than other assets. Suppose your team works with massive amounts of technical documentation that must all be maintained for document retention reasons, and can’t be reduced in a content audit. In this case, taxonomy would be useful for highlighting content that should be prioritized when retrieving information on a certain topic. Here, LLMs and taxonomies can join forces: the taxonomy can be leveraged to identify content that the LLM should assign greater importance to and weigh more heavily than other content, and the LLM can surface a more valuable response to the end user. </span></p>
<h3><span style="font-weight: 400;">Taxonomies Representing Geographic Variation</span></h3>
<p><span style="font-weight: 400;">Even as LLMs demonstrate an impressive ability to effectively summarize large quantities of content, we’ve found they still fall short when parsing between content written for different geographic regions. Recently, EK worked with a client that needed to audit and classify a corpus of content representing location-specific policies at a multinational organization with offices in dozens of different countries, each with differing legal policies. Their current-state LLM-powered summarization tool would conflate leave policies and other compliance-impacted topics across geographical regions. Fortunately, imposing a taxonomy representing geographic variation on a document level mitigated this problem.  </span></p>
<h3><span style="font-weight: 400;">Taxonomies as a Foundation for Ontologies and Knowledge Graphs </span></h3>
<p><span style="font-weight: 400;">Last but not least, taxonomies provide tremendous value in the form of providing scaffolding for more advanced models, namely ontologies and knowledge graphs. By first establishing a semantic, hierarchical foundation of fundamental concepts and context, ontologies can then be built to model non-hierarchical relationships, which can then be instantiated in a </span><strong><a href="https://enterprise-knowledge.com/how-a-knowledge-graph-supports-ai-technical-considerations/" rel="noopener" target="_blank">knowledge graph</a></strong><span style="font-weight: 400;">. </span></p>
<p><img alt="" class="aligncenter size-full wp-image-26820" height="468" src="https://enterprise-knowledge.com/wp-content/uploads/2026/04/unnamed-37.png" width="1233" /></p>
<p><span style="font-weight: 400;">Modeling more complex relationships unlocks value for organizations that need to understand the interplay between distinct entities. As shown in the visual above, taxonomies can model types of products, but an ontology can model more complex relationships between entities; the raw materials needing to be purchased to build the products developed by certain teams, and then the markets they should be distributed to. Complex competency questions require more complex modeling, but require taxonomies as a foundation. </span></p>
<p><span style="font-weight: 400;">In all of the aforementioned instances, taxonomies provide the additional semantic context that LLMs need to provide reliable responses that reflect organizational specificity, respect compliance considerations, direct attention to prioritized content, disambiguate where needed, and account for geographic variation and other forms of customization to suit user needs. </span></p>
<p>&nbsp;</p>
<h1><span style="font-weight: 400;">Taxonomies in the Age of AI: Rethinking Your Taxonomy Strategy </span></h1>
<p><span style="font-weight: 400;">If you’ve grown accustomed to thinking that topic taxonomies should be at the forefront of your semantic modeling strategy, it may be time to think differently to adapt to changes in how taxonomies are consumed and the value they provide LLM-powered tools. </span></p>
<p><span style="font-weight: 400;">If you’re ready to update your taxonomy strategy to optimize LLM outcomes and get the most out of your semantic design efforts, <strong><a href="https://enterprise-knowledge.com/contact-us/">reach out to us</a></strong>. Our team of semantic modeling experts is ready to discuss your options and develop a solution that fits your goals and keeps up with ongoing evolutions in AI capabilities.</span></p>
<p>The post <a href="https://enterprise-knowledge.com/taxonomies-in-the-age-of-ai-evolving-your-strategy/">Taxonomies in the Age of AI: Evolving Your Strategy</a> appeared first on <a href="https://enterprise-knowledge.com">Enterprise Knowledge</a>.</p>

## 中文译文

主题分类法：一种过时的产物？

随着知识工作者持续应对不断变化的优先事项，以开发出能有效支撑组织战略的人工智能解决方案，语义学的价值虽依然稳固，但其内涵已悄然发生转变，值得我们高度关注。

总体而言，一个可靠的基本原则依然成立：分类法——即以结构化、层级化方式呈现某一知识领域内容，并辅以语义上下文的模型——仍是人工智能解决方案赖以构建与消化的核心知识来源。这一点未曾改变。然而，不同分类法所能提供的价值却存在显著差异。作为拥有多年联合实践经验的语义建模专家，我们将聚焦若干关键分类法，剖析其在人工智能时代价值定位的演变，并提供切实可行的建议，助您相应调整语义建模策略。

我们首先从主题分类法（topic taxonomy）入手，探讨各类分类法对人工智能解决方案的价值。主题分类法指通过层级结构对知识资产进行主题与子主题划分的体系，旨在刻画其所表征语料库的“主题归属”（aboutness）。它可适用于任何知识领域，亦可覆盖任意范围的知识资产。尽管产品分类法、地域分类法、网站导航结构等其他类型分类法同样值得深入讨论，但主题分类法尤为典型地体现了客户长期以来最迫切的需求，也恰恰是受AI技术进步影响最为深远的一类。

资深企业知识建模师指出，在过去十余年中，主题分类法一直是跨行业组织需求最旺盛、价值最突出的语义模型之一。它在以下方面发挥了关键作用：

- 查询扩展（query expansion），从而提升搜索效果，尤其在医疗健康、科学研究等监管严格且高度复杂的领域；
- 面向多维度的筛选式搜索（faceted search）与过滤；
- 在特定知识领域内实现相关内容的发现与智能推荐；
- 为庞杂无序的内容提供归类框架，便于统一治理。

然而，随着大语言模型（LLM）能力的飞速跃升，一个根本性问题随之浮现：主题分类法是否仍具现实意义与实用价值？要回答这一问题，我们首先需回顾大语言模型的工作原理。

大语言模型 vs. 分类法：更新后的格局

大语言模型如何运作？

当用户向AI驱动的搜索或摘要工具提交查询时，系统会先从组织自有数据集中检索相关文档，并将这些内容输入大语言模型。该模型结合所检索到的材料及其在训练阶段习得的语言模式，生成自然语言形式的摘要。

该摘要的质量取决于两个关键因素：一是所检索内容与用户真实意图的匹配度；二是原始内容本身的明确性与歧义程度。我们观察到，过去一年间，由大语言模型生成的摘要在质量与准确性上已实现显著跃升。

基于上述理解，我们不妨先考察那些无需主题分类法即可获得可靠结果的场景，再进一步分析分类法确实发挥关键作用的情形。

大语言模型无需主题分类法亦可高效运行的场景

尽管分类学家或许不愿承认，但在某些情况下，投入资源专门构建主题分类法并非最优选择。这并非否定分类法本身的价值，而是建议：在这些特定领域，应将主题分类法置于较低优先级，转而优先建设其他类型的分类法。

基础性内容（Foundational Content）

大语言模型在处理基础性内容时表现良好——这类内容涵盖通用性主题，普遍适用于大多数同类组织。例如，通用人力资源主题（新员工入职、薪资发放、福利说明）或常见客户服务主题（账户注册、用户名修改等）。当然，若涉及多个地理区域且各地政策存在差异，基础性内容仍能从分类法中获益良多——这一点我们后文将详述。

结构化内容（Structured Content）

众所周知，大语言模型更善于处理结构化内容；大量研究一致表明，符合结构化规范的内容可显著提升大语言模型的检索效率与响应质量。例如，一项关于检索粒度的研究发现，将内容拆分为自包含、结构清晰的单元，相较随意切分的段落，可将问答准确率提升5–7个百分点。

虽然“结构化内容”常被默认等同于“经分类法打标的内容”，但它其实还可指遵循内容模型（content model）的文本、表格数据、代码仓库等——本质上，任何将非结构化内容或数据转化为正式、一致结构化格式的方法，皆属此类。对大语言模型而言，结构化内容尤为宝贵，因为它明确指示了内容可被合理切分的边界，避免被机械截断为任意碎片。这使得每个token预算承载更多信息，从而提升工具的准确性、效率与实效性。下图直观展示了大语言模型解析非结构化内容与结构化内容的差异，并说明施加结构如何优化响应效果。

直白型内容（Straightforward Content）

采用平实、字面化、描述性强的语言撰写的内容，通常无需分类法支持即可被大语言模型充分概括。当文字含义清晰、所言即所指时，模型误读空间极小。检索系统可仅凭词法与语义层面的直接相似性完成查询匹配，摘要生成层亦能毫无困惑地整合信息。这一规律同样适用于高质量转录的对话类内容（如会议纪要、访谈记录等）。

海量内容（Abundant Content）

许多领域（如软件工程、普通医学、消费者金融等）在大语言模型的训练数据中已有极为丰富的覆盖，这意味着模型本身已具备扎实的术语与概念基础。只要内容表述准确，且未与主流资料中的观点产生直接冲突，AI代理便足以独立完成检索、理解与摘要，无需额外依赖分类法提供语义护栏。

对于上述几类内容，单独构建主题分类法未必带来高回报，但其他类型的分类法则可能创造更大价值并有效规避风险。接下来，我们深入探讨。

分类法真正发挥差异化价值的场景

尽管大语言模型能力持续增强，分类法在如下领域仍展现出不可替代的增强价值——为其提供精准、可靠的语义上下文：

组织专属术语（Organization-Specific Terminology）

根植于业务职能的高度组织专属术语，正是分类法持续释放高价值的关键领域。单靠大语言模型在此类场景下易产出不准确、缺乏足够上下文或信息不足的回答，使用户面临风险。分类法若聚焦组织独有、具体的关键要素——这些要素往往在通用训练数据中缺失或不完整——则能有效解锁被“封存”的隐性知识（tacit knowledge），例如资深员工头脑中难以显性化的经验。产品分类法尤为典型：投入精力精准捕获组织自身的产品语境绝非徒劳；相比之下，若放任大语言模型仅从产品页面和内部文档（常存在多版本、信息重叠、信源冲突等问题）中自行拼凑产品认知，则极易失准。

用于消歧的分类法（Taxonomies for Disambiguation）

与组织专属术语类似，凡需消除歧义以防概念混淆的领域，分类法对AI解决方案仍具有极高价值。此处，分类法与业务术语表（business glossary）的功能存在一定交集。例如，对缩写“PTO”同时代表“带薪休假”（Paid Time Off）与“美国专利商标局”（Patent and Trademark Office）的情形进行明确区分，可在知识资产同等涵盖两类概念时，提供至关重要的辨析依据。

试想用谷歌搜索一个既广泛使用又高度专业化的缩略词：若未同步赋予大语言模型同等专业深度的上下文，其在处理专业文档时很可能给出不尽人意的结果。举例而言，某制造企业的工程师向内部AI助手提问：“我司EPS要求是什么？”本意是了解工厂应急电源（Emergency Power Supply）的技术规格。若缺乏消歧机制，而该大语言模型主要接受财务类内容训练（而非设施工程），则可能返回公司投资者关系文件中关于每股收益（Earnings Per Share）目标的摘要。结果，工程师白白耗费时间，对工具失去信任，甚至可能遗漏关键安全规范。

再举一例说明分类法在消歧方面的效用：某些组织对同一核心概念同时采用面向客户与面向内部的两套术语。若无明确的上下文标注，大语言模型极易混淆二者，将错误术语推送给错误受众。例如，银行客户熟知的“透支保护”（overdraft protection），在内部团队管理中可能按监管要求标记为“Reg E 礼遇付款”（Reg E courtesy pay）。

用于风险管控与权限管理的分类法（Taxonomies for Risk Mitigation and Permission Management）

延续客户视角与内部视角术语的案例，合规性与权限管理领域进一步凸显了投入时间与资源构建分类法的重大价值——此项工作理应被视为必需，而非可选项。构建详尽的分类法，明确标识不同受众或访问权限，可为大语言模型提供结构化、情境化的指导规则。尤其当分类法概念被作为标签（tag）应用于知识资产时，能精准界定哪些内容仅限特定群体访问，而对其他群体不可见。

用于赋权的分类法（Taxonomies for Assigning Value）

与受众及权限管理场景密切相关，分类法还可用于为特定知识资产赋予更高权重，使其在知识体系中被视作权威信源或高优先级内容。假设您的团队需维护海量技术文档，出于存档合规要求，所有文档均须保留，无法在内容审计中删减。此时，分类法可用于标示在特定主题检索中应被优先调取的内容。在此场景下，分类法与大语言模型可协同发力：分类法识别出需被大语言模型重点加权的内容，而大语言模型则据此生成对终端用户更具价值的响应。

体现地域差异的分类法（Taxonomies Representing Geographic Variation）

尽管大语言模型已展现出卓越的大规模内容摘要能力，我们在实践中发现，其在区分面向不同地理区域撰写的文本时仍显乏力。近期，Enterprise Knowledge（EK）曾协助一家跨国客户对其遍布数十个国家/地区的办公室所涉地域性政策文档库进行审核与分类。客户现有大语言模型驱动的摘要工具，会将不同国家/地区的休假政策及其他受合规影响的主题混为一谈。幸运的是，通过在文档级别施加体现地域差异的分类法，成功解决了这一问题。

作为本体与知识图谱基础的分类法（Taxonomies as a Foundation for Ontologies and Knowledge Graphs）

最后但同样重要的是，分类法在构建更高级语义模型（尤其是本体与知识图谱）时，提供了无可替代的“脚手架”价值。通过率先确立一套语义清晰、层级分明的基础概念与上下文框架，我们便可在此之上构建本体，以建模非层级化的关系；进而将这些关系实例化为知识图谱。

建模更复杂的关系，方能助力组织深入理解不同实体间的相互作用。如上图所示，分类法可定义产品类型，而本体则可建模更深层的关系链：例如，某团队研发的产品所需采购的原材料，以及该产品应投放的目标市场。解答复杂的能力型问题（competency questions）需要更复杂的建模，但这一切均以分类法为根基。

综上所述，在所有前述场景中，分类法均提供了大语言模型所亟需的附加语义上下文，使其输出具备以下关键特性：反映组织特异性、尊重合规约束、引导注意力至高优先级内容、在必要处实现精准消歧、兼顾地域差异及其他定制化需求，从而真正满足用户实际需要。

人工智能时代下的分类法：重构您的分类法战略

若您已习惯将主题分类法视为语义建模战略的首要任务，那么现在或许是时候重新思考，以适应分类法消费方式的变革及其为大语言模型赋能的新价值逻辑。

若您已准备好升级分类法战略，以优化大语言模型输出效果，并最大化语义设计工作的投资回报，请随时联系我们。我们的语义建模专家团队已整装待发，愿与您深入探讨可行方案，共同打造契合发展目标的定制化解决方案，并持续跟进人工智能能力的演进步伐。

本文《人工智能时代下的分类法：演进您的战略》首发于 Enterprise Knowledge 官网。
