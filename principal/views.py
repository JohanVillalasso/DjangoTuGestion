from django.shortcuts import render


def inicio_sesion(request):
    titulo = "Inicio sesión"
    context={
      "titulo": titulo    
    }
    return render (request, 'index.html', context)
  
def menu_ppal(request):
    titulo = "Menú"
    context={
      "titulo": titulo
    }
    return render (request, 'main.html', context)
  
def rutero(request):
    titulo = "Rutero"
    context={
      "titulo": titulo
    }
    return render (request, 'rutero.html', context)

def cap_guia(request):
    titulo = "Captura Guía"
    context={
      "titulo": titulo
    }
    return render (request, 'cap-guia.html', context)

def seg_cliente(request):
    titulo = "Seguimiento Cliente"
    context={
      "titulo": titulo
    }
    return render (request, 'seg-cliente.html', context)

def proy_cumpl(request):
    titulo = "Proyección Cumplimiento"
    context={
      "titulo": titulo
    }
    return render (request, 'proy-cumpl.html', context)

def eje_acu(request):
    titulo = "Ejecución Acumulada"
    context={
      "titulo": titulo
    }
    return render (request, 'eje-acu.html', context)

def form_gcom(request):
    titulo = "Formatos Gestión"
    context={
      "titulo": titulo
    }
    return render (request, 'form-gcom.html', context)

def e404(request):
    titulo = "Error 404"
    context={
      "titulo": titulo
    }
    return render (request, 'e404.html', context)    
