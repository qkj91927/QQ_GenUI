# 数据筛选 DataFilter 组件设计规范

> **组件 ID**：`data_filter`  
> **大类**：数据  
> **变体数量**：16 种（A页签4 + B分段选择4 + C下拉筛选1 + D标签5 + E面包屑2）

## 🔒 强约束声明

@LINT F1, F4, TK1
@SPEC_OF_TRUTH 本文件为 DataFilter 权威规范

### @MUST
- 变体仅限 A1-A4（页签）+ B1-B4（分段选择）+ C1（下拉筛选）+ D1-D5（标签）+ E1-E2（面包屑），共 16 种
- A 页签容器底线：0.5px solid `var(--border-default)`（组件内部强描边）
- **A 页签模式二选一**：① 等分模式（A1-A3，4-6 个）；② 横滑模式（A4，≥7 个或文本溢出时）。**统一 `padding: 0 16px`**（内容区 396px）
- A 等分模式项宽：**A1 (4 个) = 96px · A2 (5 个) = 80px · A3 (6 个) = 68px**；`justify-content: center`，文本居中
- A 横滑模式：`justify-content: flex-start; gap: 24px; overflow-x: auto`，项宽 auto 自适应文本
- A 指示器：宽 32px，**中心与页签文字中心对齐**（`transform: translateX(-50%)`），仅选中态可见
- B 分段选择内部垂直分隔线：0.5×16px + `var(--border-default)`
- B 选中项左右相邻分隔线 `opacity: 0`，其余恢复 `opacity: 1`
- E2 超限渐隐使用 `mask-image: linear-gradient(to right, transparent 0%, black 24px)`
- **吸顶复合角色**（S24/S27）：① **A 页签 = L2 层**（紧跟 NavBar 时可吸顶）；② **D 标签 / E 面包屑 = L3 层**（可作最下层吸顶）；③ 吸顶时 A 页签底线 `var(--border-default)` 0.5px 作整体底线承担者；④ D / E 自身无底线，作最下层时整体吸顶无分割线

### @FORBIDDEN
- 发明注册表外的变体
- 修改分隔线尺寸或颜色
- 选中态切换时未同步更新分隔线可见性
- E2 渐隐依赖特定背景色（必须用 mask-image）
- **B 分段选择 / C 下拉筛选 参与吸顶复合**（S27）：B 分段与 C 下拉**永不吸顶**，只能作为页面内容流中的普通组件
- 同层多组件并排吸顶（如两个页签并列 / 标签+面包屑并排）
- **A 页签伪左对齐**：非等分且非横滑的"左对齐固定宽度"布局 · `padding` 左右不对称 · 等分模式下手写 `justify-content: flex-start` · 横滑模式不设 `overflow-x: auto`

## 1. 概述

数据筛选（DataFilter）是页面中用于分类切换、条件筛选与层级导航的组合组件族，包含页签、分段选择、下拉筛选、标签、面包屑五种子组件类型，适用于不同信息架构与交互场景。

## 2. 变体总览

| 编号 | 类型 | 名称 | 数量/级数 | 容器高度 |
|------|------|------|-----------|----------|
| A.页签 A1 | 页签 | 四页签 | 4 | 48px |
| A.页签 A2 | 页签 | 五页签 | 5 | 48px |
| A.页签 A3 | 页签 | 六页签 | 6 | 48px |
| A.页签 A4 | 页签 | 横滑 | 8 | 48px |
| B.分段选择 B1 | 分段选择 | 二选项 | 2 | 40px |
| B.分段选择 B2 | 分段选择 | 三选项 | 3 | 40px |
| B.分段选择 B3 | 分段选择 | 四选项 | 4 | 40px |
| B.分段选择 B4 | 分段选择 | 五选项 | 5 | 40px |
| C.下拉筛选 C1 | 下拉筛选 | 一按钮 | 1 | 40px |
| D.标签 D1 | 标签 | 单行横滑 | 6 | 40px |
| D.标签 D2 | 标签 | 单行4个 | 4 | 40px |
| D.标签 D3 | 标签 | 单行3个 | 3 | 40px |
| D.标签 D4 | 标签 | 单行2个 | 2 | 40px |
| D.标签 D5 | 标签 | 双行2个 | 2 | 62px |
| E.面包屑 E1 | 面包屑 | 标准 | 4 | 24px |
| E.面包屑 E2 | 面包屑 | 超限渐隐 | 6 | 24px |

## 3. 布局规格

### 3.1 A. 页签 Tab

- **容器**：宽 **428px**，高 **48px**，透明背景（跟随页面背景色），底部 0.5px 分割线 `var(--border-default)`，`overflow: hidden`
- **统一左右边距**：`padding: 0 16px`（两种模式一致），内容区 **396px**
- **等分模式**（A1-A3，4-6 个）：`justify-content: center`，文本居中
  - A1 (4 页签)：**每项 96px**（4×96=384，居中 6px 两侧余白）
  - A2 (5 页签)：**每项 80px**（5×80=400，余 ±2px 由 overflow:hidden 裁剪，视觉可接受）
  - A3 (6 页签)：**每项 68px**（6×68=408，居中分布内容区 396px，余 ±6px 裁剪可接受）
- **横滑模式**（A4，≥7 个 或 文本溢出时）：`justify-content: flex-start; gap: 24px`，页签项宽度**自适应文本内容**（`width: auto; flex-shrink: 0`），支持左右滑动（`overflow-x: auto`，隐藏滚动条：`scrollbar-width: none` + `::-webkit-scrollbar { display: none }`）
- **文本**：16px / 22px PingFang SC，未选中 400 / 选中 500，颜色 `var(--text-primary)`
- **指示器**：宽 32px，高 3px，圆角 1.5px，品牌蓝 `var(--brand-standard)`，底部对齐（`position: absolute; bottom: 0; left: 50%; transform: translateX(-50%)`），**中心与页签文字中心对齐**，仅选中态可见（非选中 `opacity: 0`）

### 3.2 B. 分段选择 Segment

- **外层行**：`display: inline-flex`，宽度自适应内容，透明背景，`padding: 0 16px`
- **容器**：`display: inline-flex`，宽度自适应内容，背景 `var(--fill-tertiary)`，圆角 12px
- **分段栏**：高 40px，圆角 12px，背景 `var(--fill-tertiary)`
- **选项宽度**：每项 52px，总宽度 = 52.5 × n（含分隔线）
- **分隔线**：宽 0.5px，高 16px，颜色 `var(--border-default)`，选中项相邻分隔线隐藏（`opacity: 0`）
- **文本**：14px / 20px PingFang SC，未选中 400 色 `var(--text-secondary)` / 选中 500 色 `var(--text-primary)`
- **选项数量**：2 / 3 / 4 / 5 个
- **组合规则**：可独占一行，也可与相同/不同类型组件同行排列，间距 16px

### 3.3 C. 下拉筛选 Dropdown

- **外层行**：`display: inline-flex`，宽度自适应内容，透明背景，`padding: 0 16px`，`box-sizing: border-box`
- **容器**：`display: inline-flex`，宽度自适应内容，背景 `var(--fill-tertiary)`，圆角 12px，多按钮时 `gap: 16px`
- **按钮**：高 40px，圆角 12px，背景 `var(--fill-tertiary)`，内边距 `0 12px`，内部 `gap: 4px`（文本与箭头间距）
- **文本**：14px / 20px PingFang SC 400，颜色 `var(--text-primary)`
- **箭头**：`icons/chevron_down.svg`（14×14px），fill 颜色 `var(--text-primary)`
- **按钮数量**：仅 1 个（组件仅包含按钮，不包含弹窗菜单）
- **交互行为**：点击按钮后弹出菜单（菜单不属于此组件本身，由 Menu 组件承担）

### 3.4 D. 标签 Tag

- **维度控制**：标签组件由**单行/双行**和**平铺/横滑**两个变量控制，共 5 种变体
- **容器**：宽 428px，透明背景（跟随页面背景色），`overflow: hidden`
  - 平铺模式：内边距 `0 16px`，标签区宽 396px
  - 横滑模式：内边距 `0`，标签区内边距 `0 16px`，支持横向滚动（`overflow-x: auto`，隐藏滚动条：`scrollbar-width: none` + `::-webkit-scrollbar { display: none }`）
- **标签项**：圆角 12px，背景 `var(--fill-tertiary)`，项间距 `gap: 8px`，`flex-shrink: 0`
- **单行横滑**（D1，6 个标签）：容器高 40px，标签高 40px，每个标签 `padding: 0 16px` 自适应宽度，第一个文本"横滑标签"、其余"标签"
- **单行4/3/2个**（D2-D4）：容器高 40px，标签高 40px，宽度 = `(396 - (n-1)×8) / n`，等分填满
- **双行2个**（D5）：容器高 62px，标签高 62px，宽度 = `(396 - (n-1)×8) / n`，等分填满，每个标签包含标题行和描述行
- **单行文本**：14px / 20px PingFang SC
  - 未选中：font-weight 400，颜色 `var(--text-secondary)`
  - 选中：font-weight 500，颜色 `var(--text-primary)`
- **双行文本**：
  - 标题：14px / 20px PingFang SC，未选中 400 `var(--text-secondary)` / 选中 500 `var(--text-primary)`
  - 描述：14px / 20px PingFang SC 400，未选中 `var(--text-tertiary)` / 选中 `var(--text-secondary)`

### 3.5 E. 面包屑 Breadcrumb

- **容器**：宽 428px，高 24px，透明背景（跟随页面背景色），`overflow: hidden`
- **标准模式**（E1，4 级）：内边距 `0 16px`，展示 4 级目录，最后一级为当前页
- **超限渐隐模式**（E2，6 级）：内部裁切容器 412px 宽，`overflow: hidden`，内容向左偏移 `-92px`，前面的目录溢出不可见，左侧 24px 渐隐通过 `mask-image: linear-gradient(to right, transparent 0%, black 24px)` 实现（不依赖特定背景色），第2级文本为"目录超限渐隐"
- **层级文本**：14px / 20px PingFang SC 500，`white-space: nowrap`，`flex-shrink: 0`
  - 中间层级：颜色 `var(--text-secondary)`
  - 最后层级（当前页）：颜色 `var(--text-primary)`
- **分隔符**：12×12 右箭头 chevron 图标，颜色 `var(--border-default)`（与分割线 token 统一），`margin: 0 8px`

## 4. 展示规则

- 每类子组件（页签/分段选择/下拉筛选/标签/面包屑）使用独立的**分段选择器**控制展示的变体
- 点击分段选择器的不同选项，切换显示该类型下的不同变体
- 当某类子组件只有 1 个变体时（如下拉筛选仅 C1），**不显示分段选择器**，直接展示

## 5. 组件组合规则

### 5.1 合法组合场景（3 种）

| 场景 | 组合 | 布局 | 适用 |
|------|------|------|------|
| **场景 A · 视图切换 + 排序** | B × 1 + C × 1 | `flex-start`，gap 16px | 时间维度切换 + 排序 |
| **场景 B · 多条件筛选** | C × 2-3（上限 **3 个**）| `flex-start`，gap 16px | 商品筛选（类别+品牌+价格）|
| **场景 C · 文件多维度筛选** | **B × 2-3 + C × 1** | `flex-start`，gap 16px | 文件管理（类型+排序+筛选）|

> 独占一行也合法：B 或 C 可以作为唯一元素出现在一行。

### 5.2 容器规格

```css
.df-combo-row {
    width: 428px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 16px;                       /* 同行组件间距 */
    padding: 0 16px;                 /* 左右各 16px，与 A 页签统一 */
    box-sizing: border-box;
}
```

### 5.3 @MUST 约束

- 同行组合仅允许 3 种：**B+C** / **C×2-3** / **B×2-3+C×1**
- C 按钮**最多 3 个**（超过改用 HSO 筛选面板）
- B 分段**最多 3 个**（超过视觉压迫）
- **禁止** A 页签 / D 标签 / E 面包屑加入组合行（这些是独立 chrome 或分类组件）
- 统一 `padding: 0 16px` + `gap: 16px`

### 5.4 正确使用 ASCII 示例

**示例 1 · 视图切换 + 排序（场景 A）**：
```
┌─ 428px 通栏 ───────────────────────────┐
│←16→ [日 │ 周 │ 月]  ←16→  [价格 ▼]     │
│      B2 三选项              C1 下拉      │
└────────────────────────────────────────┘
```

**示例 2 · 多条件筛选（场景 B · 上限 3 个 C）**：
```
┌─ 428px 通栏 ───────────────────────────┐
│←16→ [类别 ▼] ←16→ [品牌 ▼] ←16→ [价格 ▼]│
│       C1          C1           C1       │
└────────────────────────────────────────┘
```

**示例 3 · 文件多维度筛选（场景 C · B×2+C×1）**：
```
┌─ 428px 通栏 ───────────────────────────┐
│←16→[列表│宫格]←16→[已下载│未下载]←16→[文件类型▼]│
│       B1 二选项    B1 二选项        C1 下拉    │
└────────────────────────────────────────┘
```

### 5.5 @FORBIDDEN 约束

- ❌ 组合行混入 A 页签 / D 标签 / E 面包屑
- ❌ C × 4+ 同行（改用 HSO 筛选面板）
- ❌ B × 4+ 同行
- ❌ 组合总宽度超过 428px（需要减少元素数量）
- ❌ 不设 `padding: 0 16px` 或 `gap: 16px`
- ❌ 通用：所有组件仅输出净内容高度，上下间距由外部间距组件提供

## 6. 交互行为

### 6.1 分段选择分隔线隐藏规则
- 选中项（`.selected`）左右两侧的相邻分隔线（`.df-segment-divider`）`opacity` 设为 `0`
- 其余分隔线 `opacity` 恢复为 `1`
- 切换选项时需动态更新分隔线可见性

### 6.2 页签选中指示器
- 仅 `.selected` 项的指示器（`.df-tab-indicator`）可见
- 非选中项指示器 `opacity: 0`

### 6.3 面包屑渐隐遮罩
- E2 超限渐隐模式通过 `.overflow-left` class 控制左侧渐隐
- 使用 `mask-image: linear-gradient(to right, transparent 0%, black 24px)` 实现，不依赖特定背景色
- 添加 `.overflow-left` class 后生效，无该 class 时内容完整显示

### 6.4 横滑模式滚动
- 页签 A4 和标签 D1 均支持横向滚动，滚动条通过 CSS 隐藏
- 使用 `-webkit-overflow-scrolling: touch` 优化移动端滚动体验

## 7. 设计 Token 映射

| Token 名 | 值 | 用途 |
|-----------|-----|------|
| `--brand-standard` | `#0099FF` | 页签指示器 |
| `--text-primary` | `var(--text-primary)` / `#1A1C1E` | 主文本色、标签选中色 |
| `--text-secondary` | `var(--text-secondary)` / `#6A6B6D` | 分段选择未选中色、标签未选中色、双行标签选中描述色 |
| `--text-tertiary` | `var(--text-tertiary)` | 双行标签未选中描述色 |
| `--fill-tertiary` | `var(--fill-tertiary)` | 分段/下拉/标签背景色 |
| `--border-default` | `var(--border-default)` | 页签底线、分段分隔线 |

## 8. 使用场景

- **页签**：适用于顶部或区域级信息分类切换（如：消息/通讯录/发现/我）
- **分段选择**：适用于同级视图的模式切换（如：日/周/月/年）
- **下拉筛选**：适用于条件筛选或排序切换（如：最新/最热/综合排序），点击后弹出菜单
- **标签**：适用于分类标签入口（如：推荐/热门/新品/活动）
- **面包屑**：适用于多级层级导航回溯（如：设置 > 隐私 > 权限管理）

---

## 9. CSS 实现代码块

### 9.1 页签 Tab

```css
.df-tab-container {
    width: 428px;
    height: 48px;
    background: transparent;
    position: relative;
    overflow: hidden;
    border-bottom: 0.5px solid var(--border-default);
}
.df-tab-inner {
    width: 428px;
    height: 48px;
    display: flex;
    align-items: center;
    padding: 0 16px;                 /* 统一 16px 边距，两种模式一致 */
    box-sizing: border-box;
}
.df-tab-inner.mode-equal  { justify-content: center; }
.df-tab-inner.mode-scroll { justify-content: flex-start; gap: 24px; overflow-x: auto; }
.df-tab-inner::-webkit-scrollbar { display: none; }
.df-tab-item {
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    flex-shrink: 0;
}
/* 等分模式 · 项宽 */
.df-tab-inner.mode-equal .df-tab-item.count-4 { width: 96px; }
.df-tab-inner.mode-equal .df-tab-item.count-5 { width: 80px; }
.df-tab-inner.mode-equal .df-tab-item.count-6 { width: 68px; }
/* 横滑模式 · 自适应文本 */
.df-tab-inner.mode-scroll .df-tab-item { width: auto; }
.df-tab-item .df-tab-label {
    font-size: 16px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-primary);
    text-align: center;
    line-height: 22px;
}
.df-tab-item.selected .df-tab-label {
    font-weight: 500;
}
.df-tab-item .df-tab-indicator {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 32px;
    height: 3px;
    border-radius: 1.5px;
    background: var(--brand-standard);
}
.df-tab-item:not(.selected) .df-tab-indicator {
    opacity: 0;
}
```

### 9.2 分段选择 Segment

```css
.df-segment-row {
    display: inline-flex;
    background: transparent;
    padding: 0 16px;
    box-sizing: border-box;
}
.df-segment-container {
    display: inline-flex;
    align-items: center;
    background: var(--fill-tertiary);
    border-radius: 12px;
}
.df-segment-bar {
    height: 40px;
    background: var(--fill-tertiary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    position: relative;
    flex-shrink: 0;
}
.df-segment-item {
    width: 52px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    position: relative;
    flex-shrink: 0;
    cursor: pointer;
    transition: all 200ms ease-out;
}
.df-segment-item .df-seg-label {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-secondary);
    line-height: 20px;
    pointer-events: none;
}
.df-segment-item.selected {
    background: var(--bg-bottom);
    /* 无 box-shadow（与全局规范一致：除 Menu 外其他组件不使用阴影） */
}
.df-segment-item.selected .df-seg-label {
    font-weight: 500;
    color: var(--text-primary);
}
.df-segment-divider {
    width: 0.5px;
    height: 16px;
    background: var(--border-default);
    flex-shrink: 0;
    transition: opacity 200ms ease-out;
}
```

### 9.3 下拉筛选 Dropdown

```css
.df-dropdown-row {
    display: inline-flex;
    background: transparent;
    padding: 0 16px;
    box-sizing: border-box;
}
.df-dropdown-btn {
    height: 40px;
    background: var(--fill-tertiary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    padding: 0 12px;
    gap: 4px;
}
.df-dropdown-btn .df-dd-label {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-primary);
    line-height: 20px;
}
.df-dropdown-btn .df-dd-arrow {
    width: 16px;
    height: 16px;
}
```

### 9.4 标签 Tag

```css
.df-tag-container {
    width: 428px;
    background: transparent;
    display: flex;
    align-items: center;
    overflow: hidden;
}
.df-tag-container.flat-mode { padding: 0 16px; }
.df-tag-container.scroll-mode { padding: 0; }
.df-tag-inner {
    display: flex;
    gap: 8px;
    width: 396px;
}
.df-tag-inner.scroll-mode {
    width: auto;
    padding: 0 16px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
}
.df-tag-inner.scroll-mode::-webkit-scrollbar { display: none; }
.df-tag-item {
    height: 40px;
    background: var(--fill-tertiary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.df-tag-item .df-tag-label {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-secondary);
    line-height: 20px;
    white-space: nowrap;
}
.df-tag-item.selected .df-tag-label {
    font-weight: 500;
    color: var(--text-primary);
}
/* 双行标签 D5 */
.df-tag-item.df-tag-double {
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.df-tag-item .df-tag-title {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-secondary);
    line-height: 20px;
}
.df-tag-item .df-tag-desc {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 400;
    color: var(--text-tertiary);
    line-height: 20px;
}
.df-tag-item.selected .df-tag-title {
    font-weight: 500;
    color: var(--text-primary);
}
.df-tag-item.selected .df-tag-desc {
    color: var(--text-secondary);
}
```

### 9.5 面包屑 Breadcrumb

```css
.df-breadcrumb-container {
    width: 428px;
    height: 24px;
    background: transparent;
    display: flex;
    align-items: center;
    padding: 0 16px;
    position: relative;
    overflow: hidden;
}
/* 超限渐隐遮罩 — 使用 mask-image，不依赖背景色 */
.df-breadcrumb-container::before {
    content: '';
    display: none;
}
.df-breadcrumb-container.overflow-left {
    -webkit-mask-image: linear-gradient(to right, transparent 0%, black 24px);
    mask-image: linear-gradient(to right, transparent 0%, black 24px);
}
.df-breadcrumb-inner {
    display: flex;
    align-items: center;
    white-space: nowrap;
}
.df-breadcrumb-item {
    font-size: 14px;
    font-family: 'PingFang SC', -apple-system, sans-serif;
    font-weight: 500;
    color: var(--text-secondary);
    line-height: 20px;
    flex-shrink: 0;
}
.df-breadcrumb-item.current {
    color: var(--text-primary);
}
.df-breadcrumb-sep {
    width: 12px;
    height: 12px;
    margin: 0 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
```

---

## 10. 交互行为

### 10.1 页签 Tab 切换（组件内交互）

- 点击任一页签项后：该项添加 `.selected` class（文字加粗 500 + 显示指示器），其余项移除 `.selected`（文字 400 + 指示器隐藏）
- 同一时刻只有一个页签处于选中态（互斥）
- `cursor: pointer` 提供视觉反馈

**事件委托（全局）**：
```javascript
document.addEventListener('click', function(e) {
    const tabItem = e.target.closest('.df-tab-item');
    if (tabItem) {
        const container = tabItem.closest('.df-tab-inner');
        container.querySelectorAll('.df-tab-item').forEach(t => t.classList.remove('selected'));
        tabItem.classList.add('selected');
    }
});
```

### 10.2 分段选择 Segment 切换（组件内交互）

- 点击任一分段选项后：该选项变为选中态（白色背景滑块），其余恢复非选中态
- 选中项两侧相邻分隔线隐藏（`opacity: 0`），其余恢复（`opacity: 1`）
- 过渡动画：`transition: all 200ms ease-out`

```javascript
bar.addEventListener('click', (e) => {
    const clicked = e.target.closest('.df-segment-item');
    if (!clicked) return;
    bar.querySelectorAll('.df-segment-item').forEach(it => it.classList.remove('selected'));
    clicked.classList.add('selected');
    const items = Array.from(bar.querySelectorAll('.df-segment-item'));
    const dividers = Array.from(bar.querySelectorAll('.df-segment-divider'));
    const activeIdx = items.indexOf(clicked);
    dividers.forEach((d, di) => {
        d.style.opacity = (di === activeIdx - 1 || di === activeIdx) ? '0' : '1';
    });
});
```

### 10.3 标签 Tag 切换（组件内交互）

- 点击任一标签后：该标签添加 `.selected` class（font-weight 500 + 深色文字），其余移除 `.selected`（font-weight 400 + 浅色文字）
- 单行标签：选中/未选中态仅改变文字粗细和颜色
- 双行标签(D5)：选中描述色 `var(--text-secondary)`，未选中描述色 `var(--text-tertiary)`

### 10.4 下拉筛选 Dropdown（业务层）

- 组件仅渲染按钮态（含展开箭头图标）
- 点击后弹出有勾选菜单（Menu-C）由业务层实现
- 选中后按钮文字更新为选中项文案

### 10.5 面包屑 Breadcrumb（业务层）

- 点击面包屑中非当前级别的目录项由业务层实现页面导航
- 组件本身仅渲染静态层级展示
