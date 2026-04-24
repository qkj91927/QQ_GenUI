# 通栏式列表母组件设计与技术规范 (Plain List Component Spec)

> **组件 ID**：`list`  
> **大类**：数据  
> **变体数量**：110 种（67 默认态 + 43 多选态）

## 🔒 强约束声明

@LINT F1, F3, F4, S7, S17, TK1, DV1
@SPEC_OF_TRUTH 本文件为 List（通栏列表）权威规范

### @MUST
- 变体仅限 L0-L7 × C1-C3 × R0-R9，共 110 种（67 默认 + 43 多选），经约束矩阵过滤
- 容器宽度 428px 通栏
- 行间分割线 0.5px + `var(--border-weak)`，距左 16px 到右侧边缘
- 列表最后一行底部不显示分割线
- 多选态 S1：L0-L7 × C × {R0,R1,R2,R3,R6,R7}
- 约束：L0 禁 C3 且 R 限 R1/R4/R5/R6；R2 限 L1+C1；R3 限 C1；R7/R8 限 L4；R9 限 L5+C2

### @FORBIDDEN
- 发明注册表外的变体
- 最后一行显示底部分割线
- 分割线距左非 16px 或颜色非 `--border-weak`

本文件定义了移动端通栏式列表母组件的系统化构建逻辑、属性约束及 UI 规范。

---

## 1. 组件构成 (Anatomy)

- **多选控件 (Selection Control)**：可选前置，位于左侧区域之前，24px 圆形选择器，点击切换选中/未选中态。
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
| R1 | 辅助+箭头 | 辅助文字（14px，行高 20px，`var(--text-secondary)`，**可省略**）+ `icons/chevron_right.svg`（16×16px，`var(--icon-tertiary)`） |
| R2 | 辅助+头像+箭头 | 辅助文字（14px，行高 20px，`var(--text-secondary)`）+ `icons/Avatar_32.svg`（32×32 头像）+ `icons/chevron_right.svg`（16×16px，`var(--icon-tertiary)`） |
| R3 | 辅助+图片+箭头 | 辅助文字（14px，行高 20px，`var(--text-secondary)`）+ `icons/Thumbnail_32.svg`（32×32 缩略图，圆角4px）+ `icons/chevron_right.svg`（16×16px，`var(--icon-tertiary)`） |
| R4 | 按钮 | 次级按钮 (Button) |
| R5 | Action | 蓝色链接文字 |
| R6 | Icon | `icons/empty_icon.svg`（24×24 占位，实际任务中替换为 `icons/QUI_24_icons/<图标名>.svg`） |
| R7 | 金额 | 粗体数字 (DIN) |
| R8 | 步数 | 数字 + `icons/heart.svg`（16×16 爱心图标） |
| R9 | 聊天 | 时间 + 状态图标（`icons/remind_mute.svg`，可替换为其他业务图标，也可不配置） |

### 2.4 多选状态 (S)

| 标识 | 名称 | 视觉特征 |
| :--- | :--- | :--- |
| S0 | 无多选（默认） | 不显示选择控件，行为与原有变体完全一致 |
| S1 | 多选态 | 左侧前置 24px 圆形选择控件（`padding-right: 12px`）；**未选中**：`1.5px` 灰色边框圆（`rgba(60,60,67,0.25)`）；**已选中**：蓝底（`#0099FF`）白色对勾；点击控件切换两态，不另列两个静态变体 |

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
   - **R2/R3**：仅限 C1（单行），不可与 C2（双行）或 C3（三行）组合。
   - **R1**：允许与 C1/C2/C3 搭配。
   - **L2 (File Icon)**：右侧仅限匹配 R6。
   - **R8 (步数) / R9 (聊天)**：仅限 C2。
   - **R7 (金额) / R8 (步数)**：强绑定 L4 (Medium Avatar)。
   - **R9 (聊天)**：强绑定 L5 (Large Avatar)。
4. **多选态约束（S1）**：
   - 左侧 L0-L7 均支持多选态。
   - 右侧仅限 **R0、R1、R2、R3、R6、R7**（不支持 R4 按钮、R5 Action、R8 步数、R9 聊天）。
   - 多选控件点击后在「未选中」与「已选中」之间切换，无需单独列举两个静态变体。

---

## 4. 变体矩阵逻辑 (Variants Matrix)

- **理论组合总数**: 8 (L) × 3 (C) × 10 (R) = **240 种**。
- **约束过滤后默认态有效变体数**: **67 种**（S0）。
- **多选态新增变体数**: 在默认态 67 种中，筛出右侧 R ∈ {R0,R1,R2,R3,R6,R7} 的组合，共 **43 种**（多选态）。
- **总有效变体数**: **110 种**（67 + 43）。
- **渲染原则**: HTML 层仅渲染约束过滤后的有效变体，确保三层（HTML / JSON / MD）一致。

---

## 5. UI 设计规格 (Design Specs)

- **行高 (Height)**: 
  - C1: 52px
  - C2/C3: 72px
- **内边距 (Padding)**: 左右 16px
- **文字规范**:
  - 主标题: 17px, `var(--text-primary)`, line-height: 24px
  - 描述文本: 14px, `var(--text-secondary)`, line-height: 20px
  - 链接文字: `#214CA5`（Token `--text-link`）
- **间距**: 
  - 左侧区域右间距: 12px（所有 L 类型统一）
  - 右侧区域左间距: 12px
- **描述行结构（C2/C3）**：默认仅展示描述文本（含可选 textlink），行首 empty.icon 与行尾右箭头**默认不展示**；如需添加，按以下规则可选配：
  - 行首图标：`icons/empty_icon.svg`（16×16px，`flex-shrink:0`）— 可选添加
  - 描述文本：必填，与 textlink 合并为 `.desc-text`（`flex-shrink:1`，超出截断）
  - textlink：可选，嵌套在 `.desc-text` 内，仅以链接色（`var(--text-link)`）区分，与描述文本紧挨 — 可省略
  - 行尾右箭头：`icons/chevron_right.svg`（16×16px，`flex-shrink:0`）— 可选添加

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
| R1 辅助+箭头 | 灰色文字（可省略）+ 箭头 SVG | 辅助文字 **14px**，行高 **20px**，颜色 `var(--text-secondary)`，margin-right: 4px；箭头 `icons/chevron_right.svg` 16×16px，颜色 `var(--icon-tertiary)`；辅助文字可选配，省略时仅显示箭头 |
| R2 辅助+头像+箭头 | 文字 + 32px 头像 + 箭头 | 辅助文字 **14px**，行高 **20px**，颜色 `var(--text-secondary)`；头像 margin-right: 8px；箭头同 R1 |
| R3 辅助+图片+箭头 | 文字 + 32px 图片(圆角4px) + 箭头 | 辅助文字 **14px**，行高 **20px**，颜色 `var(--text-secondary)`；图片 margin-right: 8px；箭头同 R1 |
| R4 按钮 | 次级按钮 | padding: 6px 16px, border-radius: 18px, font-size: 14px, font-weight: 500, 背景 `rgba(116,116,128,0.08)` |
| R5 Action | 蓝色链接文字 | font-size: 17px, color: `#214CA5` |
| R6 Icon | `icons/empty_icon.svg`（24×24 占位，实际任务中替换） | — |
| R7 金额 | 粗体数字 | font-family: "DIN Alternate", font-weight: 700, font-size: 20px |
| R8 步数 | 数字 + 爱心图标 | 数字 20px DIN + 图标列（排名 12px + `icons/heart.svg` 16×16），margin-left: 4px |
| R9 聊天 | 时间 + 状态图标（可选） | 时间 12px `var(--text-secondary)`, 垂直排列 flex-direction: column, align-items: flex-end；状态图标默认使用 `icons/remind_mute.svg`，可替换为其他业务图标，颜色 token `--icon-secondary`，也可不配置 |

---

## 6. 列表组合规则 (List Composition Rules)

### 6.1 单一类型原则
一个页面视图中的通栏式列表必须由**同一类型的子组件**构成。即同一视图内所有列表行的 L / C / R 组合模式应保持一致，不允许在同一列表中混用不同类型的子组件变体。

### 6.2 结构级切换
不同类型的列表必须通过**结构级切换**展示，例如：Tab、Segment Control、Filter 等视图级切换控件。每个切换状态对应一种独立的列表子组件类型。

### 6.3 页面背景色
通栏式列表的行背景为白色（`#FFFFFF`），与白色页面背景融为一体。因此使用通栏式列表时，页面背景色应使用**默认白色** `#FFFFFF`（Token `--bg-bottom`）。

> **注意**：如果同一页面还包含卡片式列表（Grouped List），则页面背景色以 `var(--bg-secondary)`（`--bg-secondary`）为准。

---

## 7. CSS 实现参考

### 7.1 列表行

```css
.list-row {
    display: flex;
    align-items: center;
    padding: 0 16px;
    width: 428px;
    background: var(--bg-bottom);
    position: relative;
}
.list-row.c1 { height: 52px; }
.list-row.c2, .list-row.c3 { height: 72px; }
```

### 7.1.1 多选控件

多选控件使用 `icons/` 中的 Checkbox SVG 资源，与其他勾选场景保持一致：

| 状态 | 图标 | 尺寸 |
|---|---|---|
| 未选中 | `icons/Checkbox.svg` | 24×24px |
| 已选中 | `icons/Checkbox_filled.svg` | 24×24px |

```css
/* 多选控件容器（前置于左侧区域之前） */
.list-selection {
    flex-shrink: 0;
    margin-right: 12px;
    cursor: pointer;
}
.list-selection img {
    width: 24px;
    height: 24px;
    display: block;
}
```

**交互实现**：点击控件通过替换 `img.src` 切换状态：
```javascript
document.addEventListener('click', function(e) {
    const selImg = e.target.closest('.list-selection img');
    if (selImg) {
        e.stopPropagation();
        if (selImg.src.includes('Checkbox_filled')) {
            selImg.src = selImg.src.replace('Checkbox_filled', 'Checkbox');
        } else {
            selImg.src = selImg.src.replace('Checkbox.svg', 'Checkbox_filled.svg');
        }
    }
});
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
    min-width: 0;           /* 允许 flex 子项被压缩到小于内容自然宽度 */
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
    color: var(--text-secondary);
    line-height: 20px;
    height: 20px;
    display: flex;
    align-items: center;    /* 图标与文字垂直居中 */
    overflow: hidden;
}
/* 描述行文字节点（含 textlink）：可被压缩，超出截断 */
.list-row .desc-text {
    flex-shrink: 1;
    min-width: 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    /* textlink 嵌套在内：<span style="color:var(--text-link)">textlink</span> */
}
/* 图标：不压缩，始终完整显示 */
.list-row .desc img {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
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
/* 辅助文字：限制最大宽度，防止挤压内容区 */
.list-row .helper-text {
    max-width: 120px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

### 5.3 文本截断规则

**通栏式列表采用三段式 Flex 布局**：`[左区 flex-shrink:0] | [内容区 flex:1] | [右区 flex-shrink:0]`

Flex 算法分配顺序：
1. 先固定左区（图标/头像）和右区（辅助信息+图标）的宽度
2. 剩余空间全部分配给内容区（`flex:1`）
3. `min-width:0` 使内容区可被压缩到任意宽度，`overflow:hidden` 才能真正生效

截断规则：
1. **内容区**：`flex:1; min-width:0`，宽度由 flex 算法自动分配，无需硬编码
2. **标题**：单行，超出内容区右边界省略（`…`）
3. **描述行**：`<img>` 设 `flex-shrink:0` 不压缩；描述文本与 textlink 合并为单一 `.desc-text` 节点（`flex-shrink:1; min-width:0`），超长时整体截断，textlink 嵌套其中仅以链接色区分，两者紧挨无额外间距
4. **右区辅助文字**：`max-width:120px` 防止辅助文字过长挤压内容区，超出省略

**右侧区域特殊元素样式**（`.right-area` 布局见 §7.4）：

| 选择器 | 关键属性 |
|--------|---------|
| `.btn-secondary` | padding: 6px 16px / radius: 18px / 14px 500 / bg: `--fill-secondary` |
| `.amount` | DIN Alternate / 700 / 20px |
| `.switch` | 44×26px / radius: 13px / bg: `--brand-standard` / 滑块 22px 圆形 |
| `.text-link` | `--text-link` / cursor: pointer |

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
- 颜色: `var(--border-weak)`

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
- 列表行高度固定（单行 52px / 双行&三行 72px），适合虚拟滚动计算
