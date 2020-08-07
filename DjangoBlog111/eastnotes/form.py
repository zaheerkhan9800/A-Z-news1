from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='fa fa-user',
                               widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter username'}))
    password = forms.CharField(label='fa fa-lock',
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please enter password'}))

    # Verify that the username and password are correct
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Incorrect username or password')
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


# Registration form
class RegForm(forms.Form):
    username = forms.CharField(label='fa fa-user',max_length=30,min_length=3,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a 3-30 digit username '}))
    email = forms.EmailField(label='fa fa-envelope',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid email'}))
    password = forms.CharField(label='fa fa-lock',min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter atleast a 6 digits password'}))
    password_again = forms.CharField(label='fa fa-lock',min_length=6,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password again'}))

    # Verification section
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('Password did not match')
        return password

