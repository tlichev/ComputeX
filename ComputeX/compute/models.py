from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from ComputeX.accounts.models import Request


class Result(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name="results")
    result = models.FloatField()

