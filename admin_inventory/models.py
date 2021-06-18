from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField

from utils.base_model import ModelAbstractBase
from utils.constants import *


class CategoryModel(ModelAbstractBase):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)


class TagModel(ModelAbstractBase):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)


class CollectionModel(ModelAbstractBase):
    organization = models.IntegerField(blank=False)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)


class AdminProductModel(ModelAbstractBase):
    """
        Model: PermissionsModel
        Description: Create PermissionsModel
        Fields:
            title: title of the permission
    """
    type = models.CharField(max_length=20, default=DEFAULT_PRODUCT_TYPE, choices=PRODUCT_TYPES)
    category = models.ManyToManyField(to=CategoryModel)
    is_part_of_collection = models.BooleanField(default=False)
    collection = models.ForeignKey(to=CollectionModel, on_delete=models.SET_NULL, null=True)
    data = JSONField(blank=True, null=True, default=dict)
    images = ArrayField(
        models.URLField(blank=True),
        size=10,
        blank=True,
        default=list
    )
    docs = ArrayField(
        models.URLField(blank=True),
        size=10,
        blank=True,
        default=list
    )
    is_premium = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=TagModel)

    # For products like video, podcast, book, tips
    link = models.URLField(blank=True)
    meta = JSONField(blank=True, null=True, default=dict)
    author = models.CharField(max_length=100)
    time = models.IntegerField(default=0)

    id_deleted = models.BooleanField(default=False)


class AdminProductTranslationModel(ModelAbstractBase):
    product = models.ForeignKey(to=AdminProductModel, related_name='product_translation', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text="title of the product")
    description = models.TextField(blank=True)
    language = models.CharField(max_length=50, blank=True, default='en-US')


class AdminServiceModel(ModelAbstractBase):
    product = models.OneToOneField(to=AdminProductModel, related_name='service', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, blank=True)
    entry_name = models.CharField(max_length=100, blank=True)
