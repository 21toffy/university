from django import forms
from django.contrib.auth.forms import UserChangeForm
from user.models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class userUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get("password2")
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('passwords do not match lol')
        return self.cleaned_data

    def clean_email(self):
        email= self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('damn it this email already exists ')
        return email

    def clean_username(self):
        username= self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('damn it this username already exists ')
        return username 
    class Meta:
        model = User
        fields = ('username', 'email','password', 'password2')


class profileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('level','bio', 'profile_pic','matric','first_name','Last_name')


class MatricUpdateForm(forms.ModelForm):
    matric = forms.IntegerField(required=False, help_text='You wouldnt be able to change your matric number laterwhich can attract severe penalties. so enter your valid matric number')
    class Meta:
        model = Profile
        fields = ( 'matric',)

        
        



class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get("password2")
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('passwords do not match lol')
        return self.cleaned_data

    def clean_email(self):
        email= self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('damn it this email already exists ')
        return email

    def clean_username(self):
        username= self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('damn it this username already exists ')
        return username