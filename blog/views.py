from django.shortcuts import render
from .models import Post


#posts = [
#    {
#        'author': 'stefan',
#        'title': 'tak',
#        'content': 'abc',
#        'date_posted': 'august 27, 2018'
#    },
#
#    {
#        'author': 'ziom',
#        'title': 'nie',
#        'content': 'cba',
#        'date_posted': 'august 12, 2018'
#    }
#]

def home(request):
    context = {
        #'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
