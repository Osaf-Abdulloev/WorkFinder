from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_job/', views.create_job, name='create_job'),
    path('all_jobs/', views.all_jobs, name='all_jobs'),
    path('update_job/<int:pk>', views.update_job, name='update_job'),
    path('seeker_profile/<int:pk>', views.seeker_profile, name='seeker_profile'),
    path('delete_job/<int:pk>', views.delete_job, name='delete_job'),
    path('erorpage', views.erorpage, name='erorpage'),
    path('my_jobs/<int:pk>', views.my_jobs, name='my_jobs'),
    path('search/', views.search, name='search'),
    path('aplicate/<int:pk>', views.aplicate, name='aplicate'),
    path('aplications/', views.aplications, name='aplications'),
    path('aplicationss/', views.aplicationss, name='aplicationss'),
    path('update_app/<int:pk>', views.update_app, name='update_app'),
    path('delete_app/<int:pk>', views.delete_app, name='delete_app')
]
