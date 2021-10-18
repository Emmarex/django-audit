from audit import settings


class AuditMiddleware():

    def process_request(self, request):
        if settings.DISABLE_AUDIT_LOG:
            return

        if not request.method in ('HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
            else:
                user = None

            session = request.session.session_key
            print(session)

    def process_response(self, request):
        if settings.DISABLE_AUDIT_LOG:
            return

    def process_exception(self, request):
        if settings.DISABLE_AUDIT_LOG:
            return None
