# Generated by Django 5.1 on 2025-03-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danisman', '0002_uygunluk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uygunluk',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='uygunluk',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
