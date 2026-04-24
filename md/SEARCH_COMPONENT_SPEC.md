# 搜索框 Search · 组件设计规范

> **组件 ID**：`search`  
> **大类**：操作  
> **变体数量**：12 种（A一级 6 种 + B二级 6 种 = 3 状态 × 2 配色 × 2 层级）

## 🔒 强约束声明

@LINT F1, TK1, TK10
@SPEC_OF_TRUTH 本文件为 Search 权威规范

### @MUST
- 变体仅限 A1-A6（一级，无返回按钮）+ B1-B6（二级，有返回按钮），共 12 种
  - A1-A3 / B1-B3：**灰底填充** `var(--fill-tertiary)`，适用于**白色系**页面
  - A4-A6 / B4-B6：**白底填充** `var(--bg-bottom)`，适用于**非白色系**页面
- **页面底色 ↔ Search 填充色 反相映射**（强约束）：
  - 页面 `--bg-bottom` / `--bg-top`（白色系，值均为 `#FFFFFF`）→ Search 填充 `--fill-tertiary`（灰）
  - 页面 `--bg-secondary`（#F2F2F7，含 Card/Grouped List/Message）→ Search 填充 `--bg-bottom`（白）
  - 页面 `--bg-bottom-brand`（#EFF4FF，品牌氛围页）→ Search 填充 `--bg-bottom`（白）
  - 页面 `--bg-select`（#F0F0F2，AIO 专属页）→ Search 填充 `--bg-bottom`（白）
- 默认态图标：`var(--icon-secondary)`
- 输入态图标/返回箭头：`var(--icon-primary)`
- 图标 SVG 使用 `fill="currentColor"`，通过 CSS `color` 着色

### @FORBIDDEN
- 发明注册表外的变体
- 页面与 Search 填充**同为白色系**（`bg-bottom` / `bg-top` 页面 + `bg-bottom` 填充 → 白上白无分隔）
- 页面与 Search 填充**同为灰色系**（`bg-secondary` / `bg-bottom-brand` / `bg-select` 页面 + `fill-tertiary` 填充 → 灰上灰无分隔）
- 图标色硬编码 rgba / `#xxx`
- 图标使用 `filter` hack 改色
- Search 填充使用 `--fill-tertiary` / `--bg-bottom` 之外的 token
- **Search A/B 全系参与吸顶复合**（S24/S27）：Search A 一级 / B 二级**均不参与**吸顶 chrome 复合结构，只能作为页面内容流中的普通组件

## 1. 概述

搜索框组件用于内容检索场景，提供从默认态 → 激活态 → 输入态的完整交互状态覆盖。按导航层级分为 A.一级（无返回按钮）和 B.二级（有返回按钮）两组，每组包含 3 种交互状态 × 2 种配色（灰底/白底），共 12 种子组件。

**配色按页面底色反相映射**：白页用灰底 Search，灰页用白底 Search，确保视觉分层。

## 2. 子组件矩阵

### A. 一级搜索（无返回按钮）

| 编号 | 名称 | 状态 | 填充色 | 适用页面底色 | 输入框宽度 | 对齐方式 |
|------|------|------|-------|------------|-----------|---------|
| A1 | 一级 · 默认 · 灰底 | Default | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 396px | 居中 |
| A2 | 一级 · 激活 · 灰底 | Focused | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 350px | 左对齐 |
| A3 | 一级 · 输入 · 灰底 | Typing | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 350px | 左对齐 |
| A4 | 一级 · 默认 · 白底 | Default | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 396px | 居中 |
| A5 | 一级 · 激活 · 白底 | Focused | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 350px | 左对齐 |
| A6 | 一级 · 输入 · 白底 | Typing | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 350px | 左对齐 |

### B. 二级搜索（有返回按钮）

| 编号 | 名称 | 状态 | 填充色 | 适用页面底色 | 输入框宽度 | 对齐方式 |
|------|------|------|-------|------------|-----------|---------|
| B1 | 二级 · 默认 · 灰底 | Default | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 328px | 左对齐 |
| B2 | 二级 · 激活 · 灰底 | Focused | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 328px | 左对齐 |
| B3 | 二级 · 输入 · 灰底 | Typing | `--fill-tertiary` | `bg-bottom` / `bg-top`（白色系） | 328px | 左对齐 |
| B4 | 二级 · 默认 · 白底 | Default | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 328px | 左对齐 |
| B5 | 二级 · 激活 · 白底 | Focused | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 328px | 左对齐 |
| B6 | 二级 · 输入 · 白底 | Typing | `--bg-bottom` | `bg-secondary` / `bg-bottom-brand` / `bg-select`（非白色系） | 328px | 左对齐 |

## 3. 视觉规范

### 3.1 容器
- **外容器**: 428 × 36px（净内容高度），水平 padding 16px。组件不含上下 padding，间距由外部间距组件提供
- **输入框**: 高 36px，圆角 12px。填充色按页面底色反相映射：
  - 在白底页面 → `var(--fill-tertiary)` (A1-A3 / B1-B3)
  - 在灰底页面 → `var(--bg-bottom)` (A4-A6 / B4-B6)

### 3.2 输入框宽度

| 场景 | 宽度 | 说明 |
|------|------|------|
| 默认态·一级 (无取消) | 396px | 占满可用区域 (428 - 32) |
| 激活/输入态·一级 (无返回) | 350px | 右侧留出"取消"按钮空间 |
| 二级 (有返回) | 328px | 左侧返回箭头 + 右侧取消按钮 |

### 3.3 图标

| 图标 | 尺寸 | 颜色 | 使用场景 |
|------|------|------|---------|
| `icons/search.svg` 搜索图标 (默认/激活) | 18 × 18px | `var(--icon-secondary)` | A1/A2/A4/A5, B1/B2/B4/B5 |
| `icons/search.svg` 搜索图标 (输入态) | 18 × 18px | `var(--icon-primary)` | A3/A6, B3/B6 |
| 蓝色光标 | 1 × 18px | `var(--brand-standard)` | 激活/输入态全部 |
| `icons/close_input.svg` 清除按钮 | 20 × 20px | `var(--icon-secondary)` | 输入态全部 |
| `icons/chevron_left.svg` 返回箭头 | 24 × 24px | `var(--icon-primary)` | B 组全部 |

### 3.4 文字

| 元素 | 字号 | 字重 | 颜色 | 字体 |
|------|------|------|------|------|
| placeholder "搜索" | 17px | 400 | `var(--text-tertiary)` | PingFang SC |
| 输入文本 "搜索" | 17px | 400 | `var(--text-primary)` | PingFang SC |
| "取消" 按钮 | 16px | 400 | `#214CA5` | PingFang SC |

### 3.5 返回箭头布局
- 返回箭头容器: 12 × 24px，位于输入框左侧
- 箭头 SVG 24 × 24px，通过 `margin-left: -6px` 对齐
- 箭头与输入框间距: 12px

## 4. 状态说明

### 默认态 (Default) — A1/A4 / B1/B4
- placeholder 文字 + 搜索图标
- A 组：图标和文字居中对齐
- B 组：图标和文字左对齐，左侧显示返回箭头

### 激活态 (Focused) — A2/A5 / B2/B5
- 输入框获得焦点，显示蓝色光标
- placeholder 文字左对齐
- 右侧显示"取消"按钮
- B 组：额外显示左侧返回箭头

### 输入态 (Typing) — A3/A6 / B3/B6
- 搜索图标变为 `var(--icon-primary)` (深色)
- 输入文字显示为 `var(--text-primary)` (深色实文)
- 光标位于文字右侧
- 输入框右侧显示清除按钮 (圆形×)
- 右侧显示"取消"按钮
- B 组：额外显示左侧返回箭头

> 配色说明：A1-A3 / B1-B3 为**灰底**（用于白页），A4-A6 / B4-B6 为**白底**（用于灰页）。状态行为与图标逻辑两套配色完全一致，仅填充色不同。

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
# 灰底配色（适用于 --bg-bottom 页面）
Search / level=primary,   state=default, align=center, fill=gray   → A1
Search / level=primary,   state=focused,                fill=gray  → A2
Search / level=primary,   state=typing,                 fill=gray  → A3
Search / level=secondary, state=default, hasBack=true,  fill=gray  → B1
Search / level=secondary, state=focused, hasBack=true,  fill=gray  → B2
Search / level=secondary, state=typing,  hasBack=true,  fill=gray  → B3

# 白底配色（适用于 --bg-secondary 页面）
Search / level=primary,   state=default, align=center, fill=white  → A4
Search / level=primary,   state=focused,                fill=white → A5
Search / level=primary,   state=typing,                 fill=white → A6
Search / level=secondary, state=default, hasBack=true,  fill=white → B4
Search / level=secondary, state=focused, hasBack=true,  fill=white → B5
Search / level=secondary, state=typing,  hasBack=true,  fill=white → B6
```

## 7. 设计令牌

```
--bg-bottom: #FFFFFF                      (外容器背景 / 白底配色 A4-A6 B4-B6 的输入框填充)
--fill-tertiary: rgba(118,118,128,0.12)    (灰底配色 A1-A3 B1-B3 的输入框填充)
--bg-secondary: #F2F2F7                   (白底 Search 配色适用的页面底色)
--text-tertiary: rgba(60,60,67,0.3)           (placeholder)
--text-primary: rgba(0,0,0,1.0)                (输入文字)
--text-link: #214CA5                            (取消按钮)
--icon-secondary: rgba(60,60,67,0.6)                       (默认态图标)
--icon-primary: #000000                         (输入态图标/返回箭头)
--brand-standard: #0099FF                       (光标)
```

---

## 8. CSS 实现代码块

> Search 在 HTML 中通过 JavaScript 内联 `style.cssText` 实现，以下为等效 CSS 类形式。

### 8.1 搜索框容器

```css
.search-container {
    width: 428px;
    height: 36px;
    background: var(--bg-bottom);
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
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    align-items: center;
    position: relative;
    flex: 1;
    padding: 0 10px;
    box-sizing: border-box;
}
/* 填充配色：按页面底色反相映射选择其一（NOT BOTH） */
.search-box.fill-gray  { background: var(--fill-tertiary); }  /* A1-A3 / B1-B3 用于白页 */
.search-box.fill-white { background: var(--bg-bottom); }       /* A4-A6 / B4-B6 用于灰页 */

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
    color: var(--text-tertiary);
}
/* 输入态文字 */
.search-input-text {
    font-size: 17px;
    font-weight: 400;
    color: var(--text-primary);
}
/* 光标 */
.search-cursor {
    width: 1px;
    height: 18px;
    background: var(--brand-standard);
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
    color: var(--text-link);
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
