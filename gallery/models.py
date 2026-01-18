from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class PhotoAlbum(models.Model):
    """相册"""
    THEME_COLOR_CHOICES = [
        ('#3C4856', '鸦青'),
        ('#B78B5D', '琥珀'),
        ('#2A5CAA', '黛蓝'),
        ('#D03B40', '朱砂'),
    ]

    title = models.CharField(max_length=100, verbose_name='相册名称')
    slug = models.SlugField(unique=True, verbose_name='URL别名')
    description = models.TextField(blank=True, verbose_name='描述')
    theme_color = models.CharField(
        max_length=7,
        choices=THEME_COLOR_CHOICES,
        default='#3C4856',
        verbose_name='主题色'
    )
    cover_photo = models.ForeignKey(
        'Photo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='album_cover',
        verbose_name='封面照片'
    )
    created_at = models.DateField(auto_now_add=True, verbose_name='创建日期')
    is_featured = models.BooleanField(default=False, verbose_name='是否精选')

    class Meta:
        verbose_name = '相册'
        verbose_name_plural = '相册'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'slug': self.slug})

    @property
    def photo_count(self):
        return self.photos.count()


class Photo(models.Model):
    """照片"""
    album = models.ForeignKey(
        PhotoAlbum,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='相册'
    )
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to="gallery/%Y/%m/", verbose_name='图片')
    # 缩略图规格
    thumbnail_square = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 80}
    )
    thumbnail_large = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1200, 800)],
        format='JPEG',
        options={'quality': 90}
    )
    description = models.TextField(blank=True, verbose_name='描述')
    location = models.CharField(max_length=100, blank=True, verbose_name='拍摄地点')
    date_taken = models.DateField(blank=True, null=True, verbose_name='拍摄日期')

    # EXIF 数据字段
    camera = models.CharField(max_length=50, blank=True, verbose_name='相机')
    lens = models.CharField(max_length=50, blank=True, verbose_name='镜头')
    focal_length = models.CharField(max_length=20, blank=True, verbose_name='焦距')
    aperture = models.CharField(max_length=10, blank=True, verbose_name='光圈')
    shutter_speed = models.CharField(max_length=20, blank=True, verbose_name='快门速度')
    iso = models.CharField(max_length=10, blank=True, verbose_name='ISO')
    exif_data = models.JSONField(null=True, blank=True, verbose_name='完整EXIF数据')

    order = models.PositiveIntegerField(default=0, verbose_name='排序')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = '照片'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_exif_display(self):
        """返回格式化的EXIF信息用于显示"""
        exif_parts = []
        if self.camera:
            exif_parts.append(self.camera)
        if self.lens:
            exif_parts.append(self.lens)
        if self.focal_length:
            exif_parts.append(self.focal_length)
        if self.aperture:
            exif_parts.append(f"f/{self.aperture}")
        if self.shutter_speed:
            exif_parts.append(f"{self.shutter_speed}s")
        if self.iso:
            exif_parts.append(f"ISO {self.iso}")
        return " | ".join(exif_parts) if exif_parts else "无EXIF信息"
