"url map for the api"
from django.urls import path

from .views import auth, query_gpt, check_session, get_user_details

app_name = "gptranspile"
urlpatterns = [
    path("auth", auth, name="authenticate"),
    path("gpt3", query_gpt, name="query gpt"),
    path("checksession", check_session, name="check session"),
    path("getuserdetails", get_user_details, name="get user details from github")
]
