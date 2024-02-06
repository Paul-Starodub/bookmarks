from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.image_create, name="create"),
    path("detail/<int:id>/<slug:slug>/", views.image_detail, name="detail"),
    path("like/", views.image_like, name="like"),
]

app_name = "images"
