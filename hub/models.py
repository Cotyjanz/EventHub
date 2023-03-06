from tkinter import CASCADE
from django.db import models

# Create your models here.
class UserDetails(models.Model):
   u_id = models.AutoField(primary_key= True)
   username = models.CharField(max_length=255)
   email = models.EmailField(max_length=255)
   password = models.CharField(max_length=255)

   
class EventDetails(models.Model):
   event_id = models.AutoField(primary_key= True)    
   u_id = models.ForeignKey(UserDetails, on_delete = models.CASCADE)
   title = models.CharField(max_length=255)
   description = models.TextField(max_length=255)
   Location = models.CharField(max_length=255)
   link = models.CharField(max_length=255)
   date = models.DateField()
   time = models.TimeField()
   Is_public = models.BooleanField(null= True)
   Is_rsvp = models.BooleanField(null=True)

   

