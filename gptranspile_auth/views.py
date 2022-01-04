"views for the api"
from dataclasses import dataclass
from dotenv import dotenv_values
from django.http import HttpResponseRedirect
import requests

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

    response = requests.get(
        "https://api.github.com/user",
        headers={'Authorization': f"token {response.access_token}"})

    print(response.text)

    return HttpResponseRedirect("http://localhost:3000")
