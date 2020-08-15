from django.shortcuts import render,get_object_or_404
from .models import job

def homepage(request):
    jobs = job.objects
    return render(request,'home.html',{'jobs':jobs})

def detail(request,job_id):
    job_detail = get_object_or_404(job,pk=job_id)
    return render (request,'detail.html',{'job':job_detail})
