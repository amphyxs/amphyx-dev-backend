from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostShortSerializer(serializers.ModelSerializer):
    """Сериализатор постов блога для отображения их в списке."""

    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    tags = serializers.StringRelatedField(many=True)
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }

    class Meta:
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'author',
            'tags',
            'slug',
        )
        model = BlogPost


class BlogPostSerializer(BlogPostShortSerializer):
    """Сериализатор постов блога с полным набором полей."""

    class Meta:
        fields = '__all__'
        model = BlogPost
