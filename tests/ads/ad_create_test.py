import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):
    expected_response = {
        "id": user.pk,
        "image": None,
        "name": "Тест не менее 10 символов",
        "price": 2500,
        "author": None,
        "category": None,
        "is_published": False,
        "description": "Описание теста"
    }

    data = {
        "author_id": user.pk,
        "name": "Тест не менее 10 символов",
        "price": 2500,
        "description": "Описание теста",
        "is_published": False,
        "category_id": category.pk
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response
