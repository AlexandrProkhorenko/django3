# Generated by Django 4.0.3 on 2022-03-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_alter_phone_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=500),
        ),
    ]
