from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from dj_audit.models import AuditLog
from dj_audit.settings import AUDIT_LOG_TEMPLATE, REQUEST_STATUS_TEMPLATE


@staff_member_required
def index_page(request):
    return HttpResponseRedirect(reverse('dj_audit_audit_log_page'))


@staff_member_required
def audit_log_page(request):
    """ List audit logs """
    query_filter = {}
    user_name = request.GET.get('user_name', None)
    if user_name:
        query_filter['user__username'] = user_name
    #
    audit_logs = AuditLog.objects.filter(**query_filter)
    context = {
        'users': get_user_model().objects.all(),
        'audit_logs': audit_logs
    }
    return render(request, AUDIT_LOG_TEMPLATE, context)


@staff_member_required
def request_status_page(request):
    """ Request Status page """

    context = {
    }
    return render(request, REQUEST_STATUS_TEMPLATE, context)
