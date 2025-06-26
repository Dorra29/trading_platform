from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\templates.html',{'posts': posts})