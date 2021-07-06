import django_filters
from admin_inventory.models import AdminProductModel
from django.db.models import Q
from admin_inventory.serializers import AdminProductTranslationSerializer
from utils.common import *
from rest_framework import serializers
from admin_inventory.models import *


class BaseUserFilter(serializers.ModelSerializer):
    product_translation = AdminProductTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = AdminProductModel
        fields = ('id', 'type', 'category', 'is_part_of_collection', 'data', 'images', 'docs', 'is_published',
                  'product_translation')


def get_product(input_data):
    query = Q()

    if 'id' in input_data and input_data['id']:
        query &= Q(id=input_data['id'])

    if 'keyword' in input_data and input_data['keyword']:
        query &= Q(product_translation__title__icontains=input_data['keyword'])

    return generate_response(product_list(filters=query))


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


def product_list(*, filters=None):
    qs = AdminProductModel.objects.all()
    return BaseUserFilter(filters, qs).qs