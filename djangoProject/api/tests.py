from rest_framework.test import APITestCase


class NicknameTests(APITestCase):
    def test_name_correct(self):
        url = 'https://127.0.0.1:8000/api/mail'
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "mail": "mail",
            "name": "[]",
        })
