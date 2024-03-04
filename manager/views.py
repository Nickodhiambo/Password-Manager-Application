from django.shortcuts import render
from .models import PasswordEntry
from .forms import PasswordEntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import bcrypt


def index(request):
    """Returns index page"""
    return render(request, 'manager/index.html')


def all_entries(request):
    """Returns a list of all password entries"""
    entries = PasswordEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'manager/entries.html', context)


def hash_password(password):
    """Hashes and salts plain-text passwords"""
    hashed_password = bcrypt(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()


def store_password(request):
    """Stores hashed password and related account info"""
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        
        if form.is_valid:
            website_name = form['website_url']
            username = form['username']
            password = form['password']

            # Hash plaintext password
            hashed_password = hash_password(password)

            # Create and save a password entry instance
            password_entry = form.save(commit=False) #Create an instance without saving
            password_entry.password = hashed_password
            password_entry.save()

            #Redirect to view all password entries
            return HttpResponseRedirect(reverse('manager:entries'))
    else:
        form = PasswordEntryForm()
    # Render the form to process new password entries
    context = {'form': form}
    return render(request, 'manager/store_password.html', context)
