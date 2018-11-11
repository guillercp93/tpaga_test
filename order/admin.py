from django.contrib import admin
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    fields = ['status']
    list_display = ('id', 'details', 'client', 'status', 'total', 'token')

admin.site.register(Order, OrderAdmin)
