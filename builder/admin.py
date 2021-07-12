from django.contrib import admin
from builder.models.admin_builder import *
from builder.models.user_builder import *

admin.site.site_header = "MYCVFACTORY ADMIN"
admin.site.site_title = "MYCVFACTORY Admin Portal"
admin.site.index_title = "Welcome to MyCvFactory Portal"

admin.site.register(AdminProductModel)
admin.site.register(AdminProductTranslationModel)
admin.site.register(AdminServiceModel)
admin.site.register(TagModel)
admin.site.register(CategoryModel)
admin.site.register(CollectionModel)

admin.site.register(BuilderModel)
