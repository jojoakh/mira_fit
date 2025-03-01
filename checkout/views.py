from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import stripe
import uuid
from .models import Order
from .forms import OrderForm
from plan.models import Plan


def generate_order_number():
    """Generate a unique order number."""
    return uuid.uuid4().hex.upper()


@login_required
def checkout(request, plan_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    plan = get_object_or_404(Plan, id=plan_id)
    form = OrderForm(request.POST or None)
    intent = None

    existing_order = Order.objects.filter(user=request.user,
                                          plans=plan, paid=True).exists()

    if existing_order:
        messages.warning(request, "You have already purchased this plan.")
        return redirect('plan')  # Redirect to the plans page

    order = Order.objects.filter(user=request.user, plans=plan).first()

    if not order:
        order = Order(
            user=request.user,
            order_number=generate_order_number(),
            amount=plan.price,
            full_name=request.user.get_full_name() or request.user.username,
            email=request.user.email
        )
        order.save()
        order.plans.set([plan])

    # ✅ Always create a PaymentIntent if it does not exist
    if not order.stripe_payment_intent_id:
        intent = stripe.PaymentIntent.create(
            amount=int(plan.price * 100),
            currency="usd",
            metadata={"order_id": str(order.id)},
        )
        order.stripe_payment_intent_id = intent.id
        order.save()
    else:
        intent = stripe.PaymentIntent.retrieve(order.stripe_payment_intent_id)

    # ✅ If intent still does not exist, set a default value to avoid crashes
    client_secret = intent.client_secret if intent else ""

    context = {
        'form': form,
        'plan': plan,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,  # ✅ Ensure this is passed correctly
    }
    return render(request, 'checkout/checkout.html', context)


@login_required
def payment_success(request, payment_intent_id):
    """Handles successful payment and displays the confirmation page."""
    order = get_object_or_404(Order,
                              stripe_payment_intent_id=payment_intent_id)

    # ✅ Mark order as Paid
    order.paid = True
    order.save()

    template = 'checkout/success.html'
    context = {
        'order': order,  # The order instance to display
    }

    return render(request, template, context)
