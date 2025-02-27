from django.contrib import admin
from .models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    list_editable = ('duration', 'price')
    search_fields = ('name',)
    list_filter = ('duration',)
    fields = ('name', 'description', 'duration', 'price')
    readonly_fields = ()


admin.site.register(Plan, PlanAdmin)
