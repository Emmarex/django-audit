from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from dj_audit.models import AuditLog
from dj_audit.settings import AUDIT_LOG_TEMPLATE, REQUEST_STATUS_TEMPLATE


@staff_member_required
def audit_log_page(request):
    """ List audit logs """
    audit_logs = AuditLog.objects.all()
    context = {
        'audit_logs': audit_logs
    }
    return render(request, AUDIT_LOG_TEMPLATE, context)


@staff_member_required
def request_status_page(request):
    """ Request Status page """

    context = {
    }
    return render(request, REQUEST_STATUS_TEMPLATE, context)
