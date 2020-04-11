from django.shortcuts import render, HttpResponseRedirect, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, ProfileUpdateForm, CreatePostForm, CreateCommentForm
from django.core.files.storage import FileSystemStorage
from .models import *

def home(request):
	return render(request,'blog/home.html')


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			return redirect('blogin')
	else:
		form=UserForm()
	args={'form': form}
	return render(request,'blog/signup.html',args)

def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('/blog/posts')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'blog/login.html',context)

@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/blog')
@login_required
def update_profile(request):
	if request.method=='POST':
		form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile_blog)
		if form.is_valid:
			form.save()

			return redirect('/blog/posts')
	else:
		form=ProfileUpdateForm()
	return render(request,'blog/formupdate.html',{'form':form})

@login_required
def post_list(request):
	posts=Posts.objects.order_by('-date_posted')

	return render(request,'blog/post_list.html',{'posts':posts})

@login_required
def create_post(request):
	if request.method=='POST':
		form=CreatePostForm(request.POST,request.FILES)
		if form.is_valid():
			p=form.save(commit=False)
			p.author=request.user
			p.date_posted=timezone.now()
			p.save()
			#form.save()
			
			return redirect('/blog/posts')
	else:
		form=CreatePostForm()
	
    
	return render(request,'blog/postenter.html',{'form':form})

@login_required
def post_details(request,key):
	posts=Posts.objects.get(id=key)
	comments=Comment.objects.filter(posts=posts).order_by('date')
	co=[]
	for i in comments:
		co.append(i)

	number_likes=posts.likes.all().count()

	if posts.author==request.user:
		return render(request,'blog/viewpost1.html',{'posts':posts,'co':co,'number_likes':number_likes})#Add delete post option
	else:
		return render(request,'blog/viewpost2.html',{'posts':posts,'co':co,'number_likes':number_likes})
@login_required
def confirm_delete(request,key):
	posts=Posts.objects.get(id=key)
	return render(request,'blog/confirm_delete.html',{'posts':posts})
@login_required
def post_delete(request,key):
	posts=Posts.objects.get(id=key)
	posts.delete()
	return redirect('/blog/posts')
@login_required
def create_comment(request,key):
	posts=Posts.objects.get(id=key)

	if request.method=='POST':
		form=CreateCommentForm(request.POST)
		if form.is_valid():
			p=form.save(commit=False)
			p.author=request.user
			p.posts=posts
			p.save()
			#next = request.POST.get('next',None)
			#return HttpResponseRedirect(next)
			#return redirect('/home/key/')
			return redirect('/blog/posts/%s' % key )
	else:
		form=CreateCommentForm()

	return render(request,'blog/create_comment.html',{'form':form})
@login_required
def create_like(request,key):
	posts=Posts.objects.get(id=key)
	new_like,create=Likes.objects.get_or_create(user=request.user, posts=posts)
	number=posts.likes.all().count()
	print(number)
	#if not create:
	return redirect('/blog/posts/% s' %key)
