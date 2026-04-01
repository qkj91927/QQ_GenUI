# 操作组合 ActionCombo 组件设计规范 (ActionCombo Component Spec)

> **组件 ID**：`action`  
> **大类**：操作  
> **变体数量**：13 种（A1-A8 按钮型 + B1-B5 文字链型）

本文件定义了移动端操作组合组件的系统化构建逻辑、属性约束及 UI 规范。操作组合用于页面底部或表单尾部的操作区域，分为 **操作组合 (A)** 和 **辅助操作组合 (B)** 两大类。

---

## 1. 组件概述 (Overview)

操作行是半屏浮层、弹窗、表单等场景底部的核心交互区域。它由两类子组件构成：

- **A. 操作行 (Action Bar)**：以 **Button 按钮** 为主的操作区域，承载主要交互行为（确认、取消、提交等）。
- **B. 辅助操作行 (Auxiliary Action Bar)**：以 **Action 文字链** 为主的辅助操作区域，承载次要交互（协议勾选、文字链跳转等）。

**核心区别：**
- **Button (按钮)**：圆角胶囊型实体按钮，具有明确的视觉层级（一级/二级），适用于主操作。
- **Action (文字链)**：纯文字链接，无背景色，颜色为 `text_link`，适用于辅助操作。

---

## 2. 属性定义 (Properties)

### 2.1 A. 操作行 (Action Bar) — 8 种变体

| 标识 | 名称 | 构成 | 高度 | 来源 Frame |
| :--- | :--- | :--- | :--- | :--- |
| A1 | 双按钮（二级+一级） | 1 个二级按钮 + 1 个一级按钮，等宽排列 | 84px | 1_9731 |
| A2 | 三按钮（二级+二级+一级） | 2 个二级按钮 + 1 个一级按钮，等宽排列 | 84px | 1_9731 |
| A3 | 单按钮（一级满宽） | 1 个一级按钮，满宽 | 84px | 1_9731 |
| A4 | 单按钮（二级满宽） | 1 个二级按钮，满宽 | 84px | 1_9731 |
| A5 | 四宫格操作 | 4 个图标+文字操作项，等宽排列 | 72px | 1_9731 |
| A6 | 六图标横排 | 6 个纯图标按钮，横向均匀分布 | 48px | 3462_5192 |
| A7 | 四图标文字行 | 4 个图标+文字操作项，等宽排列 | 48px | 3467_2977 |
| A8 | 操作+勾选+按钮 | 文字操作 + 2 个勾选项 + 小一级按钮 | 72px | 1_9731 |

### 2.2 B. 辅助操作行 (Auxiliary Action Bar) — 5 种变体

| 标识 | 名称 | 构成 | 高度 | 来源 Frame |
| :--- | :--- | :--- | :--- | :--- |
| B1 | 勾选+文案+文字链 | Checkbox + 辅助文案 + 文字链 | 36px | 1_9746 |
| B2 | 辅助文案+文字链 | 辅助说明文案 + 文字链 | 36px | 1_9746 |
| B3 | 单 Action | 1 个居中 Action 文字链 | 36px | 1_9746 |
| B4 | 双 Action | 2 个 Action 文字链 + 分隔线 | 36px | 1_9746 |
| B5 | 三 Action | 3 个 Action 文字链 + 分隔线 | 36px | 1_9746 |

---

## 3. 按钮属性详解 (Button Properties)

> **⚠️ 组件关联**：操作组合中 A1-A5 的一级/二级按钮（52px 高度）与独立 Button 组件的大尺寸(S1) 共享相同的圆角值 `14px`。修改任一组件的大按钮圆角时，必须同步更新另一组件。

### 3.1 一级按钮 (Primary Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--品牌色-brand_standard, #0099FF)` |
| 文字色 | `var(--文本色-text_allwhite, white)` |
| 字号 | 17px (大) / 14px (小) |
| 字重 | 600 (大) / 500 (小) |
| 高度 | 52px (大) / 36px (小) |
| 圆角 | 14px (大) / 9999px (小) |
| Figma 属性 | `data-图标="false" data-尺寸="大/小" data-状态="默认" data-类型="一级"` |

### 3.2 二级按钮 (Secondary Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--透明填充色-Tertiary, rgba(118, 118, 128, 0.12))` |
| 文字色 | `var(--文本色-text_primary, rgba(0, 0, 0, 0.90))` |
| 字号 | 17px |
| 字重 | 600 |
| 高度 | 52px |
| 圆角 | 14px |
| Figma 属性 | `data-图标="false" data-尺寸="大" data-状态="默认" data-类型="二级"` |

### 3.3 图标按钮 (Icon Button)
| 属性 | 值 |
| :--- | :--- |
| 背景色 | `var(--透明填充色-Tertiary, rgba(118, 118, 128, 0.12))` |
| 尺寸 | 52×52px |
| 图标尺寸 | 24×24px |
| 圆角 | 999px |
| Figma 属性 | `data-图标="true" data-尺寸="大" data-状态="默认" data-类型="二级"` |

---

## 4. Action 文字链属性详解 (Action Text Link Properties)

| 属性 | 值 |
| :--- | :--- |
| 字号 | 14px |
| 字重 | 500 |
| 颜色 | `var(--文本色-text_link, #214CA5)` |
| 分隔线 | 1×14px, `rgba(0, 0, 0, 0.08)`, 水平间距 8px |

### 辅助文案
| 属性 | 值 |
| :--- | :--- |
| 字号 | 14px |
| 字重 | 400 |
| 颜色 | `var(--文本色-text_secondary, rgba(60, 60, 67, 0.76))` |

### 勾选框 (Checkbox)
| 属性 | 值 |
| :--- | :--- |
| 尺寸 | 16×16px (B1) / 20×20px (A7) |
| 间距 | 右侧 4px |
| Figma 属性 | `data-尺寸="大" data-状态="未选中" data-类型="普通型"` |

---

## 5. 布局规格 (Layout Specs)

### A. 操作行布局
| 属性 | 值 |
| :--- | :--- |
| 容器宽度 | 428px (适配 iOS 标准宽度) |
| 定位方式 | `position: fixed; bottom: 34px; z-index: 10`（默认吸底，固定在 HomeBar 上方 34px 处） |
| 内边距 | A1-A4: `16px 24px`; A5: `16px`; A6: `12px 32px`; A7: `12px 16px`; A8: `16px` |
| 按钮间距 | 12px |
| A5 每项宽度 | 99px |
| A6 图标间距 | 68px |
| A7 每项宽度 | 99px |

### B. 辅助操作行布局
| 属性 | 值 |
| :--- | :--- |
| 容器宽度 | 428px |
| 行高 | 36px |
| 内边距 | `0 16px` |
| 对齐方式 | 居中 (center) |

---

## 6. 设计 Token (Design Tokens)

| Token 名称 | CSS 变量 | 值 |
| :--- | :--- | :--- |
| 品牌色 | `--品牌色-brand_standard` | `#0099FF` |
| 文字白 | `--文本色-text_allwhite` | `white` |
| 主文字 | `--文本色-text_primary` | `rgba(0, 0, 0, 0.90)` |
| 次文字 | `--文本色-text_secondary` | `rgba(60, 60, 67, 0.76)` |
| 链接色 | `--文本色-text_link` | `#214CA5` |
| 透明填充 | `--透明填充色-Tertiary` | `rgba(118, 118, 128, 0.12)` |
| 分隔线色 | — | `rgba(0, 0, 0, 0.08)` |

---

## 7. 资源映射 (Asset Mapping)

### Frame 1_9731 (操作行 A1-A5, A8)
| 文件 | 用途 |
| :--- | :--- |
| `2.svg` | 图标按钮内图标 (24×24) |
| `6.svg` | 四宫格操作项图标 (24×24) |
| `Checkbox.svg` | 勾选框未选中态 (SVG 固有尺寸 20×20，A8 渲染为 20×20) |
| `Checkbox_filled.svg` | 勾选框选中态 (SVG 固有尺寸 20×20，A8 渲染为 20×20) |

### Frame 3462_5192 (操作行 A6)
| 文件 | 用途 |
| :--- | :--- |
| `6.svg` | 图标按钮 (24×24) |

### Frame 3467_2977 (操作行 A7)
| 文件 | 用途 |
| :--- | :--- |
| `4.svg` | 图标+文字操作项图标 (24×24) |

### Frame 1_9746 (辅助操作行 B)
| 文件 | 用途 |
| :--- | :--- |
| `Checkbox.svg` | Checkbox 勾选框未选中态 (SVG 固有尺寸 20×20，B1 通过 CSS 缩放为 16×16) |
| `Checkbox_filled.svg` | Checkbox 勾选框选中态 (SVG 固有尺寸 20×20，B1 通过 CSS 缩放为 16×16) |
| `3.svg` | Action 分隔线 SVG |

> **注意**: `Checkbox.svg` 和 `Checkbox_filled.svg` 的 SVG 固有尺寸必须一致（均为 20×20），以确保切换选中/未选中状态时不会改变图标大小。不同场景通过 CSS `width`/`height` 控制渲染尺寸。

---

## 8. 使用场景 (Usage Scenarios)

| 场景 | 推荐变体 |
| :--- | :--- |
| 半屏浮层确认操作 | A1 (双按钮) 或 A3 (单一级按钮) |
| 表单提交 | A3 (单一级按钮) + B1 (勾选+协议文案) |
| 多操作选择 | A2 (三按钮) |
| 分享/收藏等快捷操作 | A5 (四宫格) |
| 底部辅助链接 | B3-B5 (Action 文字链) |
| 协议勾选+说明 | B1 (勾选+文案+文字链) |

---

## 9. CSS 实现代码块

### 9.1 操作容器

```css
.action-container {
    width: 428px;
    display: flex;
    flex-direction: column;
    position: fixed;
    bottom: 34px;
    z-index: 10;
}
```

### 9.2 按钮行 (A 类)

```css
.action-button-row {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 16px 24px;
    background: transparent;
    width: 428px;
    box-sizing: border-box;
    gap: 12px;
}
.action-button-row.mixed-row {
    padding: 16px;
    justify-content: space-between;
}
```

### 9.3 按钮样式

```css
.action-btn-primary {
    height: 52px;
    background: var(--color-brand-standard);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    font-weight: 600;
    color: var(--color-text-allwhite);
    flex: 1;
    min-width: 0;
}
.action-btn-primary.fixed-width {
    flex: 0 0 auto;
    padding: 0 24px;
}
.action-btn-primary.small {
    height: 36px;
    font-size: 14px;
    font-weight: 500;
    padding: 0 14px;
    flex: 0 0 72px;
}
.action-btn-secondary {
    height: 52px;
    background: var(--color-fill-tertiary);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    font-weight: 600;
    color: var(--color-text-primary);
    flex: 1;
    min-width: 0;
}
.action-icon-btn {
    width: 52px;
    height: 52px;
    background: var(--color-fill-tertiary);
    border-radius: 999px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.action-icon-btn img {
    width: 24px;
    height: 24px;
}
```

### 9.4 宫格操作项 (A6) - 绝对定位

```css
/* A6: 四宫格操作 (72px) */
.action-button-row.grid-row {
    position: relative;
    width: 428px;
    height: 72px;
    background: transparent;
    padding: 0;
}
.action-grid-item {
    position: absolute;
    width: 99px;
    height: 72px;
    top: 0px;
}
.action-grid-item:nth-child(1) { left: 16px; }
.action-grid-item:nth-child(2) { left: 115px; }
.action-grid-item:nth-child(3) { left: 214px; }
.action-grid-item:nth-child(4) { left: 313px; }
.action-grid-item-inner {
    position: absolute;
    width: 34px;
    height: 52px;
    left: 32.5px;
    top: 10px;
}
.action-grid-item-inner img {
    position: absolute;
    left: 5px;
    top: 0px;
    width: 24px;
    height: 24px;
}
.action-grid-item-inner span {
    position: absolute;
    left: 0px;
    top: 28px;
    width: 34px;
    text-align: center;
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-primary);
}
```

### 9.5 六图标横排 (A7) 和 四图标文字行 (A8)

```css
/* A7: 六图标横排 - 使用绝对定位精确还原 Figma */
.action-button-row.icon-6-row {
    position: relative;
    width: 428px;
    height: 48px;
    background: transparent;
    padding: 0;
}
.action-icon-btn-24 {
    position: absolute;
    top: 12px;
    width: 24px;
    height: 24px;
}
.action-icon-btn-24 img {
    width: 24px;
    height: 24px;
}
/* 6个图标精确位置 */
.action-icon-btn-24:nth-child(1) { left: 32px; }
.action-icon-btn-24:nth-child(2) { left: 100px; }
.action-icon-btn-24:nth-child(3) { left: 168px; }
.action-icon-btn-24:nth-child(4) { left: 236px; }
.action-icon-btn-24:nth-child(5) { left: 304px; }
.action-icon-btn-24:nth-child(6) { left: 372px; }

/* A8: 四图标文字行 */
.action-button-row.icon-text-4-row {
    padding: 12px 16px;
    height: 48px;
    gap: 0;
    justify-content: flex-start;
}
.action-icon-text-item {
    width: 99px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
}
.action-icon-text-item img {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
}
.action-icon-text-item span {
    font-size: 17px;
    font-weight: 400;
    color: var(--文本色-text_primary, var(--color-text-primary));
    text-align: center;
}
```

### 9.6 混合行与勾选项 (A9)

```css
.action-mixed-left {
    display: flex;
    align-items: center;
    gap: 24px;
}
.action-mixed-left .action-label {
    font-size: 17px;
    font-weight: 400;
    color: var(--文本色-text_primary, var(--color-text-primary));
}
.action-checkbox-item {
    display: flex;
    align-items: center;
    gap: 4px;
}
.action-checkbox-item img {
    width: 20px;
    height: 20px;
}
.action-checkbox-item span {
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-primary);
}
```

### 9.7 辅助操作行 (B 类)

```css
.action-row {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 36px;
    padding: 0 16px;
    background: transparent;
    width: 428px;
    gap: 0;
}
.action-row .action-link {
    font-size: 14px;
    font-weight: 500;
    color: var(--文本色-text_link, var(--color-text-link));
    white-space: nowrap;
}
.action-row .action-separator {
    width: 1px;
    height: 14px;
    background: var(--color-separator);
    margin: 0 8px;
    flex-shrink: 0;
}
.action-row .action-checkbox {
    width: 16px;
    height: 16px;
    margin-right: 4px;
    flex-shrink: 0;
}
.action-row .action-text {
    font-size: 14px;
    color: var(--文本色-text_secondary, var(--color-text-secondary));
}
.action-row .action-textlink {
    font-size: 14px;
    color: var(--文本色-text_link, var(--color-text-link));
}
```

---

## 10. 组件联动

### 10.1 A 类按钮型操作组合
- A1-A4 中的一级/二级按钮点击可触发 **Dialog（对话框）** 或 **ActionSheet（操作面板）**
- A5-A7 中的图标按钮点击执行独立操作（如分享、收藏）
- A8 中的小一级按钮可触发确认对话框

### 10.2 B 类文字链型
- B1 中的 Textlink 可跳转到协议详情页
- B3-B5 中的 Action 文字链可跳转到外部链接或触发页内导航

### 10.3 被嵌套场景
| 外层组件 | 说明 |
|----------|------|
| HalfScreenOverlay | 半屏浮层底部常放置 A1/A3（双按钮/单按钮）作为确认操作区 |
| Dialog | 对话框的操作按钮区已内置，不使用 ActionCombo |
| 页面底部 | A 类操作行通常固定在页面底部，B 类辅助行紧跟其下 |
