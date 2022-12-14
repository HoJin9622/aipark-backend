# Generated by Django 4.1.3 on 2022-11-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
                ("index", models.PositiveIntegerField(verbose_name="순서")),
                ("project_id", models.PositiveIntegerField(verbose_name="프로젝트 ID")),
                (
                    "project_title",
                    models.CharField(max_length=80, verbose_name="프로젝트명"),
                ),
            ],
            options={
                "verbose_name": "프로젝트",
                "verbose_name_plural": "프로젝트",
            },
        ),
    ]
