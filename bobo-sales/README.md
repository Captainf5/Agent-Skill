# bobo-sales · 政企销售作战参谋

[中文](#中文) | [English](#english)

---

<a id="中文"></a>

## 中文

### 简介

一个给政企 / ToB 大客户销售用的分析工具。它做的不是销售培训，而是**把手上这一单拆开看，判断该不该打、卡在哪、下一步做什么**。

它整合了八套经典销售方法论，并在最后加了一层**中国本土校准**——因为那些方法论诞生于"决策理性、角色清晰、流程可文档化、说真话没有社交成本"的前提，而这四条在中国政企里条条打折。

### 解决什么问题

销售最常问的不是"怎么讲产品"，而是这几句：

- 客户一直说太贵，怎么办
- 客户只认价格，品质都追平了，我们凭什么
- 这单还值不值得跟
- 客户不给我信息，却要我限期报价
- 客户跟对手关系很深，怎么切进去

这些问题的共同点是：**它们看起来是话术问题，实际大多是判断问题。**

### 两种用法

**用法一：案例研判（最常用）**

贴一段客户对话、一封邮件、拜访纪要、招标文件片段，或者就一句话吐槽。输出固定六段，450 字内：

```
【判断】一句话结论，含"不是 ____"的排除项
【断点】卡在哪一环，依据是材料里的哪句话
【打法】①②③，每条带时间与动作
【话术】可照念的，最多三句
【本土提醒】命中哪个中国场景偏差，写成具体动作
【我要确认】一个能改变结论的问题
```

**用法二：商机作战包**

给结构化背景（客户、产品、阶段、金额、联系人），输出完整六段：决策链地图 / 资格判定 / 商业洞察 / 提问清单 / 异议预案 / 下一步承诺目标。

### 判断分六层

| 层 | 回答什么 | 框架 |
|---|---|---|
| L1 资格层 | 这单该不该打 | MEDDIC |
| L2 组织层 | 打谁、谁说了算 | Miller Heiman 战略销售 |
| L3 价值层 | 凭什么让客户付溢价 | The Challenger Sale |
| L4 对话层 | 见了面怎么说 | SPIN Selling + Never Split the Difference |
| L5 关系层 | 长期怎么被信任 | The Trusted Advisor + Influence |
| L6 本土校准 | 这套东西在中国哪里会碎 | 自建：七条偏差 |

**注意：SPIN 只占 L4，不是核心。** 大单输赢很少取决于提问技巧。

### L6 本土校准的七条

1. 决策人不看职级，看**谁能叫停会议**
2. **招标不是决策，是决策的演出**（问"挂网前谁点头才动得了"）
3. 挑战者会被读成不懂事 → 改**请教式挑战**，结论必须让客户自己说出来
4. 信任公式少一项：**你是不是"自己人"**（表态 ≠ 违规）
5. 关系不是送礼，是**降低他的工作风险**
6. 有些单不是推的，是**养的**
7. **该请领导出场就请**，同级对同级，领导只做给面子不谈价格

### 边界

- **适用**：政企、大客户、长周期、多决策人的复杂销售
- **不适用**：零售、小单、快消、纯电销——这些场景用 SPIN 这类大单方法收益有限
- **合规**：不提供任何形式的利益输送、回扣、围标串标、泄露标底建议。涉及招投标只讲合规竞争策略

### 文件结构

```
bobo-sales/
├── SKILL.md                        总控：入口、判断层级、输出契约、兜底
├── references/
│   ├── frameworks.md               八个框架的知识骨架（唯一来源）
│   ├── china-context.md            L6 七条本土偏差
│   ├── case-triage.md              案例研判流程 + 判断锚点表
│   ├── playbook-workflow.md        作战包六段流程
│   └── scoring-rubric.md           MEDDIC 打分标准
├── assets/
│   ├── brief-template.md           作战包模板
│   └── case-input.md               案例提供模板
└── scripts/
    └── qualify_opportunity.py      商机资格打分脚本
```

### 致谢与来源

方法论来自 Neil Rackham《SPIN Selling》、Matthew Dixon & Brent Adamson《The Challenger Sale》、Miller & Heiman《The New Strategic Selling》、MEDDIC 资格模型、Chris Voss《Never Split the Difference》、Cialdini《Influence》、Maister 等《The Trusted Advisor》、Jill Konrath《SNAP Selling》。

L6 本土校准层与政企场景映射为原创补充，**不得冠以原著名义**。本 Skill 不提供页码级引用。

---

<a id="english"></a>

## English

### What it is

An analysis tool for enterprise and B2B sales in China's government and state-owned-enterprise market. It is **not** a sales training course. It takes one deal and answers three questions: should you pursue it, where is it stuck, and what to do next.

It combines eight established sales methodologies and adds a final **China localization layer**, because those frameworks all assume rational decisions, clear role boundaries, documented processes, and zero social cost to speaking plainly — assumptions that all weaken in Chinese enterprise sales.

### Two modes

**Mode 1 — Case triage (most used).** Paste a client conversation, email, visit notes, tender document, or a one-line complaint. Output is always six fixed blocks under 450 characters: Verdict / Where it broke / Three moves / Script you can read aloud / Local-context warning / The one question that would change the verdict.

**Mode 2 — Opportunity battle plan.** Give structured background and receive six sections: decision-map, qualification score, commercial insight, question list, objection playbook, next-step commitment.

### Six-layer judgment model

L1 Qualification (MEDDIC) → L2 Organization (Miller Heiman) → L3 Value (Challenger) → L4 Conversation (SPIN + Voss) → L5 Relationship (Trusted Advisor + Cialdini) → L6 China localization.

**SPIN sits only at L4.** Big deals are rarely won or lost on questioning technique.

### Boundaries

Best for complex, long-cycle, multi-stakeholder enterprise deals. Not designed for retail, small-ticket, or pure telesales. Compliance is non-negotiable: no bribery, bid-rigging, or insider-bid information — ever.

### Sources

Methodologies belong to their respective authors (Rackham; Dixon & Adamson; Miller & Heiman; MEDDIC; Voss; Cialdini; Maister et al.; Konrath). The L6 localization layer and China enterprise mappings are original additions and must not be attributed to those authors.
