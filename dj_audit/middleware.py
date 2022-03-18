from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone

from dj_audit import settings
from dj_audit.models import AuditLog

successful_status = [200, 201, 302, 301]


class AuditMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.request_time = timezone.now()
        self.__conf__()

    def __conf__(self):
        extra = getattr(
            settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200', False)
        extras_conditions = settings.AUDIT_LOG_DJ_EXTRA_CONDITIONS
        if extra:
            if not extras_conditions or len(extras_conditions) == 0:
                raise ImproperlyConfigured(
                    "The AUDIT_LOG_DJ_EXTRA_CONDITIONS setting is required. initialize with list of dicts of conditions")
            self.__validate_extra_conditions__(extras_conditions)

    def __validate_extra_conditions__(self, conds):
        if not isinstance(conds, list):
            raise ImproperlyConfigured(
                "Improper configure of AUDIT_LOG_DJ_EXTRA_CONDITIONS setting. Pls refer to the documentation on how to set the variable")
        for condition in conds:
            if not isinstance(condition, dict):
                raise ImproperlyConfigured(
                    "Improper configure of AUDIT_LOG_DJ_EXTRA_CONDITIONS setting. Pls refer to the documentation on how to set the variable")
            if not 'key' in condition or not 'values' in condition or not 'flag' in condition:
                raise ImproperlyConfigured(
                    "Improper configure of AUDIT_LOG_DJ_EXTRA_CONDITIONS setting. key, values and flag is required. Pls refer to the documentation on how to set the variable")
            if not isinstance(condition['values'], list):
                raise ImproperlyConfigured(
                    "Improper configure of AUDIT_LOG_DJ_EXTRA_CONDITIONS setting. The 'values' key must be a list of keys to map ")
            if not condition['flag'] in ['success', 'failed', 'warning']:
                raise ImproperlyConfigured(
                    "Improper configure of AUDIT_LOG_DJ_EXTRA_CONDITIONS setting. The 'flag' key must be set correctly ")

    def __call__(self, request, *args, **kwargs):
        self.process_request(request)
        response = self.process_response(request)
        return response

    def process_request(self, request):
        return None

    def process_response(self, request, response=None):
        response_time = timezone.now()
        response = self.get_response(request)
        static_url = getattr(settings, 'STATIC_URL', None)
        if static_url and static_url in request.path_info:
            return response

        media_url = getattr(settings, 'MEDIA_URL', None)
        if media_url and media_url in request.path_info:
            return response

        for ext in settings.IGNORE_FILE_EXTENSIONS:
            if ext in request.path_info:
                return response

        if not request.method in ('HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
            else:
                user = None
            rest_content_types = getattr(
                settings, 'AUDIT_LOG_DJ_REST_CONTENT_TYPES', [])
            req_content_type = request.META.get('CONTENT_TYPE', '')
            response_type = 'http'
            if req_content_type in rest_content_types:
                response_type = 'rest'
            log_type = 'failed'
            if response.status_code in successful_status:
                log_type = 'success'
            if response.status_code in successful_status and response_type == 'rest' and getattr(settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200', False):
                extras_conditions = settings.AUDIT_LOG_DJ_EXTRA_CONDITIONS
                log_type = None
                is_success, is_failed, is_warning = False, False, False
                for condition in extras_conditions:
                    if 'flag' in condition:
                        if condition['flag'] == 'success':
                            is_success = True
                            key = condition['key']
                            values = condition['values']
                            if key in response and response[key] in values:
                                log_type = 'success'
                        elif condition['flag'] == 'failed':
                            is_failed = True
                            key = condition['key']
                            values = condition['values']
                            if key in response and response[key] in values:
                                log_type = 'failed'
                        elif condition['flag'] == 'warning':
                            is_warning = True
                            key = condition['key']
                            values = condition['values']
                            if key in response and response[key] in values:
                                log_type = 'warning'
                if log_type is None:
                    if is_success and is_failed:
                        log_type = 'failed'
                    elif is_success:
                        log_type = 'success'
                    elif is_failed:
                        log_type = 'failed'
                    elif is_warning:
                        log_type = 'warning'
                    else:
                        log_type = 'failed'
            if response_type == 'http':
                response_body = ''
            else:
                if response.streaming:
                    response_body = "Streamed Content"
                else:
                    response_body = response.content.decode('utf-8')

            exception = getattr(self, 'exception', None)

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
                'response_type': response_type,
                'log_status': log_type,
                'response_reason_phrase': response.reason_phrase,
                'response_body': response_body if exception is None else exception,
                'attempt_time': self.request_time,
                'response_time': response_time
            }

            AuditLog.objects.create(**log_data)

        return response

    def process_exception(self, request, exception):
        self.exception = str(exception)
