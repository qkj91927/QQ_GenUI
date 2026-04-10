# 轻提示 Toast · 组件设计规范

> **组件 ID**：`toast`  
> **大类**：操作  
> **变体数量**：5 种（T1-T5）

Toast 是一种短暂性的非阻断式反馈提示组件，用于告知用户操作结果或当前状态，无需用户交互即可自动消失。

---

## 1. 组件概述

| 编号 | 名称 | 构成 | 出现位置 | 显示时长 |
|------|------|------|---------|---------|
| T1 | 加载中 | `loading.svg`（旋转）+ 文字 | 页面正中央 | 手动消失（加载完成后） |
| T2 | 成功 | `tick_circle.svg` + 文字 | 页面正中央 | **2秒** |
| T3 | 失败 | `caution_filled.svg` + 文字 | 页面正中央 | **2秒** |
| T4 | 中性文字 | 纯文字 | 页面正中央 | **2秒** |
| T5 | 带操作 | `tick_circle.svg` + 文字 + 操作文字链 | 页面底部上方 64px | **3秒（点击操作立即消失）** |

---

## 2. 组件结构

### T1 加载中

```
┌──────────────────────────────────────┐  44px
│  [loading.svg] 加载中                 │
└──────────────────────────────────────┘
 ←——————— inline-flex 自适应 ———————→
```

左：`loading.svg` 24×24px，颜色 `--icon_allwhite_primary`（`#ffffff`），旋转动画；右：文字 `--text_allwhite_primary`；`gap: 4px`；`padding: 12px 16px`

### T2 成功

```
┌──────────────────────────────────────┐  44px
│  [tick_circle.svg] 成功提示文案        │
└──────────────────────────────────────┘
 ←——————— inline-flex 自适应 ———————→
```

左：`tick_circle.svg` 24×24px，颜色 `--icon_allwhite_primary`（`#ffffff`）；右：文字 `--text_allwhite_primary`；`gap: 4px`；`padding: 12px 16px`

### T3 失败

```
┌──────────────────────────────────────┐  44px
│  [caution_filled.svg] 失败提示文案     │
└──────────────────────────────────────┘
 ←——————— inline-flex 自适应 ———————→
```

左：`caution_filled.svg` 24×24px，颜色 `--icon_allwhite_primary`（`#ffffff`）；右：文字 `--text_allwhite_primary`；`gap: 4px`；`padding: 12px 16px`

### T4 中性文字

```
┌──────────────────────────────────────┐  44px
│  Toast中性提示文案                     │
└──────────────────────────────────────┘
 ←——————— inline-flex 自适应 ———————→
```

仅文字，颜色 `--text_allwhite_primary`；`padding: 12px 16px`

### T5 带操作

```
┌────────────────────────────────────────┐  52px
│  [tick_circle.svg] 带操作Toast提示文案          撤销  │
└────────────────────────────────────────┘
 ←——————————————————— 396px ————————————→
```

左侧：`tick_circle.svg` 24×24px，颜色 `--icon_allwhite_primary`（`#ffffff`）+ 主文案 `--text_allwhite_primary`（`gap: 4px`）；右侧：操作文字链，颜色 `#4db8ff`（无对应 token，Toast 专用静态色）；`justify-content: space-between`；`padding: 12px 16px`；**出现位置：底部上方 64px；点击操作文字链后 Toast 立即消失**

---

## 3. 视觉规格

### 3.1 容器样式

| 属性 | 值 | Token |
|------|------|-------|
| 背景色 | `rgba(0, 0, 0, 0.60)` | `--bg_toast_nonopaque` |
| 毛玻璃效果 | `backdrop-filter: blur(20px)` | — |
| 圆角 | `16px` | — |
| T1-T4 高度 | `44px` | — |
| T5 高度 | `52px` | — |
| T1-T4 宽度 | 自适应内容（`inline-flex`） | — |
| T5 宽度 | `396px`（固定宽度） | — |
| 内边距 | `12px 16px` | — |

### 3.2 文字规格

| 元素 | 字号 | 字重 | 行高 | 颜色 | Token |
|------|------|------|------|------|-------|
| 主文案 | 16px | Regular 400 | 20px（T5 为 22px） | `#ffffff` | `--text_allwhite_primary` |
| 操作文字链（T5） | 14px | Regular 400 | 22px | `#4db8ff` | 无对应 token，Toast 专用静态色 |

### 3.3 图标规格

| 变体 | 图标文件 | 尺寸 | 颜色 | Token | 特殊效果 |
|------|---------|------|------|-------|---------|
| T1 加载中 | `icons/loading.svg` | 24×24px | `#ffffff` | `--icon_allwhite_primary` | CSS旋转动画 `animation: toast-spin 1s linear infinite` |
| T2 成功 | `icons/QUI_24_icons/tick_circle.svg` | 24×24px | `#ffffff` | `--icon_allwhite_primary` | — |
| T3 失败 | `icons/QUI_24_icons/caution_filled.svg` | 24×24px | `#ffffff` | `--icon_allwhite_primary` | — |
| T5 带操作 | `icons/QUI_24_icons/tick_circle.svg` | 24×24px | `#ffffff` | `--icon_allwhite_primary` | — |

图标与文字间距：**4px**（`gap: 4px`）

---

## 4. 出现位置

| 变体 | 位置 | CSS 实现 |
|------|------|---------|
| T1-T4 | 页面正中央 | `position:fixed; left:50%; top:50%; transform:translate(-50%,-50%)` |
| T5 | 页面底部上方 64px | `position:fixed; left:50%; bottom:64px; transform:translateX(-50%)` |

---

## 5. 动画规范

### 5.1 T1-T4（页面正中央）

| 阶段 | 时长 | 曲线 | 属性 |
|------|------|------|------|
| 入场 | 250ms | ease | `opacity: 0→1`，`scale: 0.92→1` |
| 停留 | 2000ms | — | — |
| 出场 | 250ms | ease | `opacity: 1→0`，`scale: 1→0.92` |

### 5.2 T5（底部）

| 阶段 | 时长 | 曲线 | 属性 |
|------|------|------|------|
| 入场 | 300ms | ease | `opacity: 0→1`，`translateY: 8px→0` |
| 停留 | 3000ms | — | — |
| 出场 | 300ms | ease | `opacity: 1→0`，`translateY: 0→8px` |

### 5.3 T1 加载图标旋转

```css
@keyframes toast-spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}
/* 使用 */
animation: toast-spin 1s linear infinite;
```

---

## 6. 触发场景

Toast 由业务逻辑在以下操作完成后程序触发，**不由用户直接操作**：

| 变体 | 典型触发场景 |
|------|------------|
| T1 加载中 | 提交表单、发送消息、上传文件、网络请求等异步操作进行中 |
| T2 成功 | 操作完成后的正向反馈：发送成功、保存成功、收藏成功、复制成功 |
| T3 失败 | 操作失败后的负向反馈：网络错误、上传失败、操作超时 |
| T4 中性文字 | 系统提示、状态通知等中性信息：已达上限、功能暂不可用 |
| T5 带操作 | 可撤销的操作完成后：删除成功（可撤销）、移动成功（可撤销） |

> **与 Dialog 的区别**：Dialog 用于需要用户明确确认的决策性操作；Toast 用于无需用户确认的轻量反馈，不阻断用户操作流。

### 组件联动关系

| 联动方向 | 说明 |
|---------|------|
| Button → T1 | 点击一级按钮触发异步操作时，按钮进入 loading 态同时显示 T1 |
| T1 → T2/T3 | 异步操作完成/失败后，T1 立即替换为 T2 或 T3 |
| 列表行操作 → T5 | 列表滑动删除、移动等可撤销操作完成后，底部显示 T5 |
| Dialog 操作按钮 → T2/T3 | 对话框中确认操作执行完成后，Toast 作为操作结果反馈 |

---

## 7. 使用规范

1. **非阻断式**：Toast 出现期间不阻止用户操作，无蒙层
2. **同时只显示一个**：新 Toast 出现时，前一个 Toast 立即消失
3. **T1 加载中**：由业务逻辑控制关闭，不自动消失；加载完成后应立即切换为 T2/T3
4. **T5 带操作**：操作文字链（如"撤销"）点击后立即关闭 Toast 并执行操作，不等待 3 秒自动消失
5. **文案长度**：单行不超过 16 个字，T5 主文案不超过 12 个字

---

## 8. CSS 实现代码块

```css
/* Toast 容器 */
.toast {
    position: fixed;
    z-index: 9999;
    background: var(--bg_toast_nonopaque, rgba(0, 0, 0, 0.60));
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 16px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 12px 16px;
    font-family: 'PingFang SC', sans-serif;
    pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease;
}
/* T1-T4：正中央 */
.toast.center {
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%) scale(1);
}
.toast.center.hidden {
    opacity: 0;
    transform: translate(-50%, -50%) scale(0.92);
}
/* T5：底部 */
.toast.bottom {
    left: 50%;
    bottom: 64px;
    transform: translateX(-50%) translateY(0);
    width: 396px;
    height: 52px;
    justify-content: space-between;
    pointer-events: auto;
    transition: opacity 0.3s ease, transform 0.3s ease;
}
.toast.bottom.hidden {
    opacity: 0;
    transform: translateX(-50%) translateY(8px);
}
/* 文字 */
.toast-text {
    font-size: 16px;
    font-weight: 400;
    line-height: 20px;
    color: var(--text_allwhite_primary, #ffffff);
    white-space: nowrap;
}
.toast-text-t5 {
    line-height: 22px;
}
/* 操作文字链（无对应 token，Toast 专用静态色） */
.toast-action {
    font-size: 14px;
    font-weight: 400;
    line-height: 22px;
    color: #4db8ff;
    white-space: nowrap;
    cursor: pointer;
}
/* 图标白化（Toast 深色背景上使用） */
.toast-icon {
    display: block;
    width: 24px;
    height: 24px;
    filter: brightness(0) invert(1);
}
/* 加载旋转 */
@keyframes toast-spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}
.toast-loading-icon {
    animation: toast-spin 1s linear infinite;
}
```
