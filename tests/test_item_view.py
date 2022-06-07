def test_get_items(client, items, mocker):
    get_items_mock = mocker.patch(
        "api.views.get_all_items_from_cache", return_value=[items, 5]
    )

    resp = client.get("/api/items/")
    get_items_mock.assert_called_once()
    assert resp.status_code == 200

    result = resp.json()

    assert int(result["total"]) == 5
    assert len(result["items"]) == int(result["total"])


def test_get_single_item(mocker, client, single_item):
    get_single_item_mock = mocker.patch(
        "api.views.get_single_item", return_value=single_item
    )

    resp = client.get("/api/items/1")
    get_single_item_mock.assert_called_once()
    assert resp.status_code == 200

    result = resp.json()
    assert result["id"] == 1
    assert result["title"] == "My Title 1"
    assert result["image"] == "http://my-image-url1.com"


def test_get_single_item_not_found(mocker, client, not_found):
    get_single_item_mock = mocker.patch(
        "api.views.get_single_item", return_value=not_found
    )

    resp = client.get("/api/items/100")
    get_single_item_mock.assert_called_once()
    assert resp.status_code == 404
