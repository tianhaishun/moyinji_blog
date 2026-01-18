from django.shortcuts import render, get_object_or_404
from .models import PhotoAlbum, Photo


def gallery_list(request):
    """相册列表页"""
    albums = PhotoAlbum.objects.all()

    context = {
        'albums': albums,
    }
    return render(request, 'gallery/gallery_list.html', context)


def gallery_detail(request, slug):
    """相册详情页"""
    album = get_object_or_404(PhotoAlbum, slug=slug)
    photos = album.photos.all()

    context = {
        'album': album,
        'photos': photos,
    }
    return render(request, 'gallery/gallery_detail.html', context)
