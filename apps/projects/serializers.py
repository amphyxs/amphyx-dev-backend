from rest_framework import serializers

from apps.projects.models import Project, ProjectTool


class ProjectToolSerializer(serializers.ModelSerializer):
    """Сериализатор инструмента для проекта."""

    class Meta:
        fields = '__all__'
        model = ProjectTool


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор проекта."""

    stack = ProjectToolSerializer(many=True)
    type = serializers.StringRelatedField()
    start_date = serializers.DateField(format='%d.%m.%Y')
    end_date = serializers.DateField(format='%d.%m.%Y')
    key_points = serializers.SerializerMethodField()

    def get_key_points(self, project: Project) -> list[str]:
        """Получить список ключевых моментов проекта."""
        return project.key_points.split(';')

    class Meta:
        fields = '__all__'
        model = Project
