from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # path("login/", views.user_login, name="login"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            http_method_names=["post", "get", "options"]
        ),
        name="logout",
    ),
    path("", views.dashboard, name="dashboard"),
]

app_name = "account"
