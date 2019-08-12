from django.contrib import admin

from apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created', 'modified']
