from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [
        path('store_entry/', views.store_password, name='store'),
        ]
