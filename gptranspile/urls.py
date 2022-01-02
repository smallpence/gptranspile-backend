"url map for the api"
from django.urls import path

from .views import root

app_name = "gptranspile"
urlpatterns = [
    path("", root, name="root")
]
