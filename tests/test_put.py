from flask import json


def test_put(test_client):

    response = test_client.put('/users/1', json=dict(
        name='test_put_name',
        password='test_put_password'
        ), follow_redirects=True)

    data = json.loads(response.data)

    users = data['user']

    assert response.status_code == 200
    assert users['name'] == 'test_put_name'
    assert users['password'] == 'test_put_password'
