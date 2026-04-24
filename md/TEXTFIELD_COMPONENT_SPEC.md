# 输入框 Textfield · 组件设计规范

> **组件 ID**：`textfield`  
> **大类**：操作  
> **变体数量**：50 种（A-D 4类型 × 5状态 = 20 + E复合输入框 6种 × 5状态 = 30）

## 🔒 强约束声明

@LINT F1, F4, F11, S11, TK1, TK10, TK15
@SPEC_OF_TRUTH 本文件为 Textfield 权威规范

### @MUST
- 变体仅限 A-D 基础 × 5 态（20）+ E1-E6 复合 × 5 态（30），共 50 种
- 5 种状态：default / focused / typing / completed / error
- 完成指示器必须用 `icons/done.svg`（40×40px 蓝色圆形+白色对勾）
- 默认态/激活态 opacity: 0.3（disabled 视觉）；输入态/完成态/错误态 opacity: 1
- 清除按钮颜色：`var(--icon-secondary)`
- 输入框描边：`0.5px solid var(--border-default)`（组件内部强描边）

### @FORBIDDEN
- 发明注册表外的变体
- 完成指示器自绘 SVG（必须调用 `icons/done.svg`）
- 输入框描边硬编码 rgba 或其他颜色
- Disabled 态单独设色（应继承默认态色 + opacity 0.3）

## 1. 组件概述

输入框（Textfield）是表单交互中最基础的信息录入组件，用于接收用户的文字、数字等文本内容输入。组件支持 A-D 共 4 种类型 × 5 种交互状态 = 20 种子组件变体，以及 E 复合输入框 6 种 × 5 种状态 = 30 种子组件变体，总计 50 种。

---

## 2. 组件类型

| 类型 | 编号 | 说明 | 场景 |
|------|------|------|------|
| 单行无标题 | A | 独立输入区域，无前置标题 | 搜索、备注等简单输入 |
| 单行有标题 | B | 左侧带固定宽度标题标签 | 表单填写（姓名、地址等） |
| 电话号码 | C | 左侧带国家区号前缀 "中国+86" | 手机号/电话号码输入 |
| 多行文本 | D | 多行文本域，带圆角容器 | 长文本输入（评论、描述等） |
| 复合输入框 | E | 大面积文本区 + 可选图片附件 + 操作按钮栏 + 可选完成指示器 | 高级编辑场景（发帖、评论配图等） |

---

## 3. 交互状态

| 状态 | 编号 | 说明 | 视觉特征 |
|------|------|------|----------|
| 默认态 | 1 | 未获得焦点 | placeholder 文字，浅灰色 var(--text-quaternary) |
| 激活态 | 2 | 获得焦点但未输入 | 蓝色光标 #0099FF + placeholder |
| 输入态 | 3 | 正在输入文字 | 实际文字 + 光标 + 清除按钮，字数统计显示 "已输入/总数" |
| 完成态 | 4 | 输入完成，失去焦点 | 实际文字，无光标无清除按钮 |
| 错误态 | 5 | 输入超限或格式错误 | 文字超长截断 + 光标 + 清除按钮，字数统计红色 `#E0462C`（`--accent-red`）|

---

## 4. 变体矩阵

### 4.1 A-D 基础输入框（4 × 5 = 20）

| 类型 \ 状态 | 默认态 | 激活态 | 输入态 | 完成态 | 错误态 |
|-------------|--------|--------|--------|--------|--------|
| A 单行无标题 | A1 | A2 | A3 | A4 | A5 |
| B 单行有标题 | B1 | B2 | B3 | B4 | B5 |
| C 电话号码   | C1 | C2 | C3 | C4 | C5 |
| D 多行文本   | D1 | D2 | D3 | D4 | D5 |

### 4.2 E 复合输入框 Advanced Textfield（6 × 5 = 30）

| 子类型 \ 状态 | 默认态 | 激活态 | 输入态 | 完成态 | 错误态 |
|-------------|--------|--------|--------|--------|--------|
| E1 卡片·基础 | E1-1 | E1-2 | E1-3 | E1-4 | E1-5 |
| E2 卡片·图片 | E2-1 | E2-2 | E2-3 | E2-4 | E2-5 |
| E3 卡片·完成 | E3-1 | E3-2 | E3-3 | E3-4 | E3-5 |
| E4 卡片·图片+完成 | E4-1 | E4-2 | E4-3 | E4-4 | E4-5 |
| E5 通栏·基础 | E5-1 | E5-2 | E5-3 | E5-4 | E5-5 |
| E6 通栏·图片 | E6-1 | E6-2 | E6-3 | E6-4 | E6-5 |

**E 类三维属性**：

| 维度 | 选项 | 说明 |
|------|------|------|
| 容器类型 | 卡片式 / 通栏式 | 卡片式：白色圆角容器（24px），内缩 16px；通栏式：透明背景，跟随页面背景色 |
| 添加图片 | 支持 / 不支持 | 支持时底部操作栏上方显示图片行，88×88px 占位图，支持横向滚动，**不显示滚动条** |
| 附带完成操作 | 附带 / 不附带 | 附带时底部操作栏右侧显示圆形完成指示器（40px 圆环 + 对勾图标） |

**E 类五种状态**：

| 状态 | 说明 | 视觉特征 |
|------|------|----------|
| 默认态 | 未获得焦点 | 无光标 + placeholder 灰色（`var(--text-quaternary)`）；完成指示器（如有）`opacity: 0.3` |
| 激活态 | 获得焦点但未输入 | 蓝色光标在左 + placeholder 灰色；完成指示器（如有）`opacity: 0.3` |
| 输入态 | 正在输入文字 | 黑色文字 + 光标在末尾；字数统计更新；完成指示器（如有）`opacity: 1` |
| 完成态 | 输入完成，失去焦点 | 无光标 + 黑色文字；完成指示器（如有）`opacity: 1` |
| 错误态 | 字数超限 | 黑色文字 + 光标 + 字数统计红色（`--accent-red`，`#E0462C`）；完成指示器（如有）`opacity: 1` |

**完成指示器**：使用 `icons/done.svg`（40×40px，含蓝色圆形+白色对勾）；默认态/激活态设 `opacity: 0.3` 表示 disabled，输入态/完成态/错误态设 `opacity: 1`。

**E 类背景色约束**：

| 变体范围 | 组件底色 | 页面背景色约束 |
|----------|---------|---------------|
| E5/E6 通栏式 | `transparent`（透明） | 跟随页面背景色 |
| E1-E4 卡片式 | `#FFFFFF`（白色） | 必须使用 `--bg-secondary`（`var(--bg-secondary)`），与卡片式列表背景色约束一致 |

**A-D 类背景色约束**：

| 变体范围 | 组件底色 | 页面背景色约束 |
|----------|---------|---------------|
| A/B/C/D 单行/多行输入框 | `#FFFFFF`（白色圆角容器）| 必须使用 `--bg-secondary`（`var(--bg-secondary)`），与卡片式列表背景色约束一致 |

> **统一规则**：除 E5/E6 通栏式外，所有 Textfield 变体（A/B/C/D 及 E1-E4）均使用白色背景，须搭配灰色页面底（`var(--bg-secondary)`）形成视觉层级分离。

---

## 5. 尺寸规范

### 5.1 单行输入框（A/B/C 类型）

| 属性 | 数值 |
|------|------|
| 总宽度 | 428px |
| 输入行高度 | 56px |
| 左右圆角装饰 | 16px × 56px，border-radius 内嵌圆角 |
| 中间输入区域宽度 | 364px |
| 底部附加说明行高度 | 24px |
| 组件总高度 | 80px (56 + 24) |
| 底部分割线 | 宽 364px，高 0.5px（**仅嵌入 Grouped List 时由列表容器添加，单独使用无分割线**） |

### 5.2 有标题型（B 类型）

| 属性 | 数值 |
|------|------|
| 标题宽度 | 90px（固定，5个中文字符） |
| 标题与输入区间距 | 24px |
| 输入区域宽度 | 250px |

### 5.3 电话号码型（C 类型）

| 属性 | 数值 |
|------|------|
| 国家代码前缀 | "中国+86 " |
| 前缀颜色 | `#214CA5`（`--text-link`） |
| 号码输入区宽度 | 275px |

### 5.4 多行文本域（D 类型）

| 属性 | 数值 |
|------|------|
| 总宽度 | 428px |
| 文本域高度 | 197px（含 16px 上下内边距） |
| 文本内容区高度 | 144px |
| 圆角 | 12px（左上/左下、右上/右下） |
| 字数统计位置 | 文本域内右下角 |
| 底部附加说明行高度 | 24px（**可隐藏**） |

> **附加说明行可隐藏**：D 类的底部附加说明文字可被隐藏（字数统计在文本域内右下角，不受影响）。隐藏时组件总高度从 221px 自适应为 197px。

### 5.5 复合输入框（E 类型）

E 类由 Figma 三个属性变量组合定义，对应 E1-E6 六种子类型：

| Figma 属性 | 变量值 | 说明 |
|-----------|-------|------|
| `Layout` | `card` / `full` | 卡片式（圆角白色容器）或通栏式（透明满宽） |
| `HasImage` | `true` / `false` | 是否包含图片附件行 |
| `HasFinish` | `true` / `false` | 是否包含完成指示器（仅 card 支持） |

---

#### 属性一：Layout（容器类型）

| | card（卡片式） | full（通栏式） |
|--|--|--|
| 宽度 | 396px（左右各 16px margin） | 428px 满宽 |
| 背景 | `#ffffff` | `transparent`（跟随页面背景） |
| 圆角 | `24px` | 无 |
| Padding | `24px 16px 16px` | `24px 16px 16px` |
| 底部操作栏 | 有 | **无** |
| 页面背景约束 | 需搭配 `var(--bg-secondary)`（`--bg-secondary`） | 跟随页面背景色 |

---

#### 属性二：HasImage（是否含图片行）

**HasImage = false（无图片行）**
- 底部操作栏按钮数量：**3 个**

**HasImage = true（含图片行）**
- 文字区下方显示图片行，`margin-top: 16px`
- 图片行布局：`overflow-x: auto`（横向滚动），**不显示滚动条**（`scrollbar-width: none` / `::-webkit-scrollbar { display: none }`）
- **添加按钮**：始终在最左侧，88×88px，`background: var(--fill-tertiary)`，`border-radius: 16px`，居中 `icons/QUI_24_icons/add.svg`（24×24px，颜色 `var(--text-tertiary)`）
- **图片占位**：`icons/Thumbnail_88.svg`，88×88px，`border-radius: 12px`，间距 12px
- **不影响底部操作栏按钮数量**

---

#### 属性三：HasFinish（是否含完成指示器）

**HasFinish = false**
- 操作栏右侧无完成指示器

**HasFinish = true（仅 card 类型支持）**
- 操作栏最右侧显示完成指示器，占用一个位置，操作栏按钮数量：**2 个**
- 状态与透明度：

| 状态 | opacity | 含义 |
|------|---------|------|
| 默认态 | `0.3` | disabled（灰显） |
| 激活态 | `0.3` | disabled（灰显） |
| 输入态 | `1` | 可点击 |
| 完成态 | `1` | 可点击 |
| 错误态 | `1` | 可点击 |

---

#### 公共规格（所有 E 类共用）

**文字区域**

| 条件 | 字号 | 行高 |
|------|------|------|
| `HasFinish = true`（E3/E4） | 20px | 28px |
| `HasFinish = false`（E1/E2/E5/E6） | 17px | 24px |

- 颜色：`--text-primary`（`var(--text-primary)`）
- 光标：`inline-block`，1px 宽，`height: 1.2em`，颜色 `--brand-standard`（`#0099FF`），`vertical-align: text-bottom`
- 支持 `word-break: break-all` 换行

**底部操作栏（card 类型）**

操作按钮数量规则（`HasFinish = true` 时完成指示器占位，按钮减为 2 个；`HasImage` 不影响按钮数量）：

| 子类型 | HasFinish | 操作按钮数 |
|--------|-----------|-----------|
| E1 卡片·基础 | false | **3 个** |
| E2 卡片·图片 | false | **3 个** |
| E3 卡片·完成 | true | **2 个** |
| E4 卡片·图片+完成 | true | **2 个** |

- 操作按钮：icon 24px + 文字 17px，`padding: 8px 12px`，`background: var(--fill-tertiary)`，`border-radius: 24px`，按钮间距 12px
- 字数统计：12px，`--text-tertiary`（`var(--text-tertiary)`），超限时变 `--accent-red`（`#E0462C`），位于操作栏右侧

**组件总尺寸**：总宽度 428px，总高度 420px，各元素间距 `margin-top: 16px`

---

## 6. 颜色规范

### 6.1 文本颜色

| 用途 | 颜色值 | CSS 变量 |
|------|--------|----------|
| Placeholder 文字 | `var(--text-quaternary)` | `--text-quaternary` |
| 输入文字 | `var(--text-primary)` | `--text-primary` |
| 标题文字 | `var(--text-primary)` | `--text-primary` |
| 附加说明 | `var(--text-tertiary)` | `--text-tertiary` |
| 字数统计（正常） | `var(--text-tertiary)` | `--text-tertiary` |
| 字数统计（超限） | `#E0462C` | `--accent-red` |
| 国家代码前缀 | `#214CA5` | `--text-link` |

### 6.2 功能颜色

| 用途 | 颜色值 | CSS 变量 |
|------|--------|----------|
| 光标 | `#0099FF` | `--brand-standard` |
| 清除按钮 | `var(--text-secondary)` | `--icon-secondary` |
| 分割线 | `var(--border-default)` | `--border-default` |
| 输入框背景 | `#FFFFFF` | `--bg-bottom` |

---

## 7. 字体规范

| 元素 | 字号 | 字重 | 字体 |
|------|------|------|------|
| 输入文字 / Placeholder | 17px | 400 (Regular) | PingFang SC |
| 标题文字 | 17px | 400 (Regular) | PingFang SC |
| 附加说明 | 14px | 400 (Regular) | PingFang SC |
| 字数统计（单行） | 14px | 400 (Regular) | PingFang SC |
| 字数统计（多行） | 12px | 400 (Regular) | PingFang SC |

---

## 8. 图标规范

### 8.1 光标（Cursor）
- 尺寸：1 × 18px
- 颜色：`#0099FF`（`--brand-standard`）
- 仅在 **激活态** 和 **输入态/错误态** 显示

### 8.2 清除按钮（Clear）
- 文件：`icons/close_input.svg`
- 尺寸：20 × 20px
- 形状：圆形实心底 + 白色 X
- 颜色：`var(--text-secondary)`（`--icon-secondary`）
- 仅在 **输入态** 和 **错误态** 显示

### 8.3 圆角装饰（Left/Right Round）
- 尺寸：16 × 56px
- 颜色：白色（与输入框背景一致）
- 用途：为单行输入框提供左右两端的大圆角视觉效果

---

## 9. 交互规范

### 9.1 状态转换

```
默认态 → (点击/聚焦) → 激活态
激活态 → (开始输入) → 输入态
输入态 → (失去焦点) → 完成态
输入态 → (字数超限) → 错误态
完成态 → (再次聚焦) → 激活态/输入态
错误态 → (删减文字) → 输入态
```

### 9.2 附加说明行

- 所有类型均支持底部附加说明行
- **附加说明行可隐藏**：在实际设计场景中，附加说明行可根据业务需要隐藏：
  - **A/B/C 类**：附加说明文字 + 字数统计作为整体隐藏，组件高度从 80px → 56px
  - **D 类**：仅附加说明文字隐藏（字数统计在文本域内右下角，不受影响），组件高度从 221px → 197px
  - 隐藏后组件高度自适应，无需手动调整
- 字数统计在附加说明行右侧显示（单行类型）
- 多行文本域的字数统计在文本域内右下角显示
- 字数统计格式：默认/激活态显示 "N字"，输入/完成/错误态显示 "已输入/N字"

### 9.3 清除按钮

- 仅在输入态和错误态显示
- 位于输入区域最右侧
- 点击后清空所有输入内容，回到激活态

---

## 10. 开发建议

1. 使用 CSS 变量实现主题切换（Light/Dark Mode）
2. 光标使用 CSS animation 实现闪烁效果（实际开发时）
3. 清除按钮建议使用 `<button>` 标签确保可访问性
4. 多行文本域建议使用原生 `<textarea>` 元素
5. 字数统计应实时更新，超限时切换为红色
6. 输入框的底部分割线在多行文本域中不显示（改用圆角容器边界）

---

## 11. CSS 实现代码块

> Textfield 在 HTML 中通过 JavaScript 内联 `style.cssText` 实现，以下为等效 CSS 类形式。

### 11.1 单行输入框外层

```css
.textfield-outer {
    width: 428px;
    height: 80px;      /* 输入行 56px + 底部说明 24px */
    position: relative;
    font-family: 'PingFang SC', sans-serif;
}
.textfield-row {
    position: absolute;
    left: 16px;
    top: 0;
    width: 396px;
    height: 56px;
    display: flex;
}
```

### 11.2 圆角装饰 + 中间内容

```css
.textfield-round-left,
.textfield-round-right {
    width: 16px;
    height: 56px;
    flex-shrink: 0;
}
.textfield-mid {
    width: 364px;
    height: 56px;
    background: var(--bg-bottom);
    position: relative;
}
```

### 11.3 输入区域样式

```css
/* 占位文字 */
.textfield-placeholder {
    font-size: 17px;
    font-weight: 400;
    color: var(--text-quaternary);
}
/* 输入文字 */
.textfield-input-text {
    font-size: 17px;
    font-weight: 400;
    color: var(--text-primary);
}
/* 标题（B类有标题型） */
.textfield-title {
    font-size: 17px;
    font-weight: 400;
    color: var(--text-primary);
    width: 90px;
}
/* 电话前缀（C类） */
.textfield-prefix {
    font-size: 17px;
    font-weight: 400;
    color: var(--text-link);
}
/* 光标 */
.textfield-cursor {
    width: 1px;
    height: 18px;
    background: var(--brand-standard);
}
/* 清除按钮 */
.textfield-clear {
    width: 20px;
    height: 20px;
}
```

### 11.4 底部说明行

```css
.textfield-footer {
    position: absolute;
    left: 0;
    top: 56px;
    width: 428px;
    height: 24px;
}
.textfield-helper {
    font-size: 14px;
    font-weight: 400;
    color: var(--text-tertiary);
}
.textfield-char-count {
    font-size: 14px;
    font-weight: 400;
    color: var(--text-tertiary);
}
.textfield-char-count.error {
    color: var(--accent-red);
}
```

### 11.5 多行文本域

```css
.textfield-multiline {
    width: 396px;
    height: 197px;
    display: flex;
}
.textfield-multiline-left {
    width: 16px;
    height: 197px;
    background: var(--bg-bottom);
    border-top-left-radius: 12px;
    border-bottom-left-radius: 12px;
}
.textfield-multiline-mid {
    width: 364px;
    height: 197px;
    background: var(--bg-bottom);
    position: relative;
}
.textfield-multiline-right {
    width: 16px;
    height: 197px;
    background: var(--bg-bottom);
    border-top-right-radius: 12px;
    border-bottom-right-radius: 12px;
}
.textfield-textarea {
    position: absolute;
    left: 0;
    top: 16px;
    width: 364px;
    height: 144px;
    overflow: hidden;
}
.textfield-multiline-counter {
    position: absolute;
    right: 0;
    bottom: 16px;
    text-align: right;
    font-size: 12px;
    color: var(--text-tertiary);
}
```

### 11.6 E 类复合输入框

```css
/* 卡片式容器（E1-E4） */
.atf-card {
    width: 396px;
    margin: 0 16px;
    background: var(--bg-bottom);
    border-radius: 24px;
    padding: 24px 16px 16px;
    box-sizing: border-box;
    font-family: 'PingFang SC', sans-serif;
}
/* 通栏式容器（E5-E6） */
.atf-full {
    width: 428px;
    background: transparent;
    padding: 24px 16px 16px;
    box-sizing: border-box;
    font-family: 'PingFang SC', sans-serif;
}
/* 文字区域 */
.atf-text-area {
    width: 100%;
    min-height: 60px;
    word-break: break-all;
    color: var(--text-primary);
    line-height: 24px; /* 17px字号 */
}
.atf-text-area.has-finish {
    font-size: 20px;
    line-height: 28px;
}
.atf-text-area:not(.has-finish) {
    font-size: 17px;
    line-height: 24px;
}
/* 光标 */
.atf-cursor {
    display: inline-block;
    width: 1px;
    height: 1.2em;
    background: var(--brand-standard);
    vertical-align: text-bottom;
    margin-left: 1px;
    animation: atf-blink 1s step-end infinite;
}
@keyframes atf-blink {
    50% { opacity: 0; }
}
/* 图片行 */
.atf-image-row {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    overflow-y: hidden;
    scrollbar-width: none;
    -webkit-overflow-scrolling: touch;
    margin-top: 16px;
    align-items: center;
}
.atf-image-row::-webkit-scrollbar {
    display: none;
}
.atf-add-btn {
    width: 88px;
    height: 88px;
    flex-shrink: 0;
    background: var(--fill-tertiary);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.atf-thumbnail {
    width: 88px;
    height: 88px;
    flex-shrink: 0;
    border-radius: 12px;
    object-fit: cover;
}
/* 操作栏 */
.atf-action-bar {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
}
.atf-action-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 8px 12px;
    background: var(--fill-tertiary);
    border-radius: 24px;
    font-size: 17px;
    color: var(--text-primary);
    white-space: nowrap;
}
/* 字数统计 */
.atf-char-count {
    margin-left: auto;
    font-size: 12px;
    color: var(--text-tertiary);
    white-space: nowrap;
}
.atf-char-count.error {
    color: var(--accent-red);
}
/* 完成指示器（done.svg，40×40px） */
.atf-done {
    width: 40px;
    height: 40px;
    flex-shrink: 0;
    margin-left: auto;
}
.atf-done.disabled {
    opacity: 0.3;
}
```

### 12.1 嵌入 Grouped List（卡片式列表）
Textfield 常嵌入 Grouped List 行中作为表单输入项：
- 嵌入时，左侧使用 Grouped List 的 L 区作为标签（如 B 类有标题型）
- Textfield 占据 Grouped List 的 C+R 区域
- 分割线遵循 Grouped List 的规则（行间 0.5px，左右缩进 16px）
- 引用：`GROUPED_LIST_COMPONENT_SPEC.md`

### 12.2 嵌入 HalfScreenOverlay（半屏浮层）
- Textfield 可嵌入半屏浮层的内容区域，作为弹出式表单输入
- 嵌入时宽度由半屏容器宽度决定（428px）

### 12.3 嵌入 Dialog（对话框）
- Dialog 的"输入框"正文类型（T-I-S/D/T）内置了简化版 Textfield
- 对话框内输入框尺寸固定 248×48px，与独立 Textfield 规格不同

---

## 13. 错误提示规范

| 错误类型 | 提示方式 | 说明 |
|----------|---------|------|
| 字数超限 | 字数统计变为红色 `#E0462C`（`--accent-red`）| 格式："已输入/N字"，超限数字高亮 |
| 格式错误（C类电话号码） | 底部附加说明行显示红色提示 | 文字："请输入正确的手机号码"，字号 14px，颜色 `--accent-red`（`#E0462C`）|
| 必填未填 | 底部附加说明行显示红色提示 | 文字："此项为必填项"，字号 14px，颜色 `--accent-red`（`#E0462C`）|
