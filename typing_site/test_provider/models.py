from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Record(models.Model):
    text = models.ForeignKey("TestText", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    speed = models.FloatField(null=False)
    wrong_keys = models.IntegerField(null=False)
    correct_keys = models.IntegerField(null=False)
    

class TestText(models.Model):
    text = models.TextField(unique=True, blank=False)


class User(AbstractUser):
    student_num = models.CharField("student number", max_length=8, blank=False)
    first_name = models.CharField("first name", max_length=30, blank=False)
    last_name = models.CharField("last name", max_length=150, blank=False)
    # student_num = models.CharField("student number", max_length=150, blank=False)

    REQUIRED_FIELDS = ["student_num", "first_name", "last_name"]

    def __str__(self):
        return "{} - ({})".format(self.get_full_name(), self.get_username())


USER_MODEL = get_user_model()
