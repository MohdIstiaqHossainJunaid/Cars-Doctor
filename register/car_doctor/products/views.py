from django.shortcuts import render
from . models import productlist


# Create your views here.


def productlist(request):
    pl = productlist.objects.all()
    return render(request, 'product.html', {'pl': pl})
