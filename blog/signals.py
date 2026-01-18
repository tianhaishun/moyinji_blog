from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import BlogPost, Category, Tag


@receiver(post_save, sender=BlogPost)
@receiver(post_delete, sender=BlogPost)
def clear_blog_post_cache(sender, instance, **kwargs):
    """清除文章相关缓存"""
    # 清除文章详情缓存
    cache.delete(f'blog:detail:{instance.slug}')

    # 清除文章列表缓存（需要清除所有可能的组合）
    cache.delete_pattern('blog:list:*')

    # 如果文章有分类，清除该分类相关的缓存
    if instance.category:
        cache.delete_pattern(f'blog:list:category:{instance.category.slug}:*')

    # 清除所有标签相关的缓存
    for tag in instance.tags.all():
        cache.delete_pattern(f'blog:list:tag:{tag.slug}:*')


@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def clear_category_cache(sender, instance, **kwargs):
    """清除分类相关缓存"""
    # 清除包含该分类的所有文章列表缓存
    cache.delete_pattern(f'blog:list:category:{instance.slug}:*')
    # 清除文章列表缓存
    cache.delete_pattern('blog:list:*')


@receiver(post_save, sender=Tag)
@receiver(post_delete, sender=Tag)
def clear_tag_cache(sender, instance, **kwargs):
    """清除标签相关缓存"""
    # 清除包含该标签的所有文章列表缓存
    cache.delete_pattern(f'blog:list:tag:{instance.slug}:*')
    # 清除文章列表缓存
    cache.delete_pattern('blog:list:*')
