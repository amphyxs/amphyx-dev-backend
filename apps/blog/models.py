from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogPostTag(models.Model):
    """Тег для поста в блоге."""

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    """Пост в блоге."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(to=BlogPostTag)

    def __str__(self) -> str:
        return self.title
