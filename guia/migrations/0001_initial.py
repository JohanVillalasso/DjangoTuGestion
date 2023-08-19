# Generated by Django 4.2.4 on 2023-08-19 23:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '__first__'),
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_guia', models.CharField(choices=[('Producida', 'Producida'), ('Generada', 'Generada'), ('Despachada', 'Despachada'), ('En Bodega Origen', 'En Bodega Origen'), ('En Bodega Destino', 'En Bodega Destino'), ('Anulada', 'Anulada')], default='Generada', max_length=45, verbose_name='Estado de la guía')),
                ('novedad_guia', models.CharField(choices=[('Direccion destino no existe', 'Direccion Destino no existe'), ('Cliente destino no se encontraba', 'Cliente destino no se encontraba'), ('Inconvenientes operativos', 'Inconvenientes Operativos')], default='Inconvenientes operativos', max_length=45, verbose_name='Novedad que presenta la guía')),
            ],
        ),
        migrations.CreateModel(
            name='GuiaDespacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(auto_now=True, verbose_name='Hora captura guía')),
                ('fecha', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha cambio estado guiía')),
                ('destinatario', models.CharField(max_length=60, verbose_name='Datos destino')),
                ('movil_destino', models.CharField(max_length=45, verbose_name='Número destino')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección de destino')),
                ('unidades', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad unidades')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=60, verbose_name='Nombre o tipo de servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Liquidador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_ciudad', models.DecimalField(decimal_places=2, max_digits=15)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado del liquidador')),
                ('fecha_tarifa', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha tarifas')),
                ('cod_CiudDANE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciudadLiquidador', to='ciudades.ciudad')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicioLiquidador', to='guia.servicio', verbose_name='Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='GuiaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guiaServicio', to='guia.guiadespacho', verbose_name='Guia')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServicioGuia', to='guia.servicio', verbose_name='Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='GuiaEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_modificacion', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha cambio estado guia')),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estadoGuia', to='guia.estado', verbose_name='Estado')),
                ('id_guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guiaEstado', to='guia.guiadespacho', verbose_name='Guía')),
            ],
        ),
        migrations.CreateModel(
            name='GuiaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clienteGuia', to='clientes.cliente')),
                ('id_guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guiaCliente', to='guia.guiadespacho', verbose_name='Guia')),
            ],
        ),
        migrations.CreateModel(
            name='DespachoCiudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ciudad', models.CharField(choices=[('Origen', 'Origen'), ('Destino', 'Destino')], default='Origen', max_length=45, verbose_name='Ciudad Origen Destino')),
                ('cod_CiudDANE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CiudadDespacho', to='ciudades.ciudad')),
                ('id_guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guiaDespacho', to='guia.guiadespacho', verbose_name='Guia')),
            ],
        ),
    ]
