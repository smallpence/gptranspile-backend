"views for the api"
import secrets
from dataclasses import dataclass
from datetime import timedelta

from django.utils import timezone
from dotenv import dotenv_values
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
import requests

from gptranspile_auth.models import UserSession

config = dotenv_values(".env")



# Create your views here.

@dataclass
class OAuthResponse:
    "class for holding the returned response by oauth"
    access_token: str
    token_type: str
    scope: str


def auth(request):
    "authenticate and create a session"

    client_id = "1c3ec89d317df07022fe"
    client_secret = config["GITHUB_CLIENT_SECRET"]
    code = request.GET.get('code')

    oauth_response = requests.post(
        headers={'Accept': "application/json"},
        url=f"https://github.com/login/oauth/access_token"
            f"?client_id={client_id}"
            f"&client_secret={client_secret}"
            f"&code={code}"
    ).json()

    oauth_response = OAuthResponse(**oauth_response)

    user_response = requests.get(
        "https://api.github.com/user",
        headers={'Authorization': f"token {oauth_response.access_token}"}).json()

    session = secrets.token_hex(16)

    user_session = UserSession(session_token=session,
                               access_token=oauth_response.access_token,
                               expiry=timezone.now() + timedelta(days=1),
                               userid=user_response["id"]
                               )
    user_session.save()

    oauth_response = HttpResponseRedirect(f"{config['URL']}")
    oauth_response.set_cookie("gptranspile_session", session, httponly=False, samesite="strict")

    return oauth_response

def secure_request(request):
    "a secured request to the database"
    session = request.COOKIES.get("gptranspile_session")

    if not session:
        return HttpResponseForbidden()

    try:
        found: UserSession = UserSession.objects.get(session_token=session)
    except UserSession.DoesNotExist:
        return HttpResponseForbidden("invalid session")

    if not found.is_fresh():
        return HttpResponseForbidden("session expired")

    return HttpResponse("hello world")
