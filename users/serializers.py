from rest_framework import serializers

from users.models import Location
from users.models import User
from validators.users import EmailDomainValidator


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailDomainValidator('rambler.ru')])

    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]
