from django.http import HttpResponse
from django.shortcuts import render
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
        pw = request.POST['password']

        user = User(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()

        js = JobSeeker(user=user, objective='', qualification='', training='', skills='',
                       experience='', cv='', image='')
        js.save()

        return HttpResponse('Ok')

    return HttpResponse('Invalid Access')
