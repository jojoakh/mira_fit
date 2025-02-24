import uuid
from django.db import models
from django.contrib.auth.models import User
from plan.models import Plan
from decimal import Decimal, ROUND_HALF_UP


class Order(models.Model):
    # Unique order number
    order_number = models.CharField(max_length=32, unique=True, editable=False,
                                    default=uuid.uuid4().hex.upper())

    # User who placed the order
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Plans in the order (Supports multiple plans if needed)
    plans = models.ManyToManyField(Plan, related_name='orders')

    # Customer details
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True)

    # Order amount (automatically calculated)
    amount = models.DecimalField(max_digits=7, decimal_places=2,
                                 blank=True, default=0)

    # Order status
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=10,
                              choices=ORDER_STATUS, default='Pending')

    # Stripe Payment Intent ID (Used for tracking payments)
    stripe_payment_intent_id = models.CharField(max_length=254,
                                                null=False, blank=False,
                                                default='')

    # Timestamp for order creation
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        """Calculate the total amount for the order."""
        total = sum(plan.price for plan in self.plans.all())
        return round(total, 2)

    def save(self, *args, **kwargs):
        """Ensure the amount is calculated properly before saving."""
        if not self.amount:
            self.amount = self.calculate_total()
        self.amount = Decimal(self.amount).quantize(Decimal('0.01'),
                                                    rounding=ROUND_HALF_UP)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"
