from django.contrib import admin

from apps.blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


admin.site.register(BlogPost, BlogPostAdmin)
