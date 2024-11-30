from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('submit_request')  # Redirect to a page after login
            else:
                # Authentication failed
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your service request has been submitted successfully!')
            return redirect('track_requests')  # Redirect to track requests page after submission
    else:
        form = ServiceRequestForm()
    return render(request, 'services/submit_request.html', {'form': form})




# services/views.py
from django.shortcuts import render
from .models import ServiceRequest

# services/views.py
from django.contrib.auth.decorators import login_required

@login_required
def track_requests(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/track_requests.html', {'service_requests': service_requests})
