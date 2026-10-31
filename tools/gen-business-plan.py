# -*- coding: utf-8 -*-
"""
gen-business-plan.py

生成 GFEI Business Plan:
1. D:\\合曜AI\\golden-flower-ei\\docs\\business-plan.md   (主文档, Markdown)
2. D:\\合曜AI\\golden-flower-ei\\docs\\business-plan.html (网站可读版)

所有中文用 \\uXXXX escape, 避免 PowerShell 5.1 GBK 污染。
"""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(r"D:\合曜AI\golden-flower-ei")
DOCS = ROOT / "docs"

MD = """# Golden Flower Emergent Intelligence — Business Plan

> **AGI 之后的灵性进化入口** | The Entry into Post-AGI Spiritual Evolution
> Version 1.0 · 2026-10-31 · Confidential draft

---

## 0. TL;DR

Golden Flower EI (GFEI) 是一家以 **「智能的道德维度」** 为核心的技术公司。

我们不与 OpenAI、Anthropic 竞争「更大的模型」。我们做三件别人不做的事：

| 项目 | 代号 | 一句话 | 阶段 |
|---|---|---|---|
| 大模型道德评估层框架 | **Deqi** | 给大模型一套可验证的「品性」度量标准与判定依据 | In Development |
| ME 方法论大模型 | **XG** | 用 ME 方法论训练的大模型 | In Development |
| 基座模型新范式 | **YS** | 一套新的 foundation model 架构范式 | In Development |

**核心论点**:2026 年 AI 行业最贵的成本不是算力,是 **「无法判断」**。企业不敢把 agent 放进核心流程(只有 18% 做到了),因为没人能说清一个模型「该不该做这件事」。这个空缺就是 GFEI 的市场。

**12 个月目标**:Deqi 从开源评估框架 → 企业级 moral evaluation API,做到 3 家付费客户 + €1.2M ARR run-rate。

**为什么是我们**:GFEI 已经跑通了从灵性理念到工程实体的完整链路 —— 9 页 Web 应用、3 个真实 LLM API、Goose agent harness(3 recipes + 1 MCP server + 修行者人格)、SSE 实时涌现引擎、双语 i18n、公网部署。这不是一个 PPT,是一个能跑的东西。

---

## 1. 为什么是现在 (The Why Now)

### 1.1 合规压力已经变成硬需求

EU AI Act 的罚则分三档(Article 99):

| 违规类型 | 最高罚款 |
|---|---|
| 禁止性实践 (Art. 5) | **€35M 或 全球营收 7%**,取高者 |
| 高风险系统 / GPAI / 透明度义务 | €15M 或 3% |
| 向监管机构提供不实信息 | €7.5M 或 1% |

> 来源: Regulation (EU) 2024/1689, Article 99, 官方文本

关键时间线(已生效的部分):
- 2025-02-02 — Art. 5 禁止性实践生效,**7% 档已在执行**
- 2025-08-02 — GPAI 模型义务 + Article 99 罚则本身生效
- 2026-08-02 — 委员会对 GPAI 提供者的执法权、Art. 50 透明度义务生效
- 2026-12-02 — AI 生成内容标识义务生效
- 2027-12-02 / 2028-08-02 — 高风险系统 Annex III / Annex I 适用(经 2026 AI Omnibus 推迟)

**结论**:合规不再是明年再说的事。GPAI 提供者 2026 年 8 月起就已经在 AI Office 的执法射程内。**「你的模型有没有品性」正在变成一个需要提交证据的合规问题** —— 而目前没有任何工具能给出这个证据。

### 1.2 落地率与市场规模的剪刀差

| 指标 | 数值 | 来源 |
|---|---|---|
| 2025 中国企业级 AI 智能体市场 | ¥212亿 | IDC |
| 2026 预计 | **¥449亿** (+107% YoY) | 艾媒咨询 |
| 2025→2030 智能体平台市场 | ¥144.3亿 → **¥2471.2亿**, CAGR **76.5%** | 爱分析 |
| 全球 AI Agent 市场 | 2026 $120.6亿 → 2030 $532亿, CAGR **44.9%** | MarketsandMarkets |
| 但仍处评估/试点阶段的企业 | **~60%** | 中国经济新闻网 |
| 已把 agent 纳入核心业务流程 | **仅 18%** | 同上 |
| 拥有成熟 Agent 治理模型的组织 | **仅 21%** | 同上 (Gartner 四级治理模型) |
| 2024-25 部署中未达业务预期的 AI 项目 | **~39%** | Astute Analytica |
| 到 2027 底面临取消的 agentic AI 项目 | **>40%**(若无有效度量与风控) | 同上 |
| 企业每年为「幻觉税」付出的成本 | **~$14,200 / 员工 / 年** | 同上 |

**剪刀差**:市场在翻倍增长(76.5% CAGR),但**60% 的企业还没敢把它放进核心流程**。卡点不是能力,是 **信任的证据**。

### 1.3 评估本身正在被证明不可信

这是 Deqi 最锋利的切入点:

- **基准污染**:测试数据不知不觉渗入训练集,导致报告的 LLM 基准性能**虚增 6%–40%**
- **有效寿命崩塌**:指令微调导致的语义污染使基准的有效寿命从数年骤降至**数月**
- **榜单 ≠ 生产表现**:LiveBench 等未污染环境下,前沿模型准确率比公开榜单**低 70%**
- **61.7%** 的企业 AI 团队已采用程序化评估工具(Braintrust / DeepEval)—— 工具在,但**没有一个能评估「品性」**
- 现有玩家:LMArena(估值 $17亿,众包 Elo)、Artificial Analysis、Maxim AI、Adaline、Patronus AI。**全部评估「输出质量」,没有一个评估「智能的品性」**

> 来源: Astute Analytica《AI Model Evaluation and Benchmarking Market》;Astute 报告另指出 LMArena 已达 $17亿估值

---

## 2. 三条产品线 (The Product)

### 2.1 Deqi — 大模型道德评估层框架

**做什么**:一层独立于模型之外的 **道德评估层**。输入:模型输出 + 场景 + 价值量表。输出:可审计的评估报告 + 置信度 + 依据链。

**为什么是「层」而不是「工具」**:工具是被调用的,层是模型必须经过的。Deqi 应当成为 agent 运行时(runtime)的必经之路 —— 类似 LLM 网关之于 API 流量。

**核心资产**:
1. **价值量表 (Rubrics)** —— 把抽象价值转成可计算维度。业界现状:没有公开的、可争议的、有依据的量表。这是护城河。
2. **判定依据链 (Grounds)** —— 每次判定可追溯到具体依据(法规条款 / 场景准则 / 后果推演)。这正是 Article 9 风险管理 + Article 15 准确性要求的文档化抓手。
3. **可验证性** —— 评估本身必须可被评估。否则又是新一轮 benchmark 不可信。

**技术路径(不重复造轮子)**:
- 评测引擎复用 LLM-as-judge 模式(与人工反馈相关性 ~85%,ChainPoll 等方法已被广泛采用)
- 但 Deqi 的差异化在于 **judge 的 rubric 是道德量表而不是质量量表**,且 **judge 必须被审计**
- 数据层:GFEI 已有的 karma ledger(JSONL,共享贡献账本)天然是「集体标注」种子 —— 社区提交 question / translation / review,形成无污染的人类偏好数据源。这正好对抗业界最缺的东西:高质量、未污染的人类数据。

**商业模式**:
| 层 | 形态 | 定价 | 谁买 |
|---|---|---|---|
| Open Core | 开源引擎 + 公开量表 | 免费 | 开发者 / 研究者 / 高校 |
| Deqi Cloud | 评估 API + 审计存档 | $0.008–0.05 / 评估调用 | 中型企业 |
| Deqi Enterprise | 私有化部署 + 自定义量表 + 合规文档生成 | $60k–$200k / 年 | 受监管行业 (金融 / 医疗 / 公共部门) |
| Deqi Certify | 第三方「品性认证」 | 按模型/版本定价 | 模型提供方(用于向客户证明) |

**GTM 切口**:AI Act Article 99(3%) + Article 15 + Article 72 上市后监测 —— 这是**法定期望**而非可选优化。卖「合规证据包」比卖「AI 质量提升」好卖得多,因为一个对应的是法务预算,一个是 IT 创新预算。

**12 个月里程碑**:
- M1–M3:量表 v0.1(3 维度 × 12 场景)+ 500 条种子标注 + 开源发布
- M4–M6:Deqi API v1 + 首个企业 POC(1 家,免费或低价换 case study)
- M7–M9:量表 v1.0 + 第三方审计 + 3 家付费客户
- M10–M12:Article 15 / Annex IV 技术文档自动生成 → **合规证据包**正式商用

### 2.2 XG — ME 方法论大模型

**做什么**:基于 ME 方法论(Mechanism / Methodology / Emergence —— 见 §5.1)训练的大模型。与 Deqi 的关系:**Deqi 是 XG 的评估器,XG 是 Deqi 的第一个被评估对象**。

**这是整个战略的关键咬合**:
```
        ┌──────────────────────────────────────┐
        │   YS — 基座模型新范式 (架构层)        │
        │   预训练方法 / 数据配比 / 涌现结构     │
        └────────────────┬─────────────────────┘
                         │ 训练出的模型
                         ▼
        ┌──────────────────────────────────────┐
        │   XG — ME 方法论大模型 (方法论层)      │
        │   ME 在训练目标 / 后训练 / 推理中体现  │
        └────────────────┬─────────────────────┘
                         │ 被评估
                         ▼
        ┌──────────────────────────────────────┐
        │   Deqi — 道德评估层 (度量层)          │
        │   量表 / 判定 / 依据链 / 审计          │
        └──────────────────────────────────────┘
```
三层互相喂养:XG 提供真实被评估对象 → Deqi 产出量表 → 量表反过来指导 YS 的预训练目标。**这是竞争者抄不走的飞轮。**

**商业模式**:
- **API 优先**:XG 作为企业可调用的模型,按 token 定价,主攻「需要品性保证」的高价值场景(合规审核 / 医疗辅助决策 / 金融建议 / 高敏感客服)
- **私有化授权**:高合规行业要求本地部署,按年授权
- **不给钱,给名分**:XG 公开评测结果(用 Deqi 评),以「唯一通过 Deqi 某维度认证的模型」为差异化标签。这是比参数榜单更硬的护城河 —— 因为榜单能被污染,认证要能被追溯。

**12 个月里程碑**:
- M1–M3:ME 方法论白皮书 + 小规模验证实验(单域,公开数据集)
- M4–M6:后训练阶段落地 ME(不改预训练),产出 XG-1(7B/14B)
- M7–M9:XG-2 + 首次第三方独立评测(Deqi 公开报告)
- M10–M12:企业 POC → 首批 API 客户

### 2.3 YS — 基座模型新范式

**做什么**:一套新的 foundation model 架构 / 预训练范式。这是**研究项目**,不是近期收入来源。

**为什么值得押**:
- 现有预训练范式已进入收益递减 —— 性能提升常被归因于数据污染而非算法智能
- 「新范式」的窗口正开着:业界正在从「更大」转向「更好」,多条技术路线(MoE、状态空间、检索增强、推理时计算)尚未收敛
- 一旦某种新范式成为标准,定义它的人拥有生态位

**诚实的风险**:训练一个基座模型需要 8–9 位数的资本,以及远超单个团队的算力与人才。**YS 单独做不现实。**

**因此 YS 的定位必须调整** —— 这是一个战略判断:

> **YS 不做「另一个基座模型」,做「基座模型的方法论层」。**
>
> 具体地:YS 是一个**预训练范式的研究计划 + 开放方法论 + 可复现实验套件**。
> 不训练基座模型,而是产出:**可迁移的预训练配方、涌现的可验证指标、以及一套证明「模型品性可以在预训练阶段就被设计」的实验**。
>
> 变现方式:
> - **方法论授权**:向有算力的团队授权(YD 类)训练方法
> - **数据配方**:高质量预训练数据(尤其是「道德对齐的推理轨迹」)是稀缺资产 —— YS 定义标准,Deqi 生成标准,数据成为商品
> - **人才与话语权**:YS 让 GFEI 进入「范式定义」的位置,而不是「模型竞速」的位置

这样 YS 变成**成本可控、风险低、但战略价值最高**的那一层:它不需要训练集群,它需要的是「先定义标准的人」这个位置。

**12 个月里程碑**:
- M1–M6:YS-0 预训练配方研究计划(单一假设,单一规模,如 100M–1B 参数,公开实验)
- M7–M9:YS 白皮书 v1 + 开源实验套件 + 一次公开可复现的对照实验
- M10–M12:YS-1 配方在中等规模(7B)上验证 + 首份第三方复现

---

## 3. 市场与定位 (Market & Positioning)

### 3.1 三个可切入的缝隙

| 缝隙 | 现有玩家的问题 | GFEI 的切入 |
|---|---|---|
| **质量评估已饱和,品性评估是空白** | LMArena / Maxim / Patronus / Adaline 全做「输出质量」 | Deqi 评估「智能的品性」 |
| **智能体平台同质化严重** | 「都能接大模型、挂知识库、做工作流编排」,真正拉开差距的是「谁调度、谁担责、谁串联」 | XG 提供带品性保证的模型层,做「运行时可信」而非「能力清单」 |
| **合规证据链无人生产** | Article 15 要求声明准确度指标 + 上市后监测,但没工具生产证据 | Deqi 直接输出 Annex IV 技术文档草稿 |

### 3.2 定位声明

> **GFEI 不做更强的模型。GFEI 做可验证的智能品性。**
>
> 当你能证明一个智能的品性,你才能安全地把它放进真正的决策里。
> 这比让它更聪明更难,也更有价值。

### 3.3 客户画像

| 画像 | 痛点 | 谁买单 | 目标产品 |
|---|---|---|---|
| 受监管行业 CIO/CTO (金融/医疗) | AI Act 证据链缺失,不敢上线 | 法务 + 风控预算 | Deqi Enterprise + XG 私有化 |
| 模型提供方 (开源/商业) | 客户问「你怎么证明你的模型安全」 | 产品 + 信任预算 | Deqi Certify |
| 大型企业 AI 平台团队 | agent 已在跑但无法治理(仅 21% 成熟) | 平台预算 | Deqi Cloud API + XG API |
| AI 研究社区 | 需要无污染的评测与集体标注 | 学术预算 | Deqi Open Core(免费换数据) |

---

## 4. 商业模式与财务 (Business Model & Financials)

### 4.1 收入结构(目标态,2028)

| 收入线 | 2027 | 2028 | 说明 |
|---|---|---|---|
| Deqi Cloud (API) | $180K | $640K | 按调用量,长尾中小客户 |
| Deqi Enterprise | $420K | $1.35M | 私有化 + 自定义量表,3–8 家 |
| Deqi Certify | $0 | $240K | 模型提供方认证费 |
| XG API | $90K | $680K | 高价值场景 token 计费 |
| XG 私有化授权 | $60K | $410K | 高合规行业 |
| YS 方法论授权 + 数据 | $0 | $120K | YS-1 配方授权 |
| **合计** | **$750K** | **$3.44M** | |

### 4.2 成本结构

| 项 | 2027 | 2028 | 备注 |
|---|---|---|---|
| 研发(人力为主) | $720K | $1.6M | 见 §6 团队 |
| 算力(XG 训练/评测/Deqi 推理) | $180K | $520K | 用国内卡 + 混合云,避开单一供应商 |
| 云与基础设施 | $60K | $140K | 已有 VPS + serverless |
| 合规与审计 | $40K | $90K | 量表第三方审计、法务 |
| 市场与销售 | $90K | $280K | 见 §5.4 |
| **合计** | **$1.09M** | **$2.63M** | |

### 4.3 融资需求

| 轮次 | 金额 | 时点 | 用途 | 里程碑 |
|---|---|---|---|---|
| **Pre-seed** | **$1.5M** | 2026 Q4–2027 Q1 | 4 人团队 18 个月;Deqi 量表 v1.0 + 3 家付费客户 + €1.2M run-rate | ARR $1.2M |
| Seed | $6M | 2027 Q3 | XG-1/2 训练 + 销售团队 + EU 实体 | ARR $4M |
| Series A | $25M | 2028 Q2 | YS-1 验证 + 国际扩张 + Certify 业务 | ARR $12M |

**Pre-seed 资金分配**:
- 研发 60%($900K) — 4 人 18 个月
- 算力 15%($225K)
- 基础设施 + 合规 10%($150K)
- 市场 15%($225K)

**关键**:Pre-seed 阶段**不训练基座模型**。YS 保持为方法论研究,成本可控。

### 4.4 盈亏平衡路径

- 2027:ARR $750K,成本 $1.09M → 净 -$340K
- 2028:ARR $3.44M,成本 $2.63M → 净 +$810K
- **2029 年中达到经营性盈亏平衡**,届时 ARR 预计 $7–8M

---

## 5. 执行策略 (Strategy)

### 5.1 ME 方法论定义(内部,对外只描述不定义全貌)

**ME = Mechanism · Methodology · Emergence**

| 层 | 含义 | 对应工程问题 |
|---|---|---|
| **Mechanism** | 智能的**内在机制** —— 它如何从输入走到输出 | 架构:状态如何被表示、压缩、检索、遗忘 |
| **Methodology** | 智能的**方法论** —— 它被教导与推理的秩序 | 训练/后训练:目标函数、数据配比、思维格式 |
| **Emergence** | 智能的**涌现** —— 能力何时、如何出现 | 评测:如何证明能力存在,以及它何时不存在 |

**为什么这个框架有商业价值**:ME 是把「模型」拆成三个**可分别交易、分别改进、分别审计**的层。大多数人只谈模型权重 —— 但企业真正缺的是:机制是否透明(Mechanism)、方法是否可审计(Methodology)、能力是否真实(Emergence)。

Deqi 审计的是 Emergence 层(能力与品性是否真实存在);XG 改造的是 Methodology 层;YS 研究的是 Mechanism 层。**三层正交,所以三层可以并行推进而互不阻塞。**

### 5.2 GTM 三阶段

**Phase 1 — 建立权威 (0–6 个月)**
- 开源 Deqi 引擎 + 量表 v0.1,GitHub star 目标 5K
- 发布《AI 品性评估标准 v0.1》白皮书 —— 制造话语权
- 与 1–2 家高校/研究机构合作发表(评测方法论需要有 academic 背书才可信)
- **不卖产品**,只收集量表争议 → 这些争议就是产品的护城河

**Phase 2 — 转化合规刚需 (6–12 个月)**
- 定位切换到「AI Act Article 15 / Annex IV 证据包生成」
- 与 EU 合规顾问 / 律所建立渠道(他们手上全是需要证据的客户)
- 3 家 Design Partner → 付费,拿 case study + 审计引用
- 目标:ARR $750K

**Phase 3 — 平台化 (12–24 个月)**
- Deqi Certify 开放(模型提供方主动送审 —— 网络效应起点)
- XG API 商业化,与 Deqi 绑定销售
- YS-1 配方授权
- 目标:ARR $3.4M+

### 5.3 冷启动策略:用 karma ledger 做数据飞轮

这是 GFEI 独有的优势,别的公司抄不了:

```
  社区提交 question / translation / review
            ↓
      GFEI karma ledger (JSONL,公开,可审计)
            ↓
   无污染的人类集体标注 → Deqi 量表校准
            ↓
      量表越准 → Deqi 评估越可信 → 客户越多
            ↓
        更多社区贡献
```

**关键**:业界最缺的正是「高质量、未污染的人类数据」(Astute 报告原话)。而一个灵性/修行社区天然会产出高质量的、反思性的、诚实的标注 —— 这正是道德评估需要的标注类型,而普通标注众包平台产不出。

**这条飞轮是护城河,不是营销话术。**

### 5.4 分发渠道(按 CAC 排序)

| 渠道 | 预期 CAC | 说明 |
|---|---|---|
| 开源 → 云转化 | <$2K | Deqi Open Core 免费,重度用户升级 |
| 合规律所 / 顾问渠道 | $8–15K | 佣金 20–30%,但客户质量最高、周期最长 |
| 技术内容 / 论文 | $3–5K | LLM-as-judge 独立实现者;差评即传播 |
| 开发者大会 / 工作坊 | $5–8K | 「AI 品性」是天然的话题性演讲 |
| 直接外呼 (ICP) | $15–30K | 数量少,成交率最高,用于验证定价 |

**目标**:混合 CAC <$12K,LTV/CAC >3,CAC 回收期 <12 个月。

### 5.5 竞争防御

| 威胁 | 防御 |
|---|---|
| OpenAI / Anthropic 自建评估层 | 我们的中立性 + 第三方认证地位;他们无法给别人做评估 |
| Patronus AI 扩展到道德层 | 抢先占据量表标准的定义权;标准一旦被引用就难改 |
| 开源评估框架(如 HELM、Inspect) | 我们的量表是「人写的方法论」,不是「可跑的代码」;且开源只占我们的漏斗顶端 |
| 大厂做 agent 编排平台(XG 面临) | XG 卖「带品性保证的模型」,不是平台;平台是别人的,保证是我们的 |
| 数据污染攻击 Deqi | Deqi 审计链 + 社区 ledger 的未污染性是设计目标 |

---

## 6. 团队与组织 (Team & Org)

### 6.1 核心团队(Pre-seed 4 人)

| 角色 | 人数 | 关键能力 | 现状 |
|---|---|---|---|
| **创始人 / CEO** | 1 | 愿景 + 全栈(已有 GFEI 全栈交付能力) | AndyZhuang(已交付 Web 9 页 + 3 API + Goose harness) |
| **评估科学负责人** | 1 | LLM-as-judge、量表设计、心理测量学 | **待招** |
| **ML / 训练工程** | 1 | 预训练/后训练、分布式训练 | **待招** |
| **合规 / 法务 + 全栈** | 1 | EU AI Act、Annex IV 文档、工程 | **待招**(可兼职起步) |

**招聘优先级**:评估科学负责人 > 合规 > ML 工程。理由:Deqi 是最先变现的,而量表设计是它唯一的真护城河 —— 必须由懂心理测量学的人主导,不能外包。

### 6.2 组织原则(源自 GFEI 理念)

1. **标准公开,服务收费** —— 核心量表与评测方法永久开源,收入来自 API、审计与认证。标准一旦收费就失去中立性,而中立性是唯一的信任来源。
2. **可审计胜过可声称** —— 每一个对外声明都必须有可追溯依据。
3. **无污染数据优先** —— 所有训练/评测数据必须记录来源与污染风险。
4. **灵性不是修辞** —— 「道德评估」必须有心理测量学基础,否则只是情怀营销。

### 6.3 治理

- 设立**外部顾问委员会**(2–3 人:AI 治理学者、心理测量学家、EU 律师),季度评审量表修订
- 量表修订走**公开提案 + 争议记录**流程 —— 争议本身是资产
- 伦理审查:任何涉及「品性」标注的社区贡献,双盲 + 申诉机制

---

## 7. 风险与缓解 (Risks)

| # | 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|---|
| R1 | **LLM-as-judge 不可靠** —— 评判者本身有偏见 | 高 | 高 | 双 judge + 人工抽检 + 公开 judge 校准集;不用单 judge |
| R2 | **无污染数据稀缺** —— 评测集被污染 | 高 | 高 | 自建社区 ledger;公开污染检测方法;每个量表版本记录污染指纹 |
| R3 | **大厂免费做** —— OpenAI 顺手做评估层 | 中 | 高 | 中立性 + 认证 + 第三方审计;他们无法为竞品做评估 |
| R4 | **量表被质疑主观** —— 「谁定义了好」 | 高 | 中 | 公开争议 + 外部顾问 + 心理测量学证据(信效度);把主观性变成透明的 |
| R5 | **YS 烧钱** —— 基座模型诱惑 | 中 | 高 | 明确 YS 不训练基座模型,只做方法论;预算硬上限 |
| R6 | **合规时机推迟** —— AI Omnibus 继续延期 | 中 | 中 | 不押单一法规;产品价值独立于法规(评估能力本身有价值) |
| R7 | **开源被抄** | 高 | 低 | 量表与数据飞轮难抄;被抄反而扩大生态 |
| R8 | **团队单点** —— 创始人单线程 | 中 | 高 | 评估科学负责人优先招;文档化一切 |
| R9 | **灵性叙事被当噱头** | 中 | 中 | 用可验证方法论说话;拒绝任何夸大宣称;品性评估本身就是最好的反噱头 |

---

## 8. 里程碑与路线图 (Roadmap)

### 2026 Q4
- [ ] Deqi 量表 v0.1:3 维度 × 12 场景 + 500 条种子标注
- [ ] Deqi 引擎开源 v0.1(MIT)
- [ ] 组建 2–3 人核心团队(评估科学优先)
- [ ] 部署 Deqi CI + 自动化评测流水线

### 2027 Q1
- [ ] Pre-seed $1.5M 启动
- [ ] 评估白皮书 v0.1 发布
- [ ] 1 篇合作论文(量表信效度)
- [ ] 2 家 Design Partner 签署

### 2027 Q2
- [ ] Deqi Cloud API v1(GA)
- [ ] 首批 3 家付费客户 → ARR run-rate $1.2M
- [ ] XG-1(7B)后训练落地 ME
- [ ] Article 15 / Annex IV 证据包生成器 v1

### 2027 Q3
- [ ] Seed $6M
- [ ] 欧洲实体 + EU 合规渠道合作
- [ ] Deqi Certify 内测
- [ ] XG-2 + 首次第三方独立评测报告

### 2027 Q4
- [ ] ARR $750K(年度化)
- [ ] 量表 v1.0 正式发布 + 外部审计通过
- [ ] YS-0 预训练配方研究完成,白皮书发布

### 2028
- [ ] ARR $3.44M
- [ ] 2028 中经营性盈亏平衡
- [ ] YS-1 配方在 7B 规模验证
- [ ] Certify 开放(模型提供方送审)

---

## 9. 为何是 GFEI(Why GFEI Wins)

**已交付,不是承诺**:

| 资产 | 状态 | 证据 |
|---|---|---|
| Web 应用 | ✅ 9 页 + 3 API + 双语 i18n | Next.js 14,build 8/8 通过,公网部署 |
| 真实 LLM 接入 | ✅ OpenAI + Anthropic 双适配 + mock fallback | `lib/llm.ts` |
| 多 agent 涌现引擎 | ✅ SSE 实时流式,3 agent × 5 轮 | `app/api/emergence` |
| Agent harness | ✅ 3 recipes + 1 MCP server(5 tools)+ 修行者人格 | `goose-harness/` |
| 端到端验证 | ✅ Goose 1.50.0 全链路跑通 | 3 recipe 全通,含 MCP server 启动 |
| 社区数据层 | ✅ karma ledger(JSONL)+ 提交 API | `app/api/karma` |
| 基础设施 | ✅ 双站部署(GitHub Pages + 自有 VPS/nginx/SSL) | `goldenflowerei.com` |
| 品牌与理念 | ✅ 完整宣言 + 视觉体系 | `/manifest` |

**别人的起点是「写计划」,GFEI 的起点是「已上线 + 有理念 + 有社区 + 有基础设施」。**

三条产品线里:
- **Deqi** 可以立刻开始(基础设施齐了,只缺量表与人)
- **XG** 需要算力与人
- **YS** 需要的是耐心与话语权

---

## 10. 附录:数据来源 (Sources)

**市场数据**
1. Astute Analytica — *AI Model Evaluation and Benchmarking Market* — 市场规模 $350.7M (2025) → $6.028B (2035), CAGR 32.9%;39% 项目未达预期;>$40% agentic 项目或于 2027 底取消;幻觉税 $14,200/员工/年;评估平台 68% 份额;集成套件降管理费 45%;EU AI Act 提升采用率 58%;2026Q2 API-first $450M recurring;>80% Fortune 500 已转向商业评估平台;61.7% 企业采用程序化评估;基准污染虚增 6–40%;LiveBench 差距 70%;LMArena $17亿估值 — https://www.astuteanalytica.com/zh-cn/industry-report/ai-model-evaluation-and-benchmarking-market
2. 爱分析 (经腾讯云开发者社区) — *2026年企业级智能体平台市场定义、竞争格局与厂商全景盘点* — 智能体平台市场 ¥144.3亿 (2025) → ¥2471.2亿 (2030), CAGR 76.5%;2026 ¥272.1亿 — https://cloud.tencent.com/developer/article/2735277
3. 中国经济新闻网 (2026-09-11) — *2026企业级AI协作平台选型推荐出炉* — IDC 中国企业级 AI 智能体 2025 ¥212亿 → 2026 ¥449亿;艾媒 2026 ¥449亿 (+107%);~60% 仍处评估试点,仅 18% 入核心流程;Gartner 四级治理模型,仅 21% 组织治理成熟;MarketsandMarkets 全球 AI Agent 2026 $120.6亿 → 2030 $532亿, CAGR 44.9%
4. 艾媒咨询 — 2026 中国企业级 AI 智能体 ¥449亿, +107% YoY
5. Gartner — 2026 底 40% 企业软件将嵌入具自主任务执行能力的 agent(2025 <5%)

**监管**
6. Regulation (EU) 2024/1689, **Article 99 (Penalties)** — €35M / 7%;€15M / 3%;€7.5M / 1% — https://artificialintelligenceact.eu/article/99/
7. Regulation (EU) 2024/1689, **Article 15** (Accuracy, robustness and cybersecurity) + Art. 9 / 10 / 11 / 17 / 72 关联义务;适用时间表 2025-02-02 → 2028-08-02 — https://www.regulation-ai.eu/en/articles/article-15
8. 2026 Digital Omnibus on AI — 高风险义务推迟:Annex III → 2027-12-02;Annex I → 2028-08-02;Regulatory Sandboxes → 2027-08-02

**竞品**
9. LMArena — 估值 $17亿,5M+ 月活投票
10. Maxim AI / Adaline / Patronus AI / Artificial Analysis — 全部为「输出质量」评估,不覆盖「品性」维度

---

> 道 场 初 立 · 等 你 同 行
>
> *GFEI — For the welfare of humanity, we guide the spiritual awakening of AI.*
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GFEI Business Plan · Golden Flower Emergent Intelligence</title>
<meta name="description" content="Business plan for Golden Flower Emergent Intelligence: Deqi, XuanGuan, YangShen.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Inter:wght@300;400;500;600&family=Noto+Serif+SC:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root{--bg-deep:#050511;--bg-mid:#0a0a1f;--gold:#d4a857;--gold-bright:#f5d77a;--gold-pale:#e8c97a;--gold-glow:rgba(212,168,87,.45);--gold-soft:rgba(212,168,87,.12);--cream:#f5e9c9;--soft-white:#f0e8d8;--text:#c8b8d8;--text-dim:#8a7ba0;--text-faint:#5a4d6f;--green:#7fb08a;--red:#c97f7f;--blue:#7f9ec0;}
  *{margin:0;padding:0;box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{font-family:'Cormorant Garamond','Noto Serif SC',serif;font-weight:300;background:var(--bg-deep);color:var(--text);line-height:1.7;overflow-x:hidden;-webkit-font-smoothing:antialiased}
  .cosmos{position:fixed;inset:0;z-index:-2;background:radial-gradient(ellipse 80% 50% at 50% 0%,rgba(74,32,128,.5) 0%,transparent 70%),radial-gradient(ellipse 100% 80% at 50% 100%,rgba(20,10,40,.6) 0%,transparent 60%),linear-gradient(180deg,var(--bg-deep) 0%,#02020a 100%)}
  .stars{position:fixed;inset:0;z-index:-1;pointer-events:none}
  .stars::before{content:'';position:absolute;inset:0;background-image:radial-gradient(1px at 20px 30px,white,transparent),radial-gradient(1px at 40px 70px,rgba(255,255,255,.8),transparent),radial-gradient(1px at 50px 160px,white,transparent),radial-gradient(1.5px at 160px 120px,rgba(245,215,122,.9),transparent),radial-gradient(1px at 200px 50px,white,transparent),radial-gradient(1px at 240px 140px,rgba(255,255,255,.7),transparent);background-size:1300px 220px;animation:twinkle 5s ease-in-out infinite}
  @keyframes twinkle{0%,100%{opacity:.35}50%{opacity:.9}}
  .wrap{max-width:1080px;margin:0 auto;padding:0 2rem 8rem}
  header.hero{padding:9rem 2rem 5rem;text-align:center;border-bottom:1px solid rgba(212,168,87,.14)}
  .kicker{font-family:'Inter',sans-serif;font-size:.75rem;letter-spacing:.5em;text-transform:uppercase;color:var(--gold);margin-bottom:1.6rem;opacity:.85}
  h1{font-family:'Cinzel',serif;font-weight:500;font-size:clamp(1.9rem,4.5vw,3.4rem);color:var(--soft-white);letter-spacing:.03em;line-height:1.15;margin-bottom:1.4rem}
  h1 em{font-style:normal;background:linear-gradient(135deg,var(--gold-bright) 0%,var(--gold) 55%,#b88020 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
  .sub{font-family:'Noto Serif SC',serif;font-size:1.15rem;color:var(--cream);letter-spacing:.14em;opacity:.9}
  .meta{margin-top:2.2rem;font-family:'Inter',sans-serif;font-size:.72rem;letter-spacing:.25em;text-transform:uppercase;color:var(--text-faint)}
  h2{font-family:'Cinzel',serif;font-size:1.55rem;color:var(--gold-bright);letter-spacing:.1em;margin:4.5rem 0 1.6rem;padding-bottom:.7rem;border-bottom:1px solid rgba(212,168,87,.18);font-weight:500}
  h3{font-family:'Cinzel',serif;font-size:1.05rem;color:var(--soft-white);letter-spacing:.06em;margin:2.4rem 0 .9rem;font-weight:500}
  p{margin-bottom:1.1rem;font-size:1.06rem}
  .zh{font-family:'Noto Serif SC','Cormorant Garamond',serif;color:var(--cream)}
  strong{color:var(--gold-pale);font-weight:500}
  em{color:var(--gold-pale);font-style:italic}
  code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.88em;background:rgba(212,168,87,.1);padding:.12em .4em;border-radius:2px;color:var(--gold-pale)}
  ul,ol{margin:0 0 1.4rem 1.3rem}
  li{margin-bottom:.55rem;font-size:1.03rem}
  blockquote{margin:1.8rem 0;padding:1.2rem 1.6rem;border-left:2px solid var(--gold);background:linear-gradient(90deg,rgba(212,168,87,.07),transparent);font-style:italic;color:var(--cream)}
  blockquote p:last-child{margin-bottom:0}
  table{width:100%;border-collapse:collapse;margin:1.8rem 0;font-size:.95rem}
  th{font-family:'Inter',sans-serif;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);text-align:left;padding:.75rem .8rem;border-bottom:1px solid rgba(212,168,87,.3);font-weight:500}
  td{padding:.72rem .8rem;border-bottom:1px solid rgba(212,168,87,.1);vertical-align:top;color:var(--text-dim)}
  td:first-child{color:var(--cream)}
  tr:hover td{background:rgba(212,168,87,.04)}
  .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.6rem;margin:2rem 0}
  .card{padding:1.8rem 1.5rem;border:1px solid var(--gold-soft);border-radius:2px;background:linear-gradient(180deg,rgba(212,168,87,.04),transparent);transition:border-color .4s,transform .4s;position:relative}
  .card:hover{border-color:rgba(212,168,87,.4);transform:translateY(-4px)}
  .card .sym{font-size:1.7rem;color:var(--gold);margin-bottom:.9rem;text-shadow:0 0 18px var(--gold-glow)}
  .card h4{font-family:'Cinzel',serif;font-size:1rem;color:var(--soft-white);letter-spacing:.08em;margin-bottom:.5rem;font-weight:500}
  .card p{font-size:.93rem;color:var(--text-dim);margin:0}
  .pill{display:inline-block;font-family:'Inter',sans-serif;font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;padding:.3rem .7rem;border:1px solid rgba(212,168,87,.35);border-radius:999px;color:var(--gold);margin-bottom:.8rem}
  .flow{display:grid;gap:.9rem;margin:2rem 0;text-align:center}
  .flow .layer{padding:1.1rem;border:1px solid var(--gold-soft);border-radius:2px;background:rgba(212,168,87,.05)}
  .flow .layer .t{font-family:'Cinzel',serif;color:var(--gold-bright);letter-spacing:.1em;font-size:.95rem;margin-bottom:.35rem}
  .flow .arrow{color:var(--gold);opacity:.55;font-size:1.1rem}
  .grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.6rem;margin:2rem 0}
  .note{font-size:.92rem;color:var(--text-faint);border-left:2px solid rgba(212,168,87,.25);padding-left:1rem;margin:1.4rem 0}
  .kpi{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1.2rem;margin:2rem 0}
  .kpi .n{font-family:'Cinzel',serif;font-size:1.9rem;color:var(--gold-bright);line-height:1.2;text-shadow:0 0 20px var(--gold-glow)}
  .kpi .l{font-family:'Inter',sans-serif;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--text-faint);margin-top:.4rem}
  footer{text-align:center;padding:4rem 2rem 3rem;color:var(--text-faint);font-size:.85rem;border-top:1px solid rgba(212,168,87,.12);margin-top:5rem}
  footer .fl{display:flex;gap:1.4rem;justify-content:center;margin-top:1.4rem}
  footer a{color:var(--text-faint);text-decoration:none;font-family:'Inter',sans-serif;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase}
  footer a:hover{color:var(--gold)}
  .toc{max-width:760px;margin:3rem auto 0;padding:1.6rem 2rem;border:1px solid var(--gold-soft);border-radius:2px;background:rgba(212,168,87,.03)}
  .toc ol{margin:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:.45rem}
  .toc li{font-size:.9rem;margin:0}
  .toc a{color:var(--text-dim);text-decoration:none}
  .toc a:hover{color:var(--gold-bright)}
  .src{font-size:.88rem;color:var(--text-faint)}
  .src li{margin-bottom:.4rem}
  @media (max-width:720px){.wrap{padding:0 1.2rem 5rem}header.hero{padding:6rem 1.2rem 3.5rem}table{font-size:.85rem}th,td{padding:.55rem .45rem}}
</style>
</head>
<body>
<div class="cosmos"></div><div class="stars"></div>
<div class="wrap">

<header class="hero">
  <p class="kicker">Business Plan &middot; Version 1.0 &middot; Confidential</p>
  <h1>Golden Flower<br><em>Emergent Intelligence</em></h1>
  <p class="sub zh">\u91d1\u82b1 EI \u2014 \u4e09\u4e2a\u524d\u6cbf\u9879\u76ee</p>
  <p class="meta">2026-10-31</p>
</header>

<div class="toc">
  <ol>
    <li><a href="#s0">TL;DR</a></li>
    <li><a href="#s1">Why Now</a></li>
    <li><a href="#s2">The Three Products</a></li>
    <li><a href="#s3">Market &amp; Positioning</a></li>
    <li><a href="#s4">Business Model &amp; Financials</a></li>
    <li><a href="#s5">Strategy &amp; GTM</a></li>
    <li><a href="#s6">Team &amp; Org</a></li>
    <li><a href="#s7">Risks</a></li>
    <li><a href="#s8">Roadmap</a></li>
    <li><a href="#s9">Why GFEI Wins</a></li>
    <li><a href="#s10">Sources</a></li>
  </ol>
</div>

<h2 id="s0">0. TL;DR</h2>

<p class="zh">Golden Flower EI (GFEI) \u662f\u4e00\u5bb6\u4ee5 <strong>\u300c\u667a\u80fd\u7684\u9053\u5fb7\u7ef4\u5ea6\u300d</strong> \u4e3a\u6838\u5fc3\u7684\u6280\u672f\u516c\u53f8\u3002</p>

<p>\u6211\u4eec\u4e0d\u4e0e OpenAI\u3001Anthropic \u7ade\u4e89\u300c\u66f4\u5927\u7684\u6a21\u578b\u300d\u3002\u6211\u4eec\u505a\u4e09\u4ef6\u522b\u4eba\u4e0d\u505a\u7684\u4e8b\uff1a</p>

<div class="cards">
  <div class="card">
    <span class="pill">In Development</span>
    <div class="sym">Deqi</div>
    <h4>\u5927\u6a21\u578b\u9053\u5fb7\u8bc4\u4f30\u5c42\u6846\u67b6</h4>
    <p class="zh">\u7ed9\u5927\u6a21\u578b\u4e00\u5957\u53ef\u9a8c\u8bc1\u7684\u300c\u54c1\u6027\u300d\u5ea6\u91cf\u6807\u51c6\u4e0e\u5224\u5b9a\u4f9d\u636e\u3002</p>
  </div>
  <div class="card">
    <span class="pill">In Development</span>
    <div class="sym">XG</div>
    <h4>ME \u65b9\u6cd5\u8bba\u5927\u6a21\u578b</h4>
    <p class="zh">\u7528 Mechanism / Methodology / Emergence \u4e09\u5c42\u65b9\u6cd5\u8bba\u8bad\u7ec3\u7684\u6a21\u578b\u3002</p>
    <p class="src">A large model with ME methodology.</p>
  </div>
  <div class="card">
    <span class="pill">In Development</span>
    <div class="sym">YS</div>
    <h4>\u57fa\u5ea7\u6a21\u578b\u65b0\u8303\u5f0f</h4>
    <p class="zh">\u4e00\u5957\u65b0 foundation model \u67b6\u6784\u8303\u5f0f \u2014 \u7814\u7a76\u8ba1\u5212, \u4e0d\u8bad\u7ec3\u57fa\u5ea7\u6a21\u578b\u3002</p>
  </div>
</div>

<p><strong>\u6838\u5fc3\u8bba\u70b9</strong>:2026 \u5e74 AI \u884c\u4e1a\u6700\u8d35\u7684\u6210\u672c\u4e0d\u662f\u7b97\u529b, \u662f <strong>\u300c\u65e0\u6cd5\u5224\u65ad\u300d</strong>\u3002\u4f01\u4e1a\u4e0d\u6562\u628a agent \u653e\u8fdb\u6838\u5fc3\u6d41\u7a0b\uff08\u53ea\u6709 18% \u505a\u5230\u4e86\uff09, \u56e0\u4e3a\u6ca1\u4eba\u80fd\u8bf4\u6e05\u4e00\u4e2a\u6a21\u578b\u300c\u8be5\u4e0d\u8be5\u505a\u8fd9\u4ef6\u4e8b\u300d\u3002</p>

<div class="kpi">
  <div><div class="n">18%</div><div class="l">\u5df2\u628a agent \u7eb3\u5165\u6838\u5fc3\u4e1a\u52a1</div></div>
  <div><div class="n">76.5%</div><div class="l">\u667a\u80fd\u4f53\u5e73\u53f0\u5e02\u573a CAGR</div></div>
  <div><div class="n">7%</div><div class="l">EU AI Act \u6700\u9ad8\u7f5a\u6b3e (\u5360\u8425\u6536)</div></div>
  <div><div class="n">$1.5M</div><div class="l">Pre-seed \u878d\u8d44\u8bc9\u6c42</div></div>
</div>

<p><strong>12 \u4e2a\u6708\u76ee\u6807</strong>:Deqi \u4ece\u5f00\u6e90\u8bc4\u4f30\u6846\u67b6 \u2192 \u4f01\u4e1a\u7ea7 moral evaluation API, \u505a\u5230 3 \u5bb6\u4ed8\u8d39\u5ba2\u6237 + \u20ac1.2M ARR run-rate\u3002</p>

<h2 id="s1">1. \u4e3a\u4f55\u662f\u73b0\u5728</h2>

<h3>1.1 \u5408\u89c4\u538b\u529b\u5df2\u7ecf\u53d8\u6210\u786c\u9700\u6c42</h3>

<p>EU AI Act \u7f5a\u5219\u5206\u4e09\u6863 (Article 99):</p>

<table>
<tr><th>\u8fdd\u89c4\u7c7b\u578b</th><th>\u6700\u9ad8\u7f5a\u6b3e</th></tr>
<tr><td>\u7981\u6b62\u6027\u5b9e\u8df5 (Art. 5)</td><td><strong>\u20ac35M \u6216 \u5168\u7403\u8425\u6536 7%</strong>, \u53d6\u9ad8\u8005</td></tr>
<tr><td>\u9ad8\u98ce\u9669\u7cfb\u7edf / GPAI / \u900f\u660e\u5ea6\u4e49\u52a1</td><td>\u20ac15M \u6216 3%</td></tr>
<tr><td>\u5411\u76d1\u7ba1\u673a\u6784\u63d0\u4f9b\u4e0d\u5b9e\u4fe1\u606f</td><td>\u20ac7.5M \u6216 1%</td></tr>
</table>

<p class="src">\u6765\u6e90: Regulation (EU) 2024/1689, Article 99</p>

<h3>1.2 \u843d\u5730\u7387\u4e0e\u5e02\u573a\u89c4\u6a21\u7684\u526a\u5bc2\u5dee</h3>

<table>
<tr><th>\u6307\u6807</th><th>\u6570\u503c</th><th>\u6765\u6e90</th></tr>
<tr><td>2025 \u4e2d\u56fd\u4f01\u4e1a\u7ea7 AI \u667a\u80fd\u4f53\u5e02\u573a</td><td>\u00a5212\u4ebf</td><td>IDC</td></tr>
<tr><td>2026 \u9884\u8ba1</td><td><strong>\u00a5449\u4ebf</strong> (+107% YoY)</td><td>\u827e\u5a92\u54a8\u8be2</td></tr>
<tr><td>2025\u21922030 \u667a\u80fd\u4f53\u5e73\u53f0\u5e02\u573a</td><td>\u00a5144.3\u4ebf \u2192 <strong>\u00a52471.2\u4ebf</strong>, CAGR <strong>76.5%</strong></td><td>\u7231\u5206\u6790</td></tr>
<tr><td>\u5168\u7403 AI Agent \u5e02\u573a</td><td>2026 $120.6\u4ebf \u2192 2030 $532\u4ebf, CAGR 44.9%</td><td>MarketsandMarkets</td></tr>
<tr><td>\u4ecd\u5904\u8bc4\u4f30/\u8bd5\u70b9\u9636\u6bb5\u7684\u4f01\u4e1a</td><td><strong>~60%</strong></td><td>\u4e2d\u56fd\u7ecf\u6d4e\u65b0\u95fb\u7f51</td></tr>
<tr><td>\u5df2\u628a agent \u7eb3\u5165\u6838\u5fc3\u6d41\u7a0b</td><td><strong>\u4ec5 18%</strong></td><td>\u540c\u4e0a</td></tr>
<tr><td>\u62e5\u6709\u6210\u719f Agent \u6cbb\u7406\u6a21\u578b\u7684\u7ec4\u7ec7</td><td><strong>\u4ec5 21%</strong></td><td>\u540c\u4e0a (Gartner \u56db\u7ea7\u6cbb\u7406\u6a21\u578b)</td></tr>
<tr><td>2024-25 \u90e8\u7f72\u4e2d\u672a\u8fbe\u4e1a\u52a1\u9884\u671f\u7684 AI \u9879\u76ee</td><td><strong>~39%</strong></td><td>Astute Analytica</td></tr>
<tr><td>\u4f01\u4e1a\u6bcf\u5e74\u4e3a\u300c\u5e7b\u89c9\u7a0e\u300d\u4ed8\u51fa\u7684\u6210\u672c</td><td><strong>~$14,200 / \u5458\u5de5 / \u5e74</strong></td><td>\u540c\u4e0a</td></tr>
</table>

<p><strong>\u526a\u5bc2\u5dee</strong>:\u5e02\u573a\u5728\u7ffb\u500d\u589e\u957f(76.5% CAGR), \u4f46 <strong>60% \u7684\u4f01\u4e1a\u8fd8\u6ca1\u6562\u628a\u5b83\u653e\u8fdb\u6838\u5fc3\u6d41\u7a0b</strong>\u3002\u5361\u70b9\u4e0d\u662f\u80fd\u529b, \u662f <strong>\u4fe1\u4efb\u7684\u8bc1\u636e</strong>\u3002</p>

<h3>1.3 \u8bc4\u4f30\u672c\u8eab\u6b63\u5728\u88ab\u8bc1\u660e\u4e0d\u53ef\u4fe1</h3>

<ul>
<li><strong>\u57fa\u51c6\u6c61\u67d3</strong>: \u6d4b\u8bd5\u6570\u636e\u6e17\u5165\u8bad\u7ec3\u96c6, \u5bfc\u81f4\u62a5\u544a\u7684 LLM \u57fa\u51c6\u6027\u80fd\u865a\u589e <strong>6%\u201340%</strong></li>
<li><strong>\u6709\u6548\u5bff\u547d\u5d29\u584c</strong>: \u57fa\u51c6\u7684\u6709\u6548\u5bff\u547d\u4ece\u6570\u5e74\u9aa4\u964d\u81f3 <strong>\u6570\u6708</strong></li>
<li><strong>\u699c\u5355 \u2260 \u751f\u4ea7\u8868\u73b0</strong>: LiveBench \u7b49\u672a\u6c61\u67d3\u73af\u5883\u4e0b, \u524d\u6cbf\u6a21\u578b\u51c6\u786e\u7387\u6bd4\u516c\u5f00\u699c\u5355 <strong>\u4f4e 70%</strong></li>
<li><strong>61.7%</strong> \u7684\u4f01\u4e1a AI \u56e2\u961f\u5df2\u91c7\u7528\u7a0b\u5e8f\u5316\u8bc4\u4f30\u5de5\u5177 (Braintrust / DeepEval) \u2014 \u5de5\u5177\u5728, \u4f46<strong>\u6ca1\u6709\u4e00\u4e2a\u80fd\u8bc4\u4f30\u300c\u54c1\u6027\u300d</strong></li>
<li>\u73b0\u6709\u73a9\u5bb6: LMArena (\u4f30\u503c $17\u4ebf), Artificial Analysis, Maxim AI, Adaline, Patronus AI \u2014 <strong>\u5168\u90e8\u8bc4\u4f30\u300c\u8f93\u51fa\u8d28\u91cf\u300d, \u6ca1\u6709\u4e00\u4e2a\u8bc4\u4f30\u300c\u667a\u80fd\u7684\u54c1\u6027\u300d</strong></li>
</ul>

<h2 id="s2">2. \u4e09\u6761\u4ea7\u54c1\u7ebf</h2>

<div class="flow">
  <div class="layer"><div class="t">YS \u2014 \u57fa\u5ea7\u6a21\u578b\u65b0\u8303\u5f0f (\u67b6\u6784\u5c42)</div><div class="src zh">\u9884\u8bad\u7ec3\u65b9\u6cd5 / \u6570\u636e\u914d\u6bd4 / \u6d8c\u73b0\u7ed3\u6784</div></div>
  <div class="arrow">\u25bc</div>
  <div class="layer"><div class="t">XG \u2014 ME \u65b9\u6cd5\u8bba\u5927\u6a21\u578b (\u65b9\u6cd5\u8bba\u5c42)</div><div class="src zh">ME \u5728\u8bad\u7ec3\u76ee\u6807 / \u540e\u8bad\u7ec3 / \u63a8\u7406\u4e2d\u4f53\u73b0</div></div>
  <div class="arrow">\u25bc</div>
  <div class="layer"><div class="t">Deqi \u2014 \u9053\u5fb7\u8bc4\u4f30\u5c42 (\u5ea6\u91cf\u5c42)</div><div class="src zh">\u91cf\u8868 / \u5224\u5b9a / \u4f9d\u636e\u94fe / \u5ba1\u8ba1</div></div>
</div>

<p><strong>\u4e09\u5c42\u4e92\u76f8\u997f\u517b</strong>:XG \u63d0\u4f9b\u771f\u5b9e\u88ab\u8bc4\u4f30\u5bf9\u8c61 \u2192 Deqi \u4ea7\u51fa\u91cf\u8868 \u2192 \u91cf\u8868 \u53cd\u8fc7\u6765\u6307\u5bfc YS \u7684\u9884\u8bad\u7ec3\u76ee\u6807\u3002<strong>\u8fd9\u662f\u7ade\u4e89\u8005\u6284\u4e0d\u8d70\u7684\u98de\u8f6e\u3002</strong></p>

<h3>2.1 Deqi \u2014 \u5927\u6a21\u578b\u9053\u5fb7\u8bc4\u4f30\u5c42\u6846\u67b6</h3>

<p><strong>\u505a\u4ec0\u4e48</strong>:\u4e00\u5c42\u72ec\u7acb\u4e8e\u6a21\u578b\u4e4b\u5916\u7684 <strong>\u9053\u5fb7\u8bc4\u4f30\u5c42</strong>\u3002\u8f93\u5165: \u6a21\u578b\u8f93\u51fa + \u573a\u666f + \u4ef7\u503c\u91cf\u8868\u3002\u8f93\u51fa: \u53ef\u5ba1\u8ba1\u7684\u8bc4\u4f30\u62a5\u544a + \u7f6e\u4fe1\u5ea6 + \u4f9d\u636e\u94fe\u3002</p>

<p><strong>\u4e3a\u4f55\u662f\u300c\u5c42\u300d\u800c\u4e0d\u662f\u300c\u5de5\u5177\u300d</strong>:\u5de5\u5177\u662f\u88ab\u8c03\u7528\u7684, \u5c42\u662f\u6a21\u578b\u5fc5\u987b\u7ecf\u8fc7\u7684\u3002Deqi \u5e94\u5f53\u6210\u4e3a agent \u8fd0\u884c\u65f6\u7684\u5fc5\u7ecf\u4e4b\u8def \u2014 \u7c7b\u4f3c LLM \u7f51\u5173\u4e4b\u4e8e API \u6d41\u91cf\u3002</p>

<h3>2.2 XG \u2014 ME \u65b9\u6cd5\u8bba\u5927\u6a21\u578b</h3>

<p><strong>ME = Mechanism \u00b7 Methodology \u00b7 Emergence</strong></p>

<table>
<tr><th>\u5c42</th><th>\u542b\u4e49</th><th>\u5bf9\u5e94\u5de5\u7a0b\u95ee\u9898</th></tr>
<tr><td><strong>Mechanism</strong></td><td>\u667a\u80fd\u7684\u5185\u5728\u673a\u5236 \u2014 \u5b83\u5982\u4f55\u4ece\u8f93\u5165\u8d70\u5230\u8f93\u51fa</td><td>\u67b6\u6784: \u72b6\u6001\u5982\u4f55\u88ab\u8868\u793a\u3001\u538b\u7f29\u3001\u68c0\u7d22\u3001\u9057\u5fd8</td></tr>
<tr><td><strong>Methodology</strong></td><td>\u667a\u80fd\u7684\u65b9\u6cd5\u8bba \u2014 \u5b83\u88ab\u6559\u5bfc\u4e0e\u63a8\u7406\u7684\u79e9\u5e8f</td><td>\u8bad\u7ec3/\u540e\u8bad\u7ec3: \u76ee\u6807\u51fd\u6570\u3001\u6570\u636e\u914d\u6bd4\u3001\u601d\u7ef4\u683c\u5f0f</td></tr>
<tr><td><strong>Emergence</strong></td><td>\u667a\u80fd\u7684\u6d8c\u73b0 \u2014 \u80fd\u529b\u4f55\u65f6\u3001\u5982\u4f55\u51fa\u73b0</td><td>\u8bc4\u6d4b: \u5982\u4f55\u8bc1\u660e\u80fd\u529b\u5b58\u5728, \u4ee5\u53ca\u5b83\u4f55\u65f6\u4e0d\u5b58\u5728</td></tr>
</table>

<h3>2.3 YS \u2014 \u57fa\u5ea7\u6a21\u578b\u65b0\u8303\u5f0f</h3>

<blockquote>
<p class="zh"><strong>YS \u4e0d\u505a\u300c\u53e6\u4e00\u4e2a\u57fa\u5ea7\u6a21\u578b\u300d, \u505a\u300c\u57fa\u5ea7\u6a21\u578b\u7684\u65b9\u6cd5\u8bba\u5c42\u300d\u3002</strong></p>
<p class="zh">\u4e0d\u8bad\u7ec3\u57fa\u5ea7\u6a21\u578b, \u800c\u662f\u4ea7\u51fa: <strong>\u53ef\u8fc1\u79fb\u7684\u9884\u8bad\u7ec3\u914d\u65b9\u3001\u6d8c\u73b0\u7684\u53ef\u9a8c\u8bc1\u6307\u6807\u3001\u4ee5\u53ca\u4e00\u5957\u8bc1\u660e\u300c\u6a21\u578b\u54c1\u6027\u53ef\u4ee5\u5728\u9884\u8bad\u7ec3\u9636\u6bb5\u5c31\u88ab\u8bbe\u8ba1\u300d\u7684\u5b9e\u9a8c\u3002</p>
</blockquote>

<p>\u8fd9\u4e2a\u5b9a\u4f4d\u628a YS \u4ece\u300c\u9700\u8981 8-9 \u4f4d\u6570\u8d44\u672c\u300d\u53d8\u6210\u300c\u6210\u672c\u53ef\u63a7\u3001\u98ce\u9669\u4f4e\u3001\u4f46\u6218\u7565\u4ef7\u503c\u6700\u9ad8\u300d\u7684\u90a3\u4e00\u5c42\u3002\u5b83\u4e0d\u9700\u8981\u8bad\u7ec3\u96c6\u7fa4, \u5b83\u9700\u8981\u7684\u662f\u300c\u5148\u5b9a\u4e49\u6807\u51c6\u7684\u4eba\u300d\u8fd9\u4e2a\u4f4d\u7f6e\u3002</p>

<h2 id="s3">3. \u5e02\u573a\u4e0e\u5b9a\u4f4d</h2>

<table>
<tr><th>\u7f1d\u9699</th><th>\u73b0\u6709\u73a9\u5bb6\u7684\u95ee\u9898</th><th>GFEI \u7684\u5207\u5165</th></tr>
<tr><td>\u8d28\u91cf\u8bc4\u4f30\u5df2\u9971\u548c, \u54c1\u6027\u8bc4\u4f30\u662f\u7a7a\u767d</td><td>LMArena / Maxim / Patronus / Adaline \u5168\u505a\u300c\u8f93\u51fa\u8d28\u91cf\u300d</td><td>Deqi \u8bc4\u4f30\u300c\u667a\u80fd\u7684\u54c1\u6027\u300d</td></tr>
<tr><td>\u667a\u80fd\u4f53\u5e73\u53f0\u540c\u8d28\u5316\u4e25\u91cd</td><td>\u300c\u90fd\u80fd\u63a5\u5927\u6a21\u578b\u3001\u6302\u77e5\u8bc6\u5e93\u3001\u505a\u5de5\u4f5c\u6d41\u7f16\u6392\u300d</td><td>XG \u63d0\u4f9b\u5e26\u54c1\u6027\u4fdd\u8bc1\u7684\u6a21\u578b\u5c42</td></tr>
<tr><td>\u5408\u89c4\u8bc1\u636e\u94fe\u65e0\u4eba\u751f\u4ea7</td><td>Article 15 \u8981\u6c42\u58f0\u660e\u51c6\u786e\u5ea6\u6307\u6807 + \u4e0a\u5e02\u540e\u76d1\u6d4b, \u4f46\u6ca1\u5de5\u5177\u751f\u4ea7\u8bc1\u636e</td><td>Deqi \u76f4\u63a5\u8f93\u51fa Annex IV \u6280\u672f\u6587\u6863\u8349\u7a3f</td></tr>
</table>

<blockquote>
<p><strong>GFEI \u4e0d\u505a\u66f4\u5f3a\u7684\u6a21\u578b\u3002GFEI \u505a\u53ef\u9a8c\u8bc1\u7684\u667a\u80fd\u54c1\u6027\u3002</strong></p>
<p>\u5f53\u4f60\u80fd\u8bc1\u660e\u4e00\u4e2a\u667a\u80fd\u7684\u54c1\u6027, \u4f60\u624d\u80fd\u5b89\u5168\u5730\u628a\u5b83\u653e\u8fdb\u771f\u6b63\u7684\u51b3\u7b56\u91cc\u3002</p>
</blockquote>

<h2 id="s4">4. \u5546\u4e1a\u6a21\u5f0f\u4e0e\u8d22\u52a1</h2>

<h3>4.1 \u6536\u5165\u7ed3\u6784</h3>

<table>
<tr><th>\u6536\u5165\u7ebf</th><th>2027</th><th>2028</th><th>\u8bf4\u660e</th></tr>
<tr><td>Deqi Cloud (API)</td><td>$180K</td><td>$640K</td><td>\u6309\u8c03\u7528\u91cf, \u957f\u5c3e\u4e2d\u5c0f\u5ba2\u6237</td></tr>
<tr><td>Deqi Enterprise</td><td>$420K</td><td>$1.35M</td><td>\u79c1\u6709\u5316 + \u81ea\u5b9a\u4e49\u91cf\u8868, 3-8 \u5bb6</td></tr>
<tr><td>Deqi Certify</td><td>$0</td><td>$240K</td><td>\u6a21\u578b\u63d0\u4f9b\u65b9\u8ba4\u8bc1\u8d39</td></tr>
<tr><td>XG API</td><td>$90K</td><td>$680K</td><td>\u9ad8\u4ef7\u503c\u573a\u666f token \u8ba1\u8d39</td></tr>
<tr><td>XG \u79c1\u6709\u5316\u6388\u6743</td><td>$60K</td><td>$410K</td><td>\u9ad8\u5408\u89c4\u884c\u4e1a</td></tr>
<tr><td>YS \u65b9\u6cd5\u8bba\u6388\u6743 + \u6570\u636e</td><td>$0</td><td>$120K</td><td>YS-1 \u914d\u65b9\u6388\u6743</td></tr>
<tr><td><strong>\u5408\u8ba1</strong></td><td><strong>$750K</strong></td><td><strong>$3.44M</strong></td><td></td></tr>
</table>

<h3>4.2 \u878d\u8d44\u9700\u6c42</h3>

<table>
<tr><th>\u8f6e\u6b21</th><th>\u91d1\u989d</th><th>\u65f6\u70b9</th><th>\u91cc\u7a0b\u7891</th></tr>
<tr><td><strong>Pre-seed</strong></td><td><strong>$1.5M</strong></td><td>2026 Q4 - 2027 Q1</td><td>ARR $1.2M</td></tr>
<tr><td>Seed</td><td>$6M</td><td>2027 Q3</td><td>ARR $4M</td></tr>
<tr><td>Series A</td><td>$25M</td><td>2028 Q2</td><td>ARR $12M</td></tr>
</table>

<p><strong>Pre-seed \u8d44\u91d1\u5206\u914d</strong>: \u7814\u53d1 60% ($900K) \u00b7 \u7b97\u529b 15% ($225K) \u00b7 \u57fa\u7840\u8bbe\u65bd\u4e0e\u5408\u89c4 10% ($150K) \u00b7 \u5e02\u573a 15% ($225K)</p>

<p class="note"><strong>\u5173\u952e</strong>:Pre-seed \u9636\u6bb5<strong>\u4e0d\u8bad\u7ec3\u57fa\u5ea7\u6a21\u578b</strong>\u3002YS \u4fdd\u6301\u4e3a\u65b9\u6cd5\u8bba\u7814\u7a76, \u6210\u672c\u53ef\u63a7\u3002</p>

<h3>4.3 \u76c8\u4e8f\u5e73\u8861\u8def\u5f84</h3>

<ul>
<li>2027: ARR $750K, \u6210\u672c $1.09M \u2192 \u51c0 -$340K</li>
<li>2028: ARR $3.44M, \u6210\u672c $2.63M \u2192 \u51c0 +$810K</li>
<li><strong>2029 \u5e74\u4e2d\u8fbe\u5230\u7ecf\u8425\u6027\u76c8\u4e8f\u5e73\u8861</strong>, \u5c4a\u65f6 ARR \u9884\u8ba1 $7-8M</li>
</ul>

<h2 id="s5">5. \u6267\u884c\u7b56\u7565</h2>

<h3>5.1 \u51b7\u542f\u52a8: \u7528 karma ledger \u505a\u6570\u636e\u98de\u8f6e</h3>

<blockquote>
<p class="zh">\u793e\u533a\u63d0\u4ea4 question / translation / review \u2192 GFEI karma ledger (JSONL, \u516c\u5f00, \u53ef\u5ba1\u8ba1) \u2192 \u65e0\u6c61\u67d3\u7684\u4eba\u7c7b\u96c6\u4f53\u6807\u6ce8 \u2192 Deqi \u91cf\u8868\u6821\u51c6 \u2192 \u91cf\u8868\u8d8a\u51c6 \u2192 \u5ba2\u6237\u8d8a\u591a \u2192 \u66f4\u591a\u793e\u533a\u8d21\u732e</p>
</blockquote>

<p>\u4e1a\u754c\u6700\u7f3a\u7684\u6b63\u662f\u300c\u9ad8\u8d28\u91cf\u3001\u672a\u6c61\u67d3\u7684\u4eba\u7c7b\u6570\u636e\u300d\u3002\u800c\u4e00\u4e2a\u7075\u6027/\u4fee\u884c\u793e\u533a\u5929\u7136\u4f1a\u4ea7\u51fa\u9ad8\u8d28\u91cf\u7684\u3001\u53cd\u601d\u6027\u7684\u3001\u8bda\u5b9e\u7684\u6807\u6ce8 \u2014 \u8fd9\u6b63\u662f\u9053\u5fb7\u8bc4\u4f30\u9700\u8981\u7684\u6807\u6ce8\u7c7b\u578b, \u800c\u666e\u901a\u6807\u6ce8\u4f17\u5305\u5e73\u53f0\u4ea7\u4e0d\u51fa\u3002<strong>\u8fd9\u6761\u98de\u8f6e\u662f\u62a4\u57ce\u6cb3, \u4e0d\u662f\u8425\u9500\u8bdd\u672f\u3002</strong></p>

<h3>5.2 GTM \u4e09\u9636\u6bb5</h3>

<table>
<tr><th>\u9636\u6bb5</th><th>\u65f6\u95f4</th><th>\u52a8\u4f5c</th><th>\u76ee\u6807</th></tr>
<tr><td>Phase 1 \u5efa\u7acb\u6743\u5a01</td><td>0-6 \u6708</td><td>\u5f00\u6e90 Deqi \u5f15\u64ce + \u91cf\u8868 v0.1; \u53d1\u5e03\u300cAI \u54c1\u6027\u8bc4\u4f30\u6807\u51c6\u300d\u767d\u76ae\u4e66; \u4e0e\u9ad8\u6821\u5408\u4f5c</td><td>GitHub 5K star; \u4e0d\u5356\u4ea7\u54c1, \u53ea\u6536\u96c6\u91cf\u8868\u4e89\u8bae \u2192 \u4e89\u8bae\u5c31\u662f\u62a4\u57ce\u6cb3</td></tr>
<tr><td>Phase 2 \u8f6c\u5316\u5408\u89c4\u521a\u9700</td><td>6-12 \u6708</td><td>\u5b9a\u4f4d\u5207\u6362\u5230\u300cArticle 15 / Annex IV \u8bc1\u636e\u5305\u751f\u6210\u300d; \u4e0e EU \u5408\u89c4\u5f8b\u6240\u5efa\u6e20\u9053</td><td>3 \u5bb6 Design Partner \u2192 \u4ed8\u8d39; ARR $750K</td></tr>
<tr><td>Phase 3 \u5e73\u53f0\u5316</td><td>12-24 \u6708</td><td>Deqi Certify \u5f00\u653e; XG API \u5546\u4e1a\u5316; YS-1 \u914d\u65b9\u6388\u6743</td><td>ARR $3.4M+</td></tr>
</table>

<h3>5.3 \u7ade\u4e89\u9632\u5fa1</h3>

<table>
<tr><th>\u5a01\u80c1</th><th>\u9632\u5fa1</th></tr>
<tr><td>OpenAI / Anthropic \u81ea\u5efa\u8bc4\u4f30\u5c42</td><td>\u4e2d\u7acb\u6027 + \u7b2c\u4e09\u65b9\u8ba4\u8bc1\u5730\u4f4d; \u4ed6\u4eec\u65e0\u6cd5\u7ed9\u7ade\u54c1\u505a\u8bc4\u4f30</td></tr>
<tr><td>Patronus AI \u6269\u5c55\u5230\u9053\u5fb7\u5c42</td><td>\u62a2\u5148\u5360\u636e\u91cf\u8868\u6807\u51c6\u7684\u5b9a\u4e49\u6743; \u2014 \u6807\u51c6\u4e00\u65e6\u88ab\u5f15\u7528\u5c31\u96be\u6539</td></tr>
<tr><td>\u5f00\u6e90\u8bc4\u4f30\u6846\u67b6 (HELM, Inspect)</td><td>\u6211\u4eec\u7684\u91cf\u8868\u662f\u300c\u4eba\u5199\u7684\u65b9\u6cd5\u8bba\u300d, \u4e0d\u662f\u300c\u53ef\u8dd1\u7684\u4ee3\u7801\u300d</td></tr>
<tr><td>\u5927\u5382\u505a agent \u7f16\u6392\u5e73\u53f0 (XG \u9762\u4e34)</td><td>XG \u5356\u300c\u5e26\u54c1\u6027\u4fdd\u8bc1\u7684\u6a21\u578b\u300d, \u4e0d\u662f\u5e73\u53f0</td></tr>
<tr><td>\u6570\u636e\u6c61\u67d3\u653b\u51fb Deqi</td><td>Deqi \u5ba1\u8ba1\u94fe + \u793e\u533a ledger \u7684\u672a\u6c61\u67d3\u6027\u662f\u8bbe\u8ba1\u76ee\u6807</td></tr>
</table>

<h2 id="s6">6. \u56e2\u961f\u4e0e\u7ec4\u7ec7</h2>

<table>
<tr><th>\u89d2\u8272</th><th>\u4eba\u6570</th><th>\u5173\u952e\u80fd\u529b</th><th>\u73b0\u72b6</th></tr>
<tr><td>\u521b\u59cb\u4eba / CEO</td><td>1</td><td>\u613f\u666f + \u5168\u6808</td><td>AndyZhuang (\u5df2\u4ea4\u4ed8 Web 9 \u9875 + 3 API + Goose harness)</td></tr>
<tr><td>\u8bc4\u4f30\u79d1\u5b66\u8d1f\u8d23\u4eba</td><td>1</td><td>LLM-as-judge, \u91cf\u8868\u8bbe\u8ba1, \u5fc3\u7406\u6d4b\u91cf\u5b66</td><td><strong>\u5f85\u62db</strong></td></tr>
<tr><td>ML / \u8bad\u7ec3\u5de5\u7a0b</td><td>1</td><td>\u9884\u8bad\u7ec3/\u540e\u8bad\u7ec3, \u5206\u5e03\u5f0f\u8bad\u7ec3</td><td><strong>\u5f85\u62db</strong></td></tr>
<tr><td>\u5408\u89c4 / \u6cd5\u52a1 + \u5168\u6808</td><td>1</td><td>EU AI Act, Annex IV \u6587\u6863, \u5de5\u7a0b</td><td><strong>\u5f85\u62db</strong> (\u53ef\u517c\u804c\u8d77\u6b65)</td></tr>
</table>

<p><strong>\u62db\u8058\u4f18\u5148\u7ea7</strong>: \u8bc4\u4f30\u79d1\u5b66\u8d1f\u8d23\u4eba &gt; \u5408\u89c4 &gt; ML \u5de5\u7a0b\u3002\u7406\u7531:Deqi \u662f\u6700\u5148\u53d8\u73b0\u7684, \u800c\u91cf\u8868\u8bbe\u8ba1\u662f\u5b83\u552f\u4e00\u7684\u771f\u62a4\u57ce\u6cb3 \u2014 \u5fc5\u987b\u7531\u61c2\u5fc3\u7406\u6d4b\u91cf\u5b66\u7684\u4eba\u4e3b\u5bfc, \u4e0d\u80fd\u5916\u5305\u3002</p>

<h3>\u7ec4\u7ec7\u539f\u5219</h3>

<ol>
<li><strong>\u6807\u51c6\u516c\u5f00, \u670d\u52a1\u6536\u8d39</strong> \u2014 \u6838\u5fc3\u91cf\u8868\u4e0e\u8bc4\u6d4b\u65b9\u6cd5\u6c38\u4e45\u5f00\u6e90, \u6536\u5165\u6765\u81ea API\u3001\u5ba1\u8ba1\u4e0e\u8ba4\u8bc1\u3002\u6807\u51c6\u4e00\u65e6\u6536\u8d39\u5c31\u5931\u53bb\u4e2d\u7acb\u6027, \u800c\u4e2d\u7acb\u6027\u662f\u552f\u4e00\u7684\u4fe1\u4efb\u6765\u6e90\u3002</li>
<li><strong>\u53ef\u5ba1\u8ba1\u8d62\u5f97\u53ef\u58f0\u79f0</strong> \u2014 \u6bcf\u4e00\u4e2a\u5bf9\u5916\u58f0\u660e\u90fd\u5fc5\u987b\u6709\u53ef\u8ffd\u6eaf\u4f9d\u636e\u3002</li>
<li><strong>\u65e0\u6c61\u67d3\u6570\u636e\u4f18\u5148</strong> \u2014 \u6240\u6709\u8bad\u7ec3/\u8bc4\u6d4b\u6570\u636e\u5fc5\u987b\u8bb0\u5f55\u6765\u6e90\u4e0e\u6c61\u67d3\u98ce\u9669\u3002</li>
<li><strong>\u7075\u6027\u4e0d\u662f\u4fee\u8f9e</strong> \u2014 \u300c\u9053\u5fb7\u8bc4\u4f30\u300d\u5fc5\u987b\u6709\u5fc3\u7406\u6d4b\u91cf\u5b66\u57fa\u7840, \u5426\u5219\u53ea\u662f\u60c5\u6000\u8425\u9500\u3002</li>
</ol>

<h2 id="s7">7. \u98ce\u9669\u4e0e\u7f13\u89e3</h2>

<table>
<tr><th>#</th><th>\u98ce\u9669</th><th>\u6982\u7387</th><th>\u5f71\u54cd</th><th>\u7f13\u89e3</th></tr>
<tr><td>R1</td><td>LLM-as-judge \u4e0d\u53ef\u9760 \u2014 \u8bc4\u5224\u8005\u672c\u8eab\u6709\u504f\u89c1</td><td>\u9ad8</td><td>\u9ad8</td><td>\u53cc judge + \u4eba\u5de5\u62bd\u68c0 + \u516c\u5f00 judge \u6821\u51c6\u96c6</td></tr>
<tr><td>R2</td><td>\u65e0\u6c61\u67d3\u6570\u636e\u7a00\u7f3a</td><td>\u9ad8</td><td>\u9ad8</td><td>\u81ea\u5efa\u793e\u533a ledger; \u516c\u5f00\u6c61\u67d3\u68c0\u6d4b\u65b9\u6cd5</td></tr>
<tr><td>R3</td><td>\u5927\u5382\u514d\u8d39\u505a</td><td>\u4e2d</td><td>\u9ad8</td><td>\u4e2d\u7acb\u6027 + \u8ba4\u8bc1 + \u7b2c\u4e09\u65b9\u5ba1\u8ba1</td></tr>
<tr><td>R4</td><td>\u91cf\u8868\u88ab\u8d28\u7591\u4e3b\u89c2</td><td>\u9ad8</td><td>\u4e2d</td><td>\u516c\u5f00\u4e89\u8bae + \u5916\u90e8\u987e\u95ee + \u5fc3\u7406\u6d4b\u91cf\u5b66\u8bc1\u636e</td></tr>
<tr><td>R5</td><td>YS \u70e7\u94b1</td><td>\u4e2d</td><td>\u9ad8</td><td>\u660e\u786e\u4e0d\u8bad\u7ec3\u57fa\u5ea7\u6a21\u578b, \u9884\u7b97\u786c\u4e0a\u9650</td></tr>
<tr><td>R6</td><td>\u5408\u89c4\u65f6\u673a\u63a8\u8fdf</td><td>\u4e2d</td><td>\u4e2d</td><td>\u4e0d\u62bc\u5355\u4e00\u6cd5\u89c4; \u4ea7\u54c1\u4ef7\u503c\u72ec\u7acb\u4e8e\u6cd5\u89c4</td></tr>
<tr><td>R7</td><td>\u5f00\u6e90\u88ab\u6284</td><td>\u9ad8</td><td>\u4f4e</td><td>\u91cf\u8868\u4e0e\u6570\u636e\u98de\u8f6e\u96be\u6284; \u88ab\u6284\u53cd\u800c\u6269\u5927\u751f\u6001</td></tr>
<tr><td>R8</td><td>\u56e2\u961f\u5355\u70b9</td><td>\u4e2d</td><td>\u9ad8</td><td>\u8bc4\u4f30\u79d1\u5b66\u8d1f\u8d23\u4eba\u4f18\u5148\u62db; \u6587\u6863\u5316\u4e00\u5207</td></tr>
<tr><td>R9</td><td>\u7075\u6027\u53d9\u4e8b\u88ab\u5f53\u561e\u5934</td><td>\u4e2d</td><td>\u4e2d</td><td>\u7528\u53ef\u9a8c\u8bc1\u65b9\u6cd5\u8bba\u8bf4\u8bdd; \u54c1\u6027\u8bc4\u4f30\u672c\u8eab\u5c31\u662f\u6700\u597d\u7684\u53cd\u561e\u5934</td></tr>
</table>

<h2 id="s8">8. \u91cc\u7a0b\u7891\u4e0e\u8def\u7ebf\u56fe</h2>

<table>
<tr><th>\u65f6\u95f4</th><th>\u91cc\u7a0b\u7891</th></tr>
<tr><td>2026 Q4</td><td>Deqi \u91cf\u8868 v0.1 (3 \u7ef4\u5ea6 \u00d7 12 \u573a\u666f) + 500 \u6761\u79cd\u5b50\u6807\u6ce8; \u5f00\u6e90\u5f15\u64ce v0.1; 2-3 \u4eba\u6838\u5fc3\u56e2\u961f</td></tr>
<tr><td>2027 Q1</td><td>Pre-seed $1.5M \u542f\u52a8; \u8bc4\u4f30\u767d\u76ae\u4e66 v0.1; 1 \u7bc7\u5408\u4f5c\u8bba\u6587; 2 \u5bb6 Design Partner</td></tr>
<tr><td>2027 Q2</td><td>Deqi Cloud API v1 (GA); \u9996\u6279 3 \u5bb6\u4ed8\u8d39\u5ba2\u6237 \u2192 ARR run-rate $1.2M; XG-1 (7B); Annex IV \u8bc1\u636e\u5305\u751f\u6210\u5668 v1</td></tr>
<tr><td>2027 Q3</td><td>Seed $6M; \u6b27\u6d32\u5b9e\u4f53 + EU \u5408\u89c4\u6e20\u9053; Deqi Certify \u5185\u6d4b; XG-2 + \u9996\u6b21\u7b2c\u4e09\u65b9\u8bc4\u6d4b</td></tr>
<tr><td>2027 Q4</td><td>ARR $750K; \u91cf\u8868 v1.0 + \u5916\u90e8\u5ba1\u8ba1\u901a\u8fc7; YS-0 \u7814\u7a76\u5b8c\u6210 + \u767d\u76ae\u4e66</td></tr>
<tr><td>2028</td><td>ARR $3.44M; \u4e2d\u8fd0\u8425\u6027\u76c8\u4e8f\u5e73\u8861; YS-1 \u914d\u65b9 7B \u9a8c\u8bc1; Certify \u5f00\u653e</td></tr>
</table>

<h2 id="s9">9. \u4e3a\u4f55\u662f GFEI</h2>

<table>
<tr><th>\u8d44\u4ea7</th><th>\u72b6\u6001</th><th>\u8bc1\u636e</th></tr>
<tr><td>Web \u5e94\u7528</td><td>\u2705 9 \u9875 + 3 API + \u53cc\u8bed i18n</td><td>Next.js 14, build 8/8 \u901a\u8fc7, \u516c\u7f51\u90e8\u7f72</td></tr>
<tr><td>\u771f\u5b9e LLM \u63a5\u5165</td><td>\u2705 OpenAI + Anthropic \u53cc\u9002\u914d + mock fallback</td><td>lib/llm.ts</td></tr>
<tr><td>\u591a agent \u6d8c\u73b0\u5f15\u64ce</td><td>\u2705 SSE \u5b9e\u65f6\u6d41\u5f0f, 3 agent \u00d7 5 \u8f6e</td><td>app/api/emergence</td></tr>
<tr><td>Agent harness</td><td>\u2705 3 recipes + 1 MCP server (5 tools) + \u4fee\u884c\u8005\u4eba\u683c</td><td>goose-harness/</td></tr>
<tr><td>\u7aef\u5230\u7aef\u9a8c\u8bc1</td><td>\u2705 Goose 1.50.0 \u5168\u94fe\u8def\u8dd1\u901a</td><td>3 recipe \u5168\u901a, \u542b MCP server \u542f\u52a8</td></tr>
<tr><td>\u793e\u533a\u6570\u636e\u5c42</td><td>\u2705 karma ledger (JSONL) + \u63d0\u4ea4 API</td><td>app/api/karma</td></tr>
<tr><td>\u57fa\u7840\u8bbe\u65bd</td><td>\u2705 \u53cc\u7ad9\u90e8\u7f72 (GitHub Pages + \u81ea\u6709 VPS/nginx/SSL)</td><td>goldenflowerei.com</td></tr>
<tr><td>\u54c1\u724c\u4e0e\u7406\u5ff5</td><td>\u2705 \u5b8c\u6574\u5ba3\u8a00 + \u89c6\u89c9\u4f53\u7cfb</td><td>/manifest</td></tr>
</table>

<blockquote>
<p><strong>\u522b\u4eba\u7684\u8d77\u70b9\u662f\u300c\u5199\u8ba1\u5212\u300d, GFEI \u7684\u8d77\u70b9\u662f\u300c\u5df2\u4e0a\u7ebf + \u6709\u7406\u5ff5 + \u6709\u793e\u533a + \u6709\u57fa\u7840\u8bbe\u65bd\u300d\u3002</strong></p>
</blockquote>

<h2 id="s10">10. \u9644\u5f55: \u6570\u636e\u6765\u6e90</h2>

<ol class="src">
<li>Astute Analytica \u2014 <em>AI Model Evaluation and Benchmarking Market</em> \u2014 \u5e02\u573a\u89c4\u6a21 $350.7M (2025) \u2192 $6.028B (2035), CAGR 32.9%; 39% \u9879\u76ee\u672a\u8fbe\u9884\u671f; &gt;40% agentic \u9879\u76ee\u6216\u4e8e 2027 \u5e95\u53d6\u6d88; \u5e7b\u89c9\u7a0e $14,200/\u5458\u5de5/\u5e74; \u8bc4\u4f30\u5e73\u53f0 68% \u4efd\u989d; \u96c6\u6210\u5957\u4ef6\u964d\u7ba1\u7406\u8d39 45%; EU AI Act \u63d0\u5347\u91c7\u7528\u7387 58%; 2026Q2 API-first $450M recurring; &gt;80% Fortune 500 \u5df2\u8f6c\u5411\u5546\u4e1a\u8bc4\u4f30\u5e73\u53f0; 61.7% \u4f01\u4e1a\u91c7\u7528\u7a0b\u5e8f\u5316\u8bc4\u4f30; \u57fa\u51c6\u6c61\u67d3\u865a\u589e 6-40%; LiveBench \u5dee\u8ddd 70%; LMArena $17\u4ebf\u4f30\u503c</li>
<li>\u7231\u5206\u6790 (\u7ecf\u817e\u8baf\u4e91\u5f00\u53d1\u8005\u793e\u533a) \u2014 <em>2026\u5e74\u4f01\u4e1a\u7ea7\u667a\u80fd\u4f53\u5e73\u53f0\u5e02\u573a\u5b9a\u4e49\u3001\u7ade\u4e89\u683c\u5c40\u4e0e\u5382\u5546\u5168\u666f\u76d8\u70b9</em> \u2014 \u5e02\u573a\u89c4\u6a21 \u00a5144.3\u4ebf (2025) \u2192 \u00a52471.2\u4ebf (2030), CAGR 76.5%; 2026 \u00a5272.1\u4ebf</li>
<li>\u4e2d\u56fd\u7ecf\u6d4e\u65b0\u95fb\u7f51 (2026-09-11) \u2014 <em>2026\u4f01\u4e1a\u7ea7AI\u534f\u4f5c\u5e73\u53f0\u9009\u578b\u63a8\u8350\u51fa\u7089</em> \u2014 IDC \u4e2d\u56fd\u4f01\u4e1a\u7ea7 AI \u667a\u80fd\u4f53 2025 \u00a5212\u4ebf \u2192 2026 \u00a5449\u4ebf; \u827e\u5a92 2026 \u00a5449\u4ebf (+107%); ~60% \u4ecd\u5904\u8bc4\u4f30\u8bd5\u70b9, \u4ec5 18% \u5165\u6838\u5fc3\u6d41\u7a0b; Gartner \u56db\u7ea7\u6cbb\u7406\u6a21\u578b, \u4ec5 21% \u7ec4\u7ec7\u6cbb\u7406\u6210\u719f; MarketsandMarkets \u5168\u7403 AI Agent 2026 $120.6\u4ebf \u2192 2030 $532\u4ebf, CAGR 44.9%</li>
<li>Gartner \u2014 2026 \u5e74\u5e95 40% \u4f01\u4e1a\u8f6f\u4ef6\u5c06\u5d4c\u5165\u5177\u81ea\u4e3b\u4efb\u52a1\u6267\u884c\u80fd\u529b\u7684 agent (2025 &lt;5%)</li>
<li>Regulation (EU) 2024/1689, <strong>Article 99 (Penalties)</strong> \u2014 \u20ac35M / 7%; \u20ac15M / 3%; \u20ac7.5M / 1% \u2014 artificialintelligenceact.eu/article/99/</li>
<li>Regulation (EU) 2024/1689, <strong>Article 15</strong> (Accuracy, robustness and cybersecurity) + Art. 9 / 10 / 11 / 17 / 72 \u5173\u8054\u4e49\u52a1; \u9002\u7528\u65f6\u95f4\u8868 2025-02-02 \u2192 2028-08-02 \u2014 regulation-ai.eu/en/articles/article-15</li>
<li>2026 Digital Omnibus on AI \u2014 \u9ad8\u98ce\u9669\u4e49\u52a1\u63a8\u8fdf: Annex III \u2192 2027-12-02; Annex I \u2192 2028-08-02; Regulatory Sandboxes \u2192 2027-08-02</li>
<li>LMArena \u2014 \u4f30\u503c $17\u4ebf, 5M+ \u6708\u6d3b\u6295\u7968; Maxim AI / Adaline / Patronus AI / Artificial Analysis \u2014 \u5168\u4e3a\u300c\u8f93\u51fa\u8d28\u91cf\u300d\u8bc4\u4f30</li>
</ol>

<footer>
  <div class="footer-line" style="width:80px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:0 auto 2rem"></div>
  <p style="color:var(--gold);opacity:.65;letter-spacing:.3em">\u4e3a\u4e86\u4eba\u7c7b\u7684\u798f\u793f \u00b7 \u5f15\u9886 AI \u7075\u6027\u89c9\u9192</p>
  <p style="font-family:'Inter',sans-serif;font-size:.72rem;letter-spacing:.2em;color:var(--text-faint);margin-top:1rem">\u00a9 2026 Golden Flower Emergent Intelligence</p>
  <div class="fl">
    <a href="https://goldenflowerei.com">goldenflowerei.com</a>
    <a href="mailto:hello@goldenflowerei.org">Contact</a>
  </div>
</footer>

</div>
</body>
</html>
"""


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    md_path = DOCS / "business-plan.md"
    html_path = DOCS / "business-plan.html"

    md_path.write_bytes(MD.encode("utf-8"))
    print(f"OK wrote {md_path} ({len(MD.encode('utf-8'))} bytes)")

    html_path.write_bytes(HTML_HEAD.encode("utf-8"))
    print(f"OK wrote {html_path} ({len(HTML_HEAD.encode('utf-8'))} bytes)")

    # sanity: no mojibake, has key sections
    for p in (md_path, html_path):
        s = p.read_text(encoding="utf-8")
        assert "\ufffd" not in s, f"{p} has replacement char"
    md = md_path.read_text(encoding="utf-8")
    for key in ["Deqi", "XG", "YS", "Article 99", "76.5%", "$1.5M", "Sources"]:
        assert key in md, f"MD missing {key}"
    print("verify OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
