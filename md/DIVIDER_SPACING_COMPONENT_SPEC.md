# 分隔与间距 Divider & Spacing · 组件规范

> **组件 ID**：`divider_spacing`  
> **大类**：数据  
> **变体数量**：7 种（A分割线1 + B间距6）

## 🔒 强约束声明

@LINT DV1, TK2a, TK4
@SPEC_OF_TRUTH 本文件为 Divider & Spacing 权威规范

### @MUST
- A 分割线独立使用时：强绑 0.5px + `var(--border-weak)`（水平高度 / 垂直宽度）
- B 间距仅 6 档：xs=4 / s=8 / m=12 / l=16 / xl=24 / xxl=32 px
- 间距区域始终透明，横向撑满屏幕（428px）
- 组件内部分割线 → 按各组件 spec 定义（允许 `--border-weak` 或 `--border-default`）

### @FORBIDDEN
- 独立使用 A 分割线时颜色非 `--border-weak`
- 分割线厚度非 0.5px
- 间距值非 4-mult（5/10/20 等）
- 间距区域添加可见元素
- 使用 `fill-*` / `accent-*` / `brand-*` 作分割线色

## 概述

**分隔与间距**是用于在界面中分隔内容层级、控制视觉节奏的基础布局组件。包含两类子组件：

- **A. 分割线 Divider**：以细线形式分隔同一区域内的列表条目或内容块
- **B. 间距 Spacing**：以透明空白区域分隔不同内容模块，控制页面纵向节奏

## 子组件清单（共 7 种）

| 分类 | ID | 名称 | 高度 |
|------|-----|------|------|
| A. 分割线 | A1 | 分割线 Divider | 0.5px |
| B. 间距 | spacing-xs | 极小间距 | 4px |
| B. 间距 | spacing-s | 小间距 | 8px |
| B. 间距 | spacing-m | 中间距 | 12px |
| B. 间距 | spacing-l | 大间距 | 16px |
| B. 间距 | spacing-xl | 超大间距 | 24px |
| B. 间距 | spacing-xxl | 最大间距 | 32px |

---

## A. 分割线 Divider

### 视觉规范

| 属性 | 水平分割线 | 垂直分割线 |
|------|-----------|-----------|
| 厚度 | 高度 0.5px | 宽度 0.5px |
| 颜色 | `var(--border-weak)` | `var(--border-weak)` |
| 背景 | 透明（跟随父容器背景） | 透明 |
| 长度 | 按场景（通栏 428 / 缩进按需）| 按场景（如 Dialog 双按钮 54px、Action B6/B7 14px、DataFilter 分段 16px）|

### 使用参数

| 模式 | 宽度/高度 | 使用场景 |
|------|----------|----------|
| 水平·通栏 | 428px | 分隔独立内容板块 |
| 水平·居中缩进 | 按需（如 396 / 364 / 起点左偏移）| 列表行之间、卡片内部行间 |
| 垂直 | 长度按场景 | 组件内部结构分隔（双按钮、分段控件、文字链组）|

### 使用语义（⚠️ 关键区分）

| 场景 | 颜色强绑定 | 说明 |
|------|----------|------|
| **独立使用**（作为 `divider_spacing` 组件在页面上分隔板块）| **强绑 `var(--border-weak)`** | 此时 divider 是通用组件，颜色必须严格为 weak |
| **组件内部分割线**（Dialog / Card / DataFilter 等组件自己内部结构的分割）| **以各组件 spec 为准**（可 `--border-weak` 或 `--border-default`）| 组件设计师可根据视觉层级需要选择 weak 或 default；lint 不强行统一 |

> `--border-default` 是 **solid 强描边**（#C6C6C8），用于 Button 次级描边、Input 边框等；组件内分割线可使用以营造更强的结构感。
> `--border-weak` 是 **半透明弱 hairline**（rgba 12%），是"独立 divider"和"列表行间"的默认选择。

### 约束

1. 厚度固定 0.5px（水平高度 / 垂直宽度）
2. 列表最后一行底部不显示分割线
3. 通栏/缩进/方向不构成独立变体
4. **禁止硬编码 rgba / 非 token 颜色**
5. **禁止**用 `fill-*` / `accent-*` / `brand-*` 作分割线色（语义错用）

---

## B. 间距 Spacing

### 视觉规范

| 属性 | 值 |
|------|-----|
| 宽度 | 428px |
| 背景 | `transparent` |
| 高度 | 4px 整数倍，共 6 档 |

### 间距选择规则

**核心原则**：关系越近间距越小，关系越远间距越大。不确定时使用 spacing-l（16px）作为安全默认值。

#### 主表（原则层）

| ID | 高度 | 语义 | 判断标准 |
|----|------|------|----------|
| **spacing-xs** | 4px | 紧贴 | 两个元素**共同构成一个信息单元**（标题+副标题、标签+说明） |
| **spacing-s** | 8px | 紧凑 | 两个元素**类型相同且并列**（段落与段落、消息与消息） |
| **spacing-m** | 12px | 容器间 | 两个**独立容器**并列（卡片与卡片、表单组与表单组） |
| **spacing-l** | 16px | 组件间（默认） | 两个**不同类型组件**相邻，且无更具体规则时 |
| **spacing-xl** | 24px | 模块间 | 两个组件属于**不同功能模块**（信息区→操作区） |
| **spacing-xxl** | 32px | 页面底部留白 | 页面**最后一个组件到底部**的留白 |

#### 场景速查表（举例层）

| 上方 → 下方 | 间距 | 归类原则 |
|-------------|------|---------|
| StatusBar → NavBar | 0px | 锚定元素，系统级固定拼接 |
| AIOInput（固定底部） | 0px | 锚定元素，系统级固定拼接 |
| 通栏列表行之间 | 分割线 | 用分割线代替间距 |
| H2 标题 + H6 摘要 | spacing-xs | 共同构成信息单元 |
| 分组标题 ↔ Grouped List ↔ 底部说明 | spacing-xs | 共同构成信息单元 |
| Textfield 输入行 ↔ 附加说明行 | spacing-xs | 共同构成信息单元 |
| Card 大标题 ↔ 副标题（C6/C7） | spacing-xs | 共同构成信息单元 |
| Dialog 标题 → 正文 | spacing-xs | 共同构成信息单元 |
| ActionCombo A行 → B辅助操作行 | spacing-xs | 共同构成信息单元 |
| TextBlock + TextBlock | spacing-s | 同类并列 |
| Message + Message | spacing-s | 同类并列 |
| Card + Card | spacing-m | 容器并列 |
| Grouped List 组 + 组 | spacing-m | 容器并列 |
| NavBar → Search / DataFilter | spacing-l | 组件间（默认） |
| DataFilter → List / Card | spacing-l | 组件间（默认） |
| Search → List | spacing-l | 组件间（默认） |
| TextBlock → Grouped List | spacing-l | 组件间（默认） |
| TextBlock → ActionCombo | spacing-xl | 内容→操作 |
| 个人信息区 → 设置列表 | spacing-xl | 不同模块 |
| 最后组件 → 页面底部 | spacing-xxl | 页面底部留白 |

> **重要**：所有组件仅输出净内容高度，上下间距 100% 由外部间距组件（spacing-xs ~ spacing-xxl）提供。组件自身不含上下 padding。

### 设计约束

1. 间距高度为 4px 整数倍，不可使用非标准值（5px、10px、20px 等）
2. 间距区域始终透明，不可添加可见元素
3. 间距区域横向撑满屏幕宽度

---

## CSS 实现代码块

### 分割线

```css
.divider-container {
    width: 428px;
    background: var(--bg-bottom);
    position: relative;
    display: flex;
    align-items: center;
}
.divider-line {
    height: 0.5px;
    background: var(--border-weak);
}
.divider-line.inset-both {
    width: 396px;
    margin: 0 auto;
}
```

### 间距

```css
.spacing-container {
    width: 428px;
    background: transparent;
    position: relative;
}
.spacing-block-inner {
    width: 428px;
    background: transparent;
}
/* 间距标注（仅设计稿展示用） */
.spacing-annotation {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 10px;
    font-family: 'SF Mono', 'Menlo', monospace;
    color: var(--brand-standard);
    opacity: 0.6;
    pointer-events: none;
    white-space: nowrap;
}
```

## Figma 属性映射

### Divider

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Width Mode | Enum | `FullWidth` / `InsetBoth` |
| Orientation | Enum | `Horizontal` / `Vertical` |

### Spacing

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Size | Enum | `xs(4)` / `s(8)` / `m(12)` / `l(16)` / `xl(24)` / `xxl(32)` |
