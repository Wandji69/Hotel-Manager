
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.





class Hotel(models.Model):
    desc_text = models.CharField(max_length=200)
    act_date = models.DateTimeField('active_date')
    def __str__(self):
        return self.desc_text

    def active_date(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.act_date <= now 
    active_date.admin_order_field = 'act_date'
    active_date.boolean = True
    active_date.short_description = 'Active recently?'  


    


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_text = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.room_text