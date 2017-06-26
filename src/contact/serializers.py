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


class BaseContactSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    contact_id = serializers.IntegerField()
    # contact_type = serializers.ChoiceField(
    #     choices=ContactPhone.CONTACT_TYPE_CHOICES)
    # custom_type = serializers.CharField(
    #     max_length=15, allow_blank=True, allow_null=True)

    def validate_contact_id(self, value):
        try:
            Contact.objects.using(self.context['shard']).get(id=value)
        except:
            raise serializers.ValidationError("Contact does not exists")
        return value

    def save(self):
        if getattr(self, "instance"):
            for key, value in self.validated_data.items():
                setattr(self.instance, key, value)
            self.instance.save()
            return self.instance
        else:
            contact = Contact.objects.using(
                self.context['shard']).get(id=self.validated_data['contact_id'])
            obj = self.Meta.model.objects.using(self.context['shard']).create(**self.validated_data, contact=contact)
            self.validated_data['id'] = obj.id
            return obj


class ContactPhoneSerializer(BaseContactSerializer):
    """
    Serializer for new user add.
    """

    class Meta:
        model = ContactPhone
        fields = ('id', 'contact_id', 'contact_type', 'custom_type', 'phone')
        read_only_fileds = ("id",)


class ContactEmailSerializer(BaseContactSerializer):
    """
    Serializer for new user add.
    """

    class Meta:
        model = ContactEmail
        fields = ('id', 'contact_id', 'contact_type', 'custom_type', 'email')
        read_only_fileds = ("id", )
