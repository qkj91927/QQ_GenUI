# 菜单 Menu · 组件设计规范

> **组件 ID**：`menu`  
> **大类**：操作  
> **变体数量**：15 种（有图标/无图标/有勾选 × 2-6项）

## 1. 概述

菜单（Menu）是一种伴随式非模态浮层组件，用于在用户点击或长按触发元素后，在触发点附近弹出一组可选操作项。菜单不覆盖全屏、不带遮罩层，用户可直接与页面其他区域交互来关闭菜单。

**适用场景：**
- 页面右上角"更多"按钮触发的操作菜单
- 长按内容弹出的上下文操作
- 工具栏图标触发的功能列表

---

## 2. 组件结构

菜单由以下部分组成：

| 层级 | 元素 | 说明 |
|------|------|------|
| 容器 | Menu Container | 白色圆角容器，承载所有菜单项 |
| 行项 | Menu Item (Row) | 每一行为一个可点击的菜单选项 |
| 图标 | Icon (可选) | 位于选项左侧的 24×24 图标 |
| 文本 | Label | 菜单项文本标签 |

---

## 3. 子组件类型

### A. 有图标菜单 (With Icon)

- **行高：** 52px
- **图标尺寸：** 24×24px
- **图标位置：** left: 20px, 垂直居中
- **文本位置：** left: 60px, 垂直居中
- **支持选项数：** 2-6 个

### B. 无图标菜单 (Without Icon)

- **行高：** 52px
- **文本位置：** left: 20px, 垂直居中
- **支持选项数：** 2-6 个

### C. 有勾选菜单 (With Checkmark)

- **行高：** 52px
- **文本位置：** left: 20px, 垂直居中
- **勾选图标：** `icons/tick.svg`（20×20px 蓝色勾选标记 `#0099FF`），位于行右侧 right: 20px, 垂直居中
- **支持选项数：** 2-6 个
- **交互规则：** 单选且互斥 — 同一时刻仅一个选项处于选中态（显示勾选图标），其余选项无勾选图标
- **触发场景：** 卡片式列表中点击 **R2（辅助信息+下拉菜单）** 时弹出此类菜单，用户选择后菜单关闭，R2 的辅助信息文字更新为选中项

---

## 4. 设计 Token

| Token | 值 | 说明 |
|-------|-----|------|
| Container Width | 180px | 菜单容器固定宽度 |
| Container Radius | 12px | 容器圆角 |
| Container Background | #FFFFFF | 白色背景 |
| Container Shadow | 0 8px 32px rgba(0,0,0,0.12) | 浮层投影 |
| Row Height (With Icon) | 52px | 有图标时的行高 |
| Row Height (No Icon) | 52px | 无图标时的行高 |
| Row Height (With Checkmark) | 52px | 有勾选时的行高 |
| Icon Size | 24×24px | 图标尺寸 |
| Icon Left Padding | 20px | 图标左侧间距 |
| Checkmark Size | 20×20px | 勾选图标尺寸 |
| Checkmark Right Padding | 20px | 勾选图标右侧间距 |
| Checkmark Color | #0099FF | 勾选图标颜色（选中态） |
| Text Left (With Icon) | 60px | 有图标时文本左侧位置 |
| Text Left (No Icon) | 20px | 无图标时文本左侧位置 |
| Text Left (With Checkmark) | 20px | 有勾选时文本左侧位置 |
| Text Font Size | 17px | 文本字号 |
| Text Font Weight | 400 (Regular) | 文本字重 |
| Text Color | rgba(0, 0, 0, 0.90) | 文本颜色 |
| Text Font Family | PingFang SC | 字体 |

---

## 5. 交互规范

### 5.1 出现方式

菜单为**伴随式**组件，出现在触发元素的上方或下方 **6px** 位置：
- 优先在触发元素**下方**展示
- 当下方空间不足时，自动切换到触发元素**上方**
- 菜单与触发元素之间保持 6px 间距

### 5.2 非模态特性

- **无遮罩层（mask）：** 菜单出现时不覆盖背景半透明遮罩
- **背景可交互：** 用户可直接点击菜单外的任意区域来关闭菜单
- **不阻断操作：** 菜单不会阻止用户与页面其他元素交互

### 5.3 动效

| 属性 | 出现 | 消失 |
|------|------|------|
| opacity | 0 → 1 | 1 → 0 |
| transform | scale(0.9) → scale(1) | scale(1) → scale(0.9) |
| duration | 200ms | 150ms |
| easing | ease-out | ease-in |
| transform-origin | 触发点方向 | 触发点方向 |

### 5.4 关闭方式

- 点击菜单项（执行操作后关闭）
- 点击菜单外任意区域
- 按下 ESC 键（桌面端）
- 页面滚动时自动关闭

---

## 6. 变体矩阵

### 6.1 编码规则

`{类型}-{选项数量}`

- **I**: 有图标 (Icon)
- **NI**: 无图标 (No Icon)
- **C**: 有勾选 (Checkmark)
- **2-6**: 选项数量

### 6.2 完整变体表

| # | 变体 ID | 类型 | 选项数 | 容器高度 |
|---|---------|------|--------|----------|
| 1 | I-2 | 有图标 | 2 | 104px |
| 2 | I-3 | 有图标 | 3 | 156px |
| 3 | I-4 | 有图标 | 4 | 208px |
| 4 | I-5 | 有图标 | 5 | 260px |
| 5 | I-6 | 有图标 | 6 | 312px |
| 6 | NI-2 | 无图标 | 2 | 104px |
| 7 | NI-3 | 无图标 | 3 | 156px |
| 8 | NI-4 | 无图标 | 4 | 208px |
| 9 | NI-5 | 无图标 | 5 | 260px |
| 10 | NI-6 | 无图标 | 6 | 312px |
| 11 | C-2 | 有勾选 | 2 | 104px |
| 12 | C-3 | 有勾选 | 3 | 156px |
| 13 | C-4 | 有勾选 | 4 | 208px |
| 14 | C-5 | 有勾选 | 5 | 260px |
| 15 | C-6 | 有勾选 | 6 | 312px |

**共 15 种子组件 = 3 (类型: 有图标/无图标/有勾选) × 5 (选项数量)**

### 6.3 可配置性（控件对应关系）

组件构建器和变体矩阵中均提供以下控件，且行为严格一致：

| 控件类型 | 控件名称 | 选项 | 对应属性 | 默认值 |
|---------|---------|------|---------|--------|
| 分段选择器 | 类型 | 有图标 / 无图标 / 有勾选 | menuType | 有图标 |
| 分段选择器 | 选项数量 | 2 / 3 / 4 / 5 / 6 | optionCount | 3 |

---

## 7. 与其他组件的区别

| 维度 | 菜单 Menu | 操作面板 ActionSheet | 对话框 Dialog |
|------|-----------|---------------------|---------------|
| 触发方式 | 点击/长按 | 用户操作触发 | 系统/用户触发 |
| 出现位置 | 触发元素旁 6px | 屏幕底部 | 屏幕居中 |
| 模态性 | 非模态 | 模态（有遮罩） | 模态（有遮罩） |
| 背景交互 | 可交互 | 不可交互 | 不可交互 |
| 宽度 | 固定 180px | 全屏 428px | 固定 296px |
| 内容类型 | 纯操作选项 | 操作选项+取消 | 标题+正文+按钮 |

---

## 8. 设计参考

本组件参考了以下主流设计系统：

- **Apple Human Interface Guidelines** — Menus (iOS/iPadOS)
- **Material Design 3** — Menus
- **WeChat Design System** — 操作菜单

遵循移动端菜单的核心设计原则：紧凑、伴随、非阻断。

---

## 9. CSS 实现代码块

### 9.1 菜单容器

```css
.menu-outer {
    width: 180px;
    background: var(--bg-item);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
}
```

### 9.2 菜单行

```css
.menu-row {
    width: 180px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
}
.menu-row.with-icon,
.menu-row.no-icon {
    height: 52px;
}
```

### 9.3 菜单元素

```css
.menu-icon {
    width: 24px;
    height: 24px;
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
}
.menu-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text-primary);
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}
.menu-text.with-icon {
    left: 60px;
}
.menu-text.no-icon {
    left: 20px;
}
.menu-check {
    width: 20px;
    height: 20px;
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
}
```
