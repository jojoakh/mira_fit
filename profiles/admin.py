from django.contrib import admin
from .models import UserProfile, WeightLog


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'gender', 'date_of_birth')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('gender',)


class WeightLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'entry_date')
    search_fields = ('user__username',)
    list_filter = ('entry_date',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(WeightLog, WeightLogAdmin)
