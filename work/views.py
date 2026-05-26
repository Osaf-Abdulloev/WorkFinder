from django.shortcuts import render
from accounts.models import *
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.

def home(request):
    user = User.objects.all()
    
    return render(request, 'work/home.html', context={'us' : user})







