from django.shortcuts import render
from rest_framework import generics
from .models import News
from serializers import NewSerializer

class ListApi(generics.ListAPIView):
      queryset = News.objects.all()
      serializer_class = NewSerializer