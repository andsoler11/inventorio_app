# Generated by Django 4.1.2 on 2022-10-10 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_password"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
