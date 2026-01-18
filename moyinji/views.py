from django.shortcuts import render
from blog.models import BlogPost
from gallery.models import PhotoAlbum


def home(request):
    """首页"""
    # 获取最新发布的文章
    latest_posts = BlogPost.objects.filter(is_published=True)[:6]

    # 获取精选相册
    featured_albums = PhotoAlbum.objects.filter(is_featured=True)

    context = {
        'latest_posts': latest_posts,
        'featured_albums': featured_albums,
    }
    return render(request, 'home.html', context)


def about(request):
    """关于页"""
    return render(request, 'about.html')
