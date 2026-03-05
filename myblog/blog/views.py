import datetime
from urllib import request
from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def create(request):
    return render(request, 'create.html')

'''
def submit_blog(request):
    title1 = ''
    content1 = ''
    title1 = request.POST.get('title')
    content1 = request.POST.get('content')
    if (title1 != '') and (content1 != ''):
        newpost = Post(title=title1, body=content1)
        newpost.save()
        message = "Blog post submitted successfully."
    else:
        message = "Title and content cannot be empty."

    return render(request, 'submit_blog.html', {'message': message})'''

def submit_blog(request):
    if request.method == 'POST':
        title1 = request.POST.get('title', '').strip()
        content1 = request.POST.get('content', '').strip()
        if title1 and content1:                       # truthiness check handles None/empty
            Post.objects.create(title=title1, body=content1)
            message = "Blog post submitted successfully!"
        else:
            message = "Title and content cannot be empty."
        return render(request, 'submit_blog.html', {'message': message})
    # GET – just show the form or redirect somewhere sensible
    return redirect('create')    
    # or render(request, 'create.html')
    
   