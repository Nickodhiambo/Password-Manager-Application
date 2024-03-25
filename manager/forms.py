from django import forms
from .models import PasswordEntry, UserProfile


class PasswordEntryForm(forms.ModelForm):
    """A form to allow a user enter password details"""
    class Meta:
        model = PasswordEntry
        fields = ['website_url', 'username', 'password']


class ThemeToggleForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["theme"]
