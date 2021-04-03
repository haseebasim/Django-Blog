from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {'author': "William Scott",
     "title": "blog post 1",
     "content": "First post content",
     "date_posted": "August 20, 2018"},

    {'author': "Jane Doe",
     "title": "blog post 2",
     "content": "Second post content",
     "date_posted": "August 28, 2018"}
]


def home(request):

    context = {
        "posts": Post.objects.all()
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title" : "About"})
