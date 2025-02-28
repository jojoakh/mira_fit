from django import forms
from .models import UserProfile, WeightLog
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
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
