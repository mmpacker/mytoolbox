# Generated by Django 3.2.2 on 2021-05-11 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_toolphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ['name']},
        ),
    ]
