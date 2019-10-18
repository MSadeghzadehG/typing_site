from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Record(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=None)
    text = models.TextField(default=None)
    speed = models.FloatField(default=None, null=True)
    wrong_keys = models.IntegerField(default=None, null=True)
    correct_keys = models.IntegerField(default=None, null=True)
    

class TestText(models.Model):
    text = models.TextField(unique=True, blank=False)


class User(AbstractUser):
    username = models.CharField("username", max_length=50, primary_key=True)
    student_num = models.CharField("student number", max_length=8, blank=False)
    first_name = models.CharField("first name", max_length=30, blank=False)
    last_name = models.CharField("last name", max_length=150, blank=False)
    email = models.CharField("email", max_length=150, blank=False)

    REQUIRED_FIELDS = ["student_num", "first_name", "last_name", "email"]

    def __str__(self):
        return "{} - ({})".format(self.get_full_name(), self.get_username())


USER_MODEL = get_user_model()
