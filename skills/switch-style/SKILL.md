---
name: switch-style
description: This skill should be used when the user wants to switch, apply, or transform an existing UI/page/component into a different brand's visual style (e.g., "switch to Apple style", "make it look like Stripe", "apply Spotify theme"). It reads the corresponding brand DESIGN.md from the awesomedesign directory and applies the brand's complete visual system — colors, typography, spacing, shadows, border-radius, component stylings — to the target interface while preserving its structure and content. Supports 58 brand styles including Apple, Stripe, Spotify, Linear, Tesla, Ferrari, Notion, Figma, Vercel, and more.
---

# switch-style

## 概述

本 skill 将已有的 UI 界面（HTML 页面/组件）切换为指定品牌的视觉风格。品牌视觉规范存储在项目 `awesomedesign/` 目录中，每个品牌子目录包含一个 `DESIGN.md` 文件，定义了完整的设计系统：颜色、字体、组件样式、布局、阴影、圆角、响应式行为等。

切换风格时，**保留页面的结构和内容不变**，仅替换视觉层（颜色、字体、间距、圆角、阴影、组件外观），使页面呈现出目标品牌的设计语言。

## 何时使用

在以下场景触发：

- 用户要求将界面"切换/转换/应用"为某个品牌的视觉风格
- 用户提及品牌名称 + 风格/样式/主题相关词汇（如"Apple 风格"、"像 Stripe 那样"、"Spotify 主题"）
- 用户要求"换个风格"、"换个视觉方案"、"用 XX 的设计语言重新渲染"
- 用户要求对比不同品牌风格的视觉效果

不触发的场景：

- 用户从零生成界面（使用 QQ-GENUI 等其他 skill）
- 用户仅讨论品牌设计理念但不要求应用到具体界面
- 纯后端或非 UI 任务

## 可用品牌列表

品牌风格文件位于 `awesomedesign/<brand>/DESIGN.md`，完整列表参见 `references/brand-index.md`。

当前支持 **58 个品牌**，涵盖科技、汽车、金融、设计工具、AI 等领域。

## 执行流程

### Step 1：确认目标品牌与源界面

- 从用户请求中识别目标品牌名称
- 将品牌名映射为 `awesomedesign/` 下的目录名（参见 `references/brand-index.md`）
- 若用户提及的品牌不在支持列表中，告知用户并列出可用品牌供选择
- 确认待切换的源界面文件（HTML）路径

### Step 2：读取品牌 DESIGN.md

- 使用 `read_file` 读取 `awesomedesign/<brand>/DESIGN.md`
- 可参考同目录下的 `preview.html`（亮色预览）和 `preview-dark.html`（暗色预览）作为该品牌的交互式 Token 目录与视觉效果参考
- 重点提取以下章节并内化为当前上下文的设计约束：
  1. **Color Palette & Roles** — 颜色映射规则
  2. **Typography Rules** — 字体、字号、字重、行高、字间距
  3. **Component Stylings** — 按钮、卡片、输入框、导航栏等组件样式
  4. **Layout Principles** — 间距系统、圆角体系
  5. **Depth & Elevation** — 阴影层级
  6. **Do's and Don'ts** — 必须遵守的设计红线

### Step 3：分析源界面结构

- 读取源 HTML 文件
- 识别页面中的组件类型（按钮、卡片、列表、导航栏、输入框、图标等）
- 提取当前使用的颜色值、字体、间距、圆角、阴影等样式属性
- 建立"源样式 → 目标样式"的映射关系

### Step 4：执行风格切换

按以下维度逐项替换，保持页面结构和内容不变：

**4.1 颜色系统**
- 页面背景色 → 目标品牌的 Primary/Surface 背景色
- 文字颜色 → 目标品牌的 Text 层级颜色（Heading / Body / Secondary / Muted）
- 强调色/交互色 → 目标品牌的 Interactive/Accent 颜色
- 边框颜色 → 目标品牌的 Border 颜色
- 语义颜色（成功/警告/错误）→ 目标品牌的 Semantic 颜色（若有定义）

**4.2 字体与排版**
- font-family → 目标品牌的字体族（含 fallback）
- 启用目标品牌要求的 OpenType 特性（如 `font-feature-settings`）
- font-size / font-weight / line-height / letter-spacing → 按目标品牌的 Typography Hierarchy 映射
- 保持文字内容和层级关系不变，仅调整视觉表现

**4.3 组件样式**
- 按钮 → 按目标品牌的 Button 规范替换（背景、文字色、padding、radius、hover 效果）
- 卡片/容器 → 按目标品牌的 Cards & Containers 规范替换
- 输入框 → 按目标品牌的 Inputs & Forms 规范替换
- 导航栏 → 按目标品牌的 Navigation 规范替换
- 徽章/标签 → 按目标品牌的 Badges/Pills 规范替换

**4.4 间距与圆角**
- padding / margin / gap → 按目标品牌的 Spacing System 调整
- border-radius → 按目标品牌的 Border Radius Scale 映射

**4.5 阴影与深度**
- box-shadow → 按目标品牌的 Depth & Elevation 层级替换
- backdrop-filter → 若目标品牌有玻璃效果等特殊处理，同步应用

**4.6 特殊处理**
- 若目标品牌为暗色系（如 Spotify、Linear）但源界面为亮色，需完整切换 Light → Dark
- 若目标品牌为亮色系（如 Apple light、Stripe）但源界面为暗色，需完整切换 Dark → Light
- 尊重 DESIGN.md 中 "Do's and Don'ts" 的硬约束

### Step 5：验证与输出

- 检查所有颜色值是否来自目标品牌的 Color Palette
- 检查字体是否正确设置（含 OpenType 特性）
- 检查组件样式是否符合目标品牌的 Component Stylings
- 检查 Do's and Don'ts 中的禁止项是否均已避免
- 输出切换后的完整 HTML 文件

## 输出格式

切换完成后，回复应包含：

1. **品牌风格概要**：一句话描述目标品牌的视觉特征
2. **切换后的 HTML 文件**：完整可运行的 HTML
3. **变更摘要**：列出关键的视觉变更点（颜色、字体、圆角、阴影等）

## 禁止项

- 禁止修改页面的结构、内容或功能逻辑，仅替换视觉样式
- 禁止使用 DESIGN.md 中未定义的颜色值
- 禁止忽略 DESIGN.md 中 "Don't" 列出的禁止规则
- 禁止在没有读取 DESIGN.md 的情况下凭记忆应用品牌风格
- 禁止混用多个品牌的视觉元素（除非用户明确要求混搭）

## 参考资料

- `references/brand-index.md`：58 个品牌的目录名索引与简要风格描述
