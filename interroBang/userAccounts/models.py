# from django.db import models
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.utils import timezone
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=35)
#     last_name = models.CharField(max_length=35)
#     def __unicode__(self):
#         return self.user.username
#


from django.contrib.auth.models import User
from django.db import models
class Profile(models.Model):
    user = models.OneToOneField(User, unique=True,related_name="profile",  on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    trip = models.CharField(max_length=35)