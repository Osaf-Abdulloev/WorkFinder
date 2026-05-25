from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
import random
from .models import EmailConfirm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

# Create your views here.



def sendcode(user):
    
    code = random.randint(100000, 999999)
    
    EmailConfirm.objects.create(user_id = user.id, code = code) 
    
    try:
        subject = 'Confirm Your Password | JobFinder'

        from_email = settings.DEFAULT_FROM_EMAIL
        
        to = [user.email]
        
        
        text_content = f'''
        Hello {user.username}
        
        Your confirmation code is: {code}
        '''
        
        
        html_content = f'''
        <div style="
            font-family: Arial;
            max-width: 600px;
            margin: auto;
            padding: 30px;
            background: #f4f4f4;
        ">
        
            <div style="
                background: white;
                padding: 30px;
                border-radius: 12px;
            ">
        
                <h1 style="color:#2563eb;">
                    JobFinder
                </h1>
        
                <h2>
                    Password Confirmation
                </h2>
        
                <p>
                    Hello <b>{user.username}</b>,
                </p>
        
                <p>
                    Use the confirmation code below:
                </p>
        
                <div style="
                    font-size: 32px;
                    font-weight: bold;
                    letter-spacing: 5px;
                    background:#eff6ff;
                    padding:20px;
                    border-radius:10px;
                    text-align:center;
                    color:#2563eb;
                ">
                    {code}
                </div>
        
                <p style="margin-top:25px;">
                    If you did not request this email,
                    you can safely ignore it.
                </p>
        
                <hr>
        
                <p style="color:gray;">
                    © JobFinder Team
                </p>
        
            </div>
        </div>
        '''
        
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            to
        )
        
        msg.attach_alternative(html_content, "text/html")
        
        msg.send()
    except Exception as e:
         print(e, '========================================')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pas1 = request.POST.get('pas1')
        pas2 = request.POST.get('pas2')
        email = request.POST.get('email')
        role = request.POST.get('role')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')
        if request.FILES.get('img'):
            img = request.FILES.get('img')
        else:
            img = None
        
        if User.objects.filter(username = username).exists():
            return render(request, 'acc/reg.html', context={'eror' : 'Username already exists'})
        
        if pas1!=pas2:
            return render(request, 'acc/reg.html', context={'eror' : 'Password`s not equal'})
        
        if User.objects.filter(email = email).exists():
            return render(request, 'acc/reg.html', context={'eror' : f'User with email {email} already exists'})
        
        if int(age) < 18:
            return render(request, 'acc/reg.html', context={'eror' : f'You are a child comeback after {18 - int(age)} years'})
        
        user = User.objects.create_user(
            username=username,
            password=pas1,
            role=role,
            email=email,
            age = age,
            phone = phone,
            adress = adress,
            img = img)
        
        user.is_active = False
        user.save()
        
        sendcode(user)
        return redirect('emailconf')
    
    return render(request, 'acc/reg.html')
        

def emailconf(request):
    if request.method == "POST":
        username = request.POST.get('username')
        code = request.POST.get('code')
        
        user = User.objects.filter(username = username).first()
        
        if not user:
            return render(request, 'acc/emailconf.html', context={'eror' : 'Invalid username'})
        
        if not EmailConfirm.objects.filter(user = user, code = code).first():
            return render(request, 'acc/emailconf.html', context={'eror' : 'Invalid code from gmail'})
        
        user.is_active = True
        user.save()
        
        return redirect('login')
    
    return render(request, 'acc/emailconf.html')





def login_us(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pas = request.POST.get('pas')
        
        user = authenticate(request, username = username, password = pas)
        
        if not user:
            print(user)
            return render(request, 'acc/login.html', context={'eror' : 'imvalid username or password'})
        
        isnt = User.objects.filter(username = username, is_active = False).first()
        
        if isnt:
            return render(request, 'acc/login.html', context={'eror' : 'Go and confirm your email'})
        
        
        login(request, user)
        return redirect('/')
    return render(request, 'acc/login.html')


def logout_us(request):
    logout(request)
    return redirect('home')