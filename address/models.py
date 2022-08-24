from uuid import uuid4

from django.core.validators import MinLengthValidator
from django.db import models


class Address(models.Model):
    class Meta:
        db_table = "addresses"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cep = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    number = models.CharField(max_length=15)
    cidade = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    bairro = models.CharField(max_length=255)

    def __str__(self):
        return self.cep
