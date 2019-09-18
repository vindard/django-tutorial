from django.shortcuts import render

posts = [
    {
        'author': 'vindard',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 18, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Sep 19, 2019'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
