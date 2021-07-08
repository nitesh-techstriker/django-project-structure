from django.contrib import admin
from builder.models import *

admin.site.site_header = "MYCVFACTORY ADMIN"
admin.site.site_title = "MYCVFACTORY Admin Portal"
admin.site.index_title = "Welcome to MyCvFactory Portal"

admin.site.register(BuilderModel)