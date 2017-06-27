"""
View for Login, Sending Mail, Reset Password
"""

from itertools import chain

from django.http import HttpResponse
from django.contrib.auth import get_user_model

from rest_framework import viewsets, response
from rest_framework.permissions import AllowAny
from .serializers import (
    ContactSerializer, ContactPhoneSerializer, ContactEmailSerializer)
from .models import (Contact, ContactPhone, ContactEmail)
from rest_framework_extensions.mixins import NestedViewSetMixin
User = get_user_model()


class ContactViewSet(NestedViewSetMixin, viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    View For list of contact
    """
    serializer_class = ContactSerializer
    parent = 'user'
    parent_lookup = 'parent_lookup_contact'

    def initial(self, request, *args, **kwargs):
        if self.kwargs.get('parent_lookup_contact'):
            self.shard = Contact.get_shard_from_id(
                self.kwargs.get('parent_lookup_contact'))
        if self.request.method in ['POST', 'PATCH', 'PUT'] and not self.request.data.get('user'):
            if not type(self.request.data) == dict:
                self.request.data._mutable = True
            self.request.data['user'] = int(kwargs.get(
                'parent_lookup_contact'))
            if not type(self.request.data) == dict:
                self.request.data._mutable = False
        super(ContactViewSet, self).initial(request, args, kwargs)

    def get_queryset(self, *args, **kwargs):
        print("sdasdasd", self.request.user.id)
        return Contact.objects.using(self.shard).filter(user=self.request.user.id)


class BaseContactViewset(viewsets.ModelViewSet):
    parent = 'contact_id'
    shard = 'default'
    parent_model = Contact
    parent_lookup = 'parent_lookup_phone'

    def initial(self, request, *args, **kwargs):
        if self.kwargs.get('parent_lookup_phone__contact'):
            self.shard = Contact.get_shard_from_id(
                self.kwargs.get('parent_lookup_phone__contact'))
        if self.request.method in ['POST', 'PATCH', 'PUT'] and not self.request.data.get('contact_id'):
            if not type(self.request.data) == dict:
                self.request.data._mutable = True
            self.request.data['contact_id'] = int(kwargs.get(
                'parent_lookup_phone'))
            if not type(self.request.data) == dict:
                self.request.data._mutable = False
        super(BaseContactViewset, self).initial(request, args, kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.using(self.shard).filter(
            contact__user=self.request.user.id)
        return qs

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'shard': self.shard
        }


class ContactPhoneViewSet(BaseContactViewset, NestedViewSetMixin):  # pylint: disable=too-many-ancestors
    """
    View For list of user
    """
    serializer_class = ContactPhoneSerializer
    model = ContactPhone


class ContactEmailViewSet(BaseContactViewset, NestedViewSetMixin):  # pylint: disable=too-many-ancestors
    """
    View For list of user
    """
    serializer_class = ContactEmailSerializer
    model = ContactEmail
