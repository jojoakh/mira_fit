from django import forms
from .models import UserProfile, WeightLog
# yourapp/forms.py
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        # Add your custom save logic here
        # For example, setting a custom attribute
        user.custom_attribute = 'value'
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile."""
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'image',
                  'gender', 'date_of_birth',
                  'current_weight', 'height', 'goal_weight']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class WeightLogForm(forms.ModelForm):
    """Form for adding a weight log."""
    class Meta:
        model = WeightLog
        fields = ['weight']
