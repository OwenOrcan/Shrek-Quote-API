from django.urls import path
from .views import random_quote,add_quote, put_all_data
urlpatterns = [
    # Your other URLs...
    path('random-quote/', random_quote, name='random-quote'),
    path('add-quote/', add_quote, name='add-quote'),
    path('put-all-data/', put_all_data, name='put-all-data'),
]
