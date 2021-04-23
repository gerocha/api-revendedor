import pytest
from flask_jwt_extended import create_access_token


@pytest.fixture
def logged_client(app, client):
    with app.app_context():
        access_token = create_access_token(identity='12312312312')
        client.environ_base['HTTP_AUTHORIZATION'] = 'Bearer ' + access_token
    yield client
