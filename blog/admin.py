from django.contrib import admin
from .models import BlogPost, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_photography', 'is_published', 'view_count', 'created_at']
    list_filter = ['is_published', 'is_photography', 'category', 'tags', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_published', 'is_photography']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    readonly_fields = ['view_count', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'slug', 'cover_image', 'excerpt')
        }),
        ('分类与标签', {
            'fields': ('category', 'tags')
        }),
        ('内容', {
            'fields': ('content',)
        }),
        ('设置', {
            'fields': ('is_photography', 'is_published')
        }),
        ('统计信息', {
            'fields': ('view_count', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
