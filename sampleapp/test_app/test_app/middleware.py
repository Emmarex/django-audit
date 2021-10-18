# from audit import settings


class AuditMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        print(dir(response))

        print(response)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(self, request, *args, **kwargs):
        print('====> request')
        print(request)

        if not request.method in ('HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user
            else:
                user = None

            session = request.session.session_key
            print(session)

        return None

    def process_response(self, request, *args, **kwargs):
        print('====> response')
        print(request)
        return None

    def process_exception(self, request, exception):
        pass
        return None
