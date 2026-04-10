# 文本块 TextBlock · 组件设计规范

> **组件 ID**：`text_block`  
> **大类**：数据  
> **变体数量**：13 种（H1-H7 居左 + C1-C6 居中）

纯文本内容的排版区域，涵盖标题、正文、摘要、提示等层级，支持居左与居中两种对齐方式，用于构建页面的信息层次与阅读节奏。

---

## 1. 组件概述

文本块组件包含 **13 种子组件变体**，分为 **H.居左**（7 种）和 **C.居中**（6 种）两大类：

| 编号 | 名称 | 对齐方式 | 文字类型 | 容器最小高度 |
|------|------|----------|----------|-------------|
| H1 | 大标题 | 居左 | title | 50px |
| H2 | 一级标题 | 居左 | subtitle | 36px |
| H3 | 二级标题 | 居左 | aux-title | 34px |
| H4 | 正文段落 | 居左 | body | 24px（自适应） |
| H5 | 前缀正文 | 居左 | body | 24px（自适应） |
| H6 | 摘要文本 | 居左 | summary | 20px（自适应） |
| H7 | 提示文本 | 居左 | hint | 17px（自适应） |
| C1 | 大标题 | 居中 | title | 50px |
| C2 | 一级标题 | 居中 | subtitle | 36px |
| C3 | 二级标题 | 居中 | aux-title | 34px |
| C4 | 正文段落 | 居中 | body | 24px（自适应） |
| C5 | 摘要文本 | 居中 | summary | 20px（自适应） |
| C6 | 提示文本 | 居中 | hint | 17px（自适应） |

> **H 类与 C 类的区别**：文字属性（字号、字重、行高、颜色）完全相同，仅 `text-align` 不同（`left` vs `center`）。居中类（C）不包含"前缀正文"变体，因为前缀标识在居中排版中无意义。

---

## 2. Markdown 渲染规范

本章节定义了 Markdown 语法与文本块子组件的对应关系，用于 AI 生成内容、富文本渲染等场景。

### 2.1 Markdown 语法触发映射

| Markdown 语法 | 触发的子组件 | 说明 |
|---------------|-------------|------|
| `# 一级标题` | **H1 大标题** | 页面/模块顶级标题 |
| `## 二级标题` | **H2 一级标题** | 内容区段标题 |
| `### 三级标题` | **H3 二级标题** | 二级分类标题 |
| `#### 四级标题` | **H3 二级标题** | 同二级标题，四级及以下统一使用 H3 |
| 普通段落文本 | **H4 正文段落** | 无特殊标记的正文内容 |
| `1. 有序列表` / `- 无序列表` | **H5 前缀正文** | 带序号/标记的列表项 |
| `> 引用文本` | **H6 摘要文本** | 引用块、摘要信息 |
| `*斜体*` / `**粗体**` 段落 | **H4 正文段落** | 内联样式，不改变段落类型 |
| `<small>提示</small>` / 脚注 | **H7 提示文本** | 次要辅助信息、脚注 |
| `[链接文本](url)` | **内联 Textlink** | 链接色文字，可在正文/摘要/提示中使用 |

### 2.1.1 Textlink 链接色规范

在 **H4 正文段落**、**H5 前缀正文**、**H6 摘要文本**、**H7 提示文本** 中，部分文字可设置为 Textlink 链接色，用于标识可点击的超链接或强调性操作入口。

#### 触发条件

| 触发方式 | 语法示例 | 说明 |
|----------|----------|------|
| Markdown 链接 | `[点击查看](https://...)` | 标准超链接语法 |
| 行内 HTML | `<a href="...">链接文字</a>` | HTML 锚点标签 |
| 自定义标记 | `<textlink>文字链接</textlink>` | 纯展示型链接样式（无实际跳转） |

#### Textlink 样式属性

| 属性 | 值 | CSS 变量 |
|------|------|----------|
| 颜色 | `#214CA5` | `var(--text_link)` |
| 字号 | 继承父容器 | — |
| 字重 | 继承父容器（400） | — |
| 下划线 | 无 | `text-decoration: none` |
| 光标 | 手型 | `cursor: pointer` |

#### 适用的文本类型

| 文本类型 | 是否支持 Textlink | 说明 |
|----------|------------------|------|
| H1 大标题 | ❌ 不支持 | 标题不应包含链接 |
| H2 一级标题 | ❌ 不支持 | 标题不应包含链接 |
| H3 二级标题 | ❌ 不支持 | 标题不应包含链接 |
| H4 正文段落 | ✅ 支持 | 正文中嵌入链接 |
| H5 前缀正文 | ✅ 支持 | 列表项中嵌入链接 |
| H6 摘要文本 | ✅ 支持 | 引用/摘要中嵌入链接 |
| H7 提示文本 | ✅ 支持 | 辅助说明中嵌入链接（如"了解更多"） |

#### 使用示例

**正文段落 (H4) 中的 Textlink：**
```
这是正文文本，点击[了解详情](https://...)可查看更多信息。
```
渲染效果：`这是正文文本，点击` <span style="color:#214CA5">了解详情</span> `可查看更多信息。`

**提示文本 (H7) 中的 Textlink：**
```
如有疑问，请[联系客服](https://...)或查看[帮助中心](https://...)。
```
渲染效果：`如有疑问，请` <span style="color:#214CA5">联系客服</span> `或查看` <span style="color:#214CA5">帮助中心</span> `。`

#### 注意事项

1. **链接密度**：单段文本中 Textlink 不宜过多，建议不超过 2 个
2. **链接长度**：Textlink 文字应简洁，通常 2-6 个字为宜
3. **位置建议**：Textlink 常位于句末或作为独立短语
4. **无下划线**：设计规范中 Textlink 不带下划线，仅通过颜色区分

### 2.2 文字块间距规范

文本块之间的垂直间距根据相邻元素类型决定，遵循"层级跨度越大，间距越大"原则：

#### 2.2.1 标题后间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| H1 大标题 | H2 一级标题 | **16px** | 大标题后接一级标题 |
| H1 大标题 | H4 正文段落 | **16px** | 大标题后接正文 |
| H2 一级标题 | H3 二级标题 | **12px** | 一级标题后接二级标题 |
| H2 一级标题 | H4 正文段落 | **12px** | 一级标题后接正文 |
| H3 二级标题 | H4 正文段落 | **8px** | 二级标题后接正文 |
| H3 二级标题 | H5 前缀正文 | **8px** | 二级标题后接列表 |

#### 2.2.2 正文/列表间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| H4 正文段落 | H4 正文段落 | **8px** | 段落之间 |
| H4 正文段落 | H5 前缀正文 | **8px** | 正文后接列表 |
| H5 前缀正文 | H5 前缀正文 | **4px** | 列表项之间 |
| H5 前缀正文 | H4 正文段落 | **8px** | 列表后接正文 |

#### 2.2.3 辅助文本间距

| 上方元素 | 下方元素 | 间距值 | 说明 |
|----------|----------|--------|------|
| H4 正文段落 | H6 摘要文本 | **12px** | 正文后接摘要 |
| H4 正文段落 | H7 提示文本 | **16px** | 正文后接提示 |
| H6 摘要文本 | H7 提示文本 | **8px** | 摘要后接提示 |
| H7 提示文本 | H2 一级标题 | **24px** | 提示后接新章节 |

#### 2.2.4 章节分隔间距

| 场景 | 间距值 | 说明 |
|------|--------|------|
| 章节结束 → 新章节开始 | **24px** | 一级标题前的分隔 |
| 内容区块结束 → 新区块开始 | **16px** | 二级标题前的分隔 |

### 2.3 组合顺序规范

文本块的堆叠应遵循以下层级顺序，从上到下递进：

```
┌─────────────────────────────────────────────────────┐
│  H1 大标题（页面/模块标题，可选）                      │
├─────────────────────────────────────────────────────┤
│  H2 一级标题（章节标题）                              │ ← 16px
├─────────────────────────────────────────────────────┤
│  H3 二级标题（子章节标题，可选）                       │ ← 12px
├─────────────────────────────────────────────────────┤
│  H4 正文段落 / H5 前缀正文（内容主体）                 │ ← 8px
│  H4 正文段落 / H5 前缀正文                           │ ← 8px/4px
│  ...                                                │
├─────────────────────────────────────────────────────┤
│  H6 摘要文本（引用/摘要，可选）                        │ ← 12px
├─────────────────────────────────────────────────────┤
│  H7 提示文本（辅助说明/脚注，可选）                    │ ← 8px
└─────────────────────────────────────────────────────┘
```

#### 2.3.1 层级递进规则

1. **标题层级递减**：大标题(H1) → 一级标题(H2) → 二级标题(H3)，不可跨级（如 H1 直接到 H3）
2. **内容主体居中**：正文段落(H4)和前缀正文(H5)构成内容核心
3. **辅助信息置尾**：摘要文本(H6)和提示文本(H7)放在内容区块末尾
4. **前缀正文限定**：H5 仅用于带编号/标记的内容，普通文本使用 H4

#### 2.3.2 禁止的组合

| 禁止模式 | 原因 |
|----------|------|
| H7 提示文本 → H4 正文段落 | 提示文本应为区块末尾，后面应是新章节 |
| H6 摘要文本 → H3 二级标题 | 引用后不应直接接子标题 |
| H1 大标题 → H1 大标题 | 同级大标题不可连续 |
| H5 前缀正文 → H1/H2 标题 | 列表项后应有间隔段落或章节分隔 |

#### 2.3.3 推荐的内容模板

**模板 A：标准文章结构**
```
H1 大标题
  └─ H4 正文段落（导语）
  
H2 一级标题（第一章）
  └─ H4 正文段落
  └─ H4 正文段落
  └─ H6 摘要文本
  
H2 一级标题（第二章）
  └─ H3 二级标题
    └─ H4 正文段落
    └─ H5 前缀正文（列表）
  └─ H3 二级标题
    └─ H4 正文段落
  └─ H7 提示文本
```

**模板 B：说明/帮助页面**
```
H2 一级标题（主题）
  └─ H4 正文段落（简介）

H3 二级标题（步骤/要点）
  └─ H5 前缀正文（1. 第一步）
  └─ H5 前缀正文（2. 第二步）
  └─ H5 前缀正文（3. 第三步）

H6 摘要文本（注意事项）
H7 提示文本（更多帮助链接）
```

**模板 C：卡片内简介**
```
H3 二级标题（卡片标题）
  └─ H4 正文段落（简短描述）
  └─ H7 提示文本（时间/来源）
```

---

## 3. 通用布局规格

| 属性 | 值 |
|------|------|
| 容器宽度 | 428px |
| 背景色 | `transparent`（组件本身透明，跟随页面背景色） |
| 布局模式 | `display: flex`（弹性布局） |
| `position` | `relative` |
| 左右内边距 | 16px（`padding-left: 16px; padding-right: 16px`） |
| 文字区域宽度 | 396px（容器 428 - 左右各 16px 内边距） |

### 3.1 上下内边距规则

| 变体分组 | 上下内边距 | 适用变体 |
|---------|-----------|---------|
| 大标题 | 8px | H1/C1 |
| 一级标题、二级标题 | 4px | H2/C2、H3/C3 |
| 正文、前缀正文、摘要、提示 | 0px | H4/C4、H5、H6/C5、H7/C6 |

---

## 4. 设计 Token

| Token 名称 | CSS 变量 | 值 | 使用变体 |
|-----------|---------|------|---------| 
| 主文字色 | `--text-primary` | `rgba(0, 0, 0, 0.90)` | 全部（H1-H7、C1-C6） |
| 链接色 | `--text-link` | `#214CA5` | H4/H5/H6/H7/C4/C5/C6 内联 Textlink |
| 背景色 | — | `transparent` | 全部（组件本身透明，跟随页面背景色） |

---

## 5. 使用场景

| 场景 | 推荐变体 |
|------|---------| 
| 页面/模块大标题 | H1（居左）、C1（居中） |
| 内容区段标题 | H2（居左）、C2（居中） |
| 二级分类标题 | H3（居左）、C3（居中） |
| 说明文案/详情描述 | H4（居左）、C4（居中） |
| 带序号/标记的段落 | H5（居左前缀正文） |
| 次要摘要信息 | H6（居左）、C5（居中） |
| 底部提示/辅助文字 | H7（居左）、C6（居中） |

---

## 8. CSS 实现代码块

### 6.1 文本块容器

```css
.text-block-container {
    width: 428px;
    background: transparent;
    position: relative;
    display: flex;
    padding-left: 16px;
    padding-right: 16px;
}
```

### 6.2 标题体系

```css
/* H1/C1 大标题 26px Semibold — padding-top/bottom: 8px */
.text-block-container .text-block-title {
    font-family: 'PingFang SC', sans-serif;
    font-size: 26px;
    font-weight: 600;
    color: var(--text_primary);
    line-height: 34px;
    word-wrap: break-word;
}
.text-block-container .text-block-title.center { text-align: center; }
.text-block-container .text-block-title.left { text-align: left; }

/* H2/C2 一级标题 22px Medium — padding-top/bottom: 4px */
.text-block-container .text-block-subtitle {
    font-family: 'PingFang SC', sans-serif;
    font-size: 22px;
    font-weight: 500;
    color: var(--text_primary);
    line-height: 28px;
    word-wrap: break-word;
}
.text-block-container .text-block-subtitle.center { text-align: center; }
.text-block-container .text-block-subtitle.left { text-align: left; }

/* H3/C3 二级标题 18px Medium — padding-top/bottom: 4px */
.text-block-container .text-block-aux-title {
    font-family: 'PingFang SC', sans-serif;
    font-size: 18px;
    font-weight: 500;
    color: var(--text_primary);
    line-height: 26px;
    word-wrap: break-word;
}
.text-block-container .text-block-aux-title.center { text-align: center; }
.text-block-container .text-block-aux-title.left { text-align: left; }
```

### 8.3 正文、摘要与提示

```css
/* H4/H5/C4 正文段落 17px Regular — padding-top/bottom: 0px */
/* H5 与 H4 样式相同，仅语义不同（H5 用于带前缀标识的列表项） */
.text-block-container .text-block-body {
    font-family: 'PingFang SC', sans-serif;
    font-size: 17px;
    font-weight: 400;
    color: var(--text_primary);
    line-height: 24px;
    word-wrap: break-word;
}
.text-block-container .text-block-body.center { text-align: center; }
.text-block-container .text-block-body.left { text-align: left; }

/* H6/C5 摘要文本 14px Regular — padding-top/bottom: 0px */
.text-block-container .text-block-summary {
    font-family: 'PingFang SC', sans-serif;
    font-size: 14px;
    font-weight: 400;
    color: var(--text_primary);
    line-height: 20px;
    word-wrap: break-word;
}
.text-block-container .text-block-summary.center { text-align: center; }
.text-block-container .text-block-summary.left { text-align: left; }

/* H7/C6 提示文本 12px Regular — padding-top/bottom: 0px */
.text-block-container .text-block-hint {
    font-family: 'PingFang SC', sans-serif;
    font-size: 12px;
    font-weight: 400;
    color: var(--text_primary);
    line-height: 17px;
    word-wrap: break-word;
}
.text-block-container .text-block-hint.center { text-align: center; }
.text-block-container .text-block-hint.left { text-align: left; }
```

### 6.4 Textlink 链接样式

```css
/* Textlink 内联链接色 - 适用于正文、摘要、提示文本 */
.text-block-container .text-link,
.text-block-container a {
    color: var(--text_link);
    text-decoration: none;
    cursor: pointer;
}

/* 字号继承父容器 */
.text-block-body .text-link { font-size: 17px; }
.text-block-summary .text-link { font-size: 14px; }
.text-block-hint .text-link { font-size: 12px; }
```

---

## 7. 溢出处理规则

### 9.1 独立使用（页面级）
- 文本块为**自适应高度**组件，不设 max-height，不截断
- 所有文本使用 `word-wrap: break-word` 自动换行
- 行数不限制，高度由内容自然撑开

### 7.2 嵌入 Card C10 时
- 受 Card C10 容器约束：`max-height: 784px`（840px - 56px 头像行）
- 超过 max-height 时启用纵向滚动（`overflow-y: auto`）
- 滚动容器支持 `-webkit-overflow-scrolling: touch`

### 9.3 文本截断规则
| 元素 | 截断方式 | 说明 |
|------|---------|------|
| 所有标题（H1-H3/C1-C3） | 不截断 | 标题自动换行，高度自适应 |
| 正文段落（H4/C4） | 不截断 | 自动换行，高度自适应 |
| 前缀正文（H5） | 不截断 | 列表项支持多行 |
| 摘要文本（H6/C5） | 不截断 | 自动换行 |
| 提示文本（H7/C6） | 不截断 | 自动换行 |

> **设计意图**：文本块是纯内容展示组件，所有文本均完整展示不截断。高度限制仅在嵌入 Card C10 等受限容器时由外层容器控制。
