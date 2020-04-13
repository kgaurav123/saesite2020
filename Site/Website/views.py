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
	event = Event.objects.get(id = pk)
	return render(request,'home/event_details.html',{'event':event})

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
	office_bearers = Profile.objects.filter(year = 4).order_by('post')

	management_final=Profile.objects.filter(department="MANAGEMENT",year=4).order_by('post')
	management_third=Profile.objects.filter(department="MANAGEMENT",year=3)
	management_second=Profile.objects.filter(department="MANAGEMENT",year=2)

	technical_final=Profile.objects.filter(department="TECHNICAL",year=4).order_by('post')
	technical_third=Profile.objects.filter(department="TECHNICAL",year=3)
	technical_second=Profile.objects.filter(department="TECHNICAL",year=2)

	webd_final=Profile.objects.filter(department="WEBD",year=4).order_by('post')
	webd_third=Profile.objects.filter(department="WEBD",year=3)
	webd_second=Profile.objects.filter(department="WEBD",year=2)

	graphics_final=Profile.objects.filter(department="GRAPHICS",year=4).order_by('post')
	graphics_third=Profile.objects.filter(department="GRAPHICS",year=3)
	graphics_second=Profile.objects.filter(department="GRAPHICS",year=2)

	baja_final=Profile.objects.filter(department="NDORS",year=4)
	baja_third=Profile.objects.filter(department="NDORS",year=3)
	baja_second=Profile.objects.filter(department="NDORS",year=2)
	

	return render(request,'home/members.html',{'office_bearers':office_bearers,'management_final':management_final,
	'management_third':management_third,'management_second':management_third,'technical_final':technical_final,
	'technical_third':technical_third,'technical_second':technical_second,'webd_final':webd_final,'webd_third':webd_third,
	'webd_second':webd_second,'graphics_final':graphics_final,'graphics_third':graphics_third,'graphics_second':graphics_second,
	'baja_final':baja_final,'baja_third':baja_third,'baja_second':baja_second})


