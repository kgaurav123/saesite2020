from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

class ProfileUpdateForm(ModelForm):
	class Meta:
		model=Profile
		fields=[
				'first_name',
				'last_name',
				'year',
				'department',
				'fb',
				'email',
				'phone',
				'photo',
				'post',
				]
		