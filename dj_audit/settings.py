from django.conf import settings as global_settings

DISABLE_AUDIT_LOG = getattr(global_settings, 'DISABLE_AUDIT_LOG', False)

AUDIT_LOG_TEMPLATE = getattr(
    global_settings, 'AUDIT_LOG_TEMPLATE', 'dj_audit/audit_list_page.html')

REQUEST_STATUS_TEMPLATE = getattr(
    global_settings, 'REQUEST_STATUS_TEMPLATE', 'dj_audit/request_status_page.html')

API_BASE_URL = getattr(
    global_settings, 'API_BASE_URL', '/admin/')
