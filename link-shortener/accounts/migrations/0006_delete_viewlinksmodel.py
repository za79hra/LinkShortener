# Generated by Django 4.1.7 on 2023-04-20 11:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_linkshortenermodel_see_url"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ViewLinksModel",
        ),
    ]
