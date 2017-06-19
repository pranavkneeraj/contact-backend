"""
Auth backend with username or email or mobile
"""
from django.db.models import Q
from django.contrib.auth import get_user_model


class CustomAuthBackend(object):
    """
    Custom Email Backend to perform authentication via email
    """

    def authenticate(self, username=None, password=None):  # pylint: disable=no-self-use
        """
        Authentication of email
        """
        user_model = get_user_model()
        try:
            user = user_model.objects.get(
                Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user  # return user on valid credentials
        except user_model.DoesNotExist:
            return None  # return None if custom user model does not exist
        except:  # pylint: disable=bare-except
            return None  # return None in case of other exceptions

    def get_user(self, user_id):  # pylint: disable=no-self-use
        """
        Get user information using user_id
        """
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
