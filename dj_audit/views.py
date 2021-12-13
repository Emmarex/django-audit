from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

    # paginate audit logs begins here
    page = request.GET.get('page', 1)
    paginator = Paginator(audit_logs, 100) #100 items per page
    try:
        audit_logs = paginator.page(page)
    except PageNotAnInteger:
        audit_logs = paginator.page(1)
    except EmptyPage:
        audit_logs = paginator.page(paginator.num_pages)
    # end of pagination

    context = {
        'users': get_user_model().objects.all(),
        'audit_logs': audit_logs
    }
    return render(request, AUDIT_LOG_TEMPLATE, context)


@staff_member_required
def request_status_page(request):
    """ Request Status page """

    audit_log = AuditLog.objects.filter(response_type="rest")
    total_success = audit_log.filter(log_status='success').count()
    total_failed = audit_log.filter(log_status='failed').count()
    total_warning = audit_log.exclude(log_status='warning').count()

    no_success = Count('id', filter=Q(log_status='success'))
    no_failed = Count('id', filter=Q(log_status='failed'))
    no_warning = Count('id', filter=Q(log_status='warning'))

    api_break_down = audit_log.values('path_info').\
        annotate(no_success=no_success).annotate(
            no_failed=no_failed).annotate(no_not_found=no_warning).order_by('path_info')

    # paginate request_status begins here
    page = request.GET.get('page', 1)
    paginator = Paginator(api_break_down, 100) #100 items per page
    try:
        api_break_down = paginator.page(page)
    except PageNotAnInteger:
        api_break_down = paginator.page(1)
    except EmptyPage:
        api_break_down = paginator.page(paginator.num_pages)
    # end of pagination
    
    context = {
        'total_success': total_success,
        'total_warning': total_warning,
        'total_failed': total_failed,
        'api_break_down': api_break_down
    }
    return render(request, REQUEST_STATUS_TEMPLATE, context)
