from django.db import models


class ContactLink(models.Model):
    """Ссылка для связи."""

    name = models.CharField(max_length=50, verbose_name='Name')
    url = models.URLField(verbose_name='URL')
    icon_name = models.CharField(max_length=50, verbose_name='Icon name')
    is_for_hire = models.BooleanField(default=False, verbose_name='For hire')
