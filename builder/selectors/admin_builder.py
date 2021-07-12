import django_filters
from builder.models.admin_builder import AdminProductModel
from django.db.models import Q
from builder.serializers.admin_builder import *
from utils.common import *
from rest_framework import serializers
from builder.models.user_builder import *


class ProductFilter(serializers.ModelSerializer):
    product_translation = AdminProductTranslationSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = AdminProductModel
        fields = ('id', 'type', 'is_part_of_collection', 'data', 'images', 'docs', 'is_published',
                  'product_translation', 'category')


def get_product(input_data):
    query = Q()
    many = True
    if 'id' in input_data and input_data['id']:
        query &= Q(id=input_data['id'])
        many = False

    if 'type' in input_data and input_data['type']:
        query &= Q(type=input_data['type'])

    if 'keyword' in input_data and input_data['keyword']:
        query &= Q(product_translation__title__icontains=input_data['keyword'])

    if 'id' in input_data:
        qs = AdminProductModel.objects.filter(query).last()
    else:
        qs = AdminProductModel.objects.filter(query)

    slz = ProductFilter(qs, many=many)
    return generate_response(slz.data)


def get_category(input_data):
    query = Q()

    if 'type' in input_data and input_data['type']:
        query &= Q(type=input_data['type'])
    if 'id' in input_data and input_data['id']:
        query &= Q(id=input_data['id'])

    return generate_response(data=list(CategoryModel.objects.filter(query).values()))


def get_tag(input_data):
    query = Q()

    if 'type' in input_data and input_data['type']:
        query &= Q(type=input_data['type'])
    if 'id' in input_data and input_data['id']:
        query &= Q(id=input_data['id'])

    return generate_response(data=list(TagModel.objects.filter(query).values()))
