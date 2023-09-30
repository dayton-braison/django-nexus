from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Update
from django.contrib import messages
from .forms import AddUpdateForm, RegisterUserForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


def home(request):
    if request.user.is_authenticated:
        form = AddUpdateForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                update = form.save(commit=False)
                update.user = request.user
                update.save()
                messages.info(request, ("Awesome!! Your update has been posted!!"))
                return redirect("home")
        updates = Update.objects.all().order_by("-created_at")
        return render(request, 'nexus/home.html', {'updates': updates, 'form': form})
    else:
        updates = Update.objects.all().order_by("-created_at")
        return render(request, 'nexus/home.html', {'updates': updates})


def profile_list(request):
    if request.user.is_authenticated:
        # Show all profiles except for user that is signed in
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'nexus/profile_list.html', {'profiles': profiles})
    else:
        messages.error(request, "You must be logged in to view this page!!")
        return redirect('home')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        updates = Update.objects.filter(user_id=pk).order_by("-created_at")
        # POST form logic
        if request.method == 'POST':
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            else: 
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save()
        return render(request, 'nexus/profile.html', {'profile': profile, 'updates': updates})
    else:
        messages.error(request, "You must be logged in to view this page!!")
        return redirect('login')
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, ("You have been successfully logged in!!"))
            return redirect("home")
        else:
            messages.error(request, ("Uh oh!! There was an error logging in. Please try again"))
            return redirect("login")
    else:
        return render(request, "nexus/login.html", {})


def logout_user(request):
    logout(request)
    messages.info(request, ("You have been successfully logged out!!"))
    return redirect("login")


def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, ("You have successfully registered! Welcome to Nexus!!"))
            return redirect("home")
    return render(request, 'nexus/register.html', {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        # Get forms
        user_form = RegisterUserForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)
            messages.info(request, ("Your profile has been updated!"))
            return redirect("home")
        return render(request, 'nexus/update_user.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        messages.error(request, ("You must be logged in to view that page"))
        return redirect("login")
    

def update_like(request, pk):
    if request.user.is_authenticated:
        update = get_object_or_404(Update, id=pk)
        if update.likes.filter(id=request.user.id):
            update.likes.remove(request.user)
        else:
            update.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request, ("You must be logged in to like updates"))
        return redirect('home')
    

def update_show(request, pk):
    # if request.user.is_authenticated:
    update = get_object_or_404(Update, id=pk)
    if update:
        return render(request, "nexus/update_show.html", {'update': update})
    else:
        messages.error(request, ("That update does not exist"))
        return redirect("home")