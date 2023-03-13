from django.db import models
from django.contrib.auth.models import User


# Create your models here.

   
class EventDetails(models.Model):
   event_id = models.AutoField(primary_key= True)
   u_id = models.ForeignKey(User, on_delete= models.CASCADE)
   title = models.CharField(max_length=255)
   description = models.TextField(max_length=255)
   Location = models.CharField(max_length=255)
   date = models.DateField()
   time = models.TimeField()
   Is_public = models.BooleanField(null= True)
   Is_rsvp = models.BooleanField(null=True)

   

