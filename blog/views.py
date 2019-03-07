from django.shortcuts import render

posts = [
    {
        'author': 'corey ms',
        'title': "blog post 1",
        'content': 'asdfg fgh',
        'date_posted': 'August 27 2018'
    },
    {
        'author': 'bendeh',
        'title': "blog post 2",
        'content': 'allah wakubar',
        'date_posted': 'August 27 2017'
    }
]


def home(request):  # must take the response argument
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
