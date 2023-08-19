# Generated by Django 4.2.4 on 2023-08-19 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_nomina', models.CharField(max_length=45, verbose_name='Código nómina')),
                ('cedula', models.CharField(max_length=15, verbose_name='Cédula')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('nombre_dos', models.CharField(max_length=60, verbose_name='Segundo nombre')),
                ('apellido', models.CharField(max_length=60, verbose_name='Apellido')),
                ('apellido_dos', models.CharField(max_length=60, verbose_name='Segundo apellido')),
                ('correo', models.CharField(max_length=100, verbose_name='Correo')),
                ('password', models.CharField(max_length=8, verbose_name='Contraseña')),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Empleado', 'Empleado')], default='Empleado', max_length=13, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='PuntoVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('cod_CiudDANE', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CiudadPVenta', to='ciudades.ciudad')),
            ],
        ),
    ]
