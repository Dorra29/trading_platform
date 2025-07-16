from django.urls import path
from .views import chatbot_view
from . import views

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot'),
]