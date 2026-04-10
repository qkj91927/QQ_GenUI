# 半屏导航栏组件设计与技术规范 (HalfScreen NavBar Component Spec)

> **组件 ID**：`hs_navbar`  
> **大类**：导航  
> **变体数量**：7 种（A1-A4 + B1-B3）

## 1. 组件概述 (Overview)

半屏导航栏是专用于半屏浮层（Bottom Sheet / Half-Screen Overlay）顶部的导航组件，承载标题展示、层级返回与关闭操作。与全屏顶部导航栏（NavBar）不同，半屏导航栏始终锚定在浮层内容区顶部，宽度跟随浮层容器而非全屏。

## 2. 组件分类

### A. 一级导航（Primary Level）

一级导航用于半屏浮层的首屏，无返回层级，右侧固定为关闭操作。

| ID | 名称 | 结构 | 高度 | 说明 |
|----|------|------|------|------|
| A1 | 标题+关闭 | 左侧标题 + 右侧关闭按钮(圆形底色) | 54px | 最常用的半屏导航形态 |
| A2 | 标题+副标题+关闭 | 左侧标题+副标题 + 右侧关闭按钮(圆形底色) | 65px | 需要补充说明信息时使用 |
| A3 | 单关闭 | 右侧关闭按钮(圆形底色)，无标题 | 54px | 内容自带标题或以图片开头时使用；遇到图片组件时叠在图片上不占高度 |
| A4 | 图标+标题+关闭 | 左侧App图标+标题 + 右侧功能图标 | 54px | 展示来源应用信息时使用 |

### B. 二级导航（Secondary Level）

二级导航用于半屏浮层内的子页面，左侧为返回操作，中间居中显示标题。

| ID | 名称 | 结构 | 高度 | 说明 |
|----|------|------|------|------|
| B1 | 返回+标题+操作 | 左侧返回箭头 + 居中标题 + 右侧文字操作 | 54px | 子页面带操作入口 |
| B2 | 返回+标题+关闭 | 左侧返回箭头 + 居中标题 + 右侧功能图标 | 54px | 子页面带功能图标 |
| B3 | 返回+标题 | 左侧返回箭头 + 居中标题 | 54px | 最简子页面导航 |

## 3. 布局规范

### 3.1 尺寸与间距

- **组件宽度**：跟随半屏浮层宽度（默认 100%）
- **基准高度**：54px（A2 副标题型为 65px）
- **水平内边距**：左右各 16px
- **关闭按钮**：直接使用 `icons/Close_HalfScreen.svg`（30×30px，SVG 自带灰底圆 `rgba(0,0,0,0.04)` + X 图标，**不需要外层容器包裹**）
- **返回箭头**：`icons/chevron_left.svg`（24×24px）
- **App图标**：`icons/Thumbnail_24.svg`（24×24px 占位，实际任务中替换），与标题间距 8px

### 3.2 文字规范

| 元素 | 字号 | 字重 | 颜色 |
|------|------|------|------|
| 标题 | 17px | Medium (500) | text_primary rgba(0,0,0,0.90) |
| 副标题 | 12px | Regular (400) | text_secondary rgba(60,60,67,0.76) |
| 操作文字 | 17px | Regular (400) | text_primary rgba(0,0,0,0.90) |
| 二级标题 | 17px | Medium (500) | text_primary rgba(0,0,0,0.90) |

### 3.3 对齐方式

- **一级导航**：标题左对齐，关闭按钮右对齐，垂直居中
- **二级导航**：返回箭头左对齐，标题绝对居中，操作/图标右对齐

## 4. 交互规范

### 4.1 A3 单关闭型特殊逻辑

A3 类型无标题文字，仅显示关闭按钮。在组合使用时遵循以下规则：

- **遇到图片组件（image_block）**：A3 叠在图片上方，设置为绝对定位，不占据内容流高度（`position: absolute; z-index: 10`），关闭按钮使用白色/半透明背景以保证可见性
- **遇到其他组件类型**：A3 正常占据一行高度（54px），按标准流式布局排列

### 4.2 关闭行为

- 点击关闭按钮：收起整个半屏浮层
- 点击返回箭头：返回半屏内上一层级页面

## 5. 变体矩阵

共 7 种子组件，由 A一级(4种) + B二级(3种) 构成。

```
A1  标题+关闭           → [标题]                    [X]
A2  标题+副标题+关闭    → [标题/副标题]              [X]
A3  单关闭              →                            [X]
A4  图标+标题+关闭      → [Icon 标题]               [X]
B1  返回+标题+操作      → [←]      [二级标题]     [操作]
B2  返回+标题+关闭      → [←]      [二级标题]      [X]
B3  返回+标题           → [←]      [二级标题]
```

---

## 6. CSS 实现代码块

### 6.1 半屏导航栏行

```css
.hs-navbar-row {
    display: flex;
    align-items: center;
    width: 429px;
    background: transparent;
    position: relative;
    box-sizing: border-box;
}
.hs-navbar-row.level-1 {
    height: 54px;
    padding: 0 16px;
    justify-content: space-between;
}
.hs-navbar-row.level-1-subtitle {
    height: 65px;
    padding: 0 16px;
    justify-content: space-between;
}
.hs-navbar-row.level-2 {
    height: 54px;
    padding: 0 16px;
    justify-content: space-between;
}
```

### 6.2 三区域

```css
.hs-navbar-row .hs-left-area {
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
.hs-navbar-row .hs-left-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.hs-navbar-row .hs-center-title {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 500;
    color: var(--text_primary);
    line-height: 24px;
    text-align: center;
}
.hs-navbar-row .hs-right-area {
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
```

### 6.3 文字与操作元素

```css
.hs-navbar-row .hs-title {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 500;
    color: var(--text_primary);
    line-height: 24px;
}
.hs-navbar-row .hs-subtitle {
    font-size: 12px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text_primary_light);
    line-height: 17px;
}
/* 关闭按钮：直接使用 Close_HalfScreen.svg（自带30px灰底圆，不需要外层样式） */
.hs-navbar-row .hs-close-btn {
    width: 30px;
    height: 30px;
}
.hs-navbar-row .hs-action-text {
    font-size: 17px;
    font-family: 'PingFang SC', sans-serif;
    font-weight: 400;
    color: var(--text_primary);
    line-height: 24px;
}
.hs-navbar-row .hs-back-icon {
    width: 24px;
    height: 24px;
}
.hs-navbar-row .hs-app-icon {
    width: 24px;
    height: 24px;
    margin-right: 8px;
}
.hs-navbar-row .hs-icon-24 {
    width: 24px;
    height: 24px;
}
```

---

## 7. 与浮层内部组件的间距衔接

半屏导航栏固定在半屏浮层顶部，与浮层内部内容区之间插入 **B2（8px）间距组件**：

| 导航栏类型 | 下方组件 | 间距 | 说明 |
|-----------|----------|------|------|
| A1 / A2 / A3 / A4 / B1 / B2 / B3 | 任意内容组件 | **B2（8px）** | 统一紧凑间距，半屏浮层内空间有限 |
| A3（叠在图片上） | ImageBlock | **0px** | A3 绝对定位叠在图片上方，不占据内容流高度 |

---

## 8. 使用限制与底色规则

### 8.1 使用限制
- ⚠️ 半屏导航栏（HS_NavBar）**不可独立使用**，必须嵌入 HalfScreenOverlay 标准型（HSO-A）内部
- **仅标准型（HSO-A）使用半屏导航栏（HS_NavBar）**
- **把手型（HSO-B）不使用半屏导航栏（HS_NavBar）**，半屏态顶部为把手条；上滑进入全屏态后，把手条隐藏，显示全屏导航栏（NavBar），左侧必须为 L3 关闭，中间/右侧可按业务配置（交叉过渡规范详见 `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` §6.6）
- 全屏页面顶部应使用 NavBar（`navbar`），不可使用 HS_NavBar

### 8.2 底色规则
- 半屏导航栏本身为**透明底色**（`background: transparent`）
- 视觉上跟随半屏浮层面板的底色显示（默认白色 `#FFFFFF`）
- 当浮层内容区因嵌入 Card/Grouped List 而切换为灰底（`#F0F0F2`）时，导航栏底色需同步调整
