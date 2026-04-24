# 顶部导航栏设计与技术规范 (NavBar Component Spec)

> **组件 ID**：`navbar`  
> **大类**：导航  
> **变体数量**：97 种（6L × 6C × 7R 经约束过滤）

## 🔒 强约束声明

@LINT F1, F4, F5, NV1, NV2, S14, S15, S17
@SPEC_OF_TRUTH 本文件为 NavBar 权威规范；与 matrix 渲染冲突时以此为准

### @MUST
- 容器高度固定 44px，宽度 428px 通栏
- 定位 `position: sticky; top: 0; z-index: 10`
- **内容滚动时必须从 NavBar 下方穿过，不可覆盖 NavBar**（S18）：页面 scroll container 须在 NavBar 之下，滚动内容不得盖过 chrome
- **吸顶复合 L1 层**（S24）：NavBar 为吸顶复合结构的 L1 层（必有）。可与 L2（DataFilter A 页签）、L3（DataFilter D 标签 / E 面包屑）组合共 4 种形态：L1 / L1+L2 / L1+L3 / L1+L2+L3。L1 单独时自身 NV2 规则生效；L2/L3 在场时 **NavBar 自身 NV2 禁用**，整体底线由 L2 页签承担（若 L3 在场则整体无底线）
- 页面最多 1 个 NavBar
- 底色从 `bg-*` 4-token 白名单选择（`bg-bottom` / `bg-secondary` / `bg-bottom-brand` / `bg-top`），默认 `var(--bg-bottom)`（NV1）
- 滚动态分割线：默认 `opacity: 0`；scrollY > 0 时显 `opacity: 1`，使用 `::after` 伪元素 + 0.5px + `var(--border-weak)`，`transition: opacity 200ms ease-out`（NV2）
- 变体必须在 L1-L6 × C0-C5 × R0-R6 经约束过滤后的 97 种内
- 约束矩阵：L2 只配 C1/C4+R1；L5 只配 R3；L6 只配 C0+R1/R2；C5 只配 L1/L3+R0/R1

### @FORBIDDEN
- 发明注册表外的变体
- 修改容器高度 44px / 宽度 428px / padding 等固定值
- 底色使用 `transparent` / `fill-*` / `backdrop-filter` 毛玻璃 / 硬编码 rgba / 品牌色 / 警示色
- 默认态永久显示分割线 / 使用 `border-bottom` / 厚度非 0.5px / 颜色非 `--border-weak`
- 分割线过渡使用非 `opacity` 属性（如 border-color / transform）
- 使用 `@media (prefers-color-scheme)` 切换暗色（必须走 `[data-theme]`）

本文件定义了移动端顶部导航栏母组件的系统化构建逻辑、属性定义及 UI 规范。

---

## 1. 组件构成 (Anatomy)

顶部导航栏（NavBar）采用三段式布局，各区域高度固定，逻辑独立：
- **左侧区域 (Left Area)**：功能动作（如返回、关闭）或个人标识（头像）。
- **中间区域 (Middle Area)**：核心内容展示（如标题、分段选择）。
- **右侧区域 (Right Area)**：页面级操作入口（如分享、提交、更多）。

---

## 2. 属性定义 (Properties)

### 2.1 左侧区域 (L)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| L1 | 返回 | `icons/chevron_left.svg`（返回箭头） |
| L2 | 返回+气泡 | `icons/chevron_left.svg`（返回箭头）+ **Badge A1-A3**（AIO 导航栏类气泡，浅灰底 `--fill-tertiary` + 黑字 `--text-primary`，14px Medium，圆角 12px）。**仅用于 AIO 页面**：返回 AIO 聊天列表时显示该列表未读消息数。组件级规范见 `md/BADGE_COMPONENT_SPEC.md`。 |
| L3 | 关闭 | `icons/close.svg`（关闭图标） |
| L4 | 图标 | `icons/empty_icon.svg`（占位，实际任务中替换） |
| L5 | 操作 | 17px 纯文字按钮 (如"操作") |
| L6 | 头像 | `icons/Avatar_32.svg`（36×36 头像占位）+ 昵称 + 描述信息 |

### 2.2 中间区域 (C)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| C0/Empty | Empty | 空白，用于左右分布或自定义 |
| C1 | 标题 | 17px 粗体居中标题 |
| C2 | 下拉标题 | 标题文字 + 向下箭头图标 |
| C3 | 标题+副标题 | 主标题 + 12px 辅助描述 |
| C4 | 标题+可点击副标题 | 主标题 + `--text-secondary` 12px 副标题 (具备点击态) |
| C5 | 分段选择 | 分段控制器 (Segmented Control)，胶囊背景 + 选中滑块 |

### 2.3 右侧区域 (R)
| 标识 | 属性名 | 视觉特征 |
| :--- | :--- | :--- |
| R0/Empty | Empty | 不显示任何内容 |
| R1 | 图标 | `icons/empty_icon.svg`（单个功能操作图标占位，实际任务中替换） |
| R2 | 双图标 | `icons/empty_icon.svg` × 2（两个横向排列的操作图标占位） |
| R3 | 操作 | 黑色 17px 动作文字 (如"完成") |
| R4 | 按钮 | 胶囊形高亮动作按钮 |
| R5 | 图标+按钮 | `icons/empty_icon.svg`（功能图标占位）与按钮的组合展示 |
| R6 | 勾选 | `icons/Checkbox_filled.svg`（蓝色勾选） |

---

## 3. 属性约束 (Constraints)

1. **[L2/返回+气泡] 强绑定**：
   - 只能与中间区域 **[C1/标题]** 或 **[C4/标题+可点击副标题]** 组合。
   - 只能与右侧区域 **[R1/图标]** 组合。（注：在配合 C4 时，允许组合 R3/操作）
   - **气泡子元素 ⇔ Badge A1-A3 双向独占**：L2 的"气泡"必须使用 Badge A1-A3 组件；Badge A1-A3 反向只能出现于此处。**仅用于 AIO 页面**（返回 AIO 聊天列表时显示未读消息数）。详见 `md/BADGE_COMPONENT_SPEC.md` §10。
2. **[L5/操作] 约束**：
   - 只能与右侧区域 **[R3/操作]** 组合（形成"取消/完成"或"取消/发送"等经典布局）。
3. **[L6/头像] 约束**：
   - 只能与中间区域 **[C0/Empty]** 组合。
   - 只能与右侧区域 **[R1/图标]** 或 **[R2/双图标]** 组合.
4. **[C4/标题+可点击副标题] 强绑定**：
   - 只能与左侧 **[L2/返回+气泡]** 和 right **[R3/操作]** 同时组合.
   - **UI 结构**: 副标题采用与 L6 描述组一致的双 icon + 分隔点结构.
5. **[C5/分段选择] 约束**：
   - 只能与左侧 **[L1/返回]** 或 **[L3/关闭]** 组合.
   - 只能与右侧 **[R1/图标]** 或 **[R0/Empty]** 组合.

---

## 4. 变体矩阵逻辑 (Variants Matrix)

根据 Figma 属性定义，该组件理论全量排列组合为：
- **理论组合总数**: 6 (L) × 6 (C) × 7 (R) = **252 种**。
- **约束过滤后有效变体数**: 应用第 3 节属性约束后，实际有效组合为 **97 种变体**。
- **渲染原则**: HTML 层仅渲染约束过滤后的有效变体，确保三层（HTML / JSON / MD）一致。

---

## 5. UI 设计规格 (Design Specs)

- **容器高度 (Height)**: 44px
- **左右安全区 (Padding)**: 16px
- **定位方式**: `position: sticky; top: 0; z-index: 10`（默认吸顶，始终固定在页面顶部，内容区在其下方滚动）
- **滚动态分割线（NV2）**: 默认态无分割线；当页面 scrollY > 0 时显示 0.5px 分割线（复用 divider A1 规范）。推荐用 `IntersectionObserver + sentinel` 实现，详见 §6.X。
- **布局逻辑**: 
  - **中间内容绝对居中**: 采用 `absolute` 定位，确保标题始终处于容器几何中心，不受左右侧按钮宽度不平衡的影响。
- **区域占位**:
  - 左右区域最小宽度: 60px (确保点击热区)
- **字体规范**:
  - 标题: `font-size: 17px; font-weight: 600; color: var(--text-primary)`
  - 副标题 (C3): `font-size: 12px; color: var(--text-secondary)`
  - 描述组 (C4/L6): `font-size: 10px; color: var(--text-secondary)`; 图标: `var(--icon-secondary)`
  - 动作文字: `font-size: 17px; color: var(--text-primary)`
- **图标尺寸**: 24x24px (大图标) / 10x10px (描述组图标)
- **品牌色**: `#0099FF`

---

## 6. CSS 实现代码块

> 全局字体：`'PingFang SC', -apple-system, sans-serif`。以下省略重复的 `font-family` 声明。

### 6.1 容器与三区域布局

```css
.navbar-row {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 16px; width: 428px; height: 44px;
    /* 底色：严格遵守 NV1（见 QUI_DESIGN_LINT_SKILL.md）。默认 --bg-bottom（白）；
       一体式时可同步页面底色（见白名单拼接矩阵）。禁止 transparent / fill-* / 硬编码 rgba。 */
    background: var(--bg-bottom);
    position: sticky; top: 0; z-index: 10;
}
/* NV2 · 滚动态分割线（复用 divider A1 视觉规范：0.5px + --border-weak） */
.navbar-row::after {
    content: '';
    position: absolute;
    left: 0; right: 0; bottom: 0;
    height: 0.5px;
    background: var(--border-weak);
    opacity: 0;
    transition: opacity 200ms ease-out;
    pointer-events: none;
}
.navbar-row.scrolled::after { opacity: 1; }
.navbar-row .left-area  { min-width: 60px; height: 44px; display: flex; align-items: center; justify-content: flex-start; z-index: 2; }
.navbar-row .middle-area { position: absolute; left: 50%; transform: translateX(-50%); width: 280px; height: 44px;
    display: flex; align-items: center; justify-content: center; text-align: center; overflow: hidden; z-index: 1; pointer-events: none; }
.navbar-row .middle-area > * { pointer-events: auto; }
.navbar-row .right-area { min-width: 60px; height: 44px; display: flex; align-items: center; justify-content: flex-end; gap: 12px; z-index: 2; }
```

### 6.2 元素样式速查表

| 选择器 | 关键属性 |
|--------|---------|
| `.nav-title` | 17px / 600 / `--text-primary` / nowrap / line-height: 1.2 |
| `.nav-subtitle` | 12px / 400 / `--text-secondary` / line-height: 1.2 / margin-top: 1px |
| `.nav-text` | 17px / 400 / `--text-primary` / cursor: pointer |
| `.nav-btn` | 72×32px / radius: 16px / bg: `--brand-standard` / 14px 500 / `--text-white` |
| `.nav-icon` | 24×24px |
| `.nav-search-bar` | flex:1 / 32px / radius: 8px / bg: `--fill-tertiary` / 14px / `--text-secondary` / margin: 0 8px |
| `.nav-segmented-control` | 196×36px / radius: 20px / bg: `--fill-tertiary` / padding: 4px |
| `.nav-segment-item` | flex:1 / 28px / 14px 500 / active: bg `--bg-bottom` / radius: 16px（**无 shadow，与全局规范一致**）|
| `.nav-badge` | 12px 500 / bg: `--border-default` / padding: 2px 6px / radius: 10px |
| `.nav-badge-neutral` | 14px **500** SF Pro Display / 24×29px / radius: 12px / bg: `--fill-secondary` / **position: absolute; left: 24px; top: 10px** |
| `.nav-checkbox-selected` | 24×24px（直接使用 `Checkbox_filled.svg`） |
| `.nav-segment-item` | cursor: pointer / transition: all 0.2s（补充交互属性） |
| `.clickable:hover` | opacity: 0.7 |

### 6.3 L6 头像组件

| 选择器 | 关键属性 |
|--------|---------|
| `.nav-profile` | flex / gap: 8px |
| `.nav-profile-avatar` | 32×32 / radius: 50%（**头像无描边，统一规范**） |
| `.nav-profile-img` | 36×36 / radius: 50% |
| `.nav-profile-name` | 17px / 500 / `--text-primary` |
| `.nav-profile-desc-group` | flex / gap: 4px / 10px / `--text-secondary` |
| `.nav-profile-desc-group img` | opacity: 0.6（匹配 `--icon-secondary`） |
| `.nav-profile-dot` | margin: 0 2px（分隔点） |
| `.clickable` | cursor: pointer / transition: opacity 0.2s |

---

## 7. 交互行为

| 元素 | 交互 | 说明 |
|------|------|------|
| L1 返回箭头 | 点击 | 返回上一页 |
| L3 关闭 | 点击 | 关闭当前页面 |
| L5 操作文字 | 点击 | 执行对应操作（如"取消"） |
| R1/R2 图标 | 点击 | 触发对应功能：更多图标 → Menu（气泡菜单）；分享图标 → ActionSheet（分享面板） |
| R3 操作文字 | 点击 | 执行对应操作（如"完成""发送"） |
| R4 按钮 | 点击 | 执行主要操作 |
| R6 勾选 | 点击 | 切换勾选状态 |
| C2 下拉标题 | 点击 | 展开下拉选择器 |
| C4 可点击副标题 | 点击 | 导航到对应页面 |
| C5 分段选择 | 点击 | 切换选项卡，选中滑块滑动到目标位置 |

---

## 8. 底部分割线规则

导航栏底部分割线（0.5px，`var(--border-default)`）遵循 iOS 15+ `scrollEdgeAppearance` 设计范式：

### 核心原则

分割线是**功能性视觉提示**——告诉用户"下方有被导航栏遮挡的内容正在滚动"。**静态设计稿中导航栏默认不画分割线**。

### 显示规则

| 状态 | 分割线 | 说明 |
|------|--------|------|
| 页面内容**未滚动**（处于顶部） | **无** | 导航栏与下方内容视觉融合，无遮挡感 |
| 页面内容**向上滚动**至导航栏下方 | **有** | 提示用户有内容被导航栏遮挡 |

### 与下方组件的关系

导航栏分割线与下方组件类型**无关**。无论下方是 Search、DataFilter、TextBlock、List 还是其他组件，分割线的显隐**仅取决于滚动状态**：
- 内容在顶部 → 透明无线（`scrollEdgeAppearance`）
- 内容已滚动 → 模糊背景+分割线（`standardAppearance`）

> **注意**：在组件构建器（component-builder.html）中，画布为静态展示，导航栏**不显示底部分割线**。

---

## 9. 资源文件映射

| 用途 | 文件路径 | 尺寸 |
|------|---------|------|
| 返回箭头（L1/L2） | `icons/chevron_left.svg` | 24×24px |
| 关闭（L3） | `icons/close.svg` | 24×24px |
| 功能图标（L4/R1/R2/R5） | `icons/empty_icon.svg`（占位，实际任务中替换为 `icons/QUI_24_icons/<图标名>.svg`） | 24×24px |
| 头像（L6） | `icons/Avatar_32.svg` 或 `icons/Avatar_40.svg` | 32×32px / 36×36px |
| 下拉箭头（C2） | `icons/chevron_down.svg` | 12×12px |
| 勾选（R6） | `icons/Checkbox_filled.svg` | 24×24px |
| 描述组图标（C4/L6） | `icons/empty_icon.svg`（占位，实际任务中替换为 `icons/QUI_24_icons/<图标名>.svg`） | 10×10px |
| 分段选择控件（C5） | 无外部资源，纯 CSS 实现 | — |

---

## 8. NV2 · 滚动态分割线实现

NavBar 默认**不展示**底部分割线；当页面内容因滚动进入 NavBar 下方覆盖区时，**显示** 0.5px 分割线（完全复用 `divider_spacing` A1 视觉规范）；回滚到顶部时分割线淡出。

### 8.1 HTML 结构
```html
<!-- sentinel 必须放在 NavBar 之前、页面顶部处。
     当页面滚动使 sentinel 滑出视口即触发 scrolled 态。 -->
<div class="scroll-sentinel" aria-hidden="true"></div>
<nav class="navbar-row">...</nav>
```

### 8.2 CSS（已内置于 §6.1 容器样式，此处仅为速查）
```css
/* 默认态：无分割线 */
.navbar-row::after {
    content: '';
    position: absolute;
    left: 0; right: 0; bottom: 0;
    height: 0.5px;                    /* 对齐 divider A1 */
    background: var(--border-weak);   /* 对齐 divider A1 */
    opacity: 0;
    transition: opacity 200ms ease-out;  /* TK12 白名单 */
    pointer-events: none;
}
/* 滚动遮挡态：显示分割线 */
.navbar-row.scrolled::after { opacity: 1; }

.scroll-sentinel {
    position: absolute;
    top: 0; left: 0;
    height: 1px; width: 1px;
    pointer-events: none;
    visibility: hidden;
}
```

### 8.3 JS（IntersectionObserver，方案 A · 推荐）
```js
(function initNavbarEdge() {
    const sentinel = document.querySelector('.scroll-sentinel');
    const navbar = document.querySelector('.navbar-row');
    if (!sentinel || !navbar) return;
    new IntersectionObserver(([entry]) => {
        navbar.classList.toggle('scrolled', !entry.isIntersecting);
    }).observe(sentinel);
})();
```

### 8.4 约束
1. 默认态**禁止**使用 `border-bottom`（会占高度导致切换时 1px 跳动）——必须用伪元素方案
2. 分割线必须复用 divider A1 规范：**0.5px + `var(--border-weak)`**，禁止其他高度/颜色
3. 过渡属性仅允许 `opacity`（200ms ease-out），禁止 border-color / transform / box-shadow 等
4. matrix 等静态展示页**只需加 CSS**（默认态），不需加 JS；只有真实可滚动页面才初始化 IntersectionObserver
