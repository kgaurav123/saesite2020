from django.db import models
from datetime import date,time
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 
from django.core.exceptions import ValidationError



def validate_image_size(value):
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MiB.')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    yr_choices = [
        (1,'First Year'),
        (2,'Second Year'),
        (3,'Third Year'),
        (4,'Final Year'),
    ]
    dept_choices = [
        ('OFFICE BEARERS','Office Bearers'),
        ('MANAGEMENT','Management'),
        ('TECHNICAL','Technical'),
        ('WEBD','Web Developement'),
        ('GRAPHICS','Graphics and Photography'),
        ('NDORS','NDORS'),
        ]
    post_choices = [
        ('PRESIDENT','President'),
        ('VICE PRESIDENT','Vice President'),
        ('GENERAL SECRETARY','General Secretary'),
        ('TREASURER','Treasurer'),
        ('CONVENER','Convener'),
        ('TECH HEAD','Tech Head'),
        ('DESIGN HEAD','Design Head'),
        ('WEBD','web D'),
        ('PUBLICITY HEAD','Publicity Head'),
        ('CREATIVE HEAD','Creative Head'),
        ('SPONSORSHIP HEAD','Sponsorship Head'),
        ('ACCOMODATION,TRAVEL AND HOSPITALITY HEAD','Accomodation,travel and Hospitality Head'),
        ('BAJA COORDINATOR','Baja coordinator'),
        ('WORKSHOP HEAD','Workshop Head'),
        ('EVENTS HEAD','Events Head'),
        ('EVENTS AND FEST COORDINATOR','Events and Fest coordinator'),
        ('LOGISTIC HEAD','Logistic Head'),
        ('NONE','None'),
    ]

    
    first_name=models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length = 50)
    year = models.IntegerField(choices = yr_choices,default=2)
    department = models.CharField(max_length=20,choices = dept_choices,default='FIRST')
    post = models.CharField(max_length=40,choices = post_choices,default='None')
    fb=models.URLField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(null=True,blank=False, max_length=15)
    photo = models.ImageField(null=True, blank=False,upload_to='profile_pics',validators=[validate_image_size])

    def __str__(self):
        #return (self.first_name + self.last_name)
        return (str(self.user))

    def isPostHolder(self):
        if (self.post == 'NONE'):
            return 0
        else:
            return 1

@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Event(models.Model):
    event_type = [
        ('online','ONLINE'),
        ('offline','OFFLINE')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    type_event = models.CharField(max_length = 50,choices=event_type,default='offline')
    venue = models.CharField(max_length = 200)
    date = models.DateField(auto_now=False,auto_now_add=False,blank = True)
    time = models.TimeField(auto_now=False,auto_now_add=False,blank = True)
    poster = models.ImageField(null=True, blank=False,upload_to='event_poster',height_field=None, width_field=None)
    
    def __str__(self):
        return self.name
    


    

