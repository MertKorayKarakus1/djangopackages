# Generated by Django 4.0.3 on 2022-03-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("package", "0015_alter_package_deprecates_package"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="pypi_info",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
