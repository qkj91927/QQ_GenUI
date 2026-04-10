# 图片块 ImageBlock · 组件设计规范

> **组件 ID**：`image_block`  
> **大类**：数据  
> **变体数量**：10 种（A1-A5 通栏 + B1-B5 嵌入）

> Figma Frame: `1_9610` (468×4056px)  
> 资源路径: `icons/`（通用占位图：`placeholder_landscape.svg` / `placeholder_portrait.svg` / `placeholder_square.svg`）

---

## 一、组件概述

图片块组件用于在半屏浮层内展示图片内容，支持 **通栏** 和 **嵌入** 两种样式，共 **10 种子组件变体**。

| 分类 | 编号 | 数量 | 说明 |
|------|------|------|------|
| A · 通栏 | A1-A5 | 5 种 | 图片撑满容器宽度（428px），无内边距 |
| B · 嵌入 | B1-B5 | 5 种 | 图片区域 396px，四周各 16px 内边距 |

---

## 二、变体定义

### A. 通栏（Full-Width）

图片直接铺满 428px 容器宽度，无 padding。

| 编号 | 名称 | 图片尺寸 | 容器高度 | 说明 |
|------|------|----------|----------|------|
| A1 | 单图轮播 · 短 | 428×200 | 200px | 底部有 6 个分页指示器 |
| A2 | 单图轮播 · 中 | 428×320 | 320px | 底部有 6 个分页指示器 |
| A3 | 单图轮播 · 长 | 428×420 | 420px | 底部有 6 个分页指示器 |
| A4 | 四宫格 | 428×428 | 428px | 2×2 布局，格子 213×213px，间距 2px |
| A5 | 九宫格 | 428×428 | 428px | 3×3 布局，格子 141.33×141.33px，间距 2px |

### B. 嵌入（Inset）

图片区域宽 396px，位于容器内 padding: 16px。

| 编号 | 名称 | 图片尺寸 | 容器高度 | 说明 |
|------|------|----------|----------|------|
| B1 | 单图轮播 · 短 | 396×200 | 232px | 底部有 6 个分页指示器 |
| B2 | 单图轮播 · 中 | 396×320 | 352px | 底部有 6 个分页指示器 |
| B3 | 单图轮播 · 长 | 396×388 | 420px | 底部有 6 个分页指示器 |
| B4 | 四宫格 | 396×396 | 428px | 2×2 布局，格子 197×197px，间距 2px |
| B5 | 九宫格 | 396×396 | 428px | 3×3 布局，格子 130.67×130.67px，间距 2px |

---

## 三、布局规格

### 3.0 容器通用属性

```css
.image-block-container {
    width: 428px;
    background: var(--bg_bottom_light);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}
```

### 3.1 通栏布局

```
┌──────────────────────────────────┐  428px
│                                  │
│          图片（撑满宽度）           │  imgHeight
│                                  │
│         ● ○ ○ ○ ○ ○             │  分页指示器（距底部 24px）
└──────────────────────────────────┘
```

- 图片 `width: 428px`，`display: block`

### 3.2 嵌入布局

```
┌──────────────────────────────────┐  428px
│  ┌────────────────────────────┐  │
│  │      图片（396px宽）        │  │  padding: 16px
│  │                            │  │  imgHeight
│  │                            │  │
│  └────────────────────────────┘  │
│         ● ○ ○ ○ ○ ○             │  分页指示器
└──────────────────────────────────┘
```

- 图片 `width: 396px`，`margin: 16px 16px 0 16px`，`display: block`

### 3.3 宫格布局

**宫格容器通用属性**：
```css
.image-block-grid {
    position: relative;      /* 子元素绝对定位 */
}
.image-block-grid img {
    display: block;
    position: absolute;      /* 每个格子通过 left/top 精确定位 */
}
```

**通栏四宫格（A4）：**
- 容器宽度: 428px，高度: 428px
- 格子尺寸: 213×213px
- 间距: 2px
- 布局: 绝对定位 — (0,0), (215,0), (0,215), (215,215)

**通栏九宫格（A5）：**
- 容器宽度: 428px，高度: 428px
- 格子尺寸: 141.33×141.33px
- 间距: 2px
- 布局: 绝对定位，3×3 网格

**嵌入四宫格（B4）：**
- 宫格容器: 396×396px，`margin: 16px`
- 格子尺寸: 197×197px
- 间距: 2px
- 外层容器高度: 396 + 16 × 2 = **428px**

**嵌入九宫格（B5）：**
- 宫格容器: 396×396px，`margin: 16px`
- 格子尺寸: 130.67×130.67px
- 间距: 2px
- 外层容器高度: 396 + 16 × 2 = **428px**

> 嵌入宫格的外层容器高度计算：`totalHeight - 32` = gridWrap 高度（其中 32 = 上下各 16px margin）

---

## 四、分页指示器

仅轮播类变体（A1-A3、B1-B3）包含分页指示器，宫格类（A4-A5、B4-B5）不包含。

**CSS 属性**：
```css
.image-block-dots {
    width: 428px;           /* 撑满容器宽度 */
    height: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;               /* 圆点间距 */
    position: absolute;
    left: 0;
}
.image-block-dots .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
}
.image-block-dots .dot.active { background: var(--brand_standard); }     /* 品牌蓝 */
.image-block-dots .dot.inactive { background: var(--fill_standard_primary); }
```

**图片样式**：
```css
.image-block-container.full-width .image-block-img {
    width: 428px;
    display: block;
}
.image-block-container.inset .image-block-img {
    width: 396px;
    margin: 16px 16px 0 16px;
    display: block;
}
```

- **数量**: 6 个圆点（1 个激活 + 5 个非激活）
- **激活态**: 第一个圆点，`#0099FF`
- **非激活态**: 其余 5 个，`rgba(13, 16, 49, 0.04)`
- **垂直定位**: 通过 `top` 属性精确控制，距图片底部约 24px

| 变体 | 指示器 Y 坐标 |
|------|--------------|
| A1 | 176px |
| A2 | 288px |
| A3 | 396px |
| B1 | 192px |
| B2 | 312px |
| B3 | 380px |

---

## 五、设计 Token

| 属性 | 通栏 | 嵌入 |
|------|------|------|
| 容器宽度 | 428px | 428px |
| 图片宽度 | 428px | 396px |
| 水平内边距 | 0 | 16px |
| 顶部内边距 | 0 | 16px |
| 底部内边距 | 0 | 16px |
| 背景色 | `#FFFFFF` | `#FFFFFF` |
| 宫格间距 | 2px | 2px |

---

## 六、资源文件映射

### 图片资源（通用占位图）

| 文件 | 对应变体 | 说明 |
|------|---------|------|
| `icons/placeholder_landscape.svg` | A1/A2/B1/B2 | 横版占位图，通过 `object-fit: cover` 适配不同高度 |
| `icons/placeholder_portrait.svg` | A3/B3 | 竖版占位图，通过 `object-fit: cover` 适配不同高度 |
| `icons/placeholder_square.svg` | A4/A5/B4/B5 | 正方形占位图，通过 `object-fit: cover` 适配宫格单元格尺寸 |

### 指示器 SVG

| 文件 | 说明 |
|------|------|
| 1.svg | 激活态圆点（#0099FF, 8×8） |
| 2-6.svg | A1 非激活态圆点 |
| 7-11.svg | A2 非激活态圆点 |
| 12-16.svg | A3 非激活态圆点 |
| 17-21.svg | B1 非激活态圆点 |
| 22-26.svg | B2 非激活态圆点 |
| 27-31.svg | B3 非激活态圆点 |

---

## 七、交互行为

### 7.1 轮播指示器点击切换（组件内交互）
- 轮播类变体（A1-A3、B1-B3）的 6 个分页指示器圆点支持**点击切换激活态**
- 点击某个圆点后：该圆点变为激活态（`#0099FF`），其余圆点变为非激活态（`rgba(13, 16, 49, 0.04)`）
- 状态切换通过添加/移除 CSS class `active` / `inactive` 实现
- 过渡动画：`transition: background 200ms ease-out`
- 圆点设置 `cursor: pointer` 提供视觉反馈

### 7.2 轮播滑动（业务层）
- 左右滑动切换图片由业务层实现
- 滑动时需同步更新指示器激活态（与 7.1 相同的 class 切换逻辑）
- 变体矩阵和组件构建器中不实现滑动交互，仅实现指示器点击切换

### 7.3 宫格点击（业务层）
- 组件仅渲染宫格布局的静态图片
- 点击单张图片打开大图预览由业务层实现

### 7.4 组件构建器特有行为
- ImageBlock 在侧边栏预览中使用 A1（通栏·单图轮播·短）缩略展示
- 画布中拖入后以原始 428px 宽度渲染
- 图片不可编辑（与 TextBlock 的文本可编辑不同）

### 7.5 交互状态 CSS 参考

```css
.image-block-dots .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    cursor: pointer;
    transition: background 200ms ease-out;
}
.image-block-dots .dot.active { background: var(--brand_standard); }
.image-block-dots .dot.inactive { background: var(--fill_standard_primary); }
```

**事件委托（全局）**：
```javascript
document.addEventListener('click', function(e) {
    const dot = e.target.closest('.image-block-dots .dot');
    if (dot) {
        const dotsBar = dot.parentElement;
        dotsBar.querySelectorAll('.dot').forEach(d => {
            d.classList.remove('active');
            d.classList.add('inactive');
        });
        dot.classList.remove('inactive');
        dot.classList.add('active');
    }
});
```

---

## 八、使用场景

| 场景 | 推荐变体 |
|------|---------|
| Banner 轮播 | A1/A2（通栏短/中） |
| 详情大图预览 | A3（通栏长） |
| 图片选择器 | A4/A5（通栏宫格） |
| 卡片内嵌图片 | B1/B2（嵌入短/中） |
| 内容详情配图 | B3（嵌入长） |
| 内嵌相册缩略图 | B4/B5（嵌入宫格） |
