from django.urls import path

from links import views

urlpatterns = [
    path("<str:link_id>/", views.link_detail, name="link_detail"),
]


app_name = "links"
