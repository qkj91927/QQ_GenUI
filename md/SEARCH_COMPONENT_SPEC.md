# 搜索框 Search · 组件设计规范

> **组件 ID**：`search`  
> **大类**：操作  
> **变体数量**：6 种（A一级3态 + B二级3态）

## 1. 概述

搜索框组件用于内容检索场景，提供从默认态 → 激活态 → 输入态的完整交互状态覆盖。按导航层级分为 A.一级（无返回按钮）和 B.二级（有返回按钮）两组，每组包含 3 种交互状态，共 6 种子组件。

## 2. 子组件矩阵

### A. 一级搜索（无返回按钮）

| 编号 | 名称 | 状态 | 输入框宽度 | 对齐方式 |
|------|------|------|-----------|---------|
| A1 | 一级 · 默认 | Default | 396px | 居中 |
| A2 | 一级 · 激活 | Focused | 350px | 左对齐 |
| A3 | 一级 · 输入 | Typing | 350px | 左对齐 |

### B. 二级搜索（有返回按钮）

| 编号 | 名称 | 状态 | 输入框宽度 | 对齐方式 |
|------|------|------|-----------|---------|
| B1 | 二级 · 默认 | Default | 328px | 左对齐 |
| B2 | 二级 · 激活 | Focused | 328px | 左对齐 |
| B3 | 二级 · 输入 | Typing | 328px | 左对齐 |

## 3. 视觉规范

### 3.1 容器
- **外容器**: 428 × 60px，背景 `var(--bg_bottom_light)`（#FFFFFF），水平 padding 16px
- **输入框**: 高 36px，背景 `var(--fill_standard_primary)`（rgba(13, 16, 49, 0.04)），圆角 12px

### 3.2 输入框宽度

| 场景 | 宽度 | 说明 |
|------|------|------|
| 默认态·一级 (无取消) | 396px | 占满可用区域 (428 - 32) |
| 激活/输入态·一级 (无返回) | 350px | 右侧留出"取消"按钮空间 |
| 二级 (有返回) | 328px | 左侧返回箭头 + 右侧取消按钮 |

### 3.3 图标

| 图标 | 尺寸 | 颜色 | 使用场景 |
|------|------|------|---------|
| `icons/search.svg` 搜索图标 (默认/激活) | 18 × 18px | `#929296` | A1, A2, B1, B2 |
| `icons/search.svg` 搜索图标 (输入态) | 18 × 18px | `#1A1A1A` | A3, B3 |
| 蓝色光标 | 1 × 18px | `#0099FF` | A2, A3, B2, B3 |
| `icons/close_input.svg` 清除按钮 | 20 × 20px | `#929296` | A3, B3 |
| `icons/chevron_left.svg` 返回箭头 | 24 × 24px | `#1A1A1A` | B1, B2, B3 |

### 3.4 文字

| 元素 | 字号 | 字重 | 颜色 | 字体 |
|------|------|------|------|------|
| placeholder "搜索" | 17px | 400 | `rgba(60, 60, 67, 0.56)` | PingFang SC |
| 输入文本 "搜索" | 17px | 400 | `rgba(0, 0, 0, 0.90)` | PingFang SC |
| "取消" 按钮 | 16px | 400 | `#214CA5` | PingFang SC |

### 3.5 返回箭头布局
- 返回箭头容器: 12 × 24px，位于输入框左侧
- 箭头 SVG 24 × 24px，通过 `margin-left: -6px` 对齐
- 箭头与输入框间距: 12px

## 4. 状态说明

### 默认态 (Default) — A1 / B1
- placeholder 文字 + 搜索图标
- A1: 图标和文字居中对齐
- B1: 图标和文字左对齐，左侧显示返回箭头

### 激活态 (Focused) — A2 / B2
- 输入框获得焦点，显示蓝色光标
- placeholder 文字左对齐
- 右侧显示"取消"按钮
- B2: 额外显示左侧返回箭头

### 输入态 (Typing) — A3 / B3
- 搜索图标变为 `#1A1A1A` (深色)
- 输入文字显示为 `rgba(0, 0, 0, 0.90)` (深色实文)
- 光标位于文字右侧
- 输入框右侧显示清除按钮 (圆形×)
- 右侧显示"取消"按钮
- B3: 额外显示左侧返回箭头

## 5. 交互行为

| 触发 | 行为 |
|------|------|
| 点击默认态输入框 | 进入激活态，显示光标和取消按钮 |
| 开始输入文字 | 进入输入态，搜索图标变深色，显示清除按钮 |
| 点击清除按钮 | 清空文字，回到激活态 |
| 点击取消按钮 | 回到默认态 |
| 点击返回箭头 | 返回上一级页面 |

## 6. Figma 属性映射

```
Search / level=primary, state=default, align=center    → A1
Search / level=primary, state=focused                  → A2
Search / level=primary, state=typing                   → A3
Search / level=secondary, state=default, hasBack=true  → B1
Search / level=secondary, state=focused, hasBack=true  → B2
Search / level=secondary, state=typing, hasBack=true   → B3
```

## 7. 设计令牌

```
--bg-item: #FFFFFF                              (容器背景)
--fill-standard: rgba(13,16,49,0.04)            (输入框背景)
--text-tertiary: rgba(60,60,67,0.56)            (placeholder)
--text-primary: rgba(0,0,0,0.90)                (输入文字)
--text-link: #214CA5                             (取消按钮)
--icon-secondary: #929296                        (默认态图标)
--icon-primary: #1A1A1A                          (输入态图标)
--brand-blue: #0099FF                            (光标)
--icon-primary: #1A1A1A                          (返回箭头)
```

---

## 8. CSS 实现代码块

> Search 在 HTML 中通过 JavaScript 内联 `style.cssText` 实现，以下为等效 CSS 类形式。

### 8.1 搜索框容器

```css
.search-container {
    width: 428px;
    height: 60px;
    background: var(--bg_bottom_light);
    display: flex;
    align-items: center;
    padding: 0 16px;
    box-sizing: border-box;
    font-family: 'PingFang SC', sans-serif;
}
```

### 8.2 返回箭头（二级搜索框 B 类）

```css
.search-back {
    display: flex;
    align-items: center;
    width: 12px;
    height: 24px;
    flex-shrink: 0;
    margin-right: 12px;
}
```

### 8.3 搜索输入框

```css
.search-box {
    height: 36px;
    background: var(--fill_standard_primary);
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    align-items: center;
    position: relative;
    flex: 1;
    padding: 0 10px;
    box-sizing: border-box;
}
/* 一级默认态居中，其余左对齐 */
.search-box.center { justify-content: center; }
.search-box.left { justify-content: flex-start; }
```

### 8.4 三种状态文字

```css
/* 默认态 placeholder */
.search-placeholder {
    font-size: 17px;
    font-weight: 400;
    color: var(--text_secondary);
}
/* 输入态文字 */
.search-input-text {
    font-size: 17px;
    font-weight: 400;
    color: var(--text_primary);
}
/* 光标 */
.search-cursor {
    width: 1px;
    height: 18px;
    background: var(--brand_standard);
}
/* 清除按钮 */
.search-clear {
    width: 20px;
    height: 20px;
    margin-left: auto;
}
```

### 8.5 取消按钮

```css
.search-cancel {
    margin-left: auto;
    font-size: 16px;
    font-weight: 400;
    color: var(--text_link);
    flex-shrink: 0;
    padding-left: 14px;
}
```

---

## 9. 与导航栏的布局关系

| 搜索级别 | 与 NavBar 的关系 | 说明 |
|----------|-----------------|------|
| A 一级搜索框 | **独立于 NavBar** | 通常位于 NavBar 下方，作为页面内搜索入口。NavBar 保持正常显示 |
| B 二级搜索框 | **替代 NavBar 显示** | 自带返回箭头，进入搜索页时替代原有 NavBar。返回箭头共享导航栈，点击后返回上一页 |

> **页面结构示例**：
> - A 一级：`StatusBar → NavBar → Search(A) → 列表内容`
> - B 二级：`StatusBar → Search(B，含返回箭头) → 搜索结果列表`
