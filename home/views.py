from django.shortcuts import render, redirect
from django.contrib import messages
from home.forms import NewsletterForm


def home(request):
    """
    Home page view with newsletter subscription handling.
    """
    # Handle newsletter form submission
    if request.method == 'POST' and request.POST.get('form_type') == 'newsletter':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Successfully subscribed to the newsletter!",
                             extra_tags='newsletter')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request,
                                   f"{field.capitalize()}: {error}",
                                   extra_tags='newsletter')

    # Pass context (must be a dictionary)
    context = {
        'newsletter_form': NewsletterForm()
    }
    return render(request, 'home/home.html', context)
