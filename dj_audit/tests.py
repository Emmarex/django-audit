from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from dj_audit.middleware import AuditMiddleware
from dj_audit.models import AuditLog


def get_response_empty(request):
    return HttpResponse()


class TestAuditMiddleware(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='jacob', email='jacob@…', password='top_secret')

    def test_request_processing(self):
        request = self.factory.get('/')

        response = AuditMiddleware(
            get_response_empty).process_response(request)

        self.assertIsNotNone(response)

        audit_logs_count = AuditLog.objects.all().count()
        self.assertEqual(audit_logs_count, 1)

        request.user = self.user
        response = AuditMiddleware(
            get_response_empty).process_response(request)

        self.assertIsNotNone(response)

        audit_logs_count = AuditLog.objects.all().count()
        self.assertEqual(audit_logs_count, 2)
