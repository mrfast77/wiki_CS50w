from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("search/", views.search_view, name="search"),
    path("<str:entry>/", views.title, name="title")
]
