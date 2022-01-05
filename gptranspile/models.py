"models to be used by the backend, just the user session"

from django.db import models

# Create your models here.
from django.utils import timezone


class UserSession(models.Model):
    "combining an access token & a session to allow remaining signed in"
    session_token = models.CharField(primary_key=True, max_length=32)
    access_token = models.CharField(max_length=32)
    expiry = models.DateTimeField('expiry date')
    userid = models.CharField(max_length=16)


    def __str__(self):
        return f"s: {self.session_token} a: {self.access_token} u: {self.userid}"


    def is_fresh(self):
        "checks whether this session remains valid"
        return timezone.now() < self.expiry
