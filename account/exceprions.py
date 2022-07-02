from rest_framework.exceptions import APIException
from rest_framework.views import status


class InvalidCredentials(APIException):
    default_detail = {"detail": "Invalid credentials."}
    status_code = status.HTTP_401_UNAUTHORIZED
