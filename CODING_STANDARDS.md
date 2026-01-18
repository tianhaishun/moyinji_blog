# 墨影纪 · 编码规范

> 版本：1.0
> 最后更新：2026-01-18

本文档定义了**墨影纪**项目的Python和Django编码规范，确保代码质量、可维护性和团队协作效率。

---

## 目录

- [1. Python编码规范](#1-python编码规范)
  - [1.1 PEP 8遵循](#11-pep-8遵循)
  - [1.2 命名规范](#12-命名规范)
  - [1.3 代码格式化](#13-代码格式化)
  - [1.4 类型注解](#14-类型注解)
  - [1.5 文档字符串](#15-文档字符串)
- [2. Django编码规范](#2-django编码规范)
  - [2.1 模型设计](#21-模型设计)
  - [2.2 视图编写](#22-视图编写)
  - [2.3 URL配置](#23-url配置)
  - [2.4 模板规范](#24-模板规范)
  - [2.5 表单处理](#25-表单处理)
  - [2.6 管理后台](#26-管理后台)
- [3. 数据库规范](#3-数据库规范)
  - [3.1 查询优化](#31-查询优化)
  - [3.2 索引设计](#32-索引设计)
  - [3.3 迁移管理](#33-迁移管理)
- [4. API设计规范](#4-api设计规范)
  - [4.1 RESTful原则](#41-restful原则)
  - [4.2 响应格式](#42-响应格式)
  - [4.3 错误处理](#43-错误处理)
- [5. 安全规范](#5-安全规范)
  - [5.1 输入验证](#51-输入验证)
  - [5.2 SQL注入防护](#52-sql注入防护)
  - [5.3 XSS防护](#53-xss防护)
  - [5.4 CSRF防护](#54-csrf防护)
- [6. 性能规范](#6-性能规范)
  - [6.1 缓存策略](#61-缓存策略)
  - [6.2 查询优化](#62-查询优化)
  - [6.3 静态资源](#63-静态资源)
- [7. 测试规范](#7-测试规范)
  - [7.1 单元测试](#71-单元测试)
  - [7.2 集成测试](#72-集成测试)
  - [7.3 测试覆盖率](#73-测试覆盖率)
- [8. 代码审查清单](#8-代码审查清单)

---

## 1. Python编码规范

### 1.1 PEP 8遵循

**基本规则**

```python
# ✅ 正确：使用4个空格缩进
def my_function():
    if condition:
        do_something()

# ❌ 错误：使用Tab缩进
def my_function():
	if condition:
		do_something()

# ✅ 正确：每行最多79个字符（建议）
long_string = (
    "这是一个非常长的字符串，"
    "使用括号进行隐式连接"
)

# ❌ 错误：单行过长
long_string = "这是一个非常长的字符串，超过了79个字符的限制"
```

**导入顺序**

```python
# 1. 标准库导入
import os
from datetime import datetime, timedelta

# 2. 第三方库导入
from django.db import models
from django.views.decorators.cache import cache_page
from rest_framework import status
import redis

# 3. 本地应用导入
from .models import BlogPost
from .services import PostService
from .utils import format_date

# 每组之间空一行
```

**导入规范**

```python
# ✅ 正确：明确导入
from django.db import models
from django.http import HttpResponse

# ❌ 错误：通配符导入（除了__init__.py）
from django.db import *

# ✅ 正确：多行导入（超过2个时）
from myapp.models import (
    BlogPost,
    Category,
    Tag,
)
```

---

### 1.2 命名规范

#### 变量命名

```python
# ✅ 函数和变量：snake_case
user_name = "Justin"
is_published = True
view_count = 0

# ✅ 常量：UPPER_SNAKE_CASE
MAX_UPLOAD_SIZE = 10 * 1024 * 1024
DEFAULT_PAGE_SIZE = 12
CACHE_TIMEOUT = 60 * 15

# ✅ 类：PascalCase
class BlogPost(models.Model):
    pass

class UserService:
    pass

# ✅ 私有变量/方法：前缀下划线
class UserService:
    def __init__(self):
        self._internal_state = {}

    def _private_method(self):
        pass
```

#### 模型字段命名

```python
class BlogPost(models.Model):
    # ✅ 使用描述性名称
    title = models.CharField(max_length=200)
    cover_image = models.ImageField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # ❌ 避免缩写（除非广为人知）
    # img = models.ImageField()  # 不推荐
    # pub_date = models.DateField()  # 不推荐
```

---

### 1.3 代码格式化

#### 空格使用

```python
# ✅ 正确：运算符两侧加空格
x = 1 + 2
result = (a + b) * (c - d)

# ✅ 正确：逗号后加空格
def function(arg1, arg2, arg3):
    items = [1, 2, 3]
    dictionary = {'key': 'value', 'key2': 'value2'}

# ✅ 正确：冒号和箭头两侧不加空格
def function(param: str) -> bool:
    return param.startswith('prefix')

# ✅ 正确：切片冒号两侧不加空格
items[1:10]
items[start:end:step]
```

#### 空行使用

```python
# ✅ 顶层定义之间空两行
class BlogPost(models.Model):
    pass


class Category(models.Model):
    pass


# ✅ 类内部方法之间空一行
class BlogPost(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])

# ✅ 函数内部逻辑块之间空一行（可选，用于提高可读性）
def publish_post(post):
    # 验证
    if not post.title:
        raise ValueError("标题不能为空")

    # 发布
    post.is_published = True
    post.save()

    # 通知
    send_notification(post)
```

---

### 1.4 类型注解

**基础类型注解**

```python
from typing import List, Dict, Optional, Union

# ✅ 函数签名添加类型注解
def get_blog_posts(
    category: Optional[str] = None,
    tag: Optional[str] = None,
    limit: int = 10
) -> List[BlogPost]:
    """
    获取博客文章列表

    Args:
        category: 分类slug
        tag: 标签slug
        limit: 返回数量限制

    Returns:
        文章列表
    """
    queryset = BlogPost.objects.filter(is_published=True)

    if category:
        queryset = queryset.filter(category__slug=category)
    if tag:
        queryset = queryset.filter(tags__slug=tag)

    return list(queryset[:limit])


# ✅ 复杂类型使用TypeAlias
PostDict = Dict[str, Union[str, int, bool]]

def format_post(post: BlogPost) -> PostDict:
    return {
        'title': post.title,
        'slug': post.slug,
        'created_at': post.created_at.isoformat(),
    }
```

---

### 1.5 文档字符串

**Google风格文档字符串（推荐）**

```python
def get_published_posts(
    category: Optional[str] = None,
    limit: int = 12
) -> QuerySet['BlogPost']:
    """获取已发布的文章列表。

    支持按分类筛选和数量限制。

    Args:
        category: 分类slug，None表示获取所有分类
        limit: 返回的最大文章数量，默认12篇

    Returns:
        已发布的文章QuerySet

    Raises:
        ValueError: 当limit小于1时

    Examples:
        >>> get_published_posts(category='landscape', limit=5)
        <QuerySet [<BlogPost: 山水意境1>, ...]>
    """
    if limit < 1:
        raise ValueError("limit必须大于0")

    queryset = BlogPost.objects.filter(is_published=True)

    if category:
        queryset = queryset.filter(category__slug=category)

    return queryset[:limit]
```

**类文档字符串**

```python
class BlogPost(models.Model):
    """博客文章模型。

    存储博客文章的所有信息，包括标题、内容、分类、标签等。
    支持Markdown格式的文章内容。

    Attributes:
        title: 文章标题，最大200字符
        slug: URL友好的唯一标识符
        content: Markdown格式的文章内容
        is_published: 是否已发布
        created_at: 创建时间
        updated_at: 最后更新时间
    """

    title = models.CharField(max_length=200, verbose_name='标题')
    # ...
```

---

## 2. Django编码规范

### 2.1 模型设计

#### 基础模型结构

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    """博客文章模型。"""

    # 字段定义顺序：
    # 1. 关系字段
    category = models.ForeignKey(
        'blog.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='分类'
    )

    # 2. 普通字段
    title = models.CharField(
        max_length=200,
        verbose_name='标题',
        help_text='建议长度不超过50字'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL别名',
        help_text='自动生成，可手动修改'
    )
    content = models.TextField(verbose_name='内容')

    # 3. 可选字段
    excerpt = models.TextField(
        max_length=300,
        blank=True,
        verbose_name='摘要'
    )

    # 4. 布尔字段
    is_published = models.BooleanField(
        default=False,
        verbose_name='是否发布'
    )

    # 5. 时间字段
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新时间'
    )

    # Meta类
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),
            models.Index(fields=['is_published', '-created_at']),
        ]
        # 权限
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # 自动生成slug（如果未提供）
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
```

#### 模型方法规范

```python
class BlogPost(models.Model):
    # ... 字段定义 ...

    def get_related_posts(self, limit: int = 3) -> QuerySet['BlogPost']:
        """获取相关文章。

        基于相同分类或标签推荐相关文章。

        Args:
            limit: 返回数量，默认3篇

        Returns:
            相关文章QuerySet
        """
        # 优先推荐同分类文章
        if self.category:
            related = BlogPost.objects.filter(
                category=self.category,
                is_published=True
            ).exclude(id=self.id)
            return related[:limit]

        # 次选：基于标签推荐
        # （实现省略）
        return BlogPost.objects.none()

    @property
    def is_recent(self) -> bool:
        """判断是否为最近发布的文章（7天内）。"""
        from django.utils import timezone
        delta = timezone.now() - self.created_at
        return delta.days <= 7
```

---

### 2.2 视图编写

#### 函数视图规范

```python
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from .models import BlogPost
from .forms import BlogPostForm


@require_http_methods(['GET'])
@cache_page(60 * 15)  # 缓存15分钟
def blog_list(request):
    """文章列表页。

    支持分页、分类筛选、标签筛选、搜索。
    """
    # 获取参数
    page = request.GET.get('page', 1)
    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    query = request.GET.get('q')

    # 构建查询
    posts = BlogPost.objects.filter(is_published=True)

    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)
    if query:
        posts = posts.filter(title__icontains=query)

    # 分页
    paginator = Paginator(posts, 12)
    posts_page = paginator.get_page(page)

    # 上下文
    context = {
        'posts': posts_page,
        'current_category': category_slug,
        'current_tag': tag_slug,
        'query': query,
    }

    return render(request, 'blog/blog_list.html', context)


@require_http_methods(['GET'])
def blog_detail(request, slug):
    """文章详情页。"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    # 增加浏览次数
    post.view_count += 1
    post.save(update_fields=['view_count'])

    # 相关文章
    related_posts = post.get_related_posts()

    context = {
        'post': post,
        'related_posts': related_posts,
    }

    return render(request, 'blog/blog_detail.html', context)
```

#### 类视图规范

```python
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost


class BlogListView(ListView):
    """文章列表视图。"""

    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 12
    ordering = ['-created_at']

    def get_queryset(self):
        """获取查询集，支持筛选。"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)

        return queryset

    def get_context_data(self, **kwargs):
        """添加额外上下文。"""
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.request.GET.get('category')
        return context


class BlogDetailView(DetailView):
    """文章详情视图。"""

    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_queryset(self):
        """仅获取已发布的文章。"""
        return super().get_queryset().filter(is_published=True)

    def get_object(self, queryset=None):
        """获取对象时增加浏览次数。"""
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj
```

---

### 2.3 URL配置

#### URL设计规范

```python
# urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 列表页
    path('',
         views.blog_list,
         name='list'),

    # 详情页
    path('<slug:slug>/',
         views.blog_detail,
         name='detail'),

    # 分类筛选
    path('category/<slug:category_slug>/',
         views.blog_list,
         name='category'),

    # 标签筛选
    path('tag/<slug:tag_slug>/',
         views.blog_list,
         name='tag'),
]
```

**URL命名规范**

```python
# ✅ 正确：使用简短、描述性的名称
path('posts/', views.post_list, name='list')
path('posts/<int:id>/', views.post_detail, name='detail')
path('about/', views.about, name='about')

# ❌ 错误：过于简短或模糊
path('posts/', views.post_list, name='pl')
path('posts/<int:id>/', views.post_detail, name='pd')
```

**使用reverse()**

```python
from django.urls import reverse
from django.http import HttpResponseRedirect

def redirect_to_post(request, post_id):
    # ✅ 正确：使用URL名称
    url = reverse('blog:detail', kwargs={'slug': post.slug})
    return HttpResponseRedirect(url)

    # ❌ 错误：硬编码URL
    # return HttpResponseRedirect(f'/blog/{post.slug}/')
```

---

### 2.4 模板规范

#### 模板继承

```django
{% extends "base.html" %}

{% block title %}{{ post.title }} - 墨影纪{% endblock %}

{% block meta %}
<meta name="description" content="{{ post.excerpt }}">
{% endblock %}

{% block content %}
<div class="min-h-screen bg-yuebai">
    <!-- 内容 -->
</div>
{% endblock %}
```

#### 模板最佳实践

```django
<!-- ✅ 正确：使用模板变量 -->
<h1>{{ post.title }}</h1>
<p>{{ post.content|safe }}</p>

<!-- ❌ 错误：硬编码文本 -->
<h1>文章标题</h1>

<!-- ✅ 正确：使用过滤器 -->
<p class="text-sm">
    {{ post.created_at|date:"Y年m月d日" }}
</p>

<!-- ✅ 正确：条件渲染 -->
{% if post.cover_image %}
<img src="{{ post.cover_image.url }}" alt="{{ post.title }}">
{% else %}
<div class="placeholder">无封面</div>
{% endif %}

<!-- ✅ 正确：循环 -->
{% for post in posts %}
<article class="card-song">
    <h3>{{ post.title }}</h3>
</article>
{% empty %}
<p>暂无文章</p>
{% endfor %}
```

---

### 2.5 表单处理

```python
from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """文章表单。"""

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'category', 'tags', 'excerpt']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-yaqing/20',
                'placeholder': '请输入文章标题'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full h-96 p-4',
                'placeholder': '支持Markdown格式'
            }),
        }
        help_texts = {
            'slug': '留空将自动生成',
        }

    def clean_title(self):
        """验证标题。"""
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("标题至少5个字符")
        return title

    def save(self, commit=True, user=None):
        """保存时添加作者信息。"""
        post = super().save(commit=False)
        if user:
            post.author = user
        if commit:
            post.save()
            self.save_m2m()  # 保存多对多关系
        return post
```

**视图中的表单处理**

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BlogPostForm


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    """创建文章视图。"""

    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """表单验证通过后添加作者。"""
        form.instance.author = self.request.user
        return super().form_valid(form)
```

---

### 2.6 管理后台

```python
from django.contrib import admin
from .models import BlogPost, Category, Tag


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """文章管理。"""

    list_display = [
        'title',
        'category',
        'is_published',
        'view_count',
        'created_at',
    ]
    list_filter = ['is_published', 'category', 'tags', 'created_at']
    search_fields = ['title', 'content', 'slug']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    # 只读字段
    readonly_fields = ['view_count', 'created_at', 'updated_at']

    # 字段分组
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'slug', 'category', 'tags')
        }),
        ('内容', {
            'fields': ('cover_image', 'excerpt', 'content')
        }),
        ('发布设置', {
            'fields': ('is_published',),
            'classes': ('collapse',),
        }),
        ('统计信息', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # 操作
    actions = ['make_published', 'make_draft']

    def make_published(self, request, queryset):
        """批量发布。"""
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f'{updated}篇文章已发布'
        )
    make_published.short_description = '批量发布'

    def make_draft(self, request, queryset):
        """批量设为草稿。"""
        updated = queryset.update(is_published=False)
        self.message_user(
            request,
            f'{updated}篇文章已设为草稿'
        )
    make_draft.short_description = '批量设为草稿'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """分类管理。"""

    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}

    def post_count(self, obj):
        """文章数量。"""
        return obj.posts.count()
    post_count.short_description = '文章数'
```

---

## 3. 数据库规范

### 3.1 查询优化

#### 避免N+1问题

```python
# ❌ 错误：N+1查询问题
posts = BlogPost.objects.all()
for post in posts:
    print(post.category.name)  # 每次循环查询一次数据库

# ✅ 正确：使用select_related
posts = BlogPost.objects.select_related('category').all()
for post in posts:
    print(post.category.name)  # 只查询一次数据库

# ✅ 正确：多对多使用prefetch_related
posts = BlogPost.objects.prefetch_related('tags').all()
for post in posts:
    for tag in post.tags.all():
        print(tag.name)
```

#### 仅查询需要的字段

```python
# ✅ 仅查询需要的字段
posts = BlogPost.objects.values('title', 'slug', 'created_at')

# ✅ 仅查询需要的字段（返回对象）
posts = BlogPost.objects.only('title', 'slug', 'created_at')

# ✅ 延迟加载不常用的字段
posts = BlogPost.objects.defer('content', 'excerpt')
```

#### 使用聚合

```python
from django.db.models import Count, Avg, Max

# ✅ 使用聚合而非循环
category_stats = Category.objects.annotate(
    post_count=Count('posts')
)

for category in category_stats:
    print(f"{category.name}: {category.post_count}篇文章")
```

---

### 3.2 索引设计

```python
class BlogPost(models.Model):
    # ... 字段定义 ...

    class Meta:
        indexes = [
            # 单列索引
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),

            # 复合索引（注意顺序）
            models.Index(fields=['is_published', '-created_at']),

            # 条件索引（PostgreSQL）
            # models.Index(
            #     fields=['title'],
            #     name='title_idx',
            #     condition=Q(is_published=True),
            # ),
        ]
```

**索引设计原则**

1. **为WHERE子句中的列添加索引**
2. **为ORDER BY子句中的列添加索引**
3. **为外键添加索引**
4. **避免过度索引**（索引会降低写入性能）
5. **复合索引注意列顺序**（最常用的列在前）

---

### 3.3 迁移管理

```bash
# 创建迁移
python manage.py makemigrations

# 创建命名迁移
python manage.py makemigrations --name add_view_count_to_posts

# 应用迁移
python manage.py migrate

# 查看迁移SQL
python manage.py sqlmigrate app_name migration_number

# 回滚迁移
python manage.py migrate app_name migration_number

# 检查未应用的迁移
python manage.py showmigrations
```

**迁移文件命名**

```python
# ✅ 正确：描述性的迁移名称
# 0001_initial.py
# 0002_add_view_count_to_posts.py
# 0003_add_slug_to_categories.py

# ❌ 错误：无意义的名称
# 0001_20230101_120000.py
# migration_2.py
```

---

## 4. API设计规范

### 4.1 RESTful原则

```python
# blog/serializers.py
from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """文章序列化器。"""

    category_name = serializers.CharField(source='category.name', read_only=True)
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'excerpt',
            'category',
            'category_name',
            'tag_names',
            'is_published',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_tag_names(self, obj):
        """获取标签名称列表。"""
        return [tag.name for tag in obj.tags.all()]


# blog/views.py
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class BlogPostViewSet(viewsets.ModelViewSet):
    """文章ViewSet。"""

    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'tags', 'is_published']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'view_count']
    ordering = ['-created_at']

    def get_queryset(self):
        """优化查询。"""
        return super().get_queryset().select_related('category').prefetch_related('tags')

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """获取最近文章。"""
        recent_posts = self.get_queryset()[:5]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        """增加浏览次数。"""
        post = self.get_object()
        post.view_count += 1
        post.save(update_fields=['view_count'])
        return Response({'view_count': post.view_count})
```

---

### 4.2 响应格式

**成功响应**

```json
{
    "success": true,
    "data": {
        "id": 1,
        "title": "文章标题",
        "slug": "article-slug",
        "created_at": "2026-01-18T10:00:00Z"
    },
    "message": "操作成功"
}
```

**列表响应**

```json
{
    "success": true,
    "data": {
        "results": [...],
        "count": 100,
        "next": "http://api.example.com/posts?page=2",
        "previous": null
    }
}
```

**错误响应**

```json
{
    "success": false,
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "验证失败",
        "details": {
            "title": ["标题不能为空"]
        }
    }
}
```

---

### 4.3 错误处理

```python
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    """自定义异常处理。"""

    # 调用DRF默认异常处理
    response = exception_handler(exc, context)

    if response is not None:
        # 自定义错误格式
        custom_response = {
            'success': False,
            'error': {
                'code': exc.__class__.__name__,
                'message': str(exc),
                'details': response.data
            },
            'status_code': response.status_code
        }
        response.data = custom_response

    return response


# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myproject.exceptions.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}
```

---

## 5. 安全规范

### 5.1 输入验证

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def clean_title(title):
    """验证标题。"""
    if not title:
        raise ValidationError(_("标题不能为空"))

    if len(title) < 5:
        raise ValidationError(_("标题至少5个字符"))

    if len(title) > 200:
        raise ValidationError(_("标题不超过200字符"))

    # 检查敏感词
    sensitive_words = ['敏感词1', '敏感词2']
    for word in sensitive_words:
        if word in title:
            raise ValidationError(_("标题包含敏感词"))

    return title
```

---

### 5.2 SQL注入防护

```python
# ✅ 正确：使用ORM参数化查询
post = BlogPost.objects.get(slug=slug)

# ✅ 正确：使用raw()时参数化
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM blog_blogpost WHERE slug = %s", [slug])

# ❌ 错误：字符串拼接（SQL注入风险）
cursor.execute(f"SELECT * FROM blog_blogpost WHERE slug = '{slug}'")
```

---

### 5.3 XSS防护

```python
from django.utils.safestring import mark_safe
from django.utils.html import escape

# ✅ 默认转义HTML
{{ user_input }}  # 自动转义

# ✅ 确认安全后再输出
{{ post.content|safe }}  # 管理员输入的HTML

# ✅ 手动转义
clean_content = escape(user_input)

# ✅ Python代码中
from django.utils.html import strip_tags
clean_title = strip_tags(user_input)
```

---

### 5.4 CSRF防护

```python
# ✅ 模板中添加CSRF token
<form method="post">
    {% csrf_token %}
    <!-- 表单字段 -->
</form>

# ✅ 视图中使用@csrf_protect装饰器
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def my_view(request):
    if request.method == 'POST':
        # 处理表单
        pass

# ✅ AJAX请求中添加CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

fetch('/api/posts/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
});
```

---

## 6. 性能规范

### 6.1 缓存策略

```python
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator

# 视图缓存
@cache_page(60 * 15)  # 缓存15分钟
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

# 类视图缓存
@method_decorator(cache_page(60 * 15), name='dispatch')
class BlogListView(ListView):
    model = BlogPost

# 模板片段缓存
{% load cache %}
{% cache 500 sidebar %}
    <!-- 耗时渲染的内容 -->
{% endcache %}

# 查询结果缓存
def get_categories():
    cache_key = 'categories:all'
    categories = cache.get(cache_key)

    if not categories:
        categories = list(Category.objects.all())
        cache.set(cache_key, categories, 60 * 60)

    return categories
```

---

### 6.2 查询优化

```python
# ✅ 使用exists()而非count()
if BlogPost.objects.filter(slug=slug).exists():
    pass

# ❌ 避免
if BlogPost.objects.filter(slug=slug).count() > 0:
    pass

# ✅ 使用批量操作
BlogPost.objects.bulk_create([
    BlogPost(title='Post 1'),
    BlogPost(title='Post 2'),
])

# ✅ 使用update()而非循环save()
BlogPost.objects.filter(is_published=False).update(is_published=True)
```

---

### 6.3 静态资源

```python
# settings.py
# 静态文件收集
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

# 生产环境
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# 媒体文件
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
```

```bash
# 收集静态文件
python manage.py collectstatic --noinput

# 使用Whitenoise（开发环境）
pip install whitenoise
```

---

## 7. 测试规范

### 7.1 单元测试

```python
from django.test import TestCase
from .models import BlogPost, Category
from .services import PostService


class BlogPostModelTest(TestCase):
    """文章模型测试。"""

    @classmethod
    def setUpTestData(cls):
        """创建测试数据（仅执行一次）。"""
        cls.category = Category.objects.create(
            name='测试分类',
            slug='test-category'
        )
        cls.post = BlogPost.objects.create(
            title='测试文章',
            slug='test-post',
            category=cls.category,
            content='测试内容'
        )

    def test_title_max_length(self):
        """测试标题最大长度。"""
        max_length = self.post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        """测试URL生成。"""
        self.assertEqual(
            self.post.get_absolute_url(),
            '/blog/test-post/'
        )

    def test_post_creation(self):
        """测试文章创建。"""
        self.assertEqual(self.post.title, '测试文章')
        self.assertTrue(self.post.slug)
        self.assertEqual(self.post.category, self.category)


class PostServiceTest(TestCase):
    """文章服务测试。"""

    def setUp(self):
        """每个测试前执行。"""
        self.service = PostService()

    def test_get_published_posts(self):
        """测试获取已发布文章。"""
        # 创建测试数据
        BlogPost.objects.create(
            title='已发布',
            slug='published',
            is_published=True
        )
        BlogPost.objects.create(
            title='草稿',
            slug='draft',
            is_published=False
        )

        # 调用方法
        posts = self.service.get_published_posts()

        # 验证结果
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts.first().title, '已发布')
```

---

### 7.2 集成测试

```python
from django.test import Client, TestCase
from django.urls import reverse
from .models import BlogPost


class BlogViewTest(TestCase):
    """博客视图集成测试。"""

    def setUp(self):
        self.client = Client()
        self.post = BlogPost.objects.create(
            title='测试文章',
            slug='test-post',
            is_published=True
        )

    def test_blog_list_status_code(self):
        """测试列表页状态码。"""
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_template(self):
        """测试列表页模板。"""
        response = self.client.get(reverse('blog:list'))
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_blog_detail_context(self):
        """测试详情页上下文。"""
        response = self.client.get(
            reverse('blog:detail', kwargs={'slug': 'test-post'})
        )
        self.assertIn('post', response.context)
        self.assertEqual(response.context['post'].title, '测试文章')

    def test_pagination(self):
        """测试分页。"""
        # 创建多篇文章
        for i in range(15):
            BlogPost.objects.create(
                title=f'文章{i}',
                slug=f'post-{i}',
                is_published=True
            )

        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
```

---

### 7.3 测试覆盖率

```bash
# 安装coverage
pip install coverage

# 运行测试并生成覆盖率报告
coverage run --source='.' manage.py test
coverage report
coverage html  # 生成HTML报告
```

```python
# .coveragerc
[run]
source = .
omit =
    */migrations/*
    */venv/*
    */tests/*
    manage.py

[report]
precision = 2
show_missing = True
skip_covered = False
```

**覆盖率目标**

- 核心业务逻辑：≥ 90%
- 模型层：≥ 85%
- 视图层：≥ 80%
- 工具函数：≥ 95%

---

## 8. 代码审查清单

### 提交代码前自检

#### 功能性
- [ ] 功能符合需求
- [ ] 边界情况处理完善
- [ ] 错误处理合理
- [ ] 日志记录充分

#### 代码质量
- [ ] 遵循PEP 8规范
- [ ] 命名清晰有意义
- [ ] 函数简短专注（<50行）
- [ ] 注释适度不过度
- [ ] 无重复代码（DRY原则）
- [ ] 无硬编码配置

#### 性能
- [ ] 无N+1查询问题
- [ ] 使用了select_related/prefetch_related
- [ ] 添加了必要的索引
- [ ] 实现了缓存策略
- [ ] 优化了图片和静态资源

#### 安全性
- [ ] 无SQL注入风险
- [ ] 无XSS漏洞
- [ ] CSRF保护启用
- [ ] 敏感数据未泄露
- [ ] 输入验证完善

#### 测试
- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 测试覆盖率达标
- [ ] 边界情况已测试

#### 文档
- [ ] 文档字符串完整
- [ ] API文档更新
- [ ] README更新（如需要）
- [ ] 迁移文件正确

---

## 附录

### A. 有用的工具

```bash
# 代码格式化
pip install black
black .

# 代码检查
pip install flake8
flake8 .

# 类型检查
pip install mypy
mypy .

# 导入排序
pip install isort
isort .

# 安全检查
pip install bandit
bandit -r .
```

### B. VSCode配置

```json
// .vscode/settings.json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.sortImports.args": ["--profile", "black"],
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        ".pytest_cache": true
    }
}
```

### C. Pre-commit钩子

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
```

```bash
# 安装
pip install pre-commit
pre-commit install
```

---

**本文档由墨影纪团队维护**
**最后更新：2026-01-18**
