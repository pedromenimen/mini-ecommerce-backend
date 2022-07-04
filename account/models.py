from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from .utils import CustomUserManager


class User(AbstractUser):
    class Meta:
        db_table = "accounts"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=150, null=False)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=255)
    username = models.CharField(unique=False, null=True, max_length=255)

    address = models.ForeignKey(
        "address.Address", on_delete=models.CASCADE, related_name="users", null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.name
