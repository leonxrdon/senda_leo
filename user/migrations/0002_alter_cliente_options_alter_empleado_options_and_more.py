# Generated by Django 4.0.4 on 2023-10-26 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='puestoempleado',
            options={'verbose_name_plural': 'Puesto Empleados'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RenameField(
            model_name='puestoempleado',
            old_name='p_emp_description',
            new_name='p_emp_descripcion',
        ),
        migrations.RenameField(
            model_name='puestoempleado',
            old_name='p_emp_name',
            new_name='p_emp_nombre',
        ),
    ]
