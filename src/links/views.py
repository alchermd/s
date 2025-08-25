from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from links.models import Link


def link_detail(request: HttpRequest, link_id: int):
    link = get_object_or_404(Link, public_id=link_id)
    link.clicks.create(
        ip_address=request.META.get("REMOTE_ADDR"),
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
    )
    return redirect(link.url)
