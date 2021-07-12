from rest_framework.serializers import Serializer, ModelSerializer
from builder.models.admin_builder import *


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = AdminServiceModel
        fields = ['product', 'service_type', 'entry_name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['type', 'title', 'description']


class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['type', 'title', 'description']


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
        tags, categories = [], []
        if 'tags' in validated_data and type(validated_data['tags']) is list:
            tags = validated_data['tags']
        if 'category' in validated_data and type(validated_data['category']) is list:
            categories = validated_data['category']
        validated_data.pop('category')
        validated_data.pop('tags')
        product = AdminProductModel.objects.create(**validated_data)
        for tag in tags:
            product.tags.add(tag)
        for category in categories:
            product.category.add(category)

        return product
