from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
import random
from .forms import SignupForm
from .utils import send_otp_email


# Generate 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))


# Step 1 → Signup Page (collect details & send OTP)
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            request.session['signup_data'] = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']
            }
            otp = generate_otp()
            request.session['otp'] = otp
            try:
                 send_otp_email(form.cleaned_data['email'], otp)  # Send email with OTP
                 messages.success(request, "OTP sent to your email.")
                 return redirect('verify_otp')  # Go to OTP page
            except Exception as e:
                print("Email Sending Failed:",e)
                print(f"your otp is:{otp}")
                messages.warning(request, "Could not send email. OTP shown in console for testing.")
    else:
        form = SignupForm()

    return render(request, "signup.html", {'form': form})


# Step 2 → OTP Verification Page
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect

def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        # Check OTP
        if entered_otp == request.session.get("otp"):
            data = request.session.get('signup_data')

            if not data:
                messages.error(request, "Signup data not found. Please start again.")
                return redirect('signup')

            # Check if username already exists
            if User.objects.filter(username=data['username']).exists():
                messages.error(request, "Username already exists. Please choose another.")
                return redirect('signup')

            # Check if email already exists if possible

            try:
                # Create the new user
                User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password']
                )
            except IntegrityError:
                messages.error(request, "An error occurred while creating your account.")
                return redirect('signup')

            # Clear session data
            request.session.pop('signup_data', None)
            request.session.pop('otp', None)

            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')  # Use URL name, not template name

        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, "otp_verify.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Django login session
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def dashboard(request):
    return render(request, "dashboard.html")


def home(request):
    return render(request, "home.html")