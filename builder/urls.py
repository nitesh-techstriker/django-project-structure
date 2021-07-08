from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BuilderView.as_view()),
]
