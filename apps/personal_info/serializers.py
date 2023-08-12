from rest_framework.serializers import ModelSerializer

from apps.personal_info.models import ContactLink


class ContactLinkSerializer(ModelSerializer):
    """Сериализатор для ссылок-контактов."""

    class Meta:
        fields = '__all__'
        model = ContactLink
