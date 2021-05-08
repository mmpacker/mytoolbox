# Generated by Django 3.2.2 on 2021-05-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('power', models.CharField(choices=[('N', 'None'), ('B', 'Battery'), ('C', 'Corded')], default='N', max_length=1)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]