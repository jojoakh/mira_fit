from django.contrib import admin
from .models import NewsletterSubscriber, ClientReview


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


class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'comment')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(ClientReview, ClientReviewAdmin)
