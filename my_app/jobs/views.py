from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job


def show_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def show_single_job(request, id):
    # job = Job.objects.filter(id=id)
    job = Job.objects.get(id=id)
    return render(request, 'job_details.html', {'job': job})


def show_job_by_category(request, cid):
    jobs = Job.objects.filter(category_id=cid)
    return render(request, 'jobs.html', {'jobs': jobs})


def show_searched_jobs(request):
    key = request.GET['key']
    add = request.GET['address']
    jobs = Job.objects.filter(title__icontains=key).filter(organization__address__icontains=add)
    return render(request, 'jobs.html', {'jobs': jobs})
