from address.exceptions import InvalidCepException
from address.models import Address
from address.serializers import ListCreateAddressSerializer
from rest_framework import serializers

from account.models import User


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class CreateUserSerializer(serializers.ModelSerializer):
    address = ListCreateAddressSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "name", "address", "password"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict):
        address_sended = validated_data.pop("address")
        address = Address.objects.create(**address_sended)
        user = User.objects.create_user(
            **validated_data,
        )
        user.address = address
        user.save()
        return user
