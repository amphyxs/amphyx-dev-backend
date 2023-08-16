"""Общие классы доступа."""

from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import HttpRequest
from rest_framework.views import View


class IsSuperuser(BasePermission):
    """Суперпользователь ли."""

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        user = request.user

        return user.is_superuser


class ReadOnly(BasePermission):
    """Доступ только для чтения."""

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        return request.method in SAFE_METHODS
