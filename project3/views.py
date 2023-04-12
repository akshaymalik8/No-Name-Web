from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def AboutUs(request):
    return render(request, "aboutus.html")