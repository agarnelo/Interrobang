from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20)

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

