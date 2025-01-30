from django.shortcuts import render
from . models import Post



# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post_detail(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})

def sidebar(request):
    return render(request,'sidebar.html')

