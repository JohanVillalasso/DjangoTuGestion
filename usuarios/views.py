from django.shortcuts import render
from usuarios.forms import UsuarioForm
from django.contrib.auth.models import User, Group
from usuarios.models import PuntoVenta, Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def usuarios(request):
    titulo = "Usuarios"
    usuarios = Usuario.objects.all()
    context = {
        'titulo': titulo,
        'usuarios': usuarios
    }
    return render(request, 'usuarios/usuarios.html', context)

def usuarios_crear(request):
    titulo = "Usuarios - Crear"
    mensaje_alerta = ""  # Inicializa la variable

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                # Intenta crear el usuario en la base de datos
                if not User.objects.filter(username=request.POST['cedula']):
                    user = User.objects.create_user('nombre','email@email','pass')
                    user.username= request.POST['cedula']
                    user.first_name= request.POST['nombre']
                    user.last_name= request.POST['apellido']
                    user.email= request.POST['correo']
                    user.password=make_password("@" + request.POST['nombre'][0] + request.POST['apellido'][0] + request.POST['cedula'][-4:])
                    user.save()
                    form = UsuarioForm()
                else:
                    user = User.objects.get(username=request.POST['cedula'])

                # Crear un usuario y guardar campo por campo en la base de datos
                usuario = Usuario.objects.create(
                    codigo_nomina=request.POST['codigo_nomina'],
                    cedula=request.POST['cedula'],
                    nombre=request.POST['nombre'],
                    nombre_dos=request.POST['nombre_dos'],
                    apellido=request.POST['apellido'],
                    apellido_dos=request.POST['apellido_dos'],
                    correo=request.POST['correo'],
                    telefono=request.POST['telefono'],
                    direccion=request.POST['direccion'],
                    pto_venta=PuntoVenta.objects.get(id=int(request.POST['pto_venta'])),
                    user=user,
                    rol=request.POST['rol'],
                )

                my_group = Group.objects.get(name='Normal')
                usuario.user.groups.clear()
                my_group.user_set.add(usuario.user)

                messages.success(request, "Usuario creado con éxito")
                mensaje_alerta = "Usuario creado con éxito"
            except Exception as e:
                messages.error(request, f"No se pudo crear el usuario: {str(e)}")
                mensaje_alerta = f"No se pudo crear el usuario: {str(e)}"
        else:
            mensaje_alerta = "El formulario contiene errores. Revise los datos."

    else:
        form = UsuarioForm()

 # Agrega validación para formulario vacío
    if not request.POST:
        mensaje_alerta = "El formulario está vacío. Ingrese los datos."
        
    context = {
        'titulo': titulo,
        'form': form,
        'mensaje_alerta': mensaje_alerta  # Agrega el mensaje a tu contexto
    }

    return render(request, 'usuarios/usuario-crear.html', context)


""" def usuarios_crear(request):
    titulo = "Usuarios - Crear"
    mensaje_alerta = "" 
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['cedula']): #si está vacío el usuario no se ha creado, se crea con los campos que necesita el auth_user de Django
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['cedula']
                user.first_name= request.POST['nombre']
                user.last_name= request.POST['apellido']
                user.email= request.POST['correo']
                user.password=make_password("@" + request.POST['nombre'][0] + request.POST['apellido'][0] + request.POST['cedula'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['cedula'])

            #crear un usuario y guardar campo por campo en la base de datos
            usuario= Usuario.objects.create(
                codigo_nomina=request.POST['codigo_nomina'],
                cedula=request.POST['cedula'],
                nombre=request.POST['nombre'],
                nombre_dos=request.POST['nombre_dos'],
                apellido=request.POST['apellido'],
                apellido_dos=request.POST['apellido_dos'],
                correo=request.POST['correo'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                pto_venta=PuntoVenta.objects.get(id=int(request.POST['pto_venta'])),
                user=user,
                rol=request.POST['rol'],
            )

            
            my_group= Group.objects.get(name='Normal')
            usuario.user.groups.clear()
            my_group.user_set.add(usuario.user)
    else:
        form = UsuarioForm()

    context = {
        'titulo': titulo,
        'form': form
    }

    return render(request, 'usuarios/usuario-crear.html', context) """
