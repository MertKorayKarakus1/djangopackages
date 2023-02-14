# Generated by Django 3.2.7 on 2021-09-29 09:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("package", "0008_auto_20210924_2235"),
    ]

    operations = [
        migrations.AddField(
            model_name="version",
            name="licenses",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100, verbose_name="licenses"),
                blank=True,
                help_text="Comma separated list of licenses.",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="license",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="license"
            ),
        ),
    ]
