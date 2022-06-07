import pytest
from redisearch.client import Document
from rest_framework.test import APIClient

LIST_ITEM = [
    {
        "title": "My Title 1",
        "description": "My description goes here 1",
        "image": "http://my-image-url1.com",
    },
    {
        "title": "My Title 2",
        "description": "My description goes here 2",
        "image": "http://my-image-url2.com",
    },
    {
        "title": "My Title 3",
        "description": "My description goes here 3",
        "image": "http://my-image-url3.com",
    },
    {
        "title": "My Title 4",
        "description": "My description goes here 4",
        "image": "http://my-image-url4.com",
    },
    {
        "title": "My Title 5",
        "description": "My description goes here 5",
        "image": "http://my-image-url5.com",
    },
]


@pytest.fixture
def items():
    return [Document(index, **item) for index, item in enumerate(LIST_ITEM)]


@pytest.fixture
def single_item():
    return Document(1, **LIST_ITEM[0])


@pytest.fixture
def not_found():
    return Document(100)


@pytest.fixture
def client():
    return APIClient()
