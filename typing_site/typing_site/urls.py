"""typing_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test_provider.views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('signin/', UserSignIn.as_view(), name='singin'),
    path('signout/', UserSignOut.as_view(), name='logout'),
    path('users/', UserList.as_view(), name='users'),
    # path('users/<str:username>/', UserList.as_view(), name='user'),
    # path('records/', RecordsList.as_view(), name='records'),
]
