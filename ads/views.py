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
    """ Для списка объявлений"""
    queryset = Ad.objects.filter(is_published=True)
    serializer_class = AdSerializer

    def initialize_request(self, request, *args, **kwargs):
        """ Объявления по категориям. """

        # Фильтровать по идентификатору категории
        category = request.GET.getlist("cat", [])
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)

        # Фильтровать по названию обьявлений
        if request.GET.get("text", None):
            self.queryset = self.queryset.filter(name__icontains=request.GET.get("text"))

        # Фильтровать по локации юзера
        if request.GET.get("location", None):
            self.queryset = self.queryset.filter(author__locations__name__icontains=request.GET.get("location"))

        # Фильтровать по цене
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(
                price__gte=price_from
            )
        if price_to:
            self.queryset = self.queryset.filter(
                price__lte=price_to
            )

        return super().initialize_request(request, *args, **kwargs)


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
