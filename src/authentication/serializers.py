"""
Serializer for Authentication functions
"""

from datetime import datetime
import base64
import hashlib

from django.conf import settings
from django.contrib.auth import (get_user_model, authenticate, login)
from django.utils.crypto import get_random_string

from rest_framework import serializers

from Crypto.Cipher import AES

User = get_user_model()  # pylint: disable=invalid-name


class LogInSerializer(serializers.Serializer):
    """
    Serializer for login data.
    """
    username = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=True)

    def validate(self, data):
        try:
            user = authenticate(**data)
            login(self.context['request'], user)
            return user
        except Exception as e:  # pylint: disable=invalid-name
            print(e)
            raise serializers.ValidationError('Invalid Username or Password.')

    def create(self, *a, **k):
        pass

    def update(self, *a, **k):
        pass


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    new_password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)
    code = serializers.CharField(max_length=255)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError(
                "Passwords do not match")
        decoded_data = super(ResetPasswordSerializer, self).get_decrypted_data(
            data.get('code')).split('_')
        try:
            user = User.objects.get(username=decoded_data[0])
        except User.DoesNotExist:
            raise serializers.ValidationError("User Does Not Exist")
        data['user'] = user
        return data

    def create(self, validated_data):  # pylint: disable=arguments-differ
        try:
            user = User.objects.get(username=validated_data.get('user'))
        except User.DoesNotExist:
            raise serializers.ValidationError("User Does Not Exist")

        user.set_password(validated_data.get('new_password'))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for new user add.
    """

    def __init__(self, *args, **kwargs):  # pylint: disable=no-self-use
        """
        Initialization of email field.
        """
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email', 'is_active', 'is_superuser')

    def validate_username(self, username):  # pylint: disable=no-self-use
        """
        Validation for username.
        """
        try:
            user = User.objects.get(  # pylint: disable=unused-variable
                username=username)
            raise serializers.ValidationError("Username already exists ")
        except User.DoesNotExist:
            return username

    def validate_email(self, email):  # pylint: disable=no-self-use
        """
        Validation for email.
        """
        try:
            user = User.objects.get(  # pylint: disable=unused-variable
                email=email)
            raise serializers.ValidationError("This Email already exists ")
        except User.DoesNotExist:
            return email

    def create(self, validated_data):
        """
        create user
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=get_random_string(length=10),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        recipient_email = user.email
        subject = "Welcome User"

        mail(
            "email-send-add.html",
            {
                'username': user.username,
                'password': user.password,
                'firstname': user.first_name
            }, subject, recipient_email
        )
        user.set_password(user.password)
        user.save()
        return user
