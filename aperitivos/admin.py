from django.contrib.admin import ModelAdmin, register

from aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("titulo", "creation", "vimeo_id")
    ordering = ("creation",)
    prepopulated_fields = {"slug": ("titulo",)}
