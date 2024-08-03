from django.urls import path
from .views import *

urlpatterns = [
    path('name/<str:name>/', SearchByName.as_view()),
    path('bank/<str:account>/', SearchByBankAc.as_view()),
    path('phone/<str:number>/', SearchByPhone.as_view()),
    path('citizenship/<str:number>/', SearchByCitizenship.as_view()),
]