from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=40, null=False, unique=True)
    #    passwordHash =
    #(Note: pip install bcrypt in webenv)
    #https://ghrhome.gitbooks.io/djangoknowhow/content/password_management_in_django/using_bcrypt_with_django.html

    fName = models.CharField(max_length=35, null=False)
    lname = models.CharField(max_length=35, null=False)
    email = models.EmailField(max_length=70, null=False, unique=True)
    registration = models.DateField(auto_now_add=True)

class Friend(models.Model):
    fID = models.AutoField(primary_key=True)
    #friends list
    fDate = models.DateField(auto_now_add=True)

class Location(models.Model):
    lID = models.AutoField(primary_key=True)
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

class Photo(models.Model):
    pID = models.AutoField(primary_key=True)
    #https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    imagePath = models.ImageField(upload_to="/photos", default="photo/none/noimg.jpg")
    #iEvent = models.ForeignKey(Event)

class Comment(models.Model):
    cID = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=40, null=False) #username
    #cEvent = models.ForeignKey(Event)
    
class Event(models.Model):
    text = models.CharField(max_lenght=500)
    date = models.DateTimeField()
    creator = models.CharField(max_length=35)
    public = models.BoolenField()
    album = models.ForeignKey(Trip, on_delete = models.CASCADE)
    #location = models.ForeignKey(Location, on_delete = models.CASCADE, blank = true)

class Trip(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    creator = models.CharField(max_length=35)
    dests = models.ManyToMany(Dest, on_delete = models.CASCADE)
    #travlers = models.ManyToMany(User, on_delete = models.CASCADE)

class Dest(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=250)

class Note(models.Model):
    content = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    #reciever = models.ForeignKey(User, on_delete = models.CASCADE, blank = false)

#http://tutorial.djangogirls.org/en/django_forms/
