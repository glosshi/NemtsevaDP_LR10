from django.contrib import admin
from .models import SuspiciousIP, TrafficLog, SecurityIncident

@admin.register(SuspiciousIP)
class SuspiciousIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'threat_level', 'first_detected', 'last_seen')
    list_filter = ('threat_level',)
    search_fields = ('ip_address',)

@admin.register(TrafficLog)
class TrafficLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'source_ip', 'destination_ip', 'protocol', 'entropy', 'suspicious')
    list_filter = ('protocol', 'suspicious', 'encrypted')
    search_fields = ('source_ip', 'destination_ip')

@admin.register(SecurityIncident)
class SecurityIncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'detected_at', 'resolved')
    list_filter = ('severity', 'resolved')
    search_fields = ('title', 'description')
