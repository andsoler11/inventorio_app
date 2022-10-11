# Generated by Django 4.1.2 on 2022-10-11 00:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                ("cantidad", models.IntegerField()),
                ("precio", models.IntegerField()),
                ("fecha", models.DateField(auto_now_add=True)),
                ("descripcion", models.CharField(max_length=255)),
            ],
        ),
    ]