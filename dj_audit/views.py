from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse


@staff_member_required
def audit_log_page(request):
    """ List audit logs """

    context = {
    }
    return render(request, "dj_audit/audit_list_page.html", context)
