# Agent-Skill

适合各 Agent 的各类 Skills，集中管理。

## Skills 目录

| Skill | 说明 | 安装路径 |
|-------|------|----------|
| [crb-doc-review](./crb-doc-review/) | 华润饮料公文90分自检助手 — 通知/请示/总结/讲话稿/会议纪要等内部正式材料审稿评分、诊断和优化改写 | `~/.workbuddy/skills/crb-doc-review/` |
| [bclaw](./bclaw/) | Agent 员工化技能 — 把新 Agent 培养成数字员工 | `~/.workbuddy/skills/bclaw/` |

## 安装方式（WorkBuddy 用户）

1. 下载对应 Skill 目录下的 `SKILL.md`
2. 放到自己机器的 `~/.workbuddy/skills/<skill-name>/SKILL.md`
3. 重启 WorkBuddy 即可生效

例如安装公文自检助手：
```bash
mkdir -p ~/.workbuddy/skills/crb-doc-review
# 将 SKILL.md 下载后放入该目录
```

---

## Skill 详情

### crb-doc-review — 华润饮料公文90分自检助手

粘贴一篇初稿，自动触发6步审稿流程：
1. 文种与场景判断
2. 5维度评分（总分100）
3. 主要问题诊断表
4. 90分优化稿
5. 人工复核清单
6. 提交达标判断

支持的文种：培训通知、工作请示、工作总结、会议讲话稿、会议纪要、汇报材料、其他内部正式材料

### bclaw — Agent 员工化技能

帮助新 Agent 从工具进化为数字员工：
- 定义角色如正式员工
- 识别自身知识缺口
- 向老板请求最小关键数据
- 通过 IM 循环展示成长
- 将重复成功转化为模板和 SOP
- 稳定后才扩展权限

文件结构：
- `SKILL.md`：触发规则、定位和默认输出结构
- `WORKFLOW.md`：详细操作序列和消息模板
- `CHECKLIST.md`：发布质量和实用性的质量门
