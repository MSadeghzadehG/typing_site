from rest_framework.views import APIView, View
from rest_framework import generics, status, parsers
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import RecordSerializer, TestSerializer, UserSerializer
from .models import Record, Test, User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.


class TestAPI(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]


class RecordsList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    parser_classes = (parsers.JSONParser,)

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            # if user.is_active:
            login(request, user)
            return Response("logged in.", status=status.HTTP_200_OK)
            # else:
            #     return Response("Inactive user.", status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("failed to log in", status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response("logged out", status=status.HTTP_200_OK)
