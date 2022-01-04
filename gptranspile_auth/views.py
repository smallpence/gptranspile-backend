"views for the api"
from django.http import JsonResponse

# Create your views here.

def root(_):
    "test endpoint"
    return JsonResponse({'a': 5})
