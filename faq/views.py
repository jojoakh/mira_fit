from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq_list(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, "faq/faq_list.html", {"faqs": faqs})
