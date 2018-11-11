from django.contrib import admin
from logs.models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'date_at')

admin.site.register(Log, LogAdmin)
