import re
from django.conf import settings
from django.shortcuts import HttpResponseRedirect


class SecureRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        site_url = request.META['HTTP_HOST']
        path = request.path_info
        url = "://{}{}".format(site_url, path)

        if not request.is_secure() and path in settings.SECURE_URLS:
            redirect_url = "https" + url
            return HttpResponseRedirect(redirect_url)
        elif request.is_secure() and path not in settings.SECURE_URLS:
            redirect_url = "http" + url
            return HttpResponseRedirect(redirect_url)
        else:
            pass