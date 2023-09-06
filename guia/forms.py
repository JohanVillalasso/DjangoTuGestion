from django.forms import ModelForm, widgets
from guia.models import GuiaDespacho


class GuiaForm(ModelForm):
    class Meta:
        model = GuiaDespacho
        exclude = ['estado', 'user']
