from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal, ROUND_HALF_UP


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="userprofile"
    )
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=40, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2,
                                         blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2,
                                 blank=True, null=True)
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2,
                                      blank=True, null=True)


class WeightLog(models.Model):
    """
    Model to log the user's weight entries over time.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - {self.weight} kg on "
            f"{self.entry_date.strftime('%Y-%m-%d')}"
        )

    def save(self, *args, **kwargs):
        self.weight = Decimal(self.weight).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
        super().save(*args, **kwargs)
