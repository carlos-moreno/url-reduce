from django.shortcuts import redirect

from url_reduce.core.models import UrlRedirect


def redirecionar(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destination)
