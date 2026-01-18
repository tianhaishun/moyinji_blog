from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """文章分类"""
    name = models.CharField(max_length=50, verbose_name='分类名称')
    slug = models.SlugField(unique=True, verbose_name='URL别名')
    description = models.TextField(blank=True, verbose_name='描述')
    order = models.PositiveIntegerField(default=0, verbose_name='排序')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=30, verbose_name='标签名称')
    slug = models.SlugField(unique=True, verbose_name='URL别名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={'slug': self.slug})


class BlogPost(models.Model):
    """博客文章"""
    CATEGORY_CHOICES = [
        ('landscape', '山水意境'),
        ('still_life', '器物特写'),
        ('experimental', '光影实验'),
        ('essay', '随笔'),
    ]

    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(unique=True, verbose_name='URL别名')
    cover_image = models.ImageField(upload_to="covers/", verbose_name='封面图')
    content = models.TextField(verbose_name='内容（Markdown）')
    excerpt = models.TextField(max_length=300, blank=True, verbose_name='摘要')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='分类',
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签', related_name='posts')
    is_photography = models.BooleanField(default=False, verbose_name='是否为摄影作品')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    view_count = models.PositiveIntegerField(default=0, verbose_name='浏览次数')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
