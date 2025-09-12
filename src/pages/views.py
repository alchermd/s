from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def error_400(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "pages/400.html", status=400)


def error_403(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "pages/403.html", status=403)


def error_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "pages/404.html", status=404)


def error_500(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/500.html", status=500)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/index.html")
