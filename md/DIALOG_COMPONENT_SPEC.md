# 对话框 Dialog 组件设计规范

> **组件 ID**：`dialog`  
> **大类**：模态  
> **变体数量**：15 种

## 🔒 强约束声明

@LINT F1, F3, F10, S8, S15, TK1, TK9
@SPEC_OF_TRUTH 本文件为 Dialog 权威规范

### @MUST
- 变体编码 `{T|NT}-{P|C|I}-{S|D|T}`，共 15 种
- 输入类(I) 必须有标题(T)
- 圆角统一 14px，**无阴影**（与全局规范一致：除 Menu 外其他组件不使用阴影）
- 居中对齐 + 遮罩 `var(--overlay-modal)`
- 双按钮水平排列，中间 0.5×54px 竖向分割线 + `var(--border-default)`
- 三按钮纵向堆叠，每个 54px，顶部 0.5px 横向分割线 + `var(--border-default)`
- 操作按钮区与正文区之间 0.5px 横向分割线 + `var(--border-default)`

### @FORBIDDEN
- 发明注册表外的变体
- 与 ActionSheet / HalfScreenOverlay 相互嵌套
- 修改 14px 圆角或 54px 按钮高度

## 1. 组件概述

对话框（Dialog）是居中显示的模态弹窗组件，用于向用户传达重要信息并请求确认或决策。它通常在需要用户明确响应后才能继续操作时触发，是 iOS/移动端设计中的标准交互模式。

## 2. 组件结构

```
┌───────────────────────────────────┐
│  Overlay                          │
│  var(--overlay-modal)      │
│                                   │
│  ┌─────────────────────────────┐  │  ← border-radius: 14px
│  │  Title (optional)           │  │
│  │                             │  │
│  │  Body text                  │  │  ← text / checkbox / input
│  │  o Aux info (optional)      │  │  ← checkbox only
│  ├─────────────────────────────┤  │  ← divider 0.5px
│  │  Action buttons             │  │  ← 1 of 3 layouts below
│  └─────────────────────────────┘  │
│                                   │
└───────────────────────────────────┘

Action layouts:

[Single]
├─────────────────────────────────┤  ← divider 0.5px
│             Action              │  ← 54px full width
└─────────────────────────────────┘

[Double]
├─────────────────────────────────┤  ← divider 0.5px
│    Action    ┃    Action        │  ← 54px, vertical divider 0.5px
└─────────────────────────────────┘

[Triple]
├─────────────────────────────────┤  ← divider 0.5px
│            Action 1             │  ← 54px stacked
├─────────────────────────────────┤  ← divider 0.5px
│            Action 2             │  ← 54px
├─────────────────────────────────┤  ← divider 0.5px
│            Action 3             │  ← 54px
└─────────────────────────────────┘
```

## 3. 设计 Token

### 3.1 尺寸规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 对话框宽度 | 296px | 固定宽度 |
| 圆角 | 14px | 四角统一 |
| 标题区域 padding | 20px 20px 0 | 顶部/左右内边距 |
| 纯文本/勾选正文 padding（有标题） | 4px 28px 20px | 有标题时上边距 4px |
| 纯文本/勾选正文 padding（无标题） | 20px 28px 20px | 无标题时上边距 20px |
| 输入框正文 padding | 16px 24px 24px | 仅搭配标题使用 |
| 输入框尺寸 | 248 × 48px | 背景 rgba(116,116,128,0.08)，圆角 12px |
| 输入框内文本区 left | 16px | 内部文本距左 16px |
| 操作按钮高度 | 54px | 所有按钮统一高度 |
| 分割线高度 | 0.5px | 操作区域顶部及按钮间 |
| 勾选项 SVG 图标 | 20 × 20px | 圆形样式，`icons/Checkbox.svg`(未选中) / `icons/Checkbox_filled.svg`(选中)，SVG 固有尺寸均为 20×20 |

### 3.2 颜色规范

| 元素 | 色值 | Token |
|------|------|-------|
| 遮罩层 | var(--overlay-modal) | `--overlay-modal` |
| 对话框背景 | #FFFFFF | `--bg-bottom` |
| 标题文字 | var(--text-primary) | `--text-primary` |
| 正文文字 | var(--text-primary) | `--text-primary` |
| 辅助信息文案 | var(--text-tertiary) | `--text-tertiary` |
| 输入框背景 | var(--fill-tertiary) | `--fill-tertiary` |
| 输入框placeholder | var(--text-quaternary) | `--text-quaternary` |
| 输入框光标 | #0099FF | `--brand-standard` |
| 操作按钮文字 | #214CA5 | `--text-link` |
| 分割线 | var(--border-default) | `--border-default` |
| 阴影 | 无（除 Menu 外其他组件不使用阴影） | — |

### 3.3 字体规范

| 元素 | 字号/行高 | 字重 | 字体 |
|------|----------|------|------|
| 标题 | 17px / 1.35 | 600 (Semibold) | PingFang SC |
| 正文（有标题时） | 14px / 20px | 400 (Regular) | PingFang SC |
| 正文（无标题时） | 17px / 24px | 400 (Regular) | PingFang SC |
| 辅助信息文案 | 14px | 400 (Regular) | PingFang SC |
| 操作按钮 | 17px | 400 (Regular) | PingFang SC |

## 4. 区域类型定义

### 4.1 标题区域（2 类）

| 类型 | 说明 |
|------|------|
| 有标题 | 显示 17px Semibold 标题文字，居中对齐 |
| 无标题 | 不显示标题区域，正文区域上边距调整为 20px，正文字号调整为 17px/24px |

### 4.2 正文区域（3 类）

| 类型 | 组成 | 说明 |
|------|------|------|
| 纯文本 | 正文描述 | 仅包含描述文案 |
| 文本+勾选 | 正文描述 + 勾选项（含辅助信息） | 勾选项与辅助信息捆绑显示，使用圆形 SVG 图标 + "辅助信息文案" 文字 |
| 输入框 | 输入框（248×48px） | 必须搭配标题使用；背景 rgba(116,116,128,0.08)，圆角 12px；内含光标 + placeholder "输入文本"（色 var(--text-quaternary)） |

### 4.3 正文对齐规则

| 情况 | 对齐方式 | 说明 |
|------|---------|------|
| 正文一行 | text-align: center | 单行时居中显示 |
| 正文多行 | text-align: left | 多行时左对齐 |

### 4.4 操作区域（3 类）

| 类型 | 按钮 | 说明 |
|------|------|------|
| 单按钮 | Action | 仅一个操作按钮，全宽横向，文字 `var(--text-link)` Regular |
| 双按钮 | Action + Action | 两个按钮水平排列，中间有 0.5px 竖向分割线，文字 `var(--text-link)` Regular |
| 三按钮 | Action × 3 | 三个按钮纵向堆叠，每个高 54px，顶部有 0.5px 横向分割线，文字 `var(--text-link)` Regular |

## 5. 变体矩阵

标题(2) × 正文(3) × 操作(3) = **15 种变体**（其中输入框类仅搭配标题，故无标题×输入框不存在）

| 编号 | 标题 | 正文类型 | 操作类型 |
|------|------|---------|---------|
| T-P-S | ✓ | 纯文本 | 单按钮 |
| T-P-D | ✓ | 纯文本 | 双按钮 |
| T-P-T | ✓ | 纯文本 | 三按钮 |
| T-C-S | ✓ | 文本+勾选 | 单按钮 |
| T-C-D | ✓ | 文本+勾选 | 双按钮 |
| T-C-T | ✓ | 文本+勾选 | 三按钮 |
| T-I-S | ✓ | 输入框 | 单按钮 |
| T-I-D | ✓ | 输入框 | 双按钮 |
| T-I-T | ✓ | 输入框 | 三按钮 |
| NT-P-S | ✗ | 纯文本 | 单按钮 |
| NT-P-D | ✗ | 纯文本 | 双按钮 |
| NT-P-T | ✗ | 纯文本 | 三按钮 |
| NT-C-S | ✗ | 文本+勾选 | 单按钮 |
| NT-C-D | ✗ | 文本+勾选 | 双按钮 |
| NT-C-T | ✗ | 文本+勾选 | 三按钮 |

## 6. 交互行为

### 6.1 弹出/关闭
- 居中弹出，配合遮罩层淡入
- 点击操作按钮关闭对话框
- 弹窗打开时，背景页面不可操作（模态遮罩阻断底层交互）
- **禁止**与其他模态组件（ActionSheet、HalfScreenOverlay）相互嵌套
- 注意：变体矩阵和组件构建器中仅渲染对话框本体，不渲染遮罩层

### 6.2 操作反馈
- 点击操作按钮：执行对应操作并关闭

### 6.3 控件联动规则

组件构建器和变体矩阵中均提供以下控件，且行为严格一致：

| 控件类型 | 控件名称 | 选项 | 对应属性 | 默认值 |
|---------|---------|------|---------|--------|
| 二态开关 | 标题 | 开/关 | hasTitle | 开 |
| 分段选择器 | 正文类型 | 纯文本 / 文本+勾选 / 输入框 | bodyType | 纯文本（text） |
| 分段选择器 | 操作类型 | 单按钮 / 双按钮 / 三按钮 | actionType | 双按钮（double） |

**联动逻辑**：
- 切换"正文类型"为"输入框"时 → 自动强制开启"标题"开关
- "输入框"类型选中期间 → 标题开关不可关闭（点击无效）
- 切换"正文类型"离开"输入框"后 → 标题开关恢复自由切换
- 关闭"标题"时 → 正文字号自动从 14px/20px 切换为 17px/24px，正文 padding-top 从 4px 变为 20px
- 分段选择器切换时 → 激活项两侧分隔线自动隐藏（opacity: 0）

### 6.4 正文对齐判定

- 默认先设 `text-align: left`
- 渲染完成后通过 `requestAnimationFrame` 检测 `scrollHeight`：若 `scrollHeight <= lineHeight + 2` 则为单行，切换为 `text-align: center`；否则保持 `left`
- 此规则仅适用于纯文本和文本+勾选类型；输入框类型无需对齐判定

## 7. 布局规则

1. 对话框固定宽度 **296px**，垂直居中于遮罩层
2. 圆角统一 **14px**，**无阴影**（与全局规范一致）
3. 操作按钮区域与正文区域之间有 **0.5px** 横向分割线（`var(--border-default)`）；三按钮时每个按钮顶部均有 **0.5px** 横向分割线
4. 双按钮时水平排列（`display: flex`），按钮间有 **0.5px × 54px** 竖向分割线
5. 三按钮时纵向堆叠（`flex-direction: column`），每个按钮顶部有 **0.5px** 横向分割线
6. 纯文本/勾选正文区域内容宽度 **240px**（296 - 28×2 内边距）
7. 输入框正文区域 padding **16px 24px 24px**，输入框尺寸 **248×48px**（296 - 24×2 内边距）
8. 输入框内部文本区：`left: 16px`，宽 **216px**（248 - 16×2），高 48px，垂直居中
9. 勾选行规格：`margin-top: 12px`，`height: 20px`，图标与文案 `gap: 8px`
10. 所有文本颜色使用 `background-clip: text` 技术实现，以支持 CSS 变量降级

---

## 8. CSS 实现代码块

> Dialog 在 HTML 中通过 JavaScript 内联 `style.cssText` 实现，以下为等效 CSS 类形式。

### 8.1 外层容器

```css
.dialog-outer {
    width: 296px;
    background: var(--bg-bottom);
    border-radius: 14px;
    overflow: hidden;
    /* 无 box-shadow（与全局规范一致：除 Menu 外其他组件不使用阴影；遮罩由父容器 .dialog-overlay 承担） */
}
```

### 8.2 标题区域

```css
.dialog-header {
    padding: 20px 20px 0;
    text-align: center;
}
.dialog-title {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.35;
}
```

### 8.3 正文区域（纯文本/勾选）

```css
.dialog-body {
    padding: 4px 28px 20px;   /* 有标题时 bodyPadTop=4px, 无标题时=20px */
    text-align: center;
}
.dialog-body-text {
    font-size: 14px;          /* 有标题: 14px/22px, 无标题: 17px/24px */
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text-primary);
    line-height: 22px;
    word-wrap: break-word;
}
.dialog-check-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 12px;
    height: 20px;
    overflow: hidden;
}
.dialog-check-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
}
.dialog-check-label {
    font-size: 14px;
    font-weight: 400;
    color: var(--text-tertiary);
    white-space: nowrap;
}
```

### 8.4 正文区域（输入框）

```css
.dialog-body-input {
    padding: 16px 24px 24px;
}
.dialog-input-box {
    width: 248px;
    height: 48px;
    background: var(--fill-secondary);
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}
.dialog-input-text-area {
    position: absolute;
    left: 16px;
    top: 0;
    width: 216px;
    height: 48px;
    display: flex;
    align-items: center;
}
```

### 8.5 操作按钮区域

```css
/* 双按钮 — 水平排列 */
.dialog-actions-double {
    position: relative;
    display: flex;
}
.dialog-actions-double .dialog-btn {
    flex: 1;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

/* 三按钮 — 垂直排列 */
.dialog-actions-triple {
    position: relative;
    display: flex;
    flex-direction: column;
}
.dialog-actions-triple .dialog-btn {
    width: 100%;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

/* 单按钮 */
.dialog-actions-single {
    position: relative;
}
.dialog-actions-single .dialog-btn {
    width: 100%;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* 按钮文字 */
.dialog-btn-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text-link);
}

/* 分割线 */
.dialog-divider-h {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 0.5px;
    background: var(--border-default);
}
.dialog-divider-v {
    position: absolute;
    left: 0;
    top: 0;
    width: 0.5px;
    height: 54px;
    background: var(--border-default);
}
```

---

## 9. 动效规范

### 9.1 入场动效
- **类型**：居中缩放淡入（`scale(0.85) opacity(0) → scale(1) opacity(1)`）
- **时长**：250ms
- **缓动曲线**：ease-out
- **Token**：`--anim-dialog-in-duration` / `--anim-dialog-in-easing`

### 9.2 退场动效
- **类型**：缩放淡出（`scale(1) opacity(1) → scale(0.85) opacity(0)`）
- **时长**：200ms
- **缓动曲线**：ease-in
- **Token**：`--anim-dialog-out-duration` / `--anim-dialog-out-easing`

### 9.3 蒙层动效
- **颜色**：`var(--overlay-modal)`（`--overlay-modal`）
- **淡入**：250ms / ease-out（`--anim-overlay-in-*`）
- **淡出**：200ms / ease-in（`--anim-overlay-out-*`）
- 蒙层与对话框动效**同步执行**

### 9.4 关闭方式
- ⚠️ **蒙层不可关闭**：点击蒙层**不会**关闭对话框（`closeOnOverlay: false`），用户必须通过操作按钮关闭。这是与 ActionSheet / HalfScreenOverlay 的关键区别。
- 点击操作按钮 → 执行操作并关闭

---

## 10. 组件联动

### 10.1 触发来源

| 触发场景 | 典型示例 |
|----------|---------|
| 用户执行**需要二次确认的操作**时 | 删除、退出登录、注销账号、清空数据等不可逆操作 |
| 用户执行**需要授权/同意的操作**时 | 权限申请、协议确认、隐私授权 |
| 系统需要**中断用户流程并获取明确响应**时 | 版本更新提示、会话过期通知、异常状态告警 |
| 需要用户**输入少量文本后确认**时 | 重命名、输入验证码、填写备注 |

> **通用规则**：任何可交互元素（按钮、图标、文字链、列表行、ActionSheet 选项等）均可触发 Dialog。触发条件由业务逻辑决定，不限定特定组件类型。Dialog 作为模态中断，适用于必须获得用户明确响应才能继续的场景。

### 10.2 互斥约束
- **禁止**与 ActionSheet、HalfScreenOverlay 相互嵌套
- Dialog 打开时不可再弹出另一个模态组件

---

## 11. 键盘与焦点行为

适用于正文类型为"输入框"（T-I-S / T-I-D / T-I-T）的 Dialog 变体：

| 阶段 | 行为 | 说明 |
|------|------|------|
| Dialog 弹出时 | 对话框入场动效与键盘弹起**同步进行** | 缩放淡入（250ms ease-out）和键盘弹起同时执行，输入框自动获得焦点 |
| 键盘弹起后 | 对话框保持垂直居中，不上移 | Dialog 宽 296px、居中显示，位于屏幕上半区，键盘（约 336px）不会遮挡 |
| 输入过程中 | 光标闪烁，实时输入 | 输入框内文本区 left: 16px，宽 216px |
| 点击操作按钮时 | 键盘收起与 Dialog 退场动效**同步进行** | 键盘收起和缩放淡出（200ms ease-in）同时执行 |
| 点击输入框外（Dialog 内） | 输入框不失焦 | 模态对话框内焦点锁定在输入框上 |
