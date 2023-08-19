from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogPost(models.Model):
    """Пост в блоге."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
