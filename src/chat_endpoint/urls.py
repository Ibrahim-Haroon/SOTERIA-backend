from django.urls import path
from .views import ChatEndpointView

urlpatterns = [
    path('chat_endpoint/', ChatEndpointView.as_view(), name='chat-endpoint'),
]