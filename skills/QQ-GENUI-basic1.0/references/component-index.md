# 组件索引速查（basic1.0 — Knot 知识库版）

> 所有组件规范和结构数据均通过 Knot 知识库 MCP `knowledgebase_search` 检索获取。
> knowledge_uuid: `7eafcbe5fe1b44cf8cf17a3ee195a30c`
> data_type: `git` | search_domain: `QQdesign_Foundation@DesignSystem-basic`

## 母组件列表（22）

按 **导航 → 数据 → 操作 → 模态 → 运营** 五大类排序：

| 大类 | 组件 | SPEC 文件 | JSON 文件 | Knot 检索 keyword |
|------|------|-----------|-----------|-------------------|
| 导航 | `navbar` | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` | `NAVBAR_COMPONENT_SPEC;navbar` |
| 导航 | `hs_navbar` | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` | `HS_NAVBAR_COMPONENT_SPEC;hs-navbar` |
| 数据 | `list` | `LIST_COMPONENT_SPEC.md` | `plain-list.json` | `LIST_COMPONENT_SPEC;list` |
| 数据 | `form` | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` | `GROUPED_LIST_COMPONENT_SPEC;grouped-list` |
| 数据 | `card` | `CARD_COMPONENT_SPEC.md` | `card.json` | `CARD_COMPONENT_SPEC;card` |
| 数据 | `message` | `MESSAGE_COMPONENT_SPEC.md` | `message.json` | `MESSAGE_COMPONENT_SPEC;message` |
| 数据 | `text_block` | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` | `TEXT_BLOCK_COMPONENT_SPEC;text-block` |
| 数据 | `image_block` | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` | `IMAGE_BLOCK_COMPONENT_SPEC;image-block` |
| 数据 | `data_filter` | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` | `DATA_FILTER_COMPONENT_SPEC;data-filter` |
| 数据 | `grid` | `GRID_COMPONENT_SPEC.md` | `grid.json` | `GRID_COMPONENT_SPEC;grid` |
| 数据 | `divider_spacing` | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` | `DIVIDER_SPACING_COMPONENT_SPEC;divider-spacing` |
| 操作 | `button` | `BUTTON_COMPONENT_SPEC.md` | `button.json` | `BUTTON_COMPONENT_SPEC;button` |
| 操作 | `action` | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` | `ACTION_COMPONENT_SPEC;action` |
| 操作 | `menu` | `MENU_COMPONENT_SPEC.md` | `menu.json` | `MENU_COMPONENT_SPEC;menu` |
| 操作 | `search` | `SEARCH_COMPONENT_SPEC.md` | `search.json` | `SEARCH_COMPONENT_SPEC;search` |
| 操作 | `textfield` | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` | `TEXTFIELD_COMPONENT_SPEC;textfield` |
| 操作 | `aio_input` | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` | `AIO_INPUT_COMPONENT_SPEC;aio-input` |
| 操作 | `toast` | `TOAST_COMPONENT_SPEC.md` | `toast.json` | `TOAST_COMPONENT_SPEC;toast` |
| 模态 | `action_sheet` | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` | `ACTION_SHEET_COMPONENT_SPEC;action-sheet` |
| 模态 | `dialog` | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` | `DIALOG_COMPONENT_SPEC;dialog` |
| 模态 | `half_screen_overlay` | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC;half-screen-overlay` |
| 运营 | `badge` | `BADGE_COMPONENT_SPEC.md` | `badge.json` | `BADGE_COMPONENT_SPEC;badge;红点` |

> **变体汇总 529 种**：NavBar 97 + HS NavBar 7 + Plain List 110 + Grouped List 52 + Card 10 + Message 4×2 + TextBlock 13 + ImageBlock 10 + DataFilter 16 + Grid 17 + Divider&Spacing 7 + Button 12 + ActionCombo 15 + Menu 15 + Search 12 + Textfield 50 + AIOInput 3 + Toast 5 + ActionSheet 42 + Dialog 15 + HSO 2 + Badge 11

## 常用资源检索关键词

| 资源 | keyword | query 示例 |
|------|---------|------------|
| 入口指南 | `README;设计系统` | "QQ_GenUI 设计系统全局结构" |
| **合规 Lint 规则**（Gate 9 权威依据）| `QUI_DESIGN_LINT_SKILL;lint;合规;Preflight;F1;TK1;S1` | "QUI Design Lint 两级违规制 F1-F20 TK1-TK17 S1-S28" |
| 颜色 Token | `Qdesign Color Tokens.css;颜色;token;QBasicToken` | "Qdesign 颜色 Token 定义" |
| 通用 Token | `Qdesign Tokens.css;间距;字号;圆角` | "Qdesign 通用 Token 间距字号" |
| Token 映射表 | `Qdesign-tokens映射表;token映射;旧名;新名` | "Figma 旧 token 名到 CSS 标准名映射" |
| 布局间距规范 | `DIVIDER_SPACING_COMPONENT_SPEC;divider-spacing;间距;布局` | "组件间距选择规则 6 档间距" |
| 半屏浮层模版库 | `HALF_SCREEN_OVERLAY_TEMPLATES;模版;半屏浮层` | "半屏浮层 T-01~T-06 场景模版匹配" |
| 图标库（通用）| — | 从 GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/QUI_24_icons/` 下载 |
| 状态栏图标 | — | 从 GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/` 下载 network.svg / wifi.svg / battery.svg |
| **真实头像**（F19 硬约束）| — | 从 GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/QUI_Avatars/` 下载 `Avatar1.svg`~`Avatar10.svg` |
| **插图/照片**（F20 硬约束）| — | 从 GitHub 仓库 `https://raw.githubusercontent.com/qkj91927/QQ_GenUI/main/icons/QUI_illustrations/` 下载 `illustration1.png`~`illustration14.png` 或 `landscape photos1.JPG`~`landscape photos10.JPG`（URL 编码 `%20`）|

## 关键全局约束

- Knot MCP 必须在 Gate -1 完成安装与 Token 配置后才能开始检索
- 首次使用时若项目根目录不存在 `failure-log.md`，先创建；后续每次执行前读取项目根目录 `failure-log.md`，优先规避历史高频错误；每次失败或重试后立即写入
- 间距使用 4px 网格（4 的整数倍），组件间间距遵循 `DIVIDER_SPACING_COMPONENT_SPEC.md` 6 档规则（4/8/12/16/24/32px）
- 颜色值必须来自 `css/Qdesign Color Tokens.css`，命名为连字符分隔（如 `--bg-secondary`、`--text-primary`）
- **旧命名废弃**：`--color-xxx` / `--qq-xxx` / 下划线命名（如 `--brand_standard`）均已废弃，遇到旧命名时查阅 `Qdesign-tokens映射表.csv`
- **背景色强约束（S5）**：页面包含 `Card / Grouped List / Message / AIO` 任一时，页面背景强制 `--bg-secondary`（`#F0F0F2`）；否则默认 `--bg-bottom`（`#FFFFFF`）
- 页面顶部必须包含 StatusBar（428×54），且背景与 NavBar 一致（lint S21）；页面底部系统 Home Bar 为全局唯一
- **资源本地化三项硬约束**：
  - 图标占位 `empty_icon.svg` 必须替换为 GitHub `icons/QUI_24_icons/` 或 `icons/` 中的真实图标（F11-F15）
  - 头像占位 `Avatar_32/40/52.svg` 必须替换为 `QUI_Avatars/AvatarN.svg`（**F19**）
  - 图片占位 `placeholder_landscape/portrait/square.svg` 必须替换为 `QUI_illustrations/` 真实素材（**F20**）
  - 所有资源下载到 `assets/icons/`（含 `QUI_Avatars/` 和 `QUI_illustrations/` 子目录），HTML 使用本地相对路径引用
- **禁止自绘图标 / Emoji / 外部图标库**（F11 / F12 / F13）
- **禁止模态组件互相嵌套**（F10：Dialog / ActionSheet / HSO）
- **禁止界面级滚动条**（界面尺寸须在 428×926 以内）
- **Gate 9 回归依据**：一律以 `QUI_DESIGN_LINT_SKILL.md`（F1-F20 / TK1-TK17 / S1-S28 / NV1-NV2 / DV1）为准，循环至零 ⛔ ERROR / 零 ⚠️ WARN
