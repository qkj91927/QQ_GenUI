# 半屏浮层 HalfScreenOverlay 组件设计规范

> **组件 ID**：`half_screen_overlay`  
> **大类**：模态  
> **变体数量**：2 种（标准型 + 把手型）

## 1. 组件概述

半屏浮层（HalfScreenOverlay）是从屏幕底部弹出、约占半屏高度的模态容器组件。它用于承载二级内容、表单、选择器等场景，支持下滑关闭和点击蒙层关闭。分为**标准型**（半屏导航栏，默认 A3，可根据业务需求使用 A1-A4/B1-B3 任意变体）和**把手型**（拖拽把手条，不使用导航栏）两种子组件。

## 2. 组件结构

### 2.1 标准型（HSO-A）

```
┌───────────────────────────────────┐  ← height: 926px (default)
│  Overlay                          │
│  var(--overlay_dark)        │
│                                   │
│                                   │
├───────────────────────────────────┤  ← border-radius: 20px
│ ┌───────────────────────────────┐ │
│ │                         [X]   │ │  ← 54px HS_NavBar (default A3)
│ ├───────────────────────────────┤ │
│ │                               │ │
│ │  Content (scrollable)         │ │  ← height = sheet - 54 - 34
│ │                               │ │
│ └───────────────────────────────┘ │
│         Home Bar (34px)           │  ← system, not part of component
└───────────────────────────────────┘
```

### 2.2 把手型（HSO-B）— 半屏态（默认）

```
┌───────────────────────────────────┐
│  Overlay                          │
│  var(--overlay_dark)        │
│                                   │
│                                   │
├───────────────────────────────────┤  ← border-radius: 20px
│ ┌───────────────────────────────┐ │
│ │  ---- Handle ----             │ │  ← 20px handle bar (36x5px, opacity:1)
│ ├───────────────────────────────┤ │
│ │                               │ │
│ │  Content (scrollable)         │ │  ← height = 75vh - 20 - 34
│ │                               │ │
│ └───────────────────────────────┘ │
│         Home Bar (34px)           │  ← system, not part of component
└───────────────────────────────────┘
```

### 2.3 把手型（HSO-B）— 上滑全屏态

```
┌───────────────────────────────────┐  ← border-radius: 0 (fullscreen)
│ ┌───────────────────────────────┐ │
│ │  Status Bar (54px)            │ │  ← system status bar
│ ├───────────────────────────────┤ │
│ │  [X]    (C opt)    (R opt)    │ │  ← NavBar 44px (L=L3 required)
│ ├───────────────────────────────┤ │     handle hidden (opacity: 0)
│ │                               │ │
│ │                               │ │
│ │  Content (scrollable)         │ │  ← height = 100vh - 54 - 44 - 34
│ │                               │ │
│ │                               │ │
│ │                               │ │
│ └───────────────────────────────┘ │
│         Home Bar (34px)           │  ← system, not part of component
└───────────────────────────────────┘

Transition: triggered when top < 100px
  Handle:  opacity 1 -> 0 (fade out)
  NavBar:  opacity 0 -> 1 (fade in), L=L3 (required), C/R configurable
  Radius:  20px -> 0px
  Cross-fade sync transition
  NavBar follows NAVBAR_COMPONENT_SPEC.md
```

## 3. 设计 Token

### 3.1 尺寸规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 面板宽度 | 428px | 与设备等宽 |
| 标准型高度 | 360px ~ 720px | 最小 360px，最大 720px，默认 420px，超出内容区可滚动 |
| 把手型高度 | 75vh（屏幕高度的 75%） | 默认定高，支持上滑吸附至 100vh 全屏模态 |
| 顶部圆角 | 20px | 仅左上、右上 |
| 半屏导航栏高度（标准型） | 54px（A2副标题型为65px） | 取决于所用的 HS_NavBar 变体 |
| 关闭按钮 | `icons/Close_HalfScreen.svg`（30×30px） | SVG **自带灰底圆**（rgba(0,0,0,0.04)）和 X 图标，**直接使用，不需要外层容器** |
| 把手区域高度（把手型） | 20px | 垂直居中 |
| 把手指示条尺寸 | 36 × 5px | 圆角 2.5px |

### 3.2 颜色规范

| 元素 | 色值 | Token |
|------|------|-------|
| 遮罩层 | rgba(0, 0, 0, 0.50) | 叠加色-overlay_dark |
| 面板背景 | #FFFFFF | 背景色-Primary |
| 关闭按钮背景 | rgba(0, 0, 0, 0.04) | 来自 `Close_HalfScreen.svg` 内部，无需代码设置 |
| 把手指示条 | rgba(60, 60, 67, 0.30) | — |

## 4. 子组件类型定义

### 4.1 标准型（HSO-A）

- **导航区域**：使用 **HS_NavBar** 组件（详见 `HS_NAVBAR_COMPONENT_SPEC.md`），默认 **A3**，可按业务替换为 **A1 / A2 / A4**（一级导航）或 **B1 / B2 / B3**（二级导航）
- **HS_NavBar → 内容区间距**：**B2（8px）**（A3 叠在图片上时为 0px）
- **面板高度范围**：360px ~ 720px，默认 420px
- **内容区高度**：`sheetHeight - navbarHeight - 34(HomeBar)`，其中 navbarHeight：A1/A3/A4/B1-B3 = 54px，A2 = 65px。默认 420px 时（A3）为 **332px**，超出内容区可滚动
- **适用场景**：需要明确关闭操作的内容展示、表单填写
- **关闭方式**：点击关闭按钮、点击蒙层、下滑手势

### 4.2 把手型（HSO-B）

- **导航区域**: 20px 高度，包含居中的把手指示条。**不使用半屏导航栏**，顶部自带把手条
- **面板高度**: 默认 75vh（半屏态），支持上滑吸附至 100vh（全屏模态）
- **内容区高度**: 半屏态 `75vh - 20(把手条) - 34(HomeBar)`，超出内容区可滚动
- **适用场景**: 支持手势拖拽调整高度的临时内容展示
- **关闭方式**: 下滑手势 / 右滑手势 / 点击蒙层 / 点击操作区功能按钮

## 5. 变体矩阵

**共 2 种子组件**

| 编号 | 变体 ID | 类型 | 顶部区域 | 名称 |
|------|---------|------|---------|------|
| 1 | HSO-A | 标准型 | 半屏导航栏（默认A3，54px） | 标准型 |
| 2 | HSO-B | 把手型 | 拖拽把手条（20px） | 把手型 |

## 6. 交互行为

### 6.1 弹出动效
- 面板从底部滑入，遮罩层同步淡入
- 动效曲线: cubic-bezier(0.32, 0.72, 0.35, 1)
- 入场时长: 420ms

### 6.2 收起动效
- 面板向下滑出，遮罩层同步淡出
- 退场时长: 300ms
- 退场缓动: `cubic-bezier(0.32, 0.72, 0.35, 1)`
- Token: `--anim-halfscreen-out-duration` / `--anim-halfscreen-out-easing`

### 6.3 关闭触发
- **标准型**: 下滑手势 / 点击遮罩区域 / 点击右上角关闭 Icon / 点击操作区功能按钮（可选，如取消等，视业务场景而定）
- **把手型（半屏态）**: 下滑手势 / 右滑手势 / 点击遮罩区域 / 点击操作区功能按钮
- **把手型（全屏态）**: 右滑关闭 / 下滑回到半屏态（未超过关闭阈值时）/ 下滑直接关闭（超过关闭阈值时）/ 点击全屏导航栏关闭按钮

### 6.4 内容滚动
- 内容区域支持纵向滚动
- 滚动到顶部时，继续下拉触发面板关闭手势
- 支持 -webkit-overflow-scrolling: touch（120Hz 流畅滚动）

### 6.5 组件构建器特有行为
- HalfScreenOverlay 为模态容器组件，拖入画布时自动创建模态覆盖层
- 面板底部对齐覆盖层底部（`align-items: flex-end`）
- 内容区域（`.hs-overlay-drop-content`）可接受其他非模态子组件拖入（如列表、表单等）
- 侧边栏预览使用 0.45 缩放（`scale(0.45)`），仅展示面板部分不含遮罩
- 侧边栏提供分段选择器切换"标准型 / 把手型"

### 6.6 把手型全屏态切换（仅 HSO-B）

把手型支持半屏态（75vh）与全屏模态（100vh）之间的切换：

| 阶段 | 把手条 | 全屏导航栏 | 圆角 | 触发条件 |
|------|--------|-----------|------|---------|
| 半屏态（默认） | opacity: 1 | opacity: 0, hidden | 20px | — |
| 上滑过渡中 | opacity 渐变 1→0 | opacity 渐变 0→1 | 渐变 20→0px | top < 100px 时开始交叉过渡 |
| 全屏模态 | opacity: 0 | opacity: 1, visible | 0px | top = 0 吸附 |
| 下滑退出全屏 | opacity 渐变 0→1 | opacity 渐变 1→0 | 渐变 0→20px | top > 100px |

**全屏态特征**：
- 面板铺满整屏（top: 0, height: 100vh, border-radius: 0）
- 把手条隐藏，显示全屏导航栏（系统状态栏 + NavBar）
- 遮罩层不可见（面板已铺满）

**全屏导航栏规范**：
- **左侧（L）**：必须为 **L3（关闭 ✕）**，不可更改，点击关闭整个浮层
- **中间（C）**：可根据业务场景配置（如 C0 空白 / C1 标题 / C2 下拉标题等），默认 C0 空白
- **右侧（R）**：可根据业务场景配置（如 R0 空白 / R1 图标 / R3 操作文字等），默认 R0 空白
- 全屏导航栏的布局、间距、字体等**必须遵循 NavBar 组件规范**（参见 `NAVBAR_COMPONENT_SPEC.md`）

**全屏态下滑行为**：
- 小幅下滑（top < 半屏态高度 25vh）→ 回到半屏态
- 大幅下滑（top > 半屏态高度 25vh）→ 直接关闭

### 6.7 手势参数（HSO-B 把手型）

| 参数 | 值 | 说明 |
|------|------|------|
| 下滑关闭阈值 | **100px** | 半屏态下滑超过 100px 触发关闭 |
| 右滑关闭阈值 | **100px** | 右滑 dx > 100px 且垂直位移 < 150px 时触发关闭 |
| 手势阻尼系数 | **0.85** | 拖拽位移 × 0.85 = 实际面板位移 |
| 水平→垂直映射比 | **0.6** | 右滑 dx 的 60% 叠加到垂直位移 |
| 全屏吸附阈值 | **top < 100px** | 面板顶部距屏幕顶部 < 100px 时吸附全屏 |
| 向上弹性阻尼 | **0.2** | top < 0 时位移 × 0.2（橡皮筋效果） |

## 7. 布局规则

1. 面板始终底部对齐，顶部圆角 20px
2. 遮罩层覆盖整个屏幕（matrix 中 outer 容器高度 926px = iPhone 屏幕高度）
3. **标准型高度**: 360px ~ 720px，默认 420px，可随内容增加自动撑高至最大 720px，超出内容区可滚动（`overflow-y: auto`）
4. **把手型高度**: 默认 75vh（屏幕高度的 75%），支持上滑吸附至 100vh 全屏模态，超出内容区可滚动（`overflow-y: auto`）
5. 内容区域允许其他**非模态**组件拖入（如列表、表单等），**禁止**嵌套其他模态组件（ActionSheet、Dialog）
6. 标准型导航栏：默认采用 A3 半屏导航栏样式（关闭按钮右对齐，30×30px 圆形），可按业务需求替换为其他 HS_NavBar 变体（参见 `HS_NAVBAR_COMPONENT_SPEC.md`）
7. 把手型把手条：指示条固定在顶部区域居中

## 8. CSS 实现参考

### 8.1 matrix 中的外层容器（含遮罩）

```css
.hs-overlay-outer {
    width: 428px;
    height: 926px;               /* iPhone 屏幕高度 */
    position: relative;
    background: var(--叠加色-overlay_dark, var(--overlay_dark));  /* 遮罩色 */
    overflow: hidden;
}
```

### 8.2 白色面板

```css
.hs-overlay-sheet {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 428px;
    height: /* sheetHeight */;
    background: var(--bg_bottom_light);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    overflow: hidden;
}
```

### 8.3 builder 中的面板容器（无遮罩，flex 布局）

```css
/* builder 使用 inline style 而非 class */
{
    width: 428px;  /* 或 100% */
    min-height: 360px;   /* 标准型最小高度 */
    max-height: 720px;
    background: var(--bg_bottom_light);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
}
```

### 8.4 标准型导航栏 A3

```css
.hs-overlay-navbar-a3 {
    width: 428px;
    height: 54px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 16px;
    background: var(--bg_bottom_light);
    box-sizing: border-box;
}
.hs-overlay-close-btn-a3 {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: var(--fill_standard_primary);
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### 8.5 把手条

```css
.hs-overlay-handle-bar {
    width: 428px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.hs-overlay-handle-indicator {
    width: 36px;
    height: 5px;
    background: var(--text_tertiary);
    border-radius: 2.5px;
}
```

### 8.6 底部安全区

```css
.hs-overlay-bottom {
    width: 428px;
    height: 34px;
    position: relative;
    background: var(--bg_bottom_light);
}
.hs-overlay-homebar {
    width: 144px;
    height: 5px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 8px;
    background: var(--text_primary);
    border-radius: 2.5px;
}
```

---

## 9. 内嵌组件底色规则

> **⚠️ 导航栏适用范围**：半屏导航栏（HS_NavBar）**仅适用于标准型（HSO-A）**。把手型（HSO-B）半屏态顶部为把手条，不使用导航栏；上滑进入全屏态后，把手条隐藏，显示全屏导航栏（NavBar），左侧必须为 L3 关闭，中间/右侧可按业务配置（两者交叉动画过渡，详见 §6.6）。

### 9.1 半屏导航栏底色
半屏导航栏组件（HS_NavBar）本身为**透明底色**（`background: transparent`），颜色跟随半屏浮层面板的底色显示。默认面板底色为白色（`#FFFFFF` / `--color-bg-item`），因此导航栏视觉上呈现白底。

### 9.2 内嵌组件的页面背景色约束
当以下组件嵌入半屏浮层内容区时，需要调整浮层内容区的背景色，规则与全屏页面完全一致：

| 内嵌组件 | 内容区背景色 | Token | 说明 |
|----------|------------|-------|------|
| Grouped List（卡片式列表） | `#F0F0F2` | `bg_middle_standard` | 白色卡片需灰底形成层级分离 |
| Card（卡片） | `#F0F0F2` | `bg_middle_standard` | 同上 |
| Message（消息） | `#F0F0F2` | `--bg_select_aio` | AIO 背景色 |
| 其他组件（List/Textfield/Button 等） | `#FFFFFF` | `bg_bottom_light` | 默认白底 |

> **常用场景模版**：见 `md/HALF_SCREEN_OVERLAY_TEMPLATES.md`。执行半屏浮层相关设计任务时，请优先查阅该文档，判断是否可直接使用或小幅修改已有模版。