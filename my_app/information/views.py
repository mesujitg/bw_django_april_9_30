from django.http import HttpResponse
from django.shortcuts import render


def show_home(request):
    return render(request, 'index.html')


def show_about(request):
    return HttpResponse('About Page')


def show_contacts(request):
    return HttpResponse('Contacts Page')
