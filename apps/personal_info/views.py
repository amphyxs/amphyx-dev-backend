from rest_framework.viewsets import ModelViewSet

from apps.personal_info.models import ContactLink
from apps.personal_info.serializers import ContactLinkSerializer


class ContactLinkViewSet(ModelViewSet):
    """Viewset для просмотра и редактирования списка ссылок-контактов."""

    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
