import functools
from django.shortcuts import HttpResponseRedirect


def ssl_redirect(view):
    @functools.wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.is_secure():
            site_url = request.META['HTTP_HOST']
            path = request.path_info
            redirect_url = "https://{}{}".format(site_url, path)
            return HttpResponseRedirect(redirect_url)
        return view(request, *args, **kwargs)
    return wrapper