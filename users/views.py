from django.db.models import Count
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from users.models import Location
from users.models import User
from users.serializers import UserSerializer, LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ Для списка пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

    @action(methods=['GET'], detail=False)  # detail - Для списка записей, если True -тогда одна запись.
    def total_ads(self, request):
        """ Cписок пользователей с количеством опубликованных пользователем объявлений"""
        ads = User.objects.annotate(total_ads=Count('ad'))
        return JsonResponse({'Users': [{"id": ad.id,
                                        "username": ad.username,
                                        "total_ads": ad.total_ads,
                                        "locations": list(map(str, ad.location.all()))
                                        } for ad in ads]},
                            json_dumps_params={"ensure_ascii": False})


class LocationViewSet(viewsets.ModelViewSet):
    """ Для списка локаций """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAdminUser, )