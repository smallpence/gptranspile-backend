"url map for the api"
from django.urls import path

from .views import auth, query_gpt

app_name = "gptranspile"
urlpatterns = [
    path("auth", auth, name="authenticate"),
    path("gpt3", query_gpt, name="query gpt")
]
