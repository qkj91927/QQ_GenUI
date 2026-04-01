# 分隔与间距 Divider & Spacing · 组件规范

> **组件 ID**：`divider_spacing`  
> **大类**：数据  
> **变体数量**：7 种（A分割线1 + B间距6）

## 概述

**分隔与间距**是用于在界面中分隔内容层级、控制视觉节奏的基础布局组件。包含两类子组件：

- **A. 分割线 Divider**：以细线形式分隔同一区域内的列表条目或内容块
- **B. 间距 Spacing**：以透明空白区域分隔不同内容模块，控制页面纵向节奏

## 子组件清单（共 7 种）

| 分类 | ID | 名称 |
|------|-----|------|
| A. 分割线 | A1 | 分割线 Divider |
| B. 间距 | B1 | 间距 4px |
| B. 间距 | B2 | 间距 8px |
| B. 间距 | B3 | 间距 12px |
| B. 间距 | B4 | 间距 16px |
| B. 间距 | B5 | 间距 24px |
| B. 间距 | B6 | 间距 32px |

## A. 分割线 Divider

### 视觉规范

| 属性 | 值 |
|------|-----|
| 高度 | 0.5px |
| 颜色 | `rgba(0, 0, 0, 0.08)` — `--separator` |
| 背景 | 透明（跟随父容器背景） |

### 使用参数

分割线只有一种基础样式，通栏/缩进/方向不影响基本视觉，仅为使用时的参数变化：

| 模式 | 宽度 | 偏移 | 使用场景 |
|------|------|------|----------|
| 通栏 Full Width | 428px | 无偏移 | 分隔独立内容板块、通栏列表顶底边界 |
| 居中且左右缩进 | 不固定 | 根据上下组件按需判断 | 列表行之间、卡片内部行间 |

方向支持：水平 (horizontal)、垂直 (vertical)。

### 设计约束

1. 分割线高度固定为 0.5px（Retina 显示屏上的 1 物理像素）
2. 颜色不可自定义，统一使用系统分隔色 `rgba(0, 0, 0, 0.08)`
3. 列表最后一行的底部不显示分割线
4. 同一列表内只使用一种分割线样式
5. 通栏/缩进/方向不构成独立变体

## B. 间距 Spacing

### 视觉规范

| 属性 | 值 |
|------|-----|
| 宽度 | 428px（撑满屏幕宽度） |
| 背景色 | 透明 — `transparent` |
| 高度 | 4px 的整数倍，共 6 种：4 / 8 / 12 / 16 / 24 / 32px |

### 间距选择建议规则

| 分类 | 场景 | 建议间距 |
|------|------|----------|
| 组件内部 | 紧凑排列的辅助信息之间 | B1（4px） |
| 组件内部 | 同组内容块之间、标签与内容之间 | B2（8px） |
| 组件与组件之间 | 同类组件相邻（如卡片与卡片、卡片式列表组与卡片式列表组） | B3（12px） |
| 组件与组件之间 | 不同组件相邻（默认） | B4（16px） |
| 组件与组件之间 | 不同功能模块之间（如个人信息区与设置列表区） | B5（24px） |
| 组件与页面之间 | 页面底部（最后一个组件到页面底部，可滑动场景除外） | B6（32px） |

### 设计约束

1. 间距高度为 4px 的整数倍，遵循 4px 网格系统
2. 间距区域始终为透明背景，不可添加任何可见元素
3. 间距区域横向撑满屏幕宽度
4. 不可使用非标准间距值（如 5px、10px、20px 等）

## Figma 属性映射

### Divider

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Width Mode | Enum | `FullWidth` / `InsetLeft` / `InsetBoth` |
| Orientation | Enum | `Horizontal` / `Vertical` |

### Spacing

| Figma 属性 | 类型 | 可选值 |
|------------|------|--------|
| Size | Enum | `4` / `8` / `12` / `16` / `24` / `32` |

---

## CSS 实现代码块

### 分割线

```css
.divider-container {
    width: 428px;
    background: var(--color-bg-item);
    position: relative;
    display: flex;
    align-items: center;
}
.divider-line {
    height: 0.5px;
    background: var(--color-separator);
}
.divider-line.inset-both {
    width: 396px;
    margin: 0 auto;
}
```

### 间距

```css
.spacing-container {
    width: 428px;
    background: transparent;
    position: relative;
}
.spacing-block-inner {
    width: 428px;
    background: transparent;
}
/* 间距标注（仅设计稿展示用） */
.spacing-annotation {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 10px;
    font-family: 'SF Mono', 'Menlo', monospace;
    color: rgba(0, 153, 255, 0.6);
    pointer-events: none;
    white-space: nowrap;
}
.spacing-bg-stripe {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    background: repeating-linear-gradient(
        135deg,
        rgba(0, 153, 255, 0.15),
        rgba(0, 153, 255, 0.15) 2px,
        rgba(0, 153, 255, 0.04) 2px,
        rgba(0, 153, 255, 0.04) 6px
    );
}
```

---

## 组件间间距选择矩阵

以下矩阵定义了不同组件相邻时应使用哪种间距变体，AI 在拼装页面时必须遵循：

### 特殊间距（0px / 固定值）

| 上方组件 | 下方组件 | 间距 | 说明 |
|----------|----------|------|------|
| StatusBar | NavBar | **0px** | 状态栏与导航栏紧贴，无间距 |
| NavBar | 任意内容组件 | **0px** | 导航栏与内容区紧贴 |
| HS_NavBar | 半屏浮层内容 | **8px** | 半屏导航栏与浮层内容间隔 8px（A3叠在图片上时为0px） |
| AIOInput | — | **0px** | 固定在页面最底部，不使用间距组件 |

### 同类组件相邻

| 组合场景 | 推荐间距 | 说明 |
|----------|---------|------|
| Card 与 Card | **B2（8px）** | 卡片间紧凑间隔（灰色背景露出） |
| Grouped List 组 与 组 | **B2（8px）** | 卡片式列表组间间隔 |
| List 行 与 List 行 | **0px + 分割线** | 通栏列表行间用分割线而非间距 |
| Message 与 Message | **B2（8px）** | 消息气泡间标准间隔 |
| TextBlock 与 TextBlock | **B2（8px）** | 同级文本块间 |
| ImageBlock 与 ImageBlock | **B2（8px）** | 同级图片块间 |

### 不同组件相邻

| 组合场景 | 推荐间距 | 说明 |
|----------|---------|------|
| DataFilter 与 List/Card | **B3（12px）** | 筛选器与内容区之间 |
| TextBlock 与 List/Card | **B3（12px）** | 标题文本块与列表/卡片之间 |
| Search 与 List/Card | **B3（12px）** | 搜索框与结果列表之间 |
| 其他不同组件相邻（默认） | **B4（16px）** | 无特殊规则时的默认间距 |

### 功能模块间

| 组合场景 | 推荐间距 | 说明 |
|----------|---------|------|
| 不同功能模块之间 | **B5（24px）** | 如个人信息区 → 设置列表区 |
| 页面最后一个组件 → 页面底部 | **B6（32px）** | 底部留白（有 AIOInput 时由其 72px 高度替代） |

> **使用原则**：同类紧凑（8px）、异类适中（12-16px）、跨模块宽松（24px）、页面底部最宽松（32px）。
