from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .set_default import vehicle_default, acquisition_defaule, GBforCorn, vehicletypedefault, packagindefault
from .models import CarDriverAndVehicleInformations, GrainSellerInformations


def default_set(requests):
    # retu = vehicle_default()
    # vehicletypedefault()
    # retu = packagindefault()
    # retu = acquisition_defaule()
    # retu = GBforCorn()
    return HttpResponse('ok')
