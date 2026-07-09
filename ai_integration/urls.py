from django.urls import path

from ai_integration import views
from .views import *

urlpatterns = [
    path("chat/", chat_ai, name="chat_ai"),
]