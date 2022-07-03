from django.shortcuts import render


def show_jobs(request):
    return render(request, 'jobs.html')


def show_single_job(request):
    pass


def show_job_by_category(request):
    return render(request, 'jobs.html')


def show_searched_jobs(request):
    return render(request, 'jobs.html')
