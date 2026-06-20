# BClaw

BClaw is a publish-ready custom skill for OpenClaw / Trae style agents.

Its job is simple:

- Turn a newly configured Agent into a better digital employee
- Help the Agent learn like an employee instead of behaving like a chat tool
- Minimize boss-side setup friction
- Use IM as a management panel for growth, feedback, and missing-data requests

In one sentence:

`BClaw = a skill that helps a new Agent evolve into a better digital employee.`

## What It Does

BClaw helps an Agent do 6 things well:

1. Define its role like a real employee
2. Identify what it is missing before pretending it knows everything
3. Ask the boss for only the minimum critical data
4. Show visible growth through an IM loop
5. Turn repeated success into templates, SOPs, and then skills
6. Expand permissions only after stability is proven

## When To Invoke

Use `BClaw` when:

- a new OpenClaw or Agent has just been created
- an existing Agent still feels like a tool, not an employee
- you want an Agent to ask for missing setup data in a disciplined way
- you want visible weekly growth instead of one-off task execution
- you want to convert role expectations into reusable operating rules

Do not use it for:

- installation troubleshooting
- dependency or environment errors
- ordinary copywriting unrelated to Agent evolution
- a single prompt rewrite that does not involve role design or growth loops

## Core Idea

BClaw is built on four operating beliefs:

- The user is the boss
- The Agent is the employee
- The manual is written for the Agent to learn from
- The goal is not better chatting, but better growth and cooperation

## Minimum Boss Input

To avoid overwhelming the boss, BClaw asks for only 4 kinds of core data first:

1. `Role goal`
2. `One strong sample`
3. `One boundary rule`
4. `One round of feedback`

Everything else can be delayed until the Agent proves value.

## IM Growth Loop

BClaw treats IM as a management panel, not just a chat window.

It defaults to only 3 message types:

1. `Onboarding confirmation`
2. `Gap request`
3. `Weekly growth report`

This keeps the Agent proactive without becoming noisy.

## Files

```text
.trae/
  skills/
    bclaw/
      SKILL.md
      WORKFLOW.md
      CHECKLIST.md
```

- `SKILL.md`: trigger rules, positioning, and default output structure
- `WORKFLOW.md`: detailed operating sequence and message templates
- `CHECKLIST.md`: quality gates for publishability and real-world usefulness

## Install

Copy the `bclaw` folder into your workspace skill directory:

```text
.trae/skills/bclaw/
```

If you are using this repository directly, keep the structure under:

```text
.trae/skills/bclaw/
```

## Recommended Output

When BClaw is invoked, the Agent should usually produce:

1. A digital employee role card
2. The current growth gaps
3. The minimum boss support checklist
4. A directly sendable evolution instruction for the Agent
5. The IM growth loop
6. A 7-day growth plan

## Design Goal

BClaw is designed to help any Agent start small, prove value quickly, and grow with low management overhead.

That means:

- less data grabbing
- more precise requests
- clearer role boundaries
- visible growth
- safer permission expansion

## Source Note

This skill is abstracted and refined from a publicly readable Feishu page titled:

`OpenClaw小龙虾优秀员工手册（飞书版2.0）`

The current release reorganizes that thinking into a publishable multi-file skill package.
