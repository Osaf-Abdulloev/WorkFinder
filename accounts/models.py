from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    role_choice =[
        ('Seeker', 'seeker'),
        ('Employer', 'employer')
    ]
    
    role = models.CharField(choices=role_choice)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=13)
    adress = models.CharField(max_length=30, null=True, blank=True)
    img = models.ImageField(upload_to='users/')
    create_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.username} || {self.role}'
