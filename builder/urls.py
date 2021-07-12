from django.urls import path, include
from .views import *
from django.urls import path, include
from .views.admin_builder import *
from .views.user_builder import *

urlpatterns = [
    # Admin Builder

    path('admin-builder/', ProductView.as_view()),
    path('admin-builder/category/', CategoryView.as_view()),
    path('admin-builder/tag/', TagView.as_view()),

    # User Builder

    path('user-builder/', BuilderView.as_view()),
]
