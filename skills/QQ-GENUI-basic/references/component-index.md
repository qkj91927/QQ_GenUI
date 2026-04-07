# 组件索引速查（basic-v1.0）

## 母组件列表（20）

- `navbar` → `md/NAVBAR_COMPONENT_SPEC.md` + `json/components/navbar.json`
- `hs_navbar` → `md/HS_NAVBAR_COMPONENT_SPEC.md` + `json/components/hs-navbar.json`
- `list` → `md/LIST_COMPONENT_SPEC.md` + `json/components/plain-list.json`
- `form` → `md/GROUPED_LIST_COMPONENT_SPEC.md` + `json/components/grouped-list.json`
- `card` → `md/CARD_COMPONENT_SPEC.md` + `json/components/card.json`
- `message` → `md/MESSAGE_COMPONENT_SPEC.md` + `json/components/message.json`
- `text_block` → `md/TEXT_BLOCK_COMPONENT_SPEC.md` + `json/components/text-block.json`
- `image_block` → `md/IMAGE_BLOCK_COMPONENT_SPEC.md` + `json/components/image-block.json`
- `data_filter` → `md/DATA_FILTER_COMPONENT_SPEC.md` + `json/components/data-filter.json`
- `grid` → `md/GRID_COMPONENT_SPEC.md` + `json/components/grid.json`
- `divider_spacing` → `md/DIVIDER_SPACING_COMPONENT_SPEC.md` + `json/components/divider-spacing.json`
- `button` → `md/BUTTON_COMPONENT_SPEC.md` + `json/components/button.json`
- `action` → `md/ACTION_COMPONENT_SPEC.md` + `json/components/action-combo.json`
- `menu` → `md/MENU_COMPONENT_SPEC.md` + `json/components/menu.json`
- `search` → `md/SEARCH_COMPONENT_SPEC.md` + `json/components/search.json`
- `textfield` → `md/TEXTFIELD_COMPONENT_SPEC.md` + `json/components/textfield.json`
- `aio_input` → `md/AIO_INPUT_COMPONENT_SPEC.md` + `json/components/ai-input.json`
- `action_sheet` → `md/ACTION_SHEET_COMPONENT_SPEC.md` + `json/components/action-sheet.json`
- `dialog` → `md/DIALOG_COMPONENT_SPEC.md` + `json/components/dialog.json`
- `half_screen_overlay` → `md/HALF_SCREEN_OVERLAY_COMPONENT_SPEC.md` + `json/components/half-screen-overlay.json`

## 关键全局约束

- 首次使用时若项目根目录不存在 `failure-log.md`，先创建；后续每次执行前读取项目根目录 `failure-log.md`，优先规避历史高频错误；每次失败或重试后立即写入
- 间距使用 4px 网格（4 的整数倍）
- 颜色值必须来自 `css/QQ_color_tokens.css`
- 包含 `card` 或 `form`（Grouped List）时页面背景强制灰底 `#F0F0F2`
- 页面顶部必须包含 StatusBar，且背景与 NavBar 一致
- `empty_icon.svg` 必须替换为 `icons/QUI_24_icons/` 中真实图标，并下载到本地 `assets/icons/`，HTML 使用本地路径引用
