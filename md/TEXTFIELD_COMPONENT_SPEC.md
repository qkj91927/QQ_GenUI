# 输入框 Textfield · 组件设计规范

> **组件 ID**：`textfield`  
> **大类**：操作  
> **变体数量**：20 种（4类型 × 5状态）

## 1. 组件概述

输入框（Textfield）是表单交互中最基础的信息录入组件，用于接收用户的文字、数字等文本内容输入。组件支持 4 种类型 × 5 种交互状态，共计 20 种子组件变体。

---

## 2. 组件类型

| 类型 | 编号 | 说明 | 场景 |
|------|------|------|------|
| 单行无标题 | A | 独立输入区域，无前置标题 | 搜索、备注等简单输入 |
| 单行有标题 | B | 左侧带固定宽度标题标签 | 表单填写（姓名、地址等） |
| 电话号码 | C | 左侧带国家区号前缀 "中国+86" | 手机号/电话号码输入 |
| 多行文本 | D | 多行文本域，带圆角容器 | 长文本输入（评论、描述等） |

---

## 3. 交互状态

| 状态 | 编号 | 说明 | 视觉特征 |
|------|------|------|----------|
| 默认态 | 1 | 未获得焦点 | placeholder 文字，浅灰色 rgba(60,60,67,0.26) |
| 激活态 | 2 | 获得焦点但未输入 | 蓝色光标 #0099FF + placeholder |
| 输入态 | 3 | 正在输入文字 | 实际文字 + 光标 + 清除按钮，字数统计显示 "已输入/总数" |
| 完成态 | 4 | 输入完成，失去焦点 | 实际文字，无光标无清除按钮 |
| 错误态 | 5 | 输入超限或格式错误 | 文字超长截断 + 光标 + 清除按钮，字数统计红色 #F74C30 |

---

## 4. 变体矩阵（4 × 5 = 20）

| 类型 \ 状态 | 默认态 | 激活态 | 输入态 | 完成态 | 错误态 |
|-------------|--------|--------|--------|--------|--------|
| A 单行无标题 | A1 | A2 | A3 | A4 | A5 |
| B 单行有标题 | B1 | B2 | B3 | B4 | B5 |
| C 电话号码   | C1 | C2 | C3 | C4 | C5 |
| D 多行文本   | D1 | D2 | D3 | D4 | D5 |

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
| 底部分割线 | 宽 364px，高 0.5px |

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
| 前缀颜色 | #214CA5（text_link） |
| 号码输入区宽度 | 275px |

### 5.4 多行文本域（D 类型）

| 属性 | 数值 |
|------|------|
| 总宽度 | 428px |
| 文本域高度 | 197px（含 16px 上下内边距） |
| 文本内容区高度 | 144px |
| 圆角 | 12px（左上/左下、右上/右下） |
| 字数统计位置 | 右下角 |
| 底部附加说明行高度 | 24px |

---

## 6. 颜色规范

### 6.1 文本颜色

| 用途 | 颜色值 | CSS 变量 |
|------|--------|----------|
| Placeholder 文字 | rgba(60,60,67,0.26) | --text_tertiary |
| 输入文字 | rgba(0,0,0,0.90) | --text_primary |
| 标题文字 | rgba(0,0,0,0.90) | --text_primary |
| 附加说明 | rgba(60,60,67,0.56) | --text_secondary |
| 字数统计（正常） | rgba(60,60,67,0.56) | --text_secondary |
| 字数统计（超限） | #F74C30 | --feedback_error |
| 国家代码前缀 | #214CA5 | --text_link |

### 6.2 功能颜色

| 用途 | 颜色值 | CSS 变量 |
|------|--------|----------|
| 光标 | #0099FF | --brand_standard |
| 清除按钮 | #929296 | --icon_secondary |
| 分割线 | rgba(0,0,0,0.10) | --border_standard |
| 输入框背景 | white | --fill_light_secondary |

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
- 颜色：#0099FF（品牌蓝）
- 仅在 **激活态** 和 **输入态/错误态** 显示

### 8.2 清除按钮（Clear）
- 文件：`icons/close_input.svg`
- 尺寸：20 × 20px
- 形状：圆形实心底 + 白色 X
- 颜色：#929296（次要图标色）
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
    background: var(--color-bg-item);
    position: relative;
}
```

### 11.3 输入区域样式

```css
/* 占位文字 */
.textfield-placeholder {
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-quaternary);
}
/* 输入文字 */
.textfield-input-text {
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-primary);
}
/* 标题（B类有标题型） */
.textfield-title {
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-primary);
    width: 90px;
}
/* 电话前缀（C类） */
.textfield-prefix {
    font-size: 17px;
    font-weight: 400;
    color: var(--color-text-link);
}
/* 光标 */
.textfield-cursor {
    width: 1px;
    height: 18px;
    background: var(--color-brand-standard);
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
    color: var(--color-text-tertiary);
}
.textfield-char-count {
    font-size: 14px;
    font-weight: 400;
    color: var(--color-text-tertiary);
}
.textfield-char-count.error {
    color: var(--color-feedback-error);
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
    background: var(--color-bg-item);
    border-top-left-radius: 12px;
    border-bottom-left-radius: 12px;
}
.textfield-multiline-mid {
    width: 364px;
    height: 197px;
    background: var(--color-bg-item);
    position: relative;
}
.textfield-multiline-right {
    width: 16px;
    height: 197px;
    background: var(--color-bg-item);
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
    color: var(--color-text-tertiary);
}
```

---

## 12. 嵌入场景

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
| 字数超限 | 字数统计变为红色 `#F74C30` | 格式："已输入/N字"，超限数字高亮 |
| 格式错误（C类电话号码） | 底部附加说明行显示红色提示 | 文字："请输入正确的手机号码"，字号 14px，颜色 `--color-feedback-error`（#F74C30） |
| 必填未填 | 底部附加说明行显示红色提示 | 文字："此项为必填项"，字号 14px，颜色 `--color-feedback-error` |
