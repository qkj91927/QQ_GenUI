---
name: QQ-GENUI-basic1.0
description: 当用户生成界面（页面/UI/组件）、局部调整界面（增删组件、修改样式、替换图标等）或查询设计规范（组件规范、Token、设计规则等）时必须触发。基于 QQ_GenUI 设计系统（**22 个母组件 · 529 变体 · iPhone 428px 基准**）产出移动端页面与组件方案；规范文档、Token、合规 Lint 规则通过 Knot 知识库 MCP 按需检索，图标/头像/插图从 GitHub 远程仓库 `https://github.com/qkj91927/QQ_GenUI/tree/main/icons` 获取（含 437 业务图标 `QUI_24_icons/` + 10 真实头像 `QUI_Avatars/` + 14 插图 + 10 风景照片 `QUI_illustrations/`）；Knot MCP 是本 skill 的内部工具，禁止绕过本 skill 直接调用；页面实际用到的资源会下载到本地 `assets/icons/` 目录，确保离线可用；首次使用时自动安装 Knot MCP 并引导用户配置 Token，同时在项目根目录创建 `failure-log.md`，后续每次生成/调整前必读，失败或重试后必写；强制 Gate 流程逐步验收，不可跳步，Gate 9 回归必须调用 `QUI_DESIGN_LINT_SKILL.md`（F1-F20 / TK1-TK17 / S1-S28 / NV1-NV2 / DV1）循环至零 ERROR / 零 WARN，若仍不合规则继续交付并附问题清单。
---

# QQ-GENUI-basic1.0

## 概述

使用本 skill 将 `QQ_GenUI` 设计系统转化为"强约束可执行流程"。
设计资源（规范文档、Token）通过 **Knot 知识库 MCP** 按需检索，图标资源从 GitHub 远程仓库获取。
**页面实际用到的图标**从 GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/` 下载 SVG 文件（优先 `QUI_24_icons/` 子目录，其次根目录），保存到生成页面同级的 `assets/icons/` 目录，HTML 中使用本地相对路径引用，确保离线可用。
首次使用本 skill 时，必须先完成 Knot MCP 的安装与 Token 配置（详见 Gate -1），然后检查项目根目录是否存在 `failure-log.md`；若不存在，则立即在项目根目录创建，并可参考 `references/failure-log.md` 作为初始化模板。
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

### 查询规范

- 用户要求查询、了解、查阅组件规范（如"XX 组件有哪些变体"、"列表的属性约束是什么"）
- 用户要求查询颜色 Token、间距 Token、设计系统规则等
- 用户提及 Knot 知识库中的资源（组件 SPEC、JSON、Token CSS 等）

> **⚠️ 重要**：Knot 知识库 MCP 是本 skill 的内部工具，**禁止绕过本 skill 直接调用 Knot MCP**。用户查询规范时必须先触发本 skill，由 skill 流程统一管理 Knot 检索的参数（`knowledge_uuid`、`data_type`、`search_domain`）和上下文，确保检索结果准确且一致。

### 触发判定规则

> **核心原则：凡涉及界面生成、界面修改或设计规范查询，均必须触发本 skill。**
>
> 即使用户未明确提及"设计系统"或"QQ_GenUI"，只要请求的产出物是 UI 界面（HTML/页面/组件），或请求查询的是本设计系统的组件规范/Token/设计规则，就必须走本 skill 的流程，以确保输出符合设计系统规范。

在以下场景**不**触发：

- 纯后端任务（API、数据库、服务端逻辑等）
- 与界面无关的通用前端问题（打包配置、性能优化、纯 JS 逻辑等）
- 纯文档编写、纯数据处理

## Knot 知识库 MCP 配置

### MCP 服务配置

配置文件路径：`~/.codebuddy/mcp.json`（即 `/Users/<用户名>/.codebuddy/mcp.json`）

需要在该文件的 `mcpServers` 中包含以下 `knot` 配置：

```json
{
  "mcpServers": {
    "knot": {
      "url": "http://mcp.knot.woa.com/open/mcp",
      "headers": {
        "x-knot-knowledge-uuids": "7eafcbe5fe1b44cf8cf17a3ee195a30c",
        "x-knot-api-token": "<TOKEN>"
      }
    }
  }
}
```

### 知识库参数

| 参数 | 值 |
|------|------|
| knowledge_uuid | `7eafcbe5fe1b44cf8cf17a3ee195a30c` |
| data_type（源码检索） | `git` |
| search_domain（源码检索） | `QQdesign_Foundation@DesignSystem-basic` |
| data_type（架构总结检索） | `git_iwiki` |
| search_domain（架构总结检索） | `QQdesign_Foundation@DesignSystem-basic-git_iwiki` |

### 检索规则

- 使用 `knowledgebase_search` MCP 工具检索知识库中的组件规范、Token、图标等资源
- **按需检索**：仅在当前 Gate 需要时才发起检索，不要一次性检索全部资源
- 检索时务必指定 `knowledge_uuid`、合适的 `data_type` 和 `search_domain` 以提升准确度
- 检索组件 SPEC 时：`query` 填写组件名称或描述，`keyword` 填写 `SPEC;组件名`，`data_type` 填 `git`，`search_domain` 填 `QQdesign_Foundation@DesignSystem-basic`
- 检索 Token / CSS 时：`query` 填写 Token 用途描述，`keyword` 填写 `token;css;color`
- **图标不通过 Knot 检索**：图标资源从 GitHub 远程仓库获取，基础 URL 为 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/`（优先 `QUI_24_icons/` 子目录，其次根目录），使用 `web_fetch` 下载 SVG 内容后写入本地
- 检索架构概览时：`data_type` 填 `git_iwiki`，`search_domain` 填 `QQdesign_Foundation@DesignSystem-basic-git_iwiki`
- 若检索失败或无结果，在当前 Gate 输出问题报告并暂停

### 图标本地化规则（重要）

页面实际用到的图标**必须下载到生成页面同级的 `assets/icons/` 目录**，确保离线可用：

- **图标远程源**：GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/`（优先从 `QUI_24_icons/` 子目录匹配，其次从根目录匹配）
  - 浏览图标目录列表：`https://github.com/qkj91927/QQ_GenUI/tree/main/icons` 和 `https://github.com/qkj91927/QQ_GenUI/tree/main/icons/QUI_24_icons`
- **输出目录**：在生成页面的同级目录下创建 `assets/icons/` 目录
- **下载时机**：Gate 7（图标替换）阶段，确定页面所需图标后立即下载
- **获取方式**：使用 `web_fetch` 从 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/<path>/<icon-name>.svg` 获取 SVG 内容，然后用 `write_to_file` 写入 `assets/icons/<icon-name>.svg`
- **HTML 引用路径**：页面中所有图标统一使用本地相对路径 `assets/icons/<icon-name>.svg`，**禁止在最终交付的 HTML 中使用远程 URL**
- **仅下载所需图标**：不要下载整个图标库，只下载当前页面实际引用的图标文件
- **状态栏图标同理**：`network.svg`、`wifi.svg`、`battery.svg` 等从 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/` 下载后保存到 `assets/icons/`

## 强制执行契约（GATE）

### 总则

- 从 Gate -1 开始顺序执行，必须 `-1 → 0 → 1 → 2 → 3 → ...`。
- 每个 Gate 必须满足通过条件后才能进入下一 Gate。
- 默认不要求在每个 Gate 后输出验证证据。
- 仅当某个 Gate 遇到问题导致无法继续时，输出该 Gate 的问题报告（问题、影响、处理建议）。
- 失败时优先修复并重测，不得跳过当前 Gate 直接前进。

### 失败处理

- Gate 失败 → 停止前进 → 立即将本轮失败表现、初步根因与修复计划写入项目根目录 `failure-log.md` → 修复当前 Gate 所属问题 → 重新执行当前 Gate。
- 因用户反馈触发重试、返工或"再改一版"时，继续执行前必须先把上一轮问题写入项目根目录 `failure-log.md`，再开始下一轮生成或调整。
- 若 Gate 9 在第 3 轮后仍有未修复项，继续进入 Gate 10 完成交付，并附未修复问题清单。

## Gate 流程（不可跳过）

### Gate -1：Knot MCP 安装与 Token 配置（首次必做）

本 Gate 仅在**首次使用本 skill 时**执行，后续若 MCP 已配置则自动跳过。

执行步骤：

1. **检查 MCP 配置**：读取用户的 MCP 配置文件 `~/.codebuddy/mcp.json`（即 `/Users/<用户名>/.codebuddy/mcp.json`），检查其中是否已包含 `knot` MCP 服务配置
2. **若未安装**，自动将以下配置写入（或合并到）`~/.codebuddy/mcp.json`：
   ```json
   {
     "mcpServers": {
       "knot": {
         "url": "http://mcp.knot.woa.com/open/mcp",
         "headers": {
           "x-knot-knowledge-uuids": "7eafcbe5fe1b44cf8cf17a3ee195a30c",
           "x-knot-api-token": "<TOKEN>"
         }
       }
     }
   }
   ```
   > 注意：若 `mcp.json` 已存在且包含其他 MCP 服务配置，需将 `knot` 配置合并到现有 `mcpServers` 中，不可覆盖已有配置。若文件不存在，则直接创建。
3. **引导用户获取 Token**：向用户发送以下提示信息：
   > 首次使用需要配置 Knot 知识库访问凭证。请前往 https://knot.woa.com/settings/token 获取你的个人调用 Token，然后将 Token 发送给我，我会自动完成配置。
4. **等待用户提供 Token**：用户发送 Token 后，自动将其填入 MCP 配置的 `x-knot-api-token` 字段
5. **验证连通性**：使用 `knowledgebase_search` 发起一次简单检索（如查询 `README`），确认 MCP 连接正常

通过条件：

- Knot MCP 服务已安装且配置完整
- `x-knot-api-token` 已填入用户提供的有效 Token
- 验证检索成功，MCP 连接正常

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

### Gate 1：通过 Knot 检索入口指南（必做）

- 通过 `knowledgebase_search` 检索 `README.md` 内容
  - `query`: "QQ_GenUI 设计系统入口指南 README 全局结构 组件列表 背景色约束"
  - `keyword`: "README;设计系统;组件列表;背景色"
  - `knowledge_uuid`: `7eafcbe5fe1b44cf8cf17a3ee195a30c`
  - `data_type`: `git`
  - `search_domain`: `QQdesign_Foundation@DesignSystem-basic`
- 理解设计系统全局结构、设备基准、**22 个母组件**列表、背景色约束、检查清单
- 通过 `knowledgebase_search` 检索 `QUI_DESIGN_LINT_SKILL.md` 内容（**Gate 9 回归的权威依据**）
  - `query`: "QUI Design Lint 合规自检 两级违规制 Preflight F1 TK1 S1 NV1 DV1"
  - `keyword`: "QUI_DESIGN_LINT_SKILL;lint;合规;Preflight"
  - 重点掌握：两级违规制（⛔ ERROR / ⚠️ WARN）、F1-F20 禁止行为、TK1-TK17 Token 绑定、S1-S28 结构规则、NV1-NV2 NavBar 拼接、DV1 分割线
- **禁止克隆或下载仓库到本地**

通过条件：

- 已成功通过 Knot 检索到 `README.md` 相关内容
- 已理解 22 个母组件列表、背景色规则、文件读取顺序
- 已通过 Knot 检索到 `QUI_DESIGN_LINT_SKILL.md` 内容（Gate 9 回归依据）

### Gate 2：锁定目标与组件候选

- 明确页面类型、信息层级、关键交互
- 从 22 个母组件中选择候选（导航 2 · 数据 9 · 操作 7 · 模态 3 · 运营 1）
- 标记是否包含 `Grouped List` / `Card` / `Message` / `AIO`（触发灰底 `--bg-secondary`）
- 标记是否包含需要真实头像的组件（`List` / `Card` / `Message` / `NavBar L6`）→ 后续 Gate 7 必须用 `QUI_Avatars/AvatarN.svg` 替换占位
- 标记是否包含需要真实图片的组件（`Card 富媒体` / `ImageBlock` / `HSO 新手引导` / `Grid 四宫格/九宫格`）→ 后续 Gate 7 必须用 `QUI_illustrations/` 素材替换 placeholder
- 确定需要通过 Knot 检索哪些组件的 SPEC 文档

通过条件：

- 组件候选列表完整
- 背景色触发条件已明确
- 待检索的 SPEC 文件清单已列出

### Gate 3：通过 Knot 检索组件硬约束

- 根据 Gate 2 确定的候选组件，通过 Knot 检索对应组件 SPEC
  - `query`: "<组件名> 组件规范 属性约束 变体 交互行为"
  - `keyword`: "<COMPONENT>_SPEC;组件名;属性;变体"
  - `knowledge_uuid`: `7eafcbe5fe1b44cf8cf17a3ee195a30c`
  - `data_type`: `git`
  - `search_domain`: `QQdesign_Foundation@DesignSystem-basic`
- 重点阅读"属性约束"章节
- **若 SPEC 中描述了组件自身的交互行为（如点击展开/收起、滑动、切换、长按等），在生成界面时必须按规范描述 100% 实现，不得省略或简化**
- 对 `List / Grouped List / NavBar / 模态` 执行组合合法性检查
- 不合法组合必须替换为合法变体
- 按需通过 Knot 检索对应组件 JSON 结构化数据
  - `keyword`: "<component>.json;组件结构"
- **⚠️ 涉及半屏浮层（HalfScreenOverlay）时必须先检索模版库**：
  - 通过 Knot 检索 `HALF_SCREEN_OVERLAY_TEMPLATES.md` 内容
    - `query`: "半屏浮层 模版 HalfScreen 场景匹配 T-01 T-02 T-03 T-04 T-05 T-06"
    - `keyword`: "HALF_SCREEN_OVERLAY_TEMPLATES;模版;半屏浮层"
  - 按核心特征从 T-01~T-06 六档模版中判定最匹配的模版，依据模版结构生成，避免从零搭建导致的结构错误

通过条件：

- 所有已选组件均完成 Knot SPEC 检索
- 组合合法性检查结论完整
- 已标记所有需要实现交互行为的组件及其交互描述
- 涉及半屏浮层时已完成模版库检索与匹配

### Gate 4：通过 Knot 检索并应用 Token 与主题

- 通过 Knot 检索 `Qdesign Color Tokens.css` 内容（颜色 Token）
  - `query`: "Qdesign 颜色 Token 定义 color tokens CSS QBasicToken"
  - `keyword`: "Qdesign Color Tokens.css;颜色;token;QBasicToken"
- 通过 Knot 检索 `Qdesign Tokens.css` 内容（非颜色 Token：设备/字体/间距/圆角/阴影/动效）
  - `query`: "Qdesign 通用 Token 间距 字号 圆角 CSS"
  - `keyword`: "Qdesign Tokens.css;间距;字号;圆角"
- 按需通过 Knot 检索 `Qdesign-tokens映射表.csv`（Figma 旧名 → CSS 标准名映射，遇到旧命名时查阅）
  - `keyword`: "Qdesign-tokens映射表;token映射;旧名;新名"
- 通过 Knot 检索 `DIVIDER_SPACING_COMPONENT_SPEC.md` 内容（布局间距规范）
  - `query`: "分隔与间距 组件间距 布局间距 Divider Spacing 间距档位"
  - `keyword`: "DIVIDER_SPACING_COMPONENT_SPEC;divider-spacing;间距;布局"
  - 重点理解：6 档间距值（4/8/12/16/24/32px）、组件间间距选择规则、分割线使用场景
  - **此规范是页面中组件之间正确分隔的唯一依据，未读取将导致组件间距错误**
- 在 `<html>` 设置 `data-theme="qq-light"` 或 `data-theme="qq-dark"`
- 颜色 Token 共 **39 个 QBasicToken**，命名格式 `--token-名`（**连字符分隔**，如 `--bg-secondary`、`--text-primary`、`--bg-bottom`、`--bg-bottom-brand`）
- **⚠️ 旧命名已废弃**：
  - `--color-xxx` / `--qq-xxx` 等 151 个旧 token（v1.0.5 前）已移除
  - **下划线命名（如 `--brand_standard`、`--text_primary`）也已重构为连字符命名**，禁止使用
- 颜色仅使用 `Qdesign Color Tokens.css` 中定义的 QBasicToken 值（连字符命名）
- 非颜色 Token 使用 `Qdesign Tokens.css` 中定义的值
- 组件间间距使用 `DIVIDER_SPACING_COMPONENT_SPEC.md` 中定义的间距档位和选择规则
- 间距全部为 4px 整数倍

通过条件：

- 不存在自定义颜色值
- 不存在旧命名 Token（`--color-xxx` / `--qq-xxx` / 下划线命名如 `--brand_standard`）
- 颜色 Token 均为连字符命名（`--xxx-yyy`）
- 不存在非 4px 网格间距
- 组件间间距选择符合 DIVIDER_SPACING_COMPONENT_SPEC 规则

### Gate 5：背景色强约束

根据页面包含的组件类型，背景色**强制确定**（对应 lint **S5**）：

| 背景色 | Token | 色值 | 触发条件 |
|--------|-------|------|----------|
| 浅灰色 | `--bg-secondary` | `#F0F0F2` | 页面包含 **Card / Grouped List / Message / AIO** 任一时必须使用 |
| 白色 | `--bg-bottom` | `#FFFFFF` | 默认背景色（仅当页面不含上述四种组件时） |
| 品牌浅蓝 | `--bg-bottom-brand` | `#EFF4FF` | 品牌定制页面，按业务需要使用 |

- 冲突时灰底优先（`--bg-secondary` 优先于 `--bg-bottom`）
- **NavBar 底色拼接规则**：与页面底色的合法组合矩阵见 lint **NV1**
- **Search 配色反相**：白页用灰底 Search / 非白页用白底 Search

通过条件：

- 背景色选择与触发规则一致（过 lint S5）
- NavBar 与页面底色组合符合 NV1 矩阵
- 使用新 Token 命名（连字符分隔），禁止使用旧命名 `bg_bottom_standard` / `bg_bottom_light` 等

### Gate 6：状态栏与导航一致性

- 顶部必须放置 iOS StatusBar（428×54）
- 时间固定 `9:41`
- 状态栏图标从 GitHub 远程仓库下载到 `assets/icons/`：
  - 下载 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/network.svg` → 写入 `assets/icons/network.svg`
  - 下载 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/wifi.svg` → 写入 `assets/icons/wifi.svg`
  - 下载 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/battery.svg` → 写入 `assets/icons/battery.svg`
  - HTML 中引用本地路径 `assets/icons/*.svg`
- 状态栏背景与紧随其后的 NavBar 背景一致

通过条件：

- 状态栏规格完整且与 NavBar 一致
- 状态栏图标已下载到本地且 HTML 使用本地路径引用

### Gate 7：图标 / 头像 / 插图匹配与本地化

本 Gate 负责将所有占位图标、头像、插图替换为真实资源，并**下载到本地确保离线可用**。

**资源来源**（GitHub 远程仓库）：

| 资源类型 | 远程路径 | 本地目标 | 关联 lint |
|---------|---------|---------|----------|
| 通用图标（结构/功能） | `icons/*.svg`（33 枚） | `assets/icons/` | F11-F15 |
| 业务图标 | `icons/QUI_24_icons/*.svg`（437 枚，24×24） | `assets/icons/` | F11-F15 |
| 真实头像 | `icons/QUI_Avatars/Avatar1..Avatar10.svg`（10 张 52×52） | `assets/icons/QUI_Avatars/` | **F19** |
| 插图 | `icons/QUI_illustrations/illustration1..14.png` | `assets/icons/QUI_illustrations/` | **F20** |
| 风景照片 | `icons/QUI_illustrations/landscape photos1..10.JPG`（引用 URL 编码 `%20`） | `assets/icons/QUI_illustrations/` | **F20** |

执行步骤：

1. **盘点资源需求**：列出页面中所有需要图标/头像/图片的位置及对应文件
2. **从 GitHub 远程仓库匹配**：
   - 图标：优先 `icons/QUI_24_icons/`，其次 `icons/`
   - 头像：含头像的组件（`List` / `Card` / `Message` / `NavBar L6` 等）**必须**用 `QUI_Avatars/AvatarN.svg` 替换 `Avatar_32/40/52.svg` 占位；允许等比缩放至 32/40/52；同页多个头像须用不同编号；保持 `border-radius: 50%`
   - 插图/图片：含图片的组件（`Card 富媒体` / `ImageBlock` / `HSO 新手引导` / `运营 banner` / `Grid 宫格`）**必须**用 `QUI_illustrations/` 真实素材替换 `placeholder_landscape/portrait/square.svg` 占位
     - Convention（非 MUST）：Card / HSO 新手引导 / 运营 banner → 插图（`illustrationN.png`）；四宫格 / 九宫格 → 照片（`landscape photosN.JPG`）；可混用
   - 禁止自绘图标、emoji、外部图标库（F11/F12/F13）
3. **下载资源到本地**：
   - 使用 `web_fetch` 从 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/<path>/<file>` 获取内容
   - 使用 `write_to_file` 写入 `assets/icons/<path>/<file>`
   - **照片文件名含空格**，URL 必须编码为 `%20`（如 `landscape%20photos3.JPG`）
4. **更新 HTML 引用路径**：
   - 所有资源统一使用本地相对路径：`assets/icons/...`
   - **禁止在最终交付的 HTML 中使用远程 URL**
5. **若找不到匹配资源**：输出问题报告（缺失项、影响位置、临时处理建议）

通过条件：

- `empty_icon.svg` / `placeholder_*.svg` / `Avatar_32/40/52.svg` 占位残留数量为 0
- 所有资源已下载到本地 `assets/icons/` 目录
- HTML 中所有资源路径均为本地相对路径
- 资源来源均为 GitHub 仓库 `icons/` 目录且无自绘/emoji/外部库
- 含头像组件已使用 `QUI_Avatars/AvatarN.svg`（过 lint F19）
- 含图片组件已使用 `QUI_illustrations/` 真实素材（过 lint F20）
- 无匹配资源时已输出问题报告

### Gate 8：初次产出

- 完成页面生成与必要实现
- 完成内部规则检查并记录结果

通过条件：

- 页面生成完成且可进入回归流程

### Gate 9：严格规范回归（QUI Design Lint 全量核查，强制）

对"已生成结果"调用 **`QUI_DESIGN_LINT_SKILL.md`**（Gate 1 已通过 Knot 检索获取）的五步流程进行**零容忍合规自检**，循环修复直至**零 ⛔ ERROR、零 ⚠️ WARN**（最多 3 轮）。

#### 9.0 权威依据

- 本 Gate 的所有检查项**一律以 `QUI_DESIGN_LINT_SKILL.md` 为准**，不再在本 skill 内重复罗列
- 两级违规制：
  - **⛔ ERROR**：值本身非法（如 `font-size: 15px` 不在 11 档合法字号中）
  - **⚠️ WARN**：值碰巧正确但未通过 Token 变量引用（如 `border-radius: 12px` 应写 `var（--radius-m）`）
- 元标记优先级：`@MUST` / `@FORBIDDEN` > 自然语言"必须/应该"描述

#### 9.1 五步执行流程

**第〇步 · Preflight（基线声明）**

清点并声明本次检查的代码覆盖面：涉及组件（N 个）、涉及图标（M 个含 src + 着色 Token）、涉及 Token（K 个）、页面结构（StatusBar / NavBar / HomeBar / 背景色 / 主题）、交互状态（hover / pressed / disabled / loading）、容器宽度（428 通栏 / 396 嵌入）、已扫描关联 spec 的 `@MUST` / `@FORBIDDEN` / `@LINT` / `@SPEC_OF_TRUTH`。

> ⚠️ 跳过 Preflight 直接开检，评级上限 C

**第一步 · 组件合法性验证**

对每个 UI 元素执行 4 步：识别 → 匹配变体 → 容器宽度 → 比对 UI。覆盖 F1 非法组件 / F2 魔改结构 / F3 跨组件嫁接 / F4 自创变体 / F5 修改固定值 / F9 缺少 StatusBar / F10 模态嵌套 / F18 不支持加载态的组件强加 loading。

**第 1.5 步 · 图标使用验证（专项）**

F11 自绘 / F12 Emoji / F13 外部库 / F14 硬编码尺寸 / F15 Base64 外链 / F16 SVG 内部硬编码颜色 / F17 非 Button 场景 filter hack / **F19 未替换 `QUI_Avatars/AvatarN.svg` 真实头像** / **F20 未替换 `QUI_illustrations/` 真实图片**。图标着色走 5 个 `--icon-*` Token。

**第二步 · Token 与样式检查（两级违规）**

TK1-TK17 全量：颜色 / 间距 / 圆角 / 字号 / 字重 / 行高 / 阴影 / 动效 / z-index / object-fit / border。F6 硬编码颜色 / F7 非法字号 / F8 非法间距。所有合法值必须通过 `var（--token-name）` 引用，否则降级为 ⚠️ WARN。

**第三步 · 页面结构与约束检查**

S1-S28 全量：StatusBar / HomeBar / 唯一性 / 固定位置 / 容量上限 / 标准宽度（通栏 428 / 嵌入 396）/ 吸顶吸底层级 / 禁止界面级滚动条。重点：**S5 背景色**（Card / Grouped List / Message / AIO 四组件触发 `--bg-secondary`）、**S21 StatusBar 与 NavBar 底色拼接**、**S24-S28 模态层级序**、**NV1 NavBar 底色拼接矩阵** / **NV2 滚动态分割线** / **DV1 分割线**、嵌套允许矩阵（11 种容器）。

**第四步 · 合规评分**

按 Lint Skill 评级标准输出报告（A/B/C/D/E 五级）。

#### 9.2 执行循环

1. **逐项扫描**：按第〇~四步全量核查
2. **统计违规**：按 ⛔ ERROR 和 ⚠️ WARN 分类记录
3. **逐项修复**：优先修 ERROR，再修 WARN
4. **重新扫描**：修复后重跑全流程

#### 9.3 停止条件

- 任一轮达到 **零 ⛔ ERROR / 零 ⚠️ WARN**，立即结束并进入 Gate 10
- 轮次达到 3 且仍有违规，结束回归并进入 Gate 10，附未修复问题清单

#### 9.4 硬约束

- 回归轮次最少 1 次，最多 3 次
- 中间轮次静默执行，发现违规直接修复
- **仅最后一轮**输出 lint 报告（含 Preflight、逐项违规、评分汇总）
- 禁止粗粒度抽检，必须按 lint 规则逐条比对
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

- Gate 执行摘要（Gate-1~Gate10 通过情况）
- 回归轮次摘要（轮次与每轮 ⛔ ERROR / ⚠️ WARN 数变化）
- Lint 合规评分（A/B/C/D/E 五级）
- 若未达零违规：未修复问题清单（问题、影响、建议）
- 审查与完善建议

## 输出格式约定

按以下结构组织最终回复：

1. Gate 执行状态摘要（逐 Gate：通过/失败）
2. 严格规范回归记录（最多 3 轮，最后一轮输出 QUI Design Lint 完整报告含评分）
3. 未修复问题清单（仅未达零违规时）
4. 审查与完善建议：完成设计任务后，审视最终方案，以清单形式附在回复末尾，涵盖以下维度：
  - **缺失组件**：当前 22 个母组件无法覆盖的设计需求（如需要但不存在的组件类型）
  - **缺失变体**：现有组件的变体不足以满足场景（如缺少某种尺寸、状态或布局）
  - **不合理之处**：组件规范与实际设计需求之间的冲突或不适配
- 无问题的维度注明"无缺失"

## 禁止项

- 禁止 `git clone`、`git pull` 或克隆整个仓库到用户本地
- 禁止在最终交付的 HTML 中使用远程 URL 引用图标/头像/插图（所有资源必须本地化到 `assets/icons/`）
- 禁止跳过任何 Gate（包括 Gate -1）
- 禁止 Gate 未通过时进入下一 Gate
- 禁止跳过组件 SPEC 检索直接拼组件
- 禁止使用未定义颜色值
- 禁止在列表末行显示底部分割线
- 禁止模态组件互相嵌套（F10）
- 禁止保留 `empty_icon.svg` / `Avatar_32/40/52.svg` / `placeholder_*.svg` 占位图作为最终交付
- **禁止未替换头像占位**：含头像组件（List / Card / Message / NavBar L6）必须用 `QUI_Avatars/AvatarN.svg`（F19）
- **禁止未替换图片占位**：含图片组件（Card / ImageBlock / HSO / Grid）必须用 `QUI_illustrations/` 真实素材（F20）
- 禁止自绘图标（F11）/ Emoji 当图标（F12）/ 外部图标库（F13）
- 禁止 Gate 9 跳过 QUI Design Lint 直接交付，必须按第〇~四步全量核查
- 禁止在未完成 Knot MCP Token 配置的情况下进入生成环节
- **禁止绕过本 skill 直接调用 Knot 知识库 MCP**：用户查询组件规范、Token、设计规则时，必须先触发本 skill，由 skill 统一管理检索参数和上下文，不得在未加载本 skill 的情况下直接调用 `knowledgebase_search`
- 禁止出现整个界面级的滚动条（界面尺寸必须 428×926 以内）

## 参考资料

- `references/component-index.md`：22 个母组件速查与 Knot 检索关键词映射（含 `QUI_DESIGN_LINT_SKILL` / `QUI_Avatars` / `QUI_illustrations` 检索项）
- `references/checklist.md`：Gate + 回归执行清单（Gate 9 对齐 QUI Design Lint 五步法）
