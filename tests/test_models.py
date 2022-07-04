from account.models import User
from address.models import Address
from django.test import TestCase

from tests.mocks import address_info, user_info


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_info = user_info()
        cls.address_info = address_info()

    def test_if_user_can_be_created_with_address(self):
        address: Address = Address.objects.create(**self.address_info)
        user: User = User.objects.create_user(**self.user_info, address=address)
        self.assertEqual(user.email, self.user_info["email"])
        self.assertEqual(user.name, self.user_info["name"])
        self.assertEqual(user.address, address)
        self.assertEqual(address.cep, self.address_info["cep"])
        self.assertEqual(address.bairro, self.address_info["bairro"])
        self.assertEqual(address.cidade, self.address_info["cidade"])
        self.assertEqual(address.rua, self.address_info["rua"])
        self.assertEqual(address.uf, self.address_info["uf"])
