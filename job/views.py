from multiprocessing import context
from django.shortcuts import redirect, render
from . models import Job
from django.core.paginator import Paginator
from .form import ApplyForm 
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    x = Paginator(job_list,1)
    page_number = request.GET.get('page')
    job_obj = x.get_page(page_number)


    context = {'jobs': job_obj }
    return render (request, 'job_list.html', context)

def job_detail(request ,slug):
    job_detail= Job.objects.get(slug=slug)

    if request.method == 'POST':
      
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job = job_detail 
            myform.save()
            
           
        

    else:
          form = ApplyForm()
                


    context = {'job': job_detail , 'form': form}
    return render (request, 'job_detail.html', context)