from django.urls import path
from . import views


app_name = "product"

urlpatterns = [
    path("home/", views.home_view, name="list"),
    path("about/", views.about_view, name="create"),
]