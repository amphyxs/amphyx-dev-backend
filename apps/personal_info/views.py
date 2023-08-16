from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsSuperuser, ReadOnly
from apps.personal_info.models import ContactLink
from apps.personal_info.serializers import (
    ContactLinkSerializer,
    HireLinkSerializer
)


class ContactLinkViewSet(ModelViewSet):
    """ViewSet для просмотра и редактирования списка ссылок-контактов."""

    permission_classes = [IsSuperuser | IsAdminUser | ReadOnly]
    queryset = ContactLink.objects.filter(is_for_hire=False)
    serializer_class = ContactLinkSerializer


class HireLinkViewSet(ModelViewSet):
    """ViewSet для просмотра и редактирования списка ссылок для найма."""

    permission_classes = [IsSuperuser | IsAdminUser | ReadOnly]
    queryset = ContactLink.objects.filter(is_for_hire=True)
    serializer_class = HireLinkSerializer
