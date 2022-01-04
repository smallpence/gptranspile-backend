"url map for the api"
from django.urls import path

from .views import auth

app_name = "gptranspile_auth"
urlpatterns = [
    path("", auth, name="root")
]
