from django.conf import settings
from django.db import models

import uuid


def _generate_link_public_id():
    public_id = str(uuid.uuid4()).replace("-", "")[: settings.S_LINK_PUBLIC_ID_LENGTH]
    while Link.objects.filter(public_id=public_id).exists():
        public_id = str(uuid.uuid4()).replace("-", "")[
            : settings.S_LINK_PUBLIC_ID_LENGTH
        ]
    return public_id


class Link(models.Model):
    public_id = models.CharField(
        verbose_name="Public ID",
        unique=True,
        max_length=255,
        default=_generate_link_public_id,
    )
    url = models.URLField(verbose_name="URL")
    description = models.TextField(verbose_name="Description", blank=True)
    created_at = models.DateTimeField(verbose_name="Created At", auto_now_add=True)

    def __str__(self):
        return self.url


class LinkClick(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="clicks")
    clicked_at = models.DateTimeField(verbose_name="Clicked At", auto_now_add=True)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address", null=True, blank=True
    )
    user_agent = models.TextField(verbose_name="User Agent", blank=True)

    def __str__(self):
        return f"Click on {self.link.url} at {self.clicked_at}"
