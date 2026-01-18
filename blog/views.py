from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, Tag


def blog_list(request):
    """文章列表页"""
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
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """文章详情页"""
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
    return render(request, 'blog/blog_detail.html', context)
