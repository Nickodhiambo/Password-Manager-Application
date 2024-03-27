from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
import os

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

    print(os.environ)

    if request.method == "POST":
      name = request.POST.get("name")
      message = request.POST.get("message")
      email = request.POST.get("email")
      
      if name and message and email:
        subject = f"Contact from {name}"
        message = f"Message from {name} using email {email}\n\n{message}\n\nThank you."
        from_email = os.environ.get('EMAIL_HOST_USER')
        
        try:
            res = send_mail(subject, message, from_email, [from_email])
            print(res)
        except BadHeaderError:
            return redirect(to="/public/contact?status=error")
        return redirect(to="/public/contact?status=success")
      else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return redirect(to="/public/contact?status=error")    
    
    status = request.GET.get('status')    
    return render(request, 'contact.html', {"status":status})


def contribution(request):
    """Returns contribution page"""
    return render(request, 'contribution.html')

