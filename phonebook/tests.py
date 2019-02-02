from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .views import ContactsList

import json
class TestViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ContactsList.as_view()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.endpoint = '/phonebook/'

    @staticmethod
    def setup_user():
        User = get_user_model()

        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
          request = self.factory.get(self.endpoint,
                HTTP_AUTHORIZATION='Token {}'.format(self.token.key))

          request.user = self.user
          response = self.view(request)
          self.assertEqual(response.status_code, 200,
                'Expected Response Code 200, received {0} instead.'
                .format(response.status_code))
    #
    def test_post(self):
        self.client.login(username="test", password="test")
        params = {
            "contact_name": "qwerty",
            "email": "qwerty@gmail.com"
        }
        request = self.factory.post(self.endpoint,params,
                                   HTTP_AUTHORIZATION='Token {}'.format(self.token.key))

        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
    #     client = APIClient
    #     client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    #     response = client.get(self.endpoint)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.render().content)['results']