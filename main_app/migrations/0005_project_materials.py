# Generated by Django 3.2.2 on 2021-05-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='materials',
            field=models.ManyToManyField(to='main_app.Material'),
        ),
    ]