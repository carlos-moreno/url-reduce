from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import redirect as r, render

from url_reduce.core.models import UrlRedirect, UrlLog
from url_reduce.core.slug_generator import gen_slug


def home(request):
    if "url" in request.POST:
        UrlRedirect.objects.create(
            destination=request.POST.get("url"),
            slug=gen_slug(),
        )
        context = {
            "reduce": request.build_absolute_uri(
                f"/{UrlRedirect.objects.get(destination=request.POST.get('url')).slug}"
            )
        }
        return render(request, "core/reduce.html", context)
    return render(request, "core/home.html")


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    shortened_url = request.build_absolute_uri(f"/{slug}")
    redirects_for_date = list(
        UrlRedirect.objects.filter(slug=slug)
        .annotate(date=TruncDate("logs__created_at"))
        .annotate(clicks=Count("date"))
        .order_by("date")
    )
    context = {
        "reduce": url_redirect,
        "shortened_url": shortened_url,
        "redirects_for_date": redirects_for_date,
        "total_clicks": sum(r.clicks for r in redirects_for_date),
    }
    return render(request, "core/reports.html", context)


def redirect(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origin=request.META.get("HTTP_REFERER"),
        user_agent=request.META.get("HTTP_USER_AGENT"),
        host=request.META.get("HTTP_HOST"),
        ip=request.META.get("REMOTE_ADDRESS"),
        url_redirect=url_redirect,
    )
    return r(url_redirect.destination)
