
# Register your models here.
from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['request_type', 'status', 'created_at']
    list_filter = ['status']