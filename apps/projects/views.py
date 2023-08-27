from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets, filters

from apps.common.permissions import IsSuperuser, ReadOnly
from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet для просмотра и редактирования постов в блоге."""

    permission_classes = [IsSuperuser | IsAdminUser | ReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['start_date']
    ordering = ['-start_date']
