from django.shortcuts import render
from .models import PasswordEntry
from .forms import PasswordEntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import bcrypt


def index(request):
    """Returns index page"""
    return render(request, 'manager/index.html')


@login_required
def all_entries(request):
    """Returns a list of all password entries"""
    entries = PasswordEntry.objects.filter(owner=request.user)
    context = {'entries': entries}
    return render(request, 'manager/entries.html', context)


@login_required
def entry(request, entry_id):
    """Retrieves a single entry by ID"""
    entry = PasswordEntry.objects.get(id=entry_id)
    context = {'entry': entry}
    return render(request, 'manager/entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit a password entry"""
    entry = PasswordEntry.objects.get(id=entry_id)
    if request.method != 'POST':
        # Prefill the form with existing entry before update
        form = PasswordEntryForm(instance=entry)
    else:
        form=PasswordEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # Create an instance of the update without saving
            password_entry = form.save(commit=False)
            
            #Hash the plaintext password
            hashed_password = hash_password(password_entry.password)
            
            #Update password field with hashed password
            password_entry.password = hashed_password

            return HttpResponseRedirect(reverse('manager:entries'))

    context = {'entry': entry, 'form': form}
    return render(request, 'manager/edit_entry.html', context)

def hash_password(password):
    """Hashes and salts plain-text passwords"""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()


@login_required
def store_password(request):
    """Stores hashed password and related account info"""
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        
        if form.is_valid:
            #Create an instance without saving
            password_entry = form.save(commit=False)
            
            # Hash plaintext password
            hashed_password = hash_password(password_entry.password)

            # Update the password field with hashed password
            password_entry.password = hashed_password
            password_entry.save()

            #Redirect to view all password entries
            return HttpResponseRedirect(reverse('manager:entries'))
    else:
        form = PasswordEntryForm()
    # Render the form to process new password entries
    context = {'form': form}
    return render(request, 'manager/store_password.html', context)
