from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone


class Profile_blog(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=50, blank=False, null=False)
	last_name=models.CharField(max_length=50, blank=False, null=False)
	bio=models.TextField(max_length=500, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='bprofile_pics')
	fb=models.URLField(null=True, blank=True)
	email=models.EmailField(null=False, blank=False)
	phone=models.CharField(null=False,blank=False,max_length=15)

	def __str__(self):
		return (self.first_name + self.last_name)


@receiver(post_save,sender=User)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile_blog.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile_blog.save()


class Posts(models.Model):
	title=models.CharField(max_length=100,null=False, blank=False )
	content=models.TextField(max_length=1500, null=False, blank=False)
	image=models.ImageField(upload_to='images/')
	date_posted = models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return (self.title)

class Comment(models.Model):
	posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text=models.CharField(max_length=200)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text

class Likes(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	posts=models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
	date_created=models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return (str(self.user) +"-----"+ str(self.posts))




