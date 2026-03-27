#!/usr/bin/env python3
"""
Token system switcher for plus-v1.0 and basic-v1.0.

Capabilities:
- List available token systems from othertokens/
- Apply selected token system to json/index.json and css/*.css
- Replace color vars (--color-* / --qq-*) and tokens.css vars with "exists-then-switch" strategy
- Validate results after switching
- Generate multi-dimensional comparison report
"""

from __future__ import annotations

import argparse
import json
import re
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

TOKEN_FILE_PATTERN = "*.tokens.json"

# index 颜色层级映射
INDEX_COLOR_MAPPING: Dict[str, str] = {
    "tokens.color.text_primary": "Color.文本色.text_primary",
    "tokens.color.text_secondary": "Color.文本色.text_secondary",
    "tokens.color.text_tertiary": "Color.文本色.text_tertiary",
    "tokens.color.text_quaternary": "Color.文本色.text_quaternary",
    "tokens.color.text_link": "Color.文本色.text_link",
    "tokens.color.text_allwhite": "Color.文本色.text_allwhite",
    "tokens.color.brand_standard": "Color.品牌色.brand_standard",
    "tokens.color.brand_pressed": "Color.品牌色.brand_standard",
    "tokens.color.feedback_error": "Color.反馈色.feedback_error",
    "tokens.color.separator": "Color.分割色.Separators",
    "tokens.color.border_standard": "Color.分割色.Separators",
    "tokens.color.bg_page": "Color.分组背景色.Primary",
    "tokens.color.bg_item": "Color.背景色.Primary",
    "tokens.color.bg_secondary": "Color.背景色.Secondary",
    "tokens.color.overlay_dark": "Color.叠加色.active",
    "tokens.color.overlay_dialog": "Color.叠加色.active",
    "tokens.color.btn_bg": "Color.透明填充色.Quaternary",
    "tokens.color.fill_tertiary": "Color.透明填充色.Tertiary",
    "tokens.color.fill_standard_primary": "Color.透明填充色.Quaternary",
    "tokens.color.fill_pressed": "Color.叠加色.active",
    "tokens.color.fill_standard_brand": "Color.透明填充色.Secondary",
    "tokens.color.icon_secondary": "Color.图标色.icon_secondary",
    "tokens.color.icon_primary": "Color.图标色.icon_primary",
    "tokens.color.bg_bottom_light": "Color.背景色.Primary",
    "tokens.color.bg_bottom_standard": "Color.分组背景色.Primary",
    "tokens.color.bg_bottom_brand": "Color.品牌色.brand_light",
}

# 核心 CSS 变量 -> index key
CSS_VAR_TO_INDEX_KEY: Dict[str, str] = {
    "--color-brand-standard": "brand_standard",
    "--color-brand-pressed": "brand_pressed",
    "--color-text-primary": "text_primary",
    "--color-text-secondary": "text_secondary",
    "--color-text-tertiary": "text_tertiary",
    "--color-text-quaternary": "text_quaternary",
    "--color-text-link": "text_link",
    "--color-text-allwhite": "text_allwhite",
    "--color-icon-primary": "icon_primary",
    "--color-icon-secondary": "icon_secondary",
    "--color-feedback-error": "feedback_error",
    "--color-border-standard": "border_standard",
    "--color-separator": "separator",
    "--color-overlay-dark": "overlay_dark",
    "--color-fill-pressed": "fill_pressed",
    "--color-bg-item": "bg_item",
    "--color-fill-standard-primary": "fill_standard_primary",
    "--color-fill-standard-brand": "fill_standard_brand",
    "--color-bg-bottom-light": "bg_bottom_light",
    "--color-bg-page": "bg_page",
    "--color-bg-bottom-brand": "bg_bottom_brand",
    "--color-bg-secondary": "bg_secondary",
    "--color-bg-bottom-standard": "bg_bottom_standard",
    "--color-overlay-dialog": "overlay_dialog",
    "--color-btn-bg": "btn_bg",
    "--color-fill-tertiary": "fill_tertiary",
}

# 额外显式映射：覆盖常见 qq/color 变量
EXTRA_CSS_VAR_TO_TARGET_PATH: Dict[str, str] = {
    "--color-brand-light": "Color.品牌色.brand_light",
    "--qq-on-brand-primary": "Color.品牌色.on_brand_primary",
    "--color-feedback-success": "Color.反馈色.feedback_success",
    "--qq-feedback-warning": "Color.反馈色.feedback_warning",
    "--qq-feedback-normal": "Color.反馈色.feedback_standard",
    "--color-overlay-toast": "Color.叠加色.active",
    "--color-handle": "Color.分割色.Separators",
    "--color-switch-off": "Color.分割色.Separators",
    "--color-fill-pressed-brand": "Color.透明填充色.Primary",
    "--color-border-stroke": "Color.分割色.Separators",
    "--color-border-disabled": "Color.分割色.Separators",
}

# tokens.css 非颜色变量映射（有对应才替换）
NON_COLOR_CSS_VAR_TO_TARGET_PATHS: Dict[str, List[str]] = {
    "--device-platform": ["$extensions.com.figma.modeName"],
    "--device-font": ["Typography.字体.正文字体"],
    "--font-family": ["Typography.字体.正文字体"],

    "--typo-large-title-size": ["Typography.字号.large_title"],
    "--typo-large-title-weight": ["Typography.字重.粗"],
    "--typo-large-title-lh": ["Typography.行高.large_title"],
    "--typo-title1-size": ["Typography.字号.title_2"],
    "--typo-title1-weight": ["Typography.字重.中"],
    "--typo-title1-lh": ["Typography.行高.title_2"],
    "--typo-title2-size": ["Typography.字号.title_3"],
    "--typo-title2-weight": ["Typography.字重.中"],
    "--typo-title2-lh": ["Typography.行高.title_3"],
    "--typo-headline-size": ["Typography.字号.body"],
    "--typo-headline-weight": ["Typography.字重.粗"],
    "--typo-headline-lh": ["Typography.行高.body"],
    "--typo-body-size": ["Typography.字号.body"],
    "--typo-body-weight": ["Typography.字重.常规"],
    "--typo-body-lh": ["Typography.行高.body"],
    "--typo-callout-size": ["Typography.字号.description"],
    "--typo-callout-weight": ["Typography.字重.常规"],
    "--typo-callout-lh": ["Typography.行高.description"],
    "--typo-subhead-size": ["Typography.字号.description"],
    "--typo-subhead-weight": ["Typography.字重.常规"],
    "--typo-subhead-lh": ["Typography.行高.description"],
    "--typo-footnote-size": ["Typography.字号.tips"],
    "--typo-footnote-weight": ["Typography.字重.常规"],
    "--typo-footnote-lh": ["Typography.行高.tips"],
    "--typo-caption1-size": ["Typography.字号.tiny"],
    "--typo-caption1-weight": ["Typography.字重.常规"],
    "--typo-caption1-lh": ["Typography.行高.tiny"],
    "--typo-caption2-size": ["Typography.字号.tiny"],
    "--typo-caption2-weight": ["Typography.字重.常规"],
    "--typo-caption2-lh": ["Typography.行高.tiny"],

    "--spacing-page-padding": ["Spacing.间距.500"],
    "--spacing-icon-gap": ["Spacing.间距.400"],
    "--spacing-section-gap": ["Spacing.间距.300"],
    "--spacing-grid-unit": ["Spacing.间距.200"],
    "--spacing-b1": ["Spacing.间距.200"],
    "--spacing-b2": ["Spacing.间距.300"],
    "--spacing-b3": ["Spacing.间距.400"],
    "--spacing-b4": ["Spacing.间距.500"],
    "--spacing-b5": ["Spacing.间距.600"],
    "--spacing-b6": ["Spacing.间距.700"],

    "--radius-button": ["Radius.400"],
    "--radius-button-pill": ["Radius.Full"],
    "--radius-thumb-small": ["Radius.100"],
    "--radius-thumb-medium": ["Radius.200"],
    "--radius-thumb-large": ["Radius.300"],
    "--radius-overlay": ["Radius.500", "Radius.400"],
    "--radius-action-sheet": ["Radius.300"],
    "--radius-dialog": ["Radius.300"],
    "--radius-menu": ["Radius.200"],
    "--radius-input": ["Radius.200"],
    "--radius-segment": ["Radius.100"],

    "--shadow-dialog": ["Shadow.shadow_md", "Shadow.shadow_lg"],
    "--shadow-menu": ["Shadow.shadow_md", "Shadow.shadow_lg"],

    "--anim-press-in-duration": ["Animation.duration_fast"],
    "--anim-press-in-easing": ["Animation.easing_out", "Animation.easing_default"],
    "--anim-press-out-duration": ["Animation.duration_fast", "Animation.duration_normal"],
    "--anim-press-out-easing": ["Animation.easing_out", "Animation.easing_default"],
    "--anim-switch-duration": ["Animation.duration_normal"],
    "--anim-switch-easing": ["Animation.easing_default"],
    "--anim-expand-duration": ["Animation.duration_normal", "Animation.duration_slow"],
    "--anim-expand-easing": ["Animation.easing_default"],
    "--anim-collapse-duration": ["Animation.duration_fast", "Animation.duration_normal"],
    "--anim-collapse-easing": ["Animation.easing_in", "Animation.easing_default"],
    "--anim-halfscreen-in-duration": ["Animation.duration_slow"],
    "--anim-halfscreen-in-easing": ["Animation.easing_default"],
    "--anim-halfscreen-out-duration": ["Animation.duration_normal"],
    "--anim-menu-in-duration": ["Animation.duration_normal"],
    "--anim-menu-in-easing": ["Animation.easing_out", "Animation.easing_default"],
    "--anim-menu-out-duration": ["Animation.duration_fast", "Animation.duration_normal"],
    "--anim-menu-out-easing": ["Animation.easing_in", "Animation.easing_default"],
}


@dataclass
class ValidationResult:
    json_valid: bool
    css_vars_total: int
    css_vars_replaced: int
    css_vars_skipped: int
    css_vars_failed: int
    css_vars_skipped_items: List[str]
    css_vars_failed_items: List[str]


@dataclass
class CssApplySummary:
    file_path: Path
    total_vars: int
    replaced_vars: int
    skipped_vars: List[str]
    failed_vars: List[str]


def _read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _list_token_systems(othertokens_dir: Path) -> List[Path]:
    return sorted(othertokens_dir.glob(TOKEN_FILE_PATTERN))


def _get_nested(data: Dict[str, Any], path: str) -> Any:
    cur: Any = data
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            raise KeyError(path)
        cur = cur[key]
    return cur


def _get_nested_safe(data: Dict[str, Any], path: str) -> Tuple[bool, Any]:
    cur: Any = data
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return False, None
        cur = cur[key]
    return True, cur


def _set_nested(data: Dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    cur = data
    for key in parts[:-1]:
        cur = cur[key]
    cur[parts[-1]] = value


def _resolve_alias(token_data: Dict[str, Any], value: Any) -> Any:
    if isinstance(value, str):
        m = re.fullmatch(r"\{([^{}]+)\}", value.strip())
        if m:
            ref_path = m.group(1)
            ref_obj = _get_nested(token_data, ref_path)
            if isinstance(ref_obj, dict) and "$value" in ref_obj:
                return _resolve_alias(token_data, ref_obj["$value"])
            return ref_obj
    return value


def _to_css_value(value: Any, token_data: Dict[str, Any]) -> str:
    resolved = _resolve_alias(token_data, value)
    if isinstance(resolved, dict) and "hex" in resolved:
        hex_value = resolved["hex"]
        alpha = resolved.get("alpha", 1)
        try:
            alpha_num = float(alpha)
        except Exception:
            alpha_num = 1
        if alpha_num >= 0.999:
            return hex_value.lower()
        hex_clean = hex_value.lstrip("#")
        if len(hex_clean) == 6:
            r = int(hex_clean[0:2], 16)
            g = int(hex_clean[2:4], 16)
            b = int(hex_clean[4:6], 16)
            return f"rgba({r}, {g}, {b}, {alpha_num:.3f})"
        return hex_value.lower()
    if isinstance(resolved, str):
        return resolved
    return json.dumps(resolved, ensure_ascii=False)


def _extract_target_value(target_data: Dict[str, Any], mapped_path: str) -> Any:
    node = _get_nested(target_data, mapped_path)
    if isinstance(node, dict) and "$value" in node:
        return _resolve_alias(target_data, node["$value"])
    return _resolve_alias(target_data, node)


def _extract_target_value_safe(target_data: Dict[str, Any], mapped_path: str) -> Tuple[bool, Any]:
    exists, node = _get_nested_safe(target_data, mapped_path)
    if not exists:
        return False, None
    if isinstance(node, dict) and "$value" in node:
        return True, _resolve_alias(target_data, node["$value"])
    return True, _resolve_alias(target_data, node)


def _collect_color_changes(before: Dict[str, Any], after: Dict[str, Any]) -> List[Tuple[str, Any, Any]]:
    changes: List[Tuple[str, Any, Any]] = []
    for p in sorted(INDEX_COLOR_MAPPING.keys()):
        b = _get_nested(before, p)
        a = _get_nested(after, p)
        if b != a:
            changes.append((p, b, a))
    return changes


def _replace_css_var(css_text: str, var_name: str, new_value: str) -> Tuple[str, int]:
    pattern = re.compile(rf"({re.escape(var_name)}\s*:\s*)([^;]+)(;)")

    def repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}{new_value}{match.group(3)}"

    new_css, count = pattern.subn(repl, css_text)
    return new_css, count


def _apply_index_colors(index_data: Dict[str, Any], target_data: Dict[str, Any]) -> Dict[str, Any]:
    updated = deepcopy(index_data)
    for src_path, target_path in INDEX_COLOR_MAPPING.items():
        target_value = _extract_target_value(target_data, target_path)
        if isinstance(target_value, dict) and "hex" in target_value:
            _set_nested(updated, src_path, _to_css_value(target_value, target_data))
        else:
            _set_nested(updated, src_path, target_value)
    return updated


def _infer_target_path_for_css_var(css_var: str) -> str | None:
    name = css_var.lower()

    if "allwhite" in name or "oncolor" in name:
        return "Color.文本色.text_allwhite"

    if "brand-light" in name or "bottom-brand" in name:
        return "Color.品牌色.brand_light"
    if "brand" in name:
        return "Color.品牌色.brand_standard"

    if "text-link" in name or name.endswith("-text-link"):
        return "Color.文本色.text_link"
    if "text-secondary" in name or "secondary-light" in name:
        return "Color.文本色.text_secondary"
    if "text-tertiary" in name:
        return "Color.文本色.text_tertiary"
    if "text-quaternary" in name or "text-disabled" in name:
        return "Color.文本色.text_quaternary"
    if "text" in name:
        return "Color.文本色.text_primary"

    if "icon-tertiary" in name:
        return "Color.图标色.icon_secondary"
    if "icon-secondary" in name:
        return "Color.图标色.icon_secondary"
    if "icon" in name:
        return "Color.图标色.icon_primary"

    if "feedback-success" in name:
        return "Color.反馈色.feedback_success"
    if "feedback-warning" in name:
        return "Color.反馈色.feedback_warning"
    if "feedback-error" in name:
        return "Color.反馈色.feedback_error"
    if "feedback" in name:
        return "Color.反馈色.feedback_standard"

    if "separator" in name or "border" in name or "stroke" in name:
        return "Color.分割色.Separators"

    if "overlay" in name or "mask" in name or "toast" in name:
        return "Color.叠加色.active"

    if "fill" in name or "btn-bg" in name or "button-bg" in name:
        if "tertiary" in name:
            return "Color.透明填充色.Tertiary"
        if "secondary" in name:
            return "Color.透明填充色.Secondary"
        if "quaternary" in name:
            return "Color.透明填充色.Quaternary"
        return "Color.透明填充色.Primary"

    if "bg-page" in name or "bottom-standard" in name:
        return "Color.分组背景色.Primary"
    if "bg-secondary" in name or "middle" in name:
        return "Color.背景色.Secondary"
    if "bg" in name or "bubble" in name or "nav" in name:
        return "Color.背景色.Primary"

    if "switch" in name or "handle" in name:
        return "Color.分割色.Separators"

    return None


def _is_color_css_var(css_var: str) -> bool:
    return css_var.startswith("--qq-") or css_var.startswith("--color-")


def _to_font_weight(value: Any) -> str | None:
    if isinstance(value, (int, float)):
        return str(int(value))
    if not isinstance(value, str):
        return None

    s = value.strip().lower()
    m = re.search(r"\b(100|200|300|400|500|600|700|800|900)\b", s)
    if m:
        return m.group(1)
    if "light" in s:
        return "300"
    if "regular" in s:
        return "400"
    if "medium" in s:
        return "500"
    if "semi" in s:
        return "600"
    if "bold" in s:
        return "700"
    return None


def _num_to_str(v: float | int) -> str:
    if isinstance(v, int):
        return str(v)
    if float(v).is_integer():
        return str(int(v))
    return f"{v}"


def _format_non_color_value(css_var: str, value: Any) -> str | None:
    if css_var in {"--device-platform"}:
        if not isinstance(value, str):
            return None
        return f'"{value}"'

    if css_var in {"--device-font", "--font-family"}:
        if not isinstance(value, str):
            return None
        return f'"{value}", -apple-system, "Helvetica Neue", sans-serif'

    if css_var.endswith("-weight"):
        w = _to_font_weight(value)
        return w

    if css_var.endswith("-duration"):
        if isinstance(value, (int, float)):
            return f"{_num_to_str(value)}ms"
        if isinstance(value, str):
            s = value.strip()
            if re.fullmatch(r"\d+(\.\d+)?", s):
                return f"{s}ms"
            return s
        return None

    if css_var.endswith("-easing") or css_var.endswith("-transform"):
        if isinstance(value, str):
            return value
        return None

    needs_px = (
        css_var.startswith("--typo-") and (css_var.endswith("-size") or css_var.endswith("-lh"))
    ) or css_var.startswith("--spacing-") or css_var.startswith("--radius-")

    if isinstance(value, (int, float)):
        if needs_px:
            return f"{_num_to_str(value)}px"
        return _num_to_str(value)

    if isinstance(value, str):
        if needs_px and re.fullmatch(r"\d+(\.\d+)?", value.strip()):
            return f"{value.strip()}px"
        return value

    return None


def _value_for_non_color_css_var(css_var: str, target_data: Dict[str, Any]) -> str | None:
    if css_var == "--device-platform":
        mode = target_data.get("$extensions", {}).get("com.figma.modeName")
        if isinstance(mode, str):
            return _format_non_color_value(css_var, mode)

    paths = NON_COLOR_CSS_VAR_TO_TARGET_PATHS.get(css_var)
    if not paths:
        return None

    for p in paths:
        found, value = _extract_target_value_safe(target_data, p)
        if not found:
            continue
        formatted = _format_non_color_value(css_var, value)
        if formatted is not None:
            return formatted
    return None


def _value_for_css_var(css_var: str, updated_index: Dict[str, Any], target_data: Dict[str, Any]) -> str | None:
    if _is_color_css_var(css_var):
        if css_var in CSS_VAR_TO_INDEX_KEY:
            index_key = CSS_VAR_TO_INDEX_KEY[css_var]
            src_path = f"tokens.color.{index_key}"
            return _to_css_value(_get_nested(updated_index, src_path), target_data)

        explicit = EXTRA_CSS_VAR_TO_TARGET_PATH.get(css_var)
        if explicit:
            found, value = _extract_target_value_safe(target_data, explicit)
            if found:
                return _to_css_value(value, target_data)
            return None

        inferred = _infer_target_path_for_css_var(css_var)
        if inferred:
            found, value = _extract_target_value_safe(target_data, inferred)
            if found:
                return _to_css_value(value, target_data)
        return None

    return _value_for_non_color_css_var(css_var, target_data)


def _apply_css_file(css_path: Path, updated_index: Dict[str, Any], target_data: Dict[str, Any]) -> Tuple[str, CssApplySummary]:
    css_text = _read_text(css_path)
    css_vars = sorted(set(re.findall(r"(--[a-z0-9\-]+)\s*:", css_text, flags=re.IGNORECASE)))

    result = css_text
    replaced = 0
    skipped: List[str] = []
    failed: List[str] = []

    for css_var in css_vars:
        try:
            new_value = _value_for_css_var(css_var, updated_index, target_data)
        except Exception:
            new_value = None

        if new_value is None:
            skipped.append(css_var)
            continue

        result, count = _replace_css_var(result, css_var, new_value)
        if count > 0:
            replaced += 1
        else:
            failed.append(css_var)

    summary = CssApplySummary(
        file_path=css_path,
        total_vars=len(css_vars),
        replaced_vars=replaced,
        skipped_vars=sorted(set(skipped)),
        failed_vars=sorted(set(failed)),
    )
    return result, summary


def _validate(index_path: Path, css_summaries: List[CssApplySummary]) -> ValidationResult:
    json_valid = True
    try:
        _read_json(index_path)
    except Exception:
        json_valid = False

    total = sum(s.total_vars for s in css_summaries)
    replaced = sum(s.replaced_vars for s in css_summaries)
    skipped = sum(len(s.skipped_vars) for s in css_summaries)
    failed = sum(len(s.failed_vars) for s in css_summaries)

    skipped_items: List[str] = []
    failed_items: List[str] = []
    for s in css_summaries:
        skipped_items.extend([f"{s.file_path.name}:{v}" for v in s.skipped_vars])
        failed_items.extend([f"{s.file_path.name}:{v}" for v in s.failed_vars])

    return ValidationResult(
        json_valid=json_valid,
        css_vars_total=total,
        css_vars_replaced=replaced,
        css_vars_skipped=skipped,
        css_vars_failed=failed,
        css_vars_skipped_items=sorted(skipped_items),
        css_vars_failed_items=sorted(failed_items),
    )


def _make_report(
    report_path: Path,
    target_name: str,
    color_changes: List[Tuple[str, Any, Any]],
    validation: ValidationResult,
    css_summaries: List[CssApplySummary],
) -> None:
    changed_paths = [p for p, _, _ in color_changes]
    total_mapped = len(INDEX_COLOR_MAPPING)
    changed_count = len(changed_paths)
    coverage = (changed_count / total_mapped * 100) if total_mapped else 0

    switchable = max(validation.css_vars_total - validation.css_vars_skipped, 0)
    hit_rate = (validation.css_vars_replaced / switchable * 100) if switchable else 100

    lines: List[str] = []
    lines.append("# Token 切换对比分析报告")
    lines.append("")
    lines.append(f"- 目标 Token 系统：`{target_name}`")
    lines.append(f"- 生成时间：`{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")
    lines.append("")
    lines.append("## 一、切换摘要")
    lines.append("")
    lines.append(f"- 映射总数：**{total_mapped}**")
    lines.append(f"- 实际变化：**{changed_count}**")
    lines.append(f"- 变化覆盖率：**{coverage:.1f}%**")
    lines.append(f"- CSS 总变量：**{validation.css_vars_total}**")
    lines.append(f"- CSS 已替换：**{validation.css_vars_replaced}**")
    lines.append(f"- CSS 无对应跳过：**{validation.css_vars_skipped}**")
    lines.append(f"- CSS 替换命中率（可替换项）：**{hit_rate:.1f}%**")
    lines.append("")
    lines.append("## 二、CSS 文件覆盖")
    lines.append("")
    for s in css_summaries:
        switchable_s = max(s.total_vars - len(s.skipped_vars), 0)
        ok = len(s.failed_vars) == 0
        lines.append(
            f"- `{s.file_path.as_posix()}`：替换 **{s.replaced_vars}** / 可替换 **{switchable_s}** / 总变量 **{s.total_vars}**"
            + (" ✅" if ok else " ⚠️")
        )

    lines.append("")
    lines.append("## 三、关键变化（index 映射）")
    lines.append("")
    if not color_changes:
        lines.append("- 无变化（目标系统与当前系统一致或映射值相同）")
    else:
        for path, before, after in color_changes[:30]:
            lines.append(f"- `{path}`: `{before}` → `{after}`")
        if len(color_changes) > 30:
            lines.append(f"- ... 其余 {len(color_changes) - 30} 项变化略")

    lines.append("")
    lines.append("## 四、自动校验结果")
    lines.append("")
    lines.append(f"- JSON 结构校验：{'✅ 通过' if validation.json_valid else '❌ 失败'}")
    lines.append(
        f"- CSS 替换执行校验：失败 **{validation.css_vars_failed}** 项"
        + (" ✅" if validation.css_vars_failed == 0 else " ⚠️")
    )
    if validation.css_vars_failed_items:
        lines.append("- 替换失败项：")
        for v in validation.css_vars_failed_items[:50]:
            lines.append(f"  - `{v}`")
        if len(validation.css_vars_failed_items) > 50:
            lines.append(f"  - ... 其余 {len(validation.css_vars_failed_items) - 50} 项略")
    else:
        lines.append("- 替换失败项：无")

    if validation.css_vars_skipped_items:
        lines.append("- 无对应跳过项（目标系统缺少对应 token）：")
        for v in validation.css_vars_skipped_items[:50]:
            lines.append(f"  - `{v}`")
        if len(validation.css_vars_skipped_items) > 50:
            lines.append(f"  - ... 其余 {len(validation.css_vars_skipped_items) - 50} 项略")
    else:
        lines.append("- 无对应跳过项：无")

    lines.append("")
    lines.append("## 五、多维度结论")
    lines.append("")
    lines.append("- **语义一致性**：优先显式映射，非颜色变量按存在性匹配（有对应则替换，无对应则保留原值）。")
    lines.append("- **视觉风格变化**：覆盖 `--color-*`、`--qq-*` 与 `tokens.css` 中可映射变量。")
    lines.append("- **工程影响范围**：更新 `json/index.json` 与 `css/*.css`。")
    lines.append("- **风险评估**：已输出替换失败项与无对应跳过项，便于后续补充映射。")

    _write_text(report_path, "\n".join(lines) + "\n")


def run(project_root: Path, target: str, apply: bool, report_out: Path) -> int:
    othertokens_dir = project_root / "othertokens"
    index_path = project_root / "json" / "index.json"
    css_dir = project_root / "css"

    if not othertokens_dir.exists():
        raise FileNotFoundError(f"未找到目录: {othertokens_dir}")
    if not index_path.exists():
        raise FileNotFoundError(f"未找到文件: {index_path}")
    if not css_dir.exists():
        raise FileNotFoundError(f"未找到目录: {css_dir}")

    systems = _list_token_systems(othertokens_dir)
    if not systems:
        raise FileNotFoundError("othertokens 目录下未发现 *.tokens.json")

    target_file: Path | None = None
    normalized_target = target.lower().replace(".tokens", "")
    for p in systems:
        stem_normalized = p.stem.lower().replace(".tokens", "")
        if (
            stem_normalized == normalized_target
            or p.stem.lower() == target.lower()
            or p.name.lower() == target.lower()
        ):
            target_file = p
            break
    if target_file is None:
        maybe = othertokens_dir / target
        if maybe.exists():
            target_file = maybe

    if target_file is None:
        available = ", ".join([p.stem for p in systems])
        raise ValueError(f"未找到目标系统 `{target}`。可选：{available}")

    index_before = _read_json(index_path)
    target_data = _read_json(target_file)

    index_after = _apply_index_colors(index_before, target_data)
    color_changes = _collect_color_changes(index_before, index_after)

    css_files = sorted(css_dir.glob("*.css"))
    css_outputs: Dict[Path, str] = {}
    css_summaries: List[CssApplySummary] = []

    for css_file in css_files:
        css_after, summary = _apply_css_file(css_file, index_after, target_data)
        css_outputs[css_file] = css_after
        css_summaries.append(summary)

    if apply:
        _write_json(index_path, index_after)
        for css_file, css_text in css_outputs.items():
            _write_text(css_file, css_text)

    validation = _validate(index_path, css_summaries)

    report_path = report_out if report_out.is_absolute() else (project_root / report_out)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    _make_report(report_path, target_file.stem, color_changes, validation, css_summaries)

    mode = "APPLY" if apply else "DRY-RUN"
    print(f"[{mode}] target={target_file.name}")
    print(f"index 变更项: {len(color_changes)}/{len(INDEX_COLOR_MAPPING)}")
    switchable = max(validation.css_vars_total - validation.css_vars_skipped, 0)
    print(f"css 替换项: {validation.css_vars_replaced}/{switchable} (总变量 {validation.css_vars_total}, 跳过 {validation.css_vars_skipped})")
    print(f"报告: {report_path}")
    if validation.css_vars_failed > 0:
        print(f"⚠️ 替换失败 {validation.css_vars_failed} 项，请查看报告")
    if not apply:
        print("未写入文件（dry-run）。如需应用，请增加 --apply")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Switch token system for plus-v1.0/basic-v1.0 (project-agnostic)")
    parser.add_argument("--project-root", default=".", help="项目根目录")
    parser.add_argument("--target", help="目标 token 系统名（如 iOS / Material / Microsoft / One+UI）")
    parser.add_argument("--list", action="store_true", help="列出可用 token 系统")
    parser.add_argument("--apply", action="store_true", help="真正写入文件；默认 dry-run")
    parser.add_argument("--report", default="md/TOKEN_SWITCH_REPORT.md", help="报告输出路径")

    args = parser.parse_args()
    root = Path(args.project_root).resolve()

    othertokens_dir = root / "othertokens"
    if args.list:
        systems = _list_token_systems(othertokens_dir)
        if not systems:
            print("未发现可用 token 系统")
            return 1
        print("可用 token 系统:")
        for p in systems:
            print(f"- {p.stem}")
        return 0

    if not args.target:
        raise ValueError("请通过 --target 指定目标 token 系统，或使用 --list 查看可选项")

    return run(
        project_root=root,
        target=args.target,
        apply=args.apply,
        report_out=Path(args.report),
    )


if __name__ == "__main__":
    raise SystemExit(main())
