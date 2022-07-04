import random

from account.utils import cep_verifyer
from faker import Faker
from faker.providers.person import Provider

fake: Provider = Faker()

fake.add_provider(Provider)


cep_list = [
    "57073270",
    "68911044",
    "69037114",
    "63100164",
    "72275454",
    "29190760",
    "72855027",
    "65076909",
    "78060074",
    "79064040",
    "32143572",
    "85901060",
    "58013440",
    "67133126",
    "55614415",
    "64052580",
]



def user_info():
    return {
        "email": fake.unique.email(),
        "password": fake.password(),
        "name": fake.first_name(),
    }


def address_info():
    cep = random.choice(cep_list)
    cep_info = cep_verifyer(cep)
    return {
        "cep": cep,
        "number": random.randint(1, 10000),
        "cidade": cep_info["localidade"],
        "rua": cep_info["logradouro"],
        "uf": cep_info["uf"],
        "bairro": cep_info["bairro"],
    }


def register_user_body():
    cep = random.choice(cep_list)
    cep_info = cep_verifyer(cep)
    return {
        "email": fake.unique.email(),
        "password": fake.password(),
        "name": fake.first_name(),
        "address": {
            "cep": cep,
            "number": random.randint(1, 10000),
            "cidade": cep_info["localidade"],
            "rua": cep_info["logradouro"],
            "uf": cep_info["uf"],
            "bairro": cep_info["bairro"],
        },
    }
