from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        # Get user details from the form
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')  # Added email
        contact_no = request.POST.get('contact_no')
        Gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        educational_status = request.POST.get('educational_status')
        university = request.POST.get('university')
        residential_adress = request.POST.get('residential_adress')
        

        # Get password and confirm password
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check if the username already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Check if the email already exists
        if CustomUser.objects.filter(email=email).exists():  # Email uniqueness check
            messages.error(request, 'Email already exists.')
            return redirect('register')

        # Create and save new user
        try:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,  # Added email
                contact_no=contact_no,
                Gender=Gender,
                date_of_birth=date_of_birth,
                educational_status=educational_status,
                university=university,
                residential_adress=residential_adress,
        
                password=password,  # Pass the password directly here
            )
            user.save()

            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error during registration: {e}')
            return redirect('register')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log in the user
            auth_login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('index')  # Redirect to homepage or another page after login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def index(request):
    return render(request, 'index.html')
