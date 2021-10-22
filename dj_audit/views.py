from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count, Q

from dj_audit.models import AuditLog
from dj_audit.settings import AUDIT_LOG_TEMPLATE, REQUEST_STATUS_TEMPLATE, API_BASE_URL


@staff_member_required
def index_page(request):
    return HttpResponseRedirect(reverse('dj_audit_audit_log_page'))


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

    audit_log = AuditLog.objects.filter(path_info__startswith=API_BASE_URL)
    total_success = audit_log.filter(response_status_code=200).count()
    total_not_found = audit_log.filter(response_status_code=404).count()
    total_failed =  audit_log.exclude(response_status_code=200).exclude(response_status_code=404).count()

    no_success = Count('id', filter=Q(response_status_code=200))
    no_failed = Count('id', exclude=(Q(response_status_code=200) | Q(response_status_code=404)))
    no_not_found = Count('id', filter=Q(response_status_code=404))

    api_break_down = audit_log.values('path_info').\
        annotate(no_success=no_success).annotate(no_failed=no_failed).annotate(no_not_found=no_not_found)

    context = {
        'total_success': total_success,
        'total_not_found': total_not_found,
        'total_failed': total_failed,
        'api_break_down': api_break_down
    }
    return render(request, REQUEST_STATUS_TEMPLATE, context)
