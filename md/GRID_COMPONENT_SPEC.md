# 宫格 Grid · 组件设计规范

> **组件 ID**：`grid`  
> **大类**：数据  
> **变体数量**：17 种（A1-A9 平铺 + B1-B8 横滑）

## 🔒 强约束声明

@LINT F1, S16, TK1, TK14
@SPEC_OF_TRUTH 本文件为 Grid 权威规范

### @MUST
- 变体仅限 A1-A9（平铺）+ B1-B8（横滑），共 17 种
- 平铺 Grid 格子数 ≤ 9
- 空态填充色：`var(--fill-tertiary)`；空态圆形填充同色 + `border-radius: 50%`
- 图片 `object-fit: cover`

### @FORBIDDEN
- 发明注册表外的变体
- 空态使用 `--fill-tertiary` 之外的填充色

## 概述

宫格组件用于展示多个同类内容项的网格排列，支持**平铺（Tile）**和**横滑（Scroll）**两种交互方式。宫格块分为**横版、竖版、正方形、圆形**四类形状。

## 组件结构

容器宽度固定为 `428px`，白色背景。每个宫格项由「**占位内容 + 标题文字（可选）**」上下排列构成。

占位内容根据圆角形式分为两类：
- **圆角矩形占位**（A1-A6、A8、B1-B5、B7）：使用 `var(--fill-tertiary)` 填充色，`border-radius: 12px`
- **正圆占位**（A7、A9、B6、B8）：使用相同填充色，`border-radius: 50%`

**标题文字为可选**，不配置时仅展示占位图/图标，适用于纯视觉快捷操作入口等场景。

## 子组件清单（共 17 种）

### A 平铺模式（A1 - A9）

| ID | 名称 | 列数 | 缩略图尺寸 | 圆角 | 字号 | 容器高度 | 占位类型 |
|----|------|------|-----------|------|------|---------|---------|
| A1 | 平铺·横版2列 | 2 | 192×108 | 12px | 14px | 168px | 圆角矩形 |
| A2 | 平铺·竖版2列 | 2 | 192×192 | 12px | 14px | 252px | 圆角矩形 |
| A3 | 平铺·横版2列(高) | 2 | 190×268 | 12px | 14px | 328px | 圆角矩形 |
| A4 | 平铺·竖版3列 | 3 | 120×168 | 12px | 14px | 228px | 圆角矩形 |
| A5 | 平铺·正方形3列 | 3 | 120×120 | 12px | 14px | 180px | 圆角矩形 |
| A6 | 平铺·正方形4列 | 4 | 88×88 | 12px | 12px | 145px | 圆角矩形 |
| A7 | 平铺·圆形4列 | 4 | 64×64 | 50% | 12px | 109px | 正圆 |
| A8 | 平铺·圆形5列(宽) | 5 | 64×64 | 12px | 12px | 121px | 圆角矩形 |
| A9 | 平铺·圆形5列(紧) | 5 | 64×64 | 50% | 12px | 109px | 正圆 |

### B 横滑模式（B1 - B8）

| ID | 名称 | 可见列数 | 总列数 | 缩略图尺寸 | 圆角 | 字号 | 容器高度 | 占位类型 |
|----|------|---------|-------|-----------|------|------|---------|---------|
| B1 | 横滑·竖版2列 | 2 | 6 | 172×256 | 12px | 14px | 316px | 圆角矩形 |
| B2 | 横滑·竖版3列 | 3 | 8 | 108×152 | 12px | 14px | 212px | 圆角矩形 |
| B3 | 横滑·正方形3列 | 3 | 8 | 112×112 | 12px | 14px | 172px | 圆角矩形 |
| B4 | 横滑·正方形4列 | 4 | 10 | 80×80 | 12px | 12px | 137px | 圆角矩形 |
| B5 | 横滑·圆形6列(矩) | 6 | 12 | 60×60 | 12px | 10px | 114px | 圆角矩形 |
| B6 | 横滑·圆形6列(圆) | 6 | 12 | 60×60 | 50% | 10px | 112px | 正圆 |
| B7 | 横滑·圆形7列(矩) | 7 | 14 | 52×52 | 12px | 10px | 106px | 圆角矩形 |
| B8 | 横滑·圆形7列(圆) | 7 | 14 | 52×52 | 50% | 10px | 104px | 正圆 |

## 交互规格

### 平铺模式
- 内容不可滚动，所有项在容器内完整展示
- 项目等间距排列

### 横滑模式
- 容器开启水平滚动 `overflow-x: auto`
- 隐藏滚动条 `scrollbar-width: none` / `::-webkit-scrollbar { display: none }`
- 启用惯性滚动 `-webkit-overflow-scrolling: touch`
- 当 totalCols > visibleCols 时，最右侧项会露出一部分提示可滑

## 视觉规格

### 图片占位（圆角矩形）
- 空态填充色: `var(--fill-tertiary)`（CSS变量 `--fill-tertiary`）
- 圆角统一 `12px`（A1-A6、B1-B5、B7）
- 实际使用时替换为真实图片内容

### 图标占位（正圆）
- 空态填充色同上，`border-radius: 50%`
- 涉及变体：A7/A9（平铺圆形）、B6/B8（横滑圆形）

### 标题文字（可选）
- 字体: PingFang SC
- 字重: 400
- 颜色: `var(--text-primary)`
- 对齐: 居中
- 行高: 与字号对应（14px→20px, 12px→17px, 10px→14px）
- **不配置时**：仅渲染占位图/图标，宫格项高度相应减小（去掉文字行高度）

### 间距
- 容器内边距: 12-24px（视具体变体）
- 项间距: 16px（水平）
- 缩略图到文字间距: 4-8px

## 使用场景

- **平铺模式**: 功能入口、分类导航等固定数量展示
- **横滑模式**: 推荐内容、热门分类等可探索性内容展示
- **横版**: 视频封面、Banner推广
- **竖版**: 商品卡片、人物海报
- **正方形**: 应用图标、相册封面
- **圆形**: 头像展示、功能入口、快捷操作

---

## CSS 实现代码块

### 宫格容器

```css
.grid-container {
    width: 428px;
    background: var(--bg-bottom);
    overflow: hidden;
    position: relative;
}
.grid-container.scroll-mode {
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
}
.grid-container.scroll-mode::-webkit-scrollbar {
    display: none;
}
```

### 内层布局

```css
.grid-inner {
    display: flex;
    flex-wrap: wrap;
    padding: 16px;
    gap: 0;
}
.grid-inner.scroll-inner {
    flex-wrap: nowrap;
    width: max-content;
}
```

### 宫格项

```css
.grid-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.grid-item-thumb {
    background: var(--fill-tertiary);
}
.grid-item-thumb.rounded {
    border-radius: 12px;
}
.grid-item-thumb.circle {
    border-radius: 50%;
}
.grid-item-label {
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text-primary);
    text-align: center;
    white-space: nowrap;
    word-wrap: break-word;
}
```
