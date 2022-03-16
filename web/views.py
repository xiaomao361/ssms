import imp
from django.shortcuts import render, redirect
from django_apscheduler import models as aps_models
from django.db.models import Q

# Create your views here.

# index


def index(request):
    jobs = aps_models.DjangoJob.objects.all()
    jobs_exec_success = aps_models.DjangoJobExecution.objects.filter(
        status='Executed')
    jobs_exec_unsuccess = aps_models.DjangoJobExecution.objects.filter(
        ~Q(status='Executed'))
    return render(request, 'web/index.html',
                  {'jobs': len(jobs),
                   'jobs_exec_success': len(jobs_exec_success),
                   'jobs_exec_unsuccess': len(jobs_exec_unsuccess)})
