from django.urls import path
from .views import CreateMessage, ReceiveMessage

urlpatterns = [
    path('message/', CreateMessage.as_view()),
    path('message_confirmation/', ReceiveMessage.as_view()),
    # path('createuser/', CreateUser.as_view()),
]