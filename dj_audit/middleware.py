from dj_audit import settings
from dj_audit.models import AuditLog

file_extensions = ['.svg', '.js', '.css', '.png', '.jpg', '.ico', ]


class AuditMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.process_response(request)
        return response

    def process_response(self, request, response=None):
        response = self.get_response(request)
        static_url = getattr(settings, 'STATIC_URL', None)
        if static_url and static_url in request.path_info:
            return response

        media_url = getattr(settings, 'MEDIA_URL', None)
        if media_url and media_url in request.path_info:
            return response

        for ext in file_extensions:
            if ext in request.path_info:
                return response

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
                'host_name': request.META.get('REMOTE_HOST', ''),
                'user': user,
                'content_type': request.META.get('CONTENT_TYPE', ''),
                'query_string': request.META.get('QUERY_STRING', ''),
                'http_method': request.method,
                'http_referer': request.META.get('HTTP_REFERER', ''),
                'path_info': request.path_info,
                'post_data': request.POST.dict(),
                'response_status_code': response.status_code,
                'response_reason_phrase': response.reason_phrase,
                'response_body': response.content.decode('utf-8'),
            }

            AuditLog.objects.create(**log_data)

        return response
