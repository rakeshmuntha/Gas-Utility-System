from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'services/register.html', {'form': form})

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'services/login.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from django.shortcuts import render, redirect

@login_required
def submut(request):
    print(" Submut View Triggered!")  
    print("Request Method:", request.method)  

    if request.method == 'POST':
        print("POST Method Detected") 

        request_type = request.POST.get('request_type')
        description = request.POST.get('description')
        attachment = request.FILES.get('attachment')

        print("Request Type:", request_type)
        print("Description:", description)
        print("Attachment:", attachment)

        if request_type and description:
            ServiceRequest.objects.create(
                user=request.user,
                request_type=request_type,
                description=description,
                attachment=attachment
            )
            print("Data Saved Successfully!")
            return redirect('track_request')
        else:
            print("Form data missing or invalid.")

    return render(request, 'services/submit_request.html')

@login_required
def track_request(request):
    print("Logged-in User:", request.user) 
    requests = ServiceRequest.objects.filter(user=request.user)
    print("Filtered Requests:", requests)  
    return render(request, 'services/track_requests.html', {'requests': requests})
from django.shortcuts import render

def home(request):
    return render(request, 'services/home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'services/home.html')

def customer(request):
    return render(request, 'services/customer.html')

def admin_login(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        password = request.POST.get('password')
        user = authenticate(request, username=admin_id, password=password)

        if user is not None and user.is_superuser: 
            login(request, user)
            return redirect('/admin/') 
        else:
            messages.error(request, 'Invalid Admin ID or Password')
            
    return render(request, 'services/admin_login.html')

from django.shortcuts import render

def request_options(request):
    return render(request, 'services/request_options.html')

def submit_request(request):
    return render(request, 'services/submit_request.html')