import functools
from django.shortcuts import HttpResponseRedirect


def ssl_redirect(view):
    """
    редирект сам на себя не отрабатывается properly
    мб сделать две редиректные странички на одну будет уходит защищенный
    и перенаправляться на https часть сайта
    на трафик будет ходить обратно с https на http
    """
    @functools.wraps(view)
    def wrapper(request, *args, **kwargs):
        print(request.scheme)
        if not request.is_secure():
            site_url = request.META['HTTP_HOST']
            path = request.path_info
            redirect_url = "https://{}{}".format(site_url, path)
            catalog = 'https://mysite.com/accounts/profile'
            return HttpResponseRedirect(redirect_url)
        return view(request, *args, **kwargs)
    return wrapper