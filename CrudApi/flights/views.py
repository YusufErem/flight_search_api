from django.http import JsonResponse
from django.shortcuts import render
from flights.models import Havaalanlari, Ucuslar
# Create your views here.
def create(req):
    pass

def search(req):
    ucuslar = Ucuslar.objects.all()
    ucuslar_list = list(ucuslar.values())
    return JsonResponse({
        "ucuslar":ucuslar_list
    })


def update(req):
    pass

def delete(req):
    pass