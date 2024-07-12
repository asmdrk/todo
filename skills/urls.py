from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = "index"),
    path("app/", views.appView.as_view(), name = "app"),
]