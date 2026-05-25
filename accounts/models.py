from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.



class EmailConfirm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.user.username
    


class User(AbstractUser):
    role_choice =[
        ('seeker', 'Seeker'),
        ('employer', 'Employer')
    ]
    
    role = models.CharField(max_length=25,choices=role_choice, null=True, blank=True )
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=13,null=True, blank=True)
    adress = models.CharField(max_length=30, null=True, blank=True)
    img = models.ImageField(upload_to='users/', default='def.jpg',null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.username} || {self.role}'
