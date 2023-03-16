from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#specifying the choices
SELECT_LAYOUT = (
         ("layout 1", "layout 1"),
         ("layout 2", "layout 2"),
         ("layout 3", "layout 3"),
         ("layout 4", "layout 4"),
         ("layout 5", "layout 5"),
)
   
class EventDetails(models.Model):
   event_id = models.AutoField(primary_key= True)
   u_id = models.ForeignKey(User, on_delete= models.CASCADE)
   title = models.CharField(max_length=255)
   description = models.TextField(max_length=255)
   Location = models.CharField(max_length=255)
   poster_layout = models.CharField(max_length=50, choices=SELECT_LAYOUT, default='layout 1')
   date = models.DateField()
   time = models.TimeField()
   Is_public = models.BooleanField(null= True)
   Is_rsvp = models.BooleanField(null=True)

   

