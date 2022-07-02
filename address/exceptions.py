from rest_framework.exceptions import APIException
from rest_framework.views import status


class InvalidCepException(APIException):
    default_detail = {"detail": "Invalid CEP"}
    status_code = status.HTTP_400_BAD_REQUEST
