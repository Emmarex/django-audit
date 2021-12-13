from django.urls import path

from .views import audit_log_page, index_page, request_status_page

urlpatterns = [
    path("", index_page, name="dj_audit_index_page"),
    path("audit-logs/", audit_log_page, name="dj_audit_audit_log_page"),
    path("request-status/", request_status_page,
         name="dj_audit_request_status_page"),
]
