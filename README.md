# QUI Basic 1.0

> **⚠️ AI 模型必读**：本文件是 **QUI Basic 1.0** 资源包的入口指南（22 母组件 · 529 变体 · 33 通用图标 + 437 业务图标 + **10 真实头像 SVG + 14 插图 PNG + 10 风景照片 JPG** · iPhone 428px 基准）。
>
> **⚠️ 三个硬约束**（任务交付前自检）：①含头像组件须用 `QUI_Avatars/AvatarN.svg` 替换占位（lint **F19**）；②含图片组件须用 `QUI_illustrations/` 真实素材替换 placeholder（lint **F20**）；③完成前必须跑全量 lint 至零 ERROR / 零 WARN。详细资源使用约定见**章节「三」**。

---

## 文件读取策略

> **⚠️ 设计任务工作流（强制）**：接到任何 UI 设计任务时，AI **必须**先执行**全量读取**——把 22 个母组件 + 子组件类型与规范读全，再结合需求**拆解到具体的母组件 / 子组件 / 变体 / 约束**，最终落地为页面。**严禁**在未读完所有组件 spec 的情况下凭"印象"先写代码。

### 第 0 步 · 任务预读（必读 · 任务起步前）
1. **`README.md`**（本文件）— 全局约束、组件索引、设备 / 背景色 / 吸顶 / 吸底 / 模态层级规则
2. **`QUI_DESIGN_LINT_SKILL.md`** — 合规检查规则（任务收尾强制执行；F1-F19 / TK1-TK17 / S1-S28 / NV / DV）
3. **`json/index.json`** — 组件索引、组合规则、背景色约束

### 第 1 步 · 组件全量预读（必读 · 任务起步前）
4. **`md/<COMPONENT>_SPEC.md` 全部 22 份** — 完整读取所有母组件 + 子组件类型与规范，建立完整组件认知后才能进行需求拆解。每份 spec 内含 @MUST / @FORBIDDEN / 变体表 / 约束矩阵 / 视觉规格，是**生成代码前的硬约束来源**。
5. **`md/DIVIDER_SPACING_COMPONENT_SPEC.md`** — 重点强调：页面中组件之间必须添加间距或分割线
6. **`md/HALF_SCREEN_OVERLAY_TEMPLATES.md`** — 半屏浮层场景模版库（任务涉及半屏浮层时必读）

### 第 2 步 · 需求拆解（基于上方全量认知）
1. 按 22 个母组件 + 子组件类型对照需求 → 拆解为「母组件 → 子组件 / 变体 / 状态」
2. 校验组合合法性（嵌套矩阵、约束规则、容量上限）
3. 明确每个区域的吸顶 / 吸底 / 背景色 / 头像替换策略
4. 列出需要的真实头像（`icons/QUI_Avatars/AvatarN.svg`）/ 插图（`icons/QUI_illustrations/illustrationN.png`）/ 图标（`icons/QUI_24_icons/`）

### 第 3 步 · 执行设计 · 落地代码
- 实时引用对应 `json/components/<component>.json`（精确数值）
- 颜色 / 圆角 / 字体 / 动效全走 token，禁止硬编码

### 第 4 步 · 收尾 Lint（强制循环）
- 执行 `QUI_DESIGN_LINT_SKILL.md` 全量检查 → 发现违规修复 → 再次检查 → 直至 0 ERROR / 0 WARN

### 可选（上下文充裕时补充阅读）
- **`css/Qdesign Color Tokens.css`**（39 QBasicTokens）— 完整颜色 Token 定义
- **`css/Qdesign Tokens.css`** — 非颜色 Token（设备/字体/间距/圆角/阴影/动效）

---

## 一、设备与系统框架

### 1.1 设备基准

| 属性 | 值 |
|------|------|
| 设备平台 | iOS（iPhone 14 Pro Max 基准） |
| 屏幕宽度 | **428px** |
| 屏幕高度 | 926px |
| 默认字体 | PingFang SC |
| 网格基准 | 4px（所有间距值必须为 4px 的整数倍） |

### 1.2 系统状态栏 StatusBar（顶部）

每个页面最顶部的固定元素，**每次设计任务必须在界面最顶部放置**。

| 属性 | 值 |
|------|------|
| 尺寸 | 428 × 54px（`--device-status-bar-height`） |
| 背景色 | **等于下方第一个吸顶组件的底色**：<br/>• 通常为 NavBar → 默认 `var(--bg-bottom)`，灰页场景 `var(--bg-secondary)` 等<br/>• **例外**：若顶部是图片（如沉浸式 banner），StatusBar 保持**透明底色**，由图片穿透显示 |
| 时间字体 | SF Pro / -apple-system / sans-serif，17px，font-weight: 600 |
| 图标 | `icons/network.svg` + `icons/wifi.svg` + `icons/battery.svg`（必须满格，不可替换）|

**使用规则**：
1. 必须放置在页面最顶部，紧接着放导航栏（NavBar）
2. **底色与下方第一个吸顶组件一致**（见 lint S21）：
   - 下方是 NavBar → StatusBar 底色 = NavBar 底色（确保视觉连续、不产生断层）
   - 下方是图片（沉浸式场景）→ StatusBar 保持**透明底色**，文字/图标建议切换为 `--text-white` / `--icon-white` 保证可读性
3. 纯展示元素，不可交互，不参与母组件列表计数
4. 时间固定显示 `9:41`，信号/WiFi/电池图标均为满格状态，不可修改

```css
/* StatusBar 54px */
.status-bar {
    width: 428px;
    height: 54px;
    position: relative;
    background: transparent; /* 跟随导航栏背景色 */
}
/* 内部结构：左侧时间(9:41) + 中间灵动岛占位 + 右侧信号/WiFi/电池图标 */
/* 时间: SF Pro 17px font-weight:600, 居中于左侧152px区域 */
/* 图标: icons/network.svg + icons/wifi.svg + icons/battery.svg */
```

### 1.3 底部安全区 Home Bar（底部）

iOS 底部小横条，**系统级元素，全局唯一**。

| 属性 | 值 |
|------|------|
| 安全区高度 | 34px |
| 指示条尺寸 | 144 × 5px |
| 指示条圆角 | 2.5px |
| 指示条颜色 | `var(--text-primary)` |
| 指示条位置 | 水平居中，距底部 8px |
| 背景色 | **等于上方第一个吸底组件的底色**（Action Combo / AIO Input）；若页面无吸底组件，则跟随页面底色 |

**使用规则**：
1. Home Bar 属于**页面层级最顶层**（z-index 最高），固定在屏幕最底部，叠加显示在所有内容（包括模态面板）之上（见 lint S19 吸底层级）
2. **全局唯一，仅出现一次**：无论页面内有多少层级、跳转、模态弹窗，Home Bar 始终只有一个，不随组件重复渲染
3. **底色必须与上方吸底组件一致**（见 lint S21）—— 避免 Home Bar 与 Action Combo / AIO Input 间产生视觉断层；无吸底组件的页面跟随页面底色
4. 纯展示元素，不可交互，不参与母组件列表计数
5. Home Bar 不属于任何组件自身；ActionSheet / HalfScreenOverlay 面板底部需预留 34px 安全区，但指示条由系统渲染，组件不包含
6. AIOInput 固定在 Home Bar 上方（`bottom: 34px`）

```css
/* Home Bar 34px */
.home-bar {
    width: 428px;
    height: 34px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 8px;
}
.home-bar-indicator {
    width: 144px;
    height: 5px;
    background: var(--text-primary);
    border-radius: 2.5px;
}
```

---

## 二、资源包结构

```
QUI-Basic-1.0/
├── README.md                    ← 入口指南（读取流程 + 组件索引 + 全局约束）
├── QUI_DESIGN_LINT_SKILL.md     ← 合规检查规则（任务收尾强制执行）
├── component-matrix.html        ← 组件矩阵（22 母组件 529 变体的可视化预览总览）
├── css/
│   ├── Qdesign Tokens.css       ← 全局设计 Token（设备 / 字体 / 间距 / 圆角 / 阴影 / 动效）
│   └── Qdesign Color Tokens.css ← QUI Basic 颜色 Token（39 个 QBasicToken，qq-light / qq-dark 双主题）
├── json/
│   ├── index.json               ← 全局索引 + Token 定义 + 组合规则 + 背景色约束
│   └── components/              ← 各组件的结构化数据（22 个 JSON 文件）
├── md/                          ← 各组件的设计规范文档（23 个 MD 文件，含硬性约束 + 模版库）
├── icons/
│   ├── *.svg                    ← 结构图标（占位/功能性，33 枚）
│   ├── placeholder_*.svg        ← 通用图片占位图（横版/竖版/正方形，3 枚）
│   ├── QUI_24_icons/            ← QUI 图标库（437 枚，24×24 SVG）
│   ├── QUI_Avatars/             ← 真实头像图集（Avatar1-Avatar10，10 张 52×52 SVG · 任务交付必用，替换 Avatar_32/40/52.svg 占位图）
│   └── QUI_illustrations/       ← 插图 + 风景照片（任务交付必用，替换 placeholder_landscape/portrait/square.svg 占位图）
│       ├── illustration1-14.png           ← 14 张插图（Card / HSO 新手引导 / 运营 banner 等通常用此）
│       └── landscape photos1-10.JPG       ← 10 张风景照片（四 / 九宫格等通常用此；引用需 URL 编码 %20）
├── assets/
│   └── CodeBuddyAssets/         ← 母体 demo 专属 SVG 资源
└── demo/
    └── grouped-list-demo.html   ← 母体 × 规则 → 变体 演示页（被 component-matrix.html 通过 iframe 嵌入）
```

### component-matrix.html

单一 HTML 入口，以网格形式预览全部 **22 母组件 · 529 变体**，用于快速查找、对比、复制样式代码。支持 Preview / Markdown / JSON / CSS 多视图切换；通过 iframe 嵌入 `demo/grouped-list-demo.html`（母体 × 规则 → 变体生成演示页）。

> **图标 / 头像 / 插图 / 照片资源清单**：完整的 33 通用图标 + 437 业务图标（QUI_24_icons/）+ **10 真实头像 SVG（QUI_Avatars/）** + **14 插图 PNG + 10 风景照片 JPG（QUI_illustrations/）** 清单详见 `QUI_DESIGN_LINT_SKILL.md` 的"图标资源清单"章节，含每个资源的用途、标准尺寸和选用规则。

---

## 三、资源使用约定

### 3.1 头像替换（HARD · F19）
含头像的组件（List / Card / Message / NavBar L6 等）**必须**用 `icons/QUI_Avatars/AvatarN.svg`（N ∈ 1..10）替换 `Avatar_32/40/52.svg` 占位图。允许等比缩放至 32 / 40 / 52；同页多个头像须用不同编号；渲染保持 `border-radius: 50%`。

### 3.2 图片 / 插图替换（HARD · F20）
含图片的组件（Card 富媒体 / ImageBlock / HSO 新手引导 / 运营 banner 等）**必须**用 `icons/QUI_illustrations/` 真实素材替换 `placeholder_landscape/portrait/square.svg` 占位图。

### 3.3 插图 vs 照片（软性 Convention · 非 MUST）
| 类型 | 张数 | 引用 | 推荐场景 |
|------|------|------|---------|
| 插图 Illustration | 14 | `icons/QUI_illustrations/illustrationN.png` (N=1..14) | Card / HSO 新手引导 / 运营 banner |
| 风景照片 Photo | 10 | `icons/QUI_illustrations/landscape%20photosN.JPG` (N=1..10) | 四宫格 / 九宫格 |

> ⚠️ 照片文件名含空格，HTML 引用时必须 URL 编码为 `%20`，否则部分环境加载失败。
> 同页多个素材须用不同编号；插图 / 照片可按场景灵活混用。

### 3.4 空页面 / 空状态
暂不做额外规则，保持空白即可，后续视需要再补充。

---

## 四、母组件列表（22个）

按 **导航 → 数据 → 操作 → 模态 → 运营** 五大类排序：

| 大类 | ID | 名称 | 变体数 | 规范文档 | JSON 数据 |
|------|----|------|--------|----------|-----------|
| 导航 | `navbar` | 导航栏 NavBar | 97 | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` |
| 导航 | `hs_navbar` | 半屏导航栏 HalfScreen NavBar | 7 | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` |
| 数据 | `list` | 通栏式列表 Plain List | 110 | `LIST_COMPONENT_SPEC.md` | `plain-list.json` |
| 数据 | `form` | 卡片式列表 Grouped List | 52 | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` |
| 数据 | `card` | 卡片 Card | 10 | `CARD_COMPONENT_SPEC.md` | `card.json` |
| 数据 | `message` | 消息 Message | 4×2 | `MESSAGE_COMPONENT_SPEC.md` | `message.json` |
| 数据 | `text_block` | 文本块 TextBlock | 13 | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` |
| 数据 | `image_block` | 图片块 ImageBlock | 10 | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` |
| 数据 | `data_filter` | 数据筛选 DataFilter | 16 | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` |
| 数据 | `grid` | 宫格 Grid | 17 | `GRID_COMPONENT_SPEC.md` | `grid.json` |
| 数据 | `divider_spacing` | 分隔与间距 Divider & Spacing | 7 | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` |
| 操作 | `button` | 按钮 Button | 12 | `BUTTON_COMPONENT_SPEC.md` | `button.json` |
| 操作 | `action` | 操作组合 ActionCombo | 15 | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` |
| 操作 | `menu` | 菜单 Menu | 15 | `MENU_COMPONENT_SPEC.md` | `menu.json` |
| 操作 | `search` | 搜索框 Search | 12 | `SEARCH_COMPONENT_SPEC.md` | `search.json` |
| 操作 | `textfield` | 输入框 Textfield | 50 | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` |
| 操作 | `aio_input` | AIO 输入框 AIOInput | 3 | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` |
| 操作 | `toast` | 轻提示 Toast | 5 | `TOAST_COMPONENT_SPEC.md` | `toast.json` |
| 模态 | `action_sheet` | 操作面板 ActionSheet | 42 | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` |
| 模态 | `dialog` | 对话框 Dialog | 15 | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` |
| 模态 | `half_screen_overlay` | 半屏浮层 HalfScreenOverlay | 2 | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` |
| 运营 | `badge` | 红点 Badge | 11 | `BADGE_COMPONENT_SPEC.md` | `badge.json` |

> **变体数说明**：
> - **Plain List**（110）= 67 种默认态 + 43 种多选态；R2/R3 仅限 C1（单行）；R1 允许与 C1/C2/C3 搭配；多选态同步此约束
> - **Grouped List**（52）= 46 个基础变体（L×R 矩阵，含 L8-L11 tick 勾选类）+ 6 个组合变体（Combo1-6）
> - **Card**（10）= C1-C10，其中 C10 为 Markdown 内容卡片（高度自适应）
> - **Message**（4×2）= 4 类内容（A通用文本/B图文长描述/C图文短标题/D图标消息）× 2 态（主态/客态）= 8 种子组件
> - **Search**（12）= 6 交互状态（A1-A3/B1-B3）× 2 配色（灰底用于白页 / 白底用于非白页），按页面底色反相映射
> - **Textfield**（50）= A-D 4 种类型 × 5 种状态 = 20 + E 复合输入框 6 种 × 5 种状态 = 30
> - **AIOInput**（3）= I1默认态 / I2生成中态 / I3输入态
> - **ActionSheet**（42）= 操作数量(0-10) × 提示(有/无) × 警示(有/无)，常规+警示≥1
> - **TextBlock**（13）= H1-H7 居左 + C1-C6 居中
> - **Toast**（5）= T1加载中 / T2成功 / T3失败 / T4中性文字 / T5带操作
> - **Badge**（11）= 强提醒 B1-B4（红色，含小红点 / 个位 / 两位 / 99+）+ 弱提醒 W1-W4（灰色半透明）+ AIO 导航栏 A1-A3（更弱灰底 + 深色字）

---

## 五、JSON 与 MD 文档分工指南

每个组件同时拥有 JSON 数据文件和 MD 规范文档，**分工明确、互不重复**：

| 维度 | JSON（`json/components/`） | MD（`md/`） |
|------|---------------------------|-------------|
| **定位** | 精确数值源（机器可读） | 设计意图 + 约束规则（人/AI 可读） |
| **包含** | 尺寸、间距、变体列表、状态定义、交互参数（**不含颜色**） | 组件概述、ASCII结构图、约束规则、交互行为、布局规则、使用场景 |
| **权威性** | 所有精确数值（px/字重等）以 JSON 为准；**颜色以 `css/Qdesign Color Tokens.css` 为准** | 变体数量、约束规则、组合合法性以 MD 为准 |
| **互引** | 每个 JSON 含 `"spec"` 字段指向对应 MD | MD 尺寸表精简为属性+值两列，颜色/字体引用 JSON |

### 快速引用规则

1. **生成 UI 代码**：先读 MD 了解结构和约束 → 再读 JSON 获取精确数值
2. **查变体数量**：以 MD 文档中的"变体矩阵"为准，JSON `totalVariants` 为辅助校验
3. **查约束规则**：**仅在 MD 中定义**（JSON 的 `constraints` 为摘要）
4. **查精确数值**：JSON 的 `layout` / `style` / `states` / `dimensions` 字段
5. **查颜色 Token**：`css/Qdesign Color Tokens.css` 为**唯一权威来源**，JSON 不再声明颜色
6. **跳转关联文件**：JSON 的 `"spec"` 字段 → 对应 MD 文档路径

---

## 六、组件间关系与联动

### 5.1 触发关系

| 触发源 | 触发目标 | 说明 |
|--------|----------|------|
| DataFilter 下拉筛选按钮（C1） | Menu（无图标类） | 点击下拉筛选按钮后弹出菜单，菜单内容为筛选选项 |
| Grouped List R2（箭头跳转行） | Menu-C（勾选类菜单） | 列表行右侧箭头可触发弹出菜单选择 |
| NavBar 右侧操作按钮 | Menu / ActionSheet | 导航栏右侧"更多"按钮可触发菜单或操作面板 |
| Button（主要/次要按钮） | Dialog / ActionSheet | 按钮点击可触发确认对话框或操作面板 |

### 5.2 嵌套关系 · 简表

概要：HSO-A 嵌 HS_NavBar；HSO 内嵌非模态组件；Card C10 嵌 TextBlock / ImageBlock / List / Grid / Button / Action(A1-A5)。

> **权威矩阵**：完整的「容器 → 可嵌入/禁止嵌入 子组件白名单」见 `QUI_DESIGN_LINT_SKILL.md` 的"嵌套允许矩阵"（覆盖 11 种容器）。

### 5.3 互斥关系 · 简表

- ActionSheet / Dialog / HalfScreenOverlay 三大模态**禁止互相嵌套**（见 lint F10 / S8）
- AIOInput 固定在页面底部，**不可嵌入**其他组件内部（见 lint S15）

---

## 七、⚠️ 页面背景色约束

页面背景色根据包含的组件类型**强制确定**，不可随意选择（见 lint S5）：

| 背景色 | Token | 色值 | 触发条件 |
|--------|-------|------|----------|
| 浅灰色 | `--bg-secondary` | `#F0F0F2` | 页面包含 **Card / Grouped List / Message / AIO** 任一时必须使用 |
| 白色 | `--bg-bottom` | `#FFFFFF` | 默认背景色，仅当页面不含上述组件时使用 |
| 品牌浅蓝 | `--bg-bottom-brand` | `#EFF4FF` | 品牌定制页面，按业务需要使用 |

> **NavBar 底色拼接规则**：NavBar 底色与页面底色的合法组合矩阵见 lint **NV1** 规则。
> **Search 配色反相映射**：白页用灰底 Search / 非白页用白底 Search，详见 `md/SEARCH_COMPONENT_SPEC.md`。

---

## 八、吸顶 / 吸底复合规则

### 7.1 吸顶复合（严格 3 层结构）

| 层级 | 组件 | 高度 | 必选 |
|------|------|------|------|
| **L1（必有）** | NavBar | 44px | ✅ |
| **L2（可选）** | DataFilter **A 页签** | 40px | — |
| **L3（可选）** | DataFilter **D 标签** 或 **E 面包屑**（二选一）| D1-D4: 40px / D5: 62px / E: 40px | — |

**合法组合（4 种）**：`L1` · `L1+L2` · `L1+L3` · `L1+L2+L3`

**禁止参与吸顶**：
- Search A 一级 / B 二级（全系）
- DataFilter **B 分段选择** · **C 下拉筛选**
- TextBlock · 其他未列出组件

**分割线承担规则**（只有 NavBar / A 页签可提供底线）：
- 含 L3（D 或 E）→ **整体无分割线**（D/E 自身无底线）
- 仅 L1+L2 → L2 页签底线 `var(--border-default)` 0.5px 作整体底线；L1 NV2 禁用
- 仅 L1 → L1 自身 NV2 规则（滚动时显 0.5px `var(--border-weak)`）

**层级 CSS（示例）**：
```css
.navbar-row  { position: sticky; top: 0;                      z-index: 12 }
.sticky-l2   { position: sticky; top: 44px;                   z-index: 11 }
.sticky-l3   { position: sticky; top: calc(44px + 40px);      z-index: 10 }
```

### 7.2 吸底复合

- Action Combo 多行型（A + B 辅助操作行）整体吸底 `bottom: 34px`（Home Bar 在其上方）
- **Action Combo 与 AIO Input 互斥**：同页面最多存在其中一个
- 页面滚动容器 `padding-bottom` ≥ 吸底复合高度 + 34px

### 7.3 层级序 & 互斥

**从高到低**：
1. **StatusBar · Home Bar**（最高，系统级，始终可见）
2. **Toast · 模态组件**（Dialog / ActionSheet / HSO，含遮罩）
3. 吸顶/吸底组件
4. 页面内容

**互斥**：
- **Toast 与模态组件互斥**（同屏不可共存 — 打开模态前必须关闭 Toast）
- **模态组件之间互斥**（见 lint F10）

详见 lint **S24-S28**。

---

## 九、⚠️ 任务收尾 · 强制 Lint 循环检查

每次 UI 设计任务完成前，**必须**执行以下循环直至无违规：

1. **执行检查**：读取 `QUI_DESIGN_LINT_SKILL.md`，按其 Preflight → 两级违规制 → F1-F18 / TK1-TK16 / S1-S17 / NV1-NV2 / DV1 全量扫描当前代码
2. **修复违规**：如发现 ⛔ ERROR 或 ⚠️ WARN，立即根据 lint 报告修复
3. **再次检查**：修复后重新执行 lint，确认问题已消除
4. **循环直至通过**：重复 1-3 直到 lint 报告**零 ERROR、零 WARN**
5. **输出合规声明**：在最终回复末尾附加 lint 合规评分报告（参考 lint skill 的"评分汇总"格式）

**lint skill 核心检查维度：**
- 组件合法性（F1-F18 禁止项 + 嵌套允许矩阵 + 变体约束）
- 图标合规（F11-F15 自绘/Emoji/外部库/尺寸错位 + 图标使用验证 + 着色 Token）
- Token 绑定率（TK1-TK16：颜色/间距/圆角/字号/字重/行高/阴影/动效/z-index/object-fit/border）
- 结构规则（S1-S17：StatusBar/HomeBar/唯一性/固定位置/容量上限/标准宽度）
- 专项规则（NV1 NavBar 底色拼接 · NV2 滚动态分割线 · DV1 分割线规范）
- 元标记识别（`@MUST` / `@FORBIDDEN` 视为硬约束，自然语言视为说明性内容）

> ⚠️ **跳过 lint 检查或在未通过 lint 的情况下交付，视为任务未完成。**
