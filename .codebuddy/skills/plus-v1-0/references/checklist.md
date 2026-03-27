# Gate 执行与回归检查清单（强约束版）

> 规则：每个 Gate 未通过不得进入下一 Gate。

## Gate 1：仓库拉取

- [ ] 已拉取 `https://github.com/qkj91927/test_component`
- [ ] 已切换并同步 `plus-v1.0` 分支
- [ ] 已确认本地工作目录基于 `plus-v1.0` 最新内容

## Gate 2：目标与组件候选

- [ ] 已明确页面目标、信息层级、交互动作
- [ ] 已列出候选母组件
- [ ] 已标记是否包含 `Grouped List` 或 `Card`
- [ ] 已判断是否满足 Pro 组件启用条件

## Gate 3：组件硬约束

- [ ] 已读取目标组件 `md/*_SPEC.md`
- [ ] List 组合满足 `LIST_COMPONENT_SPEC.md`
- [ ] Grouped List 组合满足 `GROUPED_LIST_COMPONENT_SPEC.md`
- [ ] NavBar 组合满足 `NAVBAR_COMPONENT_SPEC.md`
- [ ] 若使用 Pro 组件，已读取 `PRO_*_COMPONENT_SPEC.md`
- [ ] 模态组件未嵌套

## Gate 4：Token 与主题

- [ ] `<html>` 已设置 `data-theme`
- [ ] 颜色全部来自 `css/QQ_color_tokens.css`
- [ ] 非颜色 Token 来自 `css/tokens.css`
- [ ] 间距均为 4px 整数倍

## Gate 5：背景色强约束

- [ ] 包含 `Grouped List`/`Card` 时使用 `#F0F0F2`
- [ ] 默认场景使用 `#FFFFFF`
- [ ] 冲突场景灰底优先

## Gate 6：状态栏

- [ ] 页面顶部包含 428×54 StatusBar
- [ ] 时间固定 `9:41`
- [ ] 图标路径为 `network/wifi/battery`
- [ ] 状态栏背景与 NavBar 一致

## Gate 7：图标替换

- [ ] `empty_icon.svg` 残留为 0
- [ ] 图标均来自 `icons/QUI_24_icons/`
- [ ] 图标路径格式正确

## Gate 8：初次产出

- [ ] 页面生成与必要实现已完成
- [ ] 内部规则检查已完成并可进入回归

## Gate 9：回归测试与修复闭环（最多3轮）

### 轮次 1
- [ ] 已执行回归比对
- [ ] 已记录问题数
- [ ] 已完成修复
- [ ] 已复测

### 轮次 2（若轮次1未达100%）
- [ ] 已执行回归比对
- [ ] 已记录问题数
- [ ] 已完成修复
- [ ] 已复测

### 轮次 3（若轮次2未达100%）
- [ ] 已执行回归比对
- [ ] 已记录问题数
- [ ] 已完成修复
- [ ] 已复测

### 回归结果要求

- [ ] 在 ≤3 轮内达到 100% 合规（问题数=0），或执行满3轮后结束回归
- [ ] 若第3轮后仍非0，已输出未修复问题清单（问题/影响/建议）

## Gate 10：最终交付

- [ ] 已附 Gate 1~10 通过状态
- [ ] 已附回归轮次摘要（每轮问题数变化）
- [ ] 未达100%时已附未修复问题清单
- [ ] 已附审查与完善建议（四维度）
