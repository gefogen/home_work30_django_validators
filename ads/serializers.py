from rest_framework import serializers

from ads.models import Ad
from ads.models import Category
from users.models import User


class AdSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
