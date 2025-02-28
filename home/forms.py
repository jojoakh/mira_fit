from django import forms
from .models import NewsletterSubscriber, ClientReview


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'})
        }


class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = ['rating', 'comment']
