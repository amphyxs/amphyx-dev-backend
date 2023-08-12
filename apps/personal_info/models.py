from django.db import models


class ContactLink(models.Model):
    """Ссылка для связи."""

    name = models.CharField(max_length=50)
    url = models.URLField()
    icon_name = models.CharField(max_length=50)
