from django.shortcuts import render
from blog.models import blog

def homepage(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def AboutUs(request):
    return render(request, "aboutus.html")

def Blog(request):
    blogData=blog.objects.all()

    data={
        'blogData': blogData
    }    

    return render(request, "blogs.html", data)