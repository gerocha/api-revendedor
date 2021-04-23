from werkzeug.datastructures import Headers


class TestDealerResource:
    DEALER_ENDPOINT = '/dealer'
    AUTH_ENDPOINT = '/auth'

    def test_call_endpoint_with_missing_params(self, client):
        rv = client.post(self.DEALER_ENDPOINT, json={})

        assert rv.status_code == 400
        assert 'document' in rv.json['message']
        assert 'email' in rv.json['message']
        assert 'full_name' in rv.json['message']
        assert 'password' in rv.json['message']

    def test_create_dealer_with_righ_parameters(self, client):
        rv = client.post(self.DEALER_ENDPOINT, json={
            "document": "11111",
            "full_name": "maria xiquinha",
            "email": "m.xiqui@test.com",
            "password": "123456"
        })


        assert rv.status_code == 201
        assert 'id' in rv.json

    def test_auth_with_success(self, client):
        rv = client.post(self.AUTH_ENDPOINT, json={
            "email": "m.xiqui@test.com",
            "password": "123456"
        })


        assert rv.status_code == 200
        assert 'access_token' in rv.json
