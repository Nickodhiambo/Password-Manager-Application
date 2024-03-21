from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, default='light')

class PasswordEntry(models.Model):
    """Defines password's data structure"""
    website_url = models.URLField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'password entries'

    def __str__(self):
        """Returns a string rep of password entry"""
        return f"{self.username}-{self.website_url}-{self.password}"
