from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .set_default import vehicle_default,acquisition_defaule
def default_set(requests):
    retu=vehicle_default()
    retu=acquisition_defaule()
    return HttpResponse(retu)
