def test_create_list(client):
    response = client.post("/lists/", json={"name": "Test List"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test List"

def test_update_list(client):
    response = client.post("/lists/", json={"name": "Old Name"})
    list_id = response.json()["id"]
    response = client.put(f"/lists/{list_id}", json={"name": "New Name"})
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"

def test_delete_list(client):
    response = client.post("/lists/", json={"name": "To Delete"})
    list_id = response.json()["id"]
    response = client.delete(f"/lists/{list_id}")
    assert response.status_code == 204