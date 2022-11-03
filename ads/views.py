from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from ads.permissions.selection import IsCreatedBy
from ads.models import Ad, Category, Selection
from ads.serializers import AdSerializer, AdCreateSerializer, AdUpdateSerializer, AdImageSerializer, CatSerializer, \
    SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer

from django.http import JsonResponse


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


class AdListView(ListAPIView):
    """ Только для авторизованых пользователей"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ Объявления по категориям. """

        # Фильтровать по идентификатору категории
        category = request.GET.getlist("cat", [])
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)

        # Фильтровать по названию обьявлений
        if request.GET.get("text", None):
            self.queryset = self.queryset.filter(name__icontains=request.GET.get("text"))

        # Filter by user location
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

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """Только для авторизованых пользователей"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    """Создать новое объявление"""
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class IsCreatedByOrAdminOrModerator:
    pass


class AdUpdateView(UpdateAPIView):
    """Обновить объявление по id"""
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdDeleteView(DestroyAPIView):
    """Удалить обьявление по id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class CatViewPagination(PageNumberPagination):
    """ Для категорий свой класс пагинации"""
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CatViewSet(viewsets.ModelViewSet):
    """ Для списка категорий"""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CatSerializer
    pagination_class = CatViewPagination
    permission_classes = [IsCreatedByOrAdminOrModerator]


class SelectionListView(ListAPIView):
    """Отобразить все выборки"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    """Показать выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    """Создать новый выборку"""
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Обновить выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]


class SelectionDeleteView(DestroyAPIView):
    """Удалить выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]
