from django.shortcuts import render, get_object_or_404
from plan.models import Plan
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    return render(request, 'checkout/checkout.html', {'plan': plan})
