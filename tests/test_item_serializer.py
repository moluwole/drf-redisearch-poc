from api.serializer import ItemSerializer


def test_valid_item_serializer():
    valid_data = {
        "id": 1,
        "title": "My title here",
        "image": "http://imageurl.com",
        "description": "Super long description here",
    }

    serializer = ItemSerializer(data=valid_data)
    assert serializer.is_valid()
    assert serializer.errors == {}


def test_serializer_no_title():
    invalid_data = {
        "id": 2,
        "image": "http://imageurl.com",
        "description": "My description",
    }

    serializer = ItemSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.errors == {"title": ["This field is required."]}


def test_serializer_invalid_image_url():
    invalid_data = {
        "id": 3,
        "title": "My Title",
        "image": "invalid-url",
        "description": "Super long description",
    }
    serializer = ItemSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert serializer.errors == {"image": ["Enter a valid URL."]}
