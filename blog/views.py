from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from chatbot import models
from .models import TradeSimulation 
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
def chatbot_view(request):
    if request.method == "GET":
        return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\chatbot.html') 
def chatbot_personality_view(request):
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\.rasa')
def simulator_view(request):
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\simulator.html')  
def simulate_trade(request):
    if request.method == 'POST':
        asset = request.POST.get('asset')
        side = request.POST.get('side')
        amount = request.POST.get('amount')

        # Simulate trade logic here (you can add more sophisticated logic if needed)
        # For now, let's just log the trade
        trade_price = 100  # You can fetch real prices from an API, for example

        # Create a new trade entry (you can save this to the database)
        trade = TradeSimulation.objects.create(
            user=request.user,
            asset=asset,
            side=side,
            amount=amount,
            price=trade_price
        )

        # Optionally, return a success message or redirect
        return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\simulator.html', {
            'trade_history': [trade],  # Add the trade to the trade history display
            'virtual_balance': 10000,  # Update this dynamically if needed
        })

   
    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\simulator.html')
# views.py
import requests
from django.http import JsonResponse

def get_stock_data(request):
    symbol = request.GET.get("symbol", "TSLA")
    api_key = "7f6144de083b407b990bc7f6effcbda7"
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={api_key}&outputsize=30"

    r = requests.get(url)
    return JsonResponse(r.json())

