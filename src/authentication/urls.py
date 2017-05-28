"""
importing views and urls
"""

from django.conf.urls import (url)
from knox.views import LogoutView
from .views import (
    LoginView, ResetPasswordView, MeView)

urlpatterns = [
    url(r'login', LoginView.as_view(), name='knox_login'),
    url(r'logout', LogoutView.as_view(), name='knox_logout'),
    url(r'reset-password', ResetPasswordView.as_view(), name='knox_reset'),
    url(r'me', MeView.as_view(), name='user_me'),
]
