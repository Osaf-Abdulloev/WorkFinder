from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from .models import *
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.

def home(request):
    user = User.objects.all()
    
    return render(request, 'work/home.html', context={'us' : user})






def create_job(request):
    
    c = Category.objects.all()
    
    if request.method == "POST":
        Job.objects.create(
            company = request.POST.get('company'),
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            sallary = request.POST.get('sallary'),
            location = request.POST.get('location'),
            job_type = request.POST.get('job_type'),
            exp_req = request.POST.get('exp_req'),
            category_id = request.POST.get('category'),
        )
        return redirect('all_jobs')
    return render(request, 'work/create_job.html', context={'job_types': Job.JOB_TYPE, 'c' : c})
