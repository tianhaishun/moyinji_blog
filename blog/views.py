from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from .models import BlogPost, Category, Tag


@cache_page(60 * 15)  # 缓存15分钟
def blog_list(request):
    """文章列表页"""
    # 生成缓存键，包含筛选参数
    cache_key = f'blog:list:category:{request.GET.get("category", "all")}:tag:{request.GET.get("tag", "all")}'

    # 尝试从缓存获取
    cached_context = cache.get(cache_key)
    if cached_context:
        return render(request, 'blog/blog_list.html', cached_context)

    posts = BlogPost.objects.filter(is_published=True)

    # 按分类筛选
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    # 按标签筛选
    tag_slug = request.GET.get('tag')
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags=tag)

    # 获取所有分类和标签用于筛选器
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'current_category': category_slug,
        'current_tag': tag_slug,
    }

    # 缓存上下文
    cache.set(cache_key, context, 60 * 15)

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """文章详情页"""
    cache_key = f'blog:detail:{slug}'

    # 尝试从缓存获取文章
    cached_data = cache.get(cache_key)
    if cached_data and not request.GET.get('no-cache'):
        # 即使有缓存，也需要更新浏览次数（异步）
        post = BlogPost.objects.get(slug=slug, is_published=True)
        post.view_count += 1
        post.save(update_fields=['view_count'])
        cached_data['post'].view_count = post.view_count
        return render(request, 'blog/blog_detail.html', cached_data)

    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    # 增加浏览次数
    post.view_count += 1
    post.save(update_fields=['view_count'])

    # 获取相关文章（相同分类或标签）
    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(
        id=post.id
    ).filter(
        category=post.category
    )[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }

    # 缓存文章详情
    cache.set(cache_key, context, 60 * 30)  # 缓存30分钟

    return render(request, 'blog/blog_detail.html', context)
