from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('emailconf/', views.emailconf, name='emailconf'),
    path('login/', views.login_us, name='login')
]
