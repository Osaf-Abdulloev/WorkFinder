from django import forms
from .models import *




class AplicateForm(forms.Form):
    sms = forms.CharField(
     widget = forms.Textarea(attrs={'class' : 'sms'}),
     required = True
    )
    
    resume = forms.FileField(
        required = True,
        label = "Your resume",
        widget = forms.FileInput(attrs = {'class' : 'resume-aplicate'})
    )
    
    
