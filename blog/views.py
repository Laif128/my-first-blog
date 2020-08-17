from django.shortcuts import render
from django.utils import timezone
from .models import Post

#.OBJECTS kann ich machen, wenns in der selben directory ist, somit nichts weiter als Pfad angegeben werden muss!


# Create your views here.

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

#mit all werden ALLE auf der seite gezeigt