def test_create_item(client):
    list_resp = client.post("/lists/", json={"name": "With Items"})
    list_id = list_resp.json()["id"]
    item_data = {"title": "Test Item", "description": "Test Desc"}
    response = client.post(f"/lists/{list_id}/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"

def test_update_item(client):
    list_resp = client.post("/lists/", json={"name": "ListMod"})
    list_id = list_resp.json()["id"]
    item_resp = client.post(f"/lists/{list_id}/items/", json={"title": "To Update"})
    item_id = item_resp.json()["id"]
    response = client.put(f"/lists/{list_id}/items/{item_id}", json={"title": "Updated"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"

def test_delete_item(client):
    list_resp = client.post("/lists/", json={"name": "ListDel"})
    list_id = list_resp.json()["id"]
    item_resp = client.post(f"/lists/{list_id}/items/", json={"title": "To Delete"})
    item_id = item_resp.json()["id"]
    response = client.delete(f"/lists/{list_id}/items/{item_id}")
    assert response.status_code == 204