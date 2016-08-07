#http://www.marinamele.com/taskbuster-django-tutorial/model-creation-onetoone-relationship-signals-django-admin

from django.test import TestCase
from django.db import models
from django.conf import settings

# Create your tests here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name=_("user")
    )

