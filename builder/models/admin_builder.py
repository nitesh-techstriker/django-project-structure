from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField

from utils.db.base_model import ModelAbstractBase
from utils.constants import *


class CategoryModel(ModelAbstractBase):
    type = models.CharField(max_length=20, default=DEFAULT_PRODUCT_TYPE, choices=PRODUCT_TYPES)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(f"{self.title} - {self.type}")


class TagModel(ModelAbstractBase):
    type = models.CharField(max_length=20, default=DEFAULT_PRODUCT_TYPE, choices=PRODUCT_TYPES)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(f"{self.title} - {self.type}")


class CollectionModel(ModelAbstractBase):
    organization = models.IntegerField(blank=False)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(f"{self.title}")


class AdminProductModel(ModelAbstractBase):
    """
        Model: PermissionsModel
        Description: Create PermissionsModel
        Fields:
            title: title of the permission
    """
    type = models.CharField(max_length=20, default=DEFAULT_PRODUCT_TYPE, choices=PRODUCT_TYPES)
    category = models.ManyToManyField(to=CategoryModel, blank=True)
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
    tags = models.ManyToManyField(to=TagModel, blank=True)

    # For products like video, podcast, book, tips
    link = models.URLField(blank=True)
    meta = JSONField(blank=True, null=True, default=dict)
    author = models.CharField(max_length=100)
    time = models.IntegerField(default=0)

    id_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(f"{self.type}")


class AdminProductTranslationModel(ModelAbstractBase):
    product = models.ForeignKey(to=AdminProductModel, related_name='product_translation', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, help_text="title of the product", name='title', verbose_name='title')
    description = models.TextField(blank=True)
    language = models.CharField(max_length=50, blank=True, default='en-US')

    def __str__(self):
        return str(f"{self.product.type} - {self.title}")


class AdminServiceModel(ModelAbstractBase):
    product = models.OneToOneField(to=AdminProductModel, related_name='service', on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, blank=True)
    entry_name = models.CharField(max_length=100, blank=True)
