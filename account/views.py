from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')



@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get_or_create(user=user)
    context = {'profile': profile, 'user': user}

    return render(request, 'account/profile.html', context)


@login_required
def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'account/create_profile.html', context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'account/edit_profile.html', context)

def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)



def user_login(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            context = {
                'form': form,
                'error': "Invalid User Or Password !!"
            }
            return render(request, 'account/login.html', context)

    context = {'form': form}
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
