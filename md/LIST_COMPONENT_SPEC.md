# 通栏式列表母组件设计与技术规范 (Plain List Component Spec)

> **组件 ID**：`list`  
> **大类**：数据  
> **变体数量**：67 种（8L × 3C × 10R 经约束过滤）

本文件定义了移动端通栏式列表母组件的系统化构建逻辑、属性约束及 UI 规范。

---

## 1. 组件构成 (Anatomy)

- **左侧区域 (Left Area)**：Icon, Avatar, Thumbnail 等。
- **列表内容 (Content Area)**：1-3 行文本，包含标题、描述、链接等。
- **右侧区域 (Right Area)**：辅助信息、按钮、开关、金额、步数、聊天时间等。

---

## 2. 属性定义 (Properties)

### 2.1 左侧区域 (L)
| 标识 | 属性名 | 视觉特征 | 类型 |
| :--- | :--- | :--- | :--- |
| L0/Empty | Empty | 不显示左侧区域 | any |
| L1 | Icon | `icons/empty_icon.svg`（24×24 占位图标） | single |
| L2 | File Icon | `icons/doc.svg`（52×52 文件图标） | multi |
| L3 | Small Avatar | `icons/Avatar_32.svg`（32×32 圆形头像） | single |
| L4 | Medium Avatar | `icons/Avatar_40.svg`（40×40 圆形头像） | multi |
| L5 | Large Avatar | `icons/Avatar_52.svg`（52×52 圆形头像） | multi |
| L6 | 中缩略图 | `icons/Thumbnail_40.svg`（40×40 矩形缩略图，圆角 8px） | multi |
| L7 | App Icon L | `icons/Thumbnail_52.svg`（52×52 应用图标占位） | multi |

### 2.2 中间内容区域 (C)
| 标识 | 属性名 | 视觉特征 | 行数 | 类型 |
| :--- | :--- | :--- | :--- | :--- |
| C1 | 单行 | 仅主标题 | 1 | single |
| C2 | 双行 | 主标题 + 1行描述 | 2 | multi |
| C3 | 三行 | 主标题 + 2行描述 | 3 | multi |

### 2.3 右侧区域 (R)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| R0/Empty | Empty | 不显示右侧区域 |
| R1 | 辅助+箭头 | 灰色文本 + `icons/chevron_right.svg`（向右箭头） |
| R2 | 辅助+头像+箭头 | 文本 + `icons/Avatar_32.svg`（32×32 头像）+ `icons/chevron_right.svg`（箭头） |
| R3 | 辅助+图片+箭头 | 文本 + `icons/Thumbnail_32.svg`（32×32 缩略图，圆角4px）+ `icons/chevron_right.svg`（箭头） |
| R4 | 按钮 | 次级按钮 (Button) |
| R5 | Action | 蓝色链接文字 |
| R6 | Icon | 基础操作图标 |
| R7 | 金额 | 粗体数字 (DIN) |
| R8 | 步数 | 数字 + 步数图标 |
| R9 | 聊天 | 时间 + 状态图标 |

---

## 3. 属性约束 (Constraints)

1. **行高分类约束**：
   - Single-line 类型 (L1, L3) 仅匹配 C1。
   - Multi-line 类型 (L2, L4, L5, L6, L7) 仅匹配 C2 或 C3。
2. **左侧 Empty 约束**：
   - 仅限匹配 C1 或 C2（禁止三行 C3）。
   - 右侧仅限匹配 R1, R4, R5, R6。
3. **强绑定逻辑**：
   - **R2 (头像+箭头)**：仅限 L1 (Icon) 搭配 C1。
   - **R3 (图片+箭头)**：仅限 C1。
   - **L2 (File Icon)**：右侧仅限匹配 R6。
   - **R8 (步数) / R9 (聊天)**：仅限 C2。
   - **R7 (金额) / R8 (步数)**：强绑定 L4 (Medium Avatar)。
   - **R9 (聊天)**：强绑定 L5 (Large Avatar)。

---

## 4. 变体矩阵逻辑 (Variants Matrix)

- **理论组合总数**: 8 (L) × 3 (C) × 10 (R) = **240 种**。
- **约束过滤后有效变体数**: 应用第 3 节属性约束后，实际有效组合为 **67 种变体**。
- **渲染原则**: HTML 层仅渲染约束过滤后的有效变体，确保三层（HTML / JSON / MD）一致。

---

## 5. UI 设计规格 (Design Specs)

- **行高 (Height)**: 
  - C1: 52px
  - C2/C3: 72px
- **内边距 (Padding)**: 左右 16px
- **文字规范**:
  - 主标题: 17px, `rgba(0,0,0,0.9)`, line-height: 24px
  - 描述文本: 14px, `rgba(60,60,67,0.76)`, line-height: 20px
  - 链接文字: `#214CA5`（Token `--color-text-link`）
- **间距**: 
  - 左侧区域右间距: 12px（所有 L 类型统一）
  - 右侧区域左间距: 12px
- **描述行结构**: 描述行可含 `icons/empty_icon.svg`（16×16px 占位图标，实际任务中替换）+ 描述文本 · 描述文本 + textlink + `icons/chevron_right.svg`（16×16px 链接箭头）的组合

### 5.1 左侧区域尺寸类

| CSS Class | 尺寸 | 圆角 | 适用 |
|-----------|------|------|------|
| `.icon-24` | 24×24px | — | L1 |
| `.icon-52` | 52×52px | — | L2, L7 |
| `.avatar-32` | 32×32px | 50% | L3 |
| `.avatar-40` | 40×40px | 50% | L4 |
| `.avatar-52` | 52×52px | 50% | L5 |
| `.thumb-40` | 40×40px | 8px | L6 |

### 5.2 右侧区域详细样式

| R | 结构 | 样式细节 |
|---|------|---------|
| R0/Empty | 无 | 不渲染右侧区域 |
| R1 辅助+箭头 | 灰色文字 + 箭头 SVG | 文字 17px `rgba(60,60,67,0.76)`，margin-right: 4px |
| R2 辅助+头像+箭头 | 文字 + 32px 头像 + 箭头 | 头像 margin-right: 8px |
| R3 辅助+图片+箭头 | 文字 + 32px 图片(圆角4px) + 箭头 | 图片 margin-right: 8px |
| R4 按钮 | 次级按钮 | padding: 6px 16px, border-radius: 18px, font-size: 14px, font-weight: 500, 背景 `rgba(116,116,128,0.08)` |
| R5 Action | 蓝色链接文字 | font-size: 17px, color: `#214CA5` |
| R6 Icon | 操作图标 | — |
| R7 金额 | 粗体数字 | font-family: "DIN Alternate", font-weight: 700, font-size: 20px |
| R8 步数 | 数字 + 步数图标 | 数字 20px DIN + 图标列（排名 12px + 16px 图标），margin-left: 4px |
| R9 聊天 | 时间 + 状态图标 | 时间 12px `rgba(60,60,67,0.56)`, 垂直排列 flex-direction: column, align-items: flex-end |

---

## 6. 列表组合规则 (List Composition Rules)

### 6.1 单一类型原则
一个页面视图中的通栏式列表必须由**同一类型的子组件**构成。即同一视图内所有列表行的 L / C / R 组合模式应保持一致，不允许在同一列表中混用不同类型的子组件变体。

### 6.2 结构级切换
不同类型的列表必须通过**结构级切换**展示，例如：Tab、Segment Control、Filter 等视图级切换控件。每个切换状态对应一种独立的列表子组件类型。

### 6.3 页面背景色
通栏式列表的行背景为白色（`#FFFFFF`），与白色页面背景融为一体。因此使用通栏式列表时，页面背景色应使用**默认白色** `#FFFFFF`（Token `bg_bottom_light`）。

> **注意**：如果同一页面还包含卡片式列表（Grouped List），则页面背景色以 `#F0F0F2`（`bg_bottom_standard`）为准。

---

## 7. CSS 实现参考

### 7.1 列表行

```css
.list-row {
    display: flex;
    align-items: center;
    padding: 0 16px;
    width: 428px;
    background: var(--color-bg-item);
    position: relative;
}
.list-row.c1 { height: 52px; }
.list-row.c2, .list-row.c3 { height: 72px; }
```

### 7.2 左侧区域

```css
.list-row .left-area {
    margin-right: 12px;
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
/* L0/Empty 时 */
.list-row .left-area[data-empty] {
    width: 0px;
    margin-right: 0px;
}
```

### 7.3 内容区域

```css
.list-row .content-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
}
.list-row .title {
    font-size: 17px;
    line-height: 24px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.list-row .desc {
    font-size: 14px;
    color: var(--color-text-secondary);
    line-height: 20px;
    display: flex;
    align-items: center;
}
```

### 7.4 右侧区域

```css
.list-row .right-area {
    margin-left: 12px;
    display: flex;
    align-items: center;
    flex-shrink: 0;
}
.list-row .btn-secondary {
    background: var(--color-btn-bg);
    padding: 6px 16px;
    border-radius: 18px;
    font-size: 14px;
    font-weight: 500;
}
.list-row .amount {
    font-family: "DIN Alternate", sans-serif;
    font-weight: 700;
    font-size: 20px;
}
.list-row .switch {
    width: 44px;
    height: 26px;
    background: var(--color-brand-standard);
    border-radius: 13px;
    position: relative;
    transition: background 200ms ease-out;
}
.list-row .switch::after {
    content: '';
    position: absolute;
    right: 2px;
    top: 2px;
    width: 22px;
    height: 22px;
    background: var(--color-bg-item);
    border-radius: 50%;
    transition: right 200ms ease-out, left 200ms ease-out;
}
.list-row .text-link {
    color: var(--color-text-link);
    cursor: pointer;
}
```

---

## 8. 交互行为

### 8.1 点击热区
- 整行为点击热区（L0+R0 除外）
- 点击行为由右侧类型决定

### 8.2 按下态
- 背景色变为 `rgba(0,0,0,0.04)`，过渡 100ms `ease-out`
- 释放恢复默认背景，过渡 150ms `ease-out`

### 8.3 分割线
- 列表行之间的分割线由外部列表容器控制
- 分割线宽度: 距左 16px 到右侧边缘
- 分割线高度: 0.5px
- 颜色: `rgba(0,0,0,0.08)`

---

## 9. 滚动行为规则

### 9.1 列表滚动
- 通栏式列表**本身不内置滚动容器**，由页面级滚动（`<body>` 或外层 scroll container）承载
- 当列表嵌入有限高度容器（如 HalfScreenOverlay 内容区）时，由外层容器提供 `overflow-y: auto`

### 9.2 下拉刷新 / 加载更多
- 列表组件**不内置**下拉刷新和加载更多功能
- 这些功能由业务层在列表外层实现（如添加 pull-to-refresh 容器、滚动到底部触发加载）
- 设计系统仅提供列表行的静态渲染规范

### 9.3 长列表性能
- 超长列表（>100 行）建议业务层实现虚拟滚动（仅渲染可视区域内的行）
- 列表行高度固定（单行 56px / 双行 72px / 三行 88px），适合虚拟滚动计算
