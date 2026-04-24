# 红点 Badge · 组件设计规范

> **组件 ID**：`badge`
> **大类**：运营
> **变体数量**：11 种（强提醒 4 + 弱提醒 4 + AIO 导航栏 3）

## 🔒 强约束声明

@LINT F1, F11, F14, S15, TK1, TK7
@SPEC_OF_TRUTH 本文件为 Badge 权威规范

### @MUST
- 变体仅限 **B1-B4**（强提醒）+ **W1-W4**（弱提醒）+ **A1-A3**（AIO 导航栏），共 11 种
- **典型宿主**：Badge 必须贴附于宿主元素（不可独立出现）。当前推荐宿主：**头像（Avatar）、图标（Icon）、缩略图（Thumbnail）**。后续可按需扩展更多宿主类型。
- **位置语义**（统一规则）：所有 Badge（B1/W1 圆点 + B2-B4/W2-W4 胶囊含 99+）的锚点钉死在**宿主内切圆右上方 45° 的圆边点**：
  - **45° 圆边点坐标**：`P = (50% + 50%·cos45°, 50% − 50%·sin45°) ≈ (85.3553%, 14.6447%)`（相对宿主 bounding box）
  - **圆形（B1/W1）**：**圆心**钉在 P → `top: calc(14.6447% − d/2); left: calc(85.3553% − d/2)`
  - **胶囊（B2-B4 / W2-W4）**：**左半圆的圆心**钉在 P → `top: calc(14.6447% − h/2); left: calc(85.3553% − h/2)`（h=18 → `top: calc(14.6447% − 9px); left: calc(85.3553% − 9px)`）
  - 数字增长（9 → 66 → 99+）时，胶囊只向右生长，左侧 P 锚点不动
- **强提醒底色**：`var(--accent-red)`（QUI 错误/警示语义）
- **弱提醒底色**：`#D9D9D9` 硬编码实色（Figma `rgba(0,0,0,0.15)` 在白底的渲染等效色；待 QUI token 系统补充实色灰后再迁回 token）
- **AIO 导航栏底色**：`var(--fill-tertiary)`（rgba 灰 12%）
- **AIO 导航栏作用域（A1-A3）**：**专用于 AIO 页面的 NavBar L2（返回+气泡）**——返回 AIO 聊天列表时显示未读消息数。**禁止用于任何其他位置/组件**。
- **数字文本**：
  - 强 / 弱提醒带数字：12px / Semibold (600) / `var(--text-white)`，字体 SF Pro Display
  - AIO 导航栏：14px / Medium (500) / `var(--text-primary)`，字体 SF Pro Display，line-height 16
- **圆角**：B/W 系 = 10px；A 系 = 12px
- **数字截断**：≥100 显示为 "99+"
- **z-index**：Badge **在宿主元素之上**（建议 z-index: 1 或继承父级 stacking）

### @FORBIDDEN
- 发明注册表外的变体
- 修改 Badge 底色（强/弱/AIO 三色固定 token，禁止硬编码 rgba / 其他 token）
- 数字字号偏离规范（12px Semibold for B/W；14px Medium for A）
- Badge 不附加宿主元素独立使用
- **贴附于不合理宿主**：默认禁止贴附于**按钮（Button）、宫格（Grid）、图片（ImageBlock）、文本块、列表行容器自身**等元素；新增宿主类型需先在本规范声明并更新典型宿主列表
- 在不支持 Badge 的位置使用（如列表行内文本之间、按钮文字中）
- 数字超过 99 不截断为 "99+"
- 锚点偏离 45° 圆边点（不得改用矩形右上角顶点 / 任意手调偏移）
- **AIO 导航栏（A1-A3）出现在 NavBar L2 之外的任何位置**（包括 AIO Input 内、列表行、Tab Bar、其他 NavBar 形态等均禁止）

---

## 1. 概述

红点 Badge 是用于在宿主元素（典型宿主：头像、图标、缩略图——后续可扩展）**右上方 45° 圆边点**展示**未读数量**或**状态提醒**的微型徽章组件，支持三种视觉强度：

- **强提醒**（红色）：高优先级未读消息、错误数量、强调通知
- **弱提醒**（灰色半透明）：用于**已开启消息免打扰**场景下的未读数提示——降级为低对比度灰色徽章
- **AIO 导航栏**（更弱灰色 + 深色文字）：**专用于 AIO 页面的 NavBar L2（返回+气泡）**，承载返回到 AIO 聊天列表时的未读消息数；不可独立或在其他位置使用

## 2. 子组件矩阵

### 2.1 强提醒 Strong（4 种）

| 编号 | 名称 | 内容 | 尺寸 | 视觉特征 |
|------|------|------|------|----------|
| **B1** | 强 · 无数字 | — | 10 × 10px 圆点 | 实心红圆点 |
| **B2** | 强 · 个位数 | "9" | min-width 18px, height 18px, padding 0 4px | 红底圆角胶囊 + 白字 |
| **B3** | 强 · 两位数 | "66" | min-width 18px, height 18px, padding 0 4px | 红底圆角胶囊 + 白字 |
| **B4** | 强 · 99+ | "99+" | min-width 18px, height 18px, padding 0 4px | 红底圆角胶囊 + 白字 |

### 2.2 弱提醒 Weak（4 种）

| 编号 | 名称 | 内容 | 尺寸 | 视觉特征 |
|------|------|------|------|----------|
| **W1** | 弱 · 无数字 | — | 10 × 10px 圆点 | 实心灰圆点 |
| **W2** | 弱 · 个位数 | "9" | min-width 18px, height 18px, padding 3px 4px | 灰底圆角胶囊 + 白字 |
| **W3** | 弱 · 两位数 | "66" | min-width 18px, height 18px, padding 3px 4px | 灰底圆角胶囊 + 白字 |
| **W4** | 弱 · 99+ | "99+" | min-width 18px, height 18px, padding 3px 4px | 灰底圆角胶囊 + 白字 |

### 2.3 AIO 导航栏 AIO（3 种）

| 编号 | 名称 | 内容 | 尺寸 | 视觉特征 |
|------|------|------|------|----------|
| **A1** | AIO · 个位数 | "9" | min-width 24px | 浅灰底胶囊 + 深色字 |
| **A2** | AIO · 两位数 | "66" | min-width 24px | 浅灰底胶囊 + 深色字 |
| **A3** | AIO · 99+ | "99+" | min-width 24px | 浅灰底胶囊 + 深色字 |

---

## 3. 视觉规范

### 3.1 强提醒 Strong (B1-B4)

| 属性 | B1 (无数字) | B2-B4 (有数字) |
|------|-------------|----------------|
| 形状 | 圆形 | 圆角胶囊 |
| 尺寸 | 10 × 10px | min-width 18px, height 18px |
| 圆角 | 50% (perfect circle) | 10px |
| 内边距 | — | `0 4px` |
| 背景 | `var(--accent-red)` | `var(--accent-red)` |
| 文本 | — | 12px / Semibold (600) / `var(--text-white)` / SF Pro Display |
| line-height | — | normal (auto) |

### 3.2 弱提醒 Weak (W1-W4)

| 属性 | W1 (无数字) | W2-W4 (有数字) |
|------|-------------|----------------|
| 形状 | 圆形 | 圆角胶囊 |
| 尺寸 | 10 × 10px | min-width 18px, height 18px |
| 圆角 | 50% | 10px |
| 内边距 | — | `3px 4px` |
| 背景 | `#D9D9D9`（硬编码） | `#D9D9D9`（硬编码） |
| 文本 | — | 12px / Semibold (600) / `var(--text-white)` / SF Pro Display |

### 3.3 AIO 导航栏 AIO (A1-A3)

| 属性 | A1-A3 |
|------|-------|
| 形状 | 圆角胶囊 |
| 尺寸 | min-width 24px, height 24px (auto by content) |
| 圆角 | 12px |
| 内边距 | `4px 6px` |
| 背景 | `var(--fill-tertiary)` |
| 文本 | 14px / Medium (500) / `var(--text-primary)` / SF Pro Display / line-height 16px |

---

## 4. 定位规则（钉在宿主内切圆 45° 圆边点）

Badge **不可独立使用**，必须贴附于宿主元素。当前典型宿主：**头像（Avatar）、图标（Icon）、缩略图（Thumbnail）**——后续可扩展。

> **当前不建议宿主**：按钮（Button）、宫格（Grid）、图片块（ImageBlock）、文本块、列表行容器自身（如有新宿主需求，先在本规范声明再使用）。

### 统一锚点规则

所有变体（圆点 + 胶囊 含 99+）的锚点统一钉死在**宿主内切圆右上方 45° 的圆边点 P**：

```
P = (50% + 50%·cos45°, 50% − 50%·sin45°) ≈ (85.3553%, 14.6447%)
```

| 形状 | 锚点 | 对齐目标 |
|------|------|---------|
| 圆形（B1 / W1） | **圆心** | P（45° 圆边点） |
| 胶囊（B2-B4 / W2-W4，含 "99+"） | **左半圆的圆心** | P（45° 圆边点） |

> **关键属性**：无论数字宽度如何变化（"9" → "66" → "99+"），胶囊只向右生长，左半圆圆心始终钉在 P 点不动，视觉锚点稳定且贴合圆形头像的视觉边界。

### 标准定位 CSS

```css
.badge-host {
    position: relative;  /* 宿主必须 relative 容纳 absolute 子元素 */
    display: inline-block;
}

/* B1 强 · 圆点 10×10 → 圆心钉在 P */
.badge-host > .badge-strong-dot {
    position: absolute;
    top:  calc(14.6447% - 5px);
    left: calc(85.3553% - 5px);
}

/* W1 弱 · 圆点 10×10 → 圆心钉在 P */
.badge-host > .badge-weak-dot {
    position: absolute;
    top:  calc(14.6447% - 5px);
    left: calc(85.3553% - 5px);
}

/* B2-B4 / W2-W4 胶囊 height=18 → 左半圆圆心(left+9, top+9) 钉在 P
   width 由数字内容决定，胶囊向右生长，左侧锚点不动 */
.badge-host > .badge-strong-num,
.badge-host > .badge-weak-num {
    position: absolute;
    top:  calc(14.6447% - 9px);
    left: calc(85.3553% - 9px);
}
```

> **通用公式**：`top = calc(14.6447% − h/2)`，`left = calc(85.3553% − h/2)`，其中 h 为 Badge 高度（圆点 = d，胶囊 = 18）。
> **AIO 例外**：A1-A3 不走此规则——它内嵌于 NavBar L2 区域内，由 NavBar L2 自行定位（详见 §10）。

---

## 5. 使用场景

| 类别 | 典型场景 |
|------|---------|
| **强提醒 B1-B4** | QQ 未读消息红点、邮箱未读数、订单待支付提醒、警告级通知 |
| **弱提醒 W1-W4** | **会话已开启「消息免打扰」** 时使用——降级显示未读消息数（替代红色 B 系），让用户感知有未读但不被强提醒打扰 |
| **AIO 导航栏 A1-A3** | **专用且仅用于** AIO 页面顶部 NavBar L2（返回+气泡）—— 从 AIO 单聊返回聊天列表时显示该列表的未读消息数 |

---

## 6. 设计 Token 映射

```
强提醒底色      var(--accent-red)         /* QUI 错误/警示语义色 */
弱提醒底色      #D9D9D9                   /* 硬编码实色（暂未走 token，等 QUI 补充实色灰再迁回） */
AIO 底色        var(--fill-tertiary)      /* rgba 灰 12% */
B/W 文字色      var(--text-white)         /* 白色 */
AIO 文字色      var(--text-primary)       /* 黑色（rgba 1.0）*/
B/W 圆角        10px                       /* 介于 radius-s (8) 和 radius-m (12) */
A 圆角          var(--radius-m)           /* 12px */
```

> **Note**：B/W 圆角 10px 不在标准 7 档圆角白名单（4/8/12/16/20/24/1000），是 Badge 组件**固有尺寸**（按 TK2b 组件固有尺寸豁免）。设计意图：与 18px 高度形成 ~5.5:1 的视觉胶囊比，不强制 12px。

---

## 7. CSS 实现代码块

### 7.1 共享样式

```css
.badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-sizing: border-box;
    font-family: 'SF Pro Display', -apple-system, sans-serif;
    white-space: nowrap;
}
```

### 7.2 强提醒 Strong

```css
/* B1 强·无数字（小红点） */
.badge.badge-strong-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--accent-red);
}

/* B2-B4 强·有数字（统一 min-width 18 / padding 0 4） */
.badge.badge-strong-num {
    min-width: 18px;
    height: 18px;
    padding: 0 4px;
    border-radius: 10px;
    background: var(--accent-red);
    color: var(--text-white);
    font-size: 12px;
    font-weight: 600;
}
```

### 7.3 弱提醒 Weak

```css
/* W1 弱·无数字（小灰点，10×10 与 B1 同尺寸） */
.badge.badge-weak-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #D9D9D9; /* 硬编码实色，待 token 系统补充实色灰再迁回 */
}

/* W2-W4 弱·有数字（统一 min-width 18 / padding 3 4） */
.badge.badge-weak-num {
    min-width: 18px;
    height: 18px;
    padding: 3px 4px;
    border-radius: 10px;
    background: #D9D9D9; /* 硬编码实色，待 token 系统补充实色灰再迁回 */
    color: var(--text-white);
    font-size: 12px;
    font-weight: 600;
}
```

### 7.4 AIO 导航栏 AIO

```css
/* A1-A3 AIO·有数字 */
.badge.badge-aio {
    min-width: 24px;
    padding: 4px 6px;
    border-radius: var(--radius-m);  /* 12px */
    background: var(--fill-tertiary);
    color: var(--text-primary);
    font-size: 14px;
    font-weight: 500;
    line-height: 16px;
}
```

---

## 8. 交互行为

### 8.1 数量更新

- 数量 0 → Badge 隐藏（`display: none`）
- 数量 1-9 → 显示个位数（B2/W2/A1）
- 数量 10-99 → 显示两位数（B3/W3/A2）
- 数量 ≥100 → 显示 "99+"（B4/W4/A3）
- 仅状态提醒（无具体数）→ 显示无数字小圆点（B1/W1）

### 8.2 入场/出场

- 默认无动画（即时显隐）
- 可选：scale 0 → 1 入场，duration 200ms / ease-out

---

## 9. Figma 属性映射

```
Badge / state=强提醒, propValue=无数字   → B1
Badge / state=强提醒, propValue=个位数   → B2
Badge / state=强提醒, propValue=两位数   → B3
Badge / state=强提醒, propValue=99+      → B4
Badge / state=弱提醒, propValue=无数字   → W1
Badge / state=弱提醒, propValue=个位数   → W2
Badge / state=弱提醒, propValue=两位数   → W3
Badge / state=弱提醒, propValue=99+      → W4
Badge / category=AIO导航栏, propValue=个位数 → A1
Badge / category=AIO导航栏, propValue=两位数 → A2
Badge / category=AIO导航栏, propValue=99+    → A3
```

---

## 10. 与其他组件的关系

| 关系 | 说明 |
|------|------|
| **NavBar L2 ⇔ Badge A1-A3（强绑定）** | NavBar L2（返回+气泡）的"气泡"区域**必须**使用 Badge A1-A3。底色 `var(--fill-tertiary)`、文字 `var(--text-primary)`、字号 14px Medium、圆角 12px。返回到 AIO 聊天列表时显示未读消息总数。**Badge A1-A3 反向只能出现于此处**——任何其他 NavBar 形态、任何其他组件均禁止使用 A1-A3。 |
| **List / Form 行左侧的头像 / 图标 / 缩略图** | L 区域的头像 / 图标 / 缩略图右上角可叠加 B1-B4（默认未读）或 W1-W4（已开启免打扰会话的未读）。不建议贴附于 R 区域文本之间或行容器自身。 |
| **Card 头像区** | 头像右上角可叠加 B1/B2（强提醒小红点 / 个位数胶囊）提示未读；已免打扰会话改用 W1/W2 |
| **Tab Bar / 底部导航** | 各 tab **图标**右上角叠加 B1/B2（强提醒系） |
| **AIO Input** | ❌ **不使用 A1-A3**。AIO Input 是聊天页面的输入栏，不承载未读数；A1-A3 只属于 NavBar L2。 |
| **Button / Grid / ImageBlock** | 默认**不建议**贴附；如需扩展为新宿主，先在本规范声明并更新典型宿主列表。 |
