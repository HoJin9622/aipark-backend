# Generated by Django 4.1.3 on 2022-11-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_audio_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="speed",
            field=models.PositiveIntegerField(default=1, verbose_name="오디오의 스피드"),
        ),
    ]