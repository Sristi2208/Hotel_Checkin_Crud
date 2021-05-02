from django.db import models
import datetime

# Create your models here.


class Checkin(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    indate = models.DateTimeField(default=datetime.date.today)
    outdate = models.DateTimeField(default=datetime.date.today)
    intime = models.TimeField()
    outtime = models.TimeField()
    gender = models.CharField(max_length=10)
    adult = models.CharField(max_length=20)
    children = models.CharField(max_length=20)
    checkin = models.CharField(max_length=20)
    c1 = models.BooleanField(default=False) 
    c2 = models.BooleanField(default=False)
    c3 = models.BooleanField(default=False)
    c4 = models.BooleanField(default=False)
    c5 = models.BooleanField(default=False)
    pic = models.ImageField(null=True, blank=True, upload_to="images/")
    # something_truthy = models.BooleanField(required=False)

    class Meta:
        db_table = 'hotel_checkin'
