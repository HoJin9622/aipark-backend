# Generated by Django 4.1.3 on 2022-11-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_alter_project_index"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="index",
            field=models.PositiveIntegerField(unique=True, verbose_name="순서"),
        ),
    ]
