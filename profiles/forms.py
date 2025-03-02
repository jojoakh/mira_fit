from django import forms
from .models import UserProfile, WeightLog
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 label="First Name")
    last_name = forms.CharField(max_length=30, required=True,
                                label="Last Name")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "phone_number", "address", "gender",  "date_of_birth",
            "current_weight", "height", "goal_weight"
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date",
                                                    "class": "form-control"}),
            "address": forms.Textarea(attrs={"rows": 3,
                                             "class": "form-control"}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits.")
        if len(phone_number) < 8 or len(phone_number) > 15:
            raise forms.ValidationError(
                "Phone number must be between 8 and 15 digits.")
        return phone_number

    def clean_current_weight(self):
        weight = self.cleaned_data.get("current_weight")
        if weight is not None and weight <= 0:
            raise forms.ValidationError("Weight must be greater than 0.")
        return weight

    def clean_height(self):
        height = self.cleaned_data.get("height")
        if height is not None and height <= 0:
            raise forms.ValidationError("Height must be greater than 0.")
        return height

    def clean_goal_weight(self):
        goal_weight = self.cleaned_data.get("goal_weight")
        if goal_weight is not None and goal_weight <= 0:
            raise forms.ValidationError("Goal weight must be greater than 0.")
        return goal_weight


class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = ["weight"]

    def clean_weight(self):
        weight = self.cleaned_data.get("weight")
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than 0.")
        return weight
