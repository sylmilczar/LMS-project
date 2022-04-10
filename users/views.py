from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms


def login_user_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home:home'))
    else:
        form = forms.LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            if form.cleaned_data['is_instructor'] is True:
                print('*' * 20)
                permission = Permission.objects.get(name='Can add course')
                instructor_group = Group.objects.get(name='instructors')
                user.groups.add(instructor_group)
                user.user_permissions.add(permission)
            else:
                permission = Permission.objects.get(name='Can view course')
                students_group = Group.objects.get(name='students')
                user.groups.add(students_group)
                user.user_permissions.add(permission)

            return redirect(reverse_lazy('users:login'))
    return render(request, 'users/registration.html', {'form': form})
