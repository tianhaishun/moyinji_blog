from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import PhotoAlbum, Photo


@cache_page(60 * 15)  # 缓存15分钟
def gallery_list(request):
    """相册列表页"""
    cache_key = 'gallery:list:all'

    # 尝试从缓存获取
    cached_context = cache.get(cache_key)
    if cached_context:
        return render(request, 'gallery/gallery_list.html', cached_context)

    albums = PhotoAlbum.objects.all()

    context = {
        'albums': albums,
    }

    # 缓存上下文
    cache.set(cache_key, context, 60 * 15)

    return render(request, 'gallery/gallery_list.html', context)


def gallery_detail(request, slug):
    """相册详情页"""
    cache_key = f'gallery:album:{slug}:photos'

    # 尝试从缓存获取相册
    cached_data = cache.get(cache_key)
    if cached_data and not request.GET.get('no-cache'):
        return render(request, 'gallery/gallery_detail.html', cached_data)

    album = get_object_or_404(PhotoAlbum, slug=slug)
    photos = album.photos.all()

    context = {
        'album': album,
        'photos': photos,
    }

    # 缓存相册详情
    cache.set(cache_key, context, 60 * 30)  # 缓存30分钟

    return render(request, 'gallery/gallery_detail.html', context)
