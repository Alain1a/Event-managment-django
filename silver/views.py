from django.shortcuts import render
from .models import Event

# Create your views here.


def home(request):
    selectdata = Event.objects.all()
    return render(request, 'home.html')

def Register(request):
    return render(request, 'Register.html')

def Login(request):
    return render(request, 'Login.html')

def Signup(request):
    return render(request, 'Create account.html')

def Create_new_account(request):
    return render(request, 'Create account.html')

def Forgot_Passward(request):
    return render(request, 'Reset Passward.html')


# def Forgot(request):
    return render(request, 'Reset Passward.html')

def about_us(request):
    return render(request, 'About Us.html')

# def login(request):
#     return render(request, 'Book Your Ticket.html')






