# 操作面板 ActionSheet 组件设计规范

> **组件 ID**：`action_sheet`  
> **大类**：模态  
> **变体数量**：22 种

## 1. 组件概述

操作面板（ActionSheet）是从屏幕底部弹出的模态面板，用于向用户提供一组可选操作。它通常在用户需要做出选择或确认操作时触发，是 iOS/移动端设计中的标准交互模式。

## 2. 组件结构

```
┌───────────────────────────────────┐
│  Overlay                          │
│  var(--overlay_dark)        │
├───────────────────────────────────┤  ← border-radius: 16px
│  ┌─────────────────────────────┐  │
│  │     Title (optional)        │  │  ← 56px
│  ├─────────────────────────────┤  │  ← divider 0.5px
│  │          Action             │  │  ← 56px × N (0~10)
│  ├─────────────────────────────┤  │  ← divider 0.5px
│  │     ...more actions...      │  │
│  ├─────────────────────────────┤  │  ← divider 0.5px
│  │  Danger Action (optional)   │  │  ← 56px
│  └─────────────────────────────┘  │
│           10px gap                │  ← bg: var(--bg_middle_standard)
│  ┌─────────────────────────────┐  │
│  │          Cancel             │  │  ← 56px
│  └─────────────────────────────┘  │
│         Home Bar (34px)           │  ← system, not part of component
└───────────────────────────────────┘
```

## 3. 设计 Token

### 3.1 尺寸规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 面板宽度 | 428px | 与设备等宽 |
| 顶部圆角 | 16px | 仅左上、右上 |
| 行高度 | 56px | 所有行统一高度 |
| 主区块与取消间距 | 10px | 由面板背景色填充 |
| 分割线高度 | 0.5px | 行间分割 |

### 3.2 颜色规范

| 元素 | 色值 | Token |
|------|------|-------|
| 遮罩层 | rgba(0, 0, 0, 0.50) | `--color-overlay-dark` |
| 面板背景 | #F3F3F7 | `--color-bg-secondary` |
| 行背景 | #FFFFFF | `--color-bg-item` |
| 操作提示文字 | rgba(60, 60, 67, 0.76) | `--color-text-secondary` |
| 常规操作文字 | rgba(0, 0, 0, 0.90) | `--color-text-primary` |
| 警示操作文字 | #F74C30 | `--color-feedback-error` |
| 取消文字 | rgba(0, 0, 0, 0.90) | `--color-text-primary` |
| 分割线 | rgba(0, 0, 0, 0.08) | `--color-separator` |

### 3.3 字体规范

| 元素 | 字号 | 字重 | 字体 |
|------|------|------|------|
| 操作提示 | 14px | 400 (Regular) | PingFang SC |
| 常规操作 | 17px | 400 (Regular) | PingFang SC |
| 警示操作 | 17px | 400 (Regular) | PingFang SC |
| 取消 | 17px | 400 (Regular) | PingFang SC |

## 4. 行类型定义

### 4.1 标题行（操作提示）

- **样式属性**: `data-样式="标题"`
- **字号**: 14px
- **颜色**: text_secondary
- **对齐**: 水平居中
- **文本规则**: 仅单行，禁止换行，最大 **20 个字符**，超出截断（`text-overflow: ellipsis`）
- **分割线**: 无（位于第一行时）
- **可选性**: 可选

### 4.2 常规操作行

- **样式属性**: `data-样式="常规操作"`
- **字号**: 17px
- **颜色**: text_primary
- **对齐**: 水平居中
- **文本规则**: 仅单行，禁止换行，最大 **10 个字符**，超出截断（`text-overflow: ellipsis`）
- **分割线**: 顶部 0.5px（非第一行时显示）
- **可选性**: 可选

### 4.3 警示操作行

- **样式属性**: `data-样式="危险操作"`
- **字号**: 17px
- **颜色**: feedback_error (#F74C30)
- **对齐**: 水平居中
- **文本规则**: 仅单行，禁止换行，最大 **10 个字符**，超出截断（`text-overflow: ellipsis`）
- **分割线**: 顶部 0.5px
- **位置约束**: 始终位于主区块最后一行（所有常规操作行之后）
- **可选性**: 可选

### 4.4 取消行

- **样式属性**: `data-样式="常规操作"`
- **字号**: 17px
- **颜色**: text_primary
- **对齐**: 水平居中
- **文本规则**: 固定文案"取消"，不可自定义
- **分割线**: 无（独立区块）
- **可选性**: **不可移除**（始终存在）

## 5. 变体矩阵

操作数量(0-10) × 操作提示(有/无) × 警示操作(有/无) = **42 种变体**

> **约束规则**：常规操作 + 警示操作数量需 ≥ 1（至少有一行可执行操作）。

### ID 编码规则

`AS-{操作数}{T?}{D?}`
- **数字**（0-10）：常规操作数量
- **T**（可选）：有操作提示（标题行）
- **D**（可选）：有警示操作

### 完整变体列表

| 常规操作数 | 可能的变体 ID |
|-----------|-------------|
| 0 | AS-0D, AS-0TD（必须有警示操作） |
| 1-10 | AS-{n}, AS-{n}D, AS-{n}T, AS-{n}TD |

## 6. 交互行为

### 6.1 弹出/收起
- 从底部滑入，配合遮罩层淡入
- 点击遮罩层或"取消"按钮收起
- 收起时向下滑出，遮罩层淡出

### 6.2 操作反馈
- 点击常规操作行：执行对应操作并收起面板
- 点击警示操作行：可触发 Dialog 二次确认（如"确认删除？"），确认后执行操作；或直接执行并收起面板（视业务场景）
- 点击取消：关闭面板，不执行任何操作

### 6.3 组件构建器特有行为
- ActionSheet 为模态组件，拖入画布时自动创建模态覆盖层（`.modal-overlay`，半透明遮罩）
- 面板底部对齐覆盖层底部（`align-items: flex-end`）
- 覆盖层覆盖整个手机画框区域
- 侧边栏预览使用 0.5 缩放（`scale(0.5)`），仅展示面板部分不含遮罩

### 6.4 模态组件嵌套约束
- **禁止**与其他模态组件（Dialog、HalfScreenOverlay）相互嵌套
- ActionSheet 打开时不可再弹出另一个 ActionSheet、Dialog 或 HalfScreenOverlay

## 7. 布局规则

1. **主操作区块**与**取消区块**之间固定 **10px** 间距，间距区域由 outer 容器的 `#F3F3F7` 背景色填充露出
2. 面板总高度 = 主区块高度 + 10px + 取消行 56px + Home Bar 34px（系统安全区，组件外部）
3. 主区块高度 = 行数 × 56px（行数 = 标题行(0或1) + 常规操作行(0-10) + 警示行(0或1)）
4. 取消区块高度 = **56px**（仅取消行，Home Bar 由系统提供，不属于组件自身）
5. 分割线出现在**非第一行**的顶部（即第二行及以后的行在 `top: 0` 处绘制 0.5px 分割线）
6. 所有文本内容水平居中对齐（`text-align: center`）
7. 警示操作行始终位于主区块最后一行（所有常规操作行之后）
8. **滚动约束**：当主区块高度超过屏幕高度 60%（约 556px）时，主区块启用内部滚动（`overflow-y: auto`），取消区块始终固定可见

## 8. CSS 实现参考

### 8.1 outer 容器

```css
.actionsheet-outer {
    width: 428px;
    height: /* totalHeight，由JS动态设置 */;
    position: relative;
    background: var(--bg_middle_standard);  /* 间距区域的背景色 #F3F3F7 */
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    overflow: hidden;
}
```

### 8.2 主操作区块

```css
.actionsheet-main-block {
    position: absolute;
    left: 0;
    top: 0;
    width: 428px;
    height: /* mainBlockHeight，由JS动态设置 */;
    background: var(--bg_bottom_light);
}
```

### 8.3 操作行

```css
.actionsheet-row {
    width: 428px;
    height: 56px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### 8.4 分割线与文字样式

```css
.actionsheet-row .as-divider {
    position: absolute;
    left: 0;
    top: 0;
    width: 428px;
    height: 0.5px;
    background: var(--border_light);
}
.actionsheet-row .as-title-text {
    font-size: 14px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text_primary_light);
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 396px;
}
.actionsheet-row .as-action-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text_primary);
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 396px;
}
.actionsheet-row .as-danger-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--feedback_error);
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 396px;
}
```

### 8.5 取消区块

```css
.actionsheet-cancel-block {
    position: absolute;
    left: 0;
    top: /* mainBlockHeight + 10 */px;
    width: 428px;
    background: var(--bg_bottom_light);
}
.actionsheet-cancel-row {
    width: 428px;
    height: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.actionsheet-cancel-row .as-cancel-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text_primary);
    text-align: center;
}
```

---

## 9. 动效规范

### 9.1 入场动效
- **类型**：底部滑入（`translateY(100%) → translateY(0)`）
- **时长**：420ms
- **缓动曲线**：`cubic-bezier(0.32, 0.72, 0.35, 1)`
- **Token**：`--anim-actionsheet-in-duration` / `--anim-actionsheet-in-easing`

### 9.2 退场动效
- **类型**：底部滑出（`translateY(0) → translateY(100%)`）
- **时长**：300ms
- **缓动曲线**：`cubic-bezier(0.32, 0.72, 0.35, 1)`
- **Token**：`--anim-actionsheet-out-duration` / `--anim-actionsheet-out-easing`

### 9.3 蒙层动效
- **颜色**：`rgba(0, 0, 0, 0.50)`（`--color-overlay-dark`）
- **淡入**：250ms / ease-out（`--anim-overlay-in-*`）
- **淡出**：200ms / ease-in（`--anim-overlay-out-*`）
- 蒙层与面板动效**同步执行**

### 9.4 关闭方式
- 点击蒙层 → 收起面板（`closeOnOverlay: true`）
- 点击取消按钮 → 收起面板
- 下滑手势 → 收起面板

---

## 10. 组件联动

### 10.1 触发来源

| 触发场景 | 典型示例 |
|----------|---------|
| 用户需要从**多个操作中选择一个**时 | 分享到…、保存到…、发送给… |
| 用户执行**可能产生多种结果的操作**时 | 更多操作（编辑/删除/举报）、长按列表行弹出上下文菜单 |
| 用户需要**确认危险操作前展示选项**时 | 删除（含警示操作行）、退出群聊 |

> **通用规则**：任何可交互元素（按钮、图标、文字链、列表行、导航栏图标等）均可触发 ActionSheet。触发条件由业务逻辑决定，不限定特定组件类型。ActionSheet 适用于需要用户从多个操作中做选择的场景。

### 10.2 互斥约束
- **禁止**与 Dialog、HalfScreenOverlay 相互嵌套
- ActionSheet 打开时不可再弹出另一个模态组件