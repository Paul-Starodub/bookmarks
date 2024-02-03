from django.urls import path, reverse_lazy
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
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy("account:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("", views.dashboard, name="dashboard"),
]

app_name = "account"
