from rest_framework.serializers import Serializer, ModelSerializer
from .models import *


class BuilderSerializer(ModelSerializer):
    class Meta:
        model = BuilderModel
        fields = '__all__'

    # def create(self, validated_data):
    #     pass
