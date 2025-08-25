from django.contrib import admin

from links.models import Link, LinkClick


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "url",
        "created_at",
        "clicks",
    )
    search_fields = ("url",)
    list_filter = ("created_at",)
    readonly_fields = ("public_id",)

    def clicks(self, obj):
        return obj.clicks.count()


@admin.register(LinkClick)
class LinkClickAdmin(admin.ModelAdmin):
    pass
