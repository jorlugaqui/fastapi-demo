from fastapi.testclient import TestClient
from main import app, STUDENTS_DB

client = TestClient(app)


def test_get_developers():
    response = client.get('/api/v1/developers/')
    assert 200 == response.status_code

    data = response.json()
    assert 'developers' in data
    assert len(data.get('developers', [])) > 0


def test_get_developer_by_index():
    index = 1
    response = client.get(f'/api/v1/developers/{index}')
    assert 200 == response.status_code

    data = response.json()
    assert data.get('developer') is not None
    assert data.get('developer') == STUDENTS_DB[index]


def test_get_developer_by_index_default():
    # This index is too big and thus the app should return the
    # first student
    index = 5
    response = client.get(f'/api/v1/developers/{index}')
    assert 200 == response.status_code

    data = response.json()
    assert data.get('developer') is not None
    assert data.get('developer') == STUDENTS_DB[0]


def test_get_developer_random():
    response = client.get('/api/v1/developers/random')
    assert 200 == response.status_code

    data = response.json()
    assert data.get('developer') is not None
