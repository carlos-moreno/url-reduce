from django.contrib import admin

# Register your models here.
from url_reduce.core.models import UrlRedirect, UrlLog


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ("id", "destination", "slug", "created_at", "update_at")


@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "origin", "user_agent", "host", "ip", "url_redirect")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
