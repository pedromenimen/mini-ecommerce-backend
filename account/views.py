from address.exceptions import InvalidCepException
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from account.exceprions import InvalidCredentials
from account.models import User
from account.serielizers import CreateUserSerializer, LoginUserSerializer
from account.utils import cep_verifyer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if not user:
            raise InvalidCredentials

        token = Token.objects.get_or_create(user=user)[0].key

        return Response({"token": token})


class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        address_info = request.data["address"]
        cep = cep_verifyer(address_info["cep"])
        if "erro" in cep.keys():
            raise InvalidCepException
        return super().post(request, *args, **kwargs)
