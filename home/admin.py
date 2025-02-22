from django.contrib import admin
from .models import NewsletterSubscriber


class NewsletterSubscriberAdmin(admin.ModelAdmin):
    # Display the fields in the list view of the admin panel
    list_display = ('email', 'subscribed_at')

    # Filter by the 'subscribed_at' field
    list_filter = ('subscribed_at',)

    # Add search functionality based on email
    search_fields = ('email',)

    # Allow sorting by the 'subscribed_at' field
    ordering = ('-subscribed_at',)


# Register the model with the customized admin
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
