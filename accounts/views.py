from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# User login view


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Debugging: Check if username and password are being correctly received
        print(f"Username: {username}, Password: {password}")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('index')  # Redirect to home page or another page
            else:
                messages.error(request, 'Your account is inactive.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    # If GET request or login fails
    return render(request, 'accounts/login.html')

# User registration view
def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Print the registration attempt details for debugging
        print(f"Signup attempt with Username: {username}, Email: {email}, Password: {password}")

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'accounts/register.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        # Check if email already exists
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            # Create and save the new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False  # You can change this to True if you want to activate directly
            user.save()
            messages.success(request, "User registered successfully. Please login.")
            return redirect('user_login')  # Redirect to login page after successful registration

    return render(request, 'accounts/register.html')


# User logout view
def user_logout(request):
    logout(request)
    return redirect('/')  # Redirect to the homepage after logout
