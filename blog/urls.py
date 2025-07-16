from django.urls import path, include
from . import views
from chatbot.views import chatbot_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', include('chatbot.urls')),
    path('chart-news/', views.chart_news_view, name='chart_news'),
    path('chatbot-personality/', views.chatbot_personality_view, name='chatbot_personality'),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('simulator/',views.simulate_trade,name='simulator'),
]