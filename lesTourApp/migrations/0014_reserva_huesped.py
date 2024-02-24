# Generated by Django 4.2.7 on 2023-11-21 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesTourApp', '0013_reservas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesTourApp.clientes')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesTourApp.reservas')),
            ],
            options={
                'verbose_name_plural': 'Reserva_Huespedes',
            },
        ),
    ]
