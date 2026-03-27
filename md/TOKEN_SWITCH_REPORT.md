# Token 切换对比分析报告

- 目标 Token 系统：`Material.tokens`
- 生成时间：`2026-03-27 15:59:29`

## 一、切换摘要

- 映射总数：**26**
- 实际变化：**26**
- 变化覆盖率：**100.0%**
- CSS 总变量：**233**
- CSS 已替换：**219**
- CSS 无对应跳过：**14**
- CSS 替换命中率（可替换项）：**100.0%**

## 二、CSS 文件覆盖

- `/Users/qiukaijie/Downloads/plus-v1.0/css/QQ_color_tokens.css`：替换 **146** / 可替换 **146** / 总变量 **151** ✅
- `/Users/qiukaijie/Downloads/plus-v1.0/css/tokens.css`：替换 **73** / 可替换 **73** / 总变量 **82** ✅

## 三、关键变化（index 映射）

- `tokens.color.bg_bottom_brand`: `#EFF4FF` → `rgba(103, 80, 164, 0.200)`
- `tokens.color.bg_bottom_light`: `#FFFFFF` → `#fef7ff`
- `tokens.color.bg_bottom_standard`: `#F0F0F2` → `#f3edf7`
- `tokens.color.bg_item`: `#FFFFFF` → `#fef7ff`
- `tokens.color.bg_page`: `#F0F0F2` → `#f3edf7`
- `tokens.color.bg_secondary`: `#F3F3F7` → `#f3edf7`
- `tokens.color.border_standard`: `rgba(0, 0, 0, 0.10)` → `#cac4d0`
- `tokens.color.brand_pressed`: `#008AE5` → `#6750a4`
- `tokens.color.brand_standard`: `#0099FF` → `#6750a4`
- `tokens.color.btn_bg`: `rgba(116, 116, 128, 0.08)` → `rgba(79, 55, 138, 0.080)`
- `tokens.color.feedback_error`: `#F74C30` → `#b3261e`
- `tokens.color.fill_pressed`: `rgba(0, 0, 0, 0.04)` → `rgba(103, 80, 164, 0.100)`
- `tokens.color.fill_standard_brand`: `rgba(13, 16, 49, 0.04)` → `rgba(79, 55, 138, 0.160)`
- `tokens.color.fill_standard_primary`: `rgba(13, 16, 49, 0.04)` → `rgba(79, 55, 138, 0.080)`
- `tokens.color.fill_tertiary`: `rgba(118, 118, 128, 0.12)` → `rgba(79, 55, 138, 0.100)`
- `tokens.color.icon_primary`: `#1A1A1A` → `#1d1b20`
- `tokens.color.icon_secondary`: `#929296` → `#49454f`
- `tokens.color.overlay_dark`: `rgba(0, 0, 0, 0.50)` → `rgba(103, 80, 164, 0.100)`
- `tokens.color.overlay_dialog`: `rgba(0, 0, 0, 0.40)` → `rgba(103, 80, 164, 0.100)`
- `tokens.color.separator`: `rgba(0, 0, 0, 0.08)` → `#cac4d0`
- `tokens.color.text_allwhite`: `#FFFFFF` → `#ffffff`
- `tokens.color.text_link`: `#214CA5` → `#6750a4`
- `tokens.color.text_primary`: `rgba(0, 0, 0, 0.90)` → `#1d1b20`
- `tokens.color.text_quaternary`: `rgba(60, 60, 67, 0.26)` → `#cac4d0`
- `tokens.color.text_secondary`: `rgba(60, 60, 67, 0.76)` → `#49454f`
- `tokens.color.text_tertiary`: `rgba(60, 60, 67, 0.56)` → `#79747e`

## 四、自动校验结果

- JSON 结构校验：✅ 通过
- CSS 替换执行校验：失败 **0** 项 ✅
- 替换失败项：无
- 无对应跳过项（目标系统缺少对应 token）：
  - `QQ_color_tokens.css:--qq-progressbar-dot`
  - `QQ_color_tokens.css:--qq-progressbar-played`
  - `QQ_color_tokens.css:--qq-progressbar-rate`
  - `QQ_color_tokens.css:--qq-system-color-black`
  - `QQ_color_tokens.css:--qq-system-color-white`
  - `tokens.css:--anim-menu-in-transform`
  - `tokens.css:--anim-menu-out-transform`
  - `tokens.css:--device-home-bar-height`
  - `tokens.css:--device-home-bar-indicator-height`
  - `tokens.css:--device-home-bar-indicator-radius`
  - `tokens.css:--device-home-bar-indicator-width`
  - `tokens.css:--device-screen-height`
  - `tokens.css:--device-status-bar-height`
  - `tokens.css:--device-width`

## 五、多维度结论

- **语义一致性**：优先显式映射，非颜色变量按存在性匹配（有对应则替换，无对应则保留原值）。
- **视觉风格变化**：覆盖 `--color-*`、`--qq-*` 与 `tokens.css` 中可映射变量。
- **工程影响范围**：更新 `json/index.json` 与 `css/*.css`。
- **风险评估**：已输出替换失败项与无对应跳过项，便于后续补充映射。
