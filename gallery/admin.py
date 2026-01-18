from django.contrib import admin
from .models import PhotoAlbum, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ['title', 'image', 'order', 'camera', 'lens', 'aperture', 'iso']
    readonly_fields = []


@admin.register(PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'theme_color', 'photo_count', 'is_featured', 'created_at']
    list_filter = ['theme_color', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoInline]
    date_hierarchy = 'created_at'

    def photo_count(self, obj):
        return obj.photo_count
    photo_count.short_description = '照片数量'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'thumbnail_preview', 'location', 'date_taken', 'camera', 'order']
    list_filter = ['album', 'date_taken', 'created_at', 'camera']
    search_fields = ['title', 'description', 'location']
    list_editable = ['order']
    readonly_fields = ['thumbnail_preview', 'created_at']
    date_hierarchy = 'date_taken'

    fieldsets = (
        ('基本信息', {
            'fields': ('album', 'title', 'image', 'thumbnail_preview', 'order')
        }),
        ('描述', {
            'fields': ('description', 'location', 'date_taken')
        }),
        ('EXIF 信息', {
            'fields': ('camera', 'lens', 'focal_length', 'aperture', 'shutter_speed', 'iso', 'exif_data'),
            'classes': ('collapse',),
        }),
        ('时间', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.image.url)
        return "无图片"
    thumbnail_preview.short_description = '预览'
