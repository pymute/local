from django.urls import path
from .views import ListApi

urlpatterns = [
    path('',ListApi.as_view())
]