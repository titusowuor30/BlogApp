from django.shortcuts import render
from . models import Post



# Create your views here.
def index(request):
    return render(request,'index.html')

def post_detail(request):
    return render(request,'post_detail.html',{'post':Post})

def sidebar(request):
    return render(request,'sidebar.html')

