from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def index(request):
    context= {}
    return render(request, "Chatapp/index.html", context)

def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    context = {"form": form}
    return render(request, "chatapp/signup.html", context)


def signin(request):
    err = None
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        
        else:
            err = "Invalid Credentials"
        
        
    context = {"error": err}
    return render(request, "chatapp/signin.html", context)


def signout(request):
    logout(request)
    return redirect("signin")


