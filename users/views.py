from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, userLoginForm, ProfileUpdateForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated


@user_not_authenticated
def userRegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Your account has been created {user.username}")
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

@user_not_authenticated
def CustomLoginView(request):
    
    if request.method == 'POST':
        form = userLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Successfully Login in as {request.user.username}')
                return redirect('home')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    
    form =userLoginForm()

    return render(request, 'users/login.html', {'form': form})

@login_required
def CustomLogoutView(request):
    logout(request)
    messages.info(request, f'You are Logout!!')
    return redirect('home')


def CustomProfileView(request, username):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                user_form = form.save()
                messages.success(request, f"{user_form.username}, Your Profile Was Updated Successfully")
                return redirect('profile', user_form.username)
            
            for error in list(form.errors.values()):
                messages.error(request, error)

        user = get_user_model().objects.filter(username=username).first()
        if user:
            form = ProfileUpdateForm(instance=user)
            return render(request, 'users/profile.html', {'form': form})

        return redirect('home')
    return redirect('home')

