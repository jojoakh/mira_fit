from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ContactMessage model.
    """
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email')


admin.site.register(ContactMessage, ContactMessageAdmin)
