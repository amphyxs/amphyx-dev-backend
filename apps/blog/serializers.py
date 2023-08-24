from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostShortSerializer(serializers.ModelSerializer):
    """Сериализатор постов блога для отображения их в списке."""

    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'author',
            'tags',
        )
        model = BlogPost


class BlogPostSerializer(BlogPostShortSerializer):
    """Сериализатор постов блога с полным набором полей."""

    class Meta:
        fields = '__all__'
        model = BlogPost
