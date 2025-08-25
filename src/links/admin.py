from django.contrib import admin
from django.http import HttpRequest
from django.utils.html import format_html

from links.models import Link, LinkClick


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "url",
        "public_link",
        "created_at",
        "clicks",
    )
    search_fields = ("url",)
    list_filter = ("created_at",)
    readonly_fields = ("public_id",)
    request: HttpRequest

    def get_queryset(self, request):
        """
        Very hacky way of getting the request object into the admin class.
        """
        self.request = request
        return super().get_queryset(request)

    def clicks(self, obj):
        return obj.clicks.count()

    def public_link(self, obj):
        return format_html(
            f"<a href='{self.request.scheme}://{self.request.get_host()}/{obj.public_id}/' target='_blank'>{obj.public_id}</a>"
        )


@admin.register(LinkClick)
class LinkClickAdmin(admin.ModelAdmin):
    list_display = (
        "link",
        "clicked_at",
        "ip_address",
        "user_agent",
    )
    search_fields = (
        "ip_address",
        "user_agent",
    )
    list_filter = ("clicked_at",)
