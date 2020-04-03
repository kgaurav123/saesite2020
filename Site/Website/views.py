from django.shortcuts import render, HttpResponseRedirect, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ProfileUpdateForm
from django.core.files.storage import FileSystemStorage
from .models import *


# Create your views here.
def index(request):
    return render(request,'home/index.html') 

def baja(request):
    return render(request,'home/baja.html')

def events(request):
	event_list = Event.objects.all()
	return render(request,'home/events.htm',{'events':event_list})

def event_details(request,pk):
	pass

def members(request):
    return render(request,'home/members.html')

def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			return redirect('login')
	else:
		form=UserForm()
	args={'form': form}
	return render(request,'home/signup.html',args)

def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('/update')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'home/login.html',context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('/login/')

@login_required
def update_profile(request):
	if request.method=='POST':
		form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if form.is_valid:
			form.save()

			return redirect('/logout')
	else:
		form=ProfileUpdateForm()
	return render(request,'home/formupdate.html',{'form':form})

def member_list(request):
	profiles=Profile.objects.filter(department="MANUAL").order_by('-year')
	m=[]
	print(profiles)
	for i in profiles:
		m.append(i)
	print(m)

	return render(request,'home/members.html',{'m':m})


