from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from ads.models import Ad
from ads.models import Category
from ads.serializers import AdSerializer, CatSerializer

from django.http import JsonResponse


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


class AdViewSet(viewsets.ModelViewSet):
    """ Выводит список объявлений """
    queryset = Ad.objects.filter(is_published=True)
    serializer_class = AdSerializer


class CatViewPagination(PageNumberPagination):
    """ Пагинация """
    page_size = 2
    page_size_query_param = 'page_size'  # Указываем в запросе. Пример: http://localhost/cat/?page_size=5
    max_page_size = 10  # Максимальное значение для 'page_size'


class CatViewSet(viewsets.ModelViewSet):
    """ Выводит список категорий """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CatSerializer
    pagination_class = CatViewPagination
