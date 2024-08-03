from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('user/<int:pk>/', UserView.as_view()),
]