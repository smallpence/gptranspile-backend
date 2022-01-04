"views for the api"
import secrets
from dataclasses import dataclass

from django.utils import timezone
from dotenv import dotenv_values
from django.http import HttpResponseRedirect
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
    "test endpoint"

    client_id = "1c3ec89d317df07022fe"
    client_secret = config["GITHUB_CLIENT_SECRET"]
    code = request.GET.get('code')

    response = requests.post(
        headers={'Accept': "application/json"},
        url=f"https://github.com/login/oauth/access_token"
            f"?client_id={client_id}"
            f"&client_secret={client_secret}"
            f"&code={code}"
    ).json()

    response = OAuthResponse(**response)

    # response = requests.get(
    #     "https://api.github.com/user",
    #     headers={'Authorization': f"token {response.access_token}"})

    session = secrets.token_hex(16)

    user_session = UserSession(session_token=session,
                               access_token=response.access_token,
                               expiry=timezone.now()
                               )
    user_session.save()

    response = HttpResponseRedirect(f"http://localhost:3000/session?session={session}")

    return response
