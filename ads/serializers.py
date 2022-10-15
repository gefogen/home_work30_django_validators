from rest_framework import serializers

from ads.models import *


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'