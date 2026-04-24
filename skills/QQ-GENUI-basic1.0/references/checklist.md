# Gate 执行与回归检查清单（Knot 知识库 + 图标/头像/插图本地化 + QUI Design Lint 版）

> 规则：每个 Gate 未通过不得进入下一 Gate。组件规范、Token、合规 Lint 规则通过 Knot 知识库 MCP 按需检索，图标/头像/插图从 GitHub 远程仓库获取，禁止克隆仓库。页面用到的所有资源必须下载到本地 `assets/icons/`（含 `QUI_Avatars/` 和 `QUI_illustrations/` 子目录）。颜色来源唯一为 `Qdesign Color Tokens.css`，使用连字符命名（如 `--bg-secondary`），旧命名已废弃。**Gate 9 回归一律以 `QUI_DESIGN_LINT_SKILL.md`（F1-F20 / TK1-TK17 / S1-S28 / NV1-NV2 / DV1）为权威依据**，循环至零 ⛔ ERROR / 零 ⚠️ WARN。首次使用时须完成 Knot MCP 安装与 Token 配置；若项目根目录不存在 `failure-log.md`，必须先创建；后续每次生成/调整前先读；每次失败、返工或重试后立即写入。

## Gate -1：Knot MCP 安装与 Token 配置（首次）

- [ ] 已检查当前环境是否已安装 knot MCP 服务
- [ ] 若未安装，已自动写入 MCP 配置
- [ ] 已提示用户前往 https://knot.woa.com/settings/token 获取 Token
- [ ] 用户已提供 Token，已自动填入 `x-knot-api-token`
- [ ] 已通过一次简单检索验证 MCP 连接正常

## Gate 0：初始化并读取 Failure Log

- [ ] 已检查项目根目录是否存在 `failure-log.md`
- [ ] 若不存在，已在项目根目录创建 `failure-log.md`
- [ ] 已读取项目根目录 `failure-log.md`
- [ ] 已检索与当前任务相似的历史失败记录
- [ ] 已提炼本次任务的高风险错误清单
- [ ] 若日志为空，已确认后续一旦失败、返工或重试需立即补记

## Gate 1：通过 Knot 检索入口指南

- [ ] 已通过 knowledgebase_search 检索到 `README.md` 相关内容
- [ ] 已通过 knowledgebase_search 检索到 `QUI_DESIGN_LINT_SKILL.md`（Gate 9 权威依据）
- [ ] 已理解 22 个母组件列表（导航 2 · 数据 9 · 操作 7 · 模态 3 · 运营 1）、背景色规则、文件读取顺序
- [ ] 已理解两级违规制（⛔ ERROR / ⚠️ WARN）和元标记语义（`@MUST` / `@FORBIDDEN`）
- [ ] 未执行 git clone / git pull / 任何仓库级本地下载

## Gate 2：目标与组件候选

- [ ] 已明确页面目标、信息层级、交互动作
- [ ] 已从 22 个母组件中列出候选
- [ ] 已标记是否包含 `Card / Grouped List / Message / AIO`（触发 `--bg-secondary`）
- [ ] 已标记是否包含需要真实头像的组件（F19）
- [ ] 已标记是否包含需要真实图片的组件（F20）
- [ ] 已列出待通过 Knot 检索的 SPEC 文件清单
- [ ] 已结合 Failure Log 补充本次任务的风险检查点

## Gate 3：通过 Knot 检索组件硬约束

- [ ] 已通过 Knot 检索到目标组件 SPEC 内容
- [ ] 已读取 spec 顶部 `## 🔒 强约束声明` 块
- [ ] List 组合满足 `LIST_COMPONENT_SPEC.md`
- [ ] Grouped List 组合满足 `GROUPED_LIST_COMPONENT_SPEC.md`
- [ ] NavBar 组合满足 `NAVBAR_COMPONENT_SPEC.md`
- [ ] 模态组件未嵌套（F10）
- [ ] 涉及半屏浮层时已检索 `HALF_SCREEN_OVERLAY_TEMPLATES.md` 并匹配 T-01~T-06
- [ ] 涉及 Badge 时已检索 `BADGE_COMPONENT_SPEC.md` 并明确宿主与锚点
- [ ] 已标记 SPEC 中描述的组件交互行为，生成时必须 100% 实现

## Gate 4：通过 Knot 检索 Token 与主题

- [ ] 已通过 Knot 检索到 `Qdesign Color Tokens.css` 内容
- [ ] 已通过 Knot 检索到 `Qdesign Tokens.css` 内容
- [ ] 已通过 Knot 检索到 `DIVIDER_SPACING_COMPONENT_SPEC.md` 布局间距规范
- [ ] `<html>` 已设置 `data-theme`
- [ ] 颜色全部来自 `Qdesign Color Tokens.css`，使用连字符命名（`--xxx-yyy`）
- [ ] 不存在旧命名（`--color-xxx` / `--qq-xxx` / 下划线命名如 `--brand_standard`）
- [ ] 间距均为 4px 整数倍
- [ ] 组件间间距符合 `DIVIDER_SPACING_COMPONENT_SPEC.md` 6 档规则（4/8/12/16/24/32px）

## Gate 5：背景色强约束（S5）

- [ ] 包含 `Card / Grouped List / Message / AIO` 任一时使用 `--bg-secondary`（`#F0F0F2`）
- [ ] 默认场景使用 `--bg-bottom`（`#FFFFFF`）
- [ ] 品牌页使用 `--bg-bottom-brand`（`#EFF4FF`）
- [ ] 冲突场景灰底优先
- [ ] NavBar 与页面底色组合符合 NV1 矩阵
- [ ] 使用新 Token 命名，禁止旧命名（`bg_bottom_standard` / `bg_bottom_light` 等）

## Gate 6：状态栏

- [ ] 页面顶部包含 428×54 StatusBar
- [ ] 时间固定 `9:41`
- [ ] 状态栏图标已从 GitHub 远程仓库下载到本地 `assets/icons/`（network.svg / wifi.svg / battery.svg）
- [ ] HTML 中使用本地相对路径引用状态栏图标
- [ ] 状态栏背景与 NavBar 一致（S21）

## Gate 7：图标 / 头像 / 插图 匹配与本地化

**图标（F11-F15）**

- [ ] `empty_icon.svg` 残留为 0
- [ ] 图标均从 GitHub 远程仓库 `icons/QUI_24_icons/` 或 `icons/` 获取
- [ ] 所有页面用到的图标已下载到本地 `assets/icons/` 目录
- [ ] HTML 中所有图标路径均为本地相对路径 `assets/icons/*.svg`
- [ ] 不存在远程 URL / Base64 / 外链图片引用图标
- [ ] 禁止自绘 / emoji / 外部图标库

**头像（F19 硬约束）**

- [ ] 含头像组件（List / Card / Message / NavBar L6）均已使用 `QUI_Avatars/AvatarN.svg`
- [ ] 无 `Avatar_32/40/52.svg` 占位残留
- [ ] 同页多个头像使用不同编号
- [ ] 已下载到 `assets/icons/QUI_Avatars/` 目录

**插图/图片（F20 硬约束）**

- [ ] 含图片组件（Card / ImageBlock / HSO / Grid）均已使用 `QUI_illustrations/` 真实素材
- [ ] 无 `placeholder_landscape/portrait/square.svg` 占位残留
- [ ] 风景照片引用已 URL 编码 `%20`
- [ ] 已下载到 `assets/icons/QUI_illustrations/` 目录

**通用**

- [ ] 缺失资源已输出问题报告

## Gate 8：初次产出

- [ ] 页面生成与必要实现已完成
- [ ] 内部规则检查已完成并可进入回归

## Gate 9：QUI Design Lint 全量核查（最多 3 轮）

每轮按 QUI Design Lint 五步执行。中间轮次静默修复，**仅最后一轮**输出完整 lint 报告。

### 第〇步 · Preflight（基线声明）

- [ ] 已清点涉及的组件（N 个）、图标（M 个含 src + 着色 Token）、Token（K 个）
- [ ] 已声明页面结构（StatusBar / NavBar / HomeBar / 背景色 / 主题）
- [ ] 已声明交互状态（hover / pressed / disabled / loading）
- [ ] 已声明容器宽度（428 通栏 / 396 嵌入）
- [ ] 已扫描 spec 的 `@MUST` / `@FORBIDDEN` / `@LINT` / `@SPEC_OF_TRUTH`

### 第一步 · 组件合法性

- [ ] 每个 UI 元素可在组件注册表中找到母组件（否则 F1）
- [ ] 子组件 ID 在变体空间中（否则 F4）
- [ ] 容器宽度 = 通栏 428 / 嵌入 396（S17）
- [ ] 与 `component-matrix.html` / spec 视觉一致
- [ ] F2 / F3 / F5 / F9 / F10 / F18 均已规避

### 第 1.5 步 · 图标使用验证

- [ ] F11 自绘 / F12 Emoji / F13 外部库 / F14 尺寸错位 / F15 Base64 均无
- [ ] F16 SVG 无硬编码 fill（使用 `currentColor`）
- [ ] F17 非 Button 场景未使用 filter hack
- [ ] **F19 头像占位已全部替换**
- [ ] **F20 图片占位已全部替换**
- [ ] 图标着色走 5 个 `--icon-*` Token

### 第二步 · Token 与样式（两级违规）

- [ ] TK1-TK17 全部通过：颜色 / 间距 / 圆角 / 字号 / 字重 / 行高 / 阴影 / 动效 / z-index / object-fit / border
- [ ] F6 硬编码颜色 / F7 非法字号 / F8 非法间距 均无
- [ ] 所有合法值通过 `var(--token-name)` 引用（否则 ⚠️ WARN）

### 第三步 · 页面结构

- [ ] S1-S28 全部通过
- [ ] S5 背景色强约束 / S17 容器宽度 / S19 吸底层级 / S21 StatusBar-NavBar 拼接 / S24-S28 模态层级序
- [ ] NV1 NavBar 底色拼接矩阵 / NV2 滚动态分割线 / DV1 分割线规范
- [ ] 嵌套允许矩阵（11 种容器）
- [ ] 无整个界面级滚动条（界面尺寸 ≤ 428×926）

### 第四步 · 合规评分

- [ ] 按 A/B/C/D/E 五级输出评级（跳过 Preflight 上限 C）
- [ ] 仅列出有问题的项，通过项跳过

### 回归结果要求

- [ ] 在 ≤3 轮内达到 **零 ⛔ ERROR / 零 ⚠️ WARN**，或执行满 3 轮后结束回归
- [ ] 仅最后一轮输出完整 lint 报告（Preflight + 逐项违规 + 评分汇总）
- [ ] 若第 3 轮后仍不合规，已输出未修复问题清单

## Gate 10：最终交付与 Failure Log 回填

- [ ] 已附 Gate -1~10 通过状态
- [ ] 已附回归轮次摘要（每轮 ERROR / WARN 数变化）
- [ ] 已附 QUI Design Lint 评分（A/B/C/D/E）
- [ ] 未达零违规时已附未修复问题清单
- [ ] 已附审查与完善建议（缺失组件 / 缺失变体 / 不合理之处 三维度）
- [ ] 若本次出现失败、偏差、返工、重试或反复调整，已在发生后写入项目根目录 `failure-log.md`
- [ ] 最终交付前已补全对应日志的解决方式、预防规则与关联规范
