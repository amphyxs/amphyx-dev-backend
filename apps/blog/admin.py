from django.contrib import admin

from apps.blog.models import BlogPost, BlogPostTag


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title', )}


class BlogPostTagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostTag, BlogPostTagAdmin)
