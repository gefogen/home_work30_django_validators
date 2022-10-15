# from django.http import JsonResponse
# from django.shortcuts import render
#
#
# def root(request):
#     return JsonResponse({
#         "status": "ok"
#     })


from rest_framework import generics
from ads.serializers import *


class AdsAPIList(generics.ListCreateAPIView):
    """ Получение всех постов (GET), и создание списка (POST) """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdAPIUpdate(generics.RetrieveUpdateAPIView):
    """ Чтение и изменение поста отдельной записи (GET - и POST - запросы) """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CatsAPIList(generics.ListCreateAPIView):
    """ Получение всех категорий (GET), и создание списка (POST) """
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatAPIUpdate(generics.RetrieveUpdateAPIView):
    """ Получение одной категорий (GET), и создание списка (POST) """
    queryset = Category.objects.all()
    serializer_class = CatSerializer
