from django.contrib import admin
from apps.personal_info.models import ContactLink


class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ContactLink, ContactLinkAdmin)
