# Generated by Django 4.2 on 2023-05-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lesTourApp", "0003_areas_cargo_hoteles_tipo_habitacion_puesto_trabajo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Habitacion",
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
                ("numero", models.IntegerField()),
                ("piso", models.IntegerField()),
                (
                    "id_hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesTourApp.hoteles",
                    ),
                ),
                (
                    "id_tipo_habitacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesTourApp.tipo_habitacion",
                    ),
                ),
            ],
        ),
    ]
