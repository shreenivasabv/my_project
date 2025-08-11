from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken.")
        return username


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)
