from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [
        # Home page
        path('index/', views.index, name='index'),

        # Show all password entries
        path('entries/', views.all_entries, name='entries'),
        
        #Store a password
        path('store_entry/', views.store_password, name='store'),
        ]
