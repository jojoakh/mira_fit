import stripe
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Order
from .forms import OrderForm
from plan.models import Plan

# Load Stripe Secret Key from .env
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')


@login_required
def checkout(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.amount = plan.price
            order.save()
            order.plans.add(plan)

            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(plan.price * 100),
                currency="usd",
                metadata={"order_id": str(order.id)},
            )

            order.stripe_payment_intent_id = intent.id
            order.save()

            return redirect(reverse('payment', args=[order.id]))

    else:
        form = OrderForm()

    return render(request, 'checkout/checkout.html',
                  {'form': form, 'plan': plan})


@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.status == "Paid":
        return redirect(reverse('payment_success', args=[order.id]))

    # Retrieve Stripe PaymentIntent
    intent = stripe.PaymentIntent.retrieve(order.stripe_payment_intent_id)

    context = {
        'order': order,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/payment.html', context)


@login_required
def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Paid'
    order.save()
    return render(request, 'checkout/success.html', {'order': order})
