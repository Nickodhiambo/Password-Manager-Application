from django.shortcuts import render, redirect
from .models import PasswordEntry
from .forms import PasswordEntryForm
from django.http import HttpResponseRedirect, Http404, HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import string
import random
from django.http import HttpResponseRedirect




def home(request):
    """Returns index page"""
    return render(request, 'manager/home.html')

def generate_password(length=8):
    """Generates a random 8-character string"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


@login_required
def all_entries(request):
    """Returns a list of all password entries"""
    entries = PasswordEntry.objects.filter(owner=request.user).values_list('id', 'website_url')
    context = {'entries': entries}
    return render(request, 'manager/entries.html', context)


@login_required
def entry(request, entry_id):
    """Retrieves a single entry by ID"""
    entry = PasswordEntry.objects.get(id=entry_id)
    if entry.owner != request.user:
        raise Http404
    entry_fields = {
        'id': entry.id,
        'website_url': entry.website_url,
        'username': entry.username,
        'password': entry.password
    }
    context = {'entry_fields': entry_fields}
    return render(request, 'manager/entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit a password entry"""
    entry = PasswordEntry.objects.get(id=entry_id)
    if entry.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Prefill the form with existing entry before update
        form = PasswordEntryForm(instance=entry)
    else:
        form = PasswordEntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # Save updates
            form.save()
            return HttpResponseRedirect(reverse('manager:entries'))
        
    entry_fields = {
        "id": entry.id,
        "website_url": entry.website_url,
        "username": entry.username,
        "password": entry.password
    }

    context = {'entry_fields': entry_fields, 'form': form}
    return render(request, 'manager/edit_entry.html', context)


@login_required
def store_password(request):
    """Stores hashed password and related account info"""
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        
        if form.is_valid:
            #Create an instance without saving
            password_entry = form.save(commit=False)

            #Associate a new entry with current user
            password_entry.owner = request.user
            password_entry.save()

            #Redirect to view all password entries
            return HttpResponseRedirect(reverse('manager:entries'))
    else:
        form = PasswordEntryForm()
    # Render the form to process new password entries
    context = {'form': form}
    return render(request, 'manager/store_password.html', context)


@login_required
def search_entry(request):
    """Searches for a password entry by site name"""
    query = request.GET.get('q')
    if query:
        entries = PasswordEntry.objects.filter(website_url__icontains=query, owner=request.user).values_list('id', 'website_url')
    else:
        entries = PasswordEntry.objects.filter(owner=request.user).values_list('id', 'website_url')
    context = {'entries': entries}
    return render(request, 'manager/search_entries.html', context)


@login_required
def delete_entry(request, entry_id):
    """Deletes a password entry"""
    entry = PasswordEntry.objects.get(id=entry_id)
    if entry.owner != request.user:
        raise Http404
    else:
        entry.delete()
        return HttpResponseRedirect(reverse('manager:entries'))
    context = {'entry': entry}
    return render(request, 'manager/entry.html', context)

