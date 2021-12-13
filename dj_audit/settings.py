from django.conf import settings as global_settings

AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200 = getattr(
    global_settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS_FOR_200', False)

AUDIT_LOG_DJ_EXTRA_CONDITIONS = getattr(
    global_settings, 'AUDIT_LOG_DJ_EXTRA_CONDITIONS', [])

AUDIT_LOG_DJ_REST_CONTENT_TYPES = getattr(
    global_settings, 'AUDIT_LOG_DJ_REST_CONTENT_TYPES', ['application/json', 'application/xml'])

AUDIT_LOG_TEMPLATE = getattr(
    global_settings, 'AUDIT_LOG_TEMPLATE', 'dj_audit/audit_list_page.html')

REQUEST_STATUS_TEMPLATE = getattr(
    global_settings, 'REQUEST_STATUS_TEMPLATE', 'dj_audit/request_status_page.html')

IGNORE_FILE_EXTENSIONS = getattr(
    global_settings, 'IGNORE_FILE_EXTENSIONS', ['.svg', '.js', '.css', '.png', '.jpg', '.ico'])
