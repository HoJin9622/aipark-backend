# Generated by Django 4.1.3 on 2022-11-14 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_audio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="project_title",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="project",
            name="project_id",
        ),
    ]