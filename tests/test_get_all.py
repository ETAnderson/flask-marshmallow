from flask import json


def test_get_all(test_client):
    response = test_client.get('/users')

    data = json.loads(response.data)

    users = data['users']

    assert response.status_code == 200
    assert users[0]['name'] == 'Eric Anderson'
    assert users[0]['password'] == 'testpass2'

    assert users[1]['name'] == 'Rochelle Anderson'
    assert users[1]['password'] == 'Rochellepass'
