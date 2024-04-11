from django.urls import path
from .views import random_quote,add_quote
urlpatterns = [
    # Your other URLs...
    path('random-quote/', random_quote, name='random-quote'),
    path('add-quote/', add_quote, name='add-quote'),
]
