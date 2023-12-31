from django.db import models


class ProjectTool(models.Model):
    """Инструмент для проекта."""

    TOOLS_TYPES = (
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('library', 'Library'),
        ('deployment', 'Deployment'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TOOLS_TYPES)

    def __str__(self) -> str:
        return self.name


class ProjectType(models.Model):
    """Тип проекта."""

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    """Проект."""

    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    github_link = models.URLField(null=True, blank=True)
    stack = models.ManyToManyField(to=ProjectTool)
    type = models.ForeignKey(to=ProjectType, on_delete=models.PROTECT)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    key_points = models.TextField()

    def __str__(self) -> str:
        return self.name
