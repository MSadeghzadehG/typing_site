from rest_framework import serializers
from .models import Test, Record, User
from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = ['first_name', 'last_name', 'email', 'username']
        read_only_fields = ['username']
