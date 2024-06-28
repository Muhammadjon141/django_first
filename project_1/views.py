from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login_page.html')

def register(request):
    return render(request, 'register_page.html')

def home(request):
    return render(request, 'menu.html')

def groups(request):
    return render(request, 'groups.html')

def account(request):
    return render(request, 'account.html')

def index(request):
    return render(request, 'index.html')

def endex(request):
    return render(request, 'endex.html')

def Web_sahifa(request):
    return render(request, 'Web_sahifa.html')