from django.shortcuts import render
from blog.models import blog
from django.http import HttpResponse
from userdata.models import userData

def homepage(request):
    return render(request, "index.html")

def register(request):
    try:
        # name=str(request.GET['name'])
        # email=str(request.GET['email'])
        # password=str(request.GET['password'])
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
    except:
        pass    
    return render(request, "form.html")

def AboutUs(request):
    return render(request, "aboutus.html")

def saveform(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=userData(name=name,email=email,password=password,)
        data.save()    
    return render(request, "form.html")

def Blog(request):
    blogData=blog.objects.all()

    data={
        'blogData': blogData
    }    

    return render(request, "blogs.html", data)