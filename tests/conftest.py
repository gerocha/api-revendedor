import pytest

@pytest.fixture(scope='session')
def app():
    from api.app import create_app

    app = create_app()
    app.config['TESTING'] = True

    yield app


@pytest.fixture(scope='session')
def client(app):
    from api.app import db

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
