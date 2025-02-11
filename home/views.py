from django.shortcuts import render, redirect
from .forms import NewsletterForm

# Create your views here.


def home(request):
    form = NewsletterForm()  # Initialize the form
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home/home.html', {'form': form})
