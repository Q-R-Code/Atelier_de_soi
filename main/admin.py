"""Allows you to display NewsPost in the Django admin page"""

from django.contrib import admin

from .models import NewsPost


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published", )