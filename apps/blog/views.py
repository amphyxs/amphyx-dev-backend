from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from apps.blog.models import BlogPost
from apps.blog.serializers import BlogPostSerializer, BlogPostShortSerializer

from apps.common.permissions import IsSuperuser, ReadOnly


class BlogPostViewSet(viewsets.ModelViewSet):
    """ViewSet для просмотра и редактирования постов в блоге."""

    permission_classes = [IsSuperuser | IsAdminUser | ReadOnly]
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'

    def list(self, *args, **kwargs):
        self.serializer_class = BlogPostShortSerializer
        return super().list(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.serializer_class = BlogPostShortSerializer
        return super().create(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        self.serializer_class = BlogPostSerializer
        return super().retrieve(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.serializer_class = BlogPostSerializer
        return super().update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        self.serializer_class = BlogPostSerializer
        return super().destroy(*args, **kwargs)
