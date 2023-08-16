from rest_framework.serializers import ModelSerializer

from apps.personal_info.models import ContactLink


class ContactLinkSerializer(ModelSerializer):
    """Сериализатор для ссылок-контактов."""

    class Meta:
        fields = '__all__'
        model = ContactLink


class HireLinkSerializer(ModelSerializer):
    """Сериализатор ссылок для найма."""

    class Meta:
        fields = (
            'id',
            'name',
            'url',
            'icon_name',
        )
        model = ContactLink

    def create(self, validated_data: dict) -> ContactLink:
        """Добавление галочки `is_for_hire`."""
        validated_data['is_for_hire'] = True
        return super().create(validated_data)
