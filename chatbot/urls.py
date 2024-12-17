from django.urls import path
from .views import chat_home, chat_message

app_name = 'chatbot'

urlpatterns = [
    path('', chat_home, name='chat_home'),
    path('chat_message/', chat_message, name='chat_message'),
]