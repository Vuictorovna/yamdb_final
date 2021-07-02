from django.urls import path

from .views import AuthTokenView, EmailView

urlpatterns = [
    path(
        "v1/auth/token/",
        AuthTokenView.as_view(),
        name="auth_token",
    ),
    path(
        "v1/auth/email/",
        EmailView.as_view(),
        name="auth_email",
    ),
]
