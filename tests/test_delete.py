
def test_delete(test_client):

    response = test_client.delete('/users/1')

    assert response.status_code == 204
