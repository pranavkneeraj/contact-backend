"""
Serializer for Authentication functions
"""


from rest_framework import serializers
from .models import (Contact, ContactPhone, ContactEmail)


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for new user add.
    """

    class Meta:
        model = Contact
        fields = '__all__'


class BaseContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    contact_id = serializers.IntegerField()
    contact_type = serializers.ChoiceField(
        choices=ContactPhone.CONTACT_TYPE_CHOICES)
    custom_type = serializers.CharField(
        max_length=15, allow_blank=True, allow_null=True)

    def validate_contact(self, value):
        try:
            Contact.objects.using(self.context['shard']).get(id=value)
        except:
            raise serializers.ValidationError("Contact does not exists")
        return value

    def save(self):
        contact = Contact.objects.using(
            self.context['shard']).get(id=self.validated_data['contact'])
        del self.validated_data['contact']
        obj = ContactPhone.objects.create(**self.validated_data, contact=contact)
        self.validated_data['contact'] = obj.contact.id
        self.validated_data['id'] = obj.id
        return obj


class ContactPhoneSerializer(BaseContactSerializer):
    """
    Serializer for new user add.
    """
    phone = serializers.CharField(max_length=15)

    class Meta:
        fields = ('contact', 'contact_type', 'custom_type', 'phone')


class ContactEmailSerializer(BaseContactSerializer):
    """
    Serializer for new user add.
    """
    email = serializers.EmailField()

    class Meta:
        fields = ('contact', 'contact_type', 'custom_type', 'phone')
