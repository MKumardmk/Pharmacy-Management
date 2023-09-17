from django import forms
from .models import Category
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class LoginForm(forms.Form):
    email= forms.EmailField(label='',required=True,widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    password= forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))


class RegisterForm(forms.Form):
    name= forms.CharField(label='',required=True,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Full Name"}))
    email= forms.EmailField(label='',required=True,widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    password= forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    cpassword= forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))

    def clean_email(self):
        email=self.cleaned_data.get('email')
        user=User.objects.filter(username=email).first()
        if user:
            raise ValidationError('Email is already registered')
        return email


class ForgotPasswordForm(forms.Form):
    email=forms.EmailField(label='Email', required=True,widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Email'}))

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email:
            user= User.objects.filter(Q(username__iexact=email)| Q(email__iexact=email)).first()
            if user is None:
                raise ValidationError('The given email address is not registered with Topone')
        return email