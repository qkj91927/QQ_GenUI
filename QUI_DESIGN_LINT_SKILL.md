# QUI Design Lint

> 设计任务完成后的合规自检。适用于任何 AI 平台，无外部依赖。
> 基于 QUI Basic 1.0（22 个母组件 · 529 变体 · 33 通用图标 · 437 业务图标 · 10 真实头像 SVG · 14 插图 PNG · 10 风景照片 JPG · 428px iPhone 基准）。

## 使用方法

将生成的代码 + 本文件一起发给 AI：
> 请按 QUI Design Lint 逐项检查我的代码，输出报告。

---

## 第〇步：Preflight（基线声明）

开始检查前，AI 必须先**逐项清点**并声明本次检查的代码覆盖面，作为后续计分基线：

```
📋 Preflight
- 涉及组件：N 个（navbar × ? / list × ? / card × ? / ...）
- 涉及图标：M 个（逐个列出 src 路径 + 着色 Token）
- 涉及 Token：K 个（color / spacing / radius / font-size / shadow / border）
- 页面结构：StatusBar ? / NavBar ? / HomeBar ? / 背景色 ? / 主题(light/dark) ?
- 交互状态：是否包含 hover / pressed / disabled / loading 态
- 容器宽度：428 通栏 ? 个 / 396 嵌入 ? 个
- 元标记识别：已扫描关联 spec 中的 @MUST / @FORBIDDEN / @LINT / @SPEC_OF_TRUTH 声明
```

> ⚠️ 跳过 Preflight 直接开检的，视为检查不完整，评级上限为 C。

### 元标记识别表（强约束语义）

组件 spec md 文件可使用以下元标记对 AI 下达**机器可识别的硬性指令**。AI 读 spec 时必须按此语义处理：

| 标签 | 含义 | AI 处理规则 | 违规后果 |
|------|------|-----------|---------|
| `@MUST` | 必须做到 | **硬约束**，不可妥协、不可解读为建议 | ⛔ ERROR |
| `@FORBIDDEN` | 明确禁止 | **硬约束**，不可妥协、不可当"除非特殊情况"处理 | ⛔ ERROR |
| `@LINT <ID>` | 关联 lint 规则号 | 机器可读索引，便于跨文件追踪 | — |
| `@SPEC_OF_TRUTH` | 本文件为权威规范，与其他文件冲突时以此为准 | AI 必须优先信任此 spec | — |
| 自然语言（"必须"/"应该"/"推荐"/"建议"/"不可"等） | 说明性内容 | 非机器硬规则，AI 可作参考但不强制 | — |

**关键语义区分**：
- `@MUST` / `@FORBIDDEN` 是**代码级硬约束**，AI 违反会直接产生 ⛔ ERROR
- 自然语言描述（即使用"必须"二字）是**文档级说明**，不构成自动化检查的依据
- spec 顶部通常有 `## 🔒 强约束声明` 块，AI 扫描 spec 时**必须首先读此块**
- 声明块外的自然语言条款是补充说明，与 @ 标签冲突时以 @ 标签为准

---

## 检查哲学：两级违规制

所有检查项采用**两级违规**判定，严格程度递增：

| 级别 | 含义 | 示例 | 输出标记 |
|------|------|------|---------|
| **⚠️ WARN** | 值碰巧正确，但没有通过 Token/变量引用 | `border-radius: 12px` 值正确但应写 `var(--radius-m)` | ⚠️ 值正确但未绑定 Token |
| **⛔ ERROR** | 值本身就不在合法范围内 | `font-size: 15px` 不在 11 档合法字号中 | ⛔ 值非法 |

> **核心原则**（借鉴 figma-design-audit）：**即使值碰巧正确，只要没有通过 Token 变量引用，就视为违规。**
> 因为当 Token 值更新时，硬编码无法自动同步，会导致系统性不一致。

---

## 第一步：组件合法性验证（最重要）

**逐个检查代码中使用的每个 UI 元素，必须能在下方「组件注册表」中找到匹配。**

### 视觉参照

所有组件变体的**权威视觉样式**以 `component-matrix.html` 为准。
细节规范以 `md/{COMPONENT}_COMPONENT_SPEC.md` 为权威来源，skill 与 spec 冲突时**以 spec 为准**。

### 验证流程（组件层入口）

对代码中**每个 UI 元素**执行：

```
1. 识别 → 在注册表中找母组件
   ├─ 找到 → 步骤 2
   └─ 找不到 → ⛔ F1 非法组件 → 执行「替代方案」

2. 匹配变体 → 确认子组件 ID 在变体空间中
   ├─ 存在 → 步骤 3
   └─ 不存在 → ⛔ F4 非法变体 → 给出最近合法变体建议

3. 容器宽度 → 通栏=428 / 嵌入=396（见 S17）
   ├─ 一致 → 步骤 4
   └─ 不一致 → ⛔ S17 非法宽度

4. 比对 UI → 与 component-matrix.html / spec 视觉比对
   ├─ 一致 → ✅ 通过
   └─ 不一致 → ⛔ UI 不规范 → 列出差异并给出修正
```

### FORBIDDEN 模式：禁止行为 ⛔

| 代号 | 禁止行为 | 典型 AI 犯错示例 |
|------|---------|-----------------|
| F1 | **发明组件**：使用注册表中不存在的组件 | `<TabBar>`, `<Drawer>`, `<FloatingButton>`, `<Carousel>`, `<Stepper>` |
| F2 | **魔改结构**：修改组件的维度/区域/插槽 | 给 NavBar 添加第四个区域、给 List 行添加第三行描述 |
| F3 | **跨组件嫁接**：违反下方「嵌套允许矩阵」的组合 | 把 Card 放进另一个 Card、把 Dialog 放进 ActionSheet |
| F4 | **自创变体**：使用不在变体矩阵中的排列组合 | NavBar L6+C5（约束中已过滤） |
| F5 | **修改固定值**：更改组件的固定尺寸 | NavBar 高度改为 48px、ActionSheet 行高改为 60px |
| F6 | **硬编码颜色**：使用 `#xxx`/`rgb()` 代替 Token | `color: #333333` 代替 `var(--text-primary)` |
| F7 | **非法字号**：使用 11 档之外的 font-size | `font-size: 15px`、`font-size: 13px` |
| F8 | **非法间距**：见 TK2a/TK2b（布局间距 vs 组件固有尺寸）| `padding: 10px`（用户层布局）、`gap: 11px` |
| F9 | **缺少 StatusBar**：页面顶部没有 428×54px 状态栏 | 页面直接从 NavBar 开始 |
| F10 | **模态嵌套**：Dialog/ActionSheet/HalfScreenOverlay 互相嵌套 | Dialog 中弹出 ActionSheet |
| F11 | **自绘图标**：用 `<svg><path d="…"/></svg>` 直接画图形代替调用 icons/ | AI 自行编写 SVG path 画箭头/关闭/勾选等 |
| F12 | **Emoji/字符当图标**：Unicode 字符替代真实 SVG | ✓ ✗ → ← ⚠ ❤ ⭐ 🔍 等作为 UI 图标 |
| F13 | **外部图标库**：引入 QUI 之外的图标源 | Font Awesome / Material Icons / iconify / lucide / heroicons 等 |
| F14 | **硬编码图标尺寸**：Avatar/Thumbnail 显示尺寸与文件名后缀不符 | `Avatar_40.svg` 以 `width:32px` 渲染 |
| F15 | **Base64/外链图片当图标**：绕过 icons/ 目录 | `data:image/svg+xml;base64,…` 或 `https://cdn.../x.svg` |
| **F16** | **SVG 内部硬编码颜色**：SVG 文件内 `fill="#xxx"` 导致 token 着色失效 | 应改为 `fill="currentColor"` + CSS `color: var(--icon-xxx)` |
| **F17** | **非 Button 场景使用 filter hack 改色** | 用 `filter: brightness(0)` 给普通图标染色。仅 Button 内部白色图标允许 |
| **F18** | **不支持加载态的组件强加 loading** | Button S3/S4/T3 加 spinner；Menu/List 项加 loading；应改用 Toast T1 |
| **F19** | **实际任务中未替换头像占位图**：使用 `Avatar_32/40/52.svg` 占位 SVG 出现在最终交付的 demo / 页面 / 演示中，未替换为 `icons/QUI_Avatars/AvatarN.svg`（N ∈ 1..10）真实头像。允许等比缩放到 32/40/52 任一尺寸；同页多个头像须用不同编号。 | 任务交付的 list / card / message / navbar L6 等含头像的位置仍引用 `icons/Avatar_40.svg` 而非 `icons/QUI_Avatars/Avatar3.svg` |
| **F20** | **实际任务中未替换图片 / 插图占位图**：`placeholder_landscape/portrait/square.svg` 占位图出现在最终交付中，未替换为 `icons/QUI_illustrations/` 下的真实素材（插图 `illustrationN.png` N ∈ 1..14，或风景照片 `landscape photosN.JPG` N ∈ 1..10）。**插图 vs 照片的选择**按场景偏好（见下文 Convention 约定）：Card / HSO 新手引导 → 插图；四 / 九宫格 → 照片；非强制、可混用。同页多个素材须用不同编号。 | 任务交付的 Card C1-C5 / ImageBlock / 宫格 / 运营 banner 仍引用 `icons/placeholder_landscape.svg` 而非 `icons/QUI_illustrations/illustration5.png` 或 `icons/QUI_illustrations/landscape%20photos3.JPG` |

### FORBIDDEN 模式：常见 AI 错误写法 ❌ vs 正确写法 ✅

```
❌ .card-title { color: #333333; font-size: 15px; border-radius: 14px; }
✅ .card-title { color: var(--text-primary); font-size: 17px; border-radius: var(--radius-m); }

❌ <svg><path d="M6 9l6 6 6-6"/></svg>             ← F11 自绘 chevron
✅ <img src="icons/chevron_down.svg">

❌ <span>✓ 已完成</span>                           ← F12 Emoji 当图标
✅ <img src="icons/tick.svg"> 已完成

❌ <svg fill="#000000">...</svg>                    ← F16 SVG 硬编码颜色
✅ <svg fill="currentColor">...</svg> + CSS: color: var(--icon-secondary)

❌ <img src="icons/search.svg" style="filter: hue-rotate(180deg)"> ← F17 非 Button 用 filter
✅ <img src="icons/search.svg" style="color: var(--icon-blue)"> （配合 currentColor）

❌ <img src="icons/Avatar_40.svg" style="width:32px;height:32px"> ← F14 尺寸错位
✅ <img src="icons/Avatar_32.svg" style="width:32px;height:32px">

❌ <img src="icons/Avatar_40.svg" style="border-radius:50%">  ← F19 实际任务未替换占位图
✅ <img src="icons/QUI_Avatars/Avatar3.svg" style="width:40px;height:40px;border-radius:50%">

❌ <img src="icons/placeholder_landscape.svg" style="width:428px">  ← F20 实际任务未替换图片占位图
✅ <img src="icons/QUI_illustrations/illustration5.png" style="width:428px;object-fit:cover">  ← Card / HSO 新手引导用插图
✅ <img src="icons/QUI_illustrations/landscape%20photos3.JPG" style="width:141px;object-fit:cover">  ← 四宫格 / 九宫格用照片（注意 %20 编码）

❌ <div class="card"><div class="card">...</div></div>  ← F3 Card 嵌 Card
✅ 改为 Card C10 + 内部放 text_block/image_block/action
```

### ALLOWED 模式：合法用法速查

| 类别 | ALLOWED（仅以下值/方式合法） |
|------|---------------------------|
| **组件** | 仅注册表中 22 个母组件的 503 种变体 |
| **颜色** | 仅 `var(--token)` 形式引用 39 个颜色 Token |
| **字号** | 仅 10·12·14·16·17·18·20·22·26·28·34 px（11 档） |
| **字重** | 仅 400·500·600·700（Regular/Medium/Semibold/Bold 4 档） |
| **行高** | 仅 1.2·1.4·1.5·1.65（4 档比例） |
| **布局间距** | 仅 4·8·12·16·24·32 px → `var(--spacing-*)` |
| **组件固有尺寸** | 按 spec 精确匹配（含 10/14/34px 等非 4-mult 合法值） |
| **圆角** | 仅 4·8·12·16·20·24·1000 px → `var(--radius-*)`（Button S1 14px 例外）|
| **阴影** | 仅 `var(--shadow-menu)`（主 CSS 定义的唯一阴影 Token） |
| **动效时长** | 150 / 200 / 250 / 300 / 420 ms（5 档 · iOS-aligned · 见 TK12） |
| **缓动曲线** | 5 档 cubic-bezier：standard / out / in / emphasized / linear（见 TK12） |
| **缓动** | ease / ease-in / ease-out / ease-in-out / linear |
| **z-index** | 10(sticky) / 100(modal) / 9999(toast) 三档 |
| **object-fit** | `cover` 默认，特殊场景可 `contain` |
| **border-color** | 必须 `var(--border-*)`，禁止 rgba 硬编码 |
| **背景色** | 含 Card/Grouped List/Message/AIO → `var(--bg-secondary)`(#F0F0F2)；其余 → `var(--bg-bottom)`(#FFFFFF) |
| **NavBar / HS_NavBar 底色** | 仅 `bg-bottom` / `bg-secondary` / `bg-bottom-brand` / `bg-top`（见 NV1 拼接矩阵）。**禁止 transparent / fill-\* / 毛玻璃 / 硬编码 rgba** |
| **NavBar 分割线** | 默认无；滚动时显示 **0.5px + `var(--border-weak)`**（对齐 divider A1）。必须用 `::after` 伪元素 + opacity 切换，**禁止 border-bottom / 其他高度或颜色**（见 NV2）|
| **AIO Input 底色** | `var(--bg-bottom)` 实色（与 NavBar 统一 bg-* 路线，不使用毛玻璃）|
| **图标** | 仅 `icons/` 目录中的 SVG 文件（详见 Step 1.5 清单） |
| **图标着色** | `var(--icon-*)` 5 Token，配合 SVG `fill="currentColor"` |
| **占位图** | 图片缺失时必须用 `icons/placeholder_*.svg`，禁止纯灰矩形代替 |
| **空态填充** | `var(--fill-tertiary)` |
| **设备宽度** | 通栏 = 428px · 卡片/嵌入 = 396px |
| **主题** | 通过 `[data-theme="qq-light|qq-dark"]` 切换，禁止 `@media prefers-color-scheme` |

### ⛔ 非法组件的替代方案（必须执行）

发现非法组件时，**不能简单删除**，必须分析其产品意图并用合法组件替代：

| 常见非法组件 | 产品意图 | 推荐替代方案 |
|------------|---------|------------|
| 底部 TabBar | 多页面切换 | NavBar C5 分段选择 + 页面级切换 |
| 抽屉菜单/侧边栏 | 导航入口集合 | HalfScreenOverlay HSO-A + 内嵌 Grouped List |
| 浮动操作按钮 (FAB) | 主操作入口 | ActionCombo A1(单主按钮) 固定在页面底部 |
| 轮播 Banner | 图片循环展示 | ImageBlock A2(通栏轮播) 或 B2(嵌入轮播) |
| 底部弹出选择器 | 单选/多选 | ActionSheet 或 HalfScreenOverlay + Grouped List(勾选) |
| 进度条/步骤条 | 流程进度 | TextBlock H6(摘要文本) 描述当前步骤 + 多页面 NavBar 导航 |
| 徽标/红点通知 | 未读提示 | NavBar L2 的 Badge（仅限 NavBar 内） |
| 评分/星级 | 评价打分 | 不支持，需向设计师申请新增组件 |
| 下拉刷新 | 内容更新 | 交互行为，不属于静态组件范畴 |
| 自定义卡片 | 信息聚合 | Card C1-C10 中选择最接近的变体 |

---

## 第 1.5 步：图标使用验证（必检专项）

图标是 AI 最容易违规的区域——清单外、自绘、Emoji 替代、外部库、着色失效都属常见错误。对代码中**每一处图标**（含 `<img>`、`<svg>`、`background-image`）执行下列检查：

```
1. 来源验证
   是 <img src="icons/xxx.svg"> 形式？
   ├─ 是 → 步骤 2
   └─ 否 → ⛔ F11/F12/F13/F15（按具体违规类型判定）

2. 清单验证
   xxx.svg 是否存在于下方「图标资源清单」？
   ├─ 是 → 步骤 3
   └─ 否 → ⛔ 图标缺失 → 从清单中找最接近语义的替代 / 或标注 🔶 需求缺口

3. 尺寸验证
   - 通用图标：CSS 渲染尺寸是否为 16/20/24 标准档位？
   - Avatar：文件名后缀（_32/_40/_52）是否与 CSS width/height 严格一致？
   - Thumbnail：文件名后缀（_24/_32/_40/_52/_88）是否与 CSS width/height 严格一致？
   ├─ 一致 → 步骤 4
   └─ 不一致 → ⛔ F14 硬编码图标尺寸

4. 着色验证（新增）
   - 图标是否用 var(--icon-*) 之一着色？
   - SVG 内是否用 fill="currentColor"（非硬编码颜色）？
   - 着色 Token 是否与同层文字色语义对齐（见「图标着色指南」）？
   ├─ 全通过 → 步骤 5
   └─ 否 → ⛔ F16（SVG 硬编码）或 TK10（着色未绑定 Token）

5. 场景验证
   图片缺失/占位场景是否使用正确的 placeholder_landscape/portrait/square.svg？
   ├─ 是 → ✅ 通过
   └─ 否（用了灰矩形 / 彩色块 / 文字占位 / 错配场景）→ ⛔ 占位图违规
```

---

## 图标资源清单（icons/ 共 33 通用 + 437 业务）

### 通用操作图标（建议尺寸 16/20/24）
| 文件 | 用途 |
|------|------|
| `chevron_right.svg` | 右箭头 / 进入下级 / 列表右侧箭头 |
| `chevron_left.svg` | 左箭头 / 返回 |
| `chevron_down.svg` | 下箭头 / 展开 / 下拉指示 |
| `expand_list.svg` | 列表展开（专用，区别于 chevron） |
| `close.svg` | 通用关闭 |
| `close_input.svg` | 输入框内清除 |
| `Close_HalfScreen.svg` | 半屏浮层关闭（专用） |
| `search.svg` | 搜索 |
| `more_upright.svg` | 更多（竖向三点） |
| `tick.svg` | 勾选已选（用于列表项） |
| `done.svg` | 完成态（操作反馈） |
| `Checkbox.svg` | 未勾选态复选框 |
| `Checkbox_filled.svg` | 已勾选态复选框 |
| `loading.svg` | 加载态（通常需加旋转动画） |
| `heart.svg` | 收藏/喜欢 |
| `remind_mute.svg` | 免打扰/静音 |
| `doc.svg` | 文档 |
| `empty_icon.svg` | 空状态占位图标 |
| `secondary.svg` | 二级功能入口 |

### 头像占位（固定 3 档，尺寸即文件名）
| 文件 | 必须渲染尺寸 |
|------|------------|
| `Avatar_32.svg` · `Avatar_40.svg` · `Avatar_52.svg` | 32/40/52 |

> ⚠️ **占位图仅作矩阵展示用**：实际任务（demo / 页面 / 演示）中**必须**用 `icons/QUI_Avatars/` 下的真实头像资源（`Avatar1.svg` ~ `Avatar10.svg`，共 10 张 52×52 SVG · 透明背景圆形）替换 `Avatar_32/40/52.svg` 占位图。**允许等比缩放**到 32 / 40 / 52 任一尺寸。详见 F19。

### 真实头像资源：`icons/QUI_Avatars/`（10 张 52×52 SVG）
| 资源 | 用途 |
|------|------|
| `Avatar1.svg` ~ `Avatar10.svg` | QQ 企鹅头像图集，10 张随机互斥可选；任务中替换 `Avatar_32/40/52.svg` 占位图 |

**使用规则**：
1. 任务中需要展示头像时，**优先使用** `icons/QUI_Avatars/AvatarN.svg`（N ∈ 1..10，单数字无前导零）
2. **允许等比缩放**：原图 52×52，渲染时 `width: 32px; height: 32px;` / `width: 40px; height: 40px;` / `width: 52px; height: 52px;` 任一尺寸均合法
3. 同一页面多个头像时，应使用**不同编号**（避免重复，最多 10 个不重复头像）
4. 渲染必须 `border-radius: 50%` 保持圆形
5. **禁止**用第三方头像 URL、禁止 Base64 嵌入

### 插图 / 照片资源：`icons/QUI_illustrations/`（14 插图 + 10 照片）

该目录包含**两种风格**的素材，用途不同：

| 风格 | 文件 | 张数 | 典型场景 |
|------|------|------|---------|
| **插图 Illustration**（卡通 / 图形化） | `illustration1.png` ~ `illustration14.png` | 14 | Card 富媒体 / HalfScreenOverlay 新手引导 / 运营 banner / 引导图 |
| **风景照片 Landscape Photo**（真实照片） | `landscape photos1.JPG` ~ `landscape photos10.JPG` | 10 | Card C5 九宫格 · ImageBlock A4/A5/B4/B5 四宫格 / 九宫格 · 内容真实性要求强的场景 |

> ⚠️ **占位图仅作矩阵展示用**：实际任务（demo / 页面 / 演示）中**必须**用 `icons/QUI_illustrations/` 下的真实素材替换 `placeholder_landscape/portrait/square.svg` 三类占位图。详见 F20。

**📌 使用场景偏好（软性约定 · Convention，非 MUST）**：
| 场景 | 推荐素材 | 说明 |
|------|---------|------|
| **卡片 Card** 内的占位图 | 插图 `illustrationN.png` | Card 内容多为图文混排，插图更协调 |
| **半屏浮层 HSO 新手引导** | 插图 `illustrationN.png` | 新手引导需要友好、有亲和力的视觉，适合插图 |
| **运营 banner / 引导图** | 插图 `illustrationN.png` | 品牌氛围 / 营销语境 |
| **四宫格 / 九宫格**（Card C5 · ImageBlock A4/A5/B4/B5 · ActionSheet 宫格） | 照片 `landscape photosN.JPG` | 多图陈列要真实感 |

**软性约定的灵活性**：以上为推荐偏好，设计师可根据实际任务性质灵活选择——比如：某卡片内容强调"真实案例"可用照片；某宫格内容强调"品牌风格"可用插图。两者混用亦合法。

> **空页面 / 空状态**：暂不做额外规则，保持空白即可，后续视需要再补充规范。

**使用规则**：
1. 任务中需要展示图片 / 插图时，**优先使用** `icons/QUI_illustrations/` 下的素材
2. 引用方式：
   - 插图：`<img src="icons/QUI_illustrations/illustrationN.png" style="object-fit: cover;">` (N ∈ 1..14)
   - 照片：`<img src="icons/QUI_illustrations/landscape%20photosN.JPG" style="object-fit: cover;">` (N ∈ 1..10)
3. **文件名含空格的照片**：HTML 引用时**空格需 URL 编码为 `%20`**（`landscape%20photos1.JPG`），否则部分环境会加载失败
4. **同一页面多个素材时用不同编号**（插图最多 14 不重复 / 照片最多 10 不重复）
5. **禁止**用第三方图片 URL / Base64 / 自绘 SVG 替代
6. **填充方式**：默认 `object-fit: cover`（保证不变形）

### 缩略图占位（固定 5 档，尺寸即文件名）
| 文件 | 必须渲染尺寸 |
|------|------------|
| `Thumbnail_24 / 32 / 40 / 52 / 88.svg` | 24/32/40/52/88 |

### 占位图（按场景绑定，见下方映射）
`placeholder_landscape.svg` · `placeholder_portrait.svg` · `placeholder_square.svg`

**场景映射（必须精确匹配）：**
| 使用场景 | 占位图 | 填充方式 |
|---------|-------|---------|
| Card C1/C3 短图 · ImageBlock A1/A2/B1/B2 | `placeholder_landscape.svg` | `object-fit: cover` |
| Card C2/C4 长图 · ImageBlock A3/B3 | `placeholder_portrait.svg` | `object-fit: cover` |
| Card C5 九宫格 · ImageBlock A4/A5/B4/B5 | `placeholder_square.svg` | `object-fit: cover` |

### 状态栏专用
`battery.svg` · `network.svg` · `wifi.svg`（仅用于 StatusBar）

### 业务图标集：`icons/QUI_24_icons/`（437 个，全部 24×24）
覆盖聊天、社交、支付、设置、音视频、AI 等业务场景。**引用方式：`icons/QUI_24_icons/xxx.svg`**。
常见示例：`add.svg` · `QQ.svg` · `ai_chat.svg` · `activity.svg` · `address_list.svg` …（完整列表请 `ls icons/QUI_24_icons/`）。

**选用规则**：
1. 优先在顶层 33 个通用图标中找（覆盖 80% 基础场景）
2. 业务相关图标去 QUI_24_icons/ 查
3. 两处都没有 → 标注 `🔶 需求缺口`，**禁止自绘**

---

## 图标着色指南（5 个 icon-* Token）

| Token | 使用场景 | 搭配文字 Token |
|-------|---------|---------------|
| `icon-primary` | 主操作图标、输入激活态图标、标题旁图标 | `text-primary` |
| `icon-secondary` | 默认态图标、列表二级引导(L5/L6)、NavBar 描述组图标、辅助信息旁图标 | `text-secondary` |
| `icon-tertiary` | 列表右侧箭头(R1/R2/R3 chevron_right/expand_list)、次要指示 | `text-tertiary` |
| `icon-white` | 白色图标（如蓝底按钮上的白图标，通常不需单独设 color） | `text-white` |
| `icon-blue` | AIO 工具栏激活态、品牌色高亮图标 | `text-link` |

**SVG 着色机制（必须遵守）：**
```html
<!-- SVG 文件内：用 currentColor 代替具体颜色 -->
<svg><path fill="currentColor" d="…"/></svg>

<!-- CSS 中：设 color 实现 token 着色 -->
.icon-in-list { color: var(--icon-secondary); }
```

**例外（仅 Button 允许）：**
```css
/* 一级按钮（蓝底）内部深色图标 → 改白色 */
.btn-primary .icon { filter: brightness(0) invert(1); opacity: 0.9; }
/* 二级按钮（白底）内部图标 disabled → 40% 黑色 */
.btn-secondary.disabled .icon { filter: brightness(0); opacity: 0.4; }
```
> 其他场景使用 `filter` 染色 → ⛔ F17

---

## 组件注册表（22 个母组件，503 种变体）

> 📖 视觉参照：`component-matrix.html`
> 📖 规范细节：`md/{COMPONENT}_COMPONENT_SPEC.md`（23 份文档，与 skill 冲突时以 spec 为准）

### 导航（2 个）
| ID | 名称 | 变体数 | 结构 | 变体空间 |
|----|------|--------|------|---------|
| `navbar` | 导航栏 NavBar | 97 | 左(L)×中(C)×右(R) 三段式，高 44px | L1-L6 × C0-C5 × R0-R6，经约束过滤 |
| `hs_navbar` | 半屏导航栏 | 7 | 一级(A)/二级(B) | A1-A4 + B1-B3 |

### 数据（9 个）
| ID | 名称 | 变体数 | 容器宽度 | 变体空间 |
|----|------|--------|---------|---------|
| `list` | 通栏式列表 | 110 | 428px 通栏 | L0-L7 × C1-C3 × R0-R9，67 默认+43 多选 |
| `form` | 卡片式列表 | 52 | 396px 嵌入 | L1-L11 × R0-R5 |
| `text_block` | 文本块 | 13 | 自适应 | H1-H7(居左) + C1-C6(居中) |
| `image_block` | 图片块 | 10 | 428/396 | A1-A5(通栏) + B1-B5(嵌入) |
| `data_filter` | 数据筛选 | 16 | 428/396 | A1-A4 页签 + B1-B4 分段 + C1 下拉 + D1-D5 标签 + E1-E2 面包屑 |
| `grid` | 宫格 | 17 | 428/396 | A1-A9 平铺 + B1-B8 横滑 |
| `divider_spacing` | 分隔与间距 | 7 | — | A1(分割线) + spacing-xs/s/m/l/xl/xxl |
| `card` | 卡片 | 10 | 396px 嵌入 | C1-C10 |
| `message` | 消息 | 8 | 396px 气泡 | A-D × 主态/客态 |

### 操作（8 个）
| ID | 名称 | 变体数 | 变体空间 |
|----|------|--------|---------|
| `button` | 按钮 | 12 | S1-S4(大/中/小/mini) × T1-T3(一级/二级/警示) |
| `action` | 操作组合 | 15 | A1-A8(按钮型) + B1-B7(辅助操作行) |
| `menu` | 菜单 | 15 | I/NI/C × 2-6 项 |
| `search` | 搜索框 | 6 | A1-A3(一级) + B1-B3(二级) |
| `textfield` | 输入框 | 50 | A-D 基础 + E1-E6 复合（× 5 态） |
| `aio_input` | AIO 输入框 | 3 | I1(默认)/I2(生成中)/I3(输入) |
| `toast` | 轻提示 | 5 | T1(加载)/T2(成功)/T3(失败)/T4(文字)/T5(带操作) |

### 模态（3 个）
| ID | 名称 | 变体数 | 变体空间 |
|----|------|--------|---------|
| `action_sheet` | 操作面板 | 22 | `AS-{0-10}{T?}{D?}` |
| `dialog` | 对话框 | 15 | `{T\|NT}-{P\|C\|I}-{S\|D\|T}` |
| `half_screen_overlay` | 半屏浮层 | 2 | HSO-A(标准)/HSO-B(把手) |

### 运营（1 个）
| ID | 名称 | 变体数 | 变体空间 |
|----|------|--------|---------|
| `badge` | 红点 | 11 | B1-B4(强提醒) + W1-W4(弱提醒) + A1-A3(AIO 导航栏，仅 NavBar L2) |

---

## 第二步：Token 与样式检查（两级违规）

### Token 合法值速查

**布局间距** `--spacing-`: xs=4 s=8 m=12 l=16 xl=24 xxl=32 (px)
**圆角** `--radius-`: xs=4 s=8 m=12 l=16 xl=20 xxl=24 full=1000 (px)
**字号** (px): 10 · 12 · 14 · 16 · 17 · 18 · 20 · 22 · 26 · 28 · 34
**字重**: 400(Regular) · 500(Medium) · 600(Semibold) · 700(Bold)
**行高**: 1.2(紧凑) · 1.4(标准) · 1.5(舒适) · 1.65(阅读)
**阴影**: `var(--shadow-menu)`（唯一 Token）
**动效时长**: 150(快速反馈/按压) / 200(标准短/退场) / 250(标准/入场) / 300(慢退场) / 420(模态入场)
**缓动**: ease / ease-in / ease-out / ease-in-out / linear
**z-index**: 10(sticky) · 100(modal) · 9999(toast)

**颜色（39 个 Token）**:
品牌: `brand-standard` `brand-light` · 语义: `accent-green` `accent-orange` `accent-red`
文本: `text-primary` `-secondary` `-tertiary` `-quaternary` `-white` `-allwhite-secondary` `-allwhite-tertiary` `-link` `-link-dark`
图标: `icon-primary` `-secondary` `-tertiary` `-white` `-blue`
背景: `bg-bottom` `bg-secondary` `bg-top` `bg-bottom-brand` `bg-select` `fill-gray-primary`
填充: `fill-tertiary` `-secondary` `-primary` `-quaternary` `-destructive-strong` `-destructive-weak`
交互: `feedback-press` `feedback-hover` · 遮罩: `overlay-modal` `overlay-toast`
描边: `border-default` `border-weak` `border-invert` `border-white`

### 检查规则（两级违规）

| ID | 规则 | 两级判定 |
|----|------|---------|
| TK1 | 颜色必须用 `var(--token)` | ⛔ 硬编码且值不在 39 Token 中 → ERROR · ⚠️ 值匹配但未用 `var()` → WARN · **豁免**：Badge W1-W4 弱提醒底色 `#D9D9D9` 因 QUI 现有灰色 token 均为半透明、暂以硬编码实色过渡（详见 BADGE_COMPONENT_SPEC.md），待补充实色灰 token 后迁回 |
| **TK2a** | **布局间距**（user-added padding/margin/gap）必须 4-mult + Token | ⛔ 非 4 倍数 → ERROR · ⚠️ 是 4 倍数但硬编码 → WARN |
| **TK2b** | **组件固有尺寸**（spec 定义的固定值，如 ActionSheet 10px 主-取消 gap、Button S1 14px 圆角、HomeBar 34px）必须与 spec 精确匹配 | ⛔ 偏离 spec 值 → ERROR |
| TK3 | font-size 只允许 11 档合法值 | ⛔ 值不在 11 档中 → ERROR |
| TK4 | 间距 4/8/12/16/24/32px 应用 Token | ⚠️ 值正确但硬编码 → WARN |
| TK5 | 圆角 4/8/12/16/20/24/1000px 应用 Token | ⚠️ 值正确但硬编码 → WARN |
| TK6 | font-family 必须包含 "PingFang SC" | ⛔ 使用其他字体 → ERROR |
| TK7 | font-weight 只允许 400/500/600/700 | ⛔ 其他值 → ERROR |
| TK8 | line-height 只允许 1.2/1.4/1.5/1.65（或等价 px） | ⛔ 其他比例 → ERROR |
| TK9 | **box-shadow 仅允许 Menu 组件使用 `var(--shadow-menu)`**（含 Menu 渲染的 dropdown popup）；**其他所有组件禁止 box-shadow**（Dialog / AIO Input / DataFilter 分段选中态 / Card / NavBar / 头像 / 按钮等均无阴影） | ⛔ 非 Menu 组件出现 box-shadow → ERROR · ⛔ Menu 用硬编码而非 token → ERROR |
| **TK10** | 图标着色必须用 `var(--icon-*)`，且与同层文字色语义对齐 | ⛔ 硬编码图标色 / 语义错配 → ERROR · ⚠️ 值对但未用 var() → WARN |
| **TK11** | 文本溢出：单行必须 `text-overflow: ellipsis + white-space: nowrap`；多行用 `-webkit-line-clamp` | ⛔ 长文本无截断处理 → ERROR |
| **TK12** | 动效原子双层（精简版）：① 时长仅允许 150/200/250/300/420ms（5 档 · iOS）→ 必须用 `var(--duration-fast/base/medium/slow/modal)` 或硬编码 5 档之一；② 缓动仅 5 档 cubic-bezier（standard / out / in / emphasized / linear）→ 必须用 `var(--easing-*)` 或对应 cubic-bezier 值。组件级 `--anim-*` token 必须引用基础原子，禁止硬编码值。 | ⛔ 其他值（如 100ms / 500ms / 600ms / 自定义 cubic-bezier / decelerate / accelerate / sharp / spring 等已废弃 token）→ ERROR · ⚠️ 值正确但未用 `var()` → WARN |
| **TK13** | z-index 只能取 10/100/9999 三档 | ⛔ 其他值（如 999/5/1） → ERROR |
| **TK14** | `<img>` 默认 `object-fit: cover`；特殊场景可 `contain` | ⛔ `fill`/`none`/`scale-down` → ERROR |
| **TK15** | border-color 必须用 `var(--border-*)` 或 `var(--brand-standard)`；禁止 rgba 硬编码 | ⛔ `border: 1px solid rgba(0,0,0,.08)` → ERROR |
| **TK16** | 主题切换仅用 `[data-theme="qq-light|qq-dark"]`；禁止 `@media (prefers-color-scheme)` | ⛔ 媒体查询硬编码暗色 → ERROR |
| **TK17** | **图标 / 头像 / 插图 / 照片路径合规**：所有 `<img src="...">` 必须指向真实文件。合法前缀：① `icons/<name>.svg`（33 通用 + 3 placeholder + 头像/缩略图占位）；② `icons/QUI_24_icons/<name>.svg`（437 业务图标）；③ **`icons/QUI_Avatars/AvatarN.svg`（N=1..10，真实头像 · 任务交付必用）**；④ `icons/QUI_illustrations/illustrationN.png`（N=1..14，插图）；⑤ `icons/QUI_illustrations/landscape%20photosN.JPG`（N=1..10，风景照片 · 空格须 URL 编码为 %20）。**禁止**自造文件名 / 错误前缀（如 `/assets/`、`/img/`）/ Base64 / 外链 URL / 文件名大小写错误 | ⛔ 路径不存在或前缀不在白名单 → ERROR |

### 正反例对比

```
── 颜色 ──
⛔ ERROR:  color: #FF5733;                    ← 值不在 Token 中
⚠️ WARN:   color: rgba(0, 0, 0, 0.9);         ← 值 = text-primary 但没用 var()
✅ PASS:   color: var(--text-primary);

── 布局间距 ──
⛔ ERROR:  padding: 10px;                     ← TK2a 用户层间距非 4 倍数
✅ PASS:   padding: var(--spacing-m);         ← 用 Token

── 组件固有尺寸 ──
⛔ ERROR:  .action-sheet-gap { height: 8px; } ← TK2b 偏离 spec（应为 10px）
✅ PASS:   .action-sheet-gap { height: 10px; } ← 匹配 ActionSheet spec

── 图标着色 ──
⛔ ERROR:  <svg fill="#000"><path ... /></svg>    ← F16 硬编码
✅ PASS:   <svg fill="currentColor">...</svg>
           css: color: var(--icon-secondary)

── 文本截断 ──
⛔ ERROR:  .title { /* 无 ellipsis */ }       ← TK11 长文本溢出
✅ PASS:   .title { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

── 动效 ──
⛔ ERROR:  transition: all 500ms ease;        ← 500ms 不在 5 档中
✅ PASS:   transition: all 200ms ease-out;

── z-index ──
⛔ ERROR:  z-index: 999;                      ← 不在 3 档中
✅ PASS:   z-index: 100;                      ← modal 层

── border ──
⛔ ERROR:  border: 1px solid rgba(0,0,0,.08); ← TK15 硬编码
✅ PASS:   border: 1px solid var(--border-weak);

── 主题 ──
⛔ ERROR:  @media (prefers-color-scheme: dark) { ... }  ← TK16
✅ PASS:   [data-theme="qq-dark"] .card { ... }
```

---

## 第三步：页面结构与约束检查

### 基础结构规则

| ID | 规则 | 级别 |
|----|------|------|
| **S1** | **StatusBar 细则**：容器 428×54px · 时间固定 "9:41" · 必须使用 `icons/network.svg` + `icons/wifi.svg` + `icons/battery.svg`（满格，不可替换）· 字体 `SF Pro / -apple-system, 17px, 600` · 时间居中于左侧 152px 区域 | ⛔ |
| S2 | StatusBar 下方紧接 NavBar 44px | ⛔ |
| **S3** | **Home Bar 细则**：容器 428×34px 全局唯一位于页面底部 · 指示条 144×5px，圆角 2.5px，颜色 `var(--text-primary)` · 指示条水平居中、距底 8px | ⛔ |
| S4 | 全宽元素 width = 428px | ⛔ |
| S5 | 背景色：含 Card/Grouped List/Message/AIO → `var(--bg-secondary)`；其余 → `var(--bg-bottom)` | ⛔ |
| S6 | 相邻组件之间必须有间距或分割线 | ⛔ |
| S7 | 列表最后一行底部不显示分割线 | ⛔ |
| S8 | 模态组件不可嵌套（见嵌套矩阵） | ⛔ |
| S9 | 半屏浮层内只可嵌入非模态组件 | ⛔ |
| S10 | Hover: `--feedback-hover` 叠加，禁止改前景色 | ⛔ |
| **S11** | **Disabled**: `opacity ∈ [0.3, 0.4]` + `pointer-events: none`。具体值按 spec：**默认 0.3**；Grouped List 整行 **0.4**；Button 二级 disabled **0.4** | ⛔ |
| S12 | 嵌套容器内层圆角 ≤ 外层圆角 | ⛔ |
| S13 | 同一容器内字号层级递减：标题 ≥ 正文 ≥ 描述 ≥ 注释 | ⚠️ |
| **S14** | **页面级唯一组件**：StatusBar / NavBar / HomeBar / AIO Input 每页最多 1 个 | ⛔ |
| **S15** | **固定位置组件**：StatusBar 顶部 · NavBar sticky top:0 · HomeBar 页面底部 · Action Combo `position: fixed; bottom: 34px` · Toast 上半屏居中 · Dialog 垂直居中+overlay · ActionSheet 吸底+overlay | ⛔ |
| **S16** | **组件容量上限**：ActionSheet 主区 ≤10 项 · Menu 2-6 项 · Grid 平铺 ≤9 格 · NavBar C5 分段 2-4 段 · Card C10 内部组件 ≤5 个 | ⛔ |
| **S17** | **容器标准宽度**：通栏组件=**428px**（List/NavBar/StatusBar/HomeBar/ActionSheet outer/Action Combo）；卡片/嵌入=**396px**（Card/Form/HSO inner content/Message bubble/max-width inner） | ⛔ |
| **S18** | **吸顶组件不遮挡**：NavBar / HS_NavBar 必须 `position: sticky; top: 0; z-index: 10`。**内容滚动时必须从 NavBar 下方穿过**，不可被滚动内容覆盖 | ⛔ |
| **S19** | **吸底组件层级严格**：**Home Bar > 模态组件 > Action Combo / AIO Input > 页面内容**（z-index 分层：Home Bar 最高，始终最上层；滚动内容不得盖过吸底组件） | ⛔ |
| **S20** | **滚动容器位置**：页面滚动容器（如 `main-wrap`）不得覆盖 NavBar / Home Bar 的渲染区域。滚动内容必须被限制在吸顶与吸底之间的空间内 | ⛔ |
| **S21** | **吸附组件底色联动**：① StatusBar 底色 = 下方第一个吸顶组件底色：**通常为 NavBar**（默认 `var(--bg-bottom)`）；**例外 · 顶部为图片（沉浸场景）时保持 `transparent`**，由图片穿透显示，文字/图标改用 `--text-white` / `--icon-white`。② Home Bar 底色 = 上方第一个吸底组件底色（Action Combo / AIO Input），无吸底组件时跟随页面底色 | ⛔ |
| **S22** | **设备 viewport**：页面必须以 **428 × 926px**（iPhone 14 Pro Max 基准）为设备 mockup。非此尺寸的页面不符合 QUI Basic 1.0 输出规范 | ⛔ |
| **S23** | **双固定结构必备**：每个页面**必须**包含 StatusBar（顶部 54px）+ Home Bar（底部 34px）。独立组件变体预览页面可豁免（非 full-page 场景）| ⛔ |
| **S24** | **吸顶复合 3 层结构**：L1（必有）= NavBar；L2（可选）= DataFilter A 页签；L3（可选）= DataFilter D 标签 / E 面包屑（二选一）。合法组合 4 种：L1 / L1+L2 / L1+L3 / L1+L2+L3。**禁止参与吸顶**：Search A/B 全系、DataFilter B 分段选择、DataFilter C 下拉筛选、TextBlock、其他组件；禁止同层多组件并排。**分割线规则**（只有 NavBar / A 页签可提供底线）：① 含 L3（D/E 自身无底线）→ 整体无分割线；② 仅 L1+L2 → L2 页签底线 `var(--border-default)` 0.5px 作为整体底线，L1 NV2 禁用；③ 仅 L1 → L1 NV2 规则生效。**L4+ 压迫内容区 → ERROR** | ⛔ |
| **S25** | **吸底复合**：① Action Combo 多行型（A+B 辅助操作行）整体吸底 `bottom: 34px`，Home Bar 在其上层；② **Action Combo 与 AIO Input 互斥**（同页最多一个）；③ 滚动容器 `padding-bottom` ≥ 吸底复合高度 + 34px | ⛔ |
| **S26** | **层级序 & 互斥**：从高到低——**① StatusBar · Home Bar（最高，系统级）· ② Toast · 模态组件 · ③ 吸顶/吸底组件 · ④ 页面内容**。**互斥规则**：Toast 与模态组件互斥（同屏不可共存）· 模态组件之间互斥（F10）· 打开模态前必须关闭 Toast，反之亦然 | ⛔ |
| **S27** | **DataFilter 吸顶行为边界**：① DataFilter **A/D/E 作页面级次级导航紧跟 NavBar 时吸顶**；② DataFilter **B 分段选择 / C 下拉筛选 永不吸顶**；③ DataFilter 嵌入 Card / 列表行内 不吸顶；④ A 页签吸顶时底线保持 `var(--border-default)` 0.5px（作 S24 整体底线承担者） | ⛔ |
| **S28** | **StatusBar 沉浸滚动切实色**（F1-B）：① 初始（顶部为图片）→ `background: transparent` + 文字/图标 `--text-white`；② IntersectionObserver 监听图片底部 sentinel（触发 = 图片底部离开 StatusBar 底部）；③ 切换后 → 实色（匹配下方 NavBar 底色）+ 文字 `--text-primary` + 图标 `--icon-primary`；④ 过渡 `transition: background-color 200ms ease-out, color 200ms ease-out`；⑤ 反向回滚 → 同阈值反转（双向对称）；⑥ 吸顶组件内部横滚（面包屑 E2 渐隐）：sticky 容器固定，内部横滚独立 | ⛔ |
| **NV1** | **NavBar / HS_NavBar 底色约束**：底色必须从 `bg-*` 4 token 白名单选择，且"页面底色 ↔ NavBar 底色"组合必须在下方合法矩阵内。**全局禁止** `transparent` / `fill-*` / `backdrop-filter` 毛玻璃 / 硬编码 rgba / 品牌色 / 警示色 | ⛔ |
| **NV2** | **NavBar / HS_NavBar 滚动态分割线**：默认**无**分割线；当内容滚入 NavBar 下方覆盖区（scrollY > 0）时显示分割线，回滚到顶时消失。必须完全复用 divider A1 规范（**0.5px + `var(--border-weak)`**）并用 `::after` 伪元素 + `opacity` 切换实现。**禁止** `border-bottom` / 其他高度/颜色 / `box-shadow` 模拟 / 过渡非 `opacity`。**⚠️ 吸顶复合场景例外**：当 NavBar 与 DataFilter A 页签 / D 标签 / E 面包屑形成复合吸顶（S24）时，NV2 由下层组件承担或整体取消，NavBar 自身 NV2 **禁用** | ⛔ |
| **DV1** | **分割线规范**：① 独立使用的 `divider_spacing` A1 → **强绑 0.5px + `var(--border-weak)`**（水平高度 / 垂直宽度）；② 组件内部分割线 → 按各组件 spec 定义，允许 `--border-weak` 或 `--border-default`（以组件 spec 为准，不强行统一）；③ 全局禁止：硬编码 rgba / 非 0.5px 厚度 / `fill-*` / `accent-*` / `brand-*` 作分割线色 | ⛔ |

### NV1 · NavBar/HS_NavBar 底色拼接矩阵

**允许的 NavBar 底色（4 选 1）：**
| Token | 值（light/dark） | 适用 |
|-------|----------------|------|
| `var(--bg-bottom)` | #FFFFFF / #1A1C1E | **默认**。白色页面 或 分层式（灰页 + 白 chrome） |
| `var(--bg-secondary)` | #F0F0F2 / #1C1C1E | 含 Card/Grouped List/Message/AIO 的页面（一体式） |
| `var(--bg-bottom-brand)` | #EFF4FF / #0F1113 | 品牌氛围页（一体式） |
| `var(--bg-top)` | #FFFFFF / #2F3033 | 仅限 HSO/Dialog/Drawer 内嵌 HS_NavBar |

**合法拼接组合：**
| 页面底色 | NavBar 底色 | 模式 | 典型场景 |
|---------|------------|------|---------|
| `bg-bottom`（白） | `bg-bottom`（白） | 一体 | 文章详情、极简内容页 |
| `bg-secondary`（灰） | `bg-secondary`（灰） | 一体 | 含 Card/GroupedList 的标准页 |
| `bg-secondary`（灰） | `bg-bottom`（白） | **分层** | iOS 设置风：灰底 + 白 chrome |
| `bg-bottom-brand`（浅蓝） | `bg-bottom-brand`（浅蓝） | 一体 | 品牌氛围落地页 |
| `bg-bottom-brand`（浅蓝） | `bg-bottom`（白） | **分层** | 品牌页 + 白 chrome |
| HSO/Dialog/Drawer 内部 | `bg-top` | 一体 | 浮层内部 HS_NavBar |

**禁止组合：**
| 页面 | NavBar | 禁止理由 |
|------|-------|---------|
| `bg-bottom`（白） | `bg-secondary`（灰） | 视觉反转：chrome 不应比内容更暗 |
| `bg-bottom`（白） | `bg-bottom-brand` | 品牌色单独出现在 chrome 上抢焦点 |
| `bg-secondary` | `bg-bottom-brand` | 语义冲突（品牌页 vs 非品牌内容）|
| 任一页面 | `bg-top` | bg-top 严格限浮层内部 |
| 任一页面 | `bg-select` | AIO 专用 token |
| 任一页面 | `transparent` / 毛玻璃 / rgba 硬编码 | **全局禁止** |
| 任一页面 | `fill-*` / `brand-*` / `accent-*` / `fill-destructive-*` | 语义错用 |

> **重要变更**：v5.2 起**全局取消**沉浸场景透明 NavBar 例外。即使 NavBar 下方覆盖图片，也必须用 `bg-*` 实色（通过 chrome 与图片的清晰边界保证可读性）。

### NV2 · NavBar / HS_NavBar 滚动态分割线

**状态行为：**
| 滚动状态 | 分割线 |
|---------|-------|
| 默认态（scrollY = 0 / 内容在 NavBar 之下未触及）| **无**（`opacity: 0`）|
| 滚动遮挡态（内容进入 NavBar 下方覆盖区）| **显示** 0.5px `var(--border-weak)` |
| 回滚到顶 | 淡出消失（`opacity 200ms ease-out`）|

**必须对齐 divider A1（`divider_spacing` 组件）**：`height: 0.5px; background: var(--border-weak);`

**标准实现：**
```css
/* 伪元素承载分割线，避免 border-bottom 造成的 1px 布局跳动 */
.navbar-row::after, .hs-navbar-row::after {
  content: '';
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 0.5px;                       /* 对齐 divider A1 */
  background: var(--border-weak);      /* 对齐 divider A1 */
  opacity: 0;
  transition: opacity 200ms ease-out;  /* TK12 白名单 */
  pointer-events: none;
}
.navbar-row.scrolled::after,
.hs-navbar-row.scrolled::after { opacity: 1; }

.scroll-sentinel {
  position: absolute; top: 0; left: 0;
  height: 1px; width: 1px;
  pointer-events: none; visibility: hidden;
}
```

```html
<!-- sentinel 置于 NavBar 之前、scroll container 顶部 -->
<div class="scroll-sentinel" aria-hidden="true"></div>
<nav class="navbar-row">...</nav>
```

```js
/* NavBar（页面级，root = window）*/
new IntersectionObserver(([e]) => {
  navbar.classList.toggle('scrolled', !e.isIntersecting);
}).observe(sentinel);

/* HS_NavBar（浮层级，root = HSO 内容容器）*/
new IntersectionObserver(([e]) => {
  hsNavbar.classList.toggle('scrolled', !e.isIntersecting);
}, { root: hsoContentEl }).observe(hsSentinel);
```

**禁止行为：**
| 违规 | 原因 |
|------|------|
| `border-bottom: 1px solid ...` | ① 1px 违反 divider A1 的 0.5px；② border 占据高度，状态切换时元素跳动 1px |
| 分割线永久显示 | 违反 NV2 默认态"无分割线" |
| 分割线永久隐藏 | 滚动时内容与 chrome 视觉粘连 |
| `box-shadow` 模拟分割线 | 视觉不一致，与 iOS 标准不符 |
| 分割线颜色用 `--border-default` 或其他 token | 必须固定 `--border-weak`（对齐 divider A1） |
| 过渡属性用 `border-color` / `transform` / 其他 | 必须用 `opacity`（因为非 border 实现） |
| 过渡时长非 TK12 白名单 | 必须 150/200/250/300/420ms 之一（对应 `var(--duration-fast/base/medium/slow/modal)`）|

**静态陈列页例外：**
matrix 等静态展示页只加 CSS（保持默认态无分割线），**不必加 JS/sentinel**。只有真实可滚动的页面才初始化 IntersectionObserver。

### 嵌套允许矩阵（F3 配套）

| 容器 | ✅ 可嵌入 | ❌ 禁止嵌入 |
|------|---------|-----------|
| **Card C10** | text_block · image_block · action(A1-A8) · data_filter · grid | Card · list · form · message · 任何 modal |
| **Card C1-C9** | 预定义内容（已锁死），不可添加新子组件 | 任何 |
| **HalfScreenOverlay HSO-A/B** | list · form · text_block · image_block · action · grid · data_filter · search | Dialog · ActionSheet · HalfScreenOverlay（三大模态互斥） |
| **Dialog** | text_block(正文) · textfield E1（仅输入对话框）· action A1-A2（底部按钮行） | 任何其他组件 |
| **ActionSheet 主区** | action-item 行 × 1-10（按 AS-{n} 编码）| 任何复合组件 |
| **ActionSheet 取消区** | 固定 1 个 action-item 行（取消/确认） | 任何其他 |
| **Form (卡片式列表)** | L1-L11 × R0-R5 单行行项，**最多 2 级折叠** | 3 级嵌套 · Card · 任意 modal |
| **List (通栏列表)** | L0-L7 × C1-C3 × R0-R9 单行行项 | Card · form · 任意 modal |
| **NavBar** | 预定义 L/C/R 子组件（已锁死）+ Badge（仅 L2） | 任何其他组件 |
| **Message 气泡** | 预定义文本/图文内容（已锁死） | 任何其他组件 |

### 垂直节律速查（页面布局节拍）

| 场景 | 标准间距 | Token |
|------|---------|-------|
| Section 与 Section 之间（页面分区） | 24px | `--spacing-xl` |
| 组件内子项之间（List 行内、Card 行内） | 12–16px | `--spacing-m` / `-l` |
| 图标与文字之间 | 8–12px | `--spacing-s` / `-m` |
| 图标簇内部 / 行内小元素 | 4px | `--spacing-xs` |
| 页面左右安全区内边距 | 16px | `--spacing-l` |
| 列表容器上下内边距 | 8–16px | `--spacing-s` / `-l` |

### 标准内边距

| 场景 | padding |
|------|---------|
| 通栏列表行（List） | `0 16px`（左右 16，使内容 396 居中）|
| 卡片/嵌入容器外边距（Card/Form） | `margin: 0 16px`（428 − 32 = 396）|
| 页面画布主区 | `0 16px`（个别场景 `0 20px` / `0 24px`）|
| Action 容器内部 | `0 16px`（A1-A4）/ `16px` 全方向（A5/A8）|

---

## 第四步：合规评分

检查完成后，计算**合规评分**（满分 100）：

| 维度 | 权重 | 计算方式 |
|------|------|---------|
| **组件合法性** | **30%** | 含嵌套矩阵 · 唯一性 · 容量 · 宽度。有 1 个非法组件则此项 ≤60 |
| **图标合规** | **15%** | 含来源/清单/尺寸/**着色**/场景。有 1 个自绘/Emoji/着色失效则 ≤50 |
| **Token 绑定率** | **25%** | `(使用 var() 的属性数 / 应使用 Token 的属性总数) × 100` |
| **值准确率** | **20%** | 含字号/字重/行高/阴影/动效/z-index/object-fit/border |
| **结构合规** | **10%** | S1-S17 规则通过率 |

### 评级标准

| 评级 | 分数 | 含义 | 行动 |
|------|------|------|------|
| 🟢 **A** | 90-100 | 完全合规，可直接交付 | 无需修改 |
| 🟡 **B** | 75-89 | 基本合规，有少量 WARN | 建议修复 WARN 项 |
| 🟠 **C** | 60-74 | 部分合规，有 ERROR 需修复 | 必须修复所有 ERROR |
| 🔴 **D** | <60 | 严重不合规 | 需重新审视设计方案 |

> 跳过 Preflight 的检查上限 = C 级。

---

## 第五步：Skill Sync（持续优化）

每次 Lint 完成后，AI 应执行以下知识同步：

### 1. 错误模式积累
新的 AI 错误模式记入候选 FORBIDDEN：
```
📝 模式：AI 将 HalfScreenOverlay 的把手型(HSO-B)用作底部抽屉
→ 建议补充到 FORBIDDEN（下一个可用编号）
```

### 2. 需求缺口汇总
```
📝 组件演进：星级评分（3 次缺口）· 步骤条（2 次）
📝 图标演进：下载/上传（5 次）· 语音/麦克风（3 次）
```

### 3. Token 偏差趋势
```
📝 本次硬编码：颜色 5 处 · 间距 3 处 · 图标着色 2 处（svg fill="#000"）
```

---

## 脚本化自检提示（工程侧可选）

```bash
# F11 自绘 SVG
grep -rn '<svg' src/ | grep -v '<use\|viewBox=.*icons/\|icons/'

# F12 Emoji 当图标
grep -rnE '[✓✗✔✕→←↑↓⚠❤⭐🔍🗑📎]' src/

# F13 外部图标库
grep -rnE 'fontawesome|fa-[a-z]+|material-icons|mdi-|lucide|iconify|heroicon' src/

# F15 Base64/外链
grep -rnE 'data:image|https?://[^"'\'' ]+\.(svg|png|jpg|webp)' src/

# F16 SVG 硬编码颜色（应为 currentColor）
grep -rnE 'fill="#[0-9a-fA-F]{3,8}"|fill="rgb' src/ icons/

# 非法字号
grep -rnoE 'font-size:\s*[0-9]+px' src/ | grep -vE ':\s*(10|12|14|16|17|18|20|22|26|28|34)px'

# 非法 z-index
grep -rnE 'z-index:\s*[0-9]+' src/ | grep -vE ':\s*(10|100|9999)\b'

# 非法动效时长
grep -rnE 'transition:[^;]*[0-9]+m?s' src/ | grep -vE '\b(150|200|250|300|420)ms\b|\b0\.(15|2|25|3|42)s\b'

# 硬编码 border rgba
grep -rnE 'border[^:]*:\s*[^;]*rgba\(' src/

# 硬编码颜色
grep -rnE 'color:\s*#[0-9a-fA-F]{3,8}\b|background(-color)?:\s*#[0-9a-fA-F]{3,8}\b' src/

# 暗色 media query 违规
grep -rnE 'prefers-color-scheme' src/
```

> 这些命令不能替代 AI 的语义级 Lint，只用于过滤机械型违规。

---

## 输出格式

### 逐项报告（只输出有问题的项，通过的跳过）

```
⛔ F1 非法组件 · 代码中使用了"底部 TabBar"
  替代方案：使用 NavBar C5 分段选择 + 页面级视图切换

⛔ F3 跨组件嫁接 · Card 内部嵌套了另一个 Card
  → 改用 Card C10 + 内部放 text_block/image_block/action

⛔ F11 自绘图标 · <svg><path d="M6 9l6 6 6-6"/></svg>
  → 替换为 <img src="icons/chevron_down.svg">

⛔ F16 SVG 硬编码颜色 · icons/custom.svg 内 fill="#000"
  → 改为 fill="currentColor"，并在 CSS 中设 color: var(--icon-secondary)

⛔ TK2a ERROR · .section-gap { margin-top: 20px; }
  用户层布局间距非 4 倍数
  → 改为 var(--spacing-xl)（24px）

⛔ TK2b ERROR · .action-sheet-gap { height: 12px; }
  ActionSheet spec 定义主区-取消 gap = 10px，不可修改
  → 固定为 10px

⛔ TK10 图标着色语义错配 · 标题旁图标用了 icon-tertiary
  标题搭配应为 icon-primary
  → color: var(--icon-primary)

⛔ TK11 文本溢出 · .list-title 长文本无截断
  → overflow: hidden; text-overflow: ellipsis; white-space: nowrap;

⛔ TK12 非法动效时长 · transition: all 500ms
  → 改为 200ms / ease-out

⛔ TK13 非法 z-index · z-index: 50
  → 改为 10（sticky）/ 100（modal）/ 9999（toast）

⛔ TK15 border 硬编码 rgba · border: 1px solid rgba(0,0,0,.08)
  → border: 1px solid var(--border-weak)

⛔ S11 Disabled · .grouped-row.disabled { opacity: 0.5 }
  Grouped List 整行禁用 spec = 0.4
  → opacity: 0.4

⛔ S14 页面级唯一 · 一个页面出现了 2 个 NavBar
  → 删除额外 NavBar，保留页面顶部 1 个

⛔ S16 容量超限 · ActionSheet 列出了 12 个选项
  上限 10，超出部分合并 / 使用 HSO + List 替代

⛔ S17 非标宽度 · .card { width: 380px }
  Card 容器标准宽度 = 396px
  → width: 396px

🔶 需求缺口 · 产品需要"星级评分"组件，QUI Basic 1.0 无法覆盖
  建议：向设计师反馈，申请新增评分组件
```

### 评分汇总

```
QUI Design Lint Report
═══════════════════════
设备框架 ···· 4/4 通过（S22/S23/S1/S3/S21 + 吸顶吸底层级）
├─ ✓/✗ 设备 viewport 428×926
├─ ✓/✗ StatusBar 428×54，9:41，3 图标满格（network/wifi/battery）
├─ ✓/✗ Home Bar 428×34，指示条 144×5 居中距底 8px
├─ ✓/✗ 底色联动：StatusBar = NavBar；Home Bar = 相邻吸底组件
└─ ✓/✗ 吸顶/吸底层级（S18-S20：sticky 不被遮挡、z-index 分层）
─────────────────────
组件合法性 ·· 82/100  (含嵌套/唯一性/容量/宽度)
图标合规 ···· 55/100  (1 处着色失效 + 2 处 SVG 硬编码 fill + 图标路径)
Token 绑定 ·· 72/100  (18/25 使用 var())
值准确率 ···· 85/100  (字号/动效/z-index 各 1 处违规)
结构合规 ···· 92/100  (1 处嵌套违规)
─────────────────────
总分 ········ 77/100  🟡 B 级

├─ ⛔ ERROR: 6 (1 非法 + 2 图标 + 1 动效 + 1 z-index + 1 宽度)
├─ ⚠️ WARN:  7 (值正确但未绑定 Token)
├─ 🔶 缺口:  1
└─ Skill Sync: 1 条新错误模式 + 1 条演进建议
```

> **设备框架优先**：若设备 mockup / StatusBar / Home Bar / 层级任一项 ✗，**总分直接判定 ≤60（🟠 C 级或以下）**，需优先修复。

---

*v6.10 · QUI Basic 1.0 · 22 母组件 529 变体（5 大类：导航 / 数据 / 操作 / 模态 / 运营）· 33 通用图标 + 437 业务图标 + 10 真实头像 + 14 插图 + 10 风景照片 · 视觉参照 component-matrix.html · 规范 md/*
*检查哲学：即使值碰巧正确，未绑定 Token 也是违规；即使图形相似，自绘图标也是违规；即使 spec 和 skill 冲突，以 spec 为准*
