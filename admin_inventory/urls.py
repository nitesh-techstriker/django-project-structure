from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('tag/', TagView.as_view()),
]
