from django.contrib import admin

from apps.projects.models import Project, ProjectTool, ProjectType


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjectToolAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTool, ProjectToolAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
