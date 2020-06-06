from django.urls import path
from authentication.views import Login_View

from . import views

urlpatterns = [
    path("login/", Login_View.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout")
]
