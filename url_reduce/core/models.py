import uuid
from django.db import models


class UrlRedirect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "URL Redirect"
        verbose_name_plural = "URL's Redirect"
        ordering = ["-created_at"]

    def __str__(self):
        return f"UrlRedirect para {self.destination}"


class UrlLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    origin = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(
        UrlRedirect, models.DO_NOTHING, related_name="logs"
    )

    class Meta:
        verbose_name = "URL Log"
        verbose_name_plural = "URL's Log"

    def __str__(self):
        return f"UrlLog para {self.origin}"
