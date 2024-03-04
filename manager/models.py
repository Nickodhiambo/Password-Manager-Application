from django.db import models

# Create your models here.

class PasswordEntry(models.Model):
    """Defines password's data structure"""
    website_url = models.URLField(max_length=200)
    username = models.CharField(max_length=100)
    hashed_password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'password entries'

    def __str__(self):
        """Returns a string rep of password entry"""
        return f"{self.username} - {self.website_url}"
