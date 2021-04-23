class TestCashbackResource:
    CASHBACK_ENDPOINT = '/cashback'

    def test_get_document_cashback(self, client):
        rv = client.get(self.CASHBACK_ENDPOINT)


        assert rv.status_code == 200
        assert 'credit' in rv.json['body']
