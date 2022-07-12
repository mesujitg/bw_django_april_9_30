from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from jobseekers.models import JobSeeker


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['username']
        pw = make_password(request.POST['password'])

        obj = request.POST['objective']
        cv = request.FILES['cv']
        image = request.FILES['image']

        user = User(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()

        js = JobSeeker(user=user, objective=obj, qualification='', training='', skills='',
                       experience='', cv=cv, image=image)
        js.save()

        return HttpResponse('Ok')

    return HttpResponse('Invalid Access')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Wrong credentials!')

    return HttpResponse('Invalid access!')


def logout(request):
    auth.logout(request)
    return redirect('home')
