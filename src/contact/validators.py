import re
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


def user_foreign_key_valiator(user_id):
    try:
        user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        raise ValidationError(
            _("Key (user_id)=(%s) is not present in table auth_user") % (user_id))
