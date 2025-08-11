from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(email, otp):
    subject = "Your OTP Code"
    message = f"Your OTP code is {otp}. It will expire in 5 minutes."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
