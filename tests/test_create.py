from flask import json


def test_create(test_client):

    response = test_client.post('/users', json=dict(
        name='test_create_name',
        password='test_create_name_password'
        ), follow_redirects=True)

    data = json.loads(response.data)
    users = data['user']

    assert response.status_code == 201
    assert users['name'] == 'test_create_name'
    assert users['password'] == 'test_create_name_password'
