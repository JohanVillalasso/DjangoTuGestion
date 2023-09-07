from django.contrib import admin
from django.urls import path, include
from principal.views import logout_user, menu_ppal, rutero, cap_guia, seg_cliente, proy_cumpl, eje_acu, form_gcom
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', include('usuarios.urls')),
    path('ciudades/', include('ciudades.urls')),
    path('guia/', include('guia.urls')),
    path('menu/', menu_ppal, name=('menu-ppal')),
    path('rutero/', rutero, name='rutero'),
    path('cap-guia/', cap_guia, name=('cap-guia')),
    path('seg-cliente/', seg_cliente, name=('seg-cliente')),
    path('proy-cumpl/', proy_cumpl, name=('proy-cumpl')),
    path('eje-acu/', eje_acu, name=('eje-acu')),
    path('form-gcom/', form_gcom, name=('form-gcom')),

    path('', auth_views.LoginView.as_view(), name='inicio'),
    path('logout/', logout_user, name="logout"),

]
