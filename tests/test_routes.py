from account.models import User
from address.models import Address
from rest_framework.test import APITestCase
from rest_framework.views import status

from tests.mocks import register_user_body, user_info


class ModelTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.register_user_body = register_user_body()
        cls.baseUrl = "http://127.0.0.1:8000/api/"
        cls.user_info = user_info()

    def test_if_register_user_route_works_as_expected(self):
        response = self.client.post(
            f"{self.baseUrl}users/register/", self.register_user_body, format="json"
        )
        user: User = User.objects.all().first()
        address: Address = Address.objects.all().first()
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["email"], user.email)
        self.assertEqual(response.json()["address"]["cep"], address.cep)
        self.assertEqual(response.json()["address"]["number"], address.number)
        self.assertEqual(response.json()["address"]["cidade"], address.cidade)
        self.assertEqual(response.json()["address"]["rua"], address.rua)
        self.assertEqual(response.json()["address"]["uf"], address.uf)
        self.assertEqual(response.json()["address"]["bairro"], address.bairro)

    def test_if_user_cant_register_with_short_password(self):
        register_user_body = self.register_user_body
        register_user_body["password"] = 123456
        response = self.client.post(
            f"{self.baseUrl}users/register/", register_user_body, format="json"
        )

        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.json())
        self.assertEqual(
            response.json()["password"],
            ["Ensure this field has at least 8 characters."],
        )
        self.assertEqual(len(User.objects.all()), 0)

    def test_if_user_can_login(self):
        User.objects.create_user(**self.user_info)
        response = self.client.post(
            f"{self.baseUrl}users/login/",
            {
                "email": self.user_info["email"],
                "password": self.user_info["password"],
            },
            format="json",
        )

        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.json())
        self.assertIsInstance(response.json()["token"], str)
        
    def test_if_user_cant_login_with_wrong_credentials(self):
        User.objects.create_user(**self.user_info)
        response = self.client.post(
            f"{self.baseUrl}users/login/",
            {
                "email": "emailerrado@mail.com",
                "password": "senhaerrada@1234",
            },
            format="json",
        )

        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.json())
        self.assertEqual(response.json()["detail"], "Invalid credentials.")
