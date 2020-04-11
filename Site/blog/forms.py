from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

class ProfileUpdateForm(ModelForm):
	class Meta:
		model=Profile_blog
		fields=[
				'first_name',
				'last_name',
				'bio',
				'fb',
				'email',
				'phone',
				'image',
				]

class CreatePostForm(ModelForm):
	class Meta:
		model=Posts
		fields=[
				'title',
				'content',
				'image',
				]

class CreateCommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=[
				'text',
				]
		