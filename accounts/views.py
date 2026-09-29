

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CitizenRegistrationForm, NGORegistrationForm
from .models import UserProfile, NGOProfile

def register_citizen(request):
    if request.method == 'POST':
        form = CitizenRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create associated Citizen UserProfile
            UserProfile.objects.create(
                user=user,
                role='CITIZEN',
                phone=form.cleaned_data.get('phone'),
                location=form.cleaned_data.get('location')
            )

            login(request, user)
            messages.success(request, f"Account created successfully for {user.username}!")
            return redirect('dashboard_home')
    else:
        form = CitizenRegistrationForm()

    return render(request, 'accounts/register_citizen.html', {'form': form})


def register_ngo(request):
    if request.method == 'POST':
        form = NGORegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create UserProfile with NGO role
            UserProfile.objects.create(
                 user=user, 
                 role='NGO',
                 phone=form.cleaned_data.get('phone'),
                 location=form.cleaned_data.get('location')
            )
            
            # Create NGOProfile
            NGOProfile.objects.create(
                user=user,
                organization_name=form.cleaned_data.get('organization_name'),
                category_focus=form.cleaned_data.get('category_focus'),
                operating_location=form.cleaned_data.get('operating_location')
            )

            login(request, user)
            messages.success(request, f"NGO Account created for {form.cleaned_data.get('organization_name')}!")
            return redirect('dashboard_home')
    else:
        form = NGORegistrationForm()

    return render(request, 'accounts/register_ngo.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome back, {username}!")
                return redirect('dashboard_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')