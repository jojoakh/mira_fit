from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, WeightLog
from .forms import UserProfileForm, WeightLogForm
from checkout.models import Order


@login_required
def profile_view(request):
    """View for displaying user profile."""
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user=request.user)
    weight_logs = WeightLog.objects.filter(user=request.user).order_by(
        '-entry_date')

    return render(request, 'profiles/profile.html', {
        'profile': profile,
        'orders': orders,
        'weight_logs': weight_logs
    })


@login_required
def edit_profile(request):
    """View for editing user profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile.user != request.user:
        messages.error(request, "You are not authorized to edit this profile.")
        return redirect('profiles:profile_view')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Your profile has been updated successfully.")
            return redirect('profiles:profile_view')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('/')  # Redirect to home after deletion
    return render(request, 'profiles/delete_profile.html')


@login_required
def add_weight_log(request):
    """View for adding a weight log."""
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            weight_log = form.save(commit=False)
            weight_log.user = request.user
            weight_log.save()
            messages.success(request, "Weight log added successfully.")
            return redirect('profiles:profile_view')
    else:
        form = WeightLogForm()

    return render(request, 'profiles/add_weight_log.html', {'form': form})
