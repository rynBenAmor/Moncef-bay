from django.shortcuts import render
#from django.http import HttpResponse
from .models import Product
from .models import Offer


def index(request):
    products= Product.objects.all()
    return render(request,"index.html",
                  {"products":products})

def new(request):
    offers = Offer.objects.all()
    return render(request, "offerIndex.html", {"offers": offers})