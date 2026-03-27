---
name: token-switch
description: 当用户要求切换token体系、尝试不同token方案或不同配色时使用。该技能会从项目othertokens提供可选系统，按层级映射执行切换，完成自动校验，并输出前后多维度对比分析报告。
---

# Token Switch

## 概览

实现 `plus-v1.0` / `basic-v1.0` 项目的 token 系统一键切换能力。支持“先展示可选系统再切换”与“按用户指定系统直接切换”两种路径，并在切换后自动做一致性检查与对比分析。Skill 不强制绑定单一项目，按 `--project-root` 指向的工程执行。

## 触发条件

在出现以下用户意图时触发：
- 切换 token
- 尝试不同 token 方案
- 尝试不同配色体系
- 指定切换到 `iOS` / `Material` / `Microsoft` / `One+UI`

## 工作流

### 1) 预加载 `othertokens`（必须先执行）

为确保 Skill 可在任意仓库使用，第一步先从远程仓库拉取 `othertokens` 到目标项目：

```bash
TOKENS_REPO=<remote-repo-url>; PROJECT_ROOT=<project-root>; TMP_DIR=$(mktemp -d) && git clone --depth 1 --filter=blob:none --sparse "$TOKENS_REPO" "$TMP_DIR" && cd "$TMP_DIR" && git sparse-checkout set othertokens && mkdir -p "$PROJECT_ROOT/othertokens" && cp -R othertokens/. "$PROJECT_ROOT/othertokens/"
```

说明：
- `TOKENS_REPO`：包含 `othertokens/` 目录的远程仓库地址（SSH/HTTPS 均可）
- `PROJECT_ROOT`：当前要执行切换的项目根目录（可为 `plus-v1.0`、`basic-v1.0` 或其他同结构仓库）

### 2) 识别切换模式

- 若用户未明确指定目标系统：先列出 `othertokens/*.tokens.json` 可选项，再让用户选择。
- 若用户已指定目标系统：直接进入执行步骤。

### 3) 执行切换

在目标项目根目录执行（`plus-v1.0` / `basic-v1.0` 均可）：

```bash
python3 .codebuddy/skills/token-switch/scripts/switch_tokens.py --list --project-root <project-root>
```

```bash
python3 .codebuddy/skills/token-switch/scripts/switch_tokens.py --target iOS --project-root <project-root> --apply --report md/TOKEN_SWITCH_REPORT.md
```

参数说明：
- `--list`：列出可用 token 系统
- `--target`：目标系统名（支持 stem 或文件名）
- `--apply`：真正写入文件（缺省为 dry-run）
- `--report`：输出对比报告路径

### 4) 自动检查（必须执行）

切换后必须确认：
- `json/index.json` 可正常解析
- `css/*.css` 中 `--qq-*` 与 `--color-*` 变量完成替换；`tokens.css` 变量按“目标有对应 token 则替换、无对应则保留原值”执行
- 报告文件已生成

如检查失败：
- 立即告知失败点
- 给出可执行修复建议
- 不宣称切换成功

### 5) 输出对比分析结论

基于 `md/TOKEN_SWITCH_REPORT.md` 汇总输出以下维度：
- 变化覆盖率（映射总数 / 实际变化数）
- 颜色语义变化（文本色、品牌色、背景色、分割色）
- CSS 全量替换率（`--qq-*`、`--color-*`）
- 工程影响范围（受影响文件）
- 风险与兼容性（未命中变量、潜在视觉偏差）

## 映射约束

- 严格遵循层级映射：`json/index.json -> tokens.color.*` 对齐 `othertokens/*.tokens.json -> Color.*`
- 禁止随机替换、禁止脱离映射表手工改值
- 映射定义见 `references/token_mapping.json`

## 资源

- `scripts/switch_tokens.py`：执行列出/切换/校验/报告
- `references/token_mapping.json`：层级映射关系

## 响应模板

切换完成后使用简洁结论模板：
- 已切换至：`<system>`
- 核心变化：`<N>` 项，覆盖率 `<X>%`
- 校验结果：`JSON ✅/❌`，`CSS ✅/⚠️`
- 报告位置：`md/TOKEN_SWITCH_REPORT.md`
