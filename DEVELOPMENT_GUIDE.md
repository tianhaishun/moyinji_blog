# 墨影纪 · 开发手册与设计规范

> 版本：1.0
> 最后更新：2026-01-18

本文档定义了**墨影纪**项目的开发规范、设计标准和最佳实践，确保所有页面保持统一的审美风格和代码质量。

---

## 目录

- [一、设计规范](#一设计规范)
  - [1.1 色彩系统](#11-色彩系统)
  - [1.2 字体规范](#12-字体规范)
  - [1.3 间距与留白](#13-间距与留白)
  - [1.4 阴影与圆角](#14-阴影与圆角)
- [二、组件规范](#二组件规范)
  - [2.1 卡片组件](#21-卡片组件)
  - [2.2 按钮组件](#22-按钮组件)
  - [2.3 标签组件](#23-标签组件)
  - [2.4 导航组件](#24-导航组件)
- [三、布局规范](#三布局规范)
  - [3.1 页面结构](#31-页面结构)
  - [3.2 网格系统](#32-网格系统)
  - [3.3 响应式断点](#33-响应式断点)
- [四、动画规范](#四动画规范)
  - [4.1 页面过渡](#41-页面过渡)
  - [4.2 悬停效果](#42-悬停效果)
  - [4.3 加载状态](#43-加载状态)
- [五、模板规范](#五模板规范)
  - [5.1 模板继承](#51-模板继承)
  - [5.2 组件复用](#52-组件复用)
  - [5.3 条件渲染](#53-条件渲染)
- [六、代码规范](#六代码规范)
  - [6.1 命名规范](#61-命名规范)
  - [6.2 注释规范](#62-注释规范)
  - [6.3 性能优化](#63-性能优化)

---

## 一、设计规范

### 1.1 色彩系统

#### 主色调
```python
# 色彩定义（Tailwind CSS 配置）
colors: {
    'yuebai': '#F6F8FA',      # 月白 - 主背景
    'yaqing': '#3C4856',      # 鸦青 - 主文字
    'hupo': '#B78B5D',        # 琥珀 - 强调色
    'zhusha': '#D03B40',      # 朱砂 - 点缀色
    'dailan': '#2A5CAA',      # 黛蓝 - 辅助色
    'paper': '#F0EFE9',       # 古纸色 - 内容背景
    'ink': '#1A1A1A',        # 墨色 - 强调文字
}
```

#### 使用原则

| 场景 | 色彩 | 说明 |
|------|------|------|
| 页面背景 | `bg-yuebai` | 统一的主背景色 |
| 内容区背景 | `bg-paper` | 古纸色，营造阅读氛围 |
| 正文文字 | `text-yaqing` | 主文字色，保持可读性 |
| 次要文字 | `text-yaqing/70` | 降低透明度区分层级 |
| 强调元素 | `text-hupo` | 琥珀色，温和醒目 |
| 警示/重要 | `text-zhusha` | 朱砂色，谨慎使用 |
| 链接文字 | `text-dailan` | 黛蓝，专业感 |

#### 禁用色彩
- ❌ 纯黑色 (`#000000`)：改用墨色 (`#1A1A1A`)
- ❌ 纯白色 (`#FFFFFF`)：改用月白 (`#F6F8FA`)
- ❌ 高饱和度颜色：破坏宋代美学氛围

---

### 1.2 字体规范

#### 字体栈
```css
font-family: {
    'serif': ['Georgia', 'serif'],                    # 英文衬线
    'song': ['"Source Han Serif SC"',              # 思源宋体
             '"Noto Serif SC"',
             'serif'],
    'sans': ['system-ui', 'sans-serif'],             # 系统字体（备选）
}
```

#### 使用规范

| 场景 | 字体类 | 字号 | 字重 |
|------|--------|------|------|
| 页面标题 | `text-display` | 4xl-6xl | normal |
| 章节标题 | `text-heading` | 2xl-3xl | normal |
| 小标题 | `text-subheading` | lg | normal |
| 正文内容 | `text-body` | base | normal |
| 说明文字 | `text-caption` | sm | normal |

#### 实例
```html
<!-- 页面标题 -->
<h1 class="text-display font-serif text-yaqing">墨影纪</h1>

<!-- 章节标题 -->
<h2 class="text-heading font-serif">山水意境</h2>

<!-- 正文 -->
<p class="text-body text-yaqing/80">内容...</p>

<!-- 说明 -->
<span class="text-caption text-yaqing/60">2026年1月</span>
```

---

### 1.3 间距与留白

#### 间距单位
```css
spacing: {
    'song': '5%',      # 宋式留白（章节间距）
    'content': '6',    # 内容区内边距（px单位，1.5rem）
}
```

#### 使用原则

| 场景 | 间距 | 说明 |
|------|------|------|
| 页面垂直间距 | `py-16` 至 `py-20` | 64-80px |
| 水平内边距 | `px-6` | 24px |
| 元素间距 | `gap-4` 至 `gap-8` | 16-32px |
| 章节间距 | `py-song` (5%) | 强调留白美学 |
| 内边距 | `p-6` 至 `p-12` | 24-48px |

#### 实例
```html
<!-- 页面区域 -->
<section class="py-20 px-6">
  <div class="max-w-7xl mx-auto">
    <!-- 内容 -->
  </div>
</section>

<!-- 章节分隔 -->
<section class="py-song">
  <!-- 主要内容区 -->
</section>

<!-- 卡片内边距 -->
<div class="card-song p-8">
  <!-- 内容 -->
</div>
```

---

### 1.4 阴影与圆角

#### 阴影规范
```css
/* 轻微阴影（默认卡片） */
box-shadow: 0 1px 3px rgba(60, 72, 86, 0.1);

/* 中等阴影（悬停状态） */
box-shadow: 0 4px 20px rgba(60, 72, 86, 0.1);

/* 强调阴影（弹窗） */
box-shadow: 0 20px 60px rgba(60, 72, 86, 0.3);
```

#### 圆角规范
```css
/* 微圆角（默认） */
border-radius: 0.125rem;  /* 2px */

/* 小圆角（按钮） */
border-radius: 0.25rem;    /* 4px */

/* 中圆角（卡片） */
border-radius: 0.5rem;     /* 8px */
```

#### 实例
```html
<!-- 卡片 -->
<div class="card-song shadow-sm rounded-sm">
  <!-- 内容 -->
</div>

<!-- 按钮 -->
<button class="btn-song rounded-sm">
  查看更多
</button>
```

---

## 二、组件规范

### 2.1 卡片组件

#### 基础卡片
```html
<article class="card-song overflow-hidden group">
  <a href="{{ url }}" class="block">
    <!-- 图片区域 -->
    <div class="zoom-container aspect-[4/3] ink-wash-hover">
      {% if cover_image %}
      <img src="{{ cover_image.url }}"
           alt="{{ title }}"
           class="w-full h-full object-cover"
           loading="lazy">
      {% else %}
      <div class="aspect-[4/3] bg-yaqing/10 flex items-center justify-center">
        <span class="text-yaqing/40 text-4xl">墨</span>
      </div>
      {% endif %}
    </div>

    <!-- 内容区域 -->
    <div class="p-6">
      <h3 class="text-lg font-serif text-yaqing group-hover:text-hupo transition-colors">
        {{ title }}
      </h3>
      {% if excerpt %}
      <p class="text-body line-clamp-2 mt-2">{{ excerpt }}</p>
      {% endif %}
      {% if date %}
      <p class="text-caption text-yaqing/60 mt-4">{{ date }}</p>
      {% endif %}
    </div>
  </a>
</article>
```

#### 卡片变体

| 类型 | 说明 | 额外类 |
|------|------|--------|
| **基础卡片** | 默认卡片 | `card-song` |
| **可点击卡片** | 整体可点击 | 添加 `<a>` 包裹 |
| **动画卡片** | 入场动画 | `animate-unfurl` |
| **交错动画** | 延迟入场 | `{% cycle 'stagger-0' 'stagger-1' 'stagger-2' 'stagger-3' %}` |

---

### 2.2 按钮组件

#### 主要按钮（空心）
```html
<a href="{{ url }}" class="btn-song">
  按钮文字
</a>
```

#### 强调按钮（实心）
```html
<a href="{{ url }}" class="btn-song-solid">
  按钮文字
</a>
```

#### 按钮规范
```css
/* 空心按钮 */
.btn-song {
    @apply px-6 py-2 border border-hupo text-hupo
               transition-all duration-300 font-serif
               hover:bg-hupo hover:text-white;
}

/* 实心按钮 */
.btn-song-solid {
    @apply px-6 py-2 bg-hupo text-white
               transition-all duration-300 font-serif
               hover:bg-yaqing;
}
```

---

### 2.3 标签组件

#### 基础标签
```html
<span class="tag-song">标签文字</span>
```

#### 可点击标签
```html
<a href="{{ url }}" class="tag-song hover:border-hupo hover:text-hupo">
  标签文字
</a>
```

#### 激活状态
```html
<span class="tag-song border-hupo text-hupo">
  当前分类
</span>
```

#### 标签规范
```css
.tag-song {
    @apply inline-block px-3 py-1 text-sm
               border border-yaqing/20 text-yaqing/70
               hover:border-hupo hover:text-hupo
               transition-all duration-300 cursor-pointer;
}
```

---

### 2.4 导航组件

#### 导航链接样式
```html
<a href="{{ url }}" class="nav-link">链接文字</a>
```

#### 导航规范
```css
.nav-link {
    @apply text-yaqing/80 hover:text-hupo
               transition-colors duration-300
               relative;
}

.nav-link::after {
    content: '';
    @apply absolute bottom-0 left-0 w-0 h-0.5
               bg-hupo transition-all duration-300;
}

.nav-link:hover::after {
    @apply w-full;
}
```

---

## 三、布局规范

### 3.1 页面结构

#### 标准页面模板
```html
{% extends "base.html" %}

{% block content %}
<!-- 页面容器 -->
<div class="min-h-screen bg-yuebai">

  <!-- 页头（可选） -->
  <section class="py-16 px-6 border-b border-yaqing/10">
    <div class="max-w-7xl mx-auto text-center">
      <h1 class="text-display mb-6 animate-unfurl">页面标题</h1>
      {% if subtitle %}
      <p class="text-body">{{ subtitle }}</p>
      {% endif %}
    </div>
  </section>

  <!-- 主要内容 -->
  <section class="py-16 px-6">
    <div class="max-w-7xl mx-auto">
      <!-- 内容区块 -->
    </div>
  </section>

</div>
{% endblock %}
```

---

### 3.2 网格系统

#### 标准网格
```html
<div class="grid-song">
  <!-- 自动响应式网格，最小300px -->
  {% for item in items %}
  <div class="card-song">
    {{ item.content }}
  </div>
  {% endfor %}
</div>
```

#### 瀑布流（相册）
```html
<div class="masonry-song">
  <!-- 3列瀑布流，平板2列，手机1列 -->
  {% for photo in photos %}
  <div class="card-song masonry-item">
    {{ photo.content }}
  </div>
  {% endfor %}
</div>
```

#### 自定义网格
```html
<div class="grid md:grid-cols-3 gap-8">
  <!-- 固定3列网格 -->
</div>
```

---

### 3.3 响应式断点

#### 断点规范
```css
/* 移动端（默认） */
/* 适用于 < 768px */

/* 平板 */
@media (min-width: 768px) {
  /* md: 断点 */
}

/* 桌面 */
@media (min-width: 1024px) {
  /* lg: 断点 */
}

/* 大屏 */
@media (min-width: 1280px) {
  /* xl: 断点 */
}
```

#### 响应式示例
```html
<!-- 响应式网格 -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- 移动1列，平板2列，桌面3列 -->
</div>

<!-- 响应式文字 -->
<h1 class="text-2xl md:text-4xl lg:text-6xl">
  <!-- 移动24px，平板36px，桌面60px -->
</h1>

<!-- 响应式内边距 -->
<div class="p-4 md:p-8 lg:p-12">
  <!-- 移动16px，平板32px，桌面48px -->
</div>
```

---

## 四、动画规范

### 4.1 页面过渡

#### 标准页面入场
```html
<!-- 单元素入场 -->
<div class="animate-unfurl">
  内容
</div>

<!-- 多元素交错入场 -->
<div class="animate-unfurl stagger-0">内容1</div>
<div class="animate-unfurl stagger-1">内容2</div>
<div class="animate-unfurl stagger-2">内容3</div>
<div class="animate-unfurl stagger-3">内容4</div>
```

#### 循环交错动画（推荐）
```html
{% for item in items %}
<div class="animate-unfurl {% cycle 'stagger-0' 'stagger-1' 'stagger-2' 'stagger-3' %}">
  {{ item.content }}
</div>
{% endfor %}
```

---

### 4.2 悬停效果

#### 图片缩放
```html
<div class="zoom-container">
  <img src="{{ url }}" class="hover:scale-105 transition-transform duration-500">
</div>
```

#### 水墨晕染
```html
<div class="ink-wash-hover" style="--mouse-x: 50%; --mouse-y: 50%;">
  <!-- 内容 -->
</div>
```

#### 文字颜色变化
```html
<h3 class="group-hover:text-hupo transition-colors duration-300">
  标题
</h3>
```

#### 遮罩渐变
```html
<div class="relative overflow-hidden">
  <img src="{{ url }}" class="w-full h-full object-cover">
  <div class="absolute inset-0 bg-gradient-to-t from-yaqing/60 to-transparent
                  opacity-0 group-hover:opacity-100 transition-opacity duration-300">
  </div>
</div>
```

---

### 4.3 加载状态

#### 骨架屏
```html
<div class="skeleton w-full h-64 rounded-sm">
  <!-- 加载中占位 -->
</div>
```

#### 加载动画规范
```css
@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.skeleton {
    background: linear-gradient(90deg,
                #E8E8E8 25%,
                #F5F5F5 50%,
                #E8E8E8 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
}
```

---

## 五、模板规范

### 5.1 模板继承

#### 基础模板结构
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}墨影纪{% endblock %}</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- 自定义样式 -->
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/song-style.css' %}">

    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <!-- 额外CSS -->
    {% block extra_css %}{% endblock %}
</head>
<body class="bg-yuebai font-song text-yaqing antialiased">

    <!-- 导航栏 -->
    <nav>
        <!-- 导航内容 -->
    </nav>

    <!-- 主要内容 -->
    <main class="pt-16 min-h-screen">
        {% block content %}{% endblock %}
    </main>

    <!-- 页脚 -->
    <footer>
        <!-- 页脚内容 -->
    </footer>

    <!-- 额外JS -->
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

### 5.2 组件复用

#### 包含标签（推荐用于复杂组件）
```python
# 创建 templatetags/components.py
from django import template

register = template.Library()

@register.inclusion_tag('components/card.html')
def card(title, content, url=None):
    return {'title': title, 'content': content, 'url': url}
```

```html
<!-- 使用 -->
{% load components %}
{% card title="标题" content="内容" url="/path/" %}
```

---

### 5.3 条件渲染

#### 图片条件渲染
```html
<!-- 始终检查图片是否存在 -->
{% if post.cover_image %}
<img src="{{ post.cover_image.url }}" alt="{{ post.title }}">
{% else %}
<div class="aspect-[4/3] bg-yaqing/10 flex items-center justify-center">
  <span class="text-yaqing/40 text-4xl">墨</span>
</div>
{% endif %}

<!-- 带链接的条件渲染 -->
{% if url %}
<a href="{{ url }}" class="card-song">
  {% if image %}...{% endif %}
</a>
{% else %}
<div class="card-song">
  {% if image %}...{% endif %}
</div>
{% endif %}
```

---

## 六、代码规范

### 6.1 命名规范

#### 文件命名
```
模板文件：使用下划线分隔
├── blog_detail.html
├── blog_list.html
└── gallery_detail.html

静态文件：使用下划线分隔
├── song_style.css
└── lightbox.js
```

#### 模板变量命名
```python
# 使用下划线分隔的小写
blog_post
photo_album
cover_image
is_published
created_at
```

#### CSS 类命名
```css
/* 使用连字符分隔，添加前缀 */
.song-card
.song-button
.ink-wash-hover
.animate-unfurl
```

---

### 6.2 注释规范

#### 模板注释
```html
<!-- 主要区块 -->
{% comment "主要内容区块" %}
{% endcomment %}

<!-- 单行注释 -->
<!-- 图片区域 -->

<!-- 条件说明 -->
{% if post.cover_image %}
<!-- 有封面图时显示 -->
<img src="{{ post.cover_image.url }}">
{% endif %}
```

---

### 6.3 性能优化

#### 图片优化
```html
<!-- 1. 懒加载 -->
<img src="{{ url }}" loading="lazy">

<!-- 2. 使用缩略图 -->
<img src="{{ photo.thumbnail_square.url }}"
     data-full="{{ photo.image.url }}"
     class="lazyload">

<!-- 3. 设置尺寸 -->
<img src="{{ url }}" width="400" height="300">
```

#### 静态文件
```python
# settings.py
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# 收集静态文件
python manage.py collectstatic --noinput
```

---

## 七、页面开发检查清单

### 新页面开发时必须遵循：

- [ ] 使用 `base.html` 继承基础模板
- [ ] 页面背景使用 `bg-yuebai` 或 `bg-paper`
- [ ] 主内容区使用 `max-w-7xl mx-auto` 居中
- [ ] 垂直间距使用 `py-16` 或 `py-20`
- [ ] 标题使用 `text-heading` 或 `text-display`
- [ ] 正文使用 `text-body text-yaqing/80`
- [ ] 卡片使用 `card-song` 类
- [ ] 图片容器添加 `ink-wash-hover` 效果
- [ ] 列表项使用 `animate-unfurl` + `stagger-X` 动画
- [ ] 空状态提供友好的提示文案
- [ ] 响应式测试（移动端、平板、桌面）
- [ ] 图片缺失时的占位处理

---

## 八、常见模式示例

### 8.1 列表页面模式

```html
{% extends "base.html" %}

{% block content %}
<div class="min-h-screen bg-paper">
    <!-- 页头 -->
    <section class="py-16 px-6 border-b border-yaqing/10">
        <div class="max-w-7xl mx-auto text-center">
            <h1 class="text-display animate-unfurl">{{ page_title }}</h1>
        </div>
    </section>

    <!-- 列表内容 -->
    <section class="py-16 px-6">
        <div class="max-w-7xl mx-auto">
            {% if items %}
            <div class="grid-song">
                {% for item in items %}
                <div class="card-song animate-unfurl {% cycle 'stagger-0' 'stagger-1' 'stagger-2' 'stagger-3' %}">
                    <!-- 卡片内容 -->
                </div>
                {% endfor %}
            </div>
            {% else %}
            <div class="text-center py-20">
                <p class="text-yaqing/60">暂无内容</p>
            </div>
            {% endif %}
        </div>
    </section>
</div>
{% endblock %}
```

### 8.2 详情页面模式

```html
{% extends "base.html" %}

{% block content %}
<div class="min-h-screen bg-yuebai">
    <!-- 页头 -->
    <section class="py-16 px-6">
        <div class="max-w-4xl mx-auto">
            <a href="{{ back_url }}" class="text-yaqing/60 hover:text-yaqing">
                ← 返回
            </a>
        </div>
    </section>

    <!-- 主内容 -->
    <section class="py-8 px-6">
        <div class="max-w-4xl mx-auto">
            <article class="card-song p-8 md:p-12">
                <!-- 标题 -->
                <h1 class="text-display mb-6">{{ title }}</h1>

                <!-- 元信息 -->
                <div class="flex items-center gap-4 text-caption text-yaqing/60 mb-8">
                    <span>{{ date }}</span>
                    {% if category %}
                    <span>{{ category.name }}</span>
                    {% endif %}
                </div>

                <!-- 内容 -->
                <div class="prose prose-lg">
                    {{ content }}
                </div>
            </article>
        </div>
    </section>
</div>
{% endblock %}
```

---

## 九、CSS 工具类速查

### 常用组合
```html
<!-- 居中容器 -->
<div class="max-w-7xl mx-auto px-6">

<!-- 页面区块 -->
<section class="py-16 px-6">

<!-- 卡片 -->
<div class="card-song overflow-hidden group">

<!-- 动画入场 -->
<div class="animate-unfurl stagger-0">

<!-- 图片容器 -->
<div class="zoom-container ink-wash-hover">

<!-- 文字样式 -->
<h1 class="text-display font-serif text-yaqing">
<p class="text-body text-yaqing/80">
```

---

## 十、扩展指南

### 添加新页面时

1. **继承基础模板**：`{% extends "base.html" %}`
2. **包裹页面容器**：`<div class="min-h-screen bg-yuebai">`
3. **使用标准间距**：`py-16 px-6`
4. **添加入场动画**：`animate-unfurl stagger-0`
5. **保持一致色调**：遵循色彩系统
6. **处理空状态**：提供友好提示

### 修改设计时

1. **优先修改 Tailwind 配置**（`tailwind.config.js`）
2. **避免内联样式**：使用 utility classes
3. **新增颜色**：添加到色彩系统并更新文档
4. **测试响应式**：移动端 → 平板 → 桌面

---

## 附录

### A. 色彩速查表

| 名称 | 色值 | 用途 | Tailwind 类 |
|------|------|------|-----------|
| 月白 | #F6F8FA | 背景 | `bg-yuebai` |
| 鸦青 | #3C4856 | 文字 | `text-yaqing` |
| 琥珀 | #B78B5D | 强调 | `text-hupo` / `border-hupo` |
| 朱砂 | #D03B40 | 警示 | `text-zhusha` / `border-zhusha` |
| 黛蓝 | #2A5CAA | 辅助 | `text-dailan` / `border-dailan` |
| 古纸 | #F0EFE9 | 内容背景 | `bg-paper` |
| 墨色 | #1A1A1A | 强调文字 | `text-ink` |

### B. 动画速查表

| 动画名称 | 类名 | 延迟 |
|---------|------|------|
| 卷轴展开 | `animate-unfurl` | - |
| 交错入场 | `stagger-0` ~ `stagger-3` | 0s ~ 0.3s |
| 水墨晕染 | `ink-wash-hover` | - |
| 图片缩放 | `zoom-container` | - |

### C. 常见问题

**Q: 如何修改页面背景色？**
A: 在最外层 `div` 添加 `bg-yuebai`（月白）或 `bg-paper`（古纸色）。

**Q: 如何添加入场动画？**
A: 添加 `animate-unfurl` 类，如有多个元素，使用 `{% cycle 'stagger-0' 'stagger-1' 'stagger-2' 'stagger-3' %}`。

**Q: 图片缺失时如何处理？**
A: 使用 `{% if image %}...{% else %}<div class="placeholder">墨</div>{% endif %}`。

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
