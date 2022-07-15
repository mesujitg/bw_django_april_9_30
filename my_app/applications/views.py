from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from applications.models import Application
from jobs.models import Job


@login_required
def apply(request, jid):
    if request.user.is_staff:
        messages.warning(request, 'This url is not applicable for your role')
    elif request.user.role == 'Employee':
        job = Job.objects.get(id=jid)
        app = Application.objects.filter(user=request.user).filter(job=job)
        if app:
            messages.success(request, 'You have already applied for the job')
            return redirect('jobs')
        app = Application(user=request.user, job=job, status='applied')
        # app = Application(user_id=request.userid., job=jid, status='applied')
        app.save()
        messages.success(request, 'You have applied for the job')
    else:
        messages.warning(request, 'This url is not applicable for your role')

    return redirect('jobs')


