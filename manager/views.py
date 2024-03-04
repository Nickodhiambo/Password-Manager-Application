from django.shortcuts import render
from .models import PasswordEntry
import bcrypt


def index(request):
    """Returns index page"""
    return render(request, 'manager/index.html')


def all_entries(request):
    """Returns a list of all password entries"""
    entries = PasswordEntry.objects.all()
    context = {'entries': entries}
    return render(request, 'manager/entries.html', context)


# Create your views here.
def hash_password(password):
    """Hashes and salts plain-text passwords"""
    hashed_password = bcrypt(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()


def store_password(request):
    """Stores hashed password and related account info"""
    if request.method == 'POST':
        website_name = request.POST['website_name']
        username = request.POST['username']
        password = request.POST['password']

        # Hash plaintext password
        hashed_password = hash_password(password)

        # Store entry in db
        password_entry = PasswordEntry.objects.create(
                website_name = website_name,
                username = username,
                hashed_password = hashed_password
                )
        password_entry.save()
        #Redirect to view all password entries
        return redirect('password_entries')
    else:
        # Render the form to store password
        return render(request, store_password.html)
