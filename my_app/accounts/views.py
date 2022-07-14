from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from accounts.models import User
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

        # org = Organization()
        # org.save()

        # orgusr = OrgUser(org=org, user=user)
        # orgusr.save()

        messages.success(request, 'User Registered Successfully')
        return redirect('login')

    messages.error(request, 'Invalid Access')
    return redirect('register')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('home')
        else:
            messages.error(request, 'Wrong credentials!')
            return redirect('login')

    messages.error(request, 'Invalid Access')
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def profile(request):
    # if request.user.is_authenticated:
    #     jobseeker = JobSeeker.objects.get(user=request.user)
    #     return render(request, 'profile.html', {'js': jobseeker})
    #
    # messages.error(request, 'Invalid Access! You must Login First')
    # return redirect('login')

    jobseeker = JobSeeker.objects.get(user=request.user)
    return render(request, 'profile.html', {'js': jobseeker})