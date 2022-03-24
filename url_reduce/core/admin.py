from django.contrib import admin

# Register your models here.
from url_reduce.core.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ("id", "destination", "slug", "created_at", "update_at")
