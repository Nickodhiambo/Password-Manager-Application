from django.shortcuts import render, redirect


def home(request):
    """Returns index page"""
    return render(request, 'home.html')


def services(request):
    """Returns services page"""
    return render(request, 'services.html')


def landing(request):
    """Returns landing page"""
    return render(request, 'landing.html')


def contact(request):
    """Returns contact page"""
    return render(request, 'contact.html')


def contribution(request):
    """Returns contribution page"""
    return render(request, 'contribution.html')

