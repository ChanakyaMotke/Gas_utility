from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type')
