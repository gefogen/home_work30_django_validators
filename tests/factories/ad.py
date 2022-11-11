import factory

from ads.models import Ad
from .category import CategoryFactory
from .user import UserFactory


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Тест не менее 10 символов"
    price = 1000

    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)