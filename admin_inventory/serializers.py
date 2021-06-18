from rest_framework.serializers import Serializer, ModelSerializer
from .models import *


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = AdminServiceModel
        fields = ['product', 'service_type', 'entry_name']


class AdminProductTranslationSerializer(ModelSerializer):
    class Meta:
        model = AdminProductTranslationModel
        fields = ['product', 'title', 'description', 'language']


class ProductSerializer(ModelSerializer):
    product_translation = AdminProductTranslationSerializer(many=True, read_only=True)
    # service = ServiceSerializer(blank=True, null=True)

    class Meta:
        model = AdminProductModel
        fields = ['id', 'type', 'category', 'is_part_of_collection', 'collection', 'data', 'images', 'docs',
                  'is_premium', 'is_published', 'tags', 'product_translation']

    def create(self, validated_data):
        product = AdminProductModel.objects.create(**validated_data)
        product_translation_data = validated_data['product_translation']
        AdminProductTranslationModel.objects.create(product=product, **product_translation_data)

        if validated_data['type'] == SERVICE_TYPE:
            if 'service' in validated_data and validated_data['service']:
                service_data = validated_data['service']
                AdminServiceModel.objects.create(product=product, **service_data)

        return product
