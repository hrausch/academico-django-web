from django.urls import path, include
from rest_framework.authtoken import views

from usuario.views import (
    UserRegistrationAPIView,
    MyProfileView,
    ChangeMyPasswordUpdateView,
)


app_name = "usuario"

# router = routers.DefaultRouter()
# router.register("me", UserProfileViewSet, basename="Alunos")

urlpatterns = [
    path("login/", views.obtain_auth_token, name="auth"),
    path("user/me/", MyProfileView.as_view(), name="me"),

    path("user/", UserRegistrationAPIView.as_view(), name="registration"),
    path(
        "user/me/password/",
        ChangeMyPasswordUpdateView.as_view(),
        name="change_password",
    ),


]