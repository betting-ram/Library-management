from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from  django.core.exceptions import ValidationError
from .models import *
from django import forms

class Studentform(forms.Form):
   # student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter student id'}),required=True, max_length=50)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),  required=True, max_length=50)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}), required=True, max_length=50)
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter department'}), required=True, max_length=50)
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter section'}), required=True),
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter year'}), required=True)
    picture = forms.ImageField()

   # def clean_student_id(self):
   #    sid = self.cleaned_data['student_id']
   #    qs = Student.objects.filter(student_id = sid)
   #    if qs.exists():
   #      raise ValidationError("Id is already taken")
   #    return sid


'''
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
'''
'''
    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Email is already registered.')
        return email


    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords Do Not Match')
'''