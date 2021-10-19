from django.contrib import admin
from dj_audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'user_agent', 'ip_address', 'user', 'content_type', 'query_string',
        'http_method', 'http_referer', 'path_info', 'request_data',
        'response_status_code', 'response_reason_phrase', 'attempt_time'
    )
    list_filter = ('user', 'http_method')
    search_fields = ('user__username', 'ip_address')
