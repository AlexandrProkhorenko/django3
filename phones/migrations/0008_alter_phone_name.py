# Generated by Django 4.0.3 on 2022-03-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.SlugField(max_length=500),
        ),
    ]