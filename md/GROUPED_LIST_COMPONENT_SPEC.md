# 卡片式列表 Grouped List 设计规范

> **组件 ID**：`form`  
> **大类**：数据  
> **变体数量**：52 种（46 基础变体 + 6 组合变体）

## 🔒 强约束声明

@LINT F1, F3, F4, S11, S17, TK1, DV1
@SPEC_OF_TRUTH 本文件为 Grouped List（form）权威规范

### @MUST
- 变体仅限 L1-L11 × R0-R5 共 52 种（含 46 基础 + 6 Combo），经约束矩阵过滤
- 容器宽度 396px 卡片式
- 分割线 0.5px + `var(--border-weak)`，左端与标题文本左边缘对齐，右侧固定 16px
- 同一卡片组内分割线长度必须一致，混排不一致须拆分为不同卡片组
- 层级上限 2 级（父→子）
- 整行禁用 `opacity: 0.4`，`pointer-events: none`

### @FORBIDDEN
- 分割线长度不一致仍保留为同组
- 发明注册表外的变体

## 1. 组件概述

卡片式列表（Inset Grouped List）是设置页面的核心布局组件，由背景容器、内容行、左侧区域、右侧区域、分隔线及底部说明文字组成。左右缩进且以圆角容器封装，适合任务驱动型界面，在复杂信息中快速定位功能或操作。

**子组件变体数量：46 个基础变体 + 6 个组合变体 = 52 个**

## 2. 属性定义

### 2.1 整体属性
| 属性名 | 标识 | 视觉特征 |
| :--- | :--- | :--- |
| 分割线 | Separator | 底部 0.5px 实线，颜色 `var(--border-weak)`；左端与标题文本左边缘对齐，右侧固定 16px：L1/L2 左侧 16px；L3–L6/L8–L11 左侧 52px（16px 行内边距 + 24px 图标 + 12px gap）；L7 左侧 68px（16px + 40px 头像 + 12px gap）；**同一卡片组内分割线长度必须一致，若混排导致不一致须拆分为不同卡片组** |
| 底部说明 | Bottom Hint | 组件下方 14px 辅助文字，颜色 `var(--text-secondary)`；上下内边距均为 8px，左右 32px；`display: flex; align-items: center; gap: 5px` |

### 2.2 左侧区域 (L) — 11 种
| 标识 | 名称 | 视觉特征 |
| :--- | :--- | :--- |
| L1 | 单行标题 | 17px 黑色文字 (`var(--text-primary)`) |
| L2 | 双行标题 | 17px 标题 + 14px 辅助说明 |
| L3 | 图标+单行标题 | `icons/empty_icon.svg`（24px 占位图标）+ 17px 文字，间距 12px |
| L4 | 图标+双行标题 | `icons/empty_icon.svg`（24px 占位图标）+ 17px 标题 + 14px 辅助说明 |
| L5 | 二级+单行标题 | `icons/secondary.svg`（24px 二级引导图标，颜色 `var(--icon-secondary)`）+ 17px 文字（从属层级） |
| L6 | 二级+双行标题 | `icons/secondary.svg`（24px 二级引导图标，颜色 `var(--icon-secondary)`）+ 17px 标题 + 14px 辅助说明（从属层级） |
| L7 | 头像+双行标题 | `icons/Avatar_40.svg`（40px 圆形头像占位）+ 17px 标题 + 14px 辅助说明 |
| L8 | 已勾选+单行标题 | `icons/tick.svg`（24px，`var(--brand-standard)`）+ 17px 标题，间距 12px |
| L9 | 未勾选+单行标题 | 无图标 + 17px 标题（与 L8 对应的未选状态，左侧缩进与 L8 保持一致） |
| L10 | 已勾选+双行标题 | `icons/tick.svg`（24px，`var(--brand-standard)`）+ 17px 标题 + 14px 辅助说明，间距 12px |
| L11 | 未勾选+双行标题 | 无图标 + 17px 标题 + 14px 辅助说明（与 L10 对应的未选状态） |

### 2.3 右侧区域 (R) — 6 种
| 标识 | 名称 | 视觉特征 |
| :--- | :--- | :--- |
| R0 | 为空 / None | 无右侧内容 |
| R1 | 跳转 / Detail | **可选**辅助信息文字（14px，行高 20px，`var(--text-secondary)`）+ `icons/chevron_right.svg`（16×16px 右箭头，颜色 `var(--icon-tertiary)`）；辅助信息可隐藏 |
| R2 | 辅助信息+下拉菜单 / Dropdown | **可选**辅助信息文字（14px，行高 20px，`var(--text-secondary)`）+ `icons/expand_list.svg`（16×16px 下拉箭头，颜色 `var(--icon-tertiary)`）；辅助信息可隐藏 |
| R3 | 辅助信息+头像+箭头 / Avatar | **可选**辅助信息文字（14px，行高 20px，`var(--text-secondary)`）+ `icons/Avatar_32.svg`（32px 圆形头像）+ `icons/chevron_right.svg`（16×16px 右箭头，颜色 `var(--icon-tertiary)`）；辅助信息和头像均可独立隐藏 |
| R4 | 开关 / Switch | 44×26px 胶囊开关，开启态背景 `var(--brand-standard)` |
| R5 | 勾选 / Checkbox | `icons/Checkbox_filled.svg`(选中) / `icons/Checkbox.svg`(未选中)（20px，`var(--brand-standard)`） |

---

## 3. 属性约束

| # | 约束规则 | 说明 |
| :--- | :--- | :--- |
| 1 | **L5（二级+单行标题）** 与 **L6（二级+双行标题）** 只能与 **R1（跳转）**、**R2（下拉菜单）**、**R4（开关）** 组合 | 二级缩进变体可搭配跳转、下拉菜单或开关 |
| 2 | **R3（辅助信息+头像+箭头）** 只能与 **L3（图标+单行标题）**、**L4（图标+双行标题）**、**L8-L11（tick 勾选类）** 组合 | 头像右侧仅限搭配图标型或 tick 勾选型左侧 |
| 3 | **L7（头像+双行标题）** 只能与 **R0（为空）**、**R5（勾选）** 组合 | 头像型左侧仅限搭配为空或勾选右侧 |
| 4 | **R1/R2/R3** 的辅助信息文字均可隐藏 | R1 只保留箭头；R2 只保留下拉箭头；R3 辅助信息和头像可各自独立隐藏 |
| 5 | **R0（为空）** 与 **R5（勾选）** 可与左侧任意类型搭配 | 无特定左侧限制，任意 L 均可配 R0 或 R5（受其他约束限制除外） |
| 6 | 只有当父项使用 **R4（开关）** 或左侧勾选（**L8/L10**）或右侧勾选（**R5**）时，才可触发子项出现/消失 | 父子关系触发条件更新 |
| 7 | **R4（开关）** 不能与 **L7（头像+双行标题）** 组合 | 头像型左侧不支持开关 |
| 8 | **L8、L9、L10、L11** 只能与 **R0/R1/R2/R3** 组合，不能与 **R4（开关）** 或 **R5（勾选）** 组合。**使用原则**：仅当右侧有额外功能（跳转/下拉/头像）时才使用左侧 tick；单纯勾选选择使用 **R5（右侧勾选）** | 左侧 tick 不支持开关和右侧勾选并用 |
| 9 | 同一卡片组内，**L8/L9** 组合互斥：只能有一行处于 L8（已勾选）状态 | 单行 tick 左侧互斥，同时只有一个已勾选 |
| 10 | 同一卡片组内，**L10/L11** 组合互斥：只能有一行处于 L10（已勾选）状态 | 双行 tick 左侧互斥，同时只有一个已勾选 |

### 3.1 有效变体矩阵

|  | R0 | R1 | R2 | R3 | R4 | R5 | 小计 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **L1** | ✅ | ✅ | ✅ | — | ✅ | ✅ | 5 |
| **L2** | ✅ | ✅ | ✅ | — | ✅ | ✅ | 5 |
| **L3** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6 |
| **L4** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6 |
| **L5** | — | ✅ | ✅ | — | ✅ | — | 3 |
| **L6** | — | ✅ | ✅ | — | ✅ | — | 3 |
| **L7** | ✅ | — | — | — | — | ✅ | 2 |
| **L8** | ✅ | ✅ | ✅ | ✅ | — | — | 4 |
| **L9** | ✅ | ✅ | ✅ | ✅ | — | — | 4 |
| **L10** | ✅ | ✅ | ✅ | ✅ | — | — | 4 |
| **L11** | ✅ | ✅ | ✅ | ✅ | — | — | 4 |
| **合计** | | | | | | | **46** |

### 3.2 组合变体（6 个）

| ID | 组合方式 | 有分组标题 | 有底部说明 | 列表行数 |
| :--- | :--- | :---: | :---: | :---: |
| Combo1 | 分组标题+单表单+底部说明 | ✓ | ✓ | 1 |
| Combo2 | 分组标题+单表单 | ✓ | — | 1 |
| Combo3 | 单表单+底部说明 | — | ✓ | 1 |
| Combo4 | 分组标题+多表单+底部说明 | ✓ | ✓ | ≥2 |
| Combo5 | 分组标题+多表单 | ✓ | — | ≥2 |
| Combo6 | 多表单+底部说明 | — | ✓ | ≥2 |

---

## 4. UI 设计规格

- **容器宽度**: 428px（适配 iOS 标准宽度）
- **行高**: 单行(L1/L3/L5/L8/L9) 56px；双行(L2/L4/L6/L7/L10/L11) 72px
- **内边距**: 左右 16px
- **背景色**: 页面 `var(--bg-secondary)`，组件 `#FFFFFF`
- **字体**: 标题 `17px var(--text-primary)`；描述 `14px var(--text-secondary)`，line-height: 1.2, margin-top: 1px
- **分割线**: 0.5px 实线，颜色 `var(--border-weak)`；左端与标题文本左边缘对齐，右侧固定 16px
  - L1/L2（无图标）：左侧 16px
  - L3–L6/L8–L11（24px 图标/tick）：左侧 52px（= 16px 行内边距 + 24px 图标 + 12px gap）
  - L7（40px 头像）：左侧 68px（= 16px 行内边距 + 40px 头像 + 12px gap）
  - **同一卡片组内分割线长度必须一致，若混排导致不一致须拆分为不同卡片组**
- **卡片圆角**: 12px，Inset Grouped 样式
- **组间距**: spacing-m（12px）（同类卡片容器相邻规则）
- **右侧区域间距**: gap: 4px, margin-left: 12px
- **左侧区域间距**: gap: 12px

### 4.2 文本截断规则

**卡片式列表采用两段式 Flex 布局**：`[左区 flex:1] | [右区 flex-shrink:0]`

Flex 算法分配顺序：
1. 先固定右区（箭头/开关/勾选）的宽度
2. 剩余空间全部分配给左区（`flex:1`）

截断规则：
1. **左区**：`flex:1; min-width:0`，左区宽度由 flex 算法自动分配
2. **图标**（L3/L4/L5/L6/L7）：`flex-shrink:0`，不被压缩，始终完整显示
3. **文字容器（text-group）**：`flex:1; min-width:0`，承接左区剩余空间后可继续压缩
4. **标题（title）**：单行，超出 text-group 右边界省略（`…`）
5. **副标题（subtitle）**：单行，同上省略
6. **右区辅助文字（helper-text）**：`max-width:120px`，防止辅助文字过长挤压左区，超出省略

---

## 4.1 CSS 实现参考

### 外层容器

```css
.form-container {
    width: 428px;
    background: var(--bg-secondary);        /* ⚠️ 必须使用 --bg-secondary，不可用白色 */
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
}
```

### 表单行

```css
.form-row {
    display: flex;
    align-items: center;
    padding: 0 16px;
    width: 100%;
    background: var(--bg-bottom);
    position: relative;
    border-radius: 12px;        /* 单行独立卡片时 */
    overflow: hidden;
}
.form-row.single-line { height: 56px; }
.form-row.double-line { height: 72px; }
```

### 左侧区域

```css
.form-row .left-area {
    flex: 1;
    min-width: 0;           /* 允许 flex 子项被压缩，配合右区固定宽度自动分配空间 */
    display: flex;
    align-items: center;
    gap: 12px;
    overflow: hidden;
}
/* 图标+文字的文字容器：可被压缩 */
.form-row .left-area .text-group {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.form-row .title {
    font-size: 17px;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.form-row .subtitle {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.2;
    margin-top: 1px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

### 右侧区域

```css
.form-row .right-area {
    display: flex;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
    margin-left: 12px;
}
.form-row .helper-text {
    font-size: 14px;
    line-height: 20px;
    color: var(--text-secondary);
}
/* L5/L6 左侧二级引导图标（secondary.svg）：固定使用 --icon-secondary 着色 */
.form-row .left-area .icon-secondary-left {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
    color: var(--icon-secondary);       /* SVG currentColor 着色 */
    /* 若使用 <img> 标签，改用 CSS filter 实现：*/
    /* filter: opacity(0.6);             对应 --icon-secondary rgba(60,60,67,0.6) */
}
/* R1/R2/R3 方向图标（chevron_right、expand_list）：16×16px，次级图标色 */
.form-row .right-area .icon-arrow,
.form-row .right-area .icon-expand {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
    color: var(--icon-tertiary);        /* SVG currentColor 着色 */
    /* 若使用 <img> 标签，改用 CSS filter 实现：*/
    /* filter: opacity(0.3);             对应 --icon-tertiary rgba(60,60,67,0.3) */
}
.form-switch {
    width: 44px;
    height: 26px;
    background: var(--brand-standard);
    border-radius: 13px;
    position: relative;
    cursor: pointer;
    transition: background 200ms ease-out;
}
.form-switch.off {
    background: var(--fill-secondary);
}
.form-switch::after {
    content: '';
    position: absolute;
    right: 2px;
    top: 2px;
    width: 22px;
    height: 22px;
    background: var(--bg-bottom);
    border-radius: 50%;
    transition: right 200ms ease-out, left 200ms ease-out;
}
.form-switch.off::after {
    right: auto;
    left: 2px;
}
```

### 组合容器（分组标题+多行+底部说明）

```css
.form-group {
    background: var(--bg-secondary);
    padding: 0;
    border-radius: 0;
    width: 428px;
    display: flex;
    flex-direction: column;
}
.form-group-header {
    display: flex;
    width: 428px;
    padding: 8px 32px;
    align-items: flex-start;
    color: var(--text-secondary);
    font-feature-settings: 'liga' off, 'clig' off;
    font-family: "PingFang SC";
    font-size: 16px;
    font-style: normal;
    font-weight: 500;
    line-height: 22px;
}
.form-group-content {
    background: var(--bg-bottom);
    margin: 0 16px;
    border-radius: 12px;
    overflow: hidden;
    width: 396px;
}
.form-group-content .form-row {
    border-radius: 0;           /* 组合内行不单独圆角 */
    padding: 0 16px;
    width: 100%;
    margin: 0;
    background: transparent;
}
.form-group-content .form-row .left-area {
    gap: 12px;
}
.form-group-footer {
    display: flex;
    width: 428px;
    padding: 8px 32px;
    align-items: center;
    gap: 5px;
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.4;
}
/* 分割线左端与标题文本左边缘对齐，右侧固定 16px */
.form-separator {
    height: 0.5px;
    background: var(--border-weak);
    margin-left: 16px;      /* L1/L2：无图标，左侧 16px */
    margin-right: 16px;
}
.form-separator.inset-icon {
    margin-left: 52px;      /* L3–L6/L8–L11：16px + 24px 图标 + 12px gap */
}
.form-separator.inset-avatar {
    margin-left: 68px;      /* L7：16px + 40px 头像 + 12px gap */
}
```

<!-- matrix 展示容器样式（.grouped-card）为变体矩阵 UI 框架内部样式，不属于组件本身，已省略 -->

---

## 5. 组合关系

卡片式列表在设置页面中，同一卡片内的表单行之间存在 3 种组合关系，决定行的排列、状态联动和交互行为。

### 5.1 同类关系（Grouping）

**定义**：当业务、功能等属于同一类别时，多个列表行可聚合为一个卡片；不同类型的子组件也可以组合在同一卡片内。

**组合结构**：
- **分组标题 (Group Title)**: 可选，位于组合上方，左对齐
- **表单行 (Form Item)**: 核心内容
- **底部说明 (Bottom Description)**: 可选，位于组合下方，支持文本及 Textlink

> 卡片式列表组合支持选配分组标题、底部说明，也可以不配置。

**视觉规则**：
1. 组合采用 Inset Grouped 排版，宽度 396px（428px - 左右 16px 外边距）
2. 整个组合卡片 12px 圆角，父容器统一包裹
3. 分割线仅在组合内相邻项之间显示；左端与标题文本左边缘对齐，右侧固定 16px：L1/L2 左侧 16px；L3–L6/L8–L11 左侧 52px；L7 左侧 68px；**同一卡片组内分割线长度必须一致，若混排导致不一致须拆分为不同卡片组**
4. 分组标题距卡片顶边 4px（spacing-xs），卡片底边距底部说明 4px（spacing-xs）
5. 组合内单体高度由内容自适应，多项组合纵向顶部对齐

**规则**：
- 同类行**必须相邻排列**，通过分割线区隔
- 不同类型的子组件（如 L1+R1 与 L3+R4）允许混排在同一卡片内
- 组间以页面背景间距 **spacing-m（12px）** 区隔

**同组混排限制**：
- **类型 A（可自由混排）**：L1/L2 可相互混排
- **类型 B（可与任意类型混排）**：L5/L6（二级类型）、L8/L9/L10/L11（勾选类型）可与同卡片内任意其他左侧类型混排
- **类型 C（不可混排）**：L7（头像+双行标题）独占卡片，不与其他左侧类型混排

### 5.2 互斥关系（Mutual Exclusion）

**定义 A — 右侧勾选互斥（R5）**：当右侧为 **R5（勾选 / Checkbox）** 时，该组内同一时刻只能有一个 R5 处于选中态，其余行右侧为 **R0（为空）**，且组内所有行的左侧类型必须相同。

**定义 B — 左侧 tick 互斥（L8/L9 和 L10/L11）**：
- 同一卡片组内，**L8/L9** 行只能有一行处于 **L8（已勾选）**状态，其余均为 L9（未勾选）
- 同一卡片组内，**L10/L11** 行只能有一行处于 **L10（已勾选）**状态，其余均为 L11（未勾选）
- L8/L9 与 L10/L11 不可在同一卡片组内混用

**通用规则**：
- 互斥选项**必须位于同一卡片**
- 选中态即时生效，无需二次确认
- 切换过渡 ≤ 200ms `ease-out`

### 5.3 父子关系（Parent-Child）

**定义**：父行的交互状态控制下方一个或多个子行的出现与消失。

**触发条件**（三种，选其一）：
- 父行右侧为 **R4（开关）**：开关开启时子行出现，关闭时子行消失
- 父行左侧为 **L8/L10（已勾选 tick）**：处于已勾选状态时子行出现，切换为 L9/L11（未勾选）时子行消失
- 父行右侧为 **R5（勾选）**：处于选中状态时子行出现，取消选中时子行消失

#### 情况一：子列表 < 3 个

- 父子**必须在同一卡片组合内**
- 子行左侧限 **L5/L6（二级缩进变体）**，通过 L 型引导图标表达层级
- 子行右侧限 **R1（跳转）**、**R2（下拉菜单）**、**R4（开关）**（约束规则 #1）
- 父行触发条件关闭时，子行自动隐藏；触发条件开启时，子行自动展示

#### 情况二：子列表 ≥ 3 个

- 子列表可以**单独作为一个卡片组合**出现在父卡片下方
- 子列表**不限定左侧/右侧类型**，可使用任意有效的 L×R 组合
- 父行触发条件关闭时，子卡片整体隐藏；触发条件开启时，子卡片整体展示

**通用规则**：
- 层级上限 **2 级**（父→子），禁止嵌套

---

## 6. 点击/触发行为定义

| 右侧类型 | 点击热区 | 触发行为 | 说明 |
|----------|---------|---------|------|
| **R0（为空）** | 整行可点击 | 执行自定义操作 | 可与任意左侧类型搭配（受其他约束限制除外）；当左侧为 L1 时标题字色可变为**警示色**（`var(--accent-red)`）或**链接色**（`var(--brand-standard)`），用于表达危险操作或链接跳转语义 |
| **R1（跳转）** | 整行可点击 | Push 跳转到新页面 | 点击后导航至目标页面 |
| **R2（辅助信息+下拉菜单）** | 整行可点击 | 弹出**有勾选菜单（Menu-C）** | 菜单为单选互斥，选中后菜单关闭，R2 辅助信息文字更新为选中项 |
| **R3（头像+箭头）** | 头像与箭头作为整体区域可点击 | Push 跳转到新页面 | 头像+箭头为一个完整的点击热区 |
| **R4（开关）** | 仅开关热区可点击 | 切换开关状态 | 行其他区域不响应点击；开关切换可触发父子关系联动 |
| **R5（勾选）** | 整行可点击 | 触发勾选/取消勾选 | 在互斥关系中，选中当前行同时取消其他行的勾选 |

---

## 7. 交互状态规范

### 7.1 表单行状态

| 状态 | 样式 | 触发条件 |
|------|------|---------|
| 默认 | 背景 `#FFFFFF`，文字 `var(--text-primary)` | — |
| 按下 | 背景 `rgba(0,0,0,0.04)` | `touchstart` / `mousedown` |
| 禁用 | 整行 `opacity: 0.40`，`pointer-events: none` | 父子关系触发 |

### 7.2 Switch 开关状态

| 状态 | 样式 | 说明 |
|------|------|------|
| 开启 | 背景 `#0099FF`，滑块居右 | 功能生效，默认状态（无额外 class） |
| 关闭 | 背景 `rgba(120,120,128,0.16)`，滑块居左 | 添加 `.off` class |
| 禁用 | 整行 `opacity: 0.40`，开关不可操作 | 父子关系触发 |

**交互实现**：点击开关通过 `classList.toggle('off')` 切换状态。使用全局事件委托：
```javascript
document.addEventListener('click', function(e) {
    const switchEl = e.target.closest('.form-switch');
    if (switchEl) {
        e.stopPropagation();
        switchEl.classList.toggle('off');
    }
});
```

### 7.2.1 Checkbox 勾选状态

| 状态 | 图标 | 说明 |
|------|------|------|
| 选中 | `Checkbox_filled.svg` (20×20) | 蓝色实心勾选框 |
| 未选中 | `Checkbox.svg` (20×20) | 灰色空心勾选框 |

**交互实现**：点击勾选图标通过替换 `img.src` 切换状态：
```javascript
document.addEventListener('click', function(e) {
    const checkImg = e.target.closest('img[src*="Checkbox"]');
    if (checkImg) {
        e.stopPropagation();
        if (checkImg.src.includes('Checkbox_filled')) {
            checkImg.src = checkImg.src.replace('Checkbox_filled', 'Checkbox');
        } else {
            checkImg.src = checkImg.src.replace('Checkbox.svg', 'Checkbox_filled.svg');
        }
    }
});
```

### 7.3 动画规范

| 交互 | 时长 | 曲线 | 说明 |
|------|------|------|------|
| 行按下高亮 | 100ms | `ease-out` | 背景色变化 |
| 行释放恢复 | 150ms | `ease-out` | 恢复默认背景 |
| Switch 切换 | 200ms | `ease-out` | 滑块位移 + 背景色渐变 |
| 子行展开 | 250ms | `ease-in-out` | `max-height` + `opacity` |
| 子行收起 | 200ms | `ease-in` | 快收慢展 |
| 禁用态切换 | 150ms | `ease-out` | `opacity` 过渡 |

(注：Checkbox 互斥切换动画 ≤ 200ms ease-out)

---

## 8. 嵌入与联动场景

### 8.1 作为嵌套内容嵌入半屏浮层
- Grouped List 可嵌入 **HalfScreenOverlay（半屏浮层）** 内部，作为半屏表单
- 嵌入时宽度由半屏容器决定，去掉外部 margin（卡片宽度仍为 396px）
- 半屏浮层的 `canEmbed` 字段已声明支持列表/表单组件
- 引用：`HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md`

### 8.2 Textfield 嵌入
- Textfield（输入框）常嵌入 Grouped List 行中作为表单输入项
- B 类有标题型 Textfield 的标题区对应 Grouped List L 区
- 引用：`TEXTFIELD_COMPONENT_SPEC.md`

### 8.3 触发 Menu
- R2（辅助信息+下拉菜单）行点击后弹出 **Menu-C（有勾选菜单）**
- 菜单为单选互斥，选中后菜单关闭，R2 辅助信息文字更新为选中项
- 引用：`MENU_COMPONENT_SPEC.md`
