# Generated by Django 5.0.6 on 2024-07-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_extrafield'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='share_favorites',
            field=models.BooleanField(default=False, verbose_name='Share Favorites'),
        ),
    ]
