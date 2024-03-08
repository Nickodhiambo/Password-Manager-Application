from django.shortcuts import render
from .models import PasswordEntry
from .forms import PasswordEntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import string
import random


def index(request):
    """Returns index page"""
    return render(request, 'manager/index.html')


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
    context = {'entry': entry}
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
            password_entry = form.save()

            return HttpResponseRedirect(reverse('manager:entries'))

    context = {'entry': entry, 'form': form}
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


def search_entry(request):
    """Searches for a password entry by site name"""
    query = request.GET.get('q')
    if query:
        entries = PasswordEntry.objects.filter(website_url__icontains=query, owner=request.user)
    else:
        entries = PasswordEntry.objects.filter(owner=request.user)
    context = {'entries': entries}
    return render(request, 'manager/search_entries.html', context)


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
