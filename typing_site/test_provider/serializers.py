from rest_framework import serializers
from .models import Record, User, TestText
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


USER_MODEL = get_user_model()


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    student_num = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 


    class Meta:
        model = USER_MODEL
        fields = ['first_name', 'last_name', 'student_num', 'username', 'password']
        read_only_fields = ['username']
