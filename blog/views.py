from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, template_name='blog/index.html', context={'posts':posts})

def detail(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, template_name='blog/detail.html', context={'posts':posts})


'''
from django.shortcuts import render

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html',
                  {
                      'posts': posts,
                  })

def single_pages(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/index.html',
                  {
                      'post': post,
                  })
'''

'''
from django.shortcuts import render

# Create your views here.
def landing(request): 
    return render(request, 'single_pages/landing.html',
                  context={
                      'title': 'Landing',
                      'name' : '김윤정'
                  })
'''