from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import PhotoAlbum, Photo


@receiver(post_save, sender=PhotoAlbum)
@receiver(post_delete, sender=PhotoAlbum)
def clear_album_cache(sender, instance, **kwargs):
    """清除相册相关缓存"""
    # 清除相册详情缓存
    cache.delete(f'gallery:album:{instance.slug}:photos')

    # 清除相册列表缓存
    cache.delete('gallery:list:all')


@receiver(post_save, sender=Photo)
@receiver(post_delete, sender=Photo)
def clear_photo_cache(sender, instance, **kwargs):
    """清除照片相关缓存"""
    # 清除所属相册的详情缓存
    if instance.album:
        cache.delete(f'gallery:album:{instance.album.slug}:photos')

    # 清除相册列表缓存
    cache.delete('gallery:list:all')
