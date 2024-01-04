from django.shortcuts import render, HttpResponse
from .models import Blog_data
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    if request.method=="POST":
        title=request.POST.get('title')
        details=request.POST.get('details')
        submit_blog=Blog_data(title=title,details=details,date=datetime.today())
        submit_blog.save()
        confirm=messages.success(request,'Your Blog has been post successfully!')
    return render(request,'index.html')

def blogs(request):
    blogs=Blog_data.objects.all()
    return render(request,'blogs.html',{'blog':blogs})

def single(request,val):
    tab=Blog_data.objects.get(id=val)
    return render(request,'single.html',{'valu':tab})