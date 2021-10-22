from django.urls import path
from .views import audit_log_page

urlpatterns = [
    path("audit-logs/", audit_log_page, name="dj_audit_audit_log_page"),
]
