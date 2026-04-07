# 组件索引速查（basic1.0 — Knot 知识库版）

> 所有组件规范和结构数据均通过 Knot 知识库 MCP `knowledgebase_search` 检索获取。
> knowledge_uuid: `7eafcbe5fe1b44cf8cf17a3ee195a30c`
> data_type: `git` | search_domain: `QQdesign_Foundation@DesignSystem-basic`

## 母组件列表（20）

| 组件 | SPEC 文件 | JSON 文件 | Knot 检索 keyword |
|------|-----------|-----------|-------------------|
| `navbar` | `NAVBAR_COMPONENT_SPEC.md` | `navbar.json` | `NAVBAR_COMPONENT_SPEC;navbar` |
| `hs_navbar` | `HS_NAVBAR_COMPONENT_SPEC.md` | `hs-navbar.json` | `HS_NAVBAR_COMPONENT_SPEC;hs-navbar` |
| `list` | `LIST_COMPONENT_SPEC.md` | `plain-list.json` | `LIST_COMPONENT_SPEC;list` |
| `form` | `GROUPED_LIST_COMPONENT_SPEC.md` | `grouped-list.json` | `GROUPED_LIST_COMPONENT_SPEC;grouped-list` |
| `card` | `CARD_COMPONENT_SPEC.md` | `card.json` | `CARD_COMPONENT_SPEC;card` |
| `message` | `MESSAGE_COMPONENT_SPEC.md` | `message.json` | `MESSAGE_COMPONENT_SPEC;message` |
| `text_block` | `TEXT_BLOCK_COMPONENT_SPEC.md` | `text-block.json` | `TEXT_BLOCK_COMPONENT_SPEC;text-block` |
| `image_block` | `IMAGE_BLOCK_COMPONENT_SPEC.md` | `image-block.json` | `IMAGE_BLOCK_COMPONENT_SPEC;image-block` |
| `data_filter` | `DATA_FILTER_COMPONENT_SPEC.md` | `data-filter.json` | `DATA_FILTER_COMPONENT_SPEC;data-filter` |
| `grid` | `GRID_COMPONENT_SPEC.md` | `grid.json` | `GRID_COMPONENT_SPEC;grid` |
| `divider_spacing` | `DIVIDER_SPACING_COMPONENT_SPEC.md` | `divider-spacing.json` | `DIVIDER_SPACING_COMPONENT_SPEC;divider-spacing` |
| `button` | `BUTTON_COMPONENT_SPEC.md` | `button.json` | `BUTTON_COMPONENT_SPEC;button` |
| `action` | `ACTION_COMPONENT_SPEC.md` | `action-combo.json` | `ACTION_COMPONENT_SPEC;action` |
| `menu` | `MENU_COMPONENT_SPEC.md` | `menu.json` | `MENU_COMPONENT_SPEC;menu` |
| `search` | `SEARCH_COMPONENT_SPEC.md` | `search.json` | `SEARCH_COMPONENT_SPEC;search` |
| `textfield` | `TEXTFIELD_COMPONENT_SPEC.md` | `textfield.json` | `TEXTFIELD_COMPONENT_SPEC;textfield` |
| `aio_input` | `AIO_INPUT_COMPONENT_SPEC.md` | `ai-input.json` | `AIO_INPUT_COMPONENT_SPEC;aio-input` |
| `action_sheet` | `ACTION_SHEET_COMPONENT_SPEC.md` | `action-sheet.json` | `ACTION_SHEET_COMPONENT_SPEC;action-sheet` |
| `dialog` | `DIALOG_COMPONENT_SPEC.md` | `dialog.json` | `DIALOG_COMPONENT_SPEC;dialog` |
| `half_screen_overlay` | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` | `half-screen-overlay.json` | `HALF_SCREEN_OVERLAY_COMPONENT_SPEC;half-screen-overlay` |

## 常用资源检索关键词

| 资源 | keyword | query 示例 |
|------|---------|------------|
| 入口指南 | `README;设计系统` | "QQ_GenUI 设计系统全局结构" |
| 颜色 Token | `QQ_color_tokens.css;颜色;token` | "QQ 颜色 Token 定义" |
| 通用 Token | `tokens.css;间距;字号;圆角` | "通用 Token 间距字号" |
| 图标库 | `QUI_24_icons;icon;svg` | "图标 <用途描述>" |
| 状态栏图标 | `network.svg;wifi.svg;battery.svg` | "状态栏图标 网络 WiFi 电池" |

## 关键全局约束

- Knot MCP 必须在 Gate -1 完成安装与 Token 配置后才能开始检索
- 首次使用时若项目根目录不存在 `failure-log.md`，先创建；后续每次执行前读取项目根目录 `failure-log.md`，优先规避历史高频错误；每次失败或重试后立即写入
- 间距使用 4px 网格（4 的整数倍）
- 颜色值必须来自 `css/QQ_color_tokens.css`
- 包含 `card` 或 `form`（Grouped List）时页面背景强制灰底 `#F0F0F2`
- 页面顶部必须包含 StatusBar，且背景与 NavBar 一致
- `empty_icon.svg` 必须替换为 `icons/QUI_24_icons/` 中真实图标，通过 Knot 检索后下载到本地 `assets/icons/`，HTML 使用本地路径引用
