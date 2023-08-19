from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def ciudades(request):

    context={

    }
    return render(request,'ciudades/ciudades.html',context)