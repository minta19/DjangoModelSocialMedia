from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserLoginForm,UserRegistrationForm,ProfilePictureForm,ProfileForm,CreatePostForm
from django.contrib.auth.forms import get_user_model
from django.contrib.auth import authenticate,login,logout
from .models import Post,Profile,FollowersCount
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

# Create your views here.
User=get_user_model()

def home(request):
    return render(request,'SocialMediaApp/home.html')

def userLogin(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print('Username:', username)
            print('Password:', password)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('after_login')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request,user)
           return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def userLogout(request):
    logout(request)
    return redirect('home/')  
@login_required
def afterLogin(request):
    return render(request,'SocialMediaApp/afterlogin.html')


@login_required
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)

    user_posts = Post.objects.filter(user=request.user)
    user_post_length = len(user_posts)

    follower = request.user
    user = request.user

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=request.user))
    user_following = len(FollowersCount.objects.filter(follower=request.user))
    context = {
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'SocialMediaApp/profile.html', context)

@login_required
def edit_profile(request, username):
    user_object = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'SocialMediaApp/profile_form.html', context)

@login_required
def change_profile_picture(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'SocialMediaApp/pictureedit.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')  
    else:
        form = CreatePostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'SocialMediaApp/create_post.html', context)




