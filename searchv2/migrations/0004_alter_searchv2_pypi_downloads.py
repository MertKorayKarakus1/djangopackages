# Generated by Django 4.1.3 on 2022-11-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("searchv2", "0003_auto_20180214_0617"),
    ]

    operations = [
        migrations.AlterField(
            model_name="searchv2",
            name="pypi_downloads",
            field=models.IntegerField(default=0, verbose_name="PyPI downloads"),
        ),
    ]
