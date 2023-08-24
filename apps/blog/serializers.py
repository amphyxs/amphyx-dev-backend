from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostShortSerializer(serializers.ModelSerializer):
    """Сериализатор постов блога для отображения их в списке."""

    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'author',
        )
        model = BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """Сериализатор постов блога с полным набором полей."""

    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        fields = '__all__'
        model = BlogPost
