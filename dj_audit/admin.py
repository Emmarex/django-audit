from django.contrib.admin import DateFieldListFilter, ModelAdmin, register

from dj_audit.models import AuditLog


@register(AuditLog)
class AuditLogAdmin(ModelAdmin):
    list_display = (
        'user_agent', 'ip_address', 'user', 'content_type', 'query_string',
        'http_method', 'http_referer', 'path_info', 'request_data',
        'response_status_code', 'response_reason_phrase', 'attempt_time'
    )
    list_filter = (
        'user', 'http_method', 'response_status_code',
        ('attempt_time', DateFieldListFilter)
    )
    search_fields = ('user__username', 'ip_address')
