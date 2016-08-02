from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40, null=False, unique=True)
    #    passwordHash =
    #(Note: pip install bcrypt in webenv)
    #https://ghrhome.gitbooks.io/djangoknowhow/content/password_management_in_django/using_bcrypt_with_django.html

    fName = models.CharField(max_length=35, null=False)
    lname = models.CharField(max_length=35, null=False)
    email = models.EmailField(max_length=70, null=False, unique=True)
    registration = models.DateField(auto_now_add=True)

class Friend(models.Model):
    #friends list
    fDate = models.DateField(auto_now_add=True)

class Location(models.Model):
    lName = models.CharField(max_length=50, null=False)
    restaurant = 1
    museum = 2
    hotel = 3
    cafe = 4
    leisure = 5
    lType_choices = (
        (0, 'restaurant'),
        (1, 'museum'),
        (2, 'hotel'),
        (3, 'cafe'),
        (4, 'leisure'),
    )
    lType = models.IntegerField(choices=lType_choices, null=False, blank=True, default=4)
    city = models.ForeignKey(Dest, on_delete = models.CASCADE)

class Photo(models.Model):
    #https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    imagePath = models.ImageField(upload_to="/photos", default="photo/none/noimg.jpg")
    iEvent = models.ForeignKey(Event)

class Comment(models.Model):
    cID = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=40, null=False) #username
    cEvent = models.ForeignKey(Event)
    
class Dest(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=250)

class Trip(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    creator = models.CharField(max_length=35)
    dests = models.ManyToManyField(Dest, on_delete = models.CASCADE)
    travelers = models.ManyToMany(User, on_delete = models.CASCADE)

class Event(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField()
    creator = models.CharField(max_length=35)
    public = models.BooleanField()
    album = models.ForeignKey(Trip, on_delete = models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE, blank = True)


class Note(models.Model):
    content = models.CharField(max_length=250)
    site_alert = 0
    trip_add = 1
    new_friend = 2
    new_comment = 3
    nTypes = ((0, 'site_alert'),
              (1, 'trip_add'),
              (2, 'new_friend'),
              (3, 'new_comment'))
    type = models.IntegerField(choices=nTypes, null=False, blank=True, default=0)
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)

#http://tutorial.djangogirls.org/en/django_forms/
