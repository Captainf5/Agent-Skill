#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""政企/ToB 商机资格打分（MEDDIC）。

用法:
    python qualify_opportunity.py brief.json [--json]

brief.json 示例:
{
  "client": "某某集团",
  "stage": "立项",
  "metrics": 2,
  "economic_buyer": 1,
  "decision_criteria": 2,
  "decision_process": 3,
  "identify_pain": 2,
  "champion": 0
}

每项取值 0-3，缺失视为 0。economic_buyer 与 champion 权重 x2。
"""

import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

DIMS = [
    ("metrics", "M Metrics 量化收益", 1),
    ("economic_buyer", "E Economic Buyer 经济买家", 2),
    ("decision_criteria", "D Decision Criteria 决策标准", 1),
    ("decision_process", "D Decision Process 决策流程", 1),
    ("identify_pain", "I Identify Pain 痛点", 1),
    ("champion", "C Champion 内部冠军", 2),
]

SCORE_MEANING = {
    0: "未确认",
    1: "部分确认",
    2: "已确认但有缺口",
    3: "已确认且稳固",
}

LEVELS = [
    (80, "A", "可重点投入：按作战包推进，配置资源"),
    (60, "B", "补缺口后投入：只补最低分两项，补完复评"),
    (40, "C", "低优先级：降级为跟踪，设定复评时间点"),
    (0, "D", "暂不投入：先做资格补齐动作，不投入方案与报价资源"),
]


def clamp(v):
    try:
        n = int(v)
    except (TypeError, ValueError):
        return 0
    return max(0, min(3, n))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("用法: python qualify_opportunity.py brief.json")
        return 1

    with open(args[0], "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    total = 0
    full = 0
    for key, label, weight in DIMS:
        score = clamp(data.get(key, 0))
        max_score = 3 * weight
        total += score * weight
        full += max_score
        rows.append((key, label, score, weight, max_score))

    pct = round(total / full * 100, 1) if full else 0.0

    # 一票否决
    veto = []
    if clamp(data.get("economic_buyer", 0)) == 0:
        veto.append("E=0：完全不知道谁批钱")
    if clamp(data.get("champion", 0)) == 0 and data.get("stage") in ("方案", "评标", "商务", "招投标"):
        veto.append("C=0 且项目已过需求阶段：到方案/评标阶段仍无内部支持者")

    level, action = LEVELS[-1][1], LEVELS[-1][2]
    for threshold, lv, act in LEVELS:
        if pct >= threshold:
            level, action = lv, act
            break
    if veto:
        level, action = "D", "一票否决：" + "；".join(veto)

    # 缺口排序：权重 x (3 - 得分)
    gaps = sorted(rows, key=lambda r: -(r[3] * (3 - r[2])))
    top_gaps = [g for g in gaps if g[2] < 3][:3]

    if "--json" in sys.argv:
        out = {
            "client": data.get("client", ""),
            "total": pct,
            "level": level,
            "action": action,
            "veto": veto,
            "dimensions": [
                {"key": k, "label": lb, "score": s, "weight": w,
                 "meaning": SCORE_MEANING[s]}
                for k, lb, s, w, _m in rows
            ],
            "top_gaps": [{"label": g[1], "score": g[2]} for g in top_gaps],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    print("=" * 52)
    print("商机资格评分  %s" % (data.get("client", ""),))
    if data.get("stage"):
        print("阶段：%s" % data["stage"])
    print("=" * 52)
    for _k, label, score, weight, _m in rows:
        w = "  (权重x2)" if weight == 2 else ""
        print("  %-32s %d/3  %s%s" % (label, score, SCORE_MEANING[score], w))
    print("-" * 52)
    print("总分  %.1f / 100      级别  %s" % (pct, level))
    print("建议  %s" % action)
    if veto:
        print("否决  %s" % "；".join(veto))
    print("-" * 52)
    print("前三大缺口（按对成交影响排序）：")
    if top_gaps:
        for i, g in enumerate(top_gaps, 1):
            print("  %d. %s（当前 %d 分，差 %d 分）" % (i, g[1], g[2], 3 - g[2]))
    else:
        print("  无缺口，六项均已确认")
    print("=" * 52)
    return 0


if __name__ == "__main__":
    sys.exit(main())
