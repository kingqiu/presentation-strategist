# 汇报策略师 Presentation Strategist

当前版本：`v0.1.0`

一个帮助你先想清楚“怎么讲”，再去制作 PPT 的 Agent Skill。

很多 PPT 工具和 AI Skills 都在解决“怎么把页面做得更精良、更美观”：配色、字体、模板、图表、动画、版式。这些当然重要，但它们主要解决的是 PPT 的外形。

`presentation-strategist` 想解决的是另一件事：**赋予 PPT 内核与灵魂**。

一份真正有效的 PPT，不只是好看，也应该有清晰的判断、可信的证据、准确的听众洞察和能推动行动的故事线。它要回答：

- 这场汇报到底要改变谁的想法？
- 听众为什么应该相信你？
- 你的核心判断是什么？
- 哪些证据足够强，哪些还只是猜测？
- 应该按什么顺序讲，才能让人听懂、相信，并愿意行动？

`presentation-strategist` 关注的就是这些问题。它不是 PPT 美化工具，而是 PPT 的策略与表达内核工具。它会帮助你把一个模糊的汇报需求，整理成一份更清晰、更有逻辑、更有证据、更适合生成 PPT 的框架。

## 适合什么场景

适合用在：

- 向老板汇报项目进度、风险、预算或资源诉求
- 给客户做方案介绍、销售提案或 PoC 争取
- 做公司介绍、产品介绍、解决方案介绍
- 创业融资路演、商业计划展示
- 求职面试中的个人展示或作品集讲述
- 业务复盘、季度复盘、经营分析
- 技术方案评审、架构决策汇报
- 危机、延期、坏消息或风险汇报
- 企业 AI 普及培训、AI enablement、知识分享
- Review 已有 PPT 大纲，找逻辑问题和证据缺口

不适合用在：

- 单纯美化 PPT
- 调整字体、颜色、动画、版式
- 直接生成最终 PPTX 文件
- 只找模板、不需要梳理表达逻辑

## 它会输出什么

默认输出是一份给人看的汇报策略框架，通常包括：

- 对当前场景的判断
- 听众是谁，以及他们当前的认知状态
- 这场汇报真正要达成的目标
- 推荐的核心判断和故事线
- 逐页 slide 框架
- 每页的行动标题、关键信息、内容块和证据建议
- 哪些地方证据不足
- 下一步应该补充或验证什么

当你认可这个框架之后，也可以继续要求它输出一份更详细的版本，用于交给 AI PPT 工具生成真正的 PPT。

也可以指定输出长度，例如：

- 快速建议
- 3 分钟口播结构
- 5 页 PPT 框架
- 10 页详细框架
- 只做 review，不重写
- 给 AI PPT 工具的详细 brief

## 示例

你可以这样问：

```text
我明天要跟老板汇报一下当前项目进度，但现在有延期风险。帮我想一下这份 PPT 应该怎么讲。
```

或者：

```text
我们要给一家大型制造企业介绍公司的供应链管理软件，希望让对方相信这个产品能帮助他们降低库存压力、提升交付可视化，并愿意安排一次后续方案评审。汇报时间 30 分钟以内，帮我设计这次产品介绍的框架。
```

也可以是：

```text
我要给一家公司的员工做 90 分钟 AI 普及培训，听众不是技术背景。帮我设计一份培训型 PPT 的结构。
```

## 安装方式

将 `presentation-strategist/` 目录放到支持 `SKILL.md` 的 Agent 平台技能目录中即可。

常见目录示例：

```text
~/.codex/skills/presentation-strategist
~/.claude/skills/presentation-strategist
~/.openclaw/workspace/skills/presentation-strategist
~/.hermes/skills/presentation-strategist
```

如果你的平台支持显式调用，可以这样使用：

```text
Use $presentation-strategist to help me design this presentation.
```

如果平台支持自动触发，当你提出“PPT 思路”“汇报逻辑”“pitch deck”“sales deck”“帮我想清楚怎么讲”等请求时，也可以自动调用。

## 目录结构

```text
presentation-strategist/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evaluation/
├── references/
├── scripts/
└── templates/
```

其中：

- `SKILL.md` 是主技能说明。
- `evaluation/` 存放验证集、评分规则和自我改进记录结构。
- `references/` 存放场景、框架、案例和质量检查规则。
- `scripts/` 存放验证、打包和自我改进相关脚本。
- `templates/` 存放可复用的输出模板。
- `agents/openai.yaml` 是 Codex 相关的界面元数据，其他平台可以忽略。

公开示例可以查看：

```text
examples/
```

打包发布可以使用：

```text
python3 scripts/package_skill.py --check
python3 scripts/package_skill.py --clean
```

验证单个 skill 包可以使用：

```text
python3 presentation-strategist/scripts/validate_skill_package.py presentation-strategist
```

## 自我进化引擎

这个仓库包含一套实验性的 self-improvement loop，用来让 skill 在验证集上持续校准自己，而不是只靠人工凭感觉改规则。

核心流程是：

```text
验证任务 -> 模型输出 -> 自动评分 -> 失败标签聚合 -> 候选修改 -> 门控接受/拒绝 -> 记录每轮结果
```

相关文件：

- `presentation-strategist/evaluation/validation_set.jsonl`：验证样本。
- `presentation-strategist/evaluation/scoring-rubric.md`：100 分制评分规则。
- `presentation-strategist/scripts/run_validation.py`：生成验证任务，或通过 `--agent-command` 调用外部 agent。
- `presentation-strategist/scripts/score_outputs.py`：自动评分并生成失败标签；默认使用本地 deterministic scorer，也可以通过 `--judge-command` 接入 LLM judge。
- `presentation-strategist/scripts/propose_candidate_edit.py`：根据失败标签提出小范围候选修改。
- `presentation-strategist/scripts/gate_candidate.py`：比较当前版本和候选版本，决定接受或拒绝。
- `presentation-strategist/scripts/summarize_evolution.py`：汇总进化日志，生成最近 N 轮的可读报告。

每一轮进化都会写入 `evaluation/runs/` 下的详细产物，并追加到 `evaluation/evolution_log.jsonl`。这些运行时记录不会进入发布包。

最小手动流程：

```text
cd presentation-strategist
scripts/run_validation.py --skill-dir . --run-name current --limit 3
# 将模型输出放入 evaluation/runs/current/outputs/<sample-id>.md
scripts/score_outputs.py --skill-dir . --run-name current
scripts/propose_candidate_edit.py --skill-dir . --run-name current --create-candidate
scripts/summarize_evolution.py --skill-dir . --limit 10
```

如果你的 agent CLI 支持非交互执行，也可以通过 `--agent-command` 自动生成输出：

```text
scripts/run_validation.py \
  --skill-dir . \
  --run-name current \
  --agent-command 'your-agent < {prompt_file} > {output_file}'
```

`{prompt_file}`、`{output_file}`、`{sample_id}` 和 `{skill_dir}` 会由脚本自动填充。具体 CLI 参数请按你的 agent 环境调整。

如果你想用 LLM judge 做更细的语义评分，可以给 `score_outputs.py` 传入 judge 命令：

```text
scripts/score_outputs.py \
  --skill-dir . \
  --run-name current \
  --judge-command 'your-judge < {prompt_file} > {output_file}'
```

judge 需要返回结构化 JSON 分数；如果 judge 调用失败，脚本会默认回退到 deterministic scorer。

## 日志与隐私

自我进化流程可能会保存验证输入、模型输出、评分结果和候选修改建议。请不要把真实客户资料、公司机密、个人隐私或未脱敏业务数据直接写入公开仓库。

发布包会自动排除：

- `evaluation/runs/`
- `evaluation/evolution_log.jsonl`
- `evaluation/accepted_edits.jsonl`
- `evaluation/rejected_edits.jsonl`
- `evaluation/feedback/records.jsonl`
- Python 缓存和本地临时文件

## 兼容性

这个 skill 采用通用的 `SKILL.md` 目录结构，目标是兼容多个 Agent 平台，包括：

- Codex
- Claude Code / Claude Agent Skills
- OpenClaw
- Hermes Agent

不同平台的安装路径和触发方式可能略有差异，请以各平台的官方说明为准。

## 设计原则

这个 skill 遵循几个简单原则：

- 先定义听众变化，再设计 slides。
- 先建立商业论证，再选择故事线。
- 强证据支持强诉求，弱证据只适合低风险下一步。
- 每一页 slide 都应该有一个明确的逻辑任务。
- 不用漂亮页面掩盖薄弱证据。
- 高价值场景可以增加额外 review，但不让分析变得冗长。

## 当前状态

当前版本可以用于实际试跑和继续迭代。  
它已经包含发布校验、打包清理和基础自我进化引擎。建议在正式大规模发布前，继续补充更多真实业务场景验证样本，并用干净安装流程做回归测试。
