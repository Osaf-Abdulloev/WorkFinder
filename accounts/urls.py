from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('emailconf/', views.emailconf, name='emailconf'),
    path('login/', views.login_us, name='login'),
    path('logout/', views.logout_us, name='logout_us'),
    path('forget/', views.forget, name='forget'),
    path('emailconf2/', views.emailconf2, name='emailconf2'),
    path('newpas/', views.newpas, name='newpas'),
    path('seek/', views.seek, name='seek')
    
]
