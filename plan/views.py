from django.shortcuts import render
from .models import Plan

# Create your views here.


def plan(request):
    plans = Plan.objects.all()
    return render(request, 'plan/plan.html', {'plans': plans})
