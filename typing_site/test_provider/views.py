from rest_framework.views import APIView, View
from rest_framework import generics, status, parsers
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import RecordSerializer, UserSerializer
from .models import Record, User, TestText
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


from django.db.models.aggregates import Count
from random import randint

# Create your views here.


# class TestAPI(generics.CreateAPIView):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         # print(self.random().text)
#         text = self.random().text
#         user = request.user
#         return self.create(request, text=text, user=user)
    
#     def random(self):
#         count = len(TestText.objects.all())
#         random_index = randint(0, count - 1)
#         return TestText.objects.all()[random_index]



class RecordsList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return super().perform_create(serializer)


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
                json.pop('password')
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
