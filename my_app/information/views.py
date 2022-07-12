from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from information.models import Information
from jobs.models import Job
from organizations.models import Category


def show_home(request):
    jobs = Job.objects.all()

    cursor = connection.cursor()
    cursor.execute('SELECT category_id, count(*) FROM jobs_job GROUP BY category_id')
    counts = cursor.fetchall()
    
    return render(request, 'index.html', {'jobs': jobs, 'counts': counts})


def show_about(request):
    # about = Information.objects.filter(section_id=1)
    about = Information.objects.filter(section__title='About')
    return render(request, 'about.html', {'about': about})


def show_contacts(request):
    return render(request, 'contact.html')


def show_policies(request):
    return render(request, 'policy.html')
