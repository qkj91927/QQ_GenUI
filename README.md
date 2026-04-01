# 移动端设计系统资源包 v1.3

> **⚠️ AI 模型必读**：本文件是资源包的入口指南，定义了文件读取流程和生成前的强制检查清单。各组件的**硬性约束规则**定义在 `md/<COMPONENT>_SPEC.md` 中，必须在使用对应组件前读取。

---

## 文件读取策略

根据 AI 上下文容量选择对应的读取层级：

### 必读（~10K tokens）
1. **`README.md`**（本文件）— 全局约束、检查清单、组件索引
2. **`json/index.json`** — 组件索引、组合规则、背景色约束

### 按需读取（每组件 ~6K tokens）
3. **`md/<COMPONENT>_SPEC.md`** — 使用哪个组件就读哪个，**约束规则在这里**
4. **`json/components/<component>.json`** — 该组件的结构化数据（精确数值）

### 可选（上下文充裕时）
5. **`css/QQ_color_tokens.css`**（11.5K tokens）— 完整颜色 Token 定义，按需查阅
6. **`css/tokens.css`**（2.2K tokens）— 非颜色 Token，信息已在各 MD 中内联覆盖

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
| 背景色 | 与导航栏背景色相同（默认透明，由导航栏决定） |
| 时间字体 | SF Pro / -apple-system / sans-serif，17px，font-weight: 600 |
| 图标 | `icons/network.svg` + `icons/wifi.svg` + `icons/battery.svg` |

**使用规则**：
1. 必须放置在页面最顶部，紧接着放导航栏（NavBar）
2. 背景色跟随导航栏
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
| 指示条颜色 | `rgba(0, 0, 0, 0.90)`（`--color-text-primary`） |
| 指示条位置 | 水平居中，距底部 8px |
| 背景色 | 透明（叠加在页面内容之上） |

**使用规则**：
1. Home Bar 属于**页面层级最顶层**（z-index 最高），固定在屏幕最底部，叠加显示在所有内容（包括模态面板）之上
2. **全局唯一，仅出现一次**：无论页面内有多少层级、跳转、模态弹窗，Home Bar 始终只有一个，不随组件重复渲染。页面跳转时不需要在新页面再添加 Home Bar
3. 纯展示元素，不可交互，不参与母组件列表计数
4. Home Bar 不属于任何组件自身；ActionSheet / HalfScreenOverlay 面板底部需预留 34px 安全区，但指示条由系统渲染，组件不包含
5. AIOInput 固定在 Home Bar 上方（`bottom: 34px`）

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
    background: var(--color-text-primary);
    border-radius: 2.5px;
}
```

---

## 二、资源包结构

```
design-system-v1.3/
├── README.md                    ← 入口指南（读取流程 + 检查清单 + 全局约束）
├── component-matrix.html        ← 组件矩阵（所有子组件变体的可视化预览总览）
├── component-builder.html       ← 组件搭建器（拖拽式页面构建，所见即所得）
├── css/
│   ├── tokens.css               ← 全局设计 Token（设备 / 字体 / 间距 / 圆角 / 阴影 / 动效）
│   └── QQ_color_tokens.css      ← QQ 颜色 Token（qq-light / qq-dark 双主题）
├── json/
│   ├── index.json               ← 全局索引 + Token 定义 + 组合规则 + 背景色约束
│   └── components/              ← 各组件的结构化数据（20 个 JSON 文件）
├── md/                          ← 各组件的设计规范文档（20 个 MD 文件，含硬性约束）
├── icons/
│   ├── *.svg                    ← 结构图标（占位/功能性，29 枚）
│   ├── placeholder_*.svg        ← 通用图片占位图（横版/竖版/正方形，3 枚 SVG）
│   └── QUI_24_icons/            ← QUI 图标库（437 枚，24px SVG）
```

### component-matrix.html 与 component-builder.html

| 文件 | 用途 | 说明 |
|------|------|------|
| `component-matrix.html` | 组件矩阵 | 以网格形式预览全部 20 个母组件及其所有子组件变体，用于快速查找和对比 |
| `component-builder.html` | 组件搭建器 | 交互式页面构建工具，支持从母组件列表中选择组件，拖入画布组装完整页面 |

两个文件中的**子组件数量、样式、ID 编码必须严格一致**，是镜像对应关系。

### 结构图标清单（icons/ 根目录）

| 图标文件 | 尺寸 | 用途 |
|----------|------|------|
| `Avatar_32.svg` / `Avatar_40.svg` / `Avatar_52.svg` | 32/40/52px | 头像占位图（列表、消息、卡片） |
| `Thumbnail_24.svg` / `Thumbnail_32.svg` / `Thumbnail_40.svg` / `Thumbnail_52.svg` | 24/32/40/52px | 缩略图占位图 |
| `empty_icon.svg` | 12-24px | 通用占位图标（**实际任务中必须替换为真实图标**） |
| `chevron_right.svg` / `chevron_left.svg` / `chevron_down.svg` | 24px | 方向箭头（跳转/返回/展开） |
| `close.svg` / `close_input.svg` / `Close_HalfScreen.svg` | 24px | 关闭按钮（通用/输入框/半屏浮层） |
| `Checkbox.svg` / `Checkbox_filled.svg` | 24px | 复选框未选/已选（Dialog 勾选项、Grouped List R5、ActionCombo、NavBar R6） |
| `tick.svg` | 24px | 勾选标记（Menu-C 勾选菜单） |
| `expand_list.svg` | 24px | 列表展开/下拉菜单 |
| `search.svg` | 24px | 搜索图标 |
| `more_upright.svg` | 24px | 更多操作 |
| `network.svg` / `wifi.svg` / `battery.svg` | - | 系统状态栏图标（信号/WiFi/电池） |
| `heart.svg` / `like.svg` / `star.svg` / `doc.svg` / `secondary.svg` / `remind_mute.svg` | 24px | 功能性图标（收藏/点赞/文档/辅助等） |

---

## 三、母组件列表（20个）

按 **导航 → 数据 → 操作 → 模态** 四大类排序：

| 大类 | ID | 名称 | 变体数 | 规范文档 | JSON 数据 |
|------|----|------|--------|----------|-----------|
| 导航 | `navbar` | 导航栏 NavBar | 97 | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` |
| 导航 | `hs_navbar` | 半屏导航栏 HalfScreen NavBar | 7 | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` |
| 数据 | `list` | 通栏式列表 Plain List | 67 | `LIST_COMPONENT_SPEC.md` | `plain-list.json` |
| 数据 | `form` | 卡片式列表 Grouped List | 33 | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` |
| 数据 | `card` | 卡片 Card | 10 | `CARD_COMPONENT_SPEC.md` | `card.json` |
| 数据 | `message` | 消息 Message | 4×2 | `MESSAGE_COMPONENT_SPEC.md` | `message.json` |
| 数据 | `text_block` | 文本块 TextBlock | 13 | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` |
| 数据 | `image_block` | 图片块 ImageBlock | 10 | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` |
| 数据 | `data_filter` | 数据筛选 DataFilter | 16 | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` |
| 数据 | `grid` | 宫格 Grid | 17 | `GRID_COMPONENT_SPEC.md` | `grid.json` |
| 数据 | `divider_spacing` | 分隔与间距 Divider & Spacing | 7 | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` |
| 操作 | `button` | 按钮 Button | 12 | `BUTTON_COMPONENT_SPEC.md` | `button.json` |
| 操作 | `action` | 操作组合 ActionCombo | 13 | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` |
| 操作 | `menu` | 菜单 Menu | 15 | `MENU_COMPONENT_SPEC.md` | `menu.json` |
| 操作 | `search` | 搜索框 Search | 6 | `SEARCH_COMPONENT_SPEC.md` | `search.json` |
| 操作 | `textfield` | 输入框 Textfield | 20 | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` |
| 操作 | `aio_input` | AIO 输入框 AIOInput | 3 | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` |
| 模态 | `action_sheet` | 操作面板 ActionSheet | 22 | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` |
| 模态 | `dialog` | 对话框 Dialog | 15 | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` |
| 模态 | `half_screen_overlay` | 半屏浮层 HalfScreenOverlay | 2 | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` |

> **变体数说明**：
> - **NavBar**（97）和 **Plain List**（67）：采用维度矩阵 × 约束排除方式定义变体，需查阅 MD 文档中的约束规则计算有效组合
> - **Grouped List**（33）= 27 个基础变体（L×R 矩阵）+ 6 个组合变体（Combo1-6）
> - **Card**（10）= C1-C10，其中 C10 为 Markdown 内容卡片（高度自适应）
> - **Message**（4×2）= 4 类内容（A通用文本/B图文长描述/C图文短标题/D图标消息）× 2 态（主态/客态）= 8 种子组件，分段选择器默认显示客态
> - **Textfield**（20）= 4 种类型（单行无标题/单行有标题/电话号码/多行文本）× 5 种状态（默认/激活/输入/完成/错误）
> - **AIOInput**（3）= I1默认态 / I2生成中态 / I3输入态，通过分段选择器切换
> - **ActionSheet**（42）= 操作数量(0-10) × 提示(有/无) × 警示(有/无)，常规+警示≥1
> - **TextBlock**（13）= H1-H7 居左 + C1-C6 居中

---

## 四、JSON 与 MD 文档分工指南

每个组件同时拥有 JSON 数据文件和 MD 规范文档，**分工明确、互不重复**：

| 维度 | JSON（`json/components/`） | MD（`md/`） |
|------|---------------------------|-------------|
| **定位** | 精确数值源（机器可读） | 设计意图 + 约束规则（人/AI 可读） |
| **包含** | 尺寸、间距、颜色Token、变体列表、状态定义、交互参数 | 组件概述、ASCII结构图、约束规则、交互行为、布局规则、使用场景 |
| **权威性** | 所有精确数值（px/颜色/字重等）以 JSON 为准 | 变体数量、约束规则、组合合法性以 MD 为准 |
| **互引** | 每个 JSON 含 `"spec"` 字段指向对应 MD | MD 尺寸表精简为属性+值两列，颜色/字体引用 JSON |

### 快速引用规则

1. **生成 UI 代码**：先读 MD 了解结构和约束 → 再读 JSON 获取精确数值
2. **查变体数量**：以 MD 文档中的"变体矩阵"为准，JSON `totalVariants` 为辅助校验
3. **查约束规则**：**仅在 MD 中定义**（JSON 的 `constraints` 为摘要）
4. **查精确数值**：JSON 的 `layout` / `style` / `states` / `dimensions` 字段
5. **查颜色 Token**：`css/QQ_color_tokens.css` 为唯一权威源；JSON 中的颜色值为快照引用
6. **跳转关联文件**：JSON 的 `"spec"` 字段 → 对应 MD 文档路径

---

## 五、组件间关系与联动

部分组件之间存在触发、嵌套或互斥关系，在页面设计中需注意：

### 5.1 触发关系

| 触发源 | 触发目标 | 说明 |
|--------|----------|------|
| DataFilter 下拉筛选按钮（C1） | Menu（无图标类） | 点击下拉筛选按钮后弹出菜单，菜单内容为筛选选项 |
| Grouped List R2（箭头跳转行） | Menu-C（勾选类菜单） | 列表行右侧箭头可触发弹出菜单选择 |
| NavBar 右侧操作按钮 | Menu / ActionSheet | 导航栏右侧"更多"按钮可触发菜单或操作面板 |
| Button（主要/次要按钮） | Dialog / ActionSheet | 按钮点击可触发确认对话框或操作面板 |

### 5.2 嵌套关系

| 外层组件 | 可嵌套的内层组件 | 说明 |
|----------|-----------------|------|
| HalfScreenOverlay 标准型（HSO-A） | HS_NavBar（半屏导航栏） | 标准型顶部默认使用 A3，可按业务替换为任意 HS_NavBar 变体；把手型不使用导航栏 |
| HalfScreenOverlay（半屏浮层） | Grouped List / Button / Textfield 等 | 标准型使用 HS_NavBar；把手型全屏态使用 NavBar（L3必选），详见各自 MD |
| Card C10（开放插槽卡片） | TextBlock / ImageBlock / List / Grid / DividerSpacing / Button / ActionCombo(A1-A5) | C1-C9 为固定结构；C10 内容区支持自由组合，详见 CARD_COMPONENT_SPEC.md §11 |

### 5.3 互斥关系

| 规则 | 说明 |
|------|------|
| 模态组件不可嵌套 | ActionSheet、Dialog、HalfScreenOverlay 三者之间不可互相嵌套 |
| 背景色互斥 | Card/Grouped List/Message 要求灰底（#F0F0F2），不可与白底组件同页使用白底 |
| AIOInput 固定底部 | AIOInput 固定在页面底部，不可嵌入其他组件内部 |

---

## 六、⚠️ 页面背景色约束

页面背景色根据包含的组件类型**强制确定**，不可随意选择：

| 背景色 | Token | 色值 | 触发条件 |
|--------|-------|------|----------|
| 浅灰色 | `bg_bottom_standard` | `#F0F0F2` | 页面包含**卡片式列表（Grouped List）**或**卡片（Card）**时必须使用 |
| AIO背景色 | `qq-bg-aio-01` | `#F0F0F2` | 页面包含**消息（Message）**组件时必须使用 |
| 白色 | `bg_bottom_light` | `#FFFFFF` | 默认背景色，仅当页面不包含卡片式列表、卡片和消息组件时使用 |
| 品牌蓝 | `bg_bottom_brand` | `#EFF4FF` | 品牌定制页面，按业务需要使用 |

> **优先级规则**：当页面同时包含需要灰色背景和白色背景的组件时，以灰色背景（`#F0F0F2`）为准。消息组件的 AIO 背景色（`qq-bg-aio-01`）与卡片/卡片式列表的灰色背景（`bg_bottom_standard`）色值相同，可共存。

---

## 七、动效系统索引

动效 Token 定义在 `css/tokens.css` 的第 5 节，覆盖以下 9 类交互动效：

| 动效类别 | Token 前缀 | 时长 | 缓动曲线 | 适用组件 |
|----------|-----------|------|---------|---------|
| 按压缩放（进入） | `--anim-press-in-*` | 100ms | ease-out | 所有可点击元素 |
| 按压缩放（恢复） | `--anim-press-out-*` | 150ms | ease-out | 所有可点击元素 |
| 开关切换 | `--anim-switch-*` | 200ms | ease-out | Switch 开关 |
| 子行展开 | `--anim-expand-*` | 250ms | ease-in-out | 列表折叠/展开 |
| 子行收起 | `--anim-collapse-*` | 200ms | ease-in | 列表折叠/展开 |
| 半屏浮层弹入 | `--anim-halfscreen-in-*` | 420ms | cubic-bezier(0.32, 0.72, 0.35, 1) | HalfScreenOverlay |
| 半屏浮层收回 | `--anim-halfscreen-out-*` | 300ms | cubic-bezier(0.32, 0.72, 0.35, 1) | HalfScreenOverlay |
| 菜单弹入 | `--anim-menu-in-*` | 200ms | ease-out | Menu |
| 菜单收回 | `--anim-menu-out-*` | 150ms | ease-in | Menu |
| 操作面板弹入 | `--anim-actionsheet-in-*` | 420ms | cubic-bezier(0.32, 0.72, 0.35, 1) | ActionSheet |
| 操作面板收回 | `--anim-actionsheet-out-*` | 300ms | cubic-bezier(0.32, 0.72, 0.35, 1) | ActionSheet |
| 对话框弹入 | `--anim-dialog-in-*` | 250ms | ease-out | Dialog |
| 对话框收回 | `--anim-dialog-out-*` | 200ms | ease-in | Dialog |
| 蒙层淡入 | `--anim-overlay-in-*` | 250ms | ease-out | 所有模态组件蒙层 |
| 蒙层淡出 | `--anim-overlay-out-*` | 200ms | ease-in | 所有模态组件蒙层 |

> **使用方法**：在 CSS 中通过 `var(--anim-xxx-duration)` 和 `var(--anim-xxx-easing)` 引用，确保动效参数全局一致。

---

## 八、⚠️ 生成前强制检查清单

在输出任何 UI 组件 HTML 之前，**必须按以下步骤逐项验证**：

### 步骤 1：读取组件规范
- 确认要使用的组件，读取其 `md/<COMPONENT>_SPEC.md`
- 重点阅读文档中的 **"属性约束"** 章节

### 步骤 2：检查组合合法性
- 通栏式列表 → 检查 `LIST_COMPONENT_SPEC.md` §3 属性约束（L×C×R 组合过滤）
- 卡片式列表 → 检查 `GROUPED_LIST_COMPONENT_SPEC.md` §3 属性约束（L×R 组合 + 嵌套规则）
- 导航栏 → 检查 `NAVBAR_COMPONENT_SPEC.md` §3 属性约束（L×C×R 强绑定）
- 模态组件 → 检查各自 SPEC 中的控件联动规则

### 步骤 3：检查颜色 Token
- **⚠️ 颜色权威来源**：颜色值以 `css/QQ_color_tokens.css` 为唯一权威来源。`json/index.json` 中的颜色摘要仅为快速参考，若有冲突以 CSS 文件为准
- `css/tokens.css` 仅包含非颜色 Token（设备/字体/间距/圆角/阴影/动效）
- 颜色 Token 定义在 `css/QQ_color_tokens.css` 中，通过 `data-theme` 属性切换主题
- 在 `<html>` 上设置 `data-theme="qq-light"`（默认浅色模式）或 `data-theme="qq-dark"`（深色模式）
- 所有颜色值必须使用 Token 定义的值，禁止自行编造色值
- 页面背景色须遵守上方"第六章 页面背景色约束"规则

### 步骤 4：检查通用规则
- 同一通栏式列表内所有行的 L/C/R 组合必须一致
- 模态组件（ActionSheet / Dialog / HalfScreenOverlay）之间不可嵌套
- 分割线不在列表最后一行底部显示
- 间距值必须为 4px 的整数倍，共 6 档（4/8/12/16/24/32px），组件间间距选择规则详见 `DIVIDER_SPACING_COMPONENT_SPEC.md`

### 步骤 5：图标使用规则

**已绑定图标（不可替换）**：
- 组件 MD / JSON 中已绑定具体 SVG 文件名的图标（如 `chevron_right.svg`、`tick.svg`、`Close_HalfScreen.svg`、`search.svg` 等）是**固定图标**，在实际设计任务中**不能更换为其他文件**
- 这些图标承载固定的交互语义（返回、关闭、勾选、展开等），更换会导致用户认知混乱

**占位图标（必须替换）**：
- `empty_icon.svg` 是**通用占位图标**，在实际设计任务中**必须替换**为 `icons/QUI_24_icons/` 中的真实图标
- 图标库位于 `icons/QUI_24_icons/`，共 437 枚 24px SVG 图标
- 引用路径格式：`icons/QUI_24_icons/<图标名>.svg`

**头像 / 缩略图占位（保持占位图）**：
- `Avatar_32/40/52.svg` 和 `Thumbnail_24/32/40/52.svg` 是**占位资源**，在生成时**保持占位图即可，不替换为真实图片**
- 占位图用于标示该区域的语义（头像、缩略图），保持相同尺寸和圆角规则（头像 `border-radius: 50%`，缩略图按组件规范）

### 步骤 6：输出审查与完善建议
- 完成设计任务后，审视最终方案，以清单形式附在回复末尾，涵盖以下维度：
  - **缺失组件**：当前 20 个母组件无法覆盖的设计需求（如需要但不存在的组件类型）
  - **缺失变体**：现有组件的变体不足以满足场景（如缺少某种尺寸、状态或布局）
  - **不合理之处**：组件规范与实际设计需求之间的冲突或不适配
  - **主流设计系统对比**：将当前方案与国际主流设计系统（Apple HIG、Material Design 3、Samsung One UI 等）进行对比，从交互模式、视觉美学、动效规范、无障碍等方面指出差异，并给出可借鉴的完善建议
- 无问题的维度注明"无缺失"或"符合主流规范"

---

## 九、版本日志

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.3 | 2026-03-31 | **图标绑定完善**：Plain List（L1-L7/R2/R6/R8/R9/C2-C3描述行）、NavBar（L1-L4/L6/C2/C4描述组10px）、Dialog（勾选图标路径前缀）全部完成 `icons/` 路径绑定；L1 尺寸从36px修正为24px；Card MD 删除"或内联SVG" · **图标使用规则重写**：README §步骤5 分三类——已绑定图标不可替换 / empty_icon 仅从 QUI_24_icons 替换 / 头像缩略图保持占位图不替换 · **Home Bar 规则重写**：明确系统级、页面层级最顶层、全局唯一不重复 · **资源大清理**：删除 `assets/` 整个目录（含 1_9048/15个SVG + 1_9610/32个PNG + 3366_9122/4个PNG + 11个未引用子目录70个文件）；新增 3 个通用占位 SVG（`placeholder_landscape/portrait/square.svg`）统一放入 `icons/`，各组件通过 `object-fit: cover` 适配；Grid 圆形变体（A5-A7/B3-B6）从 assets SVG 改为 CSS `grid-item-thumb` 渲染；AIOInput 光标改 CSS 实现、图标改引用 `empty_icon.svg` · **同步更新**：`component-matrix.html` / `component-builder.html` / 6个MD / 3个JSON 全部同步；修复 HSO Demo 断裂引用；修复 builder 因 `assetPath: ap` 未定义变量导致的崩溃 |
| v1.3 | 2026-03-30 | 动效体系完善（ActionSheet/Dialog/Overlay token 补全）；组件间联动规范新增（触发/嵌套/互斥关系）；Button/NavBar/Search/Textfield/Card/GroupedList/ActionCombo/AIOInput MD 补充组件联动章节；modalBehavior 扩展 overlayColor/closeMethods/gestureClose；Dialog 显式标注蒙层不可关闭；AIOInput 新增状态转换条件和 Message 配合关系；所有模态组件 MD/JSON 补充量化动效参数；60个按钮 token 补充注释；20个 MD 标准化元数据头部；TextBlock 编号体系改为 H(居左)/C(居中)；ActionSheet 操作数扩展至 0-10（42变体）；HSO 把手型全屏态规范（NavBar L3 + 手势参数）；结构图统一英文化对齐；C10 开放插槽嵌套规则完善 |
