from account.utils import cep_verifyer
from rest_framework import serializers

from address.exceptions import InvalidCepException
from address.models import Address


class ListCreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "cep", "number", "cidade", "rua", "uf", "bairro"]

    def validate(self, attrs):
        cep = cep_verifyer(attrs["cep"])
        if hasattr(cep, "error"):
            raise InvalidCepException
        return super().validate(attrs)
