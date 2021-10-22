from django.views.generic import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class TestView(View):
    def get(self, request, *args, **kwargs):
        response = f"{request.GET.dict()}"
        return HttpResponse(response)

    def post(self, request, *args, **kwargs):
        response = f"{request.POST.dict()}"
        return HttpResponse(response)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)