from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job
from organizations.models import Category


def show_home(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()
    return render(request, 'index.html', {'categories': categories, 'jobs': jobs})


def show_about(request):
    return render(request, 'about.html')


def show_contacts(request):
    return render(request, 'contact.html')


def show_policies(request):
    return render(request, 'policy.html')
