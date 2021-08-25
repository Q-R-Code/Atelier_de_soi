from django.contrib import admin

from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published", )



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created_on')
    list_filter = ('author','created_on')
    search_fields = ('author', 'content')


