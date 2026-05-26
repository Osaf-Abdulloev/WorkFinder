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
    
    
    def __str__(self):
        return self.company_name
    
    


class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    exp = models.PositiveIntegerField()
    edu = models.CharField(max_length=50)
    burth_date = models.DateField()
    adress = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.user.username} || {self.bio}'
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

