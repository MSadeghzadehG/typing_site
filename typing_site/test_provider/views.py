from rest_framework.views import APIView, View
from rest_framework import generics, status, parsers
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import RecordSerializer, UserSerializer
from .models import Record, User, TestText
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotAcceptable, PermissionDenied, ValidationError

from django.db.models.aggregates import Count
from random import randint


class Records(generics.ListCreateAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.kwargs:
            record_id = str(self.kwargs['id'])
            get_object_or_404(Record, id=record_id)
            return Record.objects.filter(id=record_id)
        return Record.objects.all()

    def perform_create(self, serializer):
        if self.kwargs:
            record_id = str(self.kwargs['id'])
            record = get_object_or_404(Record, id=record_id)
            if record.user == self.request.user:
                if record.speed is None:
                    print(serializer.validated_data)
                    if serializer.validated_data.keys() >= {"wrong_keys", "correct_keys", "speed"}:
                        Record.objects.filter(id=record_id).update(**serializer.validated_data)
                    else:
                        raise ValidationError("not enough data")
                else:
                    raise NotAcceptable("the record has been saved")
            else:
                raise PermissionDenied("the record was created for another user")
        else:
            user = self.request.user
            count = len(TestText.objects.all())
            random_index = randint(0, count - 1)
            text = TestText.objects.all()[random_index].text
            Record.objects.create(user=user, text=text)


class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignIn(APIView):

    def post(self, request, format='json'):
        user = get_object_or_404(
            User,
            username=request.data['username']
        )
        if user.check_password(request.data['password']):
            token, created = Token.objects.get_or_create(user=user)
            json = {}
            json['token'] = token.key
            return Response(json, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("no matched user", status=status.HTTP_406_NOT_ACCEPTABLE)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        user = request.user
        token = get_object_or_404(Token, user=user)
        token.delete()
        return Response('User signed out', status=status.HTTP_200_OK)
