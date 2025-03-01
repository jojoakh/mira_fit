from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'get_plans', 'created_at')
    readonly_fields = ('order_number', 'full_name', 'get_plans', 'created_at')

    def get_plans(self, obj):
        return ", ".join([plan.name for plan in obj.plans.all()])
    get_plans.short_description = 'Plan Name'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
