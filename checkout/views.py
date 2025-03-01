from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import stripe
import os
import uuid
from .models import Order
from .forms import OrderForm
from plan.models import Plan

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')


def generate_order_number():
    """Generate a unique order number."""
    return uuid.uuid4().hex.upper()


@login_required
def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    order = Order.objects.filter(user=request.user,
                                 plans=plan, status="Pending").first()
    form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.order_number = generate_order_number()
            order.amount = plan.price
            order.status = "Pending"
            order.save()
            order.plans.set([plan])

            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(plan.price * 100),
                currency="usd",
                metadata={"order_id": str(order.id)},
            )

            order.stripe_payment_intent_id = intent.id
            order.save()

            return redirect(reverse('checkout', args=[plan.id]))

    context = {
        'form': form,
        'order': order,
        'plan': plan,
        'stripe_public_key': stripe_public_key,
    }
    return render(request, 'checkout/checkout.html', context)


@login_required
def payment_success(request, order_id):
    """Handles successful payment and displays the confirmation page."""
    order = get_object_or_404(Order, id=order_id)

    if order.status != 'Paid':
        order.status = 'Paid'
        order.save()

    return render(request, 'checkout/success.html', {'order': order})
