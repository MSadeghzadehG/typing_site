from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUsercd


class User(AbstractUser):
    email = models.EmailField("email address", max_length=150, blank=False)
    first_name = models.CharField("first name", max_length=30, blank=False)
    last_name = models.CharField("last name", max_length=150, blank=False)

    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return "{} - ({})".format(self.get_full_name(), self.get_username())


USER_MODEL = get_user_model()
