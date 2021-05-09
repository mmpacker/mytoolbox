# Generated by Django 3.2.2 on 2021-05-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_tool'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(to='main_app.Tool'),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.IntegerField(verbose_name='Budget ($ Dollars)'),
        ),
    ]