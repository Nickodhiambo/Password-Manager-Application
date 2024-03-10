from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Implements logout"""
    logout(request)
    return HttpResponseRedirect(reverse('manager:index'))

def register(request):
    """Registers a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid:
            try:
                new_user = form.save()

                #Authenticate the user
                authenticated_user = authenticate(
                        username=new_user.username,
                        password=request.POST['password1']
                        )
                # Logs in authenticated user
                login(request, authenticated_user)

                # Redirect logged in user to dashboard
                return HttpResponseRedirect(reverse('users:login'))
            
            # Handle credentials validation
            except ValueError as e:
                if 'username' in str(e):
                    form.add_error('username', str(e))
                if 'password' in str(e):
                    form.add_error('password', str(e))

    context = {'form': form}
    return render(request, 'users/register.html', context)
