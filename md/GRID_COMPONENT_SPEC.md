# 宫格 Grid · 组件设计规范

> **组件 ID**：`grid`  
> **大类**：数据  
> **变体数量**：17 种（A1-A9 平铺 + B1-B8 横滑）

## 概述

宫格组件用于展示多个同类内容项的网格排列，支持**平铺（Tile）**和**横滑（Scroll）**两种交互方式。宫格块分为**横版、竖版、正方形、圆形**四类形状。

## 组件结构

容器宽度固定为 `428px`，白色背景。每个宫格项由「缩略图/图标 + 标题文字」上下排列构成。

## 子组件清单（共 17 种）

### A 平铺模式（A1 - A9）

| ID | 名称 | 列数 | 缩略图尺寸 | 圆角 | 字号 | 容器高度 | 形状 |
|----|------|------|-----------|------|------|---------|------|
| A1 | 平铺·横版2列 | 2 | 192×108 | 16px | 14px | 168px | 横版 |
| A2 | 平铺·竖版2列 | 2 | 192×192 | 16px | 14px | 252px | 竖版 |
| A3 | 平铺·正方形3列 | 3 | 120×120 | 16px | 14px | 180px | 正方形 |
| A4 | 平铺·正方形4列 | 4 | 88×88 | 16px | 12px | 145px | 正方形 |
| A5 | 平铺·圆形4列 | 4 | 64×64 | 50% | 12px | 109px | 圆形 |
| A6 | 平铺·圆形5列 | 5 | 64×64 | 50% | 12px | 121px | 圆形 |
| A7 | 平铺·圆形5列 | 5 | 64×64 | 50% | 12px | 109px | 圆形 |
| A8 | 平铺·横版2列(高) | 2 | 190×269 | 16px | 14px | 329px | 横版 |
| A9 | 平铺·竖版3列 | 3 | 120×168 | 16px | 14px | 228px | 竖版 |

### B 横滑模式（B1 - B8）

| ID | 名称 | 可见列数 | 总列数 | 缩略图尺寸 | 圆角 | 字号 | 容器高度 | 形状 |
|----|------|---------|-------|-----------|------|------|---------|------|
| B1 | 横滑·正方形3列 | 3 | 8 | 112×112 | 16px | 14px | 172px | 正方形 |
| B2 | 横滑·正方形4列 | 4 | 10 | 80×80 | 12px | 12px | 137px | 正方形 |
| B3 | 横滑·圆形6列 | 6 | 12 | 60×60 | 50% | 10px | 114px | 圆形 |
| B4 | 横滑·圆形6列 | 6 | 12 | 60×60 | 50% | 10px | 112px | 圆形 |
| B5 | 横滑·圆形7列 | 7 | 14 | 52×52 | 50% | 10px | 106px | 圆形 |
| B6 | 横滑·圆形7列 | 7 | 14 | 52×52 | 50% | 10px | 104px | 圆形 |
| B7 | 横滑·竖版2列 | 2 | 6 | 172×256 | 15.2px | 14px | 316px | 竖版 |
| B8 | 横滑·竖版3列 | 3 | 8 | 108×152 | 16px | 14px | 212px | 竖版 |

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

### 缩略图
- 填充色: `rgba(13, 16, 49, 0.04)`（CSS变量 `--fill-standard`）
- 横版/竖版/正方形圆角: `16px`（B2为12px）
- 圆形: `border-radius: 50%`

### 圆形图标
- 使用独立 SVG 资源（1.svg - 36.svg），每个 SVG 内含圆角矩形或圆形填充
- 圆形模式下标签文字较小（10-12px）

### 标题文字
- 字体: PingFang SC
- 字重: 400
- 颜色: `rgba(0, 0, 0, 0.90)`
- 对齐: 居中
- 行高: 与字号对应（14px→20px, 12px→17px, 10px→14px）

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
    background: var(--bg-item);
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
    background: var(--fill-standard);
}
.grid-item-thumb.rounded {
    border-radius: 16px;
}
.grid-item-thumb.rounded-sm {
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
