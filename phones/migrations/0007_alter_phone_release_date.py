# Generated by Django 4.0.3 on 2022-03-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_alter_phone_image_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.TextField(),
        ),
    ]
