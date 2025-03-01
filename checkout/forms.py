from django import forms
from .models import Order
import re


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'required': 'required'}),
        }
        error_messages = {
            'full_name': {'required': "Full Name is required."},
            'email': {'required': "Email is required.",
                      'invalid': "Enter a valid email address."},
            'phone_number': {'required': "Phone number is required."},
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not full_name:
            raise forms.ValidationError("Full Name cannot be empty.")
        if not re.match(r"^[A-Za-z\s]+$", full_name):
            raise forms.ValidationError(
                "Full Name should only contain letters.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please provide a valid email.")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        if not phone_number.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits.")
        if len(phone_number) < 8 or len(phone_number) > 15:
            raise forms.ValidationError(
                "Phone number must be between 8 and 15 digits.")
        return phone_number
