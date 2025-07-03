from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chatbot import models

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('dashboard')
    return render(request, 'signup.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\mainpage.html',{'posts': posts})
def chart_news_view(request):
    return render(request, 'chart_news.html')
def chatbot_personality_view(request):
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\chatbot.html')
def simulator(request):
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\simulator.html')
