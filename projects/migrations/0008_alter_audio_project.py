# Generated by Django 4.1.3 on 2022-11-15 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_alter_audio_speed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="audios",
                to="projects.project",
                verbose_name="프로젝트",
            ),
        ),
    ]
