from multiprocessing import context
from django.shortcuts import render
from . models import Job
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render (request, 'job_list.html', context)

def job_detail(request ,slug):
    job_detail= Job.objects.get(slug=slug)
    context = {'job': job_detail}
    return render (request, 'job_detail.html', context)