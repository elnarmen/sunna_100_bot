from bot.models import Interval, Post
from django.contrib import admin
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["text", "get_image_preview"]

    def get_image_preview(self, img_obj):
        return format_html('<img src={} height="200"', img_obj.image.url)

    get_image_preview.short_description = "Изображение"  # type: ignore


@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = ["hours"]
