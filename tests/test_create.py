from flask import json


def test_create(test_client):

    response = test_client.post('/users', json=dict(
        name='test_create_name',
        password='test_create_name_password'
        ), follow_redirects=True)

    data = json.loads(response.data)

    assert response.status_code == 201
    assert data['user']['name'] == 'test_create_name'
    assert data['user']['password'] == 'test_create_name_password'
