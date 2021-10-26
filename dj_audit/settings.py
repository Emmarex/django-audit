from django.conf import settings as global_settings

DISABLE_AUDIT_LOG = getattr(global_settings, 'DISABLE_AUDIT_LOG', False)

AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200 = getattr(global_settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200', False)
AUDIT_LOG_DJ_EXTRA_CONDITIONS = getattr(global_settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS', [])

AUDIT_LOG_DJ_REST_CONTENT_TYPES = getattr(
    global_settings, 'AUDIT_LOG_DJ_REST_CONTENT_TYPES', ['application/json','application/xml'])

REQUEST_STATUS_TEMPLATE = getattr(
    global_settings, 'REQUEST_STATUS_TEMPLATE', 'dj_audit/request_status_page.html')
