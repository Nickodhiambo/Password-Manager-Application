from django import forms
from .models import PasswordEntry


class PasswordEntryForm(forms.ModelForm):
    """A form to allow a user enter password details"""
    class Meta:
        model = PasswordEntry
        fields = ['website_url', 'username', 'password']
