# Generated by Django 4.2.1 on 2023-06-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_relationship_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('serial', models.CharField(max_length=50, verbose_name='Serial No')),
                ('siteName', models.CharField(max_length=50, verbose_name='Site ')),
                ('faultDescription', models.TextField(verbose_name='Fault Description')),
                ('technician', models.CharField(max_length=50, verbose_name='Technician')),
            ],
        ),
    ]
