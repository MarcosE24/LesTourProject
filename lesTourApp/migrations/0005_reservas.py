# Generated by Django 4.2 on 2023-05-26 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lesTourApp", "0004_habitacion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_entrada", models.DateTimeField()),
                ("fecha_salida", models.DateTimeField()),
                ("precio", models.IntegerField()),
                ("estado", models.CharField(max_length=50)),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesTourApp.clientes",
                    ),
                ),
                (
                    "id_habitacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesTourApp.habitacion",
                    ),
                ),
            ],
        ),
    ]
