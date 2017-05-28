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
from django.conf.urls import (url, include)
from django.contrib import admin


from rest_framework_extensions.routers import ExtendedSimpleRouter

from category.views import CategoryViewSet
from product.views import ProductViewSet
from authentication.views import UserViewSet


router = ExtendedSimpleRouter()  # pylint: disable=invalid-name

router.register(r'product', ProductViewSet, base_name="Product")
router.register(r'user', UserViewSet, base_name="User")
router.register(
    r'category', CategoryViewSet, base_name="Category")


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^admin', admin.site.urls),
    url(r'^auth', include('authentication.urls')),
]
if not settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT})
    ]
