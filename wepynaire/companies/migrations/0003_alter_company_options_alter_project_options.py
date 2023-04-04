# Generated by Django 4.2 on 2023-04-03 17:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0002_project"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name_plural": "companies"},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={
                "permissions": [
                    ("share_project", "can share the project with others"),
                    ("close_project", "can close the project"),
                ]
            },
        ),
    ]
