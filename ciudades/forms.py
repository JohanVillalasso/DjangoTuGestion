from django.forms import ModelForm, widgets
from ciudades.models import Ciudad


class CiudadesForm(ModelForm):
    class Meta:
        model = Ciudad
        exclude = ['estado', 'user']
