# Generated by Django 5.1 on 2025-03-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danisman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='consultant_images/')),
                ('bio', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
    ]
