from django.shortcuts import redirect as r, render

from url_reduce.core.models import UrlRedirect


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    shortened_url = request.build_absolute_uri(f"/{slug}")
    context = {
        "reduce": url_redirect,
        "shortened_url": shortened_url
    }
    return render(request, "core/reports.html", context)


def redirect(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return r(url_redirect.destination)
