import django_filters
from builder.models.admin_builder import AdminProductModel
from django.db.models import Q
from builder.serializers.admin_builder import AdminProductTranslationSerializer
from utils.common import *
from rest_framework import serializers
from builder.models.user_builder import *


class BuilderFilter(serializers.ModelSerializer):
    class Meta:
        model = BuilderModel
        fields = ('id','title','description', 'language', 'category', 'type', 'data', 'images', 'docs')


def get_builder(input_data):
    query = Q()
    many = True

    if 'user' in input_data and input_data['user']:
        query &= Q(user=input_data['user'])

    if 'id' in input_data and input_data['id']:
        query &= Q(id=input_data['id'])
        many = False

    if 'type' in input_data and input_data['type']:
        query &= Q(type=input_data['type'])

    if 'keyword' in input_data and input_data['keyword']:
        query &= Q(title__icontains=input_data['keyword'])

    if 'id' in input_data:
        qs = BuilderModel.objects.filter(query).last()
    else:
        qs = BuilderModel.objects.filter(query)

    slz = BuilderFilter(qs, many=many)
    return generate_response(slz.data)
