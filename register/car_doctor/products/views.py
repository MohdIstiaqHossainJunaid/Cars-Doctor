from django.shortcuts import render


# Create your views here.


def productlist(request):
    return render(request, 'product.html')