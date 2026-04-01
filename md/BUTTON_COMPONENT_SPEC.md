# 按钮 Button 组件设计规范

> **组件 ID**：`button`  
> **大类**：操作  
> **变体数量**：12 种（4尺寸 × 3类型）

## 1. 组件概述

按钮（Button）是移动端最基础的操作触发组件，用于引导用户执行主要或次要操作。按钮通过视觉层级（一级/二级/警示）和尺寸变化适配不同的交互场景与布局需求。

由 **4 种尺寸**（大/中/小/mini）× **3 种类型**（一级/二级/警示）排列组合生成，共 **12 种子组件**。每种子组件支持多种交互状态。

---

## 2. 组件分类

### 2.1 尺寸维度（Size）

| 标识 | 名称 | 宽度 | 高度 | 圆角 | 字号 | 字重 |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| S1 | 大 (Large) | 320px（满宽） | 48px | 14px | 17px | 500 (Medium) |
| S2 | 中 (Medium) | 169px（自适应） | 40px | 12px | 17px | 500 (Medium) |
| S3 | 小 (Small) | min 60px（自适应） | 32px | 16px | 14px | 400 (Regular) |
| S4 | Mini | min 42px（自适应） | 24px | 12px | 10px | 400 (Regular) |

### 2.2 类型维度（Type）

| 标识 | 名称 | 视觉特征 | 使用场景 |
|:-----|:-----|:---------|:---------|
| T1 | 一级 (Primary) | 实心填充蓝色背景，白色文字 | 页面主操作、确认、提交 |
| T2 | 二级 (Secondary) | 透明背景，灰色描边，黑色文字 | 辅助操作、取消 |
| T3 | 警示 (Error) | 透明背景，灰色描边，红色文字 | 删除、警告等高风险操作 |

---

## 3. 交互状态

### 3.1 状态矩阵

| 状态 | 大(S1) | 中(S2) | 小(S3) | Mini(S4) |
|:-----|:-------|:-------|:-------|:---------|
| 默认 (Default) | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 |
| 按下 (Pressed) | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 |
| 加载 (Loading) | ✅ 一级+二级 | ✅ 一级+二级 | ❌ | ❌ |
| 不可点击 (Disabled) | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 | ✅ 全部类型 |

> **加载态限制**：仅 **大(S1)**、**中(S2)** 尺寸的 **一级(T1)** 和 **二级(T2)** 类型按钮支持加载状态。小(S3)和Mini(S4)尺寸不支持加载态，警示(T3)类型不支持加载态。

### 3.2 状态切换规则

- **默认 → 按下**：手指触摸 / 鼠标按下时立即切换
- **默认 → 加载**：触发异步操作后，按钮进入加载态，显示旋转 spinner + 文案
- **默认 → 不可点击**：当前上下文不满足操作条件时，按钮置灰禁用
- 加载态期间按钮不可再次点击

---

## 4. 颜色规范

### 4.1 一级按钮 (Primary)

| 状态 | 背景色 | 文字色 | 描边 |
|:-----|:-------|:-------|:-----|
| 默认 | `#0099FF` | `#FFFFFF` | 无 |
| 按下 | `#008AE5` | `#FFFFFF` | 无 |
| 加载 | `#008AE5` | `#FFFFFF` | 无 |
| 不可点击 | `rgba(0, 153, 255, 0.50)` | `rgba(255, 255, 255, 0.50)` | 无 |

### 4.2 二级按钮 (Secondary)

| 状态 | 背景色 | 文字色 | 描边 |
|:-----|:-------|:-------|:-----|
| 默认 | 透明 | `rgba(0, 0, 0, 0.90)` | `rgba(60, 60, 67, 0.25)` 1px |
| 按下 | `rgba(204, 204, 204, 0.30)` | `rgba(0, 0, 0, 0.90)` | `rgba(60, 60, 67, 0.25)` 1px |
| 加载 | `rgba(204, 204, 204, 0.30)` | `rgba(0, 0, 0, 0.90)` | `rgba(60, 60, 67, 0.25)` 1px |
| 不可点击 | `rgba(204, 204, 204, 0.30)` | `rgba(0, 0, 0, 0.30)` | `rgba(60, 60, 67, 0.12)` 1px |

> 二级按钮不可点击态整体叠加 `opacity: 0.30`。

### 4.3 警示按钮 (Error)

| 状态 | 背景色 | 文字色 | 描边 |
|:-----|:-------|:-------|:-----|
| 默认 | 透明 | `#F74C30` | `rgba(60, 60, 67, 0.25)` 1px |
| 按下 | `rgba(204, 204, 204, 0.30)` | `#F74C30` | `rgba(60, 60, 67, 0.25)` 1px |
| 不可点击 | 透明 | `rgba(247, 76, 48, 0.30)` | `rgba(60, 60, 67, 0.12)` 1px |

---

## 5. 加载态规范

### 5.1 Spinner 样式

- 尺寸：19 × 19px
- 形状：3/4 弧形路径
- 描边宽度：2.5px，圆角端点 (stroke-linecap: round)
- 动画：线性旋转，1 秒/圈
- 一级按钮 Spinner 颜色：`rgba(255, 255, 255, 0.90)`
- 二级按钮 Spinner 颜色：`rgba(0, 0, 0, 0.40)`

### 5.2 布局

- Spinner 与文案水平排列，间距 4px
- 整体居中于按钮容器内

---

## 6. 变体矩阵

共 12 种子组件变体（4 尺寸 × 3 类型）：

| 编号 | 标识 | 尺寸 | 类型 | 状态数 |
|:-----|:-----|:-----|:-----|:-------|
| 1 | BTN-大-一级 | 大 (320×48) | 一级 Primary | 4（默认/按下/加载/不可点击） |
| 2 | BTN-大-二级 | 大 (320×48) | 二级 Secondary | 4（默认/按下/加载/不可点击） |
| 3 | BTN-大-警示 | 大 (320×48) | 警示 Error | 3（默认/按下/不可点击） |
| 4 | BTN-中-一级 | 中 (169×40) | 一级 Primary | 4（默认/按下/加载/不可点击） |
| 5 | BTN-中-二级 | 中 (169×40) | 二级 Secondary | 4（默认/按下/加载/不可点击） |
| 6 | BTN-中-警示 | 中 (169×40) | 警示 Error | 3（默认/按下/不可点击） |
| 7 | BTN-小-一级 | 小 (60×32) | 一级 Primary | 3（默认/按下/不可点击） |
| 8 | BTN-小-二级 | 小 (60×32) | 二级 Secondary | 3（默认/按下/不可点击） |
| 9 | BTN-小-警示 | 小 (60×32) | 警示 Error | 3（默认/按下/不可点击） |
| 10 | BTN-mini-一级 | mini (42×24) | 一级 Primary | 3（默认/按下/不可点击） |
| 11 | BTN-mini-二级 | mini (42×24) | 二级 Secondary | 3（默认/按下/不可点击） |
| 12 | BTN-mini-警示 | mini (42×24) | 警示 Error | 3（默认/按下/不可点击） |

---

## 7. 布局规则

- 按钮文字始终水平垂直居中
- 大按钮（S1）通常用于页面底部操作行，撑满可用宽度（左右 padding 由父容器控制）
- 中按钮（S2）通常用于操作行内与其他按钮并排
- 小按钮（S3）通常用于列表行右侧操作区域
- Mini 按钮（S4）用于紧凑空间内的轻量操作
- 字体统一使用 PingFang SC 字族

> **⚠️ 组件关联 — ActionCombo 操作组合**：操作组合组件（`ACTION_COMPONENT_SPEC.md`）中 A1-A5 变体的一级/二级按钮（52px 高度）与本组件的大尺寸(S1, `border-radius: 14px`) 共享相同的圆角规格。修改任一组件的大按钮圆角时，必须同步更新另一组件的 CSS、MD 和 JSON 文件。

---

## 8. CSS 实现代码块

### 8.1 按钮基础类

```css
.btn-comp {
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    cursor: pointer;
    user-select: none;
    box-sizing: border-box;
    transition: all 0.15s ease;
    white-space: nowrap;
    position: relative;
}
```

### 8.2 尺寸变体

```css
/* 大按钮 S1 */
.btn-comp.size-large {
    width: 320px;
    height: 48px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: 500;
}
/* 中按钮 S2 */
.btn-comp.size-medium {
    width: 169px;
    height: 40px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 500;
}
/* 小按钮 S3 */
.btn-comp.size-small {
    min-width: 60px;
    height: 32px;
    border-radius: 16px;
    font-size: 14px;
    font-weight: 400;
    padding: 0 16px;
}
/* Mini 按钮 S4 */
.btn-comp.size-mini {
    min-width: 42px;
    height: 24px;
    border-radius: 12px;
    font-size: 10px;
    font-weight: 400;
    padding: 0 11px;
}
```

### 8.3 一级按钮 Primary

```css
.btn-comp.type-primary.state-default {
    background: var(--color-brand-standard);
    color: var(--color-text-allwhite);
}
.btn-comp.type-primary.state-pressed {
    background: var(--color-brand-pressed);
    color: var(--color-text-allwhite);
}
.btn-comp.type-primary.state-loading {
    background: var(--color-brand-pressed);
    color: var(--color-text-allwhite);
}
.btn-comp.type-primary.state-disabled {
    background: rgba(0, 153, 255, 0.50);
    color: rgba(255, 255, 255, 0.50);
    cursor: not-allowed;
}
```

### 8.4 二级按钮 Secondary

```css
.btn-comp.type-secondary.state-default {
    background: transparent;
    border: 1px solid var(--color-border-stroke);
    color: var(--color-text-primary);
}
.btn-comp.type-secondary.state-pressed {
    background: var(--color-fill-pressed-brand);
    border: 1px solid var(--color-border-stroke);
    color: var(--color-text-primary);
}
.btn-comp.type-secondary.state-loading {
    background: var(--color-fill-pressed-brand);
    border: 1px solid var(--color-border-stroke);
    color: var(--color-text-primary);
}
.btn-comp.type-secondary.state-disabled {
    background: var(--color-fill-pressed-brand);
    border: 1px solid var(--color-border-disabled);
    color: rgba(0, 0, 0, 0.30);
    opacity: 0.30;
    cursor: not-allowed;
}
```

### 8.5 警示按钮 Error

```css
.btn-comp.type-error.state-default {
    background: transparent;
    border: 1px solid var(--color-border-stroke);
    color: var(--color-feedback-error);
}
.btn-comp.type-error.state-pressed {
    background: var(--color-fill-pressed-brand);
    border: 1px solid var(--color-border-stroke);
    color: var(--color-feedback-error);
}
.btn-comp.type-error.state-disabled {
    background: transparent;
    border: 1px solid var(--color-border-disabled);
    color: rgba(247, 76, 48, 0.30);
    cursor: not-allowed;
}
```

### 8.6 加载动画

```css
.btn-spinner {
    width: 19px;
    height: 19px;
    margin-right: 4px;
    animation: btn-spin 1s linear infinite;
}
@keyframes btn-spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
```

---

## 9. 组件联动

### 9.1 可触发的模态组件

| 触发目标 | 场景 | 说明 |
|----------|------|------|
| Dialog（对话框） | 确认类操作 | 如"删除确认""退出确认"，点击按钮后弹出居中对话框 |
| ActionSheet（操作面板） | 多选项操作 | 如"分享到…""更多操作"，点击按钮后弹出底部操作面板 |
| HalfScreenOverlay（半屏浮层） | 复杂操作面板 | 如"筛选设置""编辑表单"，点击按钮后弹出半屏浮层 |

### 9.2 被嵌套场景

| 外层组件 | 说明 |
|----------|------|
| ActionCombo（操作组合） | A1-A5 变体内嵌一级/二级按钮，共享圆角14px规格 |
| Card（卡片） | C5列表行按钮、C6大按钮均为 Button 变体 |
| HalfScreenOverlay（半屏浮层） | 半屏浮层底部操作区可嵌入按钮 |
