from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField
from admin_inventory.models import CategoryModel
from utils.db.base_model import ModelAbstractBase
from utils.constants import *


class BuilderModel(ModelAbstractBase):
    """
        Model: PermissionsModel
        Description: Create PermissionsModel
        Fields:
            title: title of the permission
    """
    user = models.TextField(blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, help_text="title of the product")
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, default=DEFAULT_PRODUCT_TYPE, choices=PRODUCT_TYPES)
    language = models.CharField(max_length=50, default='en-US')
    category = models.ManyToManyField(to=CategoryModel, blank=True)
    data = JSONField(blank=True, null=True, default=dict)
    # data_backup = JSONField(blank=True, null=True, default=dict)
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

    def __str__(self):
        return str(f"{self.title}")
