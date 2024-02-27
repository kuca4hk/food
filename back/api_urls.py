from django.urls import path, include, re_path

urlpatterns = [
    path("user/", include("back.apps.user.urls")),
]