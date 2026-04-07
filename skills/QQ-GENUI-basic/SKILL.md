---
name: QQ-GENUI-basic
description: 当用户生成界面（页面/UI/组件）或局部调整界面（增删组件、修改样式、替换图标等）时必须触发。基于 QQ_GenUI 设计系统远程资源产出移动端页面与组件方案；规范文档和 Token 通过 GitHub 远程按需读取；页面实际用到的图标会下载到本地 `assets/icons/` 目录并打包，确保离线可用；首次使用时会在项目根目录创建 `failure-log.md`，后续每次生成/调整前必读，失败或重试后必写；强制 Gate 流程逐步验收，不可跳步，最多3轮回归修复，若仍不合规则继续交付并附问题清单。
---

# QQ-GENUI-basic

## 概述

使用本 skill 将 `QQ_GenUI` 设计系统转化为"强约束可执行流程"。
设计资源（规范文档、Token）通过 GitHub **远程按需读取**，不克隆仓库。
**页面实际用到的图标**会下载到本地 `assets/icons/` 目录，HTML 中使用本地相对路径引用，确保离线环境下页面也能正常显示。
首次使用本 skill 时，必须先检查项目根目录是否存在 `failure-log.md`；若不存在，则立即在项目根目录创建，并可参考 `references/failure-log.md` 作为初始化模板。
后续每次生成或调整界面前，必须先读取项目根目录 `failure-log.md`，提取与当前任务相似的失败模式；每次发生失败、返工、重试或用户指出问题后，必须立刻写入项目根目录 `failure-log.md`，记录当前失败表现、根因与修复动作。
执行过程中必须通过 Gate 校验，禁止跳步、禁止并步；若 3 轮回归后仍有剩余问题，允许交付并显式列出未修复项。

## 何时使用

在以下场景必须触发（**无需用户显式指定本 skill，匹配即自动激活**）：

### 生成界面（全量）

- 用户要求"生成页面/界面/UI/组件"——无论是否提及本设计系统
- 用户要求"用组件库拼装页面并输出 HTML"
- 用户提供 Figma 截图/线框图/口头描述，要求产出可运行的移动端页面

### 局部调整界面

- 用户要求对已有界面进行**局部修改**，包括但不限于：
  - 增删组件、调整组件顺序或嵌套关系
  - 修改颜色、间距、圆角、字号等视觉属性
  - 替换图标、更换主题（Light ↔ Dark）
  - 修改文案、状态栏、导航栏等局部元素
  - 修复界面中的样式或布局问题
- 用户要求"微调/优化/美化/对齐"等隐含界面调整的表述

### 合规与校验

- 用户要求"检查组件组合是否合法"或"检查 Token/背景色是否合规"
- 用户要求"替换占位图标 `empty_icon.svg` 为真实图标"

### 触发判定规则

> **核心原则：凡涉及界面生成或界面修改，均必须触发本 skill。**
>
> 即使用户未明确提及"设计系统"或"QQ_GenUI"，只要请求的产出物是 UI 界面（HTML/页面/组件），就必须走本 skill 的 Gate 流程，以确保输出符合设计系统规范。

在以下场景**不**触发：

- 纯后端任务（API、数据库、服务端逻辑等）
- 与界面无关的通用前端问题（打包配置、性能优化、纯 JS 逻辑等）
- 纯文档编写、纯数据处理

## 远程资源访问约定

### Base URL

```
https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/
```

### 文件映射表

| 资源 | 远程路径 |
|------|----------|
| 入口指南 | `README.md` |
| 全局索引 | `json/index.json` |
| 颜色 Token | `css/QQ_color_tokens.css` |
| 通用 Token | `css/tokens.css` |
| 组件规范 | `md/<COMPONENT>_SPEC.md` |
| 组件数据 | `json/components/<component>.json` |
| 图标库目录 | `icons/QUI_24_icons/`（通过 GitHub 页面或 API 获取列表） |
| 单个图标 | `icons/QUI_24_icons/<icon-name>.svg` |
| 结构图标 | `icons/<icon-name>.svg` |

### 远程读取规则

- 使用 `web_fetch` 或等效工具读取 `raw.githubusercontent.com` 上的文件
- **禁止** `git clone`、`git pull` 或任何将整个仓库克隆到用户本地的操作
- **按需读取**：仅在当前 Gate 需要时才获取对应文件，不要一次性读取全部资源
- 若远程读取失败（网络问题/404），在当前 Gate 输出问题报告并暂停

### 图标本地化规则（重要）

页面实际用到的图标**必须下载到本地**，确保离线可用：

- **下载目录**：在生成页面的同级目录下创建 `assets/icons/` 目录
- **下载时机**：Gate 7（图标替换）阶段，确定页面所需图标后立即下载
- **下载方式**：通过 `web_fetch` 获取 SVG 内容，使用 `write_to_file` 写入本地 `assets/icons/<icon-name>.svg`
- **HTML 引用路径**：页面中所有图标统一使用本地相对路径 `assets/icons/<icon-name>.svg`，**禁止使用远程 URL**
- **仅下载所需图标**：不要下载整个图标库，只下载当前页面实际引用的图标文件
- **状态栏图标同理**：`network.svg`、`wifi.svg`、`battery.svg` 等状态栏图标也必须下载到本地

## 强制执行契约（GATE）

### 总则

- 从 Gate 1 开始顺序执行，必须 `1 → 2 → 3 → ...`。
- 每个 Gate 必须满足通过条件后才能进入下一 Gate。
- 默认不要求在每个 Gate 后输出验证证据。
- 仅当某个 Gate 遇到问题导致无法继续时，输出该 Gate 的问题报告（问题、影响、处理建议）。
- 失败时优先修复并重测，不得跳过当前 Gate 直接前进。

### 失败处理

- Gate 失败 → 停止前进 → 立即将本轮失败表现、初步根因与修复计划写入项目根目录 `failure-log.md` → 修复当前 Gate 所属问题 → 重新执行当前 Gate。
- 因用户反馈触发重试、返工或“再改一版”时，继续执行前必须先把上一轮问题写入项目根目录 `failure-log.md`，再开始下一轮生成或调整。
- 若 Gate 9 在第 3 轮后仍有未修复项，继续进入 Gate 10 完成交付，并附未修复问题清单。

## Gate 流程（不可跳过）

### Gate 0：初始化并读取 Failure Log（必做）

- 先检查项目根目录是否存在 `failure-log.md`
- 若不存在，则立即在项目根目录创建 `failure-log.md`，可参考 `references/failure-log.md` 模板初始化
- 读取项目根目录 `failure-log.md`
- 检索与当前任务最相似的失败记录（页面类型、组件组合、交互、图标、本地化、背景色、状态栏等）
- 提炼出本次任务的"高风险错误清单"，在后续 Gate 中优先规避
- 若日志为空，则继续执行，但后续一旦出现失败、返工或重试，必须在发生后立即补记

通过条件：

- 项目根目录 `failure-log.md` 已存在
- 已读取项目根目录 `failure-log.md`
- 已提炼与当前任务相关的失败模式或确认暂无历史记录

### Gate 1：远程读取入口指南（必做）

- 通过 `web_fetch` 远程读取 `README.md`（完整内容）
- URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/README.md`
- 理解设计系统全局结构、设备基准、组件列表、背景色约束、检查清单
- **禁止克隆或下载仓库到本地**

通过条件：

- 已成功远程读取 `README.md` 完整内容
- 已理解 20 个母组件列表、背景色规则、文件读取顺序

### Gate 2：锁定目标与组件候选

- 明确页面类型、信息层级、关键交互
- 从 20 个母组件中选择候选
- 标记是否包含 `Grouped List` 或 `Card`
- 确定需要远程读取哪些组件的 SPEC 文档

通过条件：

- 组件候选列表完整
- 背景色触发条件已明确
- 待读取的 SPEC 文件清单已列出

### Gate 3：远程读取组件硬约束

- 根据 Gate 2 确定的候选组件，远程读取对应 `md/<COMPONENT>_SPEC.md`
  - URL 格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/md/<COMPONENT>_SPEC.md`
- 重点阅读"属性约束"章节
- **若 SPEC 中描述了组件自身的交互行为（如点击展开/收起、滑动、切换、长按等），在生成界面时必须按规范描述 100% 实现，不得省略或简化**
- 对 `List / Grouped List / NavBar / 模态` 执行组合合法性检查
- 不合法组合必须替换为合法变体
- 按需远程读取对应 `json/components/<component>.json` 获取结构化数据
  - URL 格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/json/components/<component>.json`

通过条件：

- 所有已选组件均完成远程 SPEC 读取
- 组合合法性检查结论完整
- 已标记所有需要实现交互行为的组件及其交互描述

### Gate 4：远程读取并应用 Token 与主题

- 远程读取 `css/QQ_color_tokens.css`
  - URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/css/QQ_color_tokens.css`
- 远程读取 `css/tokens.css`
  - URL：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/css/tokens.css`
- 在 `<html>` 设置 `data-theme="qq-light"` 或 `data-theme="qq-dark"`
- 颜色仅使用 `QQ_color_tokens.css` 中定义的值
- 非颜色 Token 使用 `tokens.css` 中定义的值
- 间距全部为 4px 整数倍

通过条件：

- 不存在自定义颜色值
- 不存在非 4px 网格间距

### Gate 5：背景色强约束

- 包含 `Grouped List` 或 `Card`：背景强制 `bg_bottom_standard`（`#F0F0F2`）
- 不包含上述组件：默认 `bg_bottom_light`（`#FFFFFF`）
- 品牌页可使用 `bg_bottom_brand`（`#EFF4FF`）
- 冲突时灰底优先

通过条件：

- 背景色选择与触发规则一致

### Gate 6：状态栏与导航一致性

- 顶部必须放置 iOS StatusBar（428×54）
- 时间固定 `9:41`
- 状态栏图标必须下载到本地 `assets/icons/` 目录：
  - 远程源：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/network.svg`
  - 远程源：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/wifi.svg`
  - 远程源：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/battery.svg`
  - 下载后 HTML 中引用本地路径：`assets/icons/network.svg`、`assets/icons/wifi.svg`、`assets/icons/battery.svg`
- 状态栏背景与紧随其后的 NavBar 背景一致

通过条件：

- 状态栏规格完整且与 NavBar 一致
- 状态栏图标已下载到本地且 HTML 使用本地路径引用

### Gate 7：图标下载与本地化（核心变更）

本 Gate 负责将所有占位图标替换为真实图标，并**下载到本地确保离线可用**。

执行步骤：

1. **盘点图标需求**：列出页面中所有需要图标的位置及对应图标名称
2. **匹配图标库**：
   - 远程浏览图标目录：`https://github.com/qkj91927/QQ_GenUI/tree/main/icons/QUI_24_icons`
   - 优先从 `icons/QUI_24_icons/` 匹配，其次从 `icons/` 根目录匹配
   - 禁止自绘图标，禁止使用 emoji
3. **下载图标到本地**：
   - 在生成页面的同级目录创建 `assets/icons/` 目录
   - 通过 `web_fetch` 获取每个 SVG 图标内容
     - URL 格式：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/QUI_24_icons/<icon-name>.svg`
     - 或：`https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/<icon-name>.svg`
   - 使用 `write_to_file` 将 SVG 内容写入 `assets/icons/<icon-name>.svg`
4. **更新 HTML 引用路径**：
   - 所有 `<img>` 标签的 `src` 属性使用本地相对路径：`assets/icons/<icon-name>.svg`
   - **禁止使用远程 URL 作为最终图标路径**
5. **若找不到匹配图标**：输出问题报告（缺失图标需求、影响位置、临时处理建议）

通过条件：

- 占位图标残留数量为 0
- 所有图标已下载到本地 `assets/icons/` 目录
- HTML 中所有图标路径均为本地相对路径 `assets/icons/*.svg`
- 图标来源均为项目 `icons/` 图标库且无自绘/emoji
- 无匹配图标时已输出问题报告

### Gate 8：初次产出

- 完成页面生成与必要实现
- 完成内部规则检查并记录结果

通过条件：

- 页面生成完成且可进入回归流程

### Gate 9：严格规范回归（逐项核对，强制）

对"已生成结果"执行**严格规范回归测试**，必须将 QQ_GenUI 的每条细粒度约束逐项重新对照，不得仅做粗粒度抽检。按以下循环执行，最多 3 轮：

#### 9.1 逐项核对清单（每轮必须全部过一遍）

**A. 组件细则核对**

对页面中使用的每个组件，重新打开其 `md/<COMPONENT>_SPEC.md`，逐条比对：

- [ ] 组件变体（variant）是否使用了 SPEC 中定义的合法值？是否存在未定义变体？
- [ ] 组件属性（props）的取值是否在 SPEC 允许范围内？（如 size、type、status 等枚举值）
- [ ] 组件的子元素数量、类型是否符合 SPEC 中的 children 约束？
- [ ] 组件之间的嵌套/组合是否在 SPEC 允许的组合列表中？禁止的组合是否已排除？
- [ ] SPEC 中标注为"必选"的属性/插槽是否均已提供？
- [ ] SPEC 中标注为"禁止"的用法是否均已避免？
- [ ] 组件交互行为（点击、展开/收起、滑动、切换、长按等）是否按 SPEC 描述 100% 实现？

**B. 结构语义核对**

- [ ] HTML 结构层级是否与 `json/components/<component>.json` 中定义的节点树一致？
- [ ] 各组件在页面中的层级关系（父子/兄弟）是否符合规范的组合规则？
- [ ] 列表类组件（List / Grouped List）的分组、行数、分割线规则是否符合 SPEC？
- [ ] 末行是否已隐藏底部分割线？
- [ ] 模态类组件（Dialog / ActionSheet / HalfScreenOverlay）是否避免了互相嵌套？
- [ ] NavBar 的按钮数量、位置、类型是否与 SPEC 一致？

**C. 版式细节核对**

- [ ] 所有颜色值是否均来自 `QQ_color_tokens.css`？是否存在硬编码颜色？
- [ ] 所有间距（margin / padding / gap）是否为 4px 整数倍？
- [ ] 字号、字重、行高是否使用 `tokens.css` 中定义的 Token？
- [ ] 圆角值是否使用 Token 或 SPEC 中指定的值？
- [ ] 背景色是否符合 Gate 5 的强约束规则？
- [ ] 状态栏尺寸（428×54）、时间（9:41）、图标是否完整？
- [ ] 状态栏背景色是否与 NavBar 背景色一致？

**D. 图标本地化核对**

- [ ] 所有图标是否已下载到 `assets/icons/` 目录？
- [ ] HTML 中是否还存在远程 URL 引用图标的情况？
- [ ] 是否残留 `empty_icon.svg` 占位图标？
- [ ] 是否存在自绘图标或 emoji 替代？

**E. 交互行为核对**

- [ ] 每个组件的 SPEC 中描述的交互行为是否均已在代码中实现？
- [ ] 交互效果（动画、过渡、状态切换）是否与 SPEC 描述一致？
- [ ] 可交互元素是否具有正确的触摸区域和反馈样式？

#### 9.2 执行流程

每轮回归按以下步骤执行：

1. **逐项核对**：按上述 A/B/C/D/E 五个维度，对照 SPEC 原文逐条检查
2. **统计不符合项**：按维度分类记录（组件细则 / 结构语义 / 版式细节 / 图标本地化 / 交互行为）
3. **逐项修复**：修复全部不符合项
4. **重新执行核对**：修复后重新走一遍核对清单

#### 9.3 停止条件

- 任一轮核对结果达到 **100% 合规（所有检查项均通过）**，立即结束并进入 Gate 10
- 轮次达到 3 且仍有不符合项，结束回归并进入 Gate 10，交付结果并附未修复问题清单

#### 9.4 硬约束

- 回归轮次最少 1 次，最多 3 次
- 中间轮次静默执行：发现问题直接修复，无需向用户输出详细核对结果
- **仅在最后一轮输出核对摘要**（维度 → 不通过项 → 问题描述），已通过的检查项无需逐条列出
- 禁止跳过任何检查项
- 禁止仅做粗粒度抽检（如"Token 大致正确"），必须逐条比对
- 第 3 轮后若仍不合规，列出未修复项及影响范围

### Gate 10：最终交付与 Failure Log 回填

Gate 10 在以下两种情况下均可执行：

- Gate 9 已达到 100% 合规
- Gate 9 已执行满 3 轮但仍有剩余问题

执行动作：

- 汇总本次任务过程中已写入项目根目录 `failure-log.md` 的条目，并补全最终解决方式、预防规则、关联组件/规范
- 若本次任务出现新的失败、偏差、返工、重试，或用户需要反复指出问题并调整，必须确保对应记录已在发生后写入项目根目录 `failure-log.md`
- 若本次一次性成功且无明显失败模式，可不新增日志

最终回复必须包含：

- Gate 执行摘要（Gate0~Gate10 通过情况）
- 回归轮次摘要（轮次与每轮问题数变化）
- 若未达100%：未修复问题清单（问题、影响、建议）
- 审查与完善建议（缺失组件/缺失变体/不合理之处/主流设计系统对比）

## 输出格式约定

按以下结构组织最终回复：

1. Gate 执行状态摘要（逐 Gate：通过/失败）
2. 严格规范回归记录（最多 3 轮，最后一轮仅输出摘要）
3. 未修复问题清单（仅未达100%时）
4. 审查与完善建议：- 完成设计任务后，审视最终方案，以清单形式附在回复末尾，涵盖以下维度：
  - **缺失组件**：当前 20 个母组件无法覆盖的设计需求（如需要但不存在的组件类型）
  - **缺失变体**：现有组件的变体不足以满足场景（如缺少某种尺寸、状态或布局）
  - **不合理之处**：组件规范与实际设计需求之间的冲突或不适配
- 无问题的维度注明"无缺失"


## 禁止项

- 禁止 `git clone`、`git pull` 或克隆整个仓库到用户本地
- 禁止在最终交付的 HTML 中使用远程 URL 引用图标（图标必须本地化到 `assets/icons/`）
- 禁止跳过任何 Gate
- 禁止 Gate 未通过时进入下一 Gate
- 禁止跳过 `md/*_SPEC.md` 直接拼组件
- 禁止使用未定义颜色值
- 禁止在列表末行显示底部分割线
- 禁止模态组件互相嵌套
- 禁止保留 `empty_icon.svg` 作为最终图标
- 禁止跳过 Gate 9 回归测试直接交付
- 禁止 Gate 9 仅做粗粒度抽检，必须逐条核对 SPEC 约束
- 禁止在回归未达 100% 且未输出未修复问题清单时宣称完成

## 参考资料

- `references/component-index.md`：20 个母组件速查与文件映射
- `references/checklist.md`：Gate + 回归执行清单（可直接逐项执行）
