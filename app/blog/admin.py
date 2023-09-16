from django.contrib import admin

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    """Post model in the admin panel."""

    list_display = ("id", "title", "time_create", "thumbnail", "is_published")
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    """Category model in the admin panel."""

    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
