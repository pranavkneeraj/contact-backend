"""
1;4205;0ccore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (url, include)
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter
from contact.views import (
    ContactViewSet, ContactPhoneViewSet, ContactEmailViewSet)
from authentication.views import UserViewSet
from core.views import *

router = ExtendedSimpleRouter()
(
    router.register(r'users', UserViewSet, base_name='user_pk')
    .register(r'contacts',
              ContactViewSet,
              base_name='contact',
              parents_query_lookups=['contact'])
    .register(r'phones',
              ContactPhoneViewSet,
              base_name='users-contact-phone',
              parents_query_lookups=['phone__contact', 'phone'])
)
(
    router.register(r'users', UserViewSet, base_name='user_pk')
    .register(r'contacts',
              ContactViewSet,
              base_name='contact',
              parents_query_lookups=['contact'])
    .register(r'emails',
              ContactEmailViewSet,
              base_name='users-contact-phone',
              parents_query_lookups=['phone__contact', 'phone'])
)

# router = router = routers.SimpleRouter()
# router.register(r'user', UserViewSet, base_name="User")
# contact_router = routers.NestedSimpleRouter(
#     router, r'user', lookup='user')
# contact_router.register(r'contact', ContactViewSet,
#                         base_name='contact')

# contact_phone_router = routers.NestedSimpleRouter(
#     contact_router, r'contact', lookup='contact')
# contact_phone_router.register(
#     r'phones', ContactPhoneViewSet, base_name='contact-phones')


urlpatterns = static(settings.ANGULAR_URL, document_root=settings.ANGULAR_ROOT) + [
    url(r'^api/', include(router.urls)),
    #    url(r'^', include(contact_router.urls)),
    #   url(r'^', include(contact_phone_router.urls)),
    url(r'^admin', admin.site.urls),
    url(r'^auth', include('authentication.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', AngularApp.as_view(), name="angular_app")
]
if not settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT})
    ]
