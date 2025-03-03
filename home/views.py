from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.forms import NewsletterForm, ClientReviewForm
from home.models import ClientReview


def home(request):
    """
    Home page view with newsletter subscription handling and latest reviews.
    """
    if request.method == 'POST' and request.POST.get(
                                        'form_type') == 'newsletter':
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
                    messages.error(request, f"{field.capitalize()}: {error}",
                                   extra_tags='newsletter')

    # Get latest approved reviews
    reviews = ClientReview.objects.filter(approved=True).order_by(
                                        '-created_at')[:3]

    context = {
        'newsletter_form': NewsletterForm(),
        'reviews': reviews
    }
    return render(request, 'home/home.html', context)


@login_required
def client_reviews(request):
    """Allow logged-in users to submit a review"""
    reviews = ClientReview.objects.filter(approved=True)

    if request.method == 'POST':
        form = ClientReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request,
                             "Review submitted and awaits approval.")
            return redirect('client_reviews')
    else:
        form = ClientReviewForm()

    context = {
        'reviews': reviews,
        'form': form
    }
    return render(request, 'home/client_reviews.html', context)
