from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [
        # Home page
        path('index/', views.index, name='index'),

        # Show all password entries
        path('entries/', views.all_entries, name='entries'),

        # Show a single password entry
        path('entry/<int:entry_id>/', views.entry, name='entry'),
        
        #Create a password entry
        path('store_entry/', views.store_password, name='store'),

		# Edit a password entry
        path('edit_entry/<int:entry_id>/', views.edit_entry, name='entry'),
]
