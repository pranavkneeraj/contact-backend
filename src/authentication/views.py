"""
View for Login, Sending Mail, Reset Password
"""


from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (GenericAPIView)


from knox.models import AuthToken
from knox.settings import knox_settings


from .serializers import (
    LogInSerializer, ResetPasswordSerializer, UserSerializer)

KNOXUSERSERIALIZER = knox_settings.USER_SERIALIZER


class LoginView(APIView):

    """
    Login View
    """
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def post(self, request):
        """"
        Post method for login.
        """
        serializer = LogInSerializer(
            data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            # User.objects.get(username=serializer.data.get('username'))
            token = AuthToken.objects.create(request.user)
            return Response({
                "user": KNOXUSERSERIALIZER(request.user).data,
                "token": token,
            })
        else:
            return Response({"data": serializer.errors})


class ResetPasswordView(GenericAPIView):
    """
    Reset Password View
    """
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Post method for Password view
        """
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse("true", status=200)
        else:
            return HttpResponse("false", status=400)


class MeView(APIView):

    """
    User's View
    """

    def get(self, request):
        """
        get method for which user is login
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)


class UserViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    View For list of user
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

    def update(self, request, pk=None):
        instance = User.objects.get(pk=pk)  # pylint: disable=no-member
        instance.first_name = request.data['first_name']
        instance.last_name = request.data['last_name']
        instance.username = request.data['username']
        instance.email = request.data['email']
        instance.save()
        return Response(request.data)
