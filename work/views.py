from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from .models import *
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
# Create your views here.

def home(request):
    user = User.objects.all()
    
    return render(request, 'work/home.html', context={'us' : user})


def erorpage(request):
    return render(request, '403.html')


def all_jobs(request):
    j = Job.objects.select_related('company', 'category')
    
    return render(request, 'work/all_jobs.html', context={'j' : j})


@permission_required('work.add_job', login_url='erorpage')
def create_job(request):
    
    e = Emploeer.objects.all()
    c = Category.objects.all()
    
    if request.method == "POST":
        Job.objects.create(
            company_id = request.POST.get('company'),
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            sallary = request.POST.get('sallary'),
            location = request.POST.get('location'),
            job_type = request.POST.get('job_type'),
            exp_req = request.POST.get('exp_req'),
            category_id = request.POST.get('category'),
        )
        return redirect('all_jobs')
    return render(request, 'work/create_job.html', context={'job_types': Job.JOB_TYPE, 'c' : c, 'e' : e})


def my_jobs(request, pk):
    user = get_object_or_404(Emploeer, pk=pk)
    jobs = user.job_set.all()
    
    return render(request, 'work/my_jobs.html', context={'j' : jobs})


def search(request):
    if request.method == "GET":
        q = request.GET.get('q', '')
        
        j = Job.objects.filter( Q(title__icontains=q) | Q(category__name__icontains=q) | Q(company__company_name__icontains=q))
        
        return render(request, 'work/all_jobs.html', context={'j' : j})

@permission_required('work.change_job', login_url='erorpage')
def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    j = Job.objects.get(id = job.id)
    e = Emploeer.objects.all()
    c = Category.objects.all()
    
    
    if request.method == "POST":
        job.company_id = request.POST.get('company')
        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.sallary = request.POST.get('sallary')
        job.location = request.POST.get('location')
        job.job_type = request.POST.get('job_type')
        job.exp_req = request.POST.get('exp_req')
        job.category_id = request.POST.get('category')
        
        job.save()
        return redirect('all_jobs')
    return render(request, 'work/update_job.html', context={'job_types': Job.JOB_TYPE, 'c' : c, 'e' : e, 'j' : j})


@permission_required('work.delete_job', login_url='erorpage')
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if request.method == "POST":
        job.delete()
        return redirect('all_jobs')
    return render(request, 'work/delete_job.html', context={'j' : job})


def seeker_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    seek = Seeker.objects.filter(user_id = user.id)
    emplo = Emploeer.objects.filter(user_id = user.id).select_related('user')
    
    if seek:
        return render(request, 'work/seeker_profile.html', context={'s' : seek})
    
    if emplo:
        return render(request, 'work/emplo_profile.html', context={'e' : emplo})


@permission_required('work.add_application', login_url='erorpage')
def aplicate(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if request.method == "POST":
        Application.objects.create(
            job_id = job.id,
            user_id = request.user.id,
            sms = request.POST.get('sms'),
            resume = request.FILES.get('resume'),
            status = 'Sended'
        )
        return redirect('all_jobs')
    return render(request, 'work/aplicate.html')
    
    
    
    
    

