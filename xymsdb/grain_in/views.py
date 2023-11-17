from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .set_default import vehicle_default
def default_set(requests):
    retu=vehicle_default()
    return HttpResponse(retu)
