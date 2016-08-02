from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40, null=False, unique=True, default="")
    #    passwordHash =
    #(Note: pip install bcrypt in webenv)
    #https://ghrhome.gitbooks.io/djangoknowhow/content/password_management_in_django/using_bcrypt_with_django.html

    firstName = models.CharField(max_length=35, null=False)
    lastName = models.CharField(max_length=35, null=False)
    email = models.EmailField(max_length=70, null=False, unique=True)
    registration = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
    def __str__(self):
        return self.username

class Friend(models.Model):
    #friends list
    friendshipDate = models.DateField(auto_now_add=True)

class Notification(models.Model):
    content = models.CharField(max_length=250)
    siteAlert = 0
    tripAdd = 1
    newFriend = 2
    newComment = 3
    nTypes = ((0, 'siteAlert'),
              (1, 'tripAdd'),
              (2, 'newFriend'),
              (3, 'newComment'))
    type = models.IntegerField(choices=nTypes, null=False, blank=True, default=0)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)