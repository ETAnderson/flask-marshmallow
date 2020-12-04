from flask import json


def test_get_by_id(test_client):
    response = test_client.get('/users/1')

    data = json.loads(response.data)

    users = data['user']

    assert response.status_code == 200
    assert users['name'] == 'Eric Anderson'
    assert users['password'] == 'testpass2'
