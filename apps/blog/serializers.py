from rest_framework.serializers import ModelSerializer

from apps.blog.models import BlogPost


class BlogPostShortSerializer(ModelSerializer):
    """Сериализатор постов блога для отображения их в списке."""

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'author',
        )
        model = BlogPost


class BlogPostSerializer(ModelSerializer):
    """Сериализатор постов блога с полным набором полей."""

    class Meta:
        fields = '__all__'
        model = BlogPost
