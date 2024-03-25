from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [
        # Home page
        path('home/', views.home, name='home'),

        # Show all password entries
        path('entries/', views.all_entries, name='entries'),

        # Show a single password entry
        path('entry/<int:entry_id>/', views.entry, name='entry'),
        
        # Create a password entry
        path('store_entry/', views.store_password, name='store'),

		# Edit a password entry
        path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit'),

        # Search for an entry
        path('search/', views.search_entry, name='search_entries'),

        # Delete an entry
        path('delete/<int:entry_id>/', views.delete_entry, name='delete'),
        
]

