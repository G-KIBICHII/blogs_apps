from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# data

posts=[
    {
        'author':'courey',
        'title':'blog post 1',
        'content':'first post',
        'date_posted':'May 24, 2024'
    },

     {
        'author':'jane doe',
        'title':'blog post 2',
        'content':'second post',
        'date_posted':'May 24, 2024'
    },
      {
        'author':'jane doe',
        'title':'blog post 2',
        'content':'second post',
        'date_posted':'May 24, 2024'
    }
]

# Create your views here.
def home(request):
    context ={
        # 'posts':posts
        'posts':Post.objects.all()
    }
    return render(request, 'blogs/home.html',context)

def about(request):
    return render(request,'blogs/about.html',{'title':'about'})
