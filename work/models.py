from django.db import models
from accounts.models import User

# Create your models here.

class Emploeer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    about = models.TextField()
    logo = models.ImageField(upload_to='companylogos/')
    location = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    is_creat = models.BooleanField(default=False, null=True, blank=True)
    
    
    def __str__(self):
        return self.company_name
    
    


class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seekerprogile')
    bio = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    exp = models.PositiveIntegerField()
    edu = models.CharField(max_length=50)
    burth_date = models.DateField()
    adress = models.CharField(max_length=50)
    is_creat = models.BooleanField(default=False, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} || {self.bio}'
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    



class Job(models.Model):
    JOB_TYPE = [
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('freelance', 'Freelance')
    ]
    
    company = models.ForeignKey(Emploeer, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    sallary = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=25, choices=JOB_TYPE)
    exp_req = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title



class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sms = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self):
        return self.job.title
    
    


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user.username} || {self.job.title}'
    
    
    

