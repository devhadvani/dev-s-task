from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":

        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():

            user = form.save(commit  = False)
            user.username = user.username.lower()
            user.save()
            print(user)
            return redirect('log')
  
    return render(request,"register.html",{'form':form})


def log(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Invalid Username or Password')
            return redirect('log')



    else:
        return render(request, 'login.html')
    return render(request,'login.html')

def logout_form(request):
    logout(request)
    return redirect('home')