from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm,forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':' confirm password'}),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name',"username", "email","roles",'image','address','city','state','pin','password1','password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': "form-control",'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class': "form-control",'placeholder':'User Name'}),
            'email': forms.TextInput(attrs={'class': "form-control",'placeholder':'Email '}),
            'roles': forms.Select(attrs={'class':"form-control",'placeholder':'Select'}),
            'address': forms.TextInput(attrs={'class': "form-control",'placeholder':' Address'}),
            'city': forms.TextInput(attrs={'class': "form-control",'placeholder':'City'}),
            'state': forms.TextInput(attrs={'class': "form-control",'placeholder':'State '}),
            'pin': forms.TextInput(attrs={'class': "form-control",'placeholder':'Pin Code '}),
            # 'password1': forms.PasswordInput(attrs={'class': "form-control",'type':'password','placeholder':'Password'}),
            # 'password2': forms.PasswordInput(attrs={'class': "form-control",'placeholder':'Confirm Password'}),
   
            }
        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
             )

class CustomUserChangeForm(UserChangeForm,forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name',"username", "email","roles",'image','address','city','state','pin')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
   
            }
