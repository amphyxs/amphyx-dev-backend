from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from apps.common.permissions import IsSuperuser, ReadOnly

from apps.personal_info.models import ContactLink
from apps.personal_info.serializers import ContactLinkSerializer


class ContactLinkViewSet(ModelViewSet):
    """ViewSet для просмотра и редактирования списка ссылок-контактов."""

    permission_classes = [IsSuperuser | IsAdminUser | ReadOnly]
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
