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
        if self.kwargs.get('parent_lookup_contact'):
            self.shard = Contact.get_shard_from_id(
                self.kwargs.get('parent_lookup_contact'))
        return Contact.objects.using(self.shard).all()

    def list(self, request, *args, **kwargs):
        return response.Response(list(chain(self.get_queryset().values(),
                                            Contact.objects.using('contact2').values())))


class BaseContactViewset(viewsets.ModelViewSet):
    parent = 'contact_id'
    shard = 'default'
    parent_model = Contact
    parent_lookup = 'parent_lookup_phone'

    def initial(self, request, *args, **kwargs):
        if self.kwargs.get('parent_lookup_phone__contact'):
            self.shard = Contact.get_shard_from_id(
                self.kwargs.get('parent_lookup_phone__contact'))
        super(BaseContactViewset, self).initial(request, args, kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = self.model.objects.using(self.shard).all()
        if kwargs.get('parent_lookup_phone'):
            qs = qs.filter(contact_id=kwargs.get('parent_lookup_phone'))
        return qs

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'shard': self.shard
        }

    def update(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(pk=kwargs["pk"])
        data = dict(request.data.items())
        if not data['contact_id']:
            data['contact_id'] = kwargs[self.parent_lookup]
        qs.update(**data)
        return response.Response(self.serializer_class(qs[0]).data)

    def create(self, request, *args, **kwargs):
        if not type(request.data) == list:
            data_list = [dict(request.data.items())]
        else:
            data_list = request.data
        res = []
        print(data_list)
        exit()
        for data in data_list:
            data['contact_id'] = kwargs['parent_loopup_phone']
            ser = self.serializer_class(data=data)
            ser.is_valid(raise_exception=True)
            obj = self.model.objects.using(self.shard).create(**ser.data)
            res.append(self.serializer_class(obj.__dict__).data)
        print(response.Response(res[0] if len(res) == 1 else res))
        return response.Response(res[0] if len(res) == 1 else res)

        # data = dict(request.data.items())
        # data['contact_id'] = kwargs['parent_lookup_phone']
        # ser = self.serializer_class(data=data)
        # if ser.is_valid():
        #     obj = self.model.objects.using(self.shard).create(**ser.data)
        #     return response.Response(self.serializer_class(obj.__dict__).data)
        # return response.Response(ser.errors())

    def retrieve(self, request, *args, **kwargs):
        try:
            return response.Response(self.get_queryset(*args, **kwargs).values().get(pk=kwargs['pk']))
        except:
            return response.Response({
                "detail": "Not found."
            })

    def list(self, request, *args, **kwargs):
        return response.Response(self.serializer_class(list(self.get_queryset(*args, **kwargs).values()), many=True).data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)


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
