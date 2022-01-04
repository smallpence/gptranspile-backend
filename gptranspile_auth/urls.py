"url map for the api"
from django.urls import path

from .views import auth, secure_request

app_name = "gptranspile_auth"
urlpatterns = [
    path("", auth, name="root"),
    path("foo", secure_request, name="root")
]
