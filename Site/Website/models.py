from django.db import models
from datetime import date,time

# Create your models here.

class Member(models.Model):
    yr_choices = [
        (1,'First Year'),
        (2,'Second Year'),
        (3,'Third Year'),
        (4,'Final Year'),
    ]
    dept_choices = [
        ('OFFICE BEARERS','Office Bearers'),
        ('MANAGEMENT','Management'),
        ('AUTOMOBILE','Automobile'),
        ('MANUAL','Manual'),
        ('WEBD','Web Developement'),
        ('GRAPHICS','Graphics and Photography'),
        ('NDORS','NDORS'),

    ]
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    year = models.IntegerField(choices = yr_choices,default=2)
    department = models.CharField(max_length=20,choices = dept_choices,default='FIRST')
    photo = models.ImageField(null=True, blank=False,upload_to='profile_pics',height_field=None, width_field=None)

    def __str__(self):
        return (self.first_name + self.last_name)

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    venue = models.CharField(max_length = 200)
    date = models.DateField(auto_now=False,auto_now_add=False,blank = True)
    time = models.TimeField(auto_now=False,auto_now_add=False,blank = True)
    poster = models.ImageField(null=True, blank=False,upload_to='event_poster',height_field=None, width_field=None)
    

    


    

