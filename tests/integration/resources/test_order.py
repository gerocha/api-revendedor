class TestOrderResource:
    ORDER_ENDPOINT = '/order'

    def test_new_order(self, logged_client):
        rv = logged_client.post(self.ORDER_ENDPOINT, json={
            "code": "bla-123",
            "value": 123.99,
            "date": "11/11/2021",
        })


        assert rv.status_code == 201

    def test_update_order(self, logged_client):
        rv = logged_client.put(self.ORDER_ENDPOINT + '/1', json={
            "code": 'xablau-0123'
        })

        assert rv.status_code == 200

        rv = logged_client.put(self.ORDER_ENDPOINT + '/1', json={
            "status": 'APPROVED'
        })

        assert rv.status_code == 200

        rv = logged_client.put(self.ORDER_ENDPOINT + '/1', json={
            "value": 2.00
        })

        assert rv.status_code == 400

    def test_delete_order(self, client, logged_client):
       rv = client.post(self.ORDER_ENDPOINT, json={
            "code": "bla-123",
            "value": 123.99,
            "date": "11/11/2021",
        })

       rv = logged_client.delete(self.ORDER_ENDPOINT + '/2')

       assert rv.status_code == 200

    def test_get_orders(self, client):
        rv = client.get(self.ORDER_ENDPOINT)

        assert rv.status_code == 200

        assert rv.json
