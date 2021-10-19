from dj_audit import settings
from dj_audit.models import AuditLog


class AuditMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.process_response(request)
        return response

    def process_response(self, request, response=None):
        response = self.get_response(request)

        if settings.DISABLE_AUDIT_LOG:
            return response

        if not request.method in ('HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
            else:
                user = None

            log_data = {
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'ip_address': request.META.get('REMOTE_ADDR', ''),
                'user': user,
                'content_type': request.META.get('CONTENT_TYPE', ''),
                'query_string': request.META.get('QUERY_STRING', ''),
                'http_method': request.method,
                'http_referer': request.META.get('HTTP_REFERER', ''),
                'path_info': request.path_info,
                'request_data': request.body.decode('utf-8'),
                'response_status_code': response.status_code,
                'response_reason_phrase': response.reason_phrase
            }

            AuditLog.objects.create(**log_data)

        return response
